---
article_id: 360041806973
category: NFSE - Nota Fiscal de Serviços Eletrônica
content_hash: b4af45341e80e4d2495a464d268e7579e038b4021d4cace2fee6ce14a9b4ce0d
fetched_at: '2026-06-28T22:39:57.360954+00:00'
product: protheus
section_id: 1500001549262
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFSE - E30 Item
  da lista inexistente
type: support-article
updated_at: '2025-06-02T12:30:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041806973-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSE-E30-Item-da-lista-inexistente
---

**Ocorrência**Ao transmitir uma NFSE ocorre a rejeição E30 - Item da lista inexistente, o que deverá ser feito?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.  
  
**Causa**Esse erro ocorre quando é informado um **Código de Serviço** com conteúdo e/ou formato incorretos no campo **B1\_CODISS** ou **BZ\_CODISS** (caso utilize indicador de produtos) ou [**CE1\_CPRISS (caso utilize a rotina FISA052)**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061751034-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFSe-Possibilidades-de-montagem-de-C%C3%B3digo-de-Servi%C3%A7o-C%C3%B3digo-de-Tributa%C3%A7%C3%A3o-e-CNAE-NFSEXMLENV-?source=search) **de acordo com o código que o contribuinte em questão está liberado à utilizar pela prefeitura.**Exemplo: O conteúdo/formato de um item pode variar de prefeitura para prefeitura:  
- 07.01 - 0701 - 7.01 - 701  
  
Existem também casos que a prefeitura descontinuou ou realizou alguma alteração no código em questão.  
  
**Solução**Entrar em contato com a prefeitura para solicitar o código correto (formato e conteúdo) a ser informado.  
  
*Obs.: Após a correção desse conteúdo deverá ser refeita a nota e transmiti-la. Caso o conteúdo destacado na nota seja diferente do informado no B1\_CODISS, verificar o conteúdo dos campos C6\_CODISS, D2\_CODISS e F3\_CODISS (o qual é utilizado para a montagem da tag).*
