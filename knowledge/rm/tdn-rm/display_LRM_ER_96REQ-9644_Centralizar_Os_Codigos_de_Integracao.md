---
content_hash: 74a77127fe8c10298c75b48871d61b1f68f7cf76538d509a10e3c69c29bfb7c6
fetched_at: '2026-06-29T00:08:05.354679+00:00'
page_id: '235594460'
product: rm
source: tdn-rm
title: ER_96REQ-9644_Centralizar_Os_Codigos_de_Integracao
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_96REQ-9644_Centralizar_Os_Codigos_de_Integracao
version: 112
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | FRAMEWORK | **Módulo** | EAI |
| **Segmento Executor** |  | | |
| **Projeto1** | R\_FRW\_FMW002 | **IRM1** | PCREC-9634 |
| **Requisito1** | PCREQ-9644 | **Subtarefa1** | PDR\_FRW\_FRW002-22 |
| **Chamado2** |  | | |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 

*<Nesta etapa informar o objetivo da especificação do requisito, ou seja, o que a funcionalidade deve fazer. Exemplo: Permitir que o usuário defina o percentual mínimo em espécie (dinheiro), a referência mínima para calculo dos débitos do aluno e o período de validade do parâmetro de negociação>.*

### (Obrigatório)

## Definição da Regra de Negócio

*<Regra de negócio é o que define a forma de fazer o negócio, o processo definido e/ou as regras que devem ser contempladas. Devem ser descritas restrições, validações, condições e exceções do processo. Caso necessário, incluir neste capítulo também regras de integridade que devem ser observadas no momento do desenvolvimento>.*

*<Na tabela abaixo informe quais são as rotinas envolvidas, o tipo de operação, a opção de menu e se necessário uma breve descrição das regras de negócio relacionadas a rotina>.*

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

***Exemplo de Aplicação:***

* *Criar o campo “% Mínimo Espécie” (AAA\_PERESP) onde o usuário informará o % que o aluno pagará em dinheiro. Esse % poderá ser alterado durante a negociação.*
* *Criar o campo “Referência Mínima para Cálculo” (AAA\_REFCAL) onde o usuário informará um dos 4 valores disponíveis para pagamento das mensalidades  como a referência mínima para calcular o débito total do aluno.*
* *Criar o parâmetro MV\_ACPARNE que definirá se as informações de “% Mínimo Espécie” e “Referência Mínima para Cálculo” serão obrigatórias.*
* *O parâmetro MV\_ACPARNE deve ter as seguintes opções: 1=Obrigatório e 2=Opcional. Deve ser inicializado como opcional>.*

***Tabelas Utilizadas***

* *SE2 – Cadastro de Contas a Pagar*
* *FI9 – Controle de Emissão de DARF>.*

### Opcional

## Protótipo de Tela

*<Caso necessário inclua protótipos de telas com o objetivo de facilitar o entendimento do requisito, apresentar conceitos e funcionalidades do software>.*

**Protótipo 01**

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
