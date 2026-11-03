---
content_hash: 9d7ec4d3c9bf70e049aaa8b8559460e6224448655ef3895e7ceff430f3c775f8
fetched_at: '2026-06-29T00:06:00.553946+00:00'
page_id: '196811138'
product: rm
source: tdn-rm
title: DT_Envio_Preco_Orcado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Envio_Preco_Orcado
version: 4
---

# ENVIO DO PREÇO ORÇADO (SA e SC)

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Movimento** |
| **Requisito (ISSUE):** | *PCREQ-5383* |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQL Server e Oracle* |
| **Sistema(s) operacional(is):** | *Windows* |
| **Versões/Release:** | *12.1.7* |

## Descrição

O Valor Orçado é uma informação pertinente ao TOP que deve ser enviada ao Nucleus para dar suporte ao papel do comprador da empresa, que a levará em consideração no momento de negociar produtos/serviços com fornecedores.

Ao gerar uma nova cotação, um campo de Descrição foi adicionado no processo, visando utilizá-lo para identificar melhor a cotação que esta sendo incluída.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Na **Gestão de Estoque, Compras e Faturamento**, acesse **Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento**. Configure o parâmetro a seguir:  
   04.06 - Gestão de Compras | 04.06.01 - Solicitação de Compra  
   Selecione o tipo de movimento a ser parametrizado  
   Item - Preços | Edição do Preço: **Edita**Apesar da parametrização da edição do preço estar como Edita, o valor só poderá ser alterado no Nucleus quando o usuário possuir permissão para alterar item integrado.
2. No **Construção e Projetos**, selecione um projeto e acesse **Construção e Projetos | Projetos - F6**    
   Integração | Suprimentos / Faturamento | Tipos de Mov. de Pedidos  
   Selecione o tipo de movimento que será utilizado para Solicitação de Compras

## Procedimento para Utilização

* **Envio do Preço Orçado**

1. No Construção e Projetos, selecione um projeto
2. Acesse Planejamento | Geração de Pedidos e inclua um novo
3. Após incluir uma nova solicitação, edite o pedido e marque a opção "Utiliza Preço Orçado"
4. Envie o pedido para Suprimento / Faturamento
5. No Gestão de Estoque, Compras e Faturamento
6. Acesse Compras | Solicitação de Compras
7. Edite a solicitação de compras incluída pelo TOP e verifique o "Preço Unitário"

* **Campo Descrição na Cotação**

1. No Gestão de Estoque, Compras e Faturamento
2. Acesse Compras | Cotação
3. Inclua uma nova cotação
4. Nos dados iniciais da cotação, um campo Descrição foi incluído.
5. Na visão o campo Descrição é exibido.
6. Ao gerar ordem de compra desta cotação, o campo Descrição será exportado para o campo Histórico.
