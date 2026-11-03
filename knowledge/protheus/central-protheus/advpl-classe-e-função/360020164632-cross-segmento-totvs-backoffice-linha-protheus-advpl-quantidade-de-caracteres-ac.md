---
article_id: 360020164632
category: ADVPL - Classe e Função
content_hash: 7441c9b6b7495289021032a9082cff646b0208b4599be7c0a82706bf119f3011
fetched_at: '2026-06-28T22:40:17.123446+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Quantidade de caracteres
  aceitos em uma pergunta de relatório do tipo Range(X1_GSC = "R")
type: support-article
updated_at: '2022-06-13T21:09:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020164632-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Quantidade-de-caracteres-aceitos-em-uma-pergunta-de-relat%C3%B3rio-do-tipo-Range-X1-GSC-R
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Bom dia, estamos com um problema em uma pergunta específica de um relatório personalizado, a pergunta em questão é do tipo "R" Range e deveria aceitar diversos tipos separados por ";" ou "-".  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Nas versões recentes de **Lib**, o local de gravação das perguntas informadas nos parâmetros de um relatório, são definidas pelas opções selecionadas em restrições de acesso no cadastro do usuário. Quando as opções **108 - Gravar Resposta Parametros** e **150 - Gravar Resposta Parametros por Empresa** estiverem marcadas, os últimos dados informados nos parâmetros serão gravados no Profile do usuário.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016277431/mceclip3.png)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360016218152/mceclip0.png)

Neste caso, e somente após o sistema gravar a primeira vez o pergunte, o limite de caracteres no campo do tipo Renge passará de 60 pra 250.  
  
**Saiba mais  
[SX1 - Perguntas do usuário](http://tdn.totvs.com/pages/viewpage.action?pageId=22479548)**
