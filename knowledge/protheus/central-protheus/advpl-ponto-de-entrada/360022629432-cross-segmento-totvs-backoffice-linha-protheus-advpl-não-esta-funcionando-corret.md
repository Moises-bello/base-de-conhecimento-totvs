---
article_id: 360022629432
category: ADVPL - Ponto de Entrada
content_hash: 725c9eab714d6bdde32af13e80fda1ba5bbd3205d5344453f3ae0821bd231c6d
fetched_at: '2026-06-28T22:40:11.767885+00:00'
product: protheus
section_id: 1500001549122
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Não esta funcionando
  corretamento o Ponto de Entrada GRVLIQSE5.
type: support-article
updated_at: '2021-12-29T14:30:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022629432-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-N%C3%A3o-esta-funcionando-corretamento-o-Ponto-de-Entrada-GRVLIQSE5
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Não esta funcionando corretamente o ponto de entrada **GRVLIQSE5**, houve alguma mudança?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL– A partir da versão 12.1.17  
 **Solução**A partir da versão 12, os pontos de entrada que manipulavam a tabela SE5 serão descontinuados devido à alteração das rotinas de gravação da SE5 para MVC e gravação das tabelas da família FK.

No padrão MVC temos um único ponto de entrada e este é chamado em vários momentos dentro do fonte padrão. Sua ação será determinada pelo seu ID de execução.

FINM010 é o modelo de dados de baixa a receber, e, portanto, é o ponto de entrada usado por rotinas que realizam este tipo de operação. O momento da sua execução será definido conforme o ID de execução utilizado.

Para gravação dos registros auxiliares (multa, juros, desconto) esse ponto de entrada não irá atender, para **gravação na tabela SE5**. Deverá ser analisado pontualmente qual o ponto de entrada que irá atender a necessidade desejada.  
  
**Saiba Mais**  
[Ponto de entrada para gravação de dados complementares nas tabelas FK´s e SE5](http://tdn.totvs.com/pages/releaseview.action?pageId=284859148)
