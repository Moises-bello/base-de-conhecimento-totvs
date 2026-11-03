---
article_id: 360017556112
category: Financeiro - Contas a Receber
content_hash: 21b9158b19894535d083b34424c4a5c2e5e81ea82dca0347ec18ae452b15d0e9
fetched_at: '2026-06-28T22:38:12.672679+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA070 - Como é calculado a multa automaticamente
type: support-article
updated_at: '2026-05-12T13:35:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017556112-MP-SIGAFIN-FINA070-Como-%C3%A9-calculado-a-multa-automaticamente
---

**Dúvida**  
A multa não está sendo calculada. Como proceder para que o sistema realize o cálculo corretamente?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Para que o sistema realize corretamente o cálculo da multa, é necessário que a empresa configure previamente os seguintes parâmetros:

* **MV\_JURTIPO = L**  
  Define o tipo de cálculo de juros e multa a ser aplicado aos títulos.
* **MV\_LJMULTA**  
  Parâmetro responsável por determinar o **percentual de multa** aplicado aos títulos a receber em atraso.

Após a configuração dos parâmetros, ao acessar o sistema com uma **data posterior ao vencimento do título** e efetuar a baixa por meio da rotina **FINA070 – Baixa manual de títulos a receber**, o campo **Multa** será automaticamente preenchido de acordo com o percentual informado no parâmetro **MV\_LJMULTA**.

**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como calcular multa e juros](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14635481028759-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-calcular-multa-e-juros)
