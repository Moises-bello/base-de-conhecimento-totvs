---
article_id: 18564938475159
category: SIGAEST - MOVIMENTAÇÕES
content_hash: ef17c7ca66b19183d8a55d69e9a8c529875e09ee71846112870ca7d1ef55a4f4
fetched_at: '2026-06-28T22:38:55.722919+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA105/MATA106 Não
  gera Solicitação de Compra quando produto importado (B1_IMPORT=S)
type: support-article
updated_at: '2025-03-12T12:27:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18564938475159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA105-MATA106-N%C3%A3o-gera-Solicita%C3%A7%C3%A3o-de-Compra-quando-produto-importado-B1-IMPORT-S
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18564894110743) Tempo aproximado para leitura: **00:03:15 min** **Dúvida**

Produtos com o campo **Produto Importado (B1\_IMPORT)** igual a **Sim** quando geramos a pre-requisição (MATA106) e o mesmo não tem saldo, não gera automaticamente uma Solicitação de Compras, qual o motivo?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões

**Solução**

Quando o produto está configurado como Importado (B1\_IMPORT=S) e o parâmetro F12 "Gera Sol. Compras/Aut. Entrega" igual a Sim na rotina Gera Pré-Requisição (MATA106), gera a ***Solicitação de Importação (****EICSI400******)*** no módulo SIGAEIC caso o saldo em estoque não seja suficiente para atender a necessidade.

Veja um passo a passo abaixo de exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18565818533271)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18565818537623)

***Observações importantes:*** Caso exibir o assistente "OBRIGAT", o mesmo é apresentado devido o campo **Cod.Unid.Req (W0\_\_CC)** do cabeçalho da SI que não foi preenchido, sendo seu preenchimento obrigatório. Para o correto funcionamento informe no parâmetro **MV\_CCUNREQ** o código da unidade requisitante.

O cadastro pode ser realizado através da rotina ***Unidade Requisitante (EICA030)***.

**Passo a passo abaixo:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18565818542615)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18565818548119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18565818561431)

Posteriormente, pode acontecer da rotina solicitar outro campo obrigatório: a de Comprador

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29710386164119)

Caso ocorra, significa que no seu Cadastro de Compradores (COMA087) não há um comprador com o usuário logado na Pré-Requisição (MATA106), necessitando que este usuário logado seja um Comprador para seguir com o Processo.

No Modulo 02 - Compras, acesse ao menu ***Atualizações -> Administração de Compras -> Compradores*** (COMA087) e efetue o Cadastro do Comprador, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29710339075223)

Posteriormente, o usuário que for comprador, ao logar na rotina da Pré-Requisição e assim o fazer, não ocorrerá mais o erro. Mas é importante esclarecer que para o produto importado (B1\_IMPORT) gerará Solicitação de Importação, e não uma Solicitação de Compras.

***Saiba Mais:***

*[Clique aqui e veja mais artigos sobre MOVIMENTAÇÕES no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)*
