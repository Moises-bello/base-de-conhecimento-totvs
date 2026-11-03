---
content_hash: cc76b409c7789d09b309d64bba4fd41bc3bdfc7bbac6b1a5b84c2da18aa8cd3d
fetched_at: '2026-06-29T00:10:22.651947+00:00'
page_id: '498449738'
product: rm
source: tdn-rm
title: 6157067 FISCAL01-9804 DT NFS-e - Belém - Tomador Exterior
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498449738
version: 1
---

**01. DADOS GERAIS**

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Backoffice |
| Módulo: | Fiscal |
| Ticket: | 6157067 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-9804 |

**02. SITUAÇÃO/REQUISITO**

Ao realizar o envio de uma NFS-e para Belém/PA, está apresentando a seguinte mensagem de rejeição:

1206 - Assinatura do RPS incorreta. Código Hash gerado para o campo assinatura do RPS esta invalido. O codigo hash 'c446c05aae0018587a394382c6ceed1e242081df' gerado para o campo Assinatura do RPS nao esta valido. 

**03. SOLUÇÃO**

Foi efetuada de forma específica para município de Belém a tratativa do CNPJ e CEP conforme a  recomendação da prefeitura nas versões de mercado, visto que já existia uma tratativa diferente para municípios DSFNET.

Trecho do layout da prefeitura:

"Caso o tomador for estrangeiro informar no campo CPFCNPJTomador o valor '99999999007790', no

campo CidadeTomador informar o valor '0009999', no campo CidadeTomadorDescricao informar o

nome do país de origem do tomador, no campo CepTomador informar '99999999' e no campo

DocTomadorEstrangeiro informar o documento de identificação do tomador estrangeiro. "
