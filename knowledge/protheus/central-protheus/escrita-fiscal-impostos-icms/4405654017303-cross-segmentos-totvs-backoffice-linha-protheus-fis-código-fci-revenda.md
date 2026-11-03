---
article_id: 4405654017303
category: Escrita Fiscal - Impostos - ICMS
content_hash: 09b8c608578fe9c3fae53e82027e0789dbd427c5647e3741a812422b3fb15f10
fetched_at: '2026-06-28T22:39:24.374404+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Código FCI - Revenda
type: support-article
updated_at: '2021-08-04T19:54:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405654017303-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%B3digo-FCI-Revenda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como gerar código FCI na Revenda?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

**1) Empresa com controle de Lote:**

Validar parâmetros:

MV\_RASTRO = S

MV\_LOTEUNI = .T.

MV\_FCIATUC = .T.

MV\_FISAUCF = .T.

MV\_FISFRAS = .T.

MV\_ORILOTE = .T.

**Cadastro do produto:**

Rastro = Lotes

**TES:**  
Atualiza Estoque = Sim  
Calcula ICMS = Sim  
l. Fiscal ICMS = Tributado

Lançar documento de entrada:

Preencher manualmente D1\_FCICOD

Ao fazer pedido de Venda, amarrar o Lote

Ao Faturar a nota fiscal, na tabela SD2, o campo: D2\_FCICOD = Deve ser preenchido

**2) Empresa sem controle de Lote:**

Preencher manualmente na entrada: D1\_FCICOD e na saída: C6\_FCICOD
