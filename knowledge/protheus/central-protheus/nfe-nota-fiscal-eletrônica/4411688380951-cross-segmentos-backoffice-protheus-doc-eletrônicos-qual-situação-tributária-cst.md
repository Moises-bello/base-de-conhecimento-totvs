---
article_id: 4411688380951
category: NFe - Nota Fiscal Eletrônica
content_hash: 6bfc2e92ac7c52e7978be36264841be9899f0bbe35a04a054ec1b96b3d851a1e
fetched_at: '2026-06-28T22:40:07.105074+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Qual situação tributária
  (CST) de  PIS e COFINS que destaca o valor do imposto no XML e DANFE
type: support-article
updated_at: '2025-06-23T11:57:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411688380951-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Qual-situa%C3%A7%C3%A3o-tribut%C3%A1ria-CST-de-PIS-e-COFINS-que-destaca-o-valor-do-imposto-no-XML-e-DANFE
---

**Dúvida**Qual situação tributária (CST) de PIS e COFINS que destaca o valor do imposto no XML e DANFE ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* Exemplo de **NÃO** destaque de **PIS e COFINS no XML**

![pis_e_cofins.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4411687681943)

Conforme está no Manual de Orientação do contribuinte da SEFAZ, **versão 6.00, páginas 213.**

Estes CSTs ***não destacam*** a situação tributária ***04, 05, 06, 07, 08 e 09;***

1. Preencher o CST do PIS e do Cofins, campo do PIS ***Sit. Trib. Pis** **F4\_CSTPIS*** o campo do ***Cofins Sit. Trib. Cof.**  **F4\_CSTCOF diferente dos acima.***

![Sit._trib_PIS_e_COF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12291982849431)

2. Após isso, **retransmita NF-e.**

* **Saiba mais:**

**O CST 05 é apenas para o PIS e Cofins-ST caso seja necessário** utilizar temos a documentação do link abaixo:

*[Clique Aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408510846871-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-PIS-COFINS-ST-no-total-da-NF-)*

* No DANFE até o momento não há leiaute previsto pela Sefaz para gerar o **PIS e COFINS em destaque, conforme o parecer da Consultoria de Segmentos no link abaixo:**

**[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=738239052)**

Para gerar o valores em ***informações complementares*** é conforme a orientação dos links abaixo:  
  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-informa%C3%A7%C3%B5es-na-TAG-infCpl-ou-infAdFisco-no-XML-e-no-DANFE?source=search)  
  
[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-mensagem-em-informa%C3%A7%C3%B5es-complementares-TAG-infcpl-e-infadfisco-do-Danfe-utilizando-f%C3%B3rmula-?source=search)
