---
article_id: 360034158814
category: ADVPL - Classe e Função
content_hash: 49ad71e02b43ecc5149a75a51d627d2669778430556b6958e731c80c8626426f
fetched_at: '2026-06-28T22:40:15.777212+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - É possível realizar
  a manipulação de arquivos temporários em nível de banco de dados
type: support-article
updated_at: '2022-04-25T16:53:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034158814-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-realizar-a-manipula%C3%A7%C3%A3o-de-arquivos-tempor%C3%A1rios-em-n%C3%ADvel-de-banco-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**É possível realizar a manipulação de arquivos temporários em nível de banco de dados?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Assim como na função `DBUseArea()`, é possível utilizar a classe `FwTemporaryTable()` para manipulação de  arquivos temporários.  
Com esta classe é possível criar arquivos de trabalho que podem ser facilmente utilizados (tanto diretamente no banco de dados, como no Protheus).

A utilização de tabelas temporárias com `FwTemporaryTable()`, além de fornecer muito mais velocidade no acesso aos dados, pode ser realizada com o uso de apenas uma classe (diferente da `DBUseArea()` que necessita das funções `CriaTrab()` + `IndRegua()`​).  
  
**Saiba mais**  
[FWTemporaryTable](http://tdn.totvs.com/display/framework/FWTemporaryTable)
