---
article_id: 6299921393431
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: fc63aded6ccdec2ea7ff53f8706e258875732d6e6f2ad987f0d6df7b8eeb1e12
fetched_at: '2026-06-28T22:38:38.559864+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Limite inferior/superior
  com TES que não gera duplicata
type: support-article
updated_at: '2022-05-24T17:14:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6299921393431-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Limite-inferior-superior-com-TES-que-n%C3%A3o-gera-duplicata
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:45 min** **Dúvida**Por que em uma remessa do Contrato de Parceria que tenha sido fornecida uma TES que não gere financeiro, é checado a questão do limite inferior/superior na remessa e não na aprovação do contrato de parceria/pedido de venda?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Limite inferior/superior com TES que não gera duplicata - Todas as versões  
  
**Solução**Na inclusão de um pedido de vendas/contrato de parceria, o limite inferior/superior da condição de pagamento não é checado por não envolver nesta hora, o pagamento da operação.

É possível na **inclusão**, por exemplo, incluir 2 produtos que somados dão R$80 e o Limite Inferior da Condição de Pagamento ser R$100, como no exemplo a seguir:

        ADA\_CONDPG: Limite inferior de R$100 (E4\_INFER: 100)

         ADB\_CODPRO: 1  
         ADB\_QUANT: 2

         ADB\_PRCVEN: 40

         ADB\_TOTAL: 80

         ADB\_TES: (Preenchida com uma TES que não gere duplicata e atualize o estoque)

         ADB\_TESCOB: (Preenchida com uma TES que gere duplicata e não atualize o estoque)

Porém, para **aprovar** ou **faturar** os itens parcialmente ou completamente, a soma dos itens tem de passar da validação dos limites da condição de pagamento, fazendo necessário que sejam atendidas no momento antes do faturamento/geração de remessa.

Empresas que realizam o faturamento parcial, na hora da remessa não enviam todos os itens, por consequência, não atingem o valor mínimo/máximo para que a operação possa acontecer de acordo com os limites da condição de pagamento.

Nestes casos basta mudar a condição de pagamento para uma condição que contenha os limites adequados que atendam a operação do momento necessária, ou alterar o parâmetro:  
**MV\_CNDPLIM = '2'**.

Exemplo de um pedido incluído e aprovado respeitando os limites da condição de pagamento :

Limite inferior no cabeçalho dentro da condição de pagamento: **500**

Item 1 - Quantidade 10 - Preço 100 - Total 1000

Item 2 - Quantidade 5 - Preço 5 - Total 25

**Soma: 1025**

[**STATUS APROVADO**, POIS A SOMA ATENDE OS LIMITES DA CONDIÇÃO DE PAGAMENTO]

Ao tentar gerar remessa parcial, para faturar todas as quantidades apenas do Item 2, ficaria deste modo:

Limite inferior no cabeçalho dentro da condição de pagamento: **500**

Item 1 - Apagado

Item 2 - Quantidade 6 - Preço 5 - Total 25

**Soma: 25**

***HELP: LJLIMINFER*** (apareceria na tela)

**[STATUS NEGADO**, POIS A SOMA NÃO ATENDE OS LIMITES DA CONDIÇÃO DE PAGAMENTO]

Com o parâmetro **MV\_CNDPLIM = '2 = Somente SigaLoja'** ativo, é possível gerar a remessa:

Limite inferior no cabeçalho dentro da condição de pagamento: **500**

Item 1 - Apagado

Item 2 - Quantidade 6 - Preço 5 - Total 25

**Soma: 25**

[**STATUS** APROVADO, POIS O PARÂMETRO = '2' FAZ COM QUE NÃO OCORRA A VALIDAÇÃO DOS LIMITES DA CONDIÇÃO DE PAGAMENTO]

Por mais que alguma TES envolvida no processo não gere duplicatas, o sistema valida a informação diretamente dos limites dentro da condição de pagamento escolhida, por isso ele não deixa passar os limites mesmo a TES não controlando financeiro no momento do processo.

**Documentações relacionadas:**

[Cross Segmentos - TOTVS Backoffice (Linha Protheus) - FAT - HELP LJLIMINFER Limite inferior e superior na condição de pagamento](Cross%20Segmentos%20-%20TOTVS%20Backoffice%20(Linha%20Protheus)%20-%20FAT%20-%20HELP%20LJLIMINFER%20Limite%20inferior%20e%20superior%20na%20condi%C3%A7%C3%A3o%20de%20pagamento)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Contrato de Parceria](Cross%20Segmento%20-%20TOTVS%20Backoffice%20(Linha%20Protheus)%20-%20SIGAFAT%20-%20Contrato%20de%20Parceria)

[Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-Fata400](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403785079831-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-Fata400)
