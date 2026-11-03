---
article_id: 360024277871
category: Escrita Fiscal - Impostos - ISS
content_hash: 0864cec131d402831cbd37a4ce4602d62393c41d391b5bbef78ae8eab69c1093
fetched_at: '2026-06-28T22:39:35.271429+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como parametrizar
  o sistema para gerar título do ISS somente via Apuração?
type: support-article
updated_at: '2021-06-15T13:34:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024277871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-parametrizar-o-sistema-para-gerar-t%C3%ADtulo-do-ISS-somente-via-Apura%C3%A7%C3%A3o
---

**Dúvida**

Como parametrizar o sistema para gerar título do ISS somente via apuração?

**Ambiente**

Protheus – Livros Fiscais – a partir da versão 11  
  
**Solução**

Configure conforme abaixo:

NATUREZA

Calcula ISS (ED\_CALCISS) = NÃO " ISS na apuração - gera uma guia com valor total após apuração do ISS"                                         

TES

Calculo ISS (F4\_ISS) = Sim

L. Fiscal ISS (F4\_LFISS) = Tributado

PRODUTO

Aliq. ISS (B1\_ALIQISS) = Informe a alíquota - Caso este campo esteja sem preenchimento, será válido o conteúdo do parâmetro MV\_ALIQISS

Cód. Serv. ISS (B1\_CODISS) = Informe o código de serviço do ISS - Caso não haja o código referente ao serviço deve ser incluído na tabela 60 do Configurador.

CLIENTE

Recolhe ISS (A1\_RECISS) = SIM - NÃO - Apuração ISS pago na apuração mensal.

ISS no preço (A1\_INCISS) = Não agrega o valor de ISS à base de cálculo

Para definir quem é responsável pelo recolhimento do ISS, deve-se informar no cadastro de clientes o responsável pelo recolhimento do ISS através do campo A1\_RECISS.

Quando o responsável pelo recolhimento do ISS é o destinatário pode-se configurar o sistema para deduzir do valor das duplicatas o valor do ISS que foi incluído na mesma. Para tanto, deve-se configurar o parâmetro MV\_DESCISS como .T.
