---
content_hash: adc6caf4e2e40cee8e9c257987b01faf6a987b26fc13fd1e23486a628492d38c
fetched_at: '2026-06-29T00:08:24.746046+00:00'
page_id: '270902422'
product: rm
source: tdn-rm
title: Parâmetros de Retenção no Tipo de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=270902422
version: 2
---

# TRATAR ALTERAÇÃO NA RETENÇÃO / DEDUÇÃO NO ITEM DE MOVIMENTO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Parâmetros de Tipo de Movimento | RMSParamsWizardAction. | | | |
| **Chamado:** | Não se aplica. | | |
| **Requisito (ISSUE):** | CPMOV001-879 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

## Objetivo

Alterar a forma de como o usuário define o controle de retenção por item de movimento.

## Definição da Regra de Negócio

Nos parâmetros de Tipo de Movimento, na **Etapa Item – Valores Financeiros 2/2,**será alterado a forma de configurar a **Retenção** por item de movimento. As opções disponíveis para este campo são:

* **Não Usa:** não controla retenção por item de movimento.
* **Usa Percentual:**controla retenção por percentual.
* **Usa Valor:** controla retenção por valor.
* **Usa Ambos:** controla retenção por valor e percentual.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Tipo de Movimento | Alteração | **Ambiente >> Parâmetros >> Gestão de Estoque, Compras e Faturamento >> Outras Movimentações >> Tipos de Movimento.** | - |

**Tabelas Utilizadas**

* TTMVEXT – Tipos de movimento.

### Procedimento para Utilização

Após definir as configurações de Retenção no tipo de movimento, consulte este documento de como utilizar o .

### Dicionário de Dados

**Arquivo ou Código do Script:** /\*$Versao=NU.2016.12\_07\*/
