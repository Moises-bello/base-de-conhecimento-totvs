---
article_id: 360036236114
category: Escrita Fiscal - Impostos - ICMS
content_hash: 3c77ba863859240bf5925cf411613fbc21181be23edb68633391549b092671bf
fetched_at: '2026-06-28T22:39:26.003506+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Relatório MATR940
type: support-article
updated_at: '2021-07-28T14:26:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036236114-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Relat%C3%B3rio-MATR940
---

**Dúvida**O relatório MATR940 não carrega informações de resumo por CFOP de algumas filiais?

 **Ambiente**Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

1. Gerar a apuração de ICMS pela rotina MATA953.

2. Conferir as informações de resumo por CFOP na apuração de ICMS.

3. Configurar o parâmetro **MV\_CONSCGC** = .F., com essa configuração o relatório MATR940 foi gerado com sucesso para todas as filiais.

**MV\_CONSCGC** - Indica se o tratamento de filial de/ate deve ser  feito através da filial de/ate das perguntas ou  através dos 8 primeiros dígitos do CNPJ.        

4. Gerar o relatório MATR940.
