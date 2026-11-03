---
article_id: 21013207544983
category: Financeiro - Contas a Receber
content_hash: a152a72e43c1906720320a34efff9ef856619f1a67035113dcc03c9741ff575e
fetched_at: '2026-06-28T22:38:14.076084+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA440 - Legendas
  referente ao campo E3_ORIGEM
type: support-article
updated_at: '2024-01-31T19:18:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21013207544983-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA440-Legendas-referente-ao-campo-E3-ORIGEM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21013207530135) Tempo aproximado para leitura: **00:04:00 min****Dúvida**Existem legendas referente ao campo E3\_ORIGEM? Quais são essas origens e a suas rotinas  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus -  Financeiro - Todas as versões  
  
**Solução**

O campo **E3\_ORIGEM** (Tabela **SE3 - comissões de venda**), possui apenas um carácter, que indica as rotina que foram originadas para o registro.

Os caracteres possíveis para utilização, serão descritos abaixo:

"E" - **Emissão Financeiro**

Rotina de Origem -> "**FINA040 ou FINA280**"

"B" - **Baixa Financeiro**

Rotina de Origem -> "**FINA070, FINA330, FINA110 ou FINA087A**"

"F" - Faturamento

Rotina de Origem -> "**MATA460, MATA520, MATA467N, MATA465N ou MATA468N**"

"D" - Devolução de Venda

Rotina de Origem ->"**MATA100**"

"R" - **Recálculo quando não há origem**

Rotina de Origem -> "**FINA440**"

"L" - SigaLoja

Rotina de Origem-> "**LOJA440**"

**Importante**  
Será gravado "L" somente se a comissão foi gerada pela rotina **LOJA440** de forma Off-Line.

"I" - Integração Mensagem única

Rotina de Origem-> "**MATI940**"
