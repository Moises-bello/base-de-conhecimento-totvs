---
content_hash: 888275f201110341ee01f356f22617274cb23e52383e87f87a1bbecc31830186
fetched_at: '2026-06-29T00:08:23.061334+00:00'
page_id: '269443638'
product: rm
source: tdn-rm
title: Dedução no Item de Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269443638
version: 11
---

# DEDUÇÃO NO ITEM DE MOVIMENTO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoAction |  |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Parâmetros Tipo de Movimento | RMSParamsWizardAction | | Item de Movimento | MovItemMovimentoAction | | | |
| **Chamado:** | N/A. | | |
| **Requisito (ISSUE):** | CPMOV001-829 | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos>.* | | |

### Objetivo

 

Permitir que o usuário defina o valor de dedução por item de movimento.

## Definição da Regra de Negócio

Atualmente as deduções são controlas através do campo Desconto no Item de Movimento.

Para que a Dedução possa ser rastreada, será disponibilizado na tela de Item de Movimento um campo específico para considerar as deduções. As regras para utilização deste campo será discriminado abaixo.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros Tipo de Movimento | Alteração | Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Tipos de Movimentos | - |
| Item de Movimento | Alteração | Gestão de Estoque, Compras e Faturamento \ Outras Movimentações | - |
| Parâmetros Gerais | Envolvido | Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento \ Parâmetros Gerais \ Definições Gerais | - |

**Parâmetros Tipo de Movimento**

Para que a dedução possa ser controlada a nível de item, será necessário configurar o tipo de movimento para usar dedução e também definir qual será o tipo de dedução. Com isso será necessário criar os parâmetros para que sejam salvas estas configurações por tipo de movimento.  Criar na tabela TTMVEXT os campos:

* **Utilizar Dedução** (USADEDUCAOIT) onde o usuário define que este tipo de movimento irá usar dedução no item de movimento. Este campo deve ser um ComboBox com as seguintes opções:
  + **Não Usa:** não usa dedução no item. Valor do campo no banco zero (0).
  + **Usa Percentual:** o valor da dedução deverá ser informado em percentual.Valor do campo no banco um(1).
  + **Usa Valor:**  a dedução deverá ser informado em valor. Valor do campo no banco dois (2).
  + **Usa Ambos:** utiliza percentual e valor. Valor do campo no banco três (3).

**Item de Movimento**

Será disponibilizado na tela de edição do item de movimento os campos referentes à dedução. Estes campos possuirão as seguintes regras:

* **Valor deduzido:****visível** e **editável**quando o tipo de movimento configurado para Utilizar Dedução e Tipo de Dedução Valor ou Ambos.
* **Percentual deduzido:****visível** e **editável**quando o tipo de movimento configurado para Utilizar Dedução  e Tipo de Dedução Percentual ou Ambos.

Este campo deve ser apresentado na pasta Tributos e Valores da janela de edição do item de movimento, similar ao que existe para Retenção. Quando o item de movimento for gerado por outro sistema (verificar código do sistema na coluna Integra Aplicação), eles não poderão ser alterados. Os campos de Percentual e Valor deverão respeitar as  casas decimais definidos nos parâmetros gerais do sistema.

Criar na tabela de Itens de Movimento (TITMMOV) os campos  Valor deduzido(VALORDEDUCAO) e Percentual deduzido(PERCENTUALDEDUCAO).

**Cálculo dos valores:**

Quando o tipo de movimento estiver configurado com Tipo de Dedução igual a Ambos, sempre que na edição do Item for alterado o valor ou percentual, deve-se realizar o recálculo considerando o novo valor ou percentual informado. Para isso devem ser considerados as seguintes fórmulas de cálculo:

* Fórmula de Cálculo do Percentual: *Percentual = Valor Deduzido / (Valor do Item \* 100)*.
* Fórmula de Cálculo do Valor: *Valor Deduzido = (Valor do Item \* Percentual Deduzido) / 100*.

O ***cálculo dos valores financeiros dependentes dos itens*** também deve considerar a dedução do item, ou seja, quando o tipo de movimento utilizar dedução deve-se realizar os cálculos dos valores considerando as fórmulas listadas acima.

