---
article_id: 4403541922455
category: Financeiro - Consultas / Relatórios
content_hash: 32b2ccf3ae19058516a3da78dd2e208b6ca1db1bbe96192e34863894c72fdc51
fetched_at: '2026-06-28T22:37:58.379455+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR190 - No relatório
  de baixa o sistema não considera na coluna valor original o valor do título, e sim
  o valor baixado em moeda2
type: support-article
updated_at: '2025-04-07T20:28:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403541922455-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR190-No-relat%C3%B3rio-de-baixa-o-sistema-n%C3%A3o-considera-na-coluna-valor-original-o-valor-do-t%C3%ADtulo-e-sim-o-valor-baixado-em-moeda2
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:05:00 min  
  
Ocorrência**No relatório de baixa o sistema não considera na coluna valor original o valor do título, e sim o valor baixado em moeda2?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**É porque mudou o valor da taxa no momento da baixa.  
  
**Solução**Neste relatório informo que é uma questão de conceito e não uma correção ou erro, porque:  
  
Ao efetuar uma  inclusão do titulo moeda 2 no valor de  21.216,00 reais a uma taxa 7,2790  
![imagem1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403606736791/imagem1.png)

Realmente se efetuar a conta 21.216,00 x 7,2790 = 154.431,26 o valor do título

Porém, no momento da baixa veja

É alterado o valor da taxa para  5,6838   
![imagem2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403606753175/imagem2.png)  
Se você efetuar a conta valor do título 21.216,00 x 7,2790 = 154.431,26 assim seria o certo.  
  
Mas no momento da baixa você  troca a taxa para 5,6838 então 21.216,00 x 5,6838 = 120.587,50.

Veja o trecho da documentação:  
  
![imagem3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403606760215/imagem3.png)

**Saiba mais:**[Relatório de Relação de Baixas (FINR190) - Conceito da Coluna Valor Original](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=543064077)  
  
Resumindo:  
Trata um conceito do Relatório que visa identificar sempre o movimento através do valor da baixa. E nesse caso leva em consideração a taxa que esta sendo executada na baixa do titulo. Como diz a documentação acima.

Então esta correto o valor original do relatório sair 120.587,50 , conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4403541860375/mceclip0.png)
