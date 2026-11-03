---
content_hash: cd836b1446b012424521e655de1fcf981fc416967d54674523b4d1cf3d7cab0f
fetched_at: '2026-06-29T00:06:25.057319+00:00'
page_id: '224129853'
product: rm
source: tdn-rm
title: DT_Desativar_Eventos
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Desativar_Eventos
version: 1
---

# DESATIVAR EVENTOS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **Totvs Folha de Pagamento **Totvs** Automação de Ponto** ****Totvs** Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | - | - | |
| **Versão/Release:** | *12.1.4* |

## Descrição

Nesta versão, evoluímos em vários locais, onde os eventos “desativos/desabilitados” não serão exibidos.

**TOTVS Folha de Pagamento**   
• Eventos vinculados;   
•  Alteração Global de Código Fixo;   
•  Alteração Global de Eventos Programados;   
•  Agrupamento de Salário Folha Educacional;   
•  Parametrizador (Folha Normal / Afastamento).

**TOTVS Automação de Ponto**   
•  Parametrizador (Sindicatos / Eventos).

**TOTVS Gestão de Pessoas**   
•  Benefícios

Também foi incluído uma validação que irá exibir uma mensagem ao usuário quando o mesmo for desativar um evento que está sendo utilizado em algum cadastro do produto.

## Procedimento para Utilização

## TOTVS Folha de Pagamento

***Eventos Vinculados***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Folha de Pagamento / Guia Administração de Pessoal / Eventos / Eventos / Anexos / Lançamentos Vinculados.**

***Alteração Global de Código Fixo***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Folha de Pagamento / Guia Administração de Pessoal / Alterações Cadastrais / Alteração Códigos Fixos**

Os eventos inativos deixam de ser exibidos no lookup do campo “Evento”, na primeira etapa do processo. Importante: Os eventos inativos, serão exibidos, quando a ação selecionada for “Exclusão”, para as demais ações, os inativos não serão exibidos.

***Alteração Global de Eventos Programados***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Folha de Pagamento / Guia Administração de Pessoal / Alterações Cadastrais / Alteração Eventos Programados**

Os eventos inativos deixar de ser exibidos no lookup do campo “Evento”, na segunda etapa do processo.   
Importante: Os eventos inativos, serão exibidos, quando o comportamento selecionado for “Exclusão”, para os demais comportamentos, os inativos não serão exibidos.

***Agrupamento de Salário Folha Educacional***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Folha de Pagamento / Guia Folha Educacional / Agrupamento Salarial / Classis Net**

Os eventos inativos deixam de ser exibidos nos lookups de Evento de Salário, Evento de Atraso e Evento de Falta.

## TOTVS Automação de Ponto

***Parametrizador ( Sindicatos / Eventos )***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Automação de Ponto / Guia Configurações / Parametrizador / Sindicatos / Eventos**

Os eventos inativos deixam de ser exibidos no lookup de Código do evento relacionado RM TOTVS Folha de Pagamento.

## TOTVS Gestão de Pessoas

***Benefícios***

Para que o usuário tenha acesso lookup do evento, siga o seguinte passo: **Acesse RH / Gestão de Pessoas / Guia Valoziração / Benefícios / Cadastro ou Edição / Aba Parâmetros de Cálculo.**

Os eventos inativos deixam de ser exibidos no lookup Evento Funcionário

## TOTVS Folha de Pagamento

***Nova Validação na Edição de Evento***

No momento em que desativar um evento que está sendo utilizado em algum cadastro do produto, irá aparecer janela demonstrando em qual local este evento está sendo utilizado.
