---
article_id: 360027743592
category: ADVPL - Rotina Automática
content_hash: d0ac772b9827d1b237e7c5ee94fe676cf9ab0a442aab2d950560bba97f9702af
fetched_at: '2026-06-28T22:40:24.156629+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL - Problemas com  Integração
  M.E.S via Execauto MATA650
type: support-article
updated_at: '2024-01-26T19:53:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027743592-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Problemas-com-Integra%C3%A7%C3%A3o-M-E-S-via-Execauto-MATA650
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Ocorrência**Utilizo integração **M.E.S** para inclusão de Ordens de Produção. Quando incluo via rotina manual, a **OP** aparece automaticamente nas pendencias do **M.E.S,** porém quando faço o processo via rotina automática a **OP** não aparece nas pendencias.  
  
**Ambiente**  
Protheus – Manufatura – A partir da versão 12  
  
**Causa**Esse incidente ocorre, pois existe uma validação na rotina padrão, a qual avalia a rotina de origem que são permitidas para executar essa integração, essas rotinas são:

```
"MATA650","MATA651","PCPA111","PCPA110","MATA632","MATA380"  
"MATA381","MATA690","MATA712","SFCA310","MATA637","PCPA107"  
"PCPA114"
```

**Solução**Para que a integração funcione a partir da rotina automática **MATA650**, é necessário incluir o parâmetro **FUNNAME** no comando **Prepare Environment**.  
A preparação de ambiente também pode ser realizada pela função **RpcSetEnv** informando o parâmetro **cFunName**.

```
Prepare Environment  
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO 'PCP' FUNNAME 'MATA650'
```

```
RpcSetEnv  
RPCSetEnv("99" , "01",,,"PCP","MATA650",,,,,)
```

**Saiba Mais:  
[Prepare Environment](http://tdn.totvs.com/pages/releaseview.action?pageId=6814708).  
[RpcSetEnv](http://tdn.totvs.com/pages/releaseview.action?pageId=6814927)**
