---
article_id: 41321464342551
category: Escrita Fiscal - Configurador de Tributos
content_hash: 29f1ba27abe3e025cece12ec9aafddde14e7486351e2da8a5586441dbdc7980e
fetched_at: '2026-06-28T22:39:17.262427+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  Remessa e Retorno de Beneficiamento no Fisa170?
type: support-article
updated_at: '2026-06-18T14:55:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41321464342551-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-Remessa-e-Retorno-de-Beneficiamento-no-Fisa170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480728599) Tempo aproximado para leitura: 10:00**min**  
  
**Dúvida**  
FIS - Como configurar Remessa e Retorno de Beneficiamento no Fisa170?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões

**Solução**

Nesse documento vamos demonstrar a configuração do CFOP 5920/1921 como exemplo de beneficiamento, sendo aplicado para qualquer CFOP que tenha controle de poder de terceiros.

Exemplo:

Nota fiscal de saídas = Remessa do Vasilhame - CFOP 5920

Nota fiscal de entradas = Retorno do Vasilhame - CFOP 1921

1a) Nota fiscal de Remessa de Vasilhame  
TES  
CFOP = 5920  
Controle poder de terceiros = Remessa

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464302487)

Campos que permanecem no TES

<https://tdn.totvs.com/pages/releaseview.action?pageId=928965724>

   
ID tributos  
ICMS  
IBSEST  
CBSFED  
 

ICMS   
Regra de base de calculo - zerada  
O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464304279)  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464305431)

Regra de Alíquota   
O:zero

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480733975)

Regra de escrituração  
Incidência = isento  
CST = 40

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464306583)  
 ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480736151)

Regra de Calculo Documentos Fiscais

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464309527)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480739607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480740119)

Aba detalhamento da formula de calculo / Isento

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464311959)

IBS/CBS  
   
Regra de base de dados  
O:zero  
   
Regra de alíquota  
O:zero  
   
Regra de escrituração  
Incidência = isento  
cClasstrib = 410029

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480742551)

Regra de Calculo Documentos Fiscais IBSEST

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464314263)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464315031)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464315927)

Regra de Cálculos Documentos Fiscais CBSFED

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464316567)

Regra de escrituração a mesma no IBSEST

Perfis os mesmos

Pedido de Vendas

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480749591)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464317975)

cBenef = CST40

Código SP010820 - cadastrado na rotina Fisa156

SP010820 - Isenção - VASILHAME/RECIPIENTE/EMBALAGEM

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464318871)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464319767)

<cBenef>**SP010820**</cBenef>

<CFOP>**5920**</CFOP>

CJ3 - nota fiscal original

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464322967)

2a) Nota fiscal de Retorno de Vasilhame   
TES  
CFOP = 1921  
Controle poder de terceiros = Devolução

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480758679)  
   
Botão retornar  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480759831)  
   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321480760471)  
CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41321464327703)

Para notas fiscais originais sem o IBS/CBS, faça o reprocessamento de dados na rotina Mata930

Verifique estar atualizado com a issue Dserfise-17465

12.1.2310:<https://r.totvs.io/p/1254446> ; 12.1.2410:<https://r.totvs.io/p/1254447> ; 12.1.2510:<https://r.totvs.io/p/1254445> ;
