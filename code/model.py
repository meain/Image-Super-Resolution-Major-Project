def create_model(self, height=32, width=32, channels=3,
                    load_weights=False, batch_size=128):
    """
        Creates a model to be used to scale images
         of specific height and width.
    """
    init = super(ImageSuperResolutionModel, self)
            .create_model(height, width, channels,
                             load_weights, batch_size)

    x = Convolution2D( 
        self.n1, (self.f1, self.f1), 
        activation='relu', padding='same', name='level1')(init)
    x = Convolution2D(
        self.n2, (self.f2, self.f2),
         activation='relu', padding='same', name='level2')(x)

    out = Convolution2D(
        channels, (self.f3, self.f3),
         padding='same', name='output')(x)

    model = Model(init, out)

    adam = optimizers.Adam(lr=1e-3)
    model.compile(
        optimizer=adam, loss='mse', metrics=[PSNRLoss])
    if load_weights: model.load_weights(self.weight_path)

    self.model = model
    return model