#!/bin/bash

curl -s https://raw.githubusercontent.com/safchain/asyncio-ari/master/ari.json |

# add global parameter definition
jq '. += {
  "parameters": { 
    "asteriskID": {
      "in": "header",
      "name": "X-Asterisk-ID",
      "type": "string",
      "required": false,
      "description": "Asterisk ID used to route the request through the API Gateway"
    }
  }
}' ari.json |

# add ref to all resources
jq '.paths[] += {
  "parameters": [
    {
      "$ref": "#/parameters/asteriskID"
    }
  ]
}' > ari-ast-id.json

docker run --rm -v ${PWD}:/local swaggerapi/swagger-codegen-cli generate -i /local/ari-ast-id.json  -l python --library asyncio -o /local/out/python --git-user-id "safchain" --git-repo-id "asyncio-ari-ast-id"
