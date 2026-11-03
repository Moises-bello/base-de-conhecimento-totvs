---
article_id: 360057155873
category: Materiais - Compras (SIGACOM)
content_hash: ac1ca778ebd54a44b842516b7b53abcd5e3e7f2d86090040eac6af7164ad1521
fetched_at: '2026-06-28T22:41:07.390071+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM -  Ponto de Entrada
  COMCOLF4: Altera o campo DT_TES'
type: support-article
updated_at: '2024-06-13T11:46:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057155873-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ponto-de-Entrada-COMCOLF4-Altera-o-campo-DT-TES
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24132303144599)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**

O ponto de entrada COMCOLF4 não está alterando o campo DT\_TES, conforme configuração.

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) – COMPRAS – A partir da versão 12.1.17

**Solução**

Na importação do documento XML para o monitor do Importador Xm, o campo DT\_TES não é gravado automaticamente, sendo necessário inserir essa informação manualmente. No entanto, ao realizar o processo de "Gerar documento" no Monitor, é acionado o Ponto de Entrada para alterar a TES e gerar o documento, utilizando o campo D1\_TESACLA ou D1\_TES, conforme explicado no documento.

***Saiba Mais:***[Totvs Colaboração - Regras TES / Condição de pagamento](https://tdn.totvs.com/pages/viewpage.action?pageId=546695574)  
[Ponto de Entrada COMCOLF4 permite alterar a TES](https://tdn.totvs.com/pages/releaseview.action?pageId=51250499)[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML?source=search)
