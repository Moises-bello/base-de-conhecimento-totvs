---
content_hash: bf198d5e914438caedc2bffd04887aa8d13b58e22e226ca722bee188cbf97397
fetched_at: '2026-06-29T00:08:43.185900+00:00'
page_id: '301197994'
product: rm
source: tdn-rm
title: 1047610 MATESTCNTFTOF01-390 DT Versão do Adapter CustomerVendor na FV de Carga
  e Sincronização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301197994
version: 99
---

# INTEGRAÇÃO DE CLIENTE/FORNECEDOR COM MENSAGEM ÚNICA CUSTOMERVENDOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. |
| **Função:** | Fórmula Visual de integração de Cliente/Fornecedor. |
| **Situação/Requisito:** | Ao executar o Configurador da Integração do Manutenção de Ativos x BackOffice RM está sendo incluído automaticamente o adapter CUSTOMERVENDOR na versão 2.002, porém as Fórmulas Visuais que estão disponíveis dentro da pasta de instalação (Objetos Gerenciais) estão com a versão antiga do adapter (1.000). |
| **Solução/Implementação:** | A fórmula visual do cadastro de Cliente/Fornecedor (MOVWKF0007 - CustomerVendor.TotvsWF) será mantida com a versão 1.000, pois será utilizada somente quando a mensagem CustomerVendor\_1.000 estiver mapeada para a integração. Este cenário será aplicado nos clientes que instalaram a integração a partir da versão 11.82.  A partir da versão 12.1.11 para os novos clientes que começarem a utilizar a integração Manutenção de Ativos x BackOffice RM, ao executar o Configurador de Integração é mapeada a versão 2.002 da CustomerVendor que não necessita de Fórmula Visual. O gatilho de integração é interno no serviço de Cliente/Fornecedor.  A fórmula visual de Sincronização de Cliente/Fornecedor teve a sua versão alterada para 2.002. |
| **Conversores e Parâmetros:** | Desnecessário. |
| **Tickets relacionados:** | Não se aplica. |
| **Requisito:** | Cliente/Fornecedor (FinCFOAction); CustomerVendor |

divs
