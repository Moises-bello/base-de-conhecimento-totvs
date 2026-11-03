---
article_id: 360045401793
category: ADVPL - Web Service
content_hash: 5f944d1bf4b6a7c489ad896c284c01318a544228b1e8e0a767bc2fac6da28fba
fetched_at: '2026-06-28T22:40:10.208535+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Configuração básica
  REST do protheus
type: support-article
updated_at: '2022-01-05T19:08:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045401793-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Configura%C3%A7%C3%A3o-b%C3%A1sica-REST-do-protheus
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Qual a configuração básica para subir o serviço ***REST*** no **PROTHEUS**?  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12  
  
**Solução**

Para configurar o serviço ***REST*** em nosso ambiente, precisamos das seguintes chaves(ini):

* **HTTPJOB**Rotina que inicializa o servidor REST;  
  Configura qual ambiente do Protheus será acessado.
* **HTTPREST**Configura um socket que o servidor utilizará para comunicação;  
  Possibilita agrupar URI para atender diferentes ambientes;  
  Configura se o Rest Server solicitará autenticação de usuários.
* **HTTPV11**Habilita o uso do Rest server;  
  Agrupa a configuração dos Sockets de comunicação.
* **HTTPURI**Controla URL base onde os serviços serão disponibilizados;  
  Possui Informações para preparação do ambiente das *working* *threads;*Controla quantidade de threads que ficarão disponíveis para responder às requisições.

```
[GENERAL]
MAXSTRINGSIZE=10
 
[HTTPV11]
Enable=1
Sockets=HTTPREST

[HTTPREST]
Port=8080
URIs=HTTPURI
SECURITY=1

[HTTPURI]
URL=/rest
PrepareIn=All
Instances=1,2

[ONSTART]
jobs=HTTPJOB
RefreshRate=30

[HTTPJOB]
MAIN=HTTP_START
ENVIRONMENT=environment
```

Se tudo estiver configurado corretamente, ira apresentar no console conforme abaixo**:**

**![Screenshot_16.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360062756473/Screenshot_16.jpg)**

Ao acessar o navegador com o endereço **<http://localhost:8080/rest> ,**deverá ser exibida uma lista de API’s disponíveis.

```
Definição da URL  
http://{IP do servidor}:(port}/{path}
```

![Imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360088588553/Imagem1.png)

Essa pagina mostra a lista de classes ***WSRESTFUL*** compiladas no RPO do ambiente configurado. Ao clicar nos detalhes de cada classe são exibidos os métodos disponíveis.  
  
**Importante:**O *web service* ***REST***do AdvPL **não** utiliza as seções **HTTP** e ***WebServices***utilizadas para o configurar o modelo ***SOAP***.  
Apesar disso o ***REST*** também utiliza *working threads* para atender as requisições recebidas também pelo protocolo **HTTP**.  
O protocoloco **HTTP** do ***REST*****não** atende a outros tipos de requisições como o **HTTP** do **SOAP** (que também atende arquivos estáticos, **APW** e **APL**).  
  
**Saiba mais** [Configuração Web Services REST/Server](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)
