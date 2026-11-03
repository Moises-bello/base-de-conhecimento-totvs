---
article_id: 360053138694
category: ADVPL - Web Service
content_hash: 81078d25d3f35d7919e1b8313b802728b79d7f691b96b2601813b77dc297f605
fetched_at: '2026-06-28T22:40:10.163189+00:00'
product: protheus
section_id: 1500001567342
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - API Relação de
  Funcionários - Global:Acessar
type: support-article
updated_at: '2024-03-20T17:37:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053138694-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-API-Rela%C3%A7%C3%A3o-de-Funcion%C3%A1rios-Global-Acessar
---

**Dúvida**API Relação de Funcionários - Global não está disponível na lista de serviços de **API** (TOTVS - RESTFul API) 

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão p12

**Solução**Para cessar a **API** Funcionários do Protheus, serviço ***employeedatacontent***.  
-Configurar e subir o serviço **Rest**. Conforme documentação. **Configuração REST**  
-Acessar a lista de serviço **API** e verificar a existência do ***employeedatacontent***  
-Para testara a **API** terá que consumir, neste teste usamos a ferramenta **PostMan**  
-Informar a **URL**(IP) DO SERVIDOR + **Porta do Serviço** REST+ **URI**do serviço  REST + Recurso  a ser consumido + Parâmetros da API

**Exemplo**

http://localhost:8106/rest99/rh/v1/employeedatacontent/

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22209319639447)

**Saiba mais**  
[API reference TOTVS](https://api.totvs.com.br/referencelist)  
[Configuração REST](https://tdn.totvs.com/pages/viewpage.action?pageId=185747842)
