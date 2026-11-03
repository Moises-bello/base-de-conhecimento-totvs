---
article_id: 360034609874
category: NFe - Nota Fiscal Eletrônica
content_hash: e58938f1fdcbe5238fb6951e1d1a85ebf640f094f3878edb5f81dcbb50931a94
fetched_at: '2026-06-28T22:40:01.510736+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 626 Rejeição :
  CFOP de operação isenta para ZFM diferente do previsto.'
type: support-article
updated_at: '2021-08-02T19:34:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034609874--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-626-Rejei%C3%A7%C3%A3o-CFOP-de-opera%C3%A7%C3%A3o-isenta-para-ZFM-diferente-do-previsto
---

**Dúvida**  
Como corrigir a 626 Rejeição : CFOP de operação isenta para ZFM diferente do previsto ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Verifique se realmente foi utilizada o motivo de desoneração na TES correto.

Na**TES** na Aba **Outros**o campo F4\_MOTICM  **Mot. Desone.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051383834/mceclip0.png)**

2- Caso esteja errado altere o conteúdo do campo F4\_MOTICM  **Mot. Desone.**, caso esteja correto a Sefaz só permite nota de suframa com a lista de **CFOPS abaixo:**

1203, 1204, 1208, 1209, 2203, 2204, 2208, 2209, 5109, 5110, 5120, 5151, 5152, 5651, 5652, 5654, 5655, 5658, 5659, 5910, **6905**, 6109, 6110, 6120, 6122, 6123, 6151, 6152, 6651, 6652, 6654, 6655, 6658, 6659, 6910, **6923** (NT2012.003) (NT2013.005 v1.10)

* **Importante:**

**Fiscalmente qual CFOP** utilizar a TOTVS **não orienta.** Caso haja dúvidas fiscais, **será necessário a empresa** como contribuinte **consultar a Sefaz.** Lembrando que essas consultas **só são feitas pelo contribuinte ou seja pela empresa.**

3- Se realmente for nota de suframa na**TES** na Aba **Impostos** preenchao campo F4\_CF  **Cod. Fiscal**com um dos CFOPS mencionados acima

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360052264173/mceclip1.png)

 4- Após isso, exclua a nota e gere novamente

* **Validação da Sefaz:**

De acordo com [Nota Técnica 2019.001 - v.1.51 - Publicada em 25/09/2020](https://www.nfe.fazenda.gov.br/portal/exibirArquivo.aspx?conteudo=JmSfVODg2Rc=)

Inclusão de novos **CFOPs na regra de validação N28-20.** Como **EXCEÇÃO,** a alteração nessa regra entrará em homologação e produção no dia **28/9/2020.**

**CFOP 6905 e 6923**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360092784514/mceclip0.png)​

* **Saiba mais:**

**Até o momento não há nenhuma exceção prevista**  que possa ser utilizado CFOPs diferentes do previsto acima.
