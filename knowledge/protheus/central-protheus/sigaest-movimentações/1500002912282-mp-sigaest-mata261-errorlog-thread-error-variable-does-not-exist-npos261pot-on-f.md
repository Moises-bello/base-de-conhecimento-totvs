---
article_id: 1500002912282
category: SIGAEST - MOVIMENTAÇÕES
content_hash: de5c2cd963c6cad55668ab25f94b33f6772f02741e163b579330aa33a7dc6013
fetched_at: '2026-06-28T22:38:58.618894+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: MP - SIGAEST - MATA261 - Error.log THREAD ERROR - Variable does not exist NPOS261POT
  on F4LOCALIZ(SIGACUSB.PRX)
type: support-article
updated_at: '2021-06-08T18:14:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002912282-MP-SIGAEST-MATA261-Error-log-THREAD-ERROR-Variable-does-not-exist-NPOS261POT-on-F4LOCALIZ-SIGACUSB-PRX
---

**Dúvida**Ao apertar o botão [F4] do teclado no campo "Quantidade" dentro da rotina MATA261 - Transferência Multipla, ocorre o seguinte error.log: "*THREAD ERROR - Variable does not exist NPOS261POT on F4LOCALIZ(SIGACUSB.PRX*)"  
  
**Ambiente**Microsiga Protheus - Estoque - A partir da versão 12.1.17  
  
**Solução**

Para correção deste problema, a variável NPOS261POT foi declarada no fonte MATA261 mais atual conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008317581/mceclip0.png)

A primeira proposta de solução é aplicando o patch pontual da rotina MATA261 conforme a sua release:

**MATA261 12.1.23: [Clique aqui](https://r.totvs.io/p/1017754) | MATA261 12.1.25: [Clique aqui](https://r.totvs.io/p/1017755) | MATA261 12.1.27: [Clique aqui](https://r.totvs.io/p/1017756)**

Em caso de persistência do erro, será necessário atualizar o ambiente com o pacote acumulado do Estoque/Custos.

***Pacotes acumulados Estoque/Custos:***

12.1.27- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/960571) **|** 12.1.25- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/826640) **|** 12.1.23- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#detail/748747)

**Observação: Sempre aplicar atualizações primeiramente em ambiente de homologação.**

Após a aplicação, basta acessar à rotina e testar novamente o botão F4 no campo "Quantidade" para que consiga visualizar normalmente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
