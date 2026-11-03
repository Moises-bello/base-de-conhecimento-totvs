---
content_hash: a3f585e6e3e193f6b85af8203c1c739abdeef1f0640e6740b9fb51f067c28d2a
fetched_at: '2026-06-29T00:11:20.657063+00:00'
page_id: '687165357'
product: rm
source: tdn-rm
title: NF-e Estadual
type: documentation
url: https://tdn.totvs.com/display/LRM/NF-e+Estadual
version: 9
---

**Chave de Acesso:**campo responsável por armazenar a **sequência****numérica** única que identifica os documentos eletrônicos, que está contido no arquivo XML e na versão impressa destes documentos, como é o caso da DANFE e do DACTE.

**Protocolo de Autorização:** campo responsável por armazenar o número de **protocolo de autorização de uso** gerado pela SEFAZ autorizando a emissão do documento e garantindo autenticidade e veracidade do mesmo.

Critério de Visibilidade campos Chave de Acesso e Protocolo de Autorização

* Movimentos de saída de Exportação de Remessa Simbólico
* Movimentos de entrada que não emitem Documentos Fiscais, mas possui o tributo ISS no item ou no movimento
* Movimentos de entrada de Documentos Fiscais
  + NFe
  + NFCe
  + CTe
  + CTe OS
  + NF3e

**Informações Adicionais ao Fisco:** Campo responsável por armazenar as informações Adicionais de Interesse do Fisco. Preenche a tag infAdFisco no xml do documento eletrônico.

**Informações Complementares do Contribuinte:** Campo responsável por armazenar as informações Complementares de interesse do Contribuinte. Preenche a tag infCpl no xml do documento eletrônico.

Critério de Visibilidade campos Informações Adicionais ao Fisco e Informações Complementares do Contribuinte

* Movimentos que emitem:  
  + NF-e
  + NFC-e
  + MDF-e
