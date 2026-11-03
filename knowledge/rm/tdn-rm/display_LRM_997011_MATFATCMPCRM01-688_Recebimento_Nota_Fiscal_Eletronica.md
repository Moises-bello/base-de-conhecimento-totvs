---
content_hash: 92614d73bd0add83d9f846df96379bd243244648a604e0197ec29d61c9d143d3
fetched_at: '2026-06-29T00:08:37.713475+00:00'
page_id: '284882738'
product: rm
source: tdn-rm
title: 997011_MATFATCMPCRM01-688_Recebimento_Nota_Fiscal_Eletronica
type: documentation
url: https://tdn.totvs.com/display/LRM/997011_MATFATCMPCRM01-688_Recebimento_Nota_Fiscal_Eletronica
version: 29
---

# Recebimento de Nota Fiscal Eletrônica

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Estoque, Compras e Faturamento* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Inclusão de Movimento através de XML - TOTVS Colaboração | MovTraducaoXMLTOTVSColabProcAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Inclusão Automática de Movimento | MovInclusaoAutomaticaMovColabProcAction | |  |  | |
| **Cadastros Iniciais:** | *Parâmetros Fiscais por Filial -> Informações TOTVS Colaboração* |
| **Parâmetro(s):** | *Parâmetros -> 04.03 - Integrações -> 04.03.03 - Fiscal -> 04.03.03.01 - Dados Fiscais -> Parâmetros por Filial -> Informações TOTVS Colaboração* |
| **Ponto de Entrada:** | *N/A* |
| **Tickets relacionados** | 997011 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-688 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | *SqlServer e Oracle* |
| **Tabelas Utilizadas:** | *TPARFILIAL* |
| **Sistema(s) Operacional(is):** | *Windows* |

**Descrição:**

Implementação de parâmetros no sistema com objetivo de definir se os movimentos serão incluídos automaticamente durante o recebimento de Nota Fiscal Eletrônica ou de Conhecimento de Transporte Eletrônico.

**Parâmetro**:  
Parâmetros  -> 04.03 - Integrações -> 04.03.03 - Fiscal -> 04.03.03.01 - Dados Fiscais -> Parâmetros por Filial -> Importação/Envio de Arquivo XML 2/2 -> **Não Incluir Movimento Automaticamente**

O procedimento padrão do sistema é incluir o movimento automaticamente durante o recebimento do XML.  Caso seja necessário alterar este comportamento, basta utilizar o parâmetro citado.

Há um parâmetro para XMLs de Nota Fiscal Eletrônica (NF-e) e outro para Conhecimento de Transporte Eletrônico (CT-e).

Caso o parâmetro esteja marcado, os XML's daquele tipo de documento serão importados e cadastrados na tabela TNFEENTRADA, no entanto, a inclusão do movimento não será realizada durante a importação.

Com o XML cadastrado, o movimento poderá ser incluído no sistema através de 2 processos, são eles:

1. **Manual**: Inclusão de Movimento através de XML - TOTVS Colaboração
2. **Automática**: Inclusão Automática de Movimento

**Importante**:  
No caso de NF-e, para utilizar a segunda opção **"Inclusão Automática de Movimento"**, o parâmetro **Tipo de Recebimento de NF-e** deve estar devidamente configurado.
