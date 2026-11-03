---
content_hash: 43a7066cbde0e1f6a0d82202f67b9f41632583b6fa2a052c2263f794ef23f5ff
fetched_at: '2026-06-29T00:08:28.982897+00:00'
page_id: '272138608'
product: rm
source: tdn-rm
title: ER SAUHRM02-748 Melhoria Protocolo TVP
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-748+Melhoria+Protocolo+TVP
version: 99
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Prontuário Eletrônico |
| **Segmento Executor** | Saúde | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-749 |
| **Requisito/Story/Issue1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-748 | **Subtarefa1** | JIRA Produção0c783de1-186e-383b-975c-a1acd7d76cb5SAUHRM02-765 |
| **Chamado/Ticket2** |  | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

  Este documento tem como objetivo especificar o requisito de automação do Protocolo TVP. 

   Este requisito implementará um sistema de pontuação, ativado via parâmetro, para fatores de risco no  TVP juntamente com a possibilidade de selecionar, via parametrização também, uma Profilaxia default para o mesmo.

## Definição da Regra de Negócio

**RN001 - Parametrização**

Será criado um parâmetro chamado "*Utiliza Sistema de Pontuação Fatores de Risco"* para que seja possível aplicar o sistema de pontuações para Fatores de Risco no TVP.

  Será criado um parâmetro chamado "*Profilaxia Default"* para que uma profilaxia seja marcada, automaticamente, por default no TVP.

**RN002 - Profilaxia da TVP**

  ·         O sistema de pontuação incrementará **1 ponto** para cada fator de risco **exceto** *“Idade > 60 anos”* e *“Trauma Grave”* que contabilizarão **2 pontos**. Essa pontuação servirá para a Classificação de Risco e funcionará da seguinte forma: 

**SE pontuação < 2            = BAIXO**

**SE pontuação** **≥** **2 e < 5 = MÉDIO**

**SE pontuação** **≥** **5           = ALTO**

·           Se o paciente tem mais de 40 anos o Fator de Risco “*Idade > 40 anos”* será selecionado automaticamente.

·           Se o paciente tem mais de 60 anos o Fator de Risco *“Idade > 60 anos”* será selecionado automaticamente. 

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parametrização | [Envolvida] | Opções -> Parâmetros / Parâmetros Gerais - aba Prontuário Eletrônico | **RN001** |
| Profilaxia da TVP | [Alteração] | Prontuário Eletrônico - aba Anamnese / Exame Físico | **RN002** |

**Exemplo de Aplicação:**

* Acesse **Opções / Parâmetros / Parâmetros Gerais,** aba Prontuário Eletrônico, sub aba Geral II.
* Marque o parâmetro *“Utiliza Sistema de Pontuação Fatores de Risco”* e selecione uma *“Profilaxia default”.*
* Acesse o Prontuário Eletrônico, selecione um paciente.
* Se o paciente tem mais de 40 anos o Fator de Risco “*Idade > 40 anos”* será selecionado automaticamente.
* Se o paciente tem mais de 60 anos o Fator de Risco *“Idade > 60 anos”* será selecionado automaticamente.
* O sistema de pontuação incrementará **1 ponto** para cada fator de risco **exceto** *“Idade > 60 anos”* e *“Trauma Grave”* que contabilizarão **2 pontos**.
* O parâmetro “*Profilaxia Default”* fará com que a profilaxia a ser utilizada no TVP venha selecionada por default.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
