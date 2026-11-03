---
article_id: 36504007950487
category: Financeiro - Contas a Receber
content_hash: d069289dadc5765f488ca0dec41c9bf019eb211f2ec3ea34f9c6a1c80ecede24
fetched_at: '2026-06-28T22:38:12.472042+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA087A - Não é possível efetuar
  a baixa dos títulos
type: support-article
updated_at: '2025-11-24T11:36:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36504007950487-Cross-Segmento-Backoffice-Linha-Protheus-FINA087A-N%C3%A3o-%C3%A9-poss%C3%ADvel-efetuar-a-baixa-dos-t%C3%ADtulos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36504007930391) Tempo aproximado para leitura: 00:05 min  
  
**Dúvida**  
Problema: não é possível efetuar a baixa dos títulos porque não existe uma Administradora Financeira de Cartão de Crédito/Débito cadastrada.  
  
  
**Solução**  
Para o correto funcionamento da rotina de**Recebimento Diversos (FINA087A)**, é necessário que o código da administradora financeira esteja devidamente cadastrado nas tabelas **SAE (Administradoras Financeiras)** e **SA1 (Clientes)**.  
  
**Não deve ser utilizado os campos de cliente (AE\_CODCLI) e loja (AE\_LOJCLI) do cadastro das administradoras que serão utilizadas nesta rotina de recebimentos diversos.**

**Saiba mais**

[Recebimentos Diversos (FINA087A - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312167649)
