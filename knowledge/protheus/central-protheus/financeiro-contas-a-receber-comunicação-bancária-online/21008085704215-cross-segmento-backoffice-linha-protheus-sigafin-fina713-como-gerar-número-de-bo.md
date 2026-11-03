---
article_id: 21008085704215
category: Financeiro - Contas a Receber - Comunicação Bancária Online
content_hash: 7dc78e1bc6394d15f0f2b158f722d608d52debf724162abde4437a5d9659bb5f
fetched_at: '2026-06-28T22:37:49.152113+00:00'
product: protheus
section_id: 26656227629847
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como gerar
  número de boleto com Num. do título + Parcela
type: support-article
updated_at: '2026-01-07T19:09:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21008085704215-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-gerar-n%C3%BAmero-de-boleto-com-Num-do-t%C3%ADtulo-Parcela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21008085665175) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como definir geração de boleto com o número do título + parcela?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
1. Na rotina FINA710, opção configuração de contas, novo layout ou editar layout.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21008085666455)  
2. Na configuração do campo "Número do Documento", digite a expressão:

ALLTRIM(SE1->E1\_NUM)+ALLTRIM(SE1->E1\_PARCELA)   
  
Dessa maneira, ele vai concatenar o Num do título e a parcela, ignorando os espaços devido à função ALLTRIM.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21008085670423)

3. esse será o resultado do boleto. (Em amarelo o número do título e em azul a parcela)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21008098748439)
