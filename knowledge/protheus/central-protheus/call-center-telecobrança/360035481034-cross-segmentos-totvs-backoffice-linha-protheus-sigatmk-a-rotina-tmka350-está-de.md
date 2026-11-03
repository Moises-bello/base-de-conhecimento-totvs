---
article_id: 360035481034
category: Call Center - Telecobrança
content_hash: 95a1846a52d76aa8b0c6df6afb418d51dc0f4fce41d625806b1e62b4ca7fdefb
fetched_at: '2026-06-28T22:41:28.629232+00:00'
product: protheus
section_id: 1500001548222
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- A rotina tmka350
  está desatualizada
type: support-article
updated_at: '2022-06-22T17:28:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035481034-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-A-rotina-tmka350-est%C3%A1-desatualizada
---

**Dúvida**Após a atualização das Procedures, ao executar as rotinas de Agenda de Operador (**tmka380**) ou Atendimento Receptivo(**tmka350**) no SIGATMK, o sistema esta apresentando erro de Procedure:

![](https://totvssuporte.zendesk.com/attachments/token/3JWcl8QLDlkXIBAFpVpQHwF1Y/?name=image001.png)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047086773/mceclip0.png)  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- A partir da release 12.1.17.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Aplique o pacote da rotina **Finxapi** para a versão do ambiente utilizado:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=798109> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=798108> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=798107> ;

2. Via TDS ou IDE, aplique o pacote no RPO;

3. Reinicie o smartclient e refaça o processo.

**Obs:** Para aplicação de pacotes é necessário o conhecimento em estrutura Protheus.

Em caso de dúvidas para a aplicação, consulte a equipe de Framework para auxiliar.

Sempre aplique pacotes ao RPO em ambiente de homologação para validar, efetuando os devidos backups, para posteriormente aplicar em ambiente de produção.
