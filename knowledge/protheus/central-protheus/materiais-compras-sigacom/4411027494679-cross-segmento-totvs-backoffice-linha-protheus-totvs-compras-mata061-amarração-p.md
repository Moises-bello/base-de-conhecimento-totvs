---
article_id: 4411027494679
category: Materiais - Compras (SIGACOM)
content_hash: ea1397c20ef5fff74a905f779dfe00bbdc0fe5625c0be9e2fd2602db9a806afc
fetched_at: '2026-06-28T22:41:11.765030+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras -  Mata061
  - Amarração Produto x Fornecedor
type: support-article
updated_at: '2025-05-30T17:36:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411027494679-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Compras-Mata061-Amarra%C3%A7%C3%A3o-Produto-x-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Qual o objetivo de cadastrar Produto x Fornecedor  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as Versões

**Solução**

Este cadastro armazena informações referentes a relação dos produtos com seus respectivos fornecedores, tais como: o histórico dos 12 últimos preços de compra, condição de pagamento firmada, datas de compra e valores, pontuação do fornecedor etc.

Estas informações são utilizadas pelo sistema Protheus para avaliação das especificações de um fornecedor para um determinado produto,  como por exemplo:

* Em Geração automática das cotações de compras,
* estas são enviadas aos fornecedores dos produtos cadastrados.
* Para controle dos produtos a serem enviados para o controle de qualidade, determinado pelos campos:
* Controle Lote (A5\_SKIPLOT) - Caso o usuário queira controlar o envio de materiais ao C.Q. pelo Skip-lote, este campo determina a freqüência de inspeção do produto de um determinado fornecedor (Skip-lote de compra) quando do recebimento do material. Exemplo: Com o Skip-lote 10, a cada 10 recebimentos deste fornecedor, 1 será direcionado ao armazém de C.Q.
* Nota (A5\_NOTA) - Nota de avaliação do fornecedor para o produto. Para este controle, cada produto também deverá possuir uma pontuação mínima para o controle de qualidade (Cadastro de Produtos).

![20211019_083744.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4411032198935/20211019_083744.gif)

Saiba mais em : <https://tdn.totvs.com/x/ikTnHg>
