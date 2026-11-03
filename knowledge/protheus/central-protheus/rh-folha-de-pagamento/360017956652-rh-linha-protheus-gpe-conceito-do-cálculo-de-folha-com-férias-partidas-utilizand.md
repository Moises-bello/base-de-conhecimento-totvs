---
article_id: 360017956652
category: RH - Folha de Pagamento
content_hash: 3ee079beb5375fa398ae4b991fadc9245b7f8b4f5bdfcf27f09c5c1e51cbc4ae
fetched_at: '2026-06-28T22:44:17.129049+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Conceito do cálculo de folha com Férias partidas
  utilizando o parâmetro MV_DINSSFM= S
type: support-article
updated_at: '2025-08-22T18:39:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017956652-RH-Linha-Protheus-GPE-Conceito-do-c%C3%A1lculo-de-folha-com-F%C3%A9rias-partidas-utilizando-o-par%C3%A2metro-MV-DINSSFM-S
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26357895949207)*** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Qual o conceito do **cálculo de folha com Férias partidas** utilizando o parâmetro **MV\_DINSSFM= S** e como funciona o cálculo?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12  
  
**Solução**O valor do INSS férias referente ao mês seguinte é levado no calculo das férias através do ID **0232 (INSS Férias Pago Mês Seguinte)**.

Nesta configuração, a base de INSS é dividida entre mês de cálculo e mês seguinte, sendo **efetuado o cálculo do % de INSS sobre cada base, assim o valor do INSS mês seguinte é fixado no calculo de Férias e não sofre recálculo.**

Por estar fixo no cálculo, entra na Base de INSS Até Limite (ID 0013) e Acima do Limite (Id 0014), as verbas de férias do Mês.  
  
![image2018-4-16_14-14-24.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-14-24.png?version=1&modificationDate=1523900434000&api=v2)  
![image2018-4-16_14-16-58.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-16-58.png?version=1&modificationDate=1523900434000&api=v2)  
![image2018-4-16_14-17-41.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-17-41.png?version=1&modificationDate=1523900434000&api=v2)  
  
Após integrado com a folha de pagamento, todas as verbas são carregadas para o cálculo, porém, somente as **verbas de férias do mês**entrarão na composição de Base de INSS e recolhimento da GPS da competência.  
  
![image2018-4-16_14-22-50.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-22-50.png?version=1&modificationDate=1523900434000&api=v2)

**Após o fechamento do período** as verbas de férias mês seguinte ficam na RGB como verbas de férias do mês com Origem F.  
  
![image2018-4-16_14-25-49.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-25-49.png?version=1&modificationDate=1523900434000&api=v2)  
  
No exemplo, ao calcular o período 02/2018 essas verbas entram para a folha e composição da Base de INSS do mês e recolhimento do INSS já descontado do funcionário no primeiro mês.  
  
![image2018-4-16_14-28-45.png](http://tdn.totvs.com/download/attachments/353283187/image2018-4-16_14-28-45.png?version=1&modificationDate=1523900434000&api=v2)

No segundo cálculo pode ser observado que o valor de INSS Férias Mês Seguinte descontado na folha anterior (01/2018) é abatido do valor da verba com ID 0164 ( Férias Pafo Mês Anterior), para não haver desconto duplicado, o objetivo de trazer na folha seguinte é o recolhimento do mesmo por se tratar de competência.  
  
Exemplo: 543,02 + 181,01 = 724,03 - 57,92 ( INSS) = 666,11 (Verba com ID 0164)

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
