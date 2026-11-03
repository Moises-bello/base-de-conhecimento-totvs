---
article_id: 1500011379522
category: Escrita Fiscal - Impostos - ICMS
content_hash: 0b923f5b7a5079e206b525eee847a31f81a0da8be8b24497b3643cff8dd8a47c
fetched_at: '2026-06-28T22:39:24.007806+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: ' CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual  calculo o
  parâmetro MV_REDIMPO faz? '
type: support-article
updated_at: '2024-01-23T19:39:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011379522--CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-calculo-o-par%C3%A2metro-MV-REDIMPO-faz
---

**Dúvida**Qual calculo o parâmetro MV\_REDIMPO faz?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

Para calcular o ICMS fictício das importações com redução de base  temos o parâmetro MV\_REDIMPO

como T ou F

As configurações do cadastro de produtos / fornecedor/ TES é a mesma para ambos os cálculos

TES

% red icm = 48,88

L fiscal icms = Isento ou Outras

<https://tdn.totvs.com/pages/releaseview.action?pageId=6076840>

Em relação ao valor das despesas (Siscomex, Frete, Despesas, Seguro e AFRMM - Adicional ao Frete para Renovação da Marinha Mercante) compor ou não a base de cálculo dos impostos, observar a configuração:

|  |  |
| --- | --- |
| **Imposto** | **Campo** |
| ICMS | Desp. Ac. ICMS (F4\_DESPICM) |
| IPI | Desp. Ac. IPI (F4\_DESPIPI) |
| PIS | Desp. Ac. PIS (F4\_DESPPIS) |
| COFINS | Desp. Ac. COF (F4\_DESPCOF) |

Para a memória de cálculo informada, configurar os campos:  
Desp. Ac. IPI (F4\_DESPIPI) = Não  
Desp. Ac. PIS (F4\_DESPPIS) = Não  
Desp. Ac. COF (F4\_DESPCOF) = Não

Exemplo de uma Importação com alíquota de ICMS 18% e redução de base calculo 48,88%

FOB = 5.000,00

II = 300,00

IPI = 10% = 530,00

PIS = 2,10% = 105,00

Cofins = 9,65% = 482,50

Despesas = 214,50 Taxa Siscomex

Total da importação = 6.632,00

Calculo com o parâmetro MV\_REDIMPO = .T.

6.632,00/0,912 = 7.271,93

7.271,93 \*48,88% = 3.554,52

3.554,52 \*18% = 639,81

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018546281)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018265442)

Calculo com o parâmetro MV\_REDIMPO = .F.

6.632,00/0,82% = 8.087,80

8.087,80\*48,88% = 3.953,31

3.953,31\*18% = 711,60

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018560361)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018560421)
