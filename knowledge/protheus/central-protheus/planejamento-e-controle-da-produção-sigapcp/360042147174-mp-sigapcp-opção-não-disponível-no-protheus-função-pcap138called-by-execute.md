---
article_id: 360042147174
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 44bf939663cb9859a11a79560f8051eb4c242de9239daf848c530ab7b084940e
fetched_at: '2026-06-28T22:42:47.322243+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'MP - SIGAPCP - Opção não disponível no Protheus Função: PCAP138Called By_Execute '
type: support-article
updated_at: '2020-01-28T17:20:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042147174-MP-SIGAPCP-Op%C3%A7%C3%A3o-n%C3%A3o-dispon%C3%ADvel-no-Protheus-Fun%C3%A7%C3%A3o-PCAP138Called-By-Execute
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:00:40 min**  
 **Ocorrência**Ao acessar a rotina de **Apontamento Pendente - PCPA138** é apresentada a mensagem:  
**Help: NOFUNCW****Problema: Opção não disponível no Protheus Função:****PCAP138Called By\_\_Execute**

![KCS.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360056146474/KCS.PNG)

**Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
   
 **Causa**Essa mensagem ocorre pois a chamada do programa no **SIGACFG - Configurador** está incorreta.  
   
 **Solução**No **SIGACFG** acesse **Ambiente** > **Cadastros** > **Menus**, selecione o modulo desejado, clique em **OK**, clique em **Adicionar,** posicione no **Apontamento pendente** e clique em **Detalhes,** altere o campo **Programa** para **PCPA138,** clique em **OK,**após isso clique em **Gerar**.

![KCS_2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360056146894/KCS_2.PNG)
