import connexion
from gen_api import encoder


def main():
    app = connexion.App(__name__, specification_dir='./gen_api/openapi/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Rig and Rack API'},
                pythonic_params=True)

    app.run(port=8080)


if __name__ == '__main__':
    main()