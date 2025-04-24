# API

## V1

Types:

```python
from agent_toolkit.types.api import V1GetCreditsResponse, V1SearchResponse
```

Methods:

- <code title="get /api/v1/credits">client.api.v1.<a href="./src/agent_toolkit/resources/api/v1/v1.py">get_credits</a>() -> <a href="./src/agent_toolkit/types/api/v1_get_credits_response.py">V1GetCreditsResponse</a></code>
- <code title="get /api/v1/search">client.api.v1.<a href="./src/agent_toolkit/resources/api/v1/v1.py">search</a>(\*\*<a href="src/agent_toolkit/types/api/v1_search_params.py">params</a>) -> <a href="./src/agent_toolkit/types/api/v1_search_response.py">V1SearchResponse</a></code>

### Extract

Types:

```python
from agent_toolkit.types.api.v1 import ExtractResponse
```

Methods:

- <code title="post /api/v1/extract">client.api.v1.extract.<a href="./src/agent_toolkit/resources/api/v1/extract.py">create</a>(\*\*<a href="src/agent_toolkit/types/api/v1/extract_create_params.py">params</a>) -> <a href="./src/agent_toolkit/types/api/v1/extract_response.py">ExtractResponse</a></code>
- <code title="get /api/v1/extract">client.api.v1.extract.<a href="./src/agent_toolkit/resources/api/v1/extract.py">retrieve</a>(\*\*<a href="src/agent_toolkit/types/api/v1/extract_retrieve_params.py">params</a>) -> <a href="./src/agent_toolkit/types/api/v1/extract_response.py">ExtractResponse</a></code>
