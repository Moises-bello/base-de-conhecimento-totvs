---
article_id: 35778267457303
category: Materiais - Compras (SIGACOM)
content_hash: c6e0d846122365edf0182dbde297a28c5dd865c331f4e1e722b55149b7b7604d
fetched_at: '2026-06-28T22:41:21.765493+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como visualizar
  as Solicitações de Compra de todas as filiais no Novo Fluxo de Compra?
type: support-article
updated_at: '2025-12-31T13:58:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35778267457303-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-visualizar-as-Solicita%C3%A7%C3%B5es-de-Compra-de-todas-as-filiais-no-Novo-Fluxo-de-Compra
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35778267426071) Tempo aproximado para leitura: **00:04:00 min**  
  
**Dúvida**  
Ao acessar a aba de Necessidade de Compras na rotina do Novo Fluxo de Compras, o sistema lista apenas as Solicitações de Compra incluídas na filial logada. Como exibir as Solicitações de Compra de todas as filiais na tela da Necessidade de Compras?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2310  
  
**Solução**  
No Novo Fluxo de Compras não existe a possibilidade de mostrar as Solicitações de Compra de todas as filiais. Por comportamento padrão da rotina, serão exibidas somente as Solicitações de Compra da filial que está logado no Protheus. Para visualizar o registro das demais filiais, é necessário realizar a troca da filial em que está logada. Portanto, não existe a possibilidade de usar um filtro Multifiliais no Produto Padrão que permita visualizar as solicitações de todas as filiais.

Porém uma alternativa seria a Compra Centralizada que é explicada abaixo.

Dentro da tela de **Necessidade de Compra**, existe o botão **"Compra centralizada"**, onde é possível realizar a centralização de solicitações de compras para uma única filial.

Por exemplo: Iremos trocar todos os notebooks das filiais, ao invés de iniciar a cotação em cada filial, nós centralizaremos todas as solicitações em uma única filial para poder cotar de uma só vez, posteriormente gerando pedidos de compra para cada uma das filiais das solicitações de compra.  
Na tela de compra centralizada, temos duas listas, sendo elas:  
(Esquerda) - Solicitações de todas as filiais - menos a logada/centralizadora  
(Direita) - Solicitações selecionadas para serem centralizadas/transferidas para filial logada/centralizadora.  
  
As solicitações que foram transferidas, são zeradas na filial de origem e ficam com status roxo.

Já as novas solicitações criadas na filial centralizadora, ficam com status disponível para cotação, passando a aparecer na listagem de necessidade de compra.

![](https://tdn.totvs.com.br/download/attachments/680260500/image-2024-5-20_14-18-7.png?version=1&modificationDate=1716225488883&api=v2)  
  
Todo o processo de cotação com itens centralizado é igual, com apenas **duas**mudanças do processo comum:  
  
1) Não é possível inserir uma quantidade disponível diferente da quantidade solicitada.

2) É possível configurar a geração dos pedidos de compra de acordo com o parâmetro MV\_COTFIAP, sendo:  
**MV\_COTFIAP = E → Os pedidos serão gerados conforme filial de entrega na solicitação de compra, ou seja:**

Filial Solicitação de Compra: D MG 02

Filial Centralizadora: D MG 01

Filial do pedido de compra: D MG 02  
Filial de entrega do pedido de compra: D MG 02

**MV\_COTFIAP = C → Os pedidos serão gerados na filial centralizadora com filial de entrega de acordo com a origem da solicitação de compra.**

Filial Solicitação de Compra: D MG 02

Filial Centralizadora: D MG 01

Filial do pedido de compra: D MG 01  
Filial de entrega do pedido de compra: D MG 02

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
