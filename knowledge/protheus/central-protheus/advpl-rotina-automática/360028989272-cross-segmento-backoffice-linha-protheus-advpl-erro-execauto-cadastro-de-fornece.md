---
article_id: 360028989272
category: ADVPL - Rotina Automática
content_hash: d4ddcaaa281cbad2733e190b27a6120e02282753b18bcb12faeb37c873b61e8a
fetched_at: '2026-06-28T22:40:23.991907+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Erro Execauto Cadastro
  de Fornecedores (MATA020)
type: support-article
updated_at: '2026-02-26T14:31:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028989272-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Erro-Execauto-Cadastro-de-Fornecedores-MATA020
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**

Estou com erro na Execauto MATA020 (MVC) e gera o erro abaixo.

Cod. Municip - A2\_COD\_MUN := 04557 < -- Invalido   
  
**Ambiente**Protheus – ADVPL – A partir da versão 12.1.23

**Solução**

Neste caso é necessário verificar a ordenação dos campos, pois campo referente ao Estado deve ser preenchido antes do Código do Município

Segue exemplo de rotina automática Mata020

**[Cadastro Fornecedor (Rotina automática - MATA020)](http://tdn.totvs.com/pages/viewpage.action?pageId=463824753)**
