---
article_id: 26738575490583
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 1289ee658d01b6273dca77345dc61489bea3e36f94a22f4c944c34b2fe5d2213
fetched_at: '2026-06-28T22:37:49.199933+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA713 - Para transmissão de
  títulos é necessário a configuração da rotina no Schedule
type: support-article
updated_at: '2026-01-07T17:42:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26738575490583-Cross-Segmentos-Backoffice-Linha-Protheus-FINA713-Para-transmiss%C3%A3o-de-t%C3%ADtulos-%C3%A9-necess%C3%A1rio-a-configura%C3%A7%C3%A3o-da-rotina-no-Schedule
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26738589877015) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar acessar a rotina FINA710 - Monitor de Pendências, é exibida a seguinte mensagem: **"Para transmissão automática de títulos é necessário a configuração da rotina FINA713 no Schedule do Módulo Configurador"**, porém, o JOB está cadastrado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26738589878295)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

Esse incidente ocorre devido a uma parametrização incorreta do JOB por meio do Configurador para o uso de transmissão, o que impede que a rotina reconheça o cadastro do JOB.

**Exemplo:** **JOB** sem **grupo de Empresas**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26738575475223)  
  
**Solução**

É necessário excluir o **JOB** e recriá-lo conforme o modelo abaixo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26738575475991)

Dessa forma, ao acessar a rotina, a mensagem não será mais exibida.  
  
**Saiba mais**

[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
