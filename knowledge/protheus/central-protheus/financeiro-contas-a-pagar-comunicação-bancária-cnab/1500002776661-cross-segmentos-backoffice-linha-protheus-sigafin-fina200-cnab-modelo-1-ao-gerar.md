---
article_id: 1500002776661
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 1b13eab95edd998a645f016d8aff9a360871fd3b276da2c84c95771cba252d17
fetched_at: '2026-06-28T22:37:55.411543+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 - Cnab Modelo
  1, ao gerar retorno com NCC já baixada por compensação, sistema não realiza baixa
  do título
type: support-article
updated_at: '2022-06-21T00:01:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002776661-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-Cnab-Modelo-1-ao-gerar-retorno-com-NCC-j%C3%A1-baixada-por-compensa%C3%A7%C3%A3o-sistema-n%C3%A3o-realiza-baixa-do-t%C3%ADtulo
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Como realizar retorno de cobrança quando houver um título de NCC compensado?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**Segue um cenário de **retorno de cobrança**, com **NCC** já compensada, como o sistema valida:  
  
-Título com valor de R$1.000,00.  
-NCC compensada de R$200,00.  
-Instrução de desconto de R$200,00 ao banco.  
  
No **retorno do CNAB** enviado pelo banco, fica da seguinte forma:  
-Valor para baixar R$800,00  
-Desconto R$200,00  
  
Nesse momento quando o sistema valida o saldo do título para baixa fica da seguinte forma:  
-Valor da baixa R$800,00  
-Valor de desconto R$200  
-Total do saldo no título necessário para baixa R$1.000,00.  
  
Neste momento é onde acontece o problema, pois o saldo do titulo já está R$800,00 e não mais R$1.000,00, pois para baixa o desconto também é usado como saldo do título. A **NCC** já baixou R$200,00 de saldo, ficando somente R$800,00 no saldo total do título para baixa.  
  
OBS: Se não tiver os R$200,00 como desconto o título baixa normalmente.  
  
Sugerimos 2 maneiras para correção.  
  
1) Realize ajuste no retorno com o ponto de entrada **F200VAR** e valide os valores quando houver **NCC** já com baixa no título.  
[F200VAR - CNAB Receber - Manipular variáveis no processamento do retorno](https://tdn.totvs.com/pages/viewpage.action?pageId=235308494)  
  
2) Realize o contato com o banco e verifique a possibilidade dessa instrução enviada, seja tratada no retorno sem ser como Desconto.
