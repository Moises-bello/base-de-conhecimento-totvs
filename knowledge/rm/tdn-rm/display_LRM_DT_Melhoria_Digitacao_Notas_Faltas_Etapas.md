---
content_hash: 58c849e9ca9d50a9ee95aa5c52fe911919dbd7271c0491a629d4e056473c086c
fetched_at: '2026-06-29T00:06:30.169022+00:00'
page_id: '235314887'
product: rm
source: tdn-rm
title: DT_Melhoria_Digitacao_Notas_Faltas_Etapas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Melhoria_Digitacao_Notas_Faltas_Etapas
version: 119
---

# Melhoria na Digitação de Notas e Faltas por Etapas

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Gestão Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Digitação de Notas e Faltas por Etapa* | *Digitação de Notas e Faltas por Etapa* | |
| **Versões/Release:** | *12.1.4* |

## Descrição

Melhoria na digitação de notas/faltas por etapa permitindo que esses campos sejam bloqueados de acordo com a necessidade da instituição de utilizar os dois modelos existentes, digitação de notas por avaliação e faltas por etapa.

## Procedimento para Implantação

Para atender as necessidades dos clientes foram feitos ajustes no Cadastro de Etapa e na Digitação de Notas/Faltas de Etapa para permitir que esses campos sejam bloqueados caso a instituição de ensino utilize a digitação de NOTAS de avaliação e a digitação de FALTAS por etapa.

Com este parâmetro desmarcado, a IE irá controlar a notas por Avaliação e as faltas por frequência diária

Um novo campo foi criado no cadastro de Etapas, **“Permite digitação diretamente na etapa”,** para controlar a digitação nas etapas de notas e faltas. O campo estará disponível para os dois tipos de etapas.

Além do cadastro de Etapas esse campo também foi disponibilizado nos cadastros de modelo de etapas por período letivo e modelo de etapas da matriz aplicada.

A digitação de notas/faltas pode ser feita através de três canais: TOTVS Educacional, Portal Corpore.Net e TOTVS Educa Mobile. Suas respectivas rotinas de digitação de nota/falta foram alteradas para se adequarem às alterações, conforme abaixo:

* TOTVS Educacional

Existem duas formas de digitação de notas/faltas, são elas:

* Notas e Faltas de Etapa (Matrícula e Avaliação | Notas e Faltas | Notas e faltas de etapa)

Se a etapa estiver com a opção “Permite digitação diretamente na etapa” **desmarcada**:

* Etapa de Notas

O coluna “Nota” não permitirá digitação, bem como a coluna “Comentário”, onde não será aberto pop-up para digitação.

* Etapa de Faltas

O coluna “Falta” não permitirá digitação, bem como a coluna “Nº Aulas”. As informações do campo “Nº de aulas dadas” não serão replicadas para a coluna “Nº Aulas”.

* Digitação por Aluno - Notas e Faltas de Etapa (Matrícula e Avaliação | Notas e Faltas | Mais... | Digitação por aluno)

Nessa tela são exibidas todas as etapas de Notas e Faltas disponíveis para o aluno selecionado, portanto o tratamento é feito por linha e não por coluna como na tela de “Notas e Faltas de Etapa”. Cada linha corresponde a uma etapa e os campos dessa linha serão desabilitados caso a opção “Permite digitação diretamente na etapa” esteja **desmarcada**. A regra adotada é a mesma da tela “Notas e Faltas de Etapa” descrita anteriormente.

* Portal Corpore.Net

Existe apenas uma opção para digitação de notas/faltas.

Se a etapa estiver com a opção “Permite digitação diretamente na etapa” **desmarcada**:

* Etapa de Notas

A coluna “Nota” ficará desabilitada e o link da coluna “Comentários” será removido para evitar a digitação desse campo.

* Etapa de Faltas

As colunas “Falta” e “Nº Aulas” ficarão desabilitadas. A informação do campo “Nº de aulas dadas” não será replicada para a coluna “Nº Aulas”.

* TOTVS Educa Mobile

Existe apenas uma opção para digitação de notas/faltas.

Se a etapa estiver com a opção “Permite digitação diretamente na etapa” **desmarcada**:

* Etapa de Notas

A coluna “Notas” será desabilitada. Não existe a coluna “Comentário”.

* Etapa de Faltas

A coluna “Faltas” será desabilitada.

## Informações Técnicas

|  |  |
| --- | --- |
| **Tabelas Utilizadas:** | SETAPAS.PERMITEDIGITACAO;  SMODETAPAHABILITACAO.PERMITEDIGITACAO;  SMODETAPAPLETIVO.PERMITEDIGITACAO |
| **Funções Envolvidas:** | Cadastro de Etapas;  Cadastro de Modelo de Etapas Por Período Letivo;  Cadastro de Modelo de Etapas da Matriz Aplicada;  Digitação de Notas/Faltas de Etapa;  Digitação Por Aluno – Notas/Faltas de Etapa. |
| **Sistemas Operacionais:** | *Windows* |

divs
