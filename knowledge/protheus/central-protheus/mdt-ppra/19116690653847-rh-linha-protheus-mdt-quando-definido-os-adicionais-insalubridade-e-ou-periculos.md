---
article_id: 19116690653847
category: MDT - PPRA
content_hash: 5db5ff163cb291ac6b11c32947742c41ea8b7214a7eab9e1e6673f97e8ed436b
fetched_at: '2026-06-28T22:44:27.200349+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Quando definido os adicionais insalubridade e ou
  periculosidade pelo medicina, qual o comportamento esperado pelo sistema e reflexos
  no cadastro do funcionário
type: support-article
updated_at: '2025-07-31T14:23:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19116690653847-RH-Linha-Protheus-MDT-Quando-definido-os-adicionais-insalubridade-e-ou-periculosidade-pelo-medicina-qual-o-comportamento-esperado-pelo-sistema-e-reflexos-no-cadastro-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19116635715223) Tempo aproximado para leitura: **00:02:00min** **Dúvida**Quando definido os adicionais insalubridade e ou periculosidade pelo medicina, qual o comportamento esperado pelo sistema e reflexos no cadastro do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para saber como definir se a taxa percentual de insalubridade e periculosidade consulte o link abaixo:  
  
[Como definir se o percentual de insalubridade/periculosidade virá do módulo Medicina e Segurança do Trabalho(SIGAMDT)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050187334)  
  
Acessando o parâmetro **MV\_MDTADIC**  do módulo configurador do Protheus **(SIGACFG)** , através do caminho **Ambiente > Cadastros > Parâmetros** e alterando seu valor para **.T.**  
  
![PARAMETRO.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197552063639)  
  
  
![gif.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/19203757768215)  
  
[Como defino um Risco com adicionais de insalubridade e ou periculosidade](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416286404247)  
  
A alteração do parâmetro **MV\_MDTADIC** apenas define de onde virá as informações em relação a **taxa percentual** do adicional (Periculosidade/Insalubridade) , o módulo **GPE (07)** possui autonomia sobre  o processo relacionado aos adicionais no cadastro do funcionário, através do caminho **Atualizações > Funcionários > Funcionários** na aba **Adicionais.**  
  
![adicionais.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19197530597783)  
  
**Observação:** Caso o funcionário tenha mais de um risco com percentuais diferentes, a taxa percentual a ser considerada será a de maior valor.  
  
**Saiba mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)
