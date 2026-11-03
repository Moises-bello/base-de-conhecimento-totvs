---
content_hash: 40b323e4c852776bc3b5bc7af76cad10cea56647216d051a699d530be666ecc1
fetched_at: '2026-06-29T00:08:45.332144+00:00'
page_id: '311625189'
product: rm
source: tdn-rm
title: 464950 FINANCEIRO01-350 Importação lançamento financeiro de IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311625189
version: 93
---

# IMPORTAÇÃO DE LANÇAMENTO FINANCEIRO GERADOR DE IRRF SEM VALOR

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos. |
| **Módulo:** | Totvs Gestão Financeira. |
| **Função:** | Importação de lançamentos financeiros. |
| **Situação/Requisito:** | Ao importar lançamentos com tipo de documento que gerar IRRF (pessoa física ou jurídica) e o sistema está parametrizado para gerar o mesmo automaticamente, caso o valor do IRRF informado na linha de dados do registro importado seja zero o sistema não conseguia realizar a inclusão, era exibida uma mensagem do banco de dados indicando em duplicidade de registro na tabela FRELLANPAI. |
| **Solução/Implementação:** | Realizado tratamento no serviço de inclusão de lançamento financeiro para não gerar novo registro para o IRRF caso o valor importado seja zero. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | 464950. |
| **Requisito:** | FINANCEIRO01-350. |

divs
