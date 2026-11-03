---
article_id: 20447098244887
category: LEGAIS - BLOCO H/MATR460
content_hash: 435be68d3f3992b09a8d5021fa28695a1e647fdd3f6cba65aabfd4d086a3f782
fetched_at: '2026-06-28T22:42:15.165265+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR460 - Saldo próprio
  negativo com controle de poder de terceiro
type: support-article
updated_at: '2024-01-09T20:42:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20447098244887-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Saldo-pr%C3%B3prio-negativo-com-controle-de-poder-de-terceiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20447044295959) Tempo aproximado para leitura: **00:02:25min** **Dúvida**O Relatório **MATR460** está trazendo um saldo negativo em estoque próprio, quando temos o seguinte cenário:

- Produto sem saldo em estoque;

- Recebo uma remessa (MATA103 - Documento de Entrada) **DE** terceiros em meu poder (Configuração da TES - F4\_PODER3 = Remessa e F4\_ESTOQUE = Sim)

- Após isso envio uma nova remessa (MATA410 - Pedido de Venda) de um produto próprio para ficar **EM**  posse de terceiros (Configuração da TES - F4\_PODER3 = Remessa e F4\_ESTOQUE = Sim);

- Após esse cenário ao emitir o MATR460 o saldo em estoque próprio fica negativo.

Segue abaixo print do resultado do relatório após essas movimentações:

Saldo estoque próprio:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447044299287)

Saldo **EM** Terceiros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447044301975)

Saldo **DE** Terceiros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447044309399)

Gostaríamos de esclarecer que o comportamento mencionado não é considerado um erro, mas sim um conceito do relatório **MATR460**. Ao realizar um Pedido de Venda e enviar estoque próprio para controle **EM** terceiros, atualizando o estoque (F4\_ESTOQUE = SIM), o sistema não pode deduzir o saldo recebido **DE** terceiros, pois isso resultaria em uma inconsistência no saldo de terceiros no Bloco H. Portanto, com a configuração para atualizar o estoque, o sistema irá apresentar um "Saldo Próprio" negativo, uma vez que não há saldo próprio para esse produto.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões]  
  
**Solução**

Para esse cenário que não existe saldo próprio uma **sugestão** de uso seria:

- Produto sem saldo em estoque;

- Recebo uma remessa (MATA103 - Documento de Entrada) **DE** terceiros em meu poder (Configuração da TES - F4\_PODER3 = Remessa e F4\_ESTOQUE = Sim)

- Após isso envio uma nova remessa (MATA410 - Pedido de Venda) de um produto próprio para ficar **EM**  posse de terceiros (Configuração da TES - F4\_PODER3 = Remessa e **F4\_ESTOQUE = Não**);

Dessa maneira o relatório dispõe do [MV\_SDTESN3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060289014-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR460-Valida%C3%A7%C3%A3o-do-par%C3%A2metro-MV-SDTESN3) que com o conteúdo igual a 2 pode atender a a sua expectativa de resultado do relatório, segue print do relatório com o MV\_SDTESN3 e as movimentações descritas acima:

Saldo estoque próprio

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447643867287)

Saldo **EM** Terceiros

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447651785751)

Saldo **DE** Terceiros:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/20447643891991)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H/MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538741-LEGAIS-BLOCO-H-MATR460)*
