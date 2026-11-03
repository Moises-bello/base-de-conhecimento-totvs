---
article_id: 24345658484631
category: TAF - eSocial - Eventos Não Periódicos
content_hash: ec39aaf9a18d69ba5b7f4162f8830cf90de10486b7a9445fedd31a98a09e2300
fetched_at: '2026-06-28T22:45:18.118119+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos de Medicina - S-2210 - Ocorrência
  188 - Descrição: Agente causador invalido. Acao Sugerida: O valor informado deve
  ser um codigo valido, existente em uma das tabelas 14 (Agente Causador do Acidente
  de Trabalho'
type: support-article
updated_at: '2026-06-24T20:52:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24345658484631-RH-Linha-Protheus-TAF-eSocial-Eventos-de-Medicina-S-2210-Ocorr%C3%AAncia-188-Descri%C3%A7%C3%A3o-Agente-causador-invalido-Acao-Sugerida-O-valor-informado-deve-ser-um-codigo-valido-existente-em-uma-das-tabelas-14-Agente-Causador-do-Acidente-de-Trabalho
---

**Ocorrência**

Erro - Codigo da ocorrência: 188

Localização: /eSocial/evtCAT/cat/agenteCausador/codAgntCausador

Descrição: Agente causador invalido.Acao Sugerida: O valor informado deve ser um codigo valido, existente em uma das tabelas 14 (Agente Causador do Acidente de Trabalho) ou 15 (Agente Causador / Situacao Geradora de Doenca Profissional), conforme a data e o codigo do acidente informados.

**Ambiente**

TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Eventos de Medicina - S-2210 - Todas as versões

**Solução**

Caso a data do acidente seja posterior ao mês 01/2024 e o tipo de acidente igual a 1 ou 3, deverá selecionar um dos códigos do agente causador da tabela 14 do manual do esocial abaixo:

<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-1-2-nt-02-2024/tabelas.html#14>

Regra de validação no MOS:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24345688846103)

Os códigos das tabelas 14 e 15 estão localizados no mesmo campo na rotina do evento S-2210 no TAF:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24345688847767)

Importante: Para que os códigos sejam apresentados corretamente é necessário que o TAF esteja atualizado com o dicionário e RPO, e que a wizard do TAF seja executada.

Verifique também os artigos abaixo:

[RH - Linha Protheus - TAF - eSocial - Medicina - S-2210 - Como acessar a Rotina de Comunicação de Acidentes de Trabalho no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008566602-RH-Linha-Protheus-TAF-eSocial-Medicina-S-2210-Como-acessar-a-Rotina-de-Comunica%C3%A7%C3%A3o-de-Acidentes-de-Trabalho-no-TAF?source=search)

[RH - Linha Protheus - TAF - ATUALIZAÇÃO - Como atualizar o TAF E-social (Expedição Contínua)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18972648169239-RH-Linha-Protheus-TAF-ATUALIZA%C3%87%C3%83O-Como-atualizar-o-TAF-E-social-Expedi%C3%A7%C3%A3o-Cont%C3%ADnua?source=search)

Cross Segmentos - Backoffice Protheus - TAF - REINF - Wizard Configuração do TAF.: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/6172197751447?source=search>
