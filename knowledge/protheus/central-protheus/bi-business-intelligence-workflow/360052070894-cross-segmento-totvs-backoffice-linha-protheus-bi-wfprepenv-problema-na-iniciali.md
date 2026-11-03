---
article_id: 360052070894
category: BI - Business- Intelligence - Workflow
content_hash: cd6e159a3689fabed998163b0677be2f42341f8276db7895c59631c013433fb1
fetched_at: '2026-06-28T22:37:03.077157+00:00'
product: protheus
section_id: 1500001550762
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - [WFPREPENV] Problema
  na inicialização de ambiente
type: support-article
updated_at: '2022-02-15T19:01:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052070894-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-WFPREPENV-Problema-na-inicializa%C3%A7%C3%A3o-de-ambiente
---

**Ocorrência**Ao tentar disparar um Workflow, o Protheus retorna o seguinte erro durante o processo:

[ERROR][SERVER] [Thread 15316 - 0 - 1596746238] ListenerClientERROR Connect : Thread not found (000001CADC975600). (wait: 1)  
[06/08|17:37] Descrição do erro (prepare environment): Saída no final: Inconsistência no ambiente.\_  
Foram encontrados os seguintes erros no ambiente:  
O servidor de licenças não está respondendo, entre em contato com o administrador do sistema.  
**A chave TopMemoMega não foi localizada no AppServer.INI**

[WFPREPENV] Problema na inicialização de ambiente  
   
 **Ambiente**MP – BI – A partir da versão 12.1.23  
   
 **Causa**Este erro ocorreu pois a chave **TopMemoMega=1** não estava inserida dentro do **AppServer.ini**  
   
 **Solução**Para correção do ocorrido, basta inserir a chave **TopMemoMega=1** dentro do Environment no **AppServer.ini** conforme o exemplo abaixo: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360084767313/mceclip0.png)**

**Saiba mais:  
[Chave TopMemoMega](https://tdn.totvs.com/display/tec/TOPMemoMega)**
