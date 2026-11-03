---
content_hash: 076da21b89b5f9809189085ed5aa69828d2adbb56cb8253c12b7a61d6d8301e1
fetched_at: '2026-06-29T00:08:14.787562+00:00'
page_id: '244715580'
product: rm
source: tdn-rm
title: ER_CPTOP001-336_Melhorias_para_MI_Calculo_por_Rendimento_Diario
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_CPTOP001-336_Melhorias_para_MI_Calculo_por_Rendimento_Diario
version: 213
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Composição |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | CPTOP001 | **IRM1** | CPTOP001-335 |
| **Requisito1** | CPTOP001-336 | **Subtarefa1** | CPTOP001-407 |
| **Chamado2** | Não se Aplica. | | |
| **País** | (  ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   ( X ) Outro - Mercado Internacional. | | |
| **Outros** | | **Pré-requisitos para melhor entendimento da especificação** | | | --- | --- | | **Entidade** | **Link** | | Composições | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Composicoes.aspx> | |  |  | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Atender a demanda do mercado internacional para licitações públicas que exigem o detalhamento dos serviços (composições) por rendimento. Esta funcionalidade está disponível somente para o mercado internacional.

Entende-se como rendimento o tempo gasto para a produção de uma unidade de serviço. O rendimento de mão de obra e equipamento é a quantidade produzida em determinado tempo. Sendo assim, o sistema permite informar os rendimentos de mãos de obra e de equipamentos por serviço (composição) separadamente. Este rendimento é a base para o cálculo da quantidade necessária do recurso no serviço.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros de Projetos | Envolvida | Construção e Projetos -> Projetos -> Parâmetros -> Construção e Projetos -> Projetos | Composição |
| Composições | Alterada | Construção e Projetos -> Orçamento -> Cadastros -> Composição -> Cadastro | Composição |
| Grupo de Custos | Envolvida | Construção e Projetos -> Orçamento -> Cadastros -> Grupo de Custo | Composição |
| Gerenciador | Envolvida | Construção e Projetos -> Concorrência -> Gerenciador | Gerenciador de Licitação |
| Cálculo do Projeto | Alterada | Construção e Projetos -> Projetos -> Calcular o Projeto | Cálculo do Projeto |
| Relatórios de Composições do Projeto | Envolvida | Construção e Projetos -> Relatórios -> Composição -> Composições do Projeto | Relatórios de Composição |
| Importa Composições Via Texto/Excel | Alterada | Construção e Projetos -> Projetos -> Conversões -> Importa Composições Via Excel | Importação de Composições (Texto e EXCEL) |
| Alteração Geral de Composições | Alterada | Construção e Projetos -> Orçamento -> Cadastros -> Composição -> Alteração Geral | Alteração Geral de Composições |
| Planilha de Atividades e Serviços | Alterada | Construção e Projetos -> Orçamento -> Planilha | Planilha de Atividades e Serviços |
| Parâmetros Gerais | Alterada | Construção e Projetos -> Projetos -> Parâmetros -> Construção e Projetos -> Gerais | Parâmetros Gerais |
| Comparador de Projetos | Alterada | Construção e Projetos -> Projetos -> Comparador de Projetos -> Composições | Comparador de Projetos Composições |
| Cópia de Itens | Alterada | Construção e Projetos -> Orçamento -> Cópia de Itens | Cópia de Itens |

# **Composição**

Está disponível um novo tipo de composição denominado  “por Rendimento”, que atende o conceito de detalhamento de serviços por rendimento. Para melhor entendimento veja o .

Para que seja possível informar a jornada e os rendimentos de mãos de obra e equipamentos, foram criados três novos campos na entidade de composições, sendo eles: jornada, rendimento para mão de obra e rendimento para equipamento. Estas informações são obrigatórias.

Entende-se por jornada a medida de tempo utilizada para cálculo da quantidade para realização de uma unidade da composição.

A "**Cuadrilla**" no mercado internacional, é o termo em espanhol para definir o agrupamento de recursos para executar um determinado serviço. Para o cálculo da quantidade dos recursos de mão de obra e equipamentos será utilizado o campo EQUIPE do recurso. Na coluna EQUIPE do recurso deve ser informado quantas unidade do recurso compõe a "**Cuadrilla**"  utilizada para obter o rendimento. 

As casas decimais para coeficientes especiais definidas nos parâmetro de projeto em "Exibição | Geral" pode ser ajustada para melhor visualização dos valores calculados da quantidade do recurso.

São aplicadas as regras comuns a todos os tipos de serviços e adicionadas as seguintes:

* O cálculo da composição por rendimento é igual ao cálculo de uma composição por preço unitário;
* A jornada definida em "PERT / Alocação de Recurso" dos parâmetros do projeto servirá como default ao realizar a inclusão da composição;
* Os campos rendimento de mão de obra  e rendimento de equipamento são utilizados para informar o rendimento que será utilizado no cálculo da quantidade do recurso horário. São obrigatórios e permitem valores positivos maiores que 0(zero);
* A quantidade é desabilitada para os recursos que possuem unidade horária conforme unidades horárias definidas nos parâmetros gerais e que sejam dos grupos de custo de mão de obra ou equipamentos. Para estes recursos o cálculo da quantidade é com base no conteúdo dos campos equipe, jornada e rendimento. Considerando **QU -** Quantidade,**EQ** - Equipe, **RN** - Rendimento e **JN** - Jornada o cálculo da quantidade será: QU = EQ \* JN / RN;

  |  |  |  |  |  |
  | --- | --- | --- | --- | --- |
  | **Composição** | **Unidade** | **Jornada** | **Rend. Mão de Obra** | **Rend. Equipamento** |
  | Remoção | M3 | 8 | 45 | 45 |
  |  | **Recursos** | | | |
  |  | **Descrição** | **Unidade** | **Equipe** | **Quantidade = (EQ \* JN / RN)** |
  |  | Encarregado | HH | 1 | 0,1778 |
* O campo equipe é habilitado somente para recursos do tipo mão de obra ou equipamentos, com exceção de insumos com unidades percentuais (%);
* A aba Variáveis é habilitada porém, não permite a  inclusão de fórmula para quantidade nos recursos horários de mão de obra e equipamentos;
* Não estão disponíveis as abas gestão de manutenção e  produção da equipe mecânica;
* O campo “Não pode ser Composição Auxiliar” poderá ser utilizado, porém as auxiliares não interferem no cálculo de rendimento.

Processos

*Gerar relatório de modelo fixo EXCEL*

Criado o modelo de relatório "Planilha de composição analítica por rendimento" para a funcionalidade "Gerar relatório de modelo fixo EXCEL" disponível nos processos de cadastro de composição. Este novo modelo contempla as informações de jornada, rendimento de mão de obra e de equipamentos para a composição e o campo equipe para os recursos.

Veja alterações no .

*Copiar dados de outra composição*

O processo de copiar dados de outra composição realiza a copia das informações de jornada, rendimento de mão de obra e equipamento. O conteúdo destes campos são copiados, quando marcado a opção de "cabeçalho" e as duas composições sejam do tipo "por Rendimento". Após realizar a copia do cabeçalho entre as composições é recomendado a realização do cálculo para que os valores de jornada e rendimento sejam refletidos nos cálculos da quantidade dos recursos na composição.

| Atenção:   * Recomenda-se não utilizar o parâmetro não fracionado do cadastro de insumos; * A unidade dos insumos percentuais tem que ter o código ‘%’. |
| --- |

# **Parâmetros Gerais**

A identificação das unidades horárias é realizada na aba "Gerais" dos parâmetros gerais. As unidades definidas neste parâmetro são utilizadas para classificar a unidade dos recursos das composições permitindo aplicar as regras para os recursos horários. Para melhor entendimento vide 

# **Planilha de Atividades e Serviços**

Ao alterar/associar um recurso na tarefa ou cadastrar um calendário, o sistema verifica se trata de um recurso de composição por rendimento e valida a jornada do calendário da tarefa com a jornada da composição. Havendo incompatibilidade, é exibido um alerta informando que deve haver a compatibilidade entre as jornadas.

# **Gerenciador de Licitação**

Não há impacto.

# **Cálculo do Projeto**

O cálculo do projeto considera o novo tipo de composição por rendimento da mesma forma que é calculado a Composição do tipo Preços Unitários (CPU).

# **Importações de Composições (Texto e EXCEL)**

As importações de composições por texto e EXCEL foram adequadas para considerar os campos jornada, rendimento de mãos de obra e equipamentos em seus layouts.

Layout modificado para a importação de composições de arquivo TEXTO

Os campos adicionados não são obrigatórios, com isto mantém compatibilidade da funcionalidade de importação com os arquivos criados no formato anterior.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **COMPOSIÇÃO** | | | | | |
| Campo | Tamanho | De | Até | Obrig. | Observação |
| Status | 1 | 1 | 1 | S | \* (asterisco) |
| Código da Comp. | 20 | 2 | 21 | S |  |
| Descrição | 200 | 22 | 221 | S |  |
| Unidade | 10 | 222 | 231 | S |  |
| Produção | 15 | 232 | 246 | N | Separar casas decimais com ponto decimal (.) |
| ***Jornada*** | ***15*** | ***247*** | ***261*** | ***N*** | ***Separar casas decimais com ponto decimal (.)*** |
| ***Rendimento Mão de Obra*** | ***15*** | ***262*** | ***276*** | ***N*** | ***Separar casas decimais com ponto decimal (.)*** |
| ***Rendimento Equipamento*** | ***15*** | ***277*** | ***291*** | ***N*** | ***Separar casas decimais com ponto decimal (.)*** |
| **RECURSO INSUMO** | | | | | |
| Campo | Tamanho | De | Até | Obrig. | Observação |
| Status | 1 | 1 | 1 | S | I (para recursos insumos) |
| Código da Comp. | 20 | 2 | 21 | S |  |
| Código do Insumo | 20 | 22 | 41 | S |  |
| Quantidade | 15 | 42 | 56 | S | Separar casas decimais com ponto decimal (.) |
| Coef. Produtivo | 15 | 57 | 71 | N | Idem |
| DMT | 15 | 72 | 86 | N | Idem |
| Origem do Recurso (Global/Local) | 1 | 87 | 87 | N | Valores Válidos: G, g (qualquer outro valor o recurso é considerado como local). |
| ***Equipe*** | ***15*** | ***88*** | ***102*** | ***N*** | ***Separar casas decimais com ponto decimal (.)*** |
| **RECURSO COMPOSIÇÃO** | | | | | |
| Campo | Tamanho | De | Até | Obrig. | Observação |
| Status | 1 | 1 | 1 | S | C (para recursos composições auxiliares) |
| Código da Comp. | 20 | 2 | 21 | S |  |
| Código da Comp. Aux. | 20 | 22 | 41 | S |  |
| Quantidade | 15 | 42 | 56 | S | Separar casas decimais com ponto decimal (.) |
| Coef. Produtivo | 15 | 57 | 71 | N | Idem |
| DMT | 15 | 72 | 86 | N | Idem |
| Grupo DNIT | 1 | 87 | 87 | N |  |
| Origem do Recurso (Global/Local) | 1 | 88 | 88 | N | Valores Válidos: G, g (qualquer outro valor o recurso é considerado como local). |

Importação de Composição via EXCEL

Permite informar a coluna que contém a informação de rendimento da composição e a equipe do recurso horário. Estas informações são exibidas somente para o mercado internacional. Para melhor entendimento veja o .

# **Relatórios de Composição**

Não há impacto.

# **Integrações Project**

Não há impacto.

# **Alteração geral de composição**

Adicionada aba "Rendimento" na alteração geral de composições para permitir a manutenção geral dos campos jornada, rendimento de mão de obra e rendimento de equipamentos. Para melhor entendimento vide o .

Ao realizar a alteração de um determinado tipo de composição para um tipo de composição por rendimento são realizadas as seguintes validações:

* Valida a obrigatoriedade dos campos jornada, rendimento de mão de obra e rendimento de equipamentos. Concluindo a alteração somente após a informação destes campos;
* Valida a existência de fórmulas para recursos horários de mão de obra e equipamentos e, caso exista serão removidas.

Ao realizar a alteração de um tipo de composição por rendimento para qualquer outro tipo, o sistema retira o conteúdo dos campos jornada, rendimento de mão de obra e rendimento de equipamentos.

O sistema consiste alteração de quantidade de recurso quando o tipo da composição é por rendimento. Emite um alerta ao usuário e ignora a quantidade para recursos que enquadrem nas regras de cálculo por rendimento.

# **Comparador de Projetos - Composições**

O comparador de composições contempla os campos jornada, rendimento de mão de obra e equipamentos.

# Cópia de Itens

Ao realizar a cópia de composições do tipo "por Rendimento" o sistema realiza a cópia das informações de jornada, rendimento de mão de obra e equipamento.

***Tabelas Utilizadas***

* *MCMP – Cadastro de Composições*

## Protótipo de Tela

**Protótipo 01****- ****Composição******

****Protótipo 02 - ******Parâmetros Gerais**********

******Protótipo 03 - Relatório de Modelo Fixo EXCEL******

****Protótipo 04 - ******Alteração Geral de Composição**********

****Protótipo 05 - ******Importação de Composições via EXCEL**********

## Dicionário de Dados

**Arquivo ou Código do Script:** AAA – Negociação Financeira / \*Versao=CP.2014.12\_03\*/

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **MCMP** | | | | |
| **Descrição** | Composições | | | |
| **Coluna** | **Tipo** | **Descrição** | **Aceita Nulo** | **Default** |
| JORNADA | decimal | Jornada | Sim |  |
| RENDMO | decimal | Rendimento Mão de Obra | Sim |  |
| RENDEQ | decimal | Rendimento Equipamento | Sim |  |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
