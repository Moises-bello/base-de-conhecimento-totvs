---
content_hash: 46360d0ad15b8e97ed60bec867fa857eb9620b42e2666a2612beec9f39c57378
fetched_at: '2026-06-29T00:10:37.297853+00:00'
page_id: '539529049'
product: rm
source: tdn-rm
title: SSL/TLS nas APIs
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539529049
version: 1
---

Para que a comunicação com os serviços HTTP seja **protegida** com **SSL/TLS** através de certificado digital, é necessário configurar o ambiente do host de acordo com o TDN: [Habilitar SSL/TLS no Host](https://tdn.totvs.com/pages/viewpage.action?pageId=244911449).

Para proteger apenas os serviços HTTP, ou seja, os Web Services e serviços REST expostos pelo HOST, é necessário habilitar o parâmetro abaixo no arquivo de configuração do HOST (RM.Host.Service.exe.config):

<add key="EnableWSSecurity" value="true" />. As demais configurações podem ser consultadas no link acima.
