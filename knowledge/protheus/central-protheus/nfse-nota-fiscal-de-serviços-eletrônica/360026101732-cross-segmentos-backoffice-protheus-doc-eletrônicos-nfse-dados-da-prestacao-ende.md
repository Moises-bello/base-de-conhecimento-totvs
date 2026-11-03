---
article_id: 360026101732
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: fb95f52b9d117bcfdf57119a37d95450a279ed188f9ebd6a04976df33f503735
fetched_at: '2026-06-28T22:39:56.424895+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - Dados da
  Prestacao: Endereço, Número, Complemento, Bairro, CEP e PAIS'
type: support-article
updated_at: '2026-06-08T19:25:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026101732-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-Dados-da-Prestacao-Endere%C3%A7o-N%C3%BAmero-Complemento-Bairro-CEP-e-PAIS
---

**Dúvida**  
Procedimento para informar Endereço, Número, Complemento, Bairro e CEP da Prestação.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Solução**  
Para informar os dados do local da prestação no padrão, temos apenas os campos C5\_ESTPRES (UF), C5\_MUNPRES (Cod.Municipio) E C5\_DESCMUN (Nome Municipio), porém algumas prefeituras exigem dados adicionais sobre o local da prestação, como endereço, número, complemento, bairro, cep e/ou país.  
  
Crie campos na tabela SC5 que compreendem o local da prestação dos serviços:  
‘Endereço, número, complemento, bairro, cep, pais’.

Exemplo:  
C5\_ENDPRES, C5\_NUMPRES, C5\_COMPPRE, C5\_BAIPRES, C5\_CEPPRES, C5\_PAIS

**Importante:** O Tamanho dos campos devem ser de acordo com o layout de cada prefeitura, portanto é imprescindível checar essas informações no manual/Layout de integração webservice do município.  
Os campos usados aqui nessa FAQ são apenas exemplos, pois cada município possui sua regra.  
  
Informe o nome dos campos no parâmetro **MV\_ENDPRES** conforme exemplo:  
  
{'C5\_ENDPRES','C5\_NUMPRES','C5\_COMPPRE','C5\_BAIPRES','C5\_CEPPRES','C5\_PAIS'}

**OBS:** Os campos C5\_ESTPRES, C5\_MUNPRES E C5\_DESCMUN já estão no padrão e não devem ser informados no parâmetro.

As Tags contendo essas informações sobre o local da prestação serão geradas apenas para municípios com essa tratativa no layout.

**Observação:**  
Caso não tenha necessidade de todos os campos, basta criar somente o necessário e informar no parâmetro conforme exemplo:  
{'','','','','','C5\_PAIS'}
