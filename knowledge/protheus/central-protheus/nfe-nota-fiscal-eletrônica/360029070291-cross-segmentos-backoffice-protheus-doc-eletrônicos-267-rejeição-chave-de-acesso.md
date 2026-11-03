---
article_id: 360029070291
category: NFe - Nota Fiscal Eletrônica
content_hash: 134a300ad780d12f3401fb6f4d59f0c22395bcabee9d62eed3da56c5fef2b64e
fetched_at: '2026-06-28T22:40:03.824822+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 267 Rejeição :
  Chave de Acesso referenciada inexistente'
type: support-article
updated_at: '2025-06-23T12:13:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029070291-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-267-Rejei%C3%A7%C3%A3o-Chave-de-Acesso-referenciada-inexistente
---

**Dúvida**

Como solucionar a rejeição abaixo:

267 Rejeição : Chave de Acesso referenciada inexistente

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- A nota original para que traga de forma correta no XML a **chave** deverá estar gravada de forma correta nas tabelas ***SF3, SFT, SF1 ou SF2 nos campos* F3\_CHVNFE, FT\_CHVNFE, F1\_CHVNFE ou F2\_CHVNFE.**

**![CHAVES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12035987238935)**

2- Se a nota for formulário próprio = Sim e tenha sido transmitida pela empresa, na rotina de transmissão de nota ir em ***Outra ações -> Monitor -> faixa ou Monitor -> Consulta NF*** para que seja preenchida a chave nas tabelas corretamente.

![Monitor_-_faixa_-_consulta_NF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4413537271319)

3- Se a nota de origem for de entrada com ***formulário próprio = Não*** verifique se a chave no campo ***F1\_CHVNFE foi digitada*** de forma correta validando a chave no portal da Sefaz no ambiente Nacional ou de Origem.

![F1_CHVNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12035671777431)

4- Além disso, é necessário que as duas notas estejam no mesmo ambiente, ou seja ***duas notas em produção ou as duas em homologação, tpamb = 1 produção e tpamb = 2 homologação.***

***![tpamb.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/12035785277975)***

*Exceção: A NF-e referenciada pode não existir no caso de **Emissão em Contingência** **(tpEmis = 2, 4 ou 5)** (NT 2013/003) Observação: A exceção acima não se aplica para “finNFe=2" (NF-e Complementar).*

* ***Validação da Sefaz:***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9862266782999)***
