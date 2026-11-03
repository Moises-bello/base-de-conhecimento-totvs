---
article_id: 6148469776535
category: Folha Mensal
content_hash: 76ddc052944cbd959dc6772892610dceab1ce896d43b8e4d45a2f6216af96bbd
fetched_at: '2026-06-28T22:46:59.181128+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Como fixar período para lançamento de arredondamento
type: support-article
updated_at: '2024-09-16T19:56:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6148469776535-RH-RM-FOP-Como-fixar-per%C3%ADodo-para-lan%C3%A7amento-de-arredondamento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:03:36 min  
  
Dúvida**  
Como fixar somente 1 período para lançamento de arredondamento?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Se não realizou o lançamento quinzenal e lança férias no mês e teve arredondamento. No próximo mês no primeiro período que ocorrer o algum lançamento em qualquer período será realizado o desconto do arredondamento referente ao mês anterior.  
   
Desta forma visualize no envelope mês anterior qual período ocorreu o arredondamento e de forma que foi lançado o arredondamento no período das férias, o período 2 das férias foi o primeiro ter lançamento.  
   
O sistema sempre irá descontar o seu arredondamento (Insuficiência de saldo) no primeiro movimento que existir, para que isso não ocorra é necessário que o seus eventos de arredondamento tanto Provento (Código de Cálculo 20) quando Desconto (Código de Cálculo 21) tenham fórmulas parametrizadas, segue uma sugestão para criar esta situação.  
  
**Evento código de calculo 20:**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148239913367/mceclip0.png)

DECL VALMIN, MENORNOTA, RES, LIQ;

SE PERIODO = 1 OU PERIODO = 2 OU PERIODO = 3

ENTAO 0

SENAO SETVAR(VALMIN, C('0005'));

              SETVAR(MENORNOTA, TABFUNC('ARREDONDAMENTO', 'V'));

              SETVAR(LIQ, L);

              SE LIQ < VALMIN

ENTAO SETVAR(RES, VALMIN - LIQ);

              SETVAR(LIQ, LIQ + RES)

FIMSE;

SE ABS(MENORNOTA) > 0.005

ENTAO SE LIQ - (INT(LIQ / MENORNOTA) \* MENORNOTA) > 0.005

ENTAO SETVAR(RES, RES + INT((LIQ + MENORNOTA) / MENORNOTA) \* MENORNOTA - LIQ)

FIMSE FIMSE;

RES

FIMSE  
  
**Evento código de calculo 21:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6148267565591/mceclip1.png)**

SE PERIODO = 2 OU PERIODO = 3 OU PERIODO = 4 OU PERIODO = 7 OU PERIODO = 8 OU PERIODO = 9 OU PERIODO = 10

ENTAO 0

SENAO MV(DECMES(MES, 1), DECANO(MES, ANO, 1), '0020')

FIMSE  
  
**Importante**  
Caso seja necessário realizar alguma alteração nas fórmulas para atender a realidade da sua empresa e você necessite de suporte, será necessário entrar em contato com a consultoria telefônica da Totvs, por se tratar de uma customização do produto padrão.  
  
**Saiba Mais**

[RM - FOP - Funcionários: Arredondamento do líquido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019749111-RM-FOP-Funcion%C3%A1rios-Arredondamento-do-l%C3%ADquido)  
[RH - RM - FOP - Desconto de arredondamento no adiantamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020837551-RH-RM-FOP-Desconto-de-arredondamento-no-adiantamento)
