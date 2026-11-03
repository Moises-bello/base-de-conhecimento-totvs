---
content_hash: e885b022125839fab43bb1a4d4f2001d21c921eb629575f5d569270180af7579
fetched_at: '2026-06-29T00:08:19.862238+00:00'
page_id: '267795157'
product: rm
source: tdn-rm
title: ER_CPMOV001-698_Analise_de_Agrupamento
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPMOV001-698_Analise_de_Agrupamento
version: 102
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão de Estoque, Compras e Faturamento |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_CP\_MOV 2016/2017 | **IRM1** | CPMOV001-665 |
| **Requisito1** | CPMOV001-698 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **País** | (x) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Analise de melhoria do Agrupamento de Itens de Orçamento, de acordo, com o parâmetro da Cotação "Não agrupar itens iguais na Cotação" localizado em Movimento -> Gestão de Compras -> Cotação -> Etapa 6 - Movimentos. Com o objetivo de melhorar o processo de agrupamento foi realizada uma analise para que seja possível realiza-lo na inclusão da Cotação, ao invés de ser executado na edição da tela de Itens de Orçamento\Negociação.

## Definição da Regra de Negócio

Para que seja possível a realização do agrupamento na inclusão da Cotação, as alterações abaixo se fazem necessárias:

* Atualmente o parâmetro  "Não agrupar itens iguais na Cotação" localizado em Movimento -> Gestão de Compras -> Cotação -> Etapa 6 - Movimentos ficaria disponível no Assistente de Geração de Cotação.
* Processo para que seja possível Agrupar ou Desagrupar os Itens de Orçamento após a inclusão da Cotação através do assistente.
* Modificação do relacionamento entre as tabelas de Itens de Orçamento e Itens de Movimento Cotado.

Atualmente o relacionamento é com os campos CODCOLIGADA, CODTACAO, CODCOLMOV, IDMOV e NSEQITMMOV, porém os campos do Movimento (CODCOLMOV, IDMOV e NSEQITMMOV) será removidos da tabela de Itens de Orçamento e os mesmos ficarão disponíveis apenas na tabela de Itens de Movimento Cotado.

Serão criados os campos SEQITMORCAMENTO e SEQITMMOVIMENTO nas tabela de Itens de Orçamento e Itens de Movimento cotado, respectivamente.

Para permitir um relacionamento N x N entre as tabelas de Itens de Orçamento e Itens de Movimento Cotados será criada a tabela TCITMORCAGRUPADO que permitirá associar para um ou mais Itens de Orçamento a um único Item de Movimento, permitindo assim o agrupamento.

* Os demais processos que sofreram impactos com a nova modelagem da Cotação serão:
  + Alteração e Exclusão da Cotação.
  + Processos de Inserir Novos Itens na Cotação e Excluir Produtos não Cotados.
  + Geração de Ordem de Compra.
  + Calculo do Quadro Comparativo.
  + Processos de Excluir Itens de Movimento e Limpar Itens Excluídos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Cotação | [Alteração] | [Compras -> Cotação ] | - |

***Tabelas Utilizadas***

* *TCCOTACAOITMMOV – Itens de Movimento Cotados*
* *TCITMORCAMENTO – Itens de Orçamento*
* *TCITMORCAGRUPADO - Relacionamento Itens de Orçamento e Itens de Movimento Cotados*
* *TCCOTACAO - Cotação*

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

 

|  |  |
| --- | --- |
| **Índice** | **Chave** |
| **01** | <FI9\_FILIAL+FI9\_IDDARF+FI9\_STATUS> |
| **02** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_EMISS+FI9\_IDDARF> |
| **03** | <FI9\_FILIAL+FI9\_FORNEC+ FI9\_LOJA+FI9\_PREFIX+FI9\_NUM+FI9\_PARCEL+FI9\_TIPO> |

|  |  |
| --- | --- |
| **Campo** | <AAA\_PERESP> |
| **Tipo** | <N> |
| **Tamanho** | <6> |
| **Valor Inicial** | <Varia de acordo com o tipo informado. Por exemplo, quando o campo “tipo” for date, neste campo pode ser informado uma data>. |
| **Mandatório** | Sim (  ) Não (  ) |
| **Descrição** | <Referência Mínima para Cálculo> |
| **Título** | <Ref.Calc.> |
| **Picture** | <@E999.99> |
| **Help de Campo** | <Informar o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação> |

### (Opcional)

## Estrutura de Menu

*<Informações utilizadas na linha Datasul>.*

**Procedimentos**

|  |  |  |  |
| --- | --- | --- | --- |
| **Procedimento** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Módulo** |  |  |  |
| **Programa base** |  |  |  |
| **Nome Menu** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Registro padrão** | Sim | Sim | Sim |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Release de Liberação** |  |  |  |

**Programas**

|  |  |  |  |
| --- | --- | --- | --- |
| **Programa** |  |  |  |
| **Descrição** | (Max 40 posições) | (Max 40 posições) | (Max 40 posições) |
| **Nome Externo** |  |  |  |
| **Nome Menu/Programa** | (Max 32 posições) | (Max 32 posições) | (Max 32 posições) |
| **Nome Verbalizado**[1]**** | (Max 254 posições) | (Max 254 posições) | (Max 254 posições) |
| **Procedimento** |  |  |  |
| **Template** | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) | (Verificar lista de opções no man01211) |
| **Tipo**[2]**** | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas | Consulta/Manutenção/ Relatório/Tarefas |
| **Interface** | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex | GUI/WEB/ChUI/Flex |
| **Categoria**[3]**** |  |  |  |
| **Executa via RPC** | Sim/Não | Sim/Não | Sim/Não |
| **Registro padrão** | Sim | Sim | Sim |
| **Outro Produto** | Não | Não | Não |
| **Visualiza Menu** | Sim/Não | Sim/Não | Sim/Não |
| **Query on-line** | Sim/Não | Sim/Não | Sim/Não |
| **Log Exec.** | Sim/Não | Sim/Não | Sim/Não |
| **Rotina (EMS)** |  |  |  |
| **Sub-Rotina (EMS)** |  |  |  |
| **Localização dentro da Sub Rotina (EMS)** |  |  |  |
| **Compact**[4]**** | Sim/Não | Sim/Não | Sim/Não |
| **Home**[5]**** | Sim/Não | Sim/Não | Sim/Não |
| **Posição do Portlet**[6]**** | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right | 0 – Top Left  1 – Top Right  2 – Bottom Left  3 – Bottom Right |
| **Informar os papeis com os quais o programa deve ser vinculado** |  |  |  |

**Cadastro de Papéis**

*<O cadastro de papéis é obrigatório para os projetos de desenvolvimento FLEX a partir do Datasul 10>.*

*<Lembrete: o nome dos papeis em inglês descrito neste ponto do documento, devem ser homologados pela equipe de tradução>.*

|  |  |
| --- | --- |
| **Código Papel** | **(máx 3 posições)** |
| **Descrição em Português\*** |  |
| **Descrição em Inglês\*** |  |

---

[1] Nome Verbalizado é obrigatório para desenvolvimentos no Datasul 10 em diante.

[2] Tipo é obrigatório para desenvolvimento no Datasul 10 em diante

[3] Categorias são obrigatórias para os programas FLEX.

[4] Obrigatório quando o projeto for FLEX

[5] Obrigatório quando o projeto for FLEX

[6] Obrigatório quando o projeto for FLEX

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
