---
article_id: 4433672227863
category: Rescisão
content_hash: 3732e828305c3e918f04108b6f365430dce12948df2dc96ac2661f427e938937
fetched_at: '2026-06-28T22:46:54.418643+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Transferência: Coligada destino não aparece na seleção de
  coligadas'
type: support-article
updated_at: '2026-05-04T16:58:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4433672227863-RH-RM-FOP-Transfer%C3%AAncia-Coligada-destino-n%C3%A3o-aparece-na-sele%C3%A7%C3%A3o-de-coligadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40216687915415) Tempo aproximado para leitura: **00:01:26min**  
  
**Ocorrência**  
No módulo da Folha de Pagamento, ao realizar a transferência entre coligadas não está sendo apresentada a coligada destino na seleção de coligadas e ao tentar inserir o código manualmente aparece o erro: "valor inválido para o campo CODCOLIGADA".  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4433681790359) ![Captura de tela 2026-05-04 110538.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40216703885847)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a competência das coligadas de origem e destino estão divergentes.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verifique se as coligadas de origem e destino estão com a competência e ano divergentes;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10376141998871)  
  
2. Caso estejam divergentes, será necessário realizar a liberação de competência, para que as coligadas de origem e destino estejam com a competência e ano iguais;  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10376191568023)  
  
**Saiba Mais**  
[RH - RM - FOP - Liberação de Competência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060636393-RH-RM-FOP-Libera%C3%A7%C3%A3o-de-Compet%C3%AAncia#:~:text=Para%20realizar%20a%20libera%C3%A7%C3%A3o%20de,ir%C3%A1%20definir%20quais%20ir%C3%A1%20atualizar.)
