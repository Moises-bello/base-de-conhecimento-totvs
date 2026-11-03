---
article_id: 360049659234
category: RH - Funcionários
content_hash: fb353a8a02a613d4ebd51328a4f99a9020ada88bade51c8172112e86fe4988f2
fetched_at: '2026-06-28T22:43:27.611581+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Como informar para o sistema que o novo afastamento
  é sequencia do anterior
type: support-article
updated_at: '2025-08-18T19:44:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049659234-RH-Linha-Protheus-GPE-Como-informar-para-o-sistema-que-o-novo-afastamento-%C3%A9-sequencia-do-anterior
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16146801223063) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como informar para o sistema que o novo afastamento é sequencia do anterior?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Para afastamento que são sequencia de um afastamento anterior, é necessário **informar o número de sequencia** para que o sistema faça o cálculo correto dos dias a serem pagos pela empresa (15 dias):

**1.** Acesse **Atualizações > Lançamentos > Ausência:**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16146483888407)

Conforme demonstramos na imagem, o afastamento 002 iniciado em 02/12/2018 **tem como numero de sequencia o afastamento anterior 001** que iniciou em 01/01/2018.

Veja que no campo **Dias Empresa** no afastamento 002, está zerado, pois os 15 dias **já foram pagos no afastamento 001.**

**2.** Após informar os campos necessários, clique em confirmar.

**Observações:**

**-**Para que os afastamento sequencias sejam validados no prazo de 60 dias habilite o parâmetro MV\_NDIAEMP, conforme [esta documentação.](https://tdn.totvs.com/pages/releaseview.action?pageId=910009761)

-Não é possível efetuar uma alteração no campo sequencia de um **período que já está fechado**, uma vez que estes campos são atualizados no fechamento da folha.

**Saiba Mais**[RH - Linha Protheus - GPE - Como configurar o sistema para afastamento superior a 15 dias](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgu8T8%2FXQE6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBmmh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzE1MDAwMDQ3NDE0MjItUkgtTGluaGEtUHJvdGhldXMtR1BFLUNvbW8tY29uZmlndXJhci1vLXNpc3RlbWEtcGFyYS1hZmFzdGFtZW50by1zdXBlcmlvci1hLTE1LWRpYXMGOwhUOg5zZWFyY2hfaWRJIikzZDFkYzgzOC1mZjg3LTRiOWItYWQxOS1iMzAyMDc0ZWI1ZDQGOwhGOglyYW5raQk6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIhlhZmFzdGFtZW50byBzdXBlcmlvcgY7CFQ6EnJlc3VsdHNfY291bnRpAmYG--4d75e07bb4303a7dfdcd832ae872bb2597361167)  
[RH - Linha Protheus - GPE - Como validar o CID para contagem correta dos primeiros 15 dias de Atestado pagos pela Empresa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007499691-RH-Linha-Protheus-GPE-Como-validar-o-CID-para-contagem-correta-dos-primeiros-15-dias-de-Atestado-pagos-pela-Empresa)  
[RH - Linha Protheus - GPE - Como é preenchido os campos Dias Pagos (R8\_DPAGOS) e Saldo Dias (R8\_SDPAGAR) na rotina de ausências](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwgCt1nUUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBxWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDA0NDkzNDkxNC1SSC1MaW5oYS1Qcm90aGV1cy1HUEUtQ29tby0lQzMlQTktcHJlZW5jaGlkby1vcy1jYW1wb3MtRGlhcy1QYWdvcy1SOC1EUEFHT1MtZS1TYWxkby1EaWFzLVI4LVNEUEFHQVItbmEtcm90aW5hLWRlLWF1cyVDMyVBQW5jaWFzBjsIVDoOc2VhcmNoX2lkSSIpY2RjMDQ4NDUtNmNiZi00Yjc5LWE2MzgtYmRkNzhiNTM0NWI0BjsIRjoJcmFua2kGOgtsb2NhbGVJIgpwdC1icgY7CFQ6CnF1ZXJ5SSIBgVJIIC0gTGluaGEgUHJvdGhldXMgLSBHUEUgLSBDb21vIMOpIHByZWVuY2hpZG8gb3MgY2FtcG9zIERpYXMgUGFnb3MgKFI4X0RQQUdPUykgZSBTYWxkbyBEaWFzIChSOF9TRFBBR0FSKSBuYSByb3RpbmEgZGUgYXVzw6puY2lhcwY7CFQ6EnJlc3VsdHNfY291bnRpAtAH--1e333872bf7a5fc88330062e130d990a8a52a34f)
