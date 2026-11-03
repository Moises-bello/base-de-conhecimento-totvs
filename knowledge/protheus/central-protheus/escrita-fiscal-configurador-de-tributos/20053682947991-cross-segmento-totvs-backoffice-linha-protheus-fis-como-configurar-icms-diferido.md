---
article_id: 20053682947991
category: Escrita Fiscal - Configurador de Tributos
content_hash: 299aa54534ad31969c644412e8bc1b28b6f850e08e306ab642ae60a9c65e9334
fetched_at: '2026-06-28T22:39:17.202008+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como configurar
  ICMS DIFERIDO PARCIAL CST 53 no FISA170?
type: support-article
updated_at: '2025-09-30T22:34:51Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20053682947991-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-ICMS-DIFERIDO-PARCIAL-CST-53-no-FISA170
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20053682938391) Tempo aproximado para leitura: 05:00**min** **Dúvida**Como configurar ICMS DIFERIDO PARCIAL CST 53 no FISA170?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Todas as versões  
  
**Solução**

MV\_ESTADO = SP  
   
Fornecedor = SP  
   
Cadastro de Produto  
Biodiesel Monofásico  
   
Dados da nota fiscal  
Quantidade = 41313,000  
Valor unitário = 5.02099  
Valor total = 207.432,15  
   
Valor do ICMS CST53 com diferimento de 33,33%  
41.313, x 0,9456 = 26.045,02  
   
Configurações no Fisa170  
   
ID tributo = ICMS  
CST = 53  
   
   
Perfil do produto  
![](https://totvssuporte.zendesk.com/attachments/token/JYUGWWWiT1mA7ahctl2A4OxP8/?name=image.png)  
   
Perfil de operação = vamos usar o 000013  
![](https://totvssuporte.zendesk.com/attachments/token/9726CFN0NIYYHIEKBvOxoC8UN/?name=image.png)  
 Perfil Participante  
   
![](https://totvssuporte.zendesk.com/attachments/token/wZE2a20QZSONz19xaVTPAvNlr/?name=image.png)  
   
Perfil Origem / destino = vamos usar operações internas = 000001  
   
![](https://totvssuporte.zendesk.com/attachments/token/rKi7LFgPRnAHXocPqcPH3wKPZ/?name=image.png)  
   
Regra de Base de calculo  
   
![](https://totvssuporte.zendesk.com/attachments/token/qzSVtQpX1SjhXqCBqWICHKyFr/?name=image.png)  
Base de calculo definida pela quantidade  
   
Regra de Alíquota  
   
![](https://totvssuporte.zendesk.com/attachments/token/ElDlKBi5i7AeM2Yv9YB3F8Xdm/?name=image.png)

Regra de escrituração - CST 53 com diferimento parcial  
![](https://totvssuporte.zendesk.com/attachments/token/Bv25moLf8pLwJrameVLo9meU7/?name=image.png)  
   
Regra de calculo = Documentos fiscais  
   
![](https://totvssuporte.zendesk.com/attachments/token/NMbTMIdWjIoZ6dj2QPZtf4eGp/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/SWBS2W3YUnnJT7BUjhnQQCC7X/?name=image.png)  
![](https://totvssuporte.zendesk.com/attachments/token/VsGFZuC0moLDrWfwT9bwXsCxv/?name=image.png)  
   
![](https://totvssuporte.zendesk.com/attachments/token/xJBysrIfInqTUMjrqZNL37NhN/?name=image.png)  
Formula  
![](https://totvssuporte.zendesk.com/attachments/token/d1VPyXt43ieplL33jro4h4i8b/?name=image.png)  
   
Lançamento da nota fiscal de entradas - mata103  
   
![](https://totvssuporte.zendesk.com/attachments/token/FFQpGF1OfB6dLShnrOiWWni1X/?name=image.png)  
 

Boletim

https://tdn.totvs.com/pages/releaseview.action?pageId=765332384
