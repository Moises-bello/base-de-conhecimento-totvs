---
article_id: 360061396234
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 2595dd58842f3e2e267923a7ee3c996c7edd54d801946b7eb8d97c9868c32ebe
fetched_at: '2026-06-28T22:38:58.577164+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - HELP A240LOCCQ ao tentar Requisitar um produto que está no C.Q
type: support-article
updated_at: '2021-04-28T15:45:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061396234-MP-SIGAEST-HELP-A240LOCCQ-ao-tentar-Requisitar-um-produto-que-est%C3%A1-no-C-Q
---

**Dúvida**É possível movimentar um saldo que está no armazém de CQ (Controle de Qualidade)?  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17

**Solução**Por padrão, as únicas formas de gerar saída de saldo de C.Q para um produto são por meio da rotina Baixa de C.Q (MATA175) ou através de Nota de Devolução de Compras (porém neste caso é recomendável antes fazer a Rejeição de C.Q na rotina MATA175 para o registro ficar com legenda vermelha).

Quando há tentativa de requisitar internamente o saldo que está no C.Q gerará o seguinte HELP:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103877273/mceclip0.png)

Com isso, o Protheus impedirá de requisitar via MATA240/MATA241/MATA260/MATA261.

Deve-se acessar à rotina MATA175 para conseguir baixar o saldo e levá-lo ao armazém padrão ou rejeitá-lo para fazer a devolução da compra.

**Saiba mais:**

*[MP - SIGAEST - Como efetuar Baixa do C.Q. (MATA175)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011962151)*

*[MP - SIGAEST - HELP A175LIB - MATA175 (Baixa de C.Q)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022005311)*
