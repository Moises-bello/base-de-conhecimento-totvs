---
content_hash: 2e0dd71c579dc5c54508ee1002b6a2b6c60dd6c70f2f2de9738cc23cb2932c6c
fetched_at: '2026-06-29T00:06:01.926743+00:00'
page_id: '198941769'
product: rm
source: tdn-rm
title: Envio de Preço Orçado SA e SC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=198941769
version: 5
---

O Preço Orçado é uma informação pertinente ao TOP que deve ser enviada ao TOTVS Gestão de Estoque, Compras e Faturamento para dar suporte ao comprador.   
Esse preço orçado é levado em consideração no momento de negociar produtos/serviços com fornecedores.  
O Tipo de Movimento utilizado pelo TOP para geração da Solicitação de Compra no TOTVS Gestão de Estoque, Compras e Faturamento deve estar parametrizado para permitir a edição do preço unitário.  
As parametrizações já realizadas para integração com o TOP devem ser mantidas.

***Importante!*** Apesar da parametrização da edição do preço estar como Edita, o valor só poderá ser alterado no TOTVS Gestão de Estoque, Compras e Faturamento quando o usuário possuir permissão para alterar item integrado.

Para que o Valor Orçado do TOP seja enviado para o Preço Unitário do Movimento, é necessário marcar a opção “Utiliza Preço Orçado” da tela de Pedido de Material. Importante ressaltar que essa opção não é um parâmetro e deve ser marcada em todos os pedidos que se deseje enviar o Valor Orçado para o Preço Unitário do Movimento.

**Detalhamento do Processo**

Ao selecionar o Pedido de Material e comandar a geração do Pedido através da opção “Enviar pedido para Suprimento/Faturamento...”, deve-se carregar os itens de movimento correspondentes aos itens de Pedido do TOP e o campo de Preço Unitário de cada item deve ser preenchido com o valor orçado, encontrado no item de pedido do TOP (anexo Item de Pedido de Material – campo “Preço Unit. Orçado”).   
Esse valor recebido pelo TOTVS Gestão de Estoque, Compras e Faturamento poderá ser visualizado no item de movimento, campo “Preço Unitário” e poderá ser usado como referência quando da geração de cotação ou mesmo faturamento da Solicitação de Compra para Ordem de Compra.

**Campos e Parâmetros**

**TCCOTACAO.DESCRICAO (novo campo):**Com o intuído de identificar melhor a cotação que foi gerada, um novo campo será inserido no wizard de cotação e o mesmo será exibido na visão da cotação.

| Detalhes do Campo | | | | |
| --- | --- | --- | --- | --- |
| **Tabela** | **Nome** | **Tipo** | **Tamanho** | **Valor Default** |
| TCCOTACAO | DESCRICAO | VARCHAR | 255 | NULL |

**Parametrização Necessária:**Acessar o módulo de Materiais | Ambiente | Parâmetros do TOTVS Gestão de Estoque, Compras e Faturamento | Acessar o tipo de movimento de SC | Na etapa Item - Preços | Edição do Preço = Edita | Etapa Projeto, parametrizar a integração com TOP.

**Parametrizar Solicitação de Compras no TOP:**Acessar o TOP, aba Projetos| Construção e Projetos | Projetos - F6 | Etapa Integração | Tipo de MOV. de Pedidos. | Informe o tipo de movimento de Solicitação de Compras parametrizado anteriormente | Clique em OK.
