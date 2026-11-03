---
article_id: 360016068372
category: RH - Leitura e Apontamento
content_hash: bdff68095f7f3c683a22dd1bf976b4e095779a9f7c4c3c1e7ee00f174d9b12c1
fetched_at: '2026-06-28T22:44:46.021855+00:00'
product: protheus
section_id: 32419281460119
source: central-protheus
title: 'RH - Linha Protheus - PON - Tabela RFB: funcionalidade e como controlar a
  leitura para evitar que o NSR gere erros no processo'
type: support-article
updated_at: '2026-03-13T18:01:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068372-RH-Linha-Protheus-PON-Tabela-RFB-funcionalidade-e-como-controlar-a-leitura-para-evitar-que-o-NSR-gere-erros-no-processo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31928161546391) Tempo aproximado para leitura: 00:01:00 min  
  
Dúvida**Qual a funcionalidade da tabela RFB e como controlar a leitura para que o NSR gere erros no processo de leitura?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**A tabela RFB grava o registro do último NSR de cada leitura para cada REP cadastrado, controlando o NSR para evitar marcação duplicada ou pré-leitura de um dia que já foi processado.   
O NSR é único e exclusivo por marcação de cada REP e é incremental e crescente, ou seja, o NSR da marcação exemplo do dia 19/05 é maior que o do dia 18/05.  
  
O responsável pela leitura precisa ler e apontar o relógio de forma cronológica, ou seja, suponhamos que o período de apontamento é de 01/05 a 30/05, logo, deve ser efetuada a coleta e leitura de forma que não seja necessário ler dias anteriores.  
Por exemplo: se de 01/05 a 07/05 já foram coletados no txt e lidas as marcações, o dia 03/05 não pode ser lido novamente, pois o NSR do dia 03.05 é menor que o último lido de 07/05.  
  
**Importante**: A tabela RFB sempre é gravada por REP, o último NSR lido.   
Exemplo: o último NSR lido para o REP 002 possui número de NSR 000123456, o sistema lê neste caso do próximo que seria 0001234567 pra frente, nunca para trás. Essa particularidade deve ser verificada e controlada por quem realiza este processo de leitura e apontamento.  
  
  
**Saiba Mais:**[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
