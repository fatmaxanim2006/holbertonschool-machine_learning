# Attention

This project implements the Encoder-Decoder architecture with Attention
for machine translation, built with TensorFlow/Keras.

## Files

### 0-rnn_encoder.py
Contains the class `RNNEncoder` that inherits from
`tensorflow.keras.layers.Layer` to encode for machine translation.

**Class constructor** `def __init__(self, vocab, embedding, units, batch):`
- `vocab` is an integer representing the size of the input vocabulary
- `embedding` is an integer representing the dimensionality of the
  embedding vector
- `units` is an integer representing the number of hidden units in the
  RNN cell
- `batch` is an integer representing the batch size

Sets the following public instance attributes:
- `batch` - the batch size
- `units` - the number of hidden units in the RNN cell
- `embedding` - a keras Embedding layer that converts words from the
  vocabulary into an embedding vector
- `gru` - a keras GRU layer with `units` units
  - Returns both the full sequence of outputs as well as the last
    hidden state
  - Recurrent weights are initialized with `glorot_uniform`

**Public instance method** `def initialize_hidden_state(self):`
- Initializes the hidden states for the RNN cell to a tensor of zeros
- Returns: a tensor of shape `(batch, units)` containing the initialized
  hidden states

**Public instance method** `def call(self, x, initial):`
- `x` is a tensor of shape `(batch, input_seq_len)` containing the input
  to the encoder layer as word indices within the vocabulary
- `initial` is a tensor of shape `(batch, units)` containing the initial
  hidden state
- Returns: `outputs, hidden`
  - `outputs` is a tensor of shape `(batch, input_seq_len, units)`
    containing the outputs of the encoder
  - `hidden` is a tensor of shape `(batch, units)` containing the last
    hidden state of the encoder

## Requirements
- Python 3.6+
- TensorFlow

## Usage
```python
RNNEncoder = __import__('0-rnn_encoder').RNNEncoder

encoder = RNNEncoder(1024, 128, 256, 32)
print(encoder.batch)
print(encoder.units)
print(type(encoder.embedding))
print(type(encoder.gru))

initial = encoder.initialize_hidden_state()
print(initial)
```

### 1-self_attention.py
Contains the class `SelfAttention` that inherits from
`tensorflow.keras.layers.Layer` to calculate the attention for machine
translation, based on the Bahdanau attention paper.

**Class constructor** `def __init__(self, units):`
- `units` is an integer representing the number of hidden units in the
  alignment model

Sets the following public instance attributes:
- `W` - a Dense layer with `units` units, applied to the previous
  decoder hidden state
- `U` - a Dense layer with `units` units, applied to the encoder
  hidden states
- `V` - a Dense layer with 1 unit, applied to the tanh of the sum of
  the outputs of `W` and `U`

**Public instance method** `def call(self, s_prev, hidden_states):`
- `s_prev` is a tensor of shape `(batch, units)` containing the
  previous decoder hidden state
- `hidden_states` is a tensor of shape `(batch, input_seq_len, units)`
  containing the outputs of the encoder
- Returns: `context, weights`
  - `context` is a tensor of shape `(batch, units)` that contains the
    context vector for the decoder
  - `weights` is a tensor of shape `(batch, input_seq_len, 1)` that
    contains the attention weights

### 2-rnn_decoder.py
Contains the class `RNNDecoder` that inherits from
`tensorflow.keras.layers.Layer` to decode for machine translation.

**Class constructor** `def __init__(self, vocab, embedding, units, batch):`
- `vocab` is an integer representing the size of the output vocabulary
- `embedding` is an integer representing the dimensionality of the
  embedding vector
- `units` is an integer representing the number of hidden units in the
  RNN cell
- `batch` is an integer representing the batch size

Sets the following public instance attributes:
- `embedding` - a keras Embedding layer that converts words from the
  vocabulary into an embedding vector
