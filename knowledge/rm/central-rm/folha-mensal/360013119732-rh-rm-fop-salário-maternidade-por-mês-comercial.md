---
article_id: 360013119732
category: Folha Mensal
content_hash: ec6ff778ad3204b99ed2aef2d3993b13a9e460bf8b9ac66f2c1ed8df2a7ab464
fetched_at: '2026-06-28T22:47:00.289267+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Salário Maternidade por mês comercial
type: support-article
updated_at: '2025-01-20T21:43:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013119732-RH-RM-FOP-Sal%C3%A1rio-Maternidade-por-m%C3%AAs-comercial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:00:40 min  
  
Dúvida**Como parametrizar o pagamento de salário maternidade com base no mês comercial, ou seja, 30 dias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Para que o sistema acate o cálculo de 30 dias para a Licença Maternidade, é necessário acessar **Configurações | Parametrizador | Folha Normal | Encargos Sociais** e desmarcar o parâmetro **Calcula salário maternidade conforme SEFIP**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4423035855127/mceclip0.png)  
  
Funcionalidade do parâmetro:

* **Desmarcado:**Log de cálculo: Salário / **30**\* 31
* **Marcado:**Log de cálculo: Salário / **31** \* 31

**Exemplo**  
Funcionário recebe R$500,00 e afastou no dia 20/03

Cálculo Salário Maternidade com o parâmetro marcado:  
500/30, sendo o número de dias do mês comercial \* 19 dias trabalhados = 316,67  
500/31, sendo o número do mês calendário \* 12 dias de Licença = 193,55  
   
Cálculo Salário Maternidade sem o parâmetro marcado:  
500/30, sendo o número de dias do mês comercial \* 19 dias trabalhados = 316,67  
500/30, sendo o número de dias do mês comercial \* 12 dias de Licença = 200,00  
  
**Importante**  
Caso o parâmetro **Calcula salário maternidade conforme SEFIP** esteja marcado, o sistema irá calcular a remuneração proporcional considerando o mês calendário, 28, 29, 30 ou 31 dias, conforme cálculo do SEFIP. O valor do Salário Maternidade será a Base de licença maternidade dividido pelo número de dia do mês, de acordo com o parâmetro, multiplicado pelo número de dias de licença no mês.
