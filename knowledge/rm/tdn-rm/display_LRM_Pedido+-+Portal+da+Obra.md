---
content_hash: 5e462f9fe9d77f2ce667faa7794e0398a8a0e47d73cb262720a04805524a0001
fetched_at: '2026-06-29T00:10:57.797163+00:00'
page_id: '599851283'
product: rm
source: tdn-rm
title: Pedido - Portal da Obra
type: documentation
url: https://tdn.totvs.com/display/LRM/Pedido+-+Portal+da+Obra
version: 25
---

### Pedido

Para a funcionalidade do Pedido no TOTVS Obras e Projetos foram desenvolvidas telas Web para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.   
Foram desenvolvidas todos os cadastros e visões de anexo para o Pedido da seguinte forma:

* Tela com a listagem dos pedidos salvos na base de dados com opções de Fazer Novo Pedido, Visualizar, Editar e Excluir;

* Ao fazer novo pedido é apresentando uma tela para preenchimento dos campos.

* Ao editar o pedido é apresentado uma tela detalhada contendo:
  + Item de Pedido (serão apresentados os insumos que ainda possuem saldo disponível);

* + Ao expandir um item são apresentados os seguintes detalhamentos:  
    - Contratos;
    - Datas de Necessidade;
    - Datas de Entrega;
    - Preço Orçado;
    - Produtos;
      * Opção de Editar item mostrando detalhes da compra separado por Tarefa, com possibilidade de alterar a Necessidade dos mesmos;

* Ao clicar em Editar itens, é exibido uma tela com os itens do insumo, e ao clicar no itens os campos de edição são carregados

* + - Histograma;
      * 511pxRequisição;
      * Necessária;
      * Pedida;

**Informações do Pedido**

* + - Status
    - Data Requisição
    - Tipo de Requisição

**Configuração:**

* + - Utiliza Preço Orçado
    - Tipo de Movimento
    - Local de Estoque
    - Observação

Para os processos foram desenvolvidas telas Web todos os processos que envolvem o Pedido, de acordo com :

* Pedido
  + Visualizar e Editar;
  + Visualizar Movimento;
  + Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) movimento;
  + Envia pedido para  Suprimentos/Faturamento gerando 1 (um) mov. por data de entrega;
  + Excluir Pedido;

# Rateio de Produto

#
