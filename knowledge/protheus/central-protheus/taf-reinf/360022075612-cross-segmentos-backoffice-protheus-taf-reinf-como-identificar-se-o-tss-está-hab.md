---
article_id: 360022075612
category: TAF - REINF
content_hash: 0f76cf457ab914486fd4a11d49932ec7860e32b1769c3cd2655a04af859f7623
fetched_at: '2026-06-28T22:41:33.705144+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como identificar se o
  TSS está habilitado para utilizar a Reinf
type: support-article
updated_at: '2023-04-04T12:08:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022075612-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-identificar-se-o-TSS-est%C3%A1-habilitado-para-utilizar-a-Reinf
---

**[*Remover as instruções entre colchetes*]****Dúvida**Como identificar se o TSS está habilitado para utilizar a Reinf?   
  
**Ambiente**TAF- TSS- REINF- A partir da versão 12.01.17

**Solução**

A transmissão da REINF deve ser realizada pelo TSS 3.0, no TSS 2.0 você consegue transmitir, mas o TSS não consegue processar o retorno. Isso ocorre quando no TAF o Evento fica com o status de Transmitindo/Aguardando.

Onde eu baixo o instalador do TSS 3.0

Windows

<https://suporte.totvs.com/portal/p/10098/download#detail/947638>

Linux

<https://suporte.totvs.com/portal/p/10098/download#detail/947642>

Se o TSS 3.0 já foi instalado você deve validar se o arquivo Appserver.ini existe a chave que liga o TSS 3.0.

O arquivo Appserver.ini fica dentro da estrutura do TAF/Protheus, na pasta APPSERVER;

Exemplo:C:\TOTVS 12\Microsiga\Protheus\bin\appserver

Na sessão Ambiente deve existir a chave TSSOndemand=1

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019113991/mceclip0.png)

Outro detalhe é que o novo TSS utiliza novos JOBS.

[ONSTART]  
JOBS = JOB\_HTTP,JOB\_WS,IPC\_ONDEMAND,IPC\_CONT,TSSTASKPROC

Lembrando que o TSS 3.0 não utiliza o JOBNFE, a transmissão da NF não utiliza mais esse JOB no 3.0, se você incluir esse JOB no Appserver vai gerar problema na transmissão da Reinf.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019114211/mceclip1.png)

Sempre utilizar a URL da sessão HTTP

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019252992/mceclip2.png)
