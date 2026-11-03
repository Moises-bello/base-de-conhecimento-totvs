---
article_id: 360060831754
category: Financeiro - Contas a Pagar
content_hash: 24b1f343aa09db939e2a1229557c8ab756938dfa650322ebae217b6e51f27cb2
fetched_at: '2026-06-28T22:38:08.276749+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA100 - Exclusão da
  movimentação bancaria apresenta a mensagem HELP FA100BAIXA
type: support-article
updated_at: '2021-12-23T18:35:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060831754-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Exclus%C3%A3o-da-movimenta%C3%A7%C3%A3o-bancaria-apresenta-a-mensagem-HELP-FA100BAIXA
---

**Ocorrência:**No módulo Financeiro FINA100, ao tentar excluir o movimento Bancário a mensagem HELP FA100BAIXA

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103207233/mceclip1.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA100  - Todas as versões

**Causa**Este erro é apresentado quando há a tentativa de excluir um movimento gerado por outra rotina.

**Solução**Nesse caso precisa identificar qual rotina esse movimento foi gerado para realizar a exclusão. Caso não saiba onde foi gerada, na  **SE5**tem um campo chamado  **E5\_ORIGEM,** através desse campo será possível identificar qual rotina o movimento foi gerado e com isso podendo realizar o estorno através da rotina que a originou. 

**Observação**

1) Em caso de transferência não é possível fazer um Cancelamento/Exclusão, nesse caso se faz necessário realizar outra transferência ( E5\_TIPODOC = TR , E5\_MOEDA = TB,  CC, CD, CH, DOC, FI e R$)  
2) Os Títulos de Adiantamento devem ser excluído por sua origem, gerando assim um movimento  
contrário na SE5 e na FINA100 aparecerá os dois lançamentos  ( Credito e um Debito ).

**Saiba Mais-**[MP - SIGAFIN - FINA100 - Contabilização on-line de cancelamento de movimentos a receber e a pagar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053506373-MP-SIGAFIN-FINA100-Contabiliza%C3%A7%C3%A3o-on-line-de-cancelamento-de-movimentos-a-receber-e-a-pagar-?source=search)