- `gru` - a keras GRU layer with `units` units
  - Returns both the full sequence of outputs as well as the last
    hidden state
  - Recurrent weights are initialized with `glorot_uniform`
- `F` - a Dense layer with `vocab` units

**Public instance method**
`def call(self, x, s_prev, hidden_states):`
- `x` is a tensor of shape `(batch, 1)` containing the previous word in
  the target sequence as an index of the target vocabulary
- `s_prev` is a tensor of shape `(batch, units)` containing the
  previous decoder hidden state
- `hidden_states` is a tensor of shape `(batch, input_seq_len, units)`
  containing the outputs of the encoder
- Uses `SelfAttention` from `1-self_attention.py`
- Concatenates the context vector with `x` in that order
- Returns: `y, s`
  - `y` is a tensor of shape `(batch, vocab)` containing the output
    word as a one hot vector in the target vocabulary
  - `s` is a tensor of shape `(batch, units)` containing the new
    decoder hidden state

### 4-positional_encoding.py
Contains the function `positional_encoding(max_seq_len, dm)` that
calculates the positional encoding for a transformer.

- `max_seq_len` is an integer representing the maximum sequence length
- `dm` is the model depth
- Returns: a `numpy.ndarray` of shape `(max_seq_len, dm)` containing
  the positional encoding vectors

### 5-sdp_attention.py
Contains the function `sdp_attention(Q, K, V, mask=None)` that
calculates the scaled dot product attention.

- `Q` is a tensor with its last two dimensions as
  `(..., seq_len_q, dk)` containing the query matrix
- `K` is a tensor with its last two dimensions as
  `(..., seq_len_v, dk)` containing the key matrix
- `V` is a tensor with its last two dimensions as
  `(..., seq_len_v, dv)` containing the value matrix
- `mask` is a tensor that can be broadcast into
  `(..., seq_len_q, seq_len_v)` containing the optional mask, or
  defaulted to `None`
  - if `mask` is not `None`, `-1e9` is multiplied to the mask and
    added to the scaled matrix multiplication
- The preceding dimensions of `Q`, `K`, and `V` are the same
- Returns: `output, weights`
  - `output` a tensor with its last two dimensions as
    `(..., seq_len_q, dv)` containing the scaled dot product attention
  - `weights` a tensor with its last two dimensions as
    `(..., seq_len_q, seq_len_v)` containing the attention weights

### 6-multihead_attention.py
Contains the class `MultiHeadAttention` that inherits from
`tensorflow.keras.layers.Layer` to perform multi head attention.

**Class constructor** `def __init__(self, dm, h):`
- `dm` is an integer representing the dimensionality of the model
- `h` is an integer representing the number of heads
  - `dm` is divisible by `h`

Sets the following public instance attributes:
- `h` - the number of heads
- `dm` - the dimensionality of the model
- `depth` - the depth of each attention head
- `Wq` - a Dense layer with `dm` units, used to generate the query
  matrix
- `Wk` - a Dense layer with `dm` units, used to generate the key
  matrix
- `Wv` - a Dense layer with `dm` units, used to generate the value
  matrix
- `linear` - a Dense layer with `dm` units, used to generate the
  attention output

**Public instance method** `def call(self, Q, K, V, mask):`
- `Q` is a tensor of shape `(batch, seq_len_q, dk)` containing the
  input to generate the query matrix
- `K` is a tensor of shape `(batch, seq_len_v, dk)` containing the
  input to generate the key matrix
- `V` is a tensor of shape `(batch, seq_len_v, dv)` containing the
  input to generate the value matrix
- `mask` is always `None`
- Uses `sdp_attention` from `5-sdp_attention.py`
- Returns: `output, weights`
  - `output` a tensor with its last two dimensions as
    `(..., seq_len_q, dm)` containing the scaled dot product attention
  - `weights` a tensor with its last three dimensions as
    `(..., h, seq_len_q, seq_len_v)` containing the attention weights
