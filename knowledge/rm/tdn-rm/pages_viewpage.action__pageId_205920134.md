---
content_hash: c197c5f643a645e7966c36e58f6a05f65e3a4bdeda563c3be39aca4b80de960d
fetched_at: '2026-06-29T00:06:12.728521+00:00'
page_id: '205920134'
product: rm
source: tdn-rm
title: PCREQ-7862_ER_Relatório_CAGED
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=205920134
version: 2
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | Folha de Pagamento | **Módulo** | CAGED |
| **Segmento Executor** | Contrução e Projetos | | |
| **Projeto1** | R\_RH\_FOP008 | **IRM1** | PCREQ-7827 |
| **Requisito1** | PCREQ-7862 | **Subtarefa1** | PDR\_RH\_FOP128-106 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

## Objetivo

 

*Permitir ao usuário a possibilidade de exportar os dados do CAGED para diversos formatos de arquivos.*

## Definição da Regra de Negócio

*Serão listadas a seguir as evoluções que serão necessárias para atender o requisito. Serão realizadas dentro da nova MDI:*

1. **Alteração de layout da tela Validador de Arquivo**

A tela de validação de arquivos do relatório CAGED que pode ser acessado através da execução do relatório através do caminho [Folha de Pagamento -> Encargos -> CAGED] terá a disposição das visões de registros e dados alteradas para obter melhor aproveitamento de espaço e suportar a opção de exportação para arquivo. As visões de registros e dados serão reposicionadas e serão exibidas lado a lado, conforme o **Protótipo 1 - Alteração de layout da tela Validador de Arquivo**.

        2.**Exportação para****arquivos**

A tela de validação de arquivos do relatório CAGED que pode ser acessado através da execução do relatório através do caminho [Folha de Pagamento -> Encargos -> CAGED] receberá uma opção para exportação dos dados para arquivo, conforme **Protótipo 2 - Exportação de arquivo.**

## Protótipo de Tela

**Protótipo 1 - Alteração de layout da tela Validador de Arquivo**

**Protótipo 2 - Exportação de arquivo**

### Opcional

## Fluxo do Processo

*<Nesta etapa incluir representações gráficas que descrevam o problema a ser resolvido e o sistema a ser desenvolvido. Exemplo: Diagrama - Caso de Uso, Diagrama de Atividades, Diagrama de Classes, Diagrama de Entidade e Relacionamento e Diagrama de Sequência>.*

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

## Grupo de Perguntas

 

*<Informações utilizadas na linha Protheus>.*

 

**Nome: FINSRF2**

|  |  |
| --- | --- |
| **X1\_ORDEM** | 01 |
| **X1\_PERGUNT** | Emissão De |
| **X1\_TIPO** | D |
| **X1\_TAMANHO** | 8 |
| **X1\_GSC** | G |
| **X1\_VAR01** | MV\_PAR01 |
| **X1\_DEF01** | Comum |
| **X1\_CNT01** | '01/01/08' |
| **X1\_HELP** | Data inicial do intervalo de emissões das guias de DARF a serem consideradas na seleção dos dados para o relatório |

### (Opcional)

## Consulta Padrão

*<Informações utilizadas na linha Protheus>*

**Consulta: AMB**

|  |  |
| --- | --- |
| **Descrição** | Configurações de Planejamento |
| **Tipo** | Consulta Padrão |
| **Tabela** | “AMB” |
| **Índice** | “Código” |
| **Campo** | “Código”; ”Descrição” |
| **Retorno** | AMB->AMB\_CODIGO |

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
