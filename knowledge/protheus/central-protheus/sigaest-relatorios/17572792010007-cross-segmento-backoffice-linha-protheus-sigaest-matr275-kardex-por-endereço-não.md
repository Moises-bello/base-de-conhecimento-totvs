---
article_id: 17572792010007
category: SIGAEST - RELATORIOS
content_hash: 938e89ddfb3124bd5dafad1c9364c0c9b97a1397fb41dd6f4efcf21a215a0d36
fetched_at: '2026-06-28T22:39:06.099723+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR275 - Kardex por
  endereço não apresenta saldo e movimentações de produto
type: support-article
updated_at: '2023-09-18T12:35:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17572792010007-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR275-Kardex-por-endere%C3%A7o-n%C3%A3o-apresenta-saldo-e-movimenta%C3%A7%C3%B5es-de-produto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17572755185303) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao emitir o relatório ***Kardex por Endereço (MATR275)***, mesmo para um produto que temos saldo e movimentações, o relatório não apresenta os dados? O que devemos avaliar?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17572858036119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17572964879767)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17572925207959)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Primeiramente para esse cenário, sempre avaliar se as parametrizações do relatório estão com os intervalos corretos.

É importante avaliar se utiliza caracteres especiais no cadastro de produtos, por exemplo hífen ( - ), nesse caso, deve informar no campo código do produto entre aspas simples. Veja o resultado abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17573194359959)

***-Após esse ajuste o saldo e as movimentações são apresentados corretamente:***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17573228775703)

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre RELATÓRIOS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)
