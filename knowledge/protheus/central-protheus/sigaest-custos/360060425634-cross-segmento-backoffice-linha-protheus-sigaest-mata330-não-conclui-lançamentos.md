---
article_id: 360060425634
category: SIGAEST - CUSTOS
content_hash: 91a716c2adc550c3d49363dd94489728bb592ae72f90e88c9e1ba1409910a08a
fetched_at: '2026-06-28T22:39:02.190509+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Não conclui
  lançamentos contábeis
type: support-article
updated_at: '2025-12-22T16:42:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060425634-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-N%C3%A3o-conclui-lan%C3%A7amentos-cont%C3%A1beis
---

Ao recalcular o custo médio no TOTVS Protheus, o sistema não valida a falta de informações obrigatórias, como Centro de Custo, Item Contábil ou Classe de Valor, devido ao parâmetro MV\_PRELAN = N estar desabilitado. Para corrigir, deve-se configurar os parâmetros MV\_CT105MS e MV\_ALTLCTO como "S", garantindo mensagens de alerta para ajustes necessários durante os lançamentos contábeis.

Ao efetuar o recalculo de custo médio o sistema não está apresentando validação quando falta alguma informação ao clicar em "Confirmar" na tela de lançamentos contábeis, exemplo Centro de Custo, Item Contábil ou Classe de Valor obrigatório.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**  
Ao clicar em "Confirmar" para continuar a execução do recalculo, na tela de lançamentos contábeis, o sistema não da continuidade a execução.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001790721)

Essa ocorrência é apresentada pois o parâmetro destinado a definir se a mensagem será ou não acionada está desabilitado, por conta da configuração do parâmetro MV\_PRELAN = N

<https://tdn.totvs.com/pages/releaseview.action?pageId=284348618>  
  
**Solução**  
Para resolver essa questão deixe os parâmetros MV\_CT105MS e MV\_ALTLCTO igual a S:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37193733227415)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37193733227799)

Assim sempre que lançar contabilizando os lançamentos e apresentados em tela, quando faltar alguma informação, uma mensagem referente ao problema será demonstrado para ajuste do usuário.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000049222-SIGAEST-CUSTOS)

[MP - SIGACTB PARÂMETROS CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504474-MP-SIGACTB-PAR%C3%82METROS-CONT%C3%81BEIS?source=search)

[MP - SIGACTB - CTBA105 Tipo de saldo 9 Pré-Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689172-MP-SIGACTB-CTBA105-Tipo-de-saldo-9-Pr%C3%A9-Lan%C3%A7amento?source=search)
