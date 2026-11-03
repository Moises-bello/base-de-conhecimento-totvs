---
content_hash: 2fec3a6bfa76baa56bc1b80284ce86cf8597fc5efc597c10f2dd6e3602c04219
fetched_at: '2026-06-29T00:09:26.099765+00:00'
page_id: '423938259'
product: rm
source: tdn-rm
title: Classificação dos Tipos de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938259
version: 3
---

**Estoque**

* Ajuste de Estoque;
* Requisição de Materiais;
* Baixa de Estoque;
* Transferências.

Tipo de Movimento classificado como 'Transferências (Gestão de Estoque)' deve ter as seguintes configurações: Tipo de Movimento do Grupo '3'.

* Inventário;
* Produção.

Tipo de Movimento classificado como 'Produção (Gestão de Estoque)' deve ter as seguintes configurações:

* Gerar Ordem de produção no RM Factor (Produção);
* ou Entrada de Produtos Acabados a Partir do RM Factor (Produção).

**Controle de EPI**  
  
Tipo de Movimento classificado como 'Controle de EPI (Gestão de Estoque)' deve ter as seguintes configurações:

* Tipo de Movimento do Grupo '1';
* ou '2'. Controle de EPI diferente de 'Não Integrado' (Recursos Humanos).

**Estoque de Terceiros**

* Compras;
* Solicitação de Compras.

Tipo de Movimento classificado como 'Solicitação de Compras (Gestão Compras)' deve ter as seguintes configurações:

* Tipo de Movimento do Grupo '1.1';
* Tipo de Movimento de Compras igual 'Solicitação de Compras' (Compra/Venda - Outros);
* Cotação.

**Ordem de Compras**  
  
Tipo de Movimento classificado como 'Ordem de Compra (Gestão Compras)' deve ter as seguintes configurações:

* Tipo de Movimento de Compra igual a 'Pedido de Compras' (Compra/Venda - Outros);
* Recebimento de Materiais.

**Importação**

* Aquisição de Serviços;
* Devolução de Compras.

Tipo de Movimento classificado como 'Devolução de Compra (Gestão Compras)' deve ter as seguintes configurações:

* Tipo de Movimento do Grupo '2.2';
* Saldo Atual igual "Diminui" (Estoque - Estoque 1/3) Motivo de Referencia igual "Devolução de Compras";
* ou "Cópia NF-e de Ajuste - Estorno de Compra" (Mov - Outros Dados).

**Vendas**

* Pedido de venda;
* Faturamento;
* Exportação;
* Devolução.

Tipo de Movimento classificado como "Devolução de Venda (Vendas)" deve ter as seguintes configurações:

* Tipo de Movimento do Grupo "1.2";
* Saldo Atual igual "Aumenta" (Estoque - Estoque 1/3);
* Motivo de Referencia igual a "Devolução de Venda";
* ou "Cópia NF-e de Ajuste - Estorno de Venda" (Mov - Outros Dados).

**Outras Movimentações**

* Controle de Imobilizado.

Tipo de Movimento classificado como 'Controle de Imobilizado' deve ter as seguintes configurações:

* Tipo de Movimento do Grupo "1";
* ou "2" ou "3" Integrado RM Bonum (Patrimônio).
