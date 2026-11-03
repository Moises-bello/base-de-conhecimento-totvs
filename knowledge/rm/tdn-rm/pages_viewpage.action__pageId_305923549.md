---
content_hash: 5ea05203f7e19076d6a84033361349439953e119c4152ccae5b1572e5767346b
fetched_at: '2026-06-29T00:08:43.650888+00:00'
page_id: '305923549'
product: rm
source: tdn-rm
title: MATESTCNTFTOF01-812 DT Alterações Bloco K - Registro K220
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305923549
version: 98
---

# Alterações Bloco K - Registro K220

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | ***Construção e Projetos*** |
| **Módulo:** | ***T**OTVS Gestão de Estoque Compras e Faturamento***** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Gerar Sped Fiscal - Layout 2.0* | *FisSpedFiscalAction* | |
| **Cadastros Iniciais:** | . |
| **Parâmetro(s):** | *.* |
| **Ponto de Entrada:** | *.* |
| **Tickets relacionados:** | *.* |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | *MATESTCNTFTOF01-812.* |
| **País(es):** | *Brasil.* |
| **Banco(s) de Dados:** | **SQLServer e Oracle.** |
| **Tabelas Utilizadas:** | **TMOTIVOREFMOV / TMOV.** |
| **Sistema(s) Operacional(is):** | *Windows.* |

## Descrição

Em 28/08/2017, foi publicado no Diário Oficial da União (DOU) o Ato COTEPE/ICMS 48, que determinou alterações no Ato COTEPE/ICMS 09/08, que dispõe sobre as especificações técnicas para a geração de arquivos da Escrituração Fiscal Digital – EFD.

Dentre as alterações propostas foi definida a alteração do Registro K220, referente ao Bloco K da EFD ICMS/IPI, que passa a ter efeito a partir de 1º de janeiro de 2018.

Baseado nisso, iremos fazer os ajustes necessários na rotina de geração do Registro K220 de forma a atender a legislação.

## Definição da Regra de Negócio

A mudança no Registro K220 se dá em relação ao campo 05, que passa a ser chamado QTD\_ORI e o acréscimo do campo 06 - QTD\_DEST, que deverá retornar a quantidade movimentada do item de destino.

O registro K220 do Bloco K da EFD ICMS/IPI passará a ter o seguinte leiaute:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Nº | Campo | Descrição | Tipo | Tam | Dec | Obrig. |
| 01 | REG | Texto Fixo contendo "K220" | C | 4 | - | O |
| 02 | DT\_MlOV | Data da movimentação interna | N | 8 | - | O |
| 03 | COD\_ITEM\_ORI | Código do item de origem (campo 02 do Registro 0200) | C | 60 | - | O |
| 04 | COD\_ITEM\_DEST | Código do item de destino (campo 02 do Registro 0200) | C | 60 | - | O |
| 05 | QTD\_ORI | Quantidade movimentada do item de origem | N | - | 3 | O |
| 06 | QTD\_DEST | Quantidade movimentada do item de destino | N | - | 3 | O |

**Validações:**

Campo 01 (REG) - Valor Válido: [K220]

Campo 02 (DT\_MOV) - Validação: a data deve estar compreendida no período informado nos campos DT\_INI e DT\_FIN do Registro K100.

Campo 03 (COD\_ITEM\_ORI) - Validação: o código do item de origem deverá existir no campo COD\_ITEM do Registro 0200.

Campo 04 (COD\_ITEM\_DEST) - Validação: o código do item de destino deverá existir no campo COD\_ITEM do Registro 0200. O valor informado deve ser diferente do COD\_ITEM\_ORI.

Campo 05 (QTD\_ORI) - Preenchimento: informar a quantidade movimentada do item de origem codificado no campo COD\_ITEM\_ORI.  
Validação: este campo deve ser maior que zero.

Campo 06 (QTD\_DEST) - Preenchimento: informar a quantidade movimentada do item de destino codificado no campo COD\_ITEM\_DEST.  
Validação: este campo deve ser maior que zero.

**Tabelas Utilizadas**

* TMOTIVOREFMOV - Motivos de Cópia por Referência
* TMOV - Movimento

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do último pacote de atualizações *da 12.1.17, 12.1.18 e release 12.1.19.*

## Procedimento para Utilização

Em relação à forma de gerar as movimentações nada muda, não havendo necessidade de alteração do processo, apenas ajuste na geração do Registro K220. Ver especificação [Bloco K - Registro K220](http://tdn.totvs.com/display/LRM/TTO575+ER+Bloco+K+Registro+K+220).

divs
