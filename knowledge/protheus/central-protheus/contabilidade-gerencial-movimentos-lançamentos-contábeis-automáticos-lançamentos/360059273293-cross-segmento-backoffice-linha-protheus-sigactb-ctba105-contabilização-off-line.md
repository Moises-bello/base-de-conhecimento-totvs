---
article_id: 360059273293
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 65a963e19b3e98e9c8dc5600578de63258b73167de67e51a34d8ed9528775610
fetched_at: '2026-06-28T22:40:32.492830+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA105 - Contabilização
  Off-Line não valida a linha do lançamento
type: support-article
updated_at: '2021-06-14T13:17:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059273293-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA105-Contabiliza%C3%A7%C3%A3o-Off-Line-n%C3%A3o-valida-a-linha-do-lan%C3%A7amento
---

**Ocorrência**Ao contabilizar de forma off-line o sistema não está apresentando validação quando falta alguma informação, exemplo Centro de Custo, Item Contábil ou Classe de Valor obrigatório.  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – A partir da versão 12.1.17  
  
**Causa**Essa ocorrência é apresentada pois o parâmetro destinado a definir se a mensagem será ou não acionada está desabilitado, o nome do parâmetro é MV\_CT105MS.

Lembrando que o sistema aciona a validação do parâmetro MV\_CT105MS apenas quando o MV\_ALTLCTO está com o conteúdo igual a S.  
  
**Solução**Para resolver essa questão deixe os parâmetros MV\_CT105MS e MV\_ALTLCTO igual a S:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360099639733/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097334314/mceclip1.png)

Assim, sempre que lançar contabilizando os lançamentos e apresentados em tela, quando faltar alguma informação, uma mensagem referente ao problema será demonstrado para ajuste do usuário.

Veja mais:

[MP - SIGACTB PARÂMETROS CONTÁBEIS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052504474-MP-SIGACTB-PAR%C3%82METROS-CONT%C3%81BEIS?source=search)

[MP - SIGACTB - CTBA105 Tipo de saldo 9 Pré-Lançamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006689172-MP-SIGACTB-CTBA105-Tipo-de-saldo-9-Pr%C3%A9-Lan%C3%A7amento?source=search)
