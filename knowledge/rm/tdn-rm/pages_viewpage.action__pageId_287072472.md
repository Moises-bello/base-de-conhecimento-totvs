---
content_hash: 8cb63e1034f5f672c480484e27b392674afbef387d64876e2d0ac258c230a3c1
fetched_at: '2026-06-29T00:08:42.429204+00:00'
page_id: '287072472'
product: rm
source: tdn-rm
title: ER MATESTCNTFTOF01-766 Alterações Bloco K - Registro K220
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=287072472
version: 109
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | Movimento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01 | **IRM/EPIC1** | MATESTCNTFTOF01-766 |
| **Requisito/Story/Issue1** | MATESTCNTFTOF01-812 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Em 28/08/2017, foi publicado no Diário Oficial da União (DOU) o Ato COTEPE/ICMS 48, que determinou alterações no Ato COTEPE/ICMS 09/08, que dispõe sobre as especificações técnicas para a geração de arquivos da Escrituração Fiscal Digital – EFD.

Dentre as alterações propostas foi definida a alteração do Registro K220, referente ao Bloco K da EFD ICMS/IPI, que passa a ter efeito a partir de 1º de janeiro de 2018.

Baseado nisso, iremos fazer os ajustes necessários na rotina de geração do Registro K220 de forma a atender a legislação.

## 

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

**Obs.:** Em relação à forma de gerar as movimentações nada muda, não havendo necessidade de alteração do processo, apenas ajuste na geração do Registro K220. Ver especificação .

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |

**Tabelas Utilizadas**

* TMOTIVOREFMOV - Motivos de Cópia por Referência
* TMOV - Movimento

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
