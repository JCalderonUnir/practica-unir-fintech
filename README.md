# practica Unir Fintech

## 📘 Traducción de texto

### Endpoint


### Request
**Headers**


**Body**
```json
{
  "text": "Hola mundo",
  "target_language": "en",
  "source_language": "auto"
}

**Endpoint**
http://<server-host>:<port>/translate

**CURL Example**

```curl
curl -X POST "http://localhost:8000/translate" \
-H "Content-Type: application/json" \
-d '{
  "text": "Hola mundo",
  "target_language": "en"
}'

**CURL Response**

```json
{
    "original_text": "Hola mundo",
    "translated_text": "Hello world",
    "source_language": "auto",
    "target_language": "en"
}

