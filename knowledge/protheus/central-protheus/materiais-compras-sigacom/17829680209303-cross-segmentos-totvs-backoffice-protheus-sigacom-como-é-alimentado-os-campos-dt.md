---
article_id: 17829680209303
category: Materiais - Compras (SIGACOM)
content_hash: d4d55ca511f616113aa79ef5a5922f53357b2667606229825c6359b574b61f53
fetched_at: '2026-06-28T22:41:15.765821+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é alimentado os
  campos DT_LOTE e DT_DTVALID pelo Importador XML?
type: support-article
updated_at: '2025-11-10T14:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17829680209303-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-alimentado-os-campos-DT-LOTE-e-DT-DTVALID-pelo-Importador-XML
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17829665553943) Tempo aproximado para leitura: **00:02min****Dúvida**Como é alimentado os campos DT\_LOTE e DT\_DTVALID pelo Importador XML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Versão 12  
  
**Solução**

O importador preenche exatamente conforme consta no XML.

**Exemplo:**

Se o XML contiver as tags <nLote> e <dVal>, elas serão gravadas nos respectivos campos DT\_LOTE e DT\_DTVALID.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24036413950999)

O sistema executará um `execauto`, como se estivesse digitando manualmente nos campos de Lote e Validade do Fornecedor.

Para que as informações do Lote sejam levadas para o documento de entrada, é obrigatório que o parâmetro **MV\_RASTRO** esteja como **S** e o campo **B1\_RASTRO** deve estar preenchido com **S** (sublote) ou **L** (lote).

As informações do lote serão preenchidas nos campos D1\_LOTECTL (código do lote) D1\_DTVALID (data de validade) e D1\_DFABRIC (data de fabricação)

Se o parâmetro estiver desativado ou se o campo B1\_RASTRO estiver como N, as informações do lote não serão levadas para o documento de entrada. E os campos de lote da tabela SD1 ficarão em branco.

***Saiba Mais:***

* [Importador XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026658994-MP-SIGACOM-Importador-XML#:~:text=No%20Importador%20de%20XML%20%C3%A9%20necess%C3%A1rio%20criar%20agendamentos,op%C3%A7%C3%B5es%20do%20menu%20Ambiente%20-%3E%20Schedule%20-%3E%20Schedule%3A)
* [Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](http://xn--cross%20segmento%20-%20backoffice%20(linha%20protheus)%20-%20sigacom%20-%20integrao%20importador%20xml%20x%20totvs%20transmite-ulk18b/)
* [Agendamento (Schedule) - Importador XML](https://tdn.totvs.com/display/public/PROT/Agendamento+%28Schedule%29+-+Importador+XML)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
