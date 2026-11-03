---
content_hash: 77c6766cd282d8163f35542a4dc0d9f7a5403ba992e8114a57033537cf1197d5
fetched_at: '2026-06-29T00:12:08.007722+00:00'
page_id: '927561043'
product: rm
source: tdn-rm
title: Envio de imagens para o Meu eduCONNECT
type: documentation
url: https://tdn.totvs.com/display/LRM/Envio+de+imagens+para+o+Meu+eduCONNECT
version: 4
---

As mensagens enviadas pela "Central de Comunicação" para o Meu eduCONNECT possuem um limite de **4000 caracteres**, o que pode restringir o envio de imagens no corpo da mensagem. Para garantir o correto funcionamento, as imagens devem ser enviadas **exclusivamente no Modo Avançado (HTML)**, seguindo as recomendações abaixo:

### ❌ Método não recomendado

A imagem é incorporada no conteúdo da mensagem em formato **Base64**, aumentando significativamente o tamanho do texto e podendo impedir o envio.

xml]]>

### ✅ Método recomendado

Utilize uma URL externa para carregar a imagem, evitando o consumo excessivo de caracteres.

xml]]>

```

```
