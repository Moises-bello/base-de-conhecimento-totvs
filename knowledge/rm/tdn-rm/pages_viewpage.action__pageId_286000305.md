---
content_hash: d97945eba212c6718210b38e8a177c41c60018095e6d0052374a79f96b1310a5
fetched_at: '2026-06-29T00:08:38.906700+00:00'
page_id: '286000305'
product: rm
source: tdn-rm
title: ER SAUHRM02-1292 - Alterações na tela de pesquisa de itens por grupo de gasto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286000305
version: 3
---

|  |
| --- |
| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |

Nenhuma anotação efetuada a mão ou rasura no documento será considerada válida.

|  |  |  |  |
| --- | --- | --- | --- |
| Especificação |  |  |  |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Faturamento |
| **Segmento Executor** | Saúde |  |  |
| **Projeto¹** | R\_SAU\_HRM1617 | **IRM¹** | SAUHRM02-1370 |
| **Requisito¹** | SAUHRM02-1292 | **SubTarefa¹** |  |
| **Chamado²** | 296570 |  |  |
| **Release de Entrega Planejada** | Não definido | **Réplica** | Não necessário |
| **País** | **(**X **) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador**   **(  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_.** |  |  |
| **Outros** |  |  |  |

\_Toc355276661\_Toc355276662

# Objetivo

\_Toc355276664Permitir que os usuários apliquem filtros de data à função de "Pesquisa de itens por grupo de gasto" disponível na tela "Elaboração de contas" do RM Saúde.

# Definição da Regra de Negócio

**RN001 –** Criar uma coluna com a apresentação da data do lançamento na tela de Pesquias de itens por grupo de gasto.   
 **RN002 –** Permitir que a partir da nova coluna sejam aplicados filtros de data, conforme nas demais colunas.   
 **RN003 –** Garantir que na composição da tela haja distinção entre itens na conta e itens estornados ou excluídos.   
 **RN004 –** Alterar o texto apresentado quando o mouse para sobre o botão de binóculo que chama a tela de Pesquisa de itens por grupo de gasto. Atualmente o texto apresentado é *LOCALIZAÇÃO RÁPIDA PELA DISCRIMINAÇÃO* e deverá ser alterado para *PESQUISA DE ITENS POR GRUPO DE GASTO*.

|  |  |  |
| --- | --- | --- |
| Rotinas Envolvidas |  |  |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** |
| Pesquisa de itens por grupo de gasto | Alteração | FATURAMENTO > ELABORAÇÃO DE CONTAS: Pesquisa de grupos por grupo de gasto. |

# \_Toc355276665Protótipo de Tela

As imagens de telas destacadas a seguir são consideradas apenas protótipos, as mesmas poderão sofrer alterações em função da atualização de componentes utilizados no sistema, devem ser utilizadas apenas para exemplificar a forma de iteração que os usuários possuirão ao acessar o sistema, o fluxo de negócio e a forma em que os dados e informações serão manipuladas.

## \_Toc355276666#Funcionalidade 01

|  |  |
| --- | --- |
| **Função** | PESQUISA DE ITENS POR GRUPO DE GASTO |
| **Objetivo** | Inserir uma coluna para que seja pos´sivel a pesquisa e organização baseada na data de um lançamento |
| **Módulo** | Faturamento |
| **Menu** | Faturamento > Elaboração de contas |

|  |
| --- |
| **Protótipos** |
| A alteração na tela deverá ser baseada nos protótipos apresentados à seguir: |

|  |  |
| --- | --- |
|  | **Regras de Interface** |
| **RI-001** | Incluir, preferencialmente após a coluna *quantidade,* uma coluna chamada *data*, na qual será apresentada a data de lançamento de cada item. |
| **RI-002** | Com esta nova coluna, será possível a ordenação e realização de filtros a partir dela, à exemplo das demais colunas. |
| **RI-003** | Incluir um checkbox chamado *estornados*. Sem que este checkbox esteja marcado, o grid deverá ser alimentado somente com os itens contidos na conta, caso esteja o checkbox marcado, e hajam itens estornados á serem apresentados, estes deverão ser tachados, de modo que seja possível ao usuário identifica-los facilmente. |
| **RI-004** | Incluir na tela um totalizador correspondente à\_GoBack coluna de valor, que considere os itens filtrados. |

# \_Toc355276667Fluxo do Processo

Não necessário para o desenvolvimento deste requisito.

# Dicionário de Dados

Não necessário para o desenvolvimento deste requisito.

# Grupo de Perguntas

Não necessário para o desenvolvimento deste requisito.

# **Consulta Padrão**

Não necessário para o desenvolvimento deste requisito.

# Estrutura de Menu

Não necessário para o desenvolvimento deste requisito.

# Assinaturas

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Nome | Cargo | Data | Ação | Assinatura |
| Cleber Correa | Analista de Negócio |  | Autor |  |
| Joji Tamekuni | Líder de Equipe de Desenvolvimento |  | Aprovador |  |
| Daniel Solari | Coordenador de Desenvolvimento |  | Revisor |  |
