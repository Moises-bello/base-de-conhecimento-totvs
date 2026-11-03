---
article_id: 4403845669271
category: RH - Lançamentos
content_hash: eb633f5214cd5181178f2d89934f887fef350044a9a6be453fb4576a37679a02
fetched_at: '2026-06-28T22:44:46.871967+00:00'
product: protheus
section_id: 32419271673111
source: central-protheus
title: RH - Linha Protheus - PON - Pré Abono não é salvo após o Apontamento quando
  o horário é Móvel Livre
type: support-article
updated_at: '2026-05-26T19:02:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403845669271-RH-Linha-Protheus-PON-Pr%C3%A9-Abono-n%C3%A3o-%C3%A9-salvo-ap%C3%B3s-o-Apontamento-quando-o-hor%C3%A1rio-%C3%A9-M%C3%B3vel-Livre
---

**Ocorrência**Pré Abono não é salvo após o Apontamento quando o horário é Móvel Livre.  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoas- Todas as versões  
  
**Causa**Quando a modalidade do horário é **Móvel Livre**, o sistema **não** valida as **marcações** feitas pelo funcionário, **e sim a quantidade de horas** que devem ser trabalhadas, com isso, o **apontamento** é feito com base na **marcação de saída**. A partir da **primeira marcação feita no dia**, o **sistema calcula** a **quantidade de horas** que devem ser trabalhadas e projeta qual deve ser o **horário de saída**. Nestes casos, o **Pré Abono** deve ser **lançado** sempre **se baseando** no horário que o funcionário deveria ter **finalizado a jornada**, e não na entrada ou em saídas durante o expediente.  
  
**Solução**Para que o **Pré Abono** seja considerado corretamente quando o horário é **Móvel Livre**, siga os passos do exemplo abaixo:  
  
1 - Neste exemplo, vou utilizar uma **Tabela de Horário Padrão, em Atualizações-Cadastro do Ponto-Tabela de horário padrão,** com horário das **08h - 12h - 13h - 17h**, ou seja, subtraindo o intervalo, o funcionário deve trabalhar no dia **08h**:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403845367575)  
  
2 - **Em Atualizações-Cadastro do ponto-Regra Apontamento** o horário está **Móvel Livre:**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403853118871)  
  
3 - **Em Atualizações-Lançamentos-Integrados**, No dia **01.06**, o funcionário iniciou o expediente às **10h**. Como o **apontamento** é feito pela **saída**, veja que foi gerada uma **SAÍDA ANTECIPADA** e não **Atraso** neste dia:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403845468183)  
  
4 - Levando em consideração o **horário de entrada** que foi às **10h**, e que meu funcionário deveria ter cumprido uma **jornada de 08h** no dia, ele deveria ter **finalizado** o expediente às **19h**, portanto, o meu **Pré Abono** será das **17h às 19h**:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403845514519)  
  
5 - Fazendo o **apontamento** das marcações (pela rotina de Integrados ou Leitura/Apontamento), veja que o **abono** foi lançado corretamente:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403853262615)  
  
**Importante ressaltar que essa regra é válida para abonos feitos por:**   
- *App* Meu RH;   
- Portal GCH;  
- Módulo de Medicina e Saúde do Trabalho;   
- diretamente na rotina de Pré Abono do SIGAPON.  
  
**Apenas o SIGAPON faz o controle da flexibilização do horário**, portanto, quando for lançado um **abono** pelos demais produtos citados, **deve ser levado em consideração as orientações dadas anteriormente para o correto lançamento.  
  
Saiba mais,**

[RH - Linha Protheus - PON - Como fazer o lançamento de Pré Abono no Ponto Eletrônico](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052082954-RH-Linha-Protheus-PON-Como-fazer-o-lan%C3%A7amento-de-Pr%C3%A9-Abono-no-Ponto-Eletr%C3%B4nico)

[RH - Linha Protheus - PORTAL GCH - Como efetuar solicitação de abono e justificativa de pré abono](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416027072535-RH-Linha-Protheus-PORTAL-GCH-Como-efetuar-solicita%C3%A7%C3%A3o-de-abono-e-justificativa-de-pr%C3%A9-abono)

[RH - Linha Protheus - PON - Alteração ou Exclusão de Pré Abonos já utilizados](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059450793-RH-Linha-Protheus-PON-Altera%C3%A7%C3%A3o-ou-Exclus%C3%A3o-de-Pr%C3%A9-Abonos-j%C3%A1-utilizados)
