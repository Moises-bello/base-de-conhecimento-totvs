---
article_id: 29188904962327
category: Materiais - Compras (SIGACOM)
content_hash: 053eae8d3aa46f25e254bcd2d0037e22836bee96d39b711287a22d9bf5a3709a
fetched_at: '2026-06-28T22:41:11.852443+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Exclusão de Pedido de compra limpa
  campos C1_FORNECE e C1_LOJA
type: support-article
updated_at: '2025-01-13T18:33:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29188904962327-Cross-Segmentos-Backoffice-Protheus-Exclus%C3%A3o-de-Pedido-de-compra-limpa-campos-C1-FORNECE-e-C1-LOJA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29188952629015) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao excluir um Pedido de Compra que está vinculado a uma Solicitação de Compra é limpado os campos C1\_FORNECE e C1\_LOJA que foram preenchidos pelo usuário durante a inclusão da Solicitação de Compras.

**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Versão 12

**Solução**

* Criado campo de controle interno chamado C1\_FLAGSC que determina se o campo C1\_FORNECE e C1\_LOJA foi preenchido pelo sistema durante o vínculo da solicitação ao Pedido de Compra,caso o campo tenha sido preenchido pelo sistema, é limpado seu conteúdo ao excluir o pedido de compra, caso tenha sido preenchido pelo usuário permanecerá com o dado inserido.
* Atualização de dicionário estará disponível automaticamente a partir do release 12.1.2510, porém poderá ser criado através da aplicação da próxima expedição contínua de compras, posterior a posterior a Dez/24 - Pacote de atualização
* Executar o UPDDISTR com o dicionário diferencial - SDFBRA.txt
* Aplicar o pacote com os fontes para atualização do RPO.

***Saiba Mais:***

[Exclusão de Pedido de compra limpa campo C1\_FORNECE/C1\_LOJA](https://tdn.totvs.com/pages/releaseview.action?pageId=899199586)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
