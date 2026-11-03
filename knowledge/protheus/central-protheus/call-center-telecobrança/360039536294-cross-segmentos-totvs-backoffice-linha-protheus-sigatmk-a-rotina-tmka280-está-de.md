---
article_id: 360039536294
category: Call Center - Telecobrança
content_hash: 3dfd3f31d86896ce8f0e7724f493dd79cc2d8e42ba2c96149a9c55f4a342de99
fetched_at: '2026-06-28T22:41:28.689818+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK-A rotina tmka280
  está desatualizada
type: support-article
updated_at: '2022-06-22T17:34:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039536294-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-A-rotina-tmka280-est%C3%A1-desatualizada
---

**Dúvida**

Ao acessar um atendimento de cobrança no pré-atendimento, aparece a mensagem que a rotina **tmka280** esta desatualizada:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052362934/mceclip0.png)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- a partir da release 12.1.17.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote da rotina **Finxapi**para a versão do ambiente utilizado:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=844661> ;

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=844660> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=844659> ;

2. Via TDS ou IDE, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.

Procure atualizar o ambiente  com o uso dos pacotes de expedição continua de sua release ao invés de utilizarem apenas pacotes pontuais, eles garantem que o ambiente esteja com a ultimas correções até a data de expedição do pacote, evitando erros e problemas de performance, para download, acesse o endereço:

12.1.17: <https://suporte.totvs.com/portal/p/10098/download#000006/P12117/P12117AP/>

12.1.23: <https://suporte.totvs.com/portal/p/10098/download#000006/P12123/P12123AP/>

12.1.25: <https://suporte.totvs.com/portal/p/10098/download#000006/P12125/P12125AP/>
