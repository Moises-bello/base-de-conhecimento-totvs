---
article_id: 360014211431
category: RH - Rescisão
content_hash: 935a4e7a96bce9252a10c543597e76f1d8379e54fda8def889bbc283d23c962b
fetched_at: '2026-06-28T22:43:48.517259+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: 'RH - Linha Protheus - GPE - Cálculo de Rescisão apresenta Help: Registro sendo
  enviado ao RET'
type: support-article
updated_at: '2025-06-13T11:53:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360014211431-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Rescis%C3%A3o-apresenta-Help-Registro-sendo-enviado-ao-RET
---

**Ocorrência**No cálculo da rescisão é gerada a mensagem abaixo:  
  
*Help*: Registro sendo enviado ao RET  
Problema: Registro de Admissão do Funcionário está em trânsito TAF x RET. Verifique no sistema TAF. A rescisão não será efetivada.   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**A mensagem apresentada informa que o **S-2200** ainda não possui recibo, e portanto a movimentação de transferência não pode ser efetivada até que tenha o recibo.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Abrir o monitor do TAF;  
2. Pesquisar o funcionário em questão;  
3. Clique em detalhamento;  
4. Confirme se o *Status* do mesmo encontra-se como **4 - Aceito pelo RET.**
