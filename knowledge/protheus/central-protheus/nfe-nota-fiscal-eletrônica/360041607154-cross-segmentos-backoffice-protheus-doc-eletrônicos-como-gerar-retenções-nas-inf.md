---
article_id: 360041607154
category: NFe - Nota Fiscal Eletrônica
content_hash: a5c144829491daa8bb3b76ab8794056685e03154eea61b437ac162d73fcb2b6c
fetched_at: '2026-06-28T22:40:06.762535+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar retenções
  nas Informações Complementares do DANFE ?
type: support-article
updated_at: '2025-09-22T18:03:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041607154-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-reten%C3%A7%C3%B5es-nas-Informa%C3%A7%C3%B5es-Complementares-do-DANFE
---

**Dúvida**

Como gerar retenções nas Informações Complementares do DANFE ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Para que ocorra o destaque das retenções nas Informações Complementares do DANFE.

Verifique o conteúdo do parâmetro MV\_IMPRET, o mesmo deve estar igual a .T.

**Nome: MV\_IMPRET**

Tipo: Lógico

Descrição: Este parâmetro define se os valores dos impostos retidos (PIS - COFINS - CSLL - INSS - IR) devem ser destacados no quadro de informações complementares da nota fiscal.

Para que os valores sejam destacados, as retenções devem estar registradas nas tabelas SF2 e SE1.

Após a configuração deste parâmetro, apenas as notas fiscais geradas posteriormente terão os valores dos impostos retidos destacados.

TABELAS:

![](https://tdn.totvs.com.br/download/attachments/236599659/RETENCAO1.jpg?version=2&modificationDate=1463157294000&api=v2)

XML:

![](https://tdn.totvs.com.br/download/attachments/236599659/RETENCAO2.jpg?version=2&modificationDate=1463157295000&api=v2)

**ou**

Utilizar os ***campos padrões do Protheus*** para gerar a mensagem através dos links abaixo:

1. [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)
2. [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

* **Saiba mais:**

*Temos um parecer da **Consultoria de Segmentos da TOTVS:***

*[Clique Aqui](https://tdn.totvs.com/display/ConSeg/NF-e+-+Destaque+IRRF+-+Obrigatoriedade)*
