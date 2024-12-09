# Define the architecture of the autoencoder with increased complexity
input_dim = len(nir_spectra[0])  # Assuming `nir_spectra` contains your input data
encoding_dim = 128  # Increased encoding dimension

# Encoder
encoder_input = layers.Input(shape=(input_dim,))
encoded = layers.Dense(256, activation="relu")(encoder_input)
encoded = layers.Dense(encoding_dim, activation="relu")(encoded)

# Decoder
decoded = layers.Dense(256, activation="relu")(encoded)
decoded = layers.Dense(input_dim, activation="sigmoid")(decoded)

# Autoencoder model
autoencoder = models.Model(encoder_input, decoded)

# Compile the model
autoencoder.compile(optimizer="adam", loss="mse")

# Train the autoencoder with increased complexity
autoencoder.fit(
    nir_spectra_train,
    nir_spectra_train,
    epochs=100,
    batch_size=64,
    validation_data=(nir_spectra_val, nir_spectra_val),
)

# Evaluate the model
loss = autoencoder.evaluate(nir_spectra_test, nir_spectra_test)
print("Test Loss:", loss)

# Use the encoder for dimensionality reduction
encoder_model = models.Model(encoder_input, encoded)
encoded_nir_spectra = encoder_model.predict(nir_spectra)
