---
article_id: 360018499651
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: fe49098f3288b1fdc83beed78ee5341d56f5025080b444542cf092c757e139fd
fetched_at: '2026-06-28T22:38:31.191886+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Erro na preparação da nota com uso do parâmetro mv_horarmt
type: support-article
updated_at: '2021-04-28T15:55:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018499651-MP-FAT-Erro-na-prepara%C3%A7%C3%A3o-da-nota-com-uso-do-par%C3%A2metro-mv-horarmt
---

**Dúvida**

Ao preparar a nota de saída no faturamento, está gerando o error.log: type mismatch on compare on MAPVL2SF2(MATA461.PRX) 06/06/2017 13:55:06 line : 5218

**Ambiente**Microsiga Protheus - a partir da versão 11.

**Causa**

O erro refere-se a um tipo incompatível que está sendo utilizado para comparação na função **MAPVL2SF2**.

A função em questão, tem uma variável do tipo caractere que recebe a informação passada pelo parâmetro MV\_HORARMT, que também é do tipo caractere. Todavia, essa variável está recebendo uma informação do tipo numérica , conforme o trecho do erro:

STACK MAPVL2SF2(MATA461.PRX) 06/06/2017 13:55:06  
Local 30: CHORARMT(N) :2

Veja que a variável **CHORARMT**, é definida como caractere, devido a letra C no início de seu nome, mas a informação que chega para ela vem entre parênteses como numérico (N), gerando incompatibilidade para a comparação de informações que variável precisa receber e o que está recebendo.

**Solução**

Para solucionar a questão, coloque a informação do parâmetro **MV\_HORARMT** entre aspas duplas ("), indicando que a informação em questão é do tipo caractere: **MV\_HORARMT="2"**
