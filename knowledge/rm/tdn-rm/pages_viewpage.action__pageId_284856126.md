---
content_hash: aaa8d7229d13e11b18b495ad2f121aaa817d8e275bff1e357293d3459980b0a4
fetched_at: '2026-06-29T00:08:36.935156+00:00'
page_id: '284856126'
product: rm
source: tdn-rm
title: DT_Adequação dos eventos da Carga Inicial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284856126
version: 6
---

|  |  |
| --- | --- |
| Descrição | Adequação dos eventos da Carga Inicial para o leiaute 2.2.02 |
| Observações | Eventos da Carga Inicial que sofreram adequações para o leiaute 2.2.02 |

Eventos que sofreram alteração no Release 12.1.17:

# S-1005 - Tabela de Estabelecimento/Obras

## Inclusão

1. Tomador de Serviço:

Criado check box “Considera dados da filial” no cadastro do Tomador e do CEI.

Marcando este parâmetro será possível  selecionar a filial do qual o sistema considerará os valores do CNAE, RAT e FAP, no momento da geração do evento S-1005.

Desmarcando este parâmetro o sistema habilitará os campos para que o usuário informe os valores quer serão considerados no momento da geração de S-1005.

. ![](http://tdn.totvs.com/download/attachments/284856126/image2017-7-13%2015%3A0%3A54.png?version=1&modificationDate=1499968855868&api=v2)

# S-1050- Tabela de Horários/Turnos de Trabalho

## Inclusão

1 - Jornada 12 x 36 (12 horas de trabalho seguidas de 36 horas ininterruptas de descanso):

 Para que o eSocial entenda a jornada 12 x 36, foi criado o parâmetro conforme demonstrado na imagem abaixo.

# S-2100 - Evento Cadastramento Inicial do Vínculo

## Exclusão

1. Trabalhador Temporário  
     
   Foi excluído o campo "Chapa do Funcionários Substituído", pois campo não deve retornar no xml conforme leiaute 2.2.02

# Alterações

1. No cadastro de Trabalhador Temporário, a descrição do campo “Motivo da contratação de trabalhador temporário (mtvContrat)” foi alterado para “Hipótese legal para contratação de trabalhador temporário (hipLeg)”.

**Antes** :

**Depois:**

# Validação:

1. Alterada a validação da idade mínima para informar o CPF.

Incluída validação de CPF para >14 anos  para não haver CPF repetido nos dependentes.
