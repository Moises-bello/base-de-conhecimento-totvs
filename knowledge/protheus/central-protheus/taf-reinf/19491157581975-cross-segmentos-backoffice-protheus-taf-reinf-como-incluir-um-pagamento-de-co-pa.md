---
article_id: 19491157581975
category: TAF - REINF
content_hash: 2aae011e0db4a1151ff26cd4c2ffa0594d14549778b40fdf97f491e9fb5c4569
fetched_at: '2026-06-28T22:41:33.720725+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Como incluir um pagamento
  de Co-participação ou Reembolso de Plano de Saúde?
type: support-article
updated_at: '2023-12-01T19:38:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19491157581975-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Como-incluir-um-pagamento-de-Co-participa%C3%A7%C3%A3o-ou-Reembolso-de-Plano-de-Sa%C3%BAde
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19491118723735) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Como incluir um pagamento de Co-participação ou reembolso de plano de saúde para a Reinf?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - TOTVS Automação Fiscal - Todas as versões  
  
**Solução**

**Atenção**:  As informações de planos de saúde e o valor da coparticipação só deverão ser escrituradas na Reinf quando o pagamento **for realizado pelo próprio beneficiário ou terceiro**, que não tiver vínculo empregatício. Pagamentos a funcionários devem ser transmitidos no **e-social**. Segue mais informações: <https://tdn.totvs.com.br/pages/releaseview.action?pageId=790638507>

1 - Acessar o menu Atualizações > Cadastros > Fiscais > Participantes. Incluir o beneficiário e caso haja dependentes, incluir os dados do dependente na aba correspondente.

![PLS 2.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491140895639)

2- Acessar o menu Atualizações > Movimentos Reinf > Cadastro Plano de Saúde. Incluir os dados do Plano de saúde.

![pls1.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491111033495)

3 - Acessar o menu Atualizações > Movimentos Reinf > Pagamento/Reembolso Plano de Saúde. Incluir os dados do beneficiário. Caso o pagamento seja referente ao dependente, deve ser efetuado um cadastro separado:

Titular:

![pls tit.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491157561111)

Dependente:

![pls 3 dep.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491126146071)

4 - Incluir o pagamento na rotina TAFA535. Atualizações > movimentos Reinf > Pagamentos.

Deve ser vinculado os dados do Participante. Incluir a natureza de rendimento e um tributo, se possuir.

![pls pagto.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/19491174063127)

Para mais informações: <https://tdn.totvs.com.br/display/public/TAF/EFD-Reinf>
