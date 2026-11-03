---
article_id: 360052173974
category: RH - Soluções para error.log
content_hash: 8c8be52a2bd12d0eb5aab30862f11919528540bae1879fdfd3c22c6f9a191169
fetched_at: '2026-06-28T22:44:08.896860+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: RH - Linha Protheus - GPE - Error log ao realizar Integração de Títulos - invalid
  typecast in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-tecx17v3r1-tecxwin64\advpl\instrvar.inl
  at line 932  on FGRAVTIT(GPEM650.PRX)
type: support-article
updated_at: '2024-06-20T13:49:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052173974-RH-Linha-Protheus-GPE-Error-log-ao-realizar-Integra%C3%A7%C3%A3o-de-T%C3%ADtulos-invalid-typecast-in-file-d-bamboo-agent-5-7-2-xml-data-build-dir-tp11-tecx17v3r1-tecxwin64-advpl-instrvar-inl-at-line-932-on-FGRAVTIT-GPEM650-PRX
---

**Ocorrência**  
Ao realizar uma **Integração de Títulos**, através da rotina **GPEM650**, é gerado ***error log**: "**invalid typecast in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-tecx17v3r1-tecxwin64\advpl\instrvar.inl at line*** **932** ***on*** **FGRAVTIT(GPEM650.PRX)***"***Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
 **Causa**Este erro ocorre devido a configuração incorreta do parâmetro de verificação de duplicidade de títulos  
  
**Solução  
1.** Para solucionar essa ocorrência, necessário corrigir o parâmetro **MV\_CONDUPL**, que deve estar conforme abaixo:![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360083961154)  
  
**Obs.**: O valor do campo **Cont. Por** pode possuir .F. ou .T., de acordo com a necessidade de seu ambiente, conforme descrito na documentação abaixo a funcionalidade deste parâmetro:  
[TSXBDD\_DT\_Consistir\_Duplicidade\_de\_Títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=204966712)  
  
**Saiba mais:**  
Pacote Acumulado do RH:  
[MP - GPE - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-MP-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-Gest%C3%A3o-de-Pessoal?source=search)  
Pacote Acumulado e-Social: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234>
