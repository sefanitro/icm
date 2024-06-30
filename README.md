
## Requirements
- docker
- docker-compose

## Run

docker-compose up

## Usage

```bash
curl --location 'localhost:8000/api/icm/' \
--header 'Content-Type: application/json' \
--data '{
    "stacks": [10000, 100, 100, 100],
    "payouts": [50,30,20]
}'
```

Response is a list of winning chance of each user
```json
{
    "chance": [
        49.4159,
        16.8336,
        16.8487,
        16.9018
    ]
}
```