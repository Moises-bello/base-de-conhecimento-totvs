---
article_id: 40798225614743
category: Financeiro - Baixas a Pagar
content_hash: 67ac9eb82b5bc1270d865a46ef26ed037b16bd368e41330be86816f318bb0698
fetched_at: '2026-06-28T22:37:24.905120+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Inclusão
  de juros para baixas e compensação no contas a pagar
type: support-article
updated_at: '2026-05-29T12:25:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40798225614743-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-Inclus%C3%A3o-de-juros-para-baixas-e-compensa%C3%A7%C3%A3o-no-contas-a-pagar
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40798225587479)** Tempo aproximado para leitura: **00:06:00 min**  
  
**Dúvida**  
Foi lançado um PA para o título, incluindo o valor original mais os juros pagos. Porém, o título atual mostra só o valor integral, sem os juros. Qual o procedimento recomendado para a baixa manual no Contas a Pagar, considerando os juros.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Todas as releases  
  
**Solução**

Nos casos em que o título principal for incluído sem os juros, será necessário realizar o ajuste manual, informando o valor dos juros diretamente no campo “Acréscimo”, para que esta informação seja considerada durante o processo de baixa manual ou baixa por compensação do título.

Ao efetivar a operação de baixa manual, o sistema apresentará o valor informado em “Acréscimo” e, no momento da gravação na tabela SE5, gerará automaticamente uma linha do tipo “JR” com o valor inserido, realizando a liquidação pelo valor total do título (valor original acrescido dos juros).  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40798225588119)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40798225588759)

Para o processo de baixa por compensação, o valor será gerado com o total no campo E5\_VALOR (valor do título somado aos juros informados no campo “Acréscimo”), sem a geração de uma nova linha para o movimento de juros. Entretanto, o sistema registrará o valor correspondente aos juros no campo E5\_VLJUROS.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40798238721687)
