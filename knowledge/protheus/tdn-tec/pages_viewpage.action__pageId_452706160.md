---
content_hash: 3c84d096081dab62e9f7bbe0b02625b798c4e0b1929614c190721833c773866d
fetched_at: '2026-07-02T19:24:23.963906+00:00'
page_id: '452706160'
product: protheus
source: tdn-tec
title: Seção [Webapp] - Chave SSLCACertificateFile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452706160
version: 2
---

INLINE

SSLCACertificateFile

Atenção

A partir da versão 4.3.0 do webapp, utilize a chave

Indica o arquivo contendo a cadeia de certificados para validação do certificado do usuario, quando utilizada a chave **SSLClientAuth**.

Este arquivo deve conter os certificados na ordem da Raiz Certificadora, entidades intermediarias e entidade emissora do certificado do cliente, na ordem, codificadas no formato **PEM** (Base 64).

textExemplo de arquivo com a cadeia de certificadosExemplo
