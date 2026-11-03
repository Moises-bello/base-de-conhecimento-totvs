---
article_id: 21138557938583
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: 10d6e748daddf51c5df3a31306bf58805fdf767f149f5fd4ebbfd8043ea02dd8
fetched_at: '2026-06-28T22:37:55.250526+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - Financeiro - FINA713 - Comportamento
  do ponto de entrada F330DESC na impressão do Boleto
type: support-article
updated_at: '2024-02-06T11:54:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21138557938583-Cross-Segmentos-Backoffice-Linha-Protheus-Financeiro-FINA713-Comportamento-do-ponto-de-entrada-F330DESC-na-impress%C3%A3o-do-Boleto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21138563412119) Tempo aproximado para leitura: **00:08:00 min** **Dúvida**Qual o comportamento do ponto de entrada F330DESC na impressão do Boleto no Novo Gestor Financeiro no Boleto Online (FINA713)?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**

Na utilização do **PE F330DESC**o valor de desconto não é exibido, o ponto de entrada visa considerar o desconto na **Compensação (FINA330)**, diminuindo o valor cobrado + o valor de compensação da nota ou **RA** vinculado.

**Importante**  
No Boleto, será demonstrado o líquido visto que o desconto já foi aplicado na Compensação que será a conta da seguinte maneira 

**Exemplo:**  
Nota Principal: 8.000,00  
Desconto: 7,00 % = 560,00  
Valor compensação: 1000   
Desconto aplicado na compensação: 560,00  
   
8.000 - 560 - 1000 = 6440

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21138563413655)  
 **Saiba Mais**[F330DESC - Desconto na compensação contas a receber](https://tdn.totvs.com/pages/releaseview.action?pageId=639933364)  
[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
