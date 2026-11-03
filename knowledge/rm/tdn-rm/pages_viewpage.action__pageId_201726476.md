---
content_hash: c2c1567b39393efc46b79b1e804441acfff76569b523816bca7f6bb4c6be270c
fetched_at: '2026-06-29T00:06:05.704077+00:00'
page_id: '201726476'
product: rm
source: tdn-rm
title: DT_Revitalização_Consultas_Rapidas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=201726476
version: 3
---

# Revitalização Consultas Rápidas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Consultas Rápidas | *Informe o nome técnico da rotina.* |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | MovMovimentoAction | |  |  | |
| **Parâmetro(s):** | Integração Fluig |
| **Requisito (ISSUE):** | PCREQ-4516 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server, Oracle |
| **Tabelas utilizadas:** | GCONSULTAFLUIG |
| **Sistema(s) operacional(is):** | Windows 7 SP1 ou superior |
| **Versões/Release:** | 12.1.7 |

## Descrição

Tem como objetivo disponibilizar o serviços de consulta rápidas referente ao módulo de Gestão de Estoque, Compras e Faturamento do BackOffice RM. Atualmente existe este serviço em funcionamento, porém foi feita uma reformulação do mesmo, para que atenda ainda melhor as necessidades dos clientes.  
A funcionalidade será disponibilizada na versão RM 12.1.7 através do Widget de Consultas Rápidas do FLUIG.

## Desenvolvimento/Procedimento

Acesso no FLUIG, através de um Widget de Consultas Rápidas.

**Pedidos Abertos por Fornecedor**

Esta consulta disponibiliza as informações de pedidos abertos (status Pendente ou Parcialmente Recebido), orientando pesquisa por fornecedor e disponibilizando filtro por datas de emissão.

O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Nome do Fornecedor |  |
| CPF/CNPJ |  |
| Código do Fornecedor |  |
| Data de Emissão | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial |  |
| Número do Pedido |  |
| Valor em aberto |  |
| CPF/CNPJ Fornecedor |  |
| Identificador do Fornecedor |  |
| Data de Emissão do Pedido |  |
| Nome do Fornecedor |  |

**Pedidos Abertos por Cliente**

Esta consulta disponibiliza as informações de pedidos abertos (status Pendente ou Parcialmente Recebido), orientando pesquisa por cliente e disponibilizando filtro por datas de emissão.

O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Nome do Cliente |  |
| CPF/CNPJ do Cliente |  |
| Código do Cliente |  |
| Data de Emissão | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial |  |
| Número do Pedido |  |
| Valor em aberto |  |
| CPF/CNPJ Cliente |  |
| Identificador do Cliente |  |
| Data de Emissão do Pedido |  |
| Nome do Cliente |  |

**Pedidos de Compra Abertos por Produto**

Esta consulta disponibiliza as informações de pedidos abertos (status Pendente ou Parcialmente Recebido), orientando pesquisa por produto e disponibilizando filtro por datas de emissão.

O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Código do Produto |  |
| Código Reduzido do Produto |  |
| Código Auxiliar do Produto |  |
| Número do Produto no Fabricante |  |
| Descrição do Produto |  |
| Descrição Complementar do Produto |  |
| Número do Pedido |  |
| Data de Emissão | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial |  |
| Número do Pedido |  |
| Código do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Descrição do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Unidade de Medida |  |
| Quantidade em Aberto |  |
| Preço Unitário |  |
| Data de Emissão do Pedido |  |
| Data Entrega do Pedido | Esse campo pode estar no movimento ou no item de movimento, dependendo da parametrização |

**Pedidos de Venda Abertos por Produto**

Esta consulta disponibiliza as informações de pedidos abertos (status Pendente ou Parcialmente Recebido), orientando pesquisa por produto e disponibilizando filtro por datas de emissão.