A ***rotina que trata as diferenças entre a cópia de itens do faturamento e cópia referência*** também deve considerar a dedução do item. Neste caso deve-se aplicar as regras abaixo:

* Quando o tipo de movimento destino Utilizar Dedução no Item igual a Usa Valor:
  + Valor deduzido do item de movimento destino recebe o valor deduzido do item de movimento origem.
  + Percentual deduzido do item de movimento destino recebe o percentual deduzido do item de movimento origem após o calculo do Movimento.
* Quando tipo de movimento destino Utilizar Dedução no Item igual a Usa Percentual:
  + Valor deduzido do item de movimento destino recebe o valor deduzido do item de movimento origem após o calculo do Movimento.
  + Percentual deduzido do item de movimento destino recebe o percentual deduzido do item de movimento origem.
* Quando tipo de movimento destino Utilizar Dedução no Item igual a Usa Ambos:
  + Valor deduzido do item de movimento destino recebe o valor deduzido do item de movimento origem.
  + Percentual deduzido do item de movimento destino recebe o percentual deduzido do item de movimento origem.

**Totaliza valores dos itens do movimento.**

Alterar a fórmula TVIM para considerar o Valor da Dedução.

**Regras de Integridade**

* Quando a dedução for configurada como Ambos, ao alterar o Valor o campo Percentual deve ser recalculado considerando o valor informado. Ao alterar o campo Percentual o Valor deve ser recalculado considerando este novo percentual.

**Tabelas Utilizadas**

* TTMVEXT – Tipos de movimento.
* TITMMOV – Itens de Movimento.

## Procedimento para Utilização

Utilização de Dedução no Item de Movimento, considerando que o tipo de movimento está configurado para **Usar Ambos.**

**Inclusão de Movimento com Dedução no Item**

1. Acesse o menu **Outras Movimentações \ Outras Movimentações**
   1. O sistema apresenta a janela de Outras Movimentações. Informe o Tipo de Movimento e a Filial e confirme
2. Selecione uma opção de Filtro e confirme.
3. Na visão de Movimento clique em **Incluir**
   1. O sistema apresenta a janela de edição de Movimentos. Preenche os dados necessários.
4. Em **Itens** clique em **Incluir**
   1. O sistema apresenta a janela de inclusão de item de movimento.
   2. Em **Identificação \ Cabeçalho** informe os dados obrigatórios e acesse **Tributos e Valores \ Valores.**
5. No campo **Dedução** informe o **Valor deduzido**.
   1. Como o movimento utiliza Dedução como Ambos, ao informar o Valor deduzido o campo Percentual deduzido é calculado automaticamente.
6. Confira as informações e confirme a inclusão.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. Acesse **Gestão de Estoque, Compras e Faturamento \ Ambiente \ Parâmetros \ Gestão de Estoque, Compras e Faturamento** selecione um **Tipo de Movimento** e na etapa **Item Valores 2/2** defina um valor para o campo **Dedução.**

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/ 

|  |  |
| --- | --- |
| **Tabela** | TTMVEXT |
| **Campo** | USADEDUCAOIT |
| **Tipo** | SMALLINT |
| **Tamanho** | 2 |
| **Valor Inicial** | NULO |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Utiliza Dedução Item. |
| **Help de Campo** | Informa que o tipo de movimento utiliza dedução por item de movimento. Este campo pode ser alterado e as opções são: Não Usa, Usa Percentual, Usa Valor ou Usa Ambos. |

|  |  |
| --- | --- |
| **Tabela** | TITMMOV |
| **Campo** | VALORDEDUCAO |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | (15,4) |
| **Valor Inicial** | NULO |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Valor Deduzido. |
| **Help de Campo** | Informar o valor que será deduzido. Este campo pode ser alterado quando tipo de movimento usar dedução no item. |

|  |  |
| --- | --- |
| **Tabela** | TITMMOV |
| **Campo** | PERCENTUALDEDUCAO |
| **Tipo** | RMDVALOR4 |
| **Tamanho** | (15,4) |
| **Valor Inicial** | NULO |
| **Mandatório** | Sim (  ) Não ( X ) |
| **Descrição** | Percentual Deduzido. |
| **Help de Campo** | Informar o percentual deduzido. Este campo pode ser alterado quando tipo de movimento usar dedução no item. |
