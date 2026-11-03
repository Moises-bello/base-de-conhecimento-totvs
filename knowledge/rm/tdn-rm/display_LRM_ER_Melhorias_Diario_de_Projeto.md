---
content_hash: a4877d3c95c47fb6ad8179f6fd0d40db386263b2f6ebbdc81a1ab6c58be63f21
fetched_at: '2026-06-29T00:06:29.752135+00:00'
page_id: '234617857'
product: rm
source: tdn-rm
title: ER_Melhorias_Diario_de_Projeto
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Melhorias_Diario_de_Projeto
version: 122
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Diário de Projeto |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP011 | **IRM1** |  |
| **Requisito1** |  | **Subtarefa1** |  |
| **Chamado2** | Não se aplica. | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | Pré-Requisitos para melhor entendimento da especificação:   | Módulo | Link | | --- | --- | | Projetos | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Projetos.aspx> | | Planilhas | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Planilhas.aspx> | | Insumo | <http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Insumos.aspx> | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Aplicar melhorias na funcionalidade de Diário de Projeto disponível no TOTVS Obras e Projetos fazendo do mesmo um novo módulo no sistema.

## Definição da Regra de Negócio

### Diário do Projeto

O diário de projeto, também conhecido como diário de obra, é um documento usado para registrar informações importantes sobre cada dia de atividade do projeto.

É uma espécie de memorial da obra. Nele, é anotado tudo o que aconteceu de importante no projeto em um determinado dia:

* Os serviços feitos
* Os equipamentos utilizados - e por quantas horas
* As condições do clima, etc.

E, se necessário, também podem ser descritos no diário os problemas na execução de serviços, falhas nos equipamentos, etc.

O diário de projeto é importante, pois ele conta, dia a dia, a história do projeto ao longo de todo seu período de execução.

No TOTVS Obras e Projetos a funcionalidade de Diário de Projeto está localizado no seguinte caminho: Construção e Projetos | Controle | Agrupador Básico| Diário de Projeto.

### Melhorias no Diário de Projeto

A entidade atual de Diário de Projeto passa a ter um comportamento de cabeçalho do Diário de Projeto, ou seja, ela terá atividades associadas e informações em comum para todas as atividades.

Irá conter as seguintes informações:

* **Número do Diário:** Um novo campo para identificar o diário. Único por coligada e projeto.
* **Data:** Campo já presente na entidade atual e será mantido para guardar a data do diário.
* **Assunto:** Campo já presente na entidade atual e será mantido para guardar um resumo do diário.
* **Comentário:** Um novo campo para comentários gerais ou informações complementares.
  + **Exemplo:** Sem energia de 07:30 às 12:00 atrasando as atividades previstas.
  + **Exemplo:**Abertura do portão da obra com atraso de 30 minutos.

#### Itens do Diário de Projeto

Os itens do diário de projeto, ou seja, as atividades executadas no dia, será uma nova entidade para inserir mais de uma atividade ao diário.

Irá conter as seguintes informações:

* **Código da Classificação:** Campo para guardar uma classificação para a ocorrência na atividade. Por exemplo: Acidente de trabalho, Aspectos ambientais, etc.
* **Tarefa:** Atividade da Planilha de Atividades que será executada no dia. Será obrigatório e poderá ser informado uma obra ou etapa, pois a ocorrência pode ser em comum para todas as atividades.
* **Ocorrência:** Campo para guardar as ocorrências de uma determinada atividade, etapa ou obra.
  + **Exemplo:** Caminhão ainda em manutenção.
  + **Exemplo:** Retroescavadeira quebrou às 15:30h.
  + **Exemplo:** Acidente de trabalho grave que paralisou a obra.

#### Condições Climáticas

O Diário de Projeto agora irá conter as condições climáticas do dia dividas em turnos a serem cadastrados no sistema.

Condições Climáticas será uma nova entidade para armazenar o cadastro de condições climáticas utilizadas pela empresa.

Esta entidade irá conter as seguintes informações:

* Código
* Descrição

**Exemplo:** Bom, tempo bom, chuvoso, chuva fraca, chuva forte, praticável, impraticável, etc.

