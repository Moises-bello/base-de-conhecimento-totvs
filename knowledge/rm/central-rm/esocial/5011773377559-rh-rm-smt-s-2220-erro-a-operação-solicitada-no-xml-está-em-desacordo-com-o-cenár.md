---
article_id: 5011773377559
category: eSocial
content_hash: a9d472d55932842e48cb9cf8a95e2be5c6af45f6811161c3d0c9a53fa8a4ff33
fetched_at: '2026-06-28T22:47:39.092010+00:00'
product: rm
section_id: 1500000912221
source: central-rm
title: 'RH - RM - SMT - S-2220: Erro: "A operação solicitada no XML está em desacordo
  com o cenário do registro na base do TAF"'
type: support-article
updated_at: '2024-09-26T14:19:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5011773377559-RH-RM-SMT-S-2220-Erro-A-opera%C3%A7%C3%A3o-solicitada-no-XML-est%C3%A1-em-desacordo-com-o-cen%C3%A1rio-do-registro-na-base-do-TAF
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035676287639) **Tempo aproximado para leitura:** **00:01:00 min** **Dúvida**Ao integrar o evento S-2220 com o TAF, há o retorno com a seguinte mensagem de erro: A operação solicitada no XML está em desacordo com o cenário do registro na base do TAF. O que fazer?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão 12.1.28  
  
**Solução**A  inconsistência geralmente ocorre ao retificar um evento do S-2220 já enviado anteriormente, onde ocorre modificação do campo **Data de emissão do ASO**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26643284482583)

A tag '**dtAso'** é uma informação chave para o eSocial. Para enviar como retificação o campo de ser igual ao evento de inclusão.  
![](https://totvssuporte.zendesk.com/attachments/token/PQrLsEtiundCfdb0qyXXTY7rj/?name=inline346108211.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/8xiItBBpMpyXeIGVNU2bn0k2q/?name=inline1595729591.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/QMoPuE9NgALsQBdZlgsj0Vfys/?name=inline-1595229551.png)  
  
No caso de alteração da data de emissão do ASO, deve ser realizado a exclusão do evento através do S-3000 e logo depois realizar o ajuste necessário na consulta medica, para assim gerar um novo gatilho de inclusão com a data correta. 

**Saiba Mais:**

Para maiores informações, acesse:

- [RH - RM - SMT - Gerar o evento S-2220 - Monitoramento da Saúde do Trabalhador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010325282)

- [RH - RM - FOP - eSocial - Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)
