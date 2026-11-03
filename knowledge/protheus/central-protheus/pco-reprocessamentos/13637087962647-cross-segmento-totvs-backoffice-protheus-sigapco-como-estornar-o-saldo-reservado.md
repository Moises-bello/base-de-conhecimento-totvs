---
article_id: 13637087962647
category: PCO - Reprocessamentos
content_hash: 7913d9be14be4cdd470d04bfad11648a9811e9e1258f1eef489a85c79023173c
fetched_at: '2026-06-28T22:37:07.035725+00:00'
product: protheus
section_id: 1500001551022
source: central-protheus
title: Cross Segmento - Totvs Backoffice Protheus - SIGAPCO - Como estornar o saldo
  reservado pelo controle orçamentário na eliminação de resíduos?
type: support-article
updated_at: '2024-10-03T11:08:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13637087962647-Cross-Segmento-Totvs-Backoffice-Protheus-SIGAPCO-Como-estornar-o-saldo-reservado-pelo-controle-or%C3%A7ament%C3%A1rio-na-elimina%C3%A7%C3%A3o-de-res%C3%ADduos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19224125062423) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Como estornar o saldo reservado pelo controle orçamentário na eliminação de resíduos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Planejamento e controle orçamentário - A partir da versão 12.1.25.  
  
**Solução**O correto para esse processo, seria utilizar o lançamento 000056 lançamento de eliminação de resíduos, utilizando o item de eliminação de pedido de compras>  
![](https://totvssuporte.zendesk.com/attachments/token/caYacWRPWDcVRpVsdQGjjX76K/?name=image.png)  
   
Esse lançamento deve ser criado com o tipo DEBITO, pois quando realizamos um empenho pelo lançamento 000052 o mesmo utiliza o tipo credito, sendo assim fica "creditado" o valor que será necessário para realizar o processo, quando não é utilizado todo o valor podemos utilizar o lançamento de eliminação resíduos do tipo DEBITO para que seja debitado desse empenho o valor que não foi utilizado e assim o valor retorna para a conta que utiliza e define no processo.

Saiba mais:

[Cross Segmentos - Backoffice Linha Protheus - SIGAPCO - PCOA310 Como validar se a rotina de reprocessamento de lançamentos esta sendo executada corretamente...](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025015274-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAPCO-PCOA310-Como-validar-se-a-rotina-de-reprocessamento-de-lan%C3%A7amentos-esta-sendo-executada-corretamente-?source=search)
