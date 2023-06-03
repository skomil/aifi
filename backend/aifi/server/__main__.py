#!/usr/bin/env python3

import connexion

from aifi.api import encoder


def main():
    app = connexion.App(__name__, specification_dir='../api/openapi/',
                        options={"swagger_ui": True} )
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'aifi - OpenAPI 3.0'},
                resolver=connexion.resolver.RelativeResolver('aifi.server.controllers.default_controller'),
                pythonic_params=True)

    app.run(port=5000)


if __name__ == '__main__':
    main()
