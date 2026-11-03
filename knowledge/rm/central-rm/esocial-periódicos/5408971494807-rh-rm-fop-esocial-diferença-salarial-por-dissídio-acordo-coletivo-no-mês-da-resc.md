---
article_id: 5408971494807
category: esocial - Periódicos
content_hash: 692c960f4d48435ec9cc652a4f63087479022b3d2a4a534935a07e84bf0dc869
fetched_at: '2026-06-28T22:47:09.239480+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Diferença salarial por dissídio/ acordo coletivo
  no mês da rescisão
type: support-article
updated_at: '2025-02-26T19:35:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5408971494807-RH-RM-FOP-eSocial-Diferen%C3%A7a-salarial-por-diss%C3%ADdio-acordo-coletivo-no-m%C3%AAs-da-rescis%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar a diferença salarial por dissídio/ acordo coletivo no mês da rescisão no evento S-1200?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**Quando no mês da rescisão houver diferença salarial por dissídio e o evento S-2299 já tiver sido enviado ao governo, deve-se enviar um evento S-1200 com as informações do pagamento do dissídio. 

Para isso, ao gerar a rescisão complementar marque o parâmetro **Pagamento de dissídio na competência do desligamento após o envio do S-2299**.

![](https://tdn.totvs.com/download/attachments/570997503/image2020-11-5_17-8-13.png?version=1&modificationDate=1604610811903&api=v2)

Após o cálculo da rescisão complementar com o parâmetro marcado, basta gerar o *XML* periódico S-1200 para o funcionário.

![](https://tdn.totvs.com/download/attachments/570997503/image2020-11-5_17-12-44.png?version=1&modificationDate=1604610811787&api=v2)

Lembrando que o gatilho do S-1200 não será gerado automaticamente, será necessário executar a rotina do menu **eSocial | Gerar XML** (Evento Periódicos).  
  
**Importante**Este parâmetro **deve ser marcado somente** quando o pagamento do **dissídio** for realizado na **mesma competência da demissão** do funcionário e **após ter enviado o evento S-2299** para o governo.

Marcando este parâmetro, as informações do dissídio serão levadas no evento S-1200.

Se fizer o lançamento do dissídio **sem marcar este parâmetro**, caso o pagamento do dissídio seja na **mesma competência da demissão** do funcionário, será necessário fazer uma **retificação do evento S-2299** para contemplar as informações do dissídio.  
  
**Saiba mais**  
Para mais informações, acesse:  
     - [Rescisão Complementar](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452718921)
