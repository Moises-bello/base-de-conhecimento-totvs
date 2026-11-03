---
content_hash: 46fce68b3abd926b4f1c5371fe44fe7d85c1df0d5f16d88e483559443ed10e96
fetched_at: '2026-06-29T00:08:51.518454+00:00'
page_id: '337347031'
product: rm
source: tdn-rm
title: DT - Filtrar Subordinados Diretos na Gestão de Férias - Portal RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=337347031
version: 3
---

# Filtrar Subordinados Diretos na Gestão de Férias - Portal RM

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Folha de Pagamento |
| **Módulo:** | RM Portal - Gestão de Férias |
| **Solução/Implementação:** | Foi criado um parâmetro na tela de Gestão de Férias do portal para exibir apenas os subordinados diretos do gestor. |
| **Requisito:** | [FOPROTINAS01-872](http://jiraproducao.totvs.com.br/browse/FOPROTINAS01-872) |

Foi criado um parâmetro na tela de Gestão de Férias do portal para exibir apenas os subordinados diretos do gestor.

Subordinados diretos são os funcionários que na hierarquia da tela de “Cadastro de Chefe/Supervisor“ respondem diretamente à um determinado chefe. Ou seja, que pertencem à própria seção da qual o chefe é responsável ou pertencem à seções filhas que não possuem chefes cadastrados e ativos.

Ao acessar a tela de Gestão de Férias no Portal RM, basta marcar a checkbox que foi adicionada no canto superior direito para que sejam exibidos apenas os subordinados diretos do gestor logado no sistema:

Atenção: Se a checkbox estiver marcada, o parâmetro também será considerado ao utilizar os filtros na aba "Filtro"
