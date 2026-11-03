---
article_id: 360034193813
category: Gestão de Armazenagem (WMS)
content_hash: 3ec5650040f93e9c28c8a91fa5cecf6486bcab3394cb9ec5bcdf12b36bc7d4b8
fetched_at: '2026-06-28T22:45:48.049783+00:00'
product: protheus
section_id: 206962247
source: central-protheus
title: Logística - Linha Protheus - WMS - Gerar trace, console e logprofile
type: support-article
updated_at: '2022-11-11T16:28:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034193813-Log%C3%ADstica-Linha-Protheus-WMS-Gerar-trace-console-e-logprofile
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:12 min**  
**Dúvida**Como gerar **trace**, **console** e **logprofile**?  
  
**Ambiente**TOTVS Logística - TOTVS WMS (Linha Protheus) - Gestão de Armazenagem (WMS) - A partir da versão 11.80  
  
**Solução**Para gerar o **trace**, o **console** e o **logprofile** para análise do seu ambiente **Protheus**, siga o procedimento a seguir:  
**1**. Pare o serviço de aplicação do **Protheus**;  
**2**. Apague o **console.log** dentro da pasta **appserver**, para que seja gerado um novo;  
**3**. Isole um **AppServer** fora do balanceamento de carga, se tiver;  
**4**. No **AppServer.ini** inclua as seguintes chaves:

* Na seção ***Environment***:  
  **LogProfiler=1**  
  **TraceStack=1**
* Na seção **General**:  
  **Consolelog=1**

**5**. Reinicie o serviço do **Protheus**;  
**6**. Entre no Sistema em modo exclusivo e execute o **SmartClient** apontado para esse **AppServer** isolado;  
**7**. Abra o **DBMonitor**, na aba **Usuários** selecione o seu usuário e clique em **Rastrear**;  
**8**. Execute a rotina que está apresentando o problema e ao finalizar o processo, encerre a conexão do **SmartClient** para que o **console.log** seja alimentado com as informações do **logprofile**;  
**9**. Volte ao **DBMonitor** e clique em **Salvar**, com isso será salvo o arquivo com o **trace** do **DBAccess**;  
**10**. Por fim, ao sair do **Protheus** será gerado dentro da pasta **appserver** um novo **console.log**.
