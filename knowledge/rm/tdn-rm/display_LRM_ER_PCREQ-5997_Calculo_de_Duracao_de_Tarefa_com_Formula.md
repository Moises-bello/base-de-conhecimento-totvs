---
content_hash: cd50b0df87c9fa150997bfa7de12d232300ce9f4f8629be508d007903060819a
fetched_at: '2026-06-29T00:06:24.337021+00:00'
page_id: '224116808'
product: rm
source: tdn-rm
title: ER_PCREQ-5997_Calculo_de_Duracao_de_Tarefa_com_Formula
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-5997_Calculo_de_Duracao_de_Tarefa_com_Formula
version: 141
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOP (TOTVS Obras e Projetos) |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP010 | **IRM1** | PCREQ-5996 |
| **Requisito1** | PCREQ-5997 | **Subtarefa1** | PDR\_CP\_TOP010-2 |
| **Chamado2** | Não se Aplica | | |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:   | Módulo | Link | | --- | --- | | PERT | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PERT.aspx> | | PERT | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.PertAlocacao.aspx> | | Formulas | <http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Formulas.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Será implementado o cálculo da duração das tarefas a partir de formulas definidas pelos clientes para  flexibilizar o planejamento das atividades no Gráfico de PERT.

## Definição da Regra de Negócio

Módulo de Serviços Globais 

Para calcular a duração da tarefa por formula será utilizado o conceito de formulas definido no módulo de serviços globais.

As formulas devem ser cadastradas em "**Administração** | Agrupador **Cadastros** | **Formulas"**.

Parâmetro Geral

Serão utilizadas as unidades horárias informadas nos parâmetros gerais. As tarefas que possuem insumos definidos com a unidade dentre as unidades horárias  e estejam associados diretamente ou em sua(s) composição(ões) serão calculadas.

Para conferir ou definir uma unidade horário, devemos acessar a aba "Configuração MS Project ®" no módulo de Projetos em "**Projetos** | Agrupador  **Parâmetros** | menu **Construção e Projetos** | **Gerais**"

Parâmetro de Projeto

Para automatizar o processo, serão adicionados três parâmetros no projeto na aba "PERT / Alocação de Recursos".

Estes parâmetros serão agrupados em "Cálculo de Duração de Tarefa com Formula"  e terão funções especificas. Não possuirão dependências entre si.

**Formula** - Determina a formula que será usada no momento do cálculo. Será utilizada em todas as tarefas que estejam marcadas para o cálculo automático e possuam insumos cuja a unidade estejam dentro das eleitas como "Unidade Horária".

**Utiliza a Quantidade da Equipe Informada na Tarefa** - Com este parâmetro marcado o sistema irá considerar a quantidade da equipe no momento do cálculo da capacidade dos recursos. Caso esteja desmarcado, será considerado como quantidade o número de associações do recurso a equipes do projeto.

**Ajustar Duração Fracionada** - Devido a necessidade do processo trabalhar com numero de dias não fracionado, este parâmetro irá determinar a forma de arredondamento dos dias retornado pela formula. Exemplo: A formula retornando 10,4 dias, se estiver marcada a opção "**Para cima**", serão considerados 11 dias, se marcado "**Para baixo**", serão considerados 10 dias.

Vide o  - Parâmetros Gerais.

 Vide o  - Parâmetros de Projeto.

Parametrização na Tarefa

Para que a duração da tarefa seja calculada automaticamente serão adicionadas duas nova opções na aba "Outros" do cadastro de planilhas. Estas opções estão descritas a seguir.

**Utiliza Cálculo da Duração por Formula** - Este parâmetro será marcado por "default". Sua função é determinar ao sistema que a tarefa deverá ser calculada no processo "Programar" do PERT. Além da marcação desta opção é necessário contemplar as seguintes regras:

* Formula informada nos parâmetros do Projeto;
* Um insumo com unidade horária associado diretamente na tarefa ou em uma de suas composições.

**Insumo Principal** - Determina ao sistema qual insumo será a referencia para o cálculo de capacidade da equipe. Serão aplicadas a esta opção as seguintes regras:

* Será informada somente se a opção "Utiliza Cálculo da Duração por Formula" estiver marcada;
* Não será editável na célula da planilha, sendo editável somente na tela de edição. Esta regra tem o intuito de não degradar o carregamento da planilha;
* Será adicionada um filtro quando a tarefa tiver como recurso um insumo, nesta situação ao marcar para calcular será adicionado automaticamente este recurso. Ao atualizar o sistema no Cliente, as tarefas que possuem o recurso como insumo, terão automaticamente este campo atualizado;
* Quando o recurso for uma composição, somente poderá ser selecionado insumos que façam parte da(s) composição(ões) da tarefa;
* Ao realizar a gravação da tarefa, este campo será limpo automaticamente caso a opção "Utiliza Cálculo da Duração por Formula" esteja desmarcada;
* Esta informação não será obrigatório. Quando não estiver informado, será realizada uma busca na(s) composição(ões) para determinar qual insumo será mais significativo para determinar a duração.

Vide o  - Planilha de Atividades e Serviços.

Vide o  - Planilha de Tarefas.

 

Atualização Múltipla de Registros

Será adicionada  na alteração múltipla a possibilidade de parametrizar as tarefas para utilizar o cálculo da duração por fórmula. Conforme apresentado no .

Cálculo da Tarefa

No PERT acesse a função programar. Assim as tarefas que estejam marcadas para calcular a duração por formula apresentarão os valores devidamente calculados no campo “Duração Programado Dias”. Vide o  definido neste documento.

Será disponibilizada uma função de formulas que poderá ser utilizada no cadastramento da formula.

A jornada para o insumo será definida de acordo com a seguinte ordem:

1. Jornada definida no calendário do recurso na tarefa;
2. Jornada definida no calendário da atividade aba da natureza do insumo (grupo DNIT);
3. Jornada definida no calendário da atividade aba geral;
4. Jornada definida no Insumo;
5. Jornada definida nos parâmetros do projeto para o PERT.

Deve considerar a data de início e fim da tarefa para verificar os períodos e encontrar os dias úteis.

Exemplo:

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Formulas | Envolvido | Modulo **Serviços Globais** / **Administração** / Agrupador **Cadastros** / **Formulas** | - |
| Planilha de Atividades e Serviços | Alteração | **Orçamento** / Agrupador **Cadastros** / **Planilha** | - |
| Atualização Múltipla de Registros | Alteração | **Orçamento** / Agrupador **Cadastros** / **Planilha /** Processo **Atualização Múltipla de Registros** | - |
| Programar no PERT | Alteração | **Planejamento** / Agrupador **Básico** / **PERT**   **Gantt** / Agrupador **GanttPert** / **Funções do Planejamento** / **Programar** | - |

***Tabelas Utilizadas***

* *- Tarefas*
* *MPARAMETRO - Parâmetros  de Projeto*
* *MGIS-Grupos de Custo*
* *MISM-Insumos*
* *MTRFREAL-Cronograma Realizado*

## Protótipo de Tela

****Protótipo 01 - Parâmetro de Projeto****

**Protótipo 02 -****Planilha de Atividades e Serviços**

**Protótipo 03 - Atualização Múltipla de Registros**

## Fluxo do Processo

## Dicionário de Dados

**Arquivo ou Código do Script:**  /\*$Versao=SO.2016.2\_2\*/

Dicionário 01 - Parâmetros de Projeto

Dicionário 02 - Planilha de Tarefas

Obs.: Ao criar os campos na tabela MTAREFA é necessário recriar as views MTRF e MSERVICO.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
