---
article_id: 1500011411822
category: RH – DIRF
content_hash: b4c2212f86ac3e66ef1c7d7e6bcdbbc42cbb322bbbc41ffabcb742fcf68512d7
fetched_at: '2026-06-28T22:44:07.874533+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Como conferir valor de adiantamento regime caixa
  na DIRF com a ficha financeira
type: support-article
updated_at: '2025-08-18T18:35:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011411822-RH-Linha-Protheus-GPE-Como-conferir-valor-de-adiantamento-regime-caixa-na-DIRF-com-a-ficha-financeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34270128739095) Tempo aproximado para leitura: **00:02:00 min**  
**Dúvida**Como conferir valor de adiantamento em regime caixa na DIRF com a ficha financeira?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Emita a **Ficha Financeira por Data de Pagamento**, com a incidência para DIRF e com a pergunta **Destaca ADI com SIM**, conforme exemplo abaixo:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501286026263)

No próximo print, a conferência é referente aos rendimentos de **FEVEREIRO**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501353758871)

O cálculo a ser considerado é: **SOMAR AS VERBAS DE PROVENTO COM INCIDÊNCIA "A" PARA A DIRF MAIS ADIANTAMENTO MÊS SEGUINTE DE FEVEREIRO E SUBTRAIR TODAS AS VERBAS DE DESCONTO COM INCIDÊNCIA "A" PARA A DIRF E SUBTRAIR O DESCONTO DE ADIANTAMENTO DE FEVEREIRO**, então temos:  
9000,00 + 3600,00 - 3600,00 = **9000,00**  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501362362903)

No exemplo abaixo, a conferência é referente aos rendimentos de **MARÇO**:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501356349463)  
  
O cálculo a ser considerado é: **SOMAR AS VERBAS DE PROVENTO COM INCIDÊNCIA "A" PARA A DIRF MAIS ADIANTAMENTO MÊS SEGUINTE DE MARÇO E SUBTRAIR TODAS AS VERBAS DE DESCONTO COM INCIDÊNCIA "A" PARA A DIRF E SUBTRAIR O DESCONTO DE ADIANTAMENTO DE MARÇO**, então temos:  
9000,00 + 4500,00 - 3600,00 = **9900,00**  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501390517271)

No exemplo abaixo, a conferência é referente aos rendimentos de **ABRIL**:  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501397310103)  
  
O cálculo a ser considerado é: **SOMAR AS VERBAS DE PROVENTO COM INCIDÊNCIA "A" PARA A DIRF MAIS ADIANTAMENTO MÊS SEGUINTE DE ABRIL E SUBTRAIR TODAS AS VERBAS DE DESCONTO COM INCIDÊNCIA "A" PARA A DIRF E SUBTRAIR O DESCONTO DE ADIANTAMENTO DE ABRIL**, então temos:  
9000,00 + 4500,00 - 4500,00 = **9000,00**  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4501406392215)  
  
**OBSERVAÇÃO:** Para o cálculo das **VERBAS COM INCIDÊNCIA PARA DIRF**, deve ser considerado tanto os proventos e os descontos.

**Deve ser considerada a mesma linha de raciocínio para conferencia dos demais meses.**

**Saiba mais:**  
[Página centralizadora Protheus - DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030307-RH-DIRF)
