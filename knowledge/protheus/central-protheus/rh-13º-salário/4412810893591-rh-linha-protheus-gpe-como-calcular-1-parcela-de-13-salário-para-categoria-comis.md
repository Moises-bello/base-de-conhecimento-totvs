---
article_id: 4412810893591
category: RH - 13º salário
content_hash: bb7a6d3a100900f6d5ebbd44bd62b40a797411d4a25763ef80d0a1c4bfa7cabb
fetched_at: '2026-06-28T22:44:00.540932+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular 1° Parcela de 13° Salário para categoria
  comissionado puro
type: support-article
updated_at: '2025-07-23T14:12:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412810893591-RH-Linha-Protheus-GPE-Como-calcular-1-Parcela-de-13-Sal%C3%A1rio-para-categoria-comissionado-puro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18910011207703)Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como calcular 1° Parcela de 13° Salário para categoria comissionado puro  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**O funcionário na categoria de comissionado puro, receberá durante o ano valores de comissão, entre outras verbas relacionadas.   
Para que o sistema gere o valor da primeira parcela, essas verbas de provento que o funcionário recebe durante o ano, **devem estar com o campo Media 13º na aba Médias devidamente parametrizado**. Dessa maneira o sistema fará o cálculo das médias de acordo com a parametrização realizada.  
  
Verba de identificador **0165 (comissão).** No exemplo a seguir, foi informado **S** no campo de **Média 13º** para que o sistema verifique a parametrização de acordo com o sindicato.  
Veja os tipos de parametrizações: [RH - Linha Protheus - GPE - Médias no cálculo do 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016223611-RH-Linha-Protheus-GPE-M%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412802380823)  
  
Para calcular, será necessário informa **SIM** na pergunta **Cálculo Médias?**No exemplo utilizamos a rotina **GPEA580 -** **Atualizações > Lançamentos > Por funcionário**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412810661271)  
  
Após confirmar, visualize e confira o calculo gerado  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412810717847)  
  
Para auxiliar na conferencia, é possível gerar a memoria de calculo e/ou demonstrativo de médias

**-Memória de Cálculo**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412802463767)

**-Demonstrativo de Médias DEM\_MED**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18958061339031)

**-Demonstrativo de médias via rotina GPER080**  
![mceclip0.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4412798146199)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412802479511)

**Importante:**

Caso o valor de médias a serem pagas não sejam superior ou igual ao valor da Garantia de comissão cadastrada no sindicato, a diferença para que seja pago o valor igual da garantia de comissão será calculado automaticamente pelo sistema nos id 0022 e 0024.

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como conferir o Relatório de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025175673-RH-Linha-Protheus-GPE-Como-conferir-o-Relat%C3%B3rio-de-M%C3%A9dias-)  
[RH - Linha Protheus - GPE - Sistema não calcula verbas de médias no 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016249711-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-calcula-verbas-de-m%C3%A9dias-no-13%C2%BA-sal%C3%A1rio)  
[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para 13º](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiXxVqaAwQ6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBlGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzQ0MTM1MjEwNTMwNzktUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tZ2VyYXItby1kZW1vbnN0cmF0aXZvLWRlLW0lQzMlQTlkaWFzLXBhcmEtMTMlQzIlQkEGOwhUOg5zZWFyY2hfaWRJIikyOGUyNzg3Yy0xMTVhLTQ2YWUtYTE1Zi0yYTBjN2QxOTE4OGIGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhdkZW1vbnN0cmF0aXZvIDEzwroGOwhUOhJyZXN1bHRzX2NvdW50aQL1BA%3D%3D--4dffb3cf15bc96a630100cd185f75ab60af3abd6)  
[RH - Linha Protheus - GPE - Como gerar memória de calculo para conferência de médias da primeira parcela do 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000096841-RH-Linha-Protheus-GPE-Como-gerar-mem%C3%B3ria-de-calculo-para-confer%C3%AAncia-de-m%C3%A9dias-da-primeira-parcela-do-13%C2%BA)
