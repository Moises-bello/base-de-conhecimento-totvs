---
article_id: 14917911087127
category: RH - Provisão
content_hash: a5b6a206f1fdf92dcf2a0cb14f0edc690ffd35e76e9d5a4905a7e3f8064826a0
fetched_at: '2026-06-28T22:43:55.650491+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixas de Provisão de 13º Salário Não são Caculadas
  para Funcionário Desligado
type: support-article
updated_at: '2025-06-18T18:19:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14917911087127-RH-Linha-Protheus-GPE-Baixas-de-Provis%C3%A3o-de-13%C2%BA-Sal%C3%A1rio-N%C3%A3o-s%C3%A3o-Caculadas-para-Funcion%C3%A1rio-Desligado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32903249921303) Tempo aproximado para leitura: **00:01:30 min****Dúvida**O que Analisar Quando as Baixas de Provisão de 13º Salário Não são Caculadas para Funcionário Desligado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todos os Releases.  
  
**Solução**

Veja no exemplo abaixo, que não foram geradas Baixas de 13º Salário para um funcionário desligado e com isto, foram gerados valores negativos na linha "No Mês":  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14915032092311)  
  
Para solucionar essa dúvida, realize os seguintes passos:

1. Verifique se todas as verbas de Baixas de 13º Salário estão cadastradas.  
Para acessar os Identificadores de Cálculo de baixas de Rescisão [Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029244891-RH-Linha-Protheus-GPE-Identificadores-de-C%C3%A1lculo-de-Baixas-de-Rescis%C3%A3o-nas-Provis%C3%A3o).  
  
2. Acesse Miscelânea / Provisões / Provisões de Férias e 13º Salário (GPEA070), e clique em "Outras Ações" e em seguida em "Cálculo";  
  
3. Nos Parâmetros para cálculo, verifique se a pergunta **Tipo de Provisão?**  está preenchida com a opção **Ambas**, e a pergunta **Incluir Demit. 13o?** está preenchida com **Sim** e processe o cálculo das provisões:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14917419960727)   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14917406792599)

4. Emita o relatório de Provisão de 13º Salário (GPER090) ou acesse o Acumulado das Provisões do funcionário (GPEA070) e confirme seas baixas foram geradas:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14917671921943)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14917653886359)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
