---
article_id: 360048518013
category: RH - Definições de Cálculo
content_hash: e275996456cd9546ec917d8b423112a30b186aa1da50a09369298ff4c4c07293
fetched_at: '2026-06-28T22:43:22.306525+00:00'
product: protheus
section_id: 360011913513
source: central-protheus
title: RH - Linha Protheus - GPE - Como cadastrar estabilidade após retorno de Ausência
type: support-article
updated_at: '2025-09-30T13:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048518013-RH-Linha-Protheus-GPE-Como-cadastrar-estabilidade-ap%C3%B3s-retorno-de-Aus%C3%AAncia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16453336650007) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**Como cadastrar estabilidade após o funcionário retornar de Ausência?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**No menu do Módulo 07 - SIGAGPE, acesse **Atualizações > Definições de Cálculo > Tipos de Ausências (GPEA430)**:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360070154874)  
  
Selecione o tipo de ausência que quer cadastrar a estabilidade e em seguida, clique na opção **Alterar**, como exemplo, utilizaremos o código 003 - Afastamento Temporário Acidente de Trabalho:  
  
![](https://i.imgur.com/FvPgXsq.png)  
  
No campo **D.Estab.** - RCM\_DIAEST, informe a quantidade de dias de estabilidade após o retorno da ausência:  
  
![](https://i.imgur.com/usuPH4I.png)

Lançar o afastamento em **Atualizações > Lançamentos > Ausências**, selecione o funcionário que deverá ser afastado e em seguida selecione o botão "**+Manutenção**" :

![](https://i.imgur.com/d7gip5E.png)

![](https://i.imgur.com/tsIn8dP.png)  
  
Informe o código do tipo de ausência e a data de inicio e fim do afastamento:

![](https://i.imgur.com/m9PYT85.png)  
  
Em **Atualizações > Funcionários > Funcionários** selecione o funcionário que foi afastado e em seguida, selecione o botão "**Visualizar**" :  
  
![](https://i.imgur.com/jSXhDc3.png)  
  
O  campo Dt.Vto.Estab (**RA\_DTVTEST**) será preenchido automaticamente após o lançamento do afastamento do funcionário levando em consideração a configuração do cadastro do Tipo de Ausência e a Data fim do Afastamento:  
  
![](https://i.imgur.com/Jf50OPr.png)  
  
**Saber Mais:**

[RH - Linha Protheus - GPE - Cadastro tipos de ausência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029174591-RH-Linha-Protheus-GPE-Cadastro-tipos-de-aus%C3%AAncia?source=search)

[RH - Linha Protheus - GPE - Quais os parâmetros utilizados para o lançamento de ausências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9071036090007-RH-Linha-Protheus-GPE-Quais-os-par%C3%A2metros-utilizados-para-o-lan%C3%A7amento-de-aus%C3%AAncias-?source=search)

[RH - Linha Protheus - GPE - Quais os pontos de entrada disponíveis na rotina GPEA240-Lançamentos de Ausências](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5421742901399--RH-Linha-Protheus-GPE-Quais-os-pontos-de-entrada-dispon%C3%ADveis-na-rotina-GPEA240-Lan%C3%A7amentos-de-Aus%C3%AAncias?source=search)

[RH - Linha Protheus - GPE - Como informar para o sistema que o novo afastamento é sequencia do anterior](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049659234-RH-Linha-Protheus-GPE-Como-informar-para-o-sistema-que-o-novo-afastamento-%C3%A9-sequencia-do-anterior?source=search)
