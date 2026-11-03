---
article_id: 360024784994
category: Atualização
content_hash: 7926cbe596720d86e6d5f8156aa818dad992f356d9eb7a12ad8e11cce7907364
fetched_at: '2026-06-28T22:42:21.331327+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus - FRAME - Memory Full Memory Allocation Failure
type: support-article
updated_at: '2022-06-08T20:53:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024784994-Framework-Linha-Protheus-FRAME-Memory-Full-Memory-Allocation-Failure
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*** Tempo aproximado para leitura: **00:01:30 min  
  
Dúvida**  
Por qual motivo a mensagem **Memory Full Memory Allocation Failure** é exibida no Sistema?  
  
**Ambiente**  
Framework - Framework (Linha Protheus) - AppServer - A partir da Versão 12.  
  
**Solução**  
Esta mensagem é reproduzida no Servidor de Aplicação quando este solicitou ao Sistema Operacional uma determinada quantidade de memória, e o Sistema Operacional não conseguiu devolver para o **TOTVS Application Server** o endereço correspondente à alocação solicitada.  
  
Maiores detalhes sobre esta mensagem, acesse o *link*: [Memory full Memory Allocation Failure](http://tdn.totvs.com/display/tec/memory+full++Memory+Allocation+Failure)  
  
**Importante**  
Em casos de problemas de memória, sugerimos utilizar o **Balanceamento de Carga**, e se já utiliza, aumentar o número de **Slaves** do balanceamento. Para mais informações sobre o Balanceamento de Carga, acesse o *link*: [Balanceamento de carga entre serviços (Load Balance)](http://tdn.totvs.com/display/tec/Balanceamento+de+carga)
