---
article_id: 360025888212
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: d7a9d1f8ebc80fb104e9e3b20a231ee2819ed952f9ca4d3a80a4f6537807985c
fetched_at: '2026-06-28T22:39:58.617487+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Valor Aproximado
  dos Tributos no XML
type: support-article
updated_at: '2025-05-23T18:43:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025888212-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Valor-Aproximado-dos-Tributos-no-XML
---

**Dúvida**Destaque no XML da NFSe o Valor Aproximado dos Tributos (Lei da transparência)  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - Todas as versões  
  
**Solução**

O valor aproximado dos tributos será destacado no XML da RPS, dentro da tag Discriminação, quando:

- Houver valores nos campos F2\_TOTIMP, F2\_TIPIMP, D2\_TOTIMP, F2\_TOTMUN, F2\_TOTFED, F2\_TOTEST, D2\_TOTMUN, D2\_TOTFED e D2\_TOTEST.  
  
- Parâmetro habilitado MV\_CRGTRIB = .T.  
  
- Parâmetro MV\_MSGTRIB conteúdo 1, 2 ou 3.  
**MV\_MSGTRIB=1** - O Rdmake destaca a mensagem dentro de **Informações complementares**, essa informação irá para o XML da prefeitura somente se o layout possuir essa tag;  
   **MV\_MSGTRIB=2 e 3** - O Rdmake destaca a mensagem dentro da tag **<discr>**, essa informação será apresentado dentro da discriminação dos serviços no xml convertido no layout da prefeitura.  
O xml gerado pelo rdmake pode ser extraído do campo **XML\_TSS** e o XML convertido para o layout da prefeitura fica no campo **XML\_ERP**, ambos na tabela **SPED051**.  
  
- Rdmakes, rotina FISA022 e TSS atualizados conforme disponível no portal do cliente.  
  
**Observação:**O preenchimento dos campos citados nas tabelas SF2 e SD2 são de responsabilidade Fiscal. O conteúdo dos campos citados são utilizados para a montagem do XML, caso eles estejam devidamente preenchidos.
