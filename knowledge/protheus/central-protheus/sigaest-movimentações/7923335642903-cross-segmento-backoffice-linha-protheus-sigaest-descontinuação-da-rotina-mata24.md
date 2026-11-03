---
article_id: 7923335642903
category: SIGAEST - MOVIMENTAÇÕES
content_hash: bfcc75e96ebd93c9da76b4f93938ba0bf3b4838de688d3bc83f952847ac07192
fetched_at: '2026-06-28T22:38:54.226579+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Descontinuação da
  rotina MATA240
type: support-article
updated_at: '2024-10-24T14:42:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7923335642903-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Descontinua%C3%A7%C3%A3o-da-rotina-MATA240
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16942785937559) Tempo aproximado para leitura: **00:04:55 min** **Dúvida**Com a rotina MATA240 descontinuada, quais as mudanças/impactos para a rotina MATA241 ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**Como sabemos a rotina MATA240 foi descontinuada, e com isso vamos precisar substituir essa rotina usando a MATA241.

**Funcionalidade rotina descontinuada:**

A rotina de Movimentação Simples permite o lançamento das movimentações internas de materiais, na forma de requisições ou devoluções. Estes procedimentos atualizam os saldos físico e financeiro dos produtos, sendo um item para cada documento criado.

**Funcionalidade rotina substituta:**

A rotina de Movimentação Múltipla permite o lançamento de várias movimentações internas no mesmo documento agilizando a operação de digitação dos movimentos a serem realizados e que pertencem a um mesmo contexto.

**Diferenças e semelhanças entre as rotinas:**

**- Diferença**

* A rotina MATA241 permite lançar várias movimentações internas em um único documento enquanto a rotina MATA240 permite o lançamento de apenas uma movimentação por vez;
* Permite adicionar campos na getdados através do ponto de entrada MTA241CPO;
* Permite selecionar estrutura como base para preenchimento automático de produtos a serem requisitados através da opção Outras Ações > 1o.Nivel;
* A rotina MATA241 foi adaptada para permitir efetuar o estorno das movimentações por Documento e também por Item para que ofereça a mesma funcionalidade de estorno da rotina MATA240.

**- Semelhança**

* A rotina MATA241 está preparada para execução via rotina automática assim como a rotina MATA240;  
  **Importante:** A funcionalidade de execução automática do programa MATA240 será adaptada e continuará funcionando mesmo com a rotina descontinuada
* Ambas rotinas estão preparadas para realizar a integração via EAI sendo que o adapter da rotina MATA241 utiliza a mensagem StockTurnover e o adapter da rotina MATA240 utiliza a mensagem MovementsInternal;
* Ambas rotinas realizam requisições e devoluções de material tanto normais (para consumo) quanto para Ordens de Produção.

**Controle de Numeração:**

A rotina MATA240 no Padrão não tinha obrigatoriedade de informar o número do documento, inclusive gerava movimentação na tabela SD3 com o campo D3\_DOC em branco caso não fosse informado, desta maneira não existia uma regra de sequencia de numeração.

Já a rotina MATA241, por definição,  obriga que seja informado um número de documento e usa a função NEXTNUMERO para controle de sequencia para o campo 'cDocumento' que será gravado na tabela SD3 no campo D3\_DOC, portanto qualquer regra que seja criada no dicionário no campo D3\_DOC não afetará o campo de documento da rotina MATA241

A função NEXTNUMERO ([Clique aqui para maiores informações](https://tdn.totvs.com/pages/releaseview.action?pageId=6814928)) usa recursos para coletar o maior número na SD3 e sugerir o próximo.

**Importante:**

A movimentação com caractere especial no documento, como por exemplo: '[', pode interferir na busca de sequencias pela função NEXTNUMERO, pois o caractere '[' encontra-se classificado na tabela ASCII após as letras maiúsculas e antes das letras minúsculas, portanto no fim da classificação e a próxima sequencia numérica valida para o campo com tamanho de 6 é 000001 e enquanto existir este D3\_DOC = '[' o controle de numeração irá trazer o próximo 000001.

Considerando que o documento '[' não é um dado correto e nem pode ser considerado como um número de documento, a melhor opção é atualizar este documento com um número valido e a sequencia voltará a funcionar.

|  |
| --- |
| **Sabendo disso, quando no ambiente existe caractere especial no campo D3\_DOC, a função NEXTNUMERO não consegue seguir a sequencia correta de numeração do campo, buscando um número já existente.** |

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
