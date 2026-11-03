---
content_hash: e813fdb724d23023d568b3d436ab54572ff54a14e4ff2344ea775cf464e6d4de
fetched_at: '2026-07-02T19:24:26.616249+00:00'
page_id: '521650725'
product: protheus
source: tdn-tec
title: Uso do broker HTTP em conexões encriptadas (SSL) abertas pelo client
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=521650725
version: 16
---

O Broker HTTP pode ser usado para receber conexões encriptadas (SSL) vindas do client (ex: SmartClient WebApp), e abrir conexões encriptadas (SSL) com o server (ex: AppServer).  
  
É importante ter em mente que não é possível garantir o funcionamento do Broker com toda e qualquer aplicação web que use conexões encriptadas, por causa da enorme variedade de técnicas que podem ser utilizadas para escrever aplicações web.  
  
Em outras palavras, antes de fazer o deployment de uma solução web neste cenário, **a solução deve ser validada em processo de homologação**, com o Broker configurado para aceitar conexões SSL.  
  
Um outro ponto a considerar é que a solução precisa ser validada com browsers específicos (p. ex: Chrome e Firefox) devido ao fato de que diferentes browsers apresentam diferentes comportamentos, dependendo dos recursos utilizados ao escrever a aplicação web.

A configuração do Broker para receber conexões encriptadas (SSL) necessita das seguintes chaves no arquivo de configuração appserver.ini:

```
...
...
SSL_METHOD=SSL/TLS
SSL_CERTIFICATE=<nome do arquivo que contem o certificado>
SSL_KEY=<nome do arquivo que contem a chave a chave privada>
SSL_PASSPHRASE=<senha de proteção da chave privada>  
...  
...
```