#### Turnos

Turnos será uma nova entidade para armazenar os turnos das condições climáticas e dos itens que foram apropriados.

Esta entidade irá conter as seguintes informações:

* Código
* Descrição

**Exemplo:** Manhã, tarde, noite, 1º turno, 2º turno, 3º turno, diurno, matutino, noturno, etc.

#### Situação Climática no Diário

Nova entidade para armazenar a situação climática do dia.

Esta entidade irá conter as seguintes informações:

* **Condição Climática:** Vinculo com a entidade Condição Climática.
* **Turno:** Vinculo com a entidade Turnos.
* **Volume de chuva (mm):** Indicar o volume de chuvas no turno.

#### Apropriação de Serviços/Insumos

Será adicionado na visão do Diário de Projeto um anexo com a visão da Apropriação de Serviços/Insumos para exibir as informações dos equipamentos e mão de obra que atuaram no dia.

Será adicionado o campo turno na Apropriação de Serviços/Insumos para saber em qual turno os equipamentos e mão de obra atuaram.

#### Processo para cópias de Diário de Projeto

Será criado um processo na visão do Diário de Projeto para realizar cópias de outros diários para facilitar e agilizar a inserção das informações de novos diários que possam ser repetitivas ao usuário.

No formulário do processo será exibido um campo para definir a data que o novo diário irá adotar.

#### Relatório do Diário de Projeto

Será criado um relatório do Diário de Projeto com todas as informações relatadas no dia.

O relatório poderá ser impresso e exportado para Excel, PDF e Word.

O modelo do relatório se encontra no tópico de protótipos deste documento.

## Protótipo de Tela

### Protótipo 01 - Tela de Cadastro do Diário de Projeto

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### Protótipo 02 - Tela de Cadastro da Classificação de Diário de Projeto

### 

### 

### 

### 

### 

### 

### 

### Protótipo 03 - Tela de Cadastro das Condições Climáticas

### 

### 

### 

### 

### 

### 

### 

### Protótipo 04 - Tela de Cadastro dos Turnos

### 

### 

### 

### 

### 

### 

### Protótipo 06 - Anexo de Apropriação de Serviços/Insumos para o Diário de Projeto

### Protótipo 06 - Relatório do Diário de Projeto

## Fluxo do Processo

### Diagrama de Caso de Uso

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### 

### Descrição do Caso de Uso: Cadastro de Diário de Projeto

 

|  |  |
| --- | --- |
| **Nome do caso de uso** | Cadastro do Diário de Projeto |
| **Sumário** | Usuário utiliza o sistema para gerar o relatório de ocorrências em obras, conhecido como Diário de Projeto ou Diário de Obra. |
| **Ator primário** | Usuário |
| **Atores secundários** | Não se aplica. |
| **Pre-condições** | 1. O Usuário está autenticado no sistema.  2. Possuir Projetos e Tarefas cadastrados. |
| **Fluxo Principal** | 1. O Usuário entra no sistema. |
| 2. O Usuário acessa a visão de Diário de Projeto: Menu | Controle | Agrupador Básico | Diário de Projeto | Cadastro |
| 3. O Usuário clica no botão Novo. |
| 4. O Usuário informa a data, o número, o assunto e os comentários gerais do Diário. |
| 5. O Usuário inclui as situações climáticas para cada turno ao Diário. |
| 6. O Usuário inclui os itens (atividades) bem como a classificação e ocorrência de cada item. |
| 7. O Usuário salva o Diário de Projeto. |
| **Fluxo Alternativo** | (6) Inclusão dos itens ao Diário. |
| a. O Usuário Salva o Diário. |
| b. O Usuário abre o Anexo de Itens do Diário de Projeto. |
| c. O Usuário clica no botão Novo do Anexo. |
| d. O usuário inclui um item ao Diário. |
| e. O Usuário salva o item. |
| **Pós-condições** | O Diário de Projeto foi criado de forma completa e já pode ser visto, impresso ou exportado pelo relatório de Diário de Projeto. |

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

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
