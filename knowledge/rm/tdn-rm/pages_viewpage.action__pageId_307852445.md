---
content_hash: 8c91f5ca9174129e6b4e798e78110f357008f959f37681936bee7444178fdfaa
fetched_at: '2026-06-29T00:08:44.440336+00:00'
page_id: '307852445'
product: rm
source: tdn-rm
title: 1435051 MATESTCNTFTOF01-860 DT Buscar Defaults de Cli/For e de Representante
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307852445
version: 93
---

# SOBREPOR DEFAULT DE CLIENTE/FORNECEDOR E DE REPRESENTANTE AO REALIZAR O FATURAMENTO/CÓPIA SIMPLES/CÓPIA POR REFERÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Buscar Default de Cli/For e de Representante. |
| **Situação/Requisito:** | Ao parametrizar a Conta Caixa default no Tipo de Movimento e marcar o parâmetro para **Buscar default de Cli/For e de Representante** o sistema busca o valor default corretamente na inclusão/edição do movimento. Entretanto, ao realizar a inclusão de movimento via faturamento/cópia simples/cópia por referência o sistema desconsidera o valor default informado no cadastro de Cli/For e o parâmetro marcado, preenchendo o movimento que está sendo incluído com a informação parametrizada no Tipo de Movimento. |
| **Solução/Implementação:** | Será realizada a alteração para que o sistema tenha o mesmo comportamento da inclusão/edição de movimentos, também no faturamento/cópia simples/cópia por referência.  A partir da versão 12.1.19 os default de Cli/For e de Representante sempre terão prioridade no preenchimento dos campos nos processos supracitados, **desde que na origem os campos que englobam os default de Cli/For e de Representante não estejam informados**. Caso esses dados existam na origem, o sistema manterá o seu comportamento padrão, ou seja, copiará os dados da origem para o destino. |
| **Conversores e Parâmetros:** | Ambiente | Parâmetros | Gestão de Estoque, Compras e Faturamento | 04.01 - Parâmetros Gerais | 04.01.01 - Definições Gerais | Etapa Definições Gerais 3/3 | **Buscar defaults de Cli/For e de Representante**. |
| **Tickets relacionados:** | 1435051. |
| **Requisito:** | MATESTCNTFTOF01-860. |

divs
