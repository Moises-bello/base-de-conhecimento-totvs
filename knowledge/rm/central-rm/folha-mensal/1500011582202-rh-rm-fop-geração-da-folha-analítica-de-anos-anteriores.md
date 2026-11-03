---
article_id: 1500011582202
category: Folha Mensal
content_hash: 9358ba0936d9071cb0d52ae0de166f92e46709de65ce40da1740ac6a6bfd5d67
fetched_at: '2026-06-28T22:46:59.405598+00:00'
product: rm
section_id: 1500000861062
source: central-rm
title: RH - RM - FOP - Geração da Folha Analítica de anos anteriores
type: support-article
updated_at: '2025-01-21T18:12:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011582202-RH-RM-FOP-Gera%C3%A7%C3%A3o-da-Folha-Anal%C3%ADtica-de-anos-anteriores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao gerar a folha analítica para anos anteriores, aparece o aviso: **Ficha financeira anterior a 24 meses foi movida para ficha financeira complementar**. Como prosseguir com a geração da Folha Analítica?  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018958141/mceclip0.png)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Por questões de desempenho, o sistema transfere as movimentações da ficha financeira para o arquivo morto chamado ficha financeira complementar. Dessa forma, quando acessar a rotina, não há necessidade de carregar toda a movimentação do funcionário, o que poderia ocasionar lentidão.  
  
Essa parametrização do período a ser enviado para a complementar é configurada no menu **Configurações | Parametrizador  | Folha Normal  | Ficha financeira.**  
![](https://totvssuporte.zendesk.com/attachments/token/tAioz96DmEmDn9Wb8Bs2h1Z1y/?name=inline-1779533510.png)​  
  
Ao gerar a rotina de folha analítica, o sistema busca as informações na ficha financeira do funcionário. Na necessidade de gerar folha analítica de anos anteriores, basta restaurar a movimentação do funcionário, retirando-a da ficha complementar e transferindo para ficha financeira. Para este processo, acesse o menu **Folha Mensal  | Ficha Financeira | Restaurar Ficha Financeira.**  
![](https://totvssuporte.zendesk.com/attachments/token/OV2piNnNXkkKxbajaK0JVSdfD/?name=inline1344499657.png)  
  
Nos parâmetros, informar o período ao qual deseja restaurar para gerar a folha analítica.   
  
![](https://totvssuporte.zendesk.com/attachments/token/y0gli5Dv1kVA2BK7wUyoBfmTZ/?name=inline-553636783.png)  
  
Após realizar a restauração, será possível gerar o relatório de folha analítica.
