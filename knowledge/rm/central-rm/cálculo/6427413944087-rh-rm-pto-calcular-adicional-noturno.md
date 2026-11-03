---
article_id: 6427413944087
category: Cálculo
content_hash: 22b54d6ad754d222298307907188330b4c74807f63b681188c461b1f8186a03c
fetched_at: '2026-06-28T22:46:29.197875+00:00'
product: rm
section_id: 1500000861662
source: central-rm
title: RH - RM - PTO - Calcular adicional noturno
type: support-article
updated_at: '2025-01-07T18:18:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6427413944087-RH-RM-PTO-Calcular-adicional-noturno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16980492205719) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como fazer para calcular adicional noturno no espelho do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - Todas as versões  
  
**Solução**

Para que o sistema Automação de Ponto considere adicional noturno no cálculo é necessário realizar algumas configurações conforme abaixo:

1. No cadastro de horário vinculado ao funcionário, na aba de Identificação, deve estar marcado o parâmetro "Paga adicional noturno".

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29041774892311)

2. No Parametrizador do Funcionário | Etapa 10- Adicional Noturno,  deve estar marcado o parâmetro "Pagar Adicional noturno".  

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29041805870999)

3 . No Parametrizador do Sindicato | Etapa 5 - Adicional noturno informar início e fim a ser considerado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29041805879959)

4 . Cadastrar os eventos do TOTVS Automação de Ponto  com os códigos de cálculo de 0009 até 0017 e 0033 ,0034,0037 e se utilizar a redução da jornada noturna valide o cadastro dos códigos de cálculo 0051 a 0053,  que se referem ao adicional noturno, posteriormente nos parâmetros do Sindicato | etapa 18 - Eventos associar estes eventos aos seus respectivos eventos do RM Labore.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29041774909719)

**Saiba mais**Para maiores informações sobre cadastro de horários noturnos, acesse o link :

[RH - RM - PTO - Cadastrar jornada em horário noturno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010026091-TOTVS-RH-Linha-RM-PTO-Como-cadastrar-jornada-em-hor%C3%A1rio-noturno-)

Para maiores informações sobre os parâmetros do adicional noturno disponíveis na Etapa 5 do Parametrizador do Sindicato, acesse o link:

[RH - RM - PTO - Parâmetros do adicional noturno](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296180603159-TOTVS-RH-Linha-RM-PTO-Qual-a-funcionalidade-dos-par%C3%A2metros-do-adicional-noturno-?source=search)
