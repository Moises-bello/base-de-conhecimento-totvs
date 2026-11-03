---
article_id: 360007259792
category: eSocial - Gerar XML/ Integração Evento
content_hash: 645b5eeb1b7709709708f473efc5a38e7ee8e8647436c03433de0f6b04295966
fetched_at: '2026-06-28T22:47:13.187024+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RM - eSocial - Erro ao integrar S-2230: O término do afastamento informado
  não possui o registro predecessor'
type: support-article
updated_at: '2024-07-22T17:14:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007259792-RM-eSocial-Erro-ao-integrar-S-2230-O-t%C3%A9rmino-do-afastamento-informado-n%C3%A3o-possui-o-registro-predecessor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25079953162775) Tempo aproximado para leitura: 00:02:30 min**

**Ocorrência**Ao tentar integrar um término de afastamento (S-2230) é apresentado o erro **O término do afastamento informado não possui o registro predecessor, essa informação é obrigatória para relacionar ao seu respectivo início de afastamento.** sendo que o início do afastamento já foi enviado corretamente para o RET.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360007844051)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões.  
  
**Causa**O TAF rejeita o término do afastamento porque o início do afastamento foi enviado como **Inclusão** e o correto seria **Início**.  
  
**Solução**  
Para solucionar essa ocorrência, será necessário executar um *script* que irá alterar o tipo de operação do S-2230 para **Início** quando o status for **Aceito TAF** ou **Aceito RET** e tipo de operação igual a **Inclusão**, após executar o Script gere novamente o XML do gatilho do término do afastamento que foi rejeitado pelo TAF e refaça o processo novamente para transmitir ao RET.  
  
**Importante**O *script* irá atualizar somente os registros anteriores que foram enviados como inclusão, com os últimos patch's disponíveis do RM a situação não será recorrente.  
  
**Saiba mais**Para mais informações acesse:  
      • [Como executar Scripts](https://tdn.totvs.com/display/LRM/Executor+de+Scripts+RM)  
      • [Download do Script (Oracle e SQL)](https://suporte.totvs.com/portal/p/10098/download?e=697791)
