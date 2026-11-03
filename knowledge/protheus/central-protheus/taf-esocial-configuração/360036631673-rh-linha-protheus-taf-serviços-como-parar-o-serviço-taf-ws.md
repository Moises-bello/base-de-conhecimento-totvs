---
article_id: 360036631673
category: TAF - eSocial - Configuração
content_hash: 7ed8ce22aecff927af7d0f9e7a7cc8ed4c530cdc7cacf4bc16684cc2d76b2c3b
fetched_at: '2026-06-28T22:45:14.447250+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - SERVIÇOS - Como parar o serviço TAF-WS
type: support-article
updated_at: '2026-06-25T11:29:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036631673-RH-Linha-Protheus-TAF-SERVI%C3%87OS-Como-parar-o-servi%C3%A7o-TAF-WS
---

**Dúvida**Ao parar o serviço do TAF-WS, apresenta a mensagem a seguir: **![1.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360047252714)****Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - TOTVS Automação Fiscal - Todas as Releases   
**Solução**1 - Acesse o prompt de comando no Windows (CMD):  
![2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360047252994)

2 - Acesse o Gerenciador de Tarefas do Windows e clique na aba Serviços:  
![3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360047253294)

3 - Procure pelo serviço TAF-WS:  
![4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048138933)

4 - Na coluna PID, há uma sequência numérica que é o Identificador do Processo do serviço em execução. Veja qual código é o serviço TAF-WS. No nosso exemplo, o nosso PID é o 4644:  
![5.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048139373)

5 - Volte para o prompt de comando (CMD) e digite o seguinte comando:  
**taskkill /pid XXXX /f**   
(onde XXXX é o PID do serviço) e tecle “Enter”:  
![6.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360048140313)

6 - Resultando em êxito, o serviço do TAF-WS será finalizado com sucesso, sem a necessidade de reiniciar o servidor ou o PC onde está instalado o serviço do TAF.
