---
content_hash: 1b9dd21f5490d1f5f184beb1e4197fb3d74f6a156de5d9d99474f2b9f12b7283
fetched_at: '2026-06-29T00:08:31.171336+00:00'
page_id: '273294129'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-166 Parâmetro Remover Caracteres Especiais da Nota Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=273294129
version: 109
---

# Parametrização de Nota Fiscal

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | NOTAS FISCAIS | NOTAS FISCAIS |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | *PARÂMETROS POR FILIAL* | *PARÂMETROS POR FILIAL* | |
| **Cadastros Iniciais:** | *Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais -> Parâmetros por Filial ->*  *Ambiente NF-e* |
| **Parâmetro(s):** | *Informe os parâmetros utilizados.* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | *N/A* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-166 |
| **País(es):** | *Brasil* |
| **Banco(s) de Dados:** | *SQLServer e Oracle* |
| **Tabelas Utilizadas:** | *TPARFILIAL* |
| **Sistema(s) Operacional(is):** | *Windows* |

## Descrição

Foi criado um novo parâmetro no sistema com o objetivo de definir se os caracteres especiais e acentuações devem ser mantidos no XML da Nota Fiscal (Estadual e Municipal).

**Etapa**: Parâmetros -> Gestão de Estoque, Compras e Faturamento -> Integrações -> Fiscal -> Dados Fiscais -> Parâmetros por Filial -> Ambiente  NFe  
**Nome**: Retirar Caracteres Especiais  
**Descrição**: Retirar os caracteres especiais e acentuações do XML da Nota Fiscal.

Com este parâmetro habilitado, durante a geração do XML da Nota Fiscal o sistema removerá qualquer caractere especial ou acentuação do arquivo.

divs
