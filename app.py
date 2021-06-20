from init_app import create_app, create_blueprint

app = create_app()
create_blueprint(app=app)


if __name__ == '__main__':
    app.run()
