---
article_id: 4412351039767
category: RH - Definições de Cálculo
content_hash: 25f157e0de5a474f417b4f345daab041f8c767f07b270a3b89bad2d764413041
fetched_at: '2026-06-28T22:43:22.587845+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Quais são as verbas de Faltas que podem influenciar
  nos cálculos
type: support-article
updated_at: '2025-09-30T17:02:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412351039767-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-verbas-de-Faltas-que-podem-influenciar-nos-c%C3%A1lculos
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26411037971735) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Quais são as verbas de Faltas que podem influenciar nos cálculos de férias, 13º, entre outros?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**No sistema existem 5 identificadores de cálculo utilizados para desconto de faltas e atrasos. São eles:  
 **0054 - Desconto de Faltas****0055 - Desconto de Atrasos****0203 - Desconto de falta mês anterior****0242 - Desconto de Faltas (II)****0243 - Atrasos (II)****Para abater** dos dias de férias e 13º por exemplo, o sistema verifica nos acumulados (SRD) **verbas de descontos** com os identificadores citados.  
Existindo estas verbas nos acumulados o sistema faz a proporcionalização no calculo de férias e 13º deduzindo gradativamente de acordo com cada legislação.  
  
Porem existem os identificadores de cálculo para reembolso, são eles:  
**0244 - Reembolso de Faltas****0245 - Reembolso de Atrasos**Estes id's devem ser vinculados à **verbas de proventos** que tratam o **reembolso de faltas e atrasos**. O sistema irá considerá-las também no calculo da proporcionalização dos dias de gozo das férias.  
Para que a falta seja considerada é necessário que esteja lançada em folha de pagamento ou rescisão em horas ou dias.  
 **Saiba Mais**[RH - Linha Protheus - GPE - Abater faltas no calculo do 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052988053)  
[RH - Linha Protheus - GPE - Como conferir faltas do funcionário apresentadas no cálculo de férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053018573-RH-Linha-Protheus-GPE-Como-conferir-faltas-do-funcion%C3%A1rio-apresentadas-no-c%C3%A1lculo-de-f%C3%A9rias)  
[RH - Linha Protheus - GPE - No cálculo da rescisão, o sistema verifica a quantidade de faltas da rotina de Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033628574-MP-GPE-No-c%C3%A1lculo-da-rescis%C3%A3o-o-sistema-verifica-a-quantidade-de-faltas-da-rotina-de-Controle-de-Dias-de-Direito-)  
[RH - Linha Protheus - GPE - Como é composto o campo 50 (Saldo de Salário) no TRCT e como abater as Faltas do mesmo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011029251-MP-GPE-Como-%C3%A9-composto-o-campo-50-Saldo-de-Sal%C3%A1rio-no-TRCT-e-como-abater-as-Faltas-do-mesmo-)
