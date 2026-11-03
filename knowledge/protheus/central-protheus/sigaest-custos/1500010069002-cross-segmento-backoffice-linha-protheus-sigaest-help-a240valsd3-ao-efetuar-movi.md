---
article_id: 1500010069002
category: SIGAEST - CUSTOS
content_hash: 42e8b3218e2ebcefe4ae1d15dd396c8ab769873bd8eead557f10dad7a6e3176a
fetched_at: '2026-06-28T22:39:00.934312+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - HELP A240VALSD3 ao
  efetuar Movimentação Valorizada (Acerto de Custo)
type: support-article
updated_at: '2021-05-10T16:31:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010069002-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-HELP-A240VALSD3-ao-efetuar-Movimenta%C3%A7%C3%A3o-Valorizada-Acerto-de-Custo
---

**Dúvida**Ao fazer uma Movimentação Valorizada para acertar o custo de algum(uns) produto(s), ocorre o HELP A240VALSD3: *"Problema: O campo Custo da Movimentação não foi preenchido, portanto este registro não será gravado. Este campo só é obrigatório caso o campo F5\_VAL esteja com conteúdo "S")."* Porém está sendo utilizado um Tipo de Movimentação com F5\_VAL = Sim e tem valor de custo inserido no campo. O que fazer para corrigir?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

Este erro normalmente ocorre em situações específicas, em geral reproduzidas em operações aritméticas onde o resultado da operação tivesse 8 dígitos inteiros significativos ou mais, onde subsequentes operações de arredondamento -- por exemplo as funções int(), round() e/ou noround() -- poderiam não apresentar o resultado correto.

Para corrigir este problema, o Kernel do AdvPL ganhou um novo bloco de funções aritméticas, habilitadas mediante parâmetro, onde a precisão em cálculos com ponto flutuante não apresentam mais flutuações de arredondamento, respeitado o limite de 15 dígitos significativos da precisão numérica do AdvPL.

A utilização deste parâmetro altera o comportamento aritmético da linguagem AdvPL, aumentando a precisão global das operações, e corrigindo erros de arredondamento oriundos de operações específicas nos contextos mencionados acima.

Valores Válidos

|  |  |
| --- | --- |
| **Valores** | **Descrição** |
| 0 (padrão) | Não usa o novo bloco de funções aritméticas internas. |
| 1 | Utiliza o novo bloco de funções aritméticas internas. |

Exemplo de aplicação no appserver.ini:

|  |
| --- |
| ``` [General] FloatingPointPrecise=1 ``` |

Observação importante: Esta chave está disponível a partir da Build 7.00.111010P. Caso seus Binários não estejam atualizados, **[clique aqui](MP%20-%20FRAME%20-%20Atualiza%C3%A7%C3%A3o%20de%20arquivos%20do%20Protheus%2012)** e veja a documentação de apoio para baixar e atualizá-los:

Após a inserção da chave, basta efetuar o movimento novamente para que o Protheus permita e valide corretamente a operação.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
