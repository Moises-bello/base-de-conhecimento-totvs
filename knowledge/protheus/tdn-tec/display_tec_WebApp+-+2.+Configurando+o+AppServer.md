---
content_hash: bd0e99692b6d45f76f2a7def0e813d2953d227af2e0018b97e7905a21c590011
fetched_at: '2026-07-02T19:24:24.826526+00:00'
page_id: '490316955'
product: protheus
source: tdn-tec
title: WebApp - 2. Configurando o AppServer
type: documentation
url: https://tdn.totvs.com/display/tec/WebApp+-+2.+Configurando+o+AppServer
version: 10
---

Para realizar o utilização do e-CPF através do Webapp, será necessário preparar seu AppServer através da configuração do arquivo **appserver.ini.**

As chaves necessárias a serem configuradas estão listadas abaixo; caso haja dúvida em como configurar uma determinada chave, clique em seu nome para ver sua documentação:

Atenção

Certifique-se que a configuração SSL foi efetivada, e testada, observando o cabeçalho do browser utilizado; caso a mensagem de "Não seguro" seja apresentada, realize novamente as configurações descritas em .

| Incorreto | Correto |
| --- | --- |
|  |  |

Para configuração específica do e-CPF, utilize as chaves abaixo:

[Seção [Webapp] - SSLCACertificate](https://tdn.totvs.com/pages/viewpage.action?pageId=417699656)

| Exemplo |
| --- |
| `[WEBAPP]` `Port=8080` `SSLMethod=SSL/TLS` `SSLCertificate=C:\TOTVS\certificate.pem` `SSLKey=C:\TOTVS\key.pem` `SSLClientAuth=required` `SSLCACertificate=C:\TOTVS\ca-chain.pem` |

Próximo passo:
