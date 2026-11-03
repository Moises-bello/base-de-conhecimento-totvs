---
article_id: 4412170874391
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: f27771e14cfc19f14976d8c68223c8e9b713f7e96523ce822eb704f0baf35311
fetched_at: '2026-06-28T22:38:41.083046+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Array out of
  bounds ( 0 of 74 ) on A410MULTT(MATV410A.PRW)
type: support-article
updated_at: '2022-03-24T16:51:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412170874391-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Array-out-of-bounds-0-of-74-on-A410MULTT-MATV410A-PRW
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar incluir ou alterar o campo **C6\_PRCVEN,** o sistema gera error.log, conforme o anexo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412177910423/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4412181526167/mceclip1.png)  
**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- Todas as versões.  
  
**Causa**

Erro de array out of bound indica que o programa está tentando acessar uma posição de array à qual não existe.

A causa pode estar relacionada a algum campo não localizado, devido a:

* Não possuir no dicionário / na base;
* Não estar devidamente marcado como usado;
* Não estar marcado como visível para o módulo em questão;
* Estar configurado com nível de campo superior ao disponível para o usuário;

Outras causa possíveis:

* Alguma customização influenciando no processo (quando há customizações por ponto de entrada ou mesmo nos dicionários);
* Ou alguma chamada indevida no fonte à uma posição de array inexistente.

Para este caso, o problema é que o campo **C6\_DESCONT** não localizado pela função podendo estar relacionado a alguma das opções de causa de campo acima.

O erro também pode ocorrer, caso o campo **C6\_VALDESC** não seja localizado pela função, podendo estar relacionado a alguma das opções de causa mencionadas acima.

**Solução**

Para solucionar:

1- Acessar o modulo **SIGACFG - Configurador → Base de Dados → Dicionário → Base de Dados;**

2 - Pesquisar a tabela SC6 e buscar pelo campo **C6\_DESCONT** ou **C6\_VALDESC**  ;

3 - Alterar o campo ,selecionar a ABA (USO), deixar o campo como  USADO e  o nível de campo igual 1.

4 - Salvar o campo, salvar a tabela e atualizar o dicionário de dados.

5 - Reinicie o smartcliente e efetue o procedimento novamente.
