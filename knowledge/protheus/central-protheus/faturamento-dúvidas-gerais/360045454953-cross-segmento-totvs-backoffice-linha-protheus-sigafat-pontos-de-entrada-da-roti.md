---
article_id: 360045454953
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fb358a7b20b4cbe5841586859170c45fcfe07d6b89abdca9f671bd2dabc3005a
fetched_at: '2026-06-28T22:38:28.635544+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Pontos de entrada
  da rotina MATA521
type: support-article
updated_at: '2021-06-02T18:17:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045454953-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-da-rotina-MATA521
---

**Dúvida**Quais os pontos de entrada da rotina da Exclusão de Documentos de Saída (**MATA521**)?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 11.80.  
  
**Solução**

Estes são os pontos existentes na rotina de Exclusão de Documentos de Saída:

**- MS520VLD -** Validar ou não a exclusão da nota: <https://tdn.totvs.com/x/OIVn>

- **MSD2520 -** Antes da exclusão do registro no SD2: <https://tdn.totvs.com/x/OoVn>

**- MS520NCA -** Localizado na função A520Dele(), será executado se o campo E1\_ORIGEM for igual a "MATA460": <https://tdn.totvs.com/x/N4Vn>

**- MS520DEL -** Executado antes da exclusão do registro da tabela SF2: <https://tdn.totvs.com/x/NoVn>

- **M521DNFS -** Lançamentos contábeis: <https://tdn.totvs.com/x/-4Vn>

**- M521CDEL -** Verificação de amarração de fatura à solicitação: <https://tdn.totvs.com/x/-oVn>

**- M521CART -** Exclusão de item da NF: <https://tdn.totvs.com/x/9IRn>

- **M520SF3 -** Exclusão de registro do SF3 (**somente Argentina**): <https://tdn.totvs.com/x/84Rn>

**- M520QRY -** Inclusão de elementos na query: <https://tdn.totvs.com/x/HoZn>

- **M520EXC -** Exibição de help (**somente Argentina**): <https://tdn.totvs.com/x/8oRn>

**- M520BROW -** Exibição de dados no browse: <https://tdn.totvs.com/x/8YRn>

**- SF2520E -** Estorno do Documento de Saída **(somente TMS)**: <https://tdn.totvs.com/x/L-lc>

**- MA520SE1 -** Vinculo condição de pagamento com condição de venda: <https://tdn.totvs.com/x/-YVn>

**- M521TRAN -** Valida a transmissão de cancelamento de Nota Fiscal de Saída: <https://tdn.totvs.com/x/Loj0G>
