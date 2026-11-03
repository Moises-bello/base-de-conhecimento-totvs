---
article_id: 360044698374
category: esocial - Periódicos
content_hash: 0b34c758adb77c0a29caccc518f4a953e12948dab6397841fdf18d6bb765099f
fetched_at: '2026-06-28T22:47:09.529515+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RM - eSocial - Erro ao gerar periódicos: O campo compAcConv do registro ideAdc
  é obrigatório e não está preenchido (v.2.5)'
type: support-article
updated_at: '2022-07-05T14:17:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044698374-RM-eSocial-Erro-ao-gerar-peri%C3%B3dicos-O-campo-compAcConv-do-registro-ideAdc-%C3%A9-obrigat%C3%B3rio-e-n%C3%A3o-est%C3%A1-preenchido-v-2-5
---

**Ocorrência**Ao gerar o **XML** de eventos periódicosocorre o erro **O****campo compAcConv do registro ideAdc é obrigatório e não esta preenchido**.  
  
**Ambiente**RM - eSocial - Todas as versões  
  
**Causa**Este erro ocorre quando é gerado um evento periódicos que possui verbas associadas à um acordo coletivo porém não foi preenchida a competência acordada para pagamento das verbas.  
  
**Solução**Para solucionar este erro realize os passos abaixo:  
1. Acesse em**Folha de Pagamento | eSocial | Acordo coletivo/Reajuste por Lei** e edite o acordo coletivo utilizado no lançamento das verbas;  
2. Preencha os campos **Mês** e **Ano** em **Competência acordada para pagamento;**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062190553/mceclip0.png)**

3. Após, gere novamente o XML.  
  
**Importante**A competência acordada para pagamento não poderá ser menor que a competência que está sendo apurada as verbas.  
Documentação válida somente para leiaute eSocial anterior à versão S-1.0
