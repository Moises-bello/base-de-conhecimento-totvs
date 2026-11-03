---
article_id: 35795110933271
category: Materiais - Compras (SIGACOM)
content_hash: 7f8e9a97489c9f3881c9b155c90385ea11c4954d0e65f3bc6bc04e15b3579505
fetched_at: '2026-06-28T22:41:21.710693+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - NFC - Como consultar
  o Histórico de Compras no Novo Fluxo de Compras?
type: support-article
updated_at: '2025-11-17T21:17:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35795110933271-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-NFC-Como-consultar-o-Hist%C3%B3rico-de-Compras-no-Novo-Fluxo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35795094992919) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como é possível consultar informações das últimas compras do Histórico de Compras no Novo Fluxo?  
  
**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Protheus Release 12.1.2510  
  
**Solução**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35795094993047)

***Atenção A funcionalidade do Histórico de Compras está em fase piloto disponível somente na release 12.1.2510***

A rotina de **Histórico de Compras** tem como objetivo centralizar as informações relacionadas ao processo de compras. A ferramenta proporciona uma visualização mais clara dos pedidos realizados, entregues e de dados específicos sobre produtos ou fornecedores, facilitando o acompanhamento e a gestão de compras.

A visualização do Histórico de Compras pode ser visualizada em relação a:

* **Produto**: Permite acompanhar o histórico de compras de produtos específicos.
* **Fornecedor**: Facilita a visualização dos pedidos relacionados a fornecedores específicos

![](https://tdn.totvs.com.br/download/attachments/680260500/historico_compras_intro.gif?version=1&modificationDate=1741628017083&api=v2)

* **Produtos:**A aba Histórico de Compras - Produtos oferece uma visualização detalhada dos processos do Pedido de Compras relacionados ao produto selecionado, permitindo um acompanhamento completo e das etapas de:  
    
  ![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-3-11_13-55-29.png?version=1&modificationDate=1741712130023&api=v2)  
    
  **Detalhamento:**
  + **Quantidade Disponível**: Estoque atual do produto no armazém (campo: `B2_QATU`)
  + **Quantidade de Entrada Prevista**: Quantidade de produto com entrada prevista no estoque (campo: `B2_SALPEDI`).
  + **Último Preço de Compra**: Valor do último preço de compra do produto (campo: `B1_UPRC`).
  + **Última Data de Compra**: Data da última compra registrada do produto (campo: `B2_USAI`).
  + **Maior Quantidade Comprada**: Maior quantidade adquirido em um único pedido de compra.

**1. Solicitações de Compra:**

Serão listadas as solicitações que estiverem parcialmente atendidas (C1\_QUJE > 0).

*Regra para listagem de SC*

**Possuírem quantidade ainda pendente em pedido** (`C1_QUJE > 0`);

**Flag de aprovação** esteja como *“Liberado”* ou em branco;

**Tipo de Solicitação** seja diferente de **2** (*Licitações*);

**Origem da SC**: A Solicitação deve ter sido gerada diretamente pelo módulo de **Solicitação de Compras**. (SCs originadas pelo módulo de Gestão de Contratos não serão consideradas na listagem.)

**2. Cotações:**

Serão listadas as cotações disponíveis para consulta.

*Regra para a listagem de Cotações*

**Preço Unitário**: O valor unitário do item deve ser maior que zero.

**3. Pedidos de Compra em Aberto:**

Serão listados os pedidos de compra em aberto e disponíveis para consulta.

*Regra para a listagem de PCs em Aberto*

**Quantidade entregue** menor ou igual à **quantidade pedida**;

**Campo de eliminação de resíduo** deve estar vazio;

**Status de aprovação** do pedido **não pode estar como "Bloqueado"**.

**4. Pedidos de Compra Entregues:**

Serão listados os pedidos de compra entregues disponíveis para consulta.

*Regra para a listagem de PCs Entregues*

**Tipo de Documento**: *N* — Nota Fiscal.

* **Fornecedores:**A aba Histórico de Compras - Fornecedores oferece uma visualização detalhada das informações de entrega e fornecimento relacionados ao fornecedor selecionado:  
    
  ![](https://tdn.totvs.com.br/download/attachments/680260500/image-2025-3-11_14-16-39.png?version=1&modificationDate=1741713399737&api=v2)  
    
  **Detalhamento:**
  + **Primeira Compra**: Data da primeira compra realizada com o fornecedor (`A2_PRICOM`).
  + **Última Compra**: Data da compra mais recente realizada com o fornecedor (`A2_ULTCOM`).
  + **Maior Atraso (dias)**: Maior número de dias de atraso no pagamento ao fornecedor - Atualizado pela movimentação de títulos (`A2_MATR`).
  + **Nota do Fornecedor**: Maior avaliação atribuída ao fornecedor com relação ao produto fornecido (Produto x Fornecedor)

**1. Produtos Fornecidos:**  
  
Serão listadas os produtos fornecidos pelo fornecedor disponíveis para consulta.

**2. Pedidos de Compra em atraso:**  
Serão listados os pedidos de compra em atraso disponíveis para consulta.

*Regra para a listagem de PCs em Atraso*

* **Quantidade entregue** menor ou igual à **quantidade pedida**;
* **Campo de eliminação de resíduo** deve estar vazio;
* **Status de aprovação** do pedido **não pode estar como "Bloqueado"**.
* **Data de Entrega**: A data de entrega deve ser anterior à data atual

**3. Pedidos de Compra em aberto:**

Serão listados os pedidos de compra em aberto disponíveis para consulta.

*Regra para a listagem de PCs em Aberto*

* **Quantidade entregue** menor ou igual à **quantidade pedida**;
* **Campo de eliminação de resíduo** deve estar vazio;
* **Status de aprovação** do pedido **não pode estar como "Bloqueado"**.

**4. Devoluções de Compras:**

Serão listados as devoluções de compra disponíveis para consulta.

***Regra para a listagem de Devoluções de Compra***

* **Tipo de Nota**: *D* — Devolução.

***Saiba Mais:***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Novo Fluxo de Compras - NFC (PGCA010)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19838751317655-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Novo-Fluxo-de-Compras-NFC-PGCA010)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
