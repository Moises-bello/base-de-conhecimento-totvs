---
article_id: 360052979613
category: Cadastros
content_hash: 9e1ec9ad8f16cfb0df1327c25e18b0e2ad2de32bc517b7fd0afd6a35018dc8e9
fetched_at: '2026-06-28T22:46:28.475882+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Configurar o Ponto para tratativa de controle por exceção,
  conforme Lei 13.874 de 2019
type: support-article
updated_at: '2025-02-20T15:06:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052979613-RH-RM-PTO-Configurar-o-Ponto-para-tratativa-de-controle-por-exce%C3%A7%C3%A3o-conforme-Lei-13-874-de-2019
---

**Dúvida**Como configurar o Ponto para tratativa de controle por exceção, conforme Lei 13.874 de 2019?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto – A partir da versão 12.1.  
  
**Solução**Considerando o disposto no artigo 74 . *§ 4º Fica permitida a utilização de registro de ponto por exceção à jornada regular de trabalho, mediante acordo individual escrito, convenção coletiva ou acordo coletivo de trabalho.*  
  
O Automação de Ponto possibilita controlar as batida de exceções que são registradas quando se utiliza em conjunto a rotina de lançamento de batidas pelo horário planejado.  
  
O ponto continuará controlando a jornada de trabalho com base no horário planejado e nas batidas de exceções importadas.  
  
Com base neste entendimento, após importar as batidas de exceções, deve-se efetuar o lançamento do horário planejado e em seguida executar o recálculo dos funcionários.

Segue um exemplo da configuração: 

Considerando um funcionário que tenha jornada das 08:00 às 18:00 com 01:12 de refeição de segunda a sexta.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22602114027799)

Observação: Como agora o controle é feito por exceção, é recomendável cadastrar o horário relacionado ao funcionário sem ausência planejada ou limite de refeição.

O funcionário registrou as batidas de exceção nas seguintes datas: 02, 03, 04, 05, 06, 09, 16, e 17.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22602133698839)

Em seguida, efetue o processo de Lançamento das batidas pelo horário planejado. 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22602114056471)

Após o lançamento das batidas e o recalculo, o sistema irá apresentar as ocorrências de trabalho e extras normalmente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22602133732503)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22602133746839)

Caso ocorra uma exceção na entrada ou saída antecipada, as outras batidas serão registradas de acordo com o horário planejado. 

**Saiba Mais**[Lançamento de horários Planejado](https://tdn.totvs.com/pages/releaseview.action?pageId=452719844)  
[Lei 13.874/19 - Registro de ponto por exceção](https://tdn.totvs.com/pages/releaseview.action?pageId=539705391)
