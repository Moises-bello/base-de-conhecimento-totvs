---
article_id: 30318851542167
category: eSocial
content_hash: fac2f219063460e37c4653e1a7b328e9fb12662d87c3fdaaa24edad7be51c7be
fetched_at: '2026-06-28T22:47:15.301633+00:00'
product: rm
section_id: 11645725240471
source: central-rm
title: 'RH - RM - RHU - Evento S-2555 - Erro: Para aceitação do evento S-2555, é necessária
  a existência de pelo menos um evento S-2501 com nrProcTrab = XXXXXXXXXXXXXXXXXXXX,
  perApurPgto = XXXX-XX e com ideSeqProc preenchido.'
type: support-article
updated_at: '2025-09-19T19:34:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30318851542167-RH-RM-RHU-Evento-S-2555-Erro-Para-aceita%C3%A7%C3%A3o-do-evento-S-2555-%C3%A9-necess%C3%A1ria-a-exist%C3%AAncia-de-pelo-menos-um-evento-S-2501-com-nrProcTrab-XXXXXXXXXXXXXXXXXXXX-perApurPgto-XXXX-XX-e-com-ideSeqProc-preenchido
---

**Dúvida**Ao cadastrar o evento S-2555 é apresentada a mensagem de erro: **Para aceitação do evento S-2555, é necessária a existência de pelo menos um evento S-2501 com nrProcTrab = XXXXXXXXXXXXXXXXXXXX, perApurPgto = XXXX-XX e com ideSeqProc preenchido.**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Gestão de Pessoas - **12.1.2402.245**, **12.1.2406.185**, **12.1.2410.121 e superiores.**  
  
  
**Solução**O campo 'Sequencial' deverá ser preenchido no momento da inclusão do Evento S-2501. O campo deve ser preenchido somente nos casos em que o processo trabalhista possuir mais de um reclamante.

![Campo sequencial.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30318851504919)

De acordo com o Leiaute do eSocial, o número sequencial é atribuído pela empresa a cada conjunto de dados de tributos decorrentes de processo trabalhista, quando for necessário enviar o mesmo processo em múltiplos S-2501, para o mesmo perApurPgto.  
  
**Importante**  
Não havendo mais reclamante, não é necessário realizar o envio do evento S-2555.  
  
**Saiba Mais**  
Para maiores informações sobre o cadastro, acesse os links abaixo:  
[RH - RM - RHU - Processos Trabalhistas: Dúvidas quanto ao preenchimento do campo 'Sequencial'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30192023184279-RH-RM-RHU-Processos-Trabalhistas-D%C3%BAvidas-quanto-ao-preenchimento-do-campo-Sequencial)  
[RH - RM - RHU - Processos Trabalhistas: Preenchimento indevido do campo 'Sequencial'](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30198505796887-RH-RM-RHU-Processos-Trabalhistas-Preenchimento-indevido-do-campo-Sequencial)  
[RH - RM - RHU - eSocial: S-2501 - Mapeamento dos campos para geração do evento S-2501](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18863423016855-RH-RM-RHU-eSocial-S-2501-Mapeamento-dos-campos-para-gera%C3%A7%C3%A3o-do-evento-S-2501)