O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Código do Produto |  |
| Código Reduzido do Produto |  |
| Código Auxiliar do Produto |  |
| Número do Produto no Fabricante |  |
| Descrição do Produto |  |
| Descrição Complementar do Produto |  |
| Número do Pedido |  |
| Data de Emissão | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial |  |
| Número do Pedido |  |
| Código do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Descrição do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Unidade de Medida |  |
| Quantidade em Aberto |  |
| Preço Unitário |  |
| Data de Emissão do Pedido |  |
| Data Entrega do Pedido | Esse campo pode estar no movimento ou no item de movimento, dependendo da parametrização |

**Consulta Estoque e Ressuprimento**

Esta consulta disponibiliza ao cliente as informações de saldo em estoque do Produto, juntamente com informações de ressuprimento do mesmo, como ponto de ressuprimento e saldo em pedido de compra.

O Backoffice RM permite a parametrização do nível de controle de Ressuprimento por Coligada, Filial ou Local de Estoque. A consulta será balizada por este parâmetro, consolidando os seus dados seguindo o nível definido no mesmo. Caso o cliente não utilize o módulo de ressuprimento será consolidado no nível de local de estoque.

O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Nome do Produto |  |
| Código do Produto |  |
| Código Reduzido do Produto |  |
| Código Auxiliar do Produto |  |
| Número do Produto no Fabricante |  |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial | Campo apresentado somente se nível de consolidação for igual a ‘Por Filial’ ou ‘Por Local de Estoque’ |
| Cód. Local de Estoque | Campo apresentado somente se nível de consolidação for igual a ‘Por Local de Estoque’ |
| Nome do Produto | Campo obtido a partir do campo TITMMOV.IDPRD |
| Cód. Produto |  |
| Saldo Atual |  |
| Saldo Financeiro |  |
| Custo Médio | Se o nível de consolidação for igual a ‘Por Local de Estoque’, usar TPRDLOC.CUSTOMEDIO, senão TPRDCUSTOFILIAL.CUSTOMEDIO |

**Relação de Solicitações de Compra**

 Esta consulta disponibiliza as informações de solicitações de compra, apresentando filtros por dados de produto ou de solicitação.

 O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Código do Produto |  |
| Código Reduzido do Produto |  |
| Código Auxiliar do Produto |  |
| Número do Produto no Fabricante |  |
| Descrição do Produto |  |
| Descrição Complementar do Produto |  |
| Número da Solicitação |  |
| Solicitante | Verificar qual entidade será relacionada ao campo. |
| Status | Auto-Complete com lista de status possíveis. |
| Data da Solicitação | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Cód. Filial |  |
| Número da Solicitação |  |
| Solicitante |  |
| Código do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Descrição do Produto | Campo obtido a partir do campo TITMMOV.IDPRD. |
| Unidade de Medida |  |
| Quantidade solicitada | Caso o campo QUANTIDADE seja 0, será exibido o campo QUANTIDADEORIGINAL |
| Status |  |
| Data da Solicitação |  |

**Relação de Cotações**

Esta consulta disponibiliza as informações de cotações realizadas, apresentando filtros por dados de produto, fornecedor, cotação e datas de abertura.

 O usuário tem opção de filtrar os dados pelos seguintes campos:

|  |  |
| --- | --- |
| **Filtro Fluig** | **Observação** |
| Código do Produto |  |
| Descrição do Produto |  |
| Código da Cotação |  |
| Nome do Fornecedor |  |
| Código do Fornecedor |  |
| Número da Solicitação |  |
| Data de Inclusão | Filtro apresentado como ComboBox com os seguintes dados:  30 dias  60 dias  90 dias  120 dias  360 dias  Todos os dias |

Os dados exibidos são:

|  |  |
| --- | --- |
| **Campo Retorno Fluig** | **Observação** |
| Número da Cotação |  |
| Nome do Fornecedor | Campo obtido a partir do item de movimento relacionado na tabela TCITMORCAMENTO. |
| Código do Produto | Campo obtido a partir do item de movimento relacionado na tabela TCITMORCAMENTO. |
| Descrição do Produto | Campo obtido a partir do item de movimento relacionado na tabela TCITMORCAMENTO. |
| Unidade de Medida |  |
| Quantidade Orçada |  |
| Preço |  |
| Data da Cotação |  |
| Valor Total |  |

##
