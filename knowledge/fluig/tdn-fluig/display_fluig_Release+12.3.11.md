---
content_hash: 240f412c12475f8068c92a994c1b1ff3b06b81fa24b91a613e357c3f9182fe41
fetched_at: '2026-06-28T21:35:27.194926+00:00'
page_id: '501473369'
product: fluig
source: tdn-fluig
title: Release 12.3.11
type: documentation
url: https://tdn.totvs.com/display/fluig/Release+12.3.11
version: 5
---

Este documento contém breves descritivos acerca das implementações e correções efetuadas no pacote **12.3.11**.

## Implementações

#### TOTVS | ESB Plugin e TOTVS | ESB Server

**Função**: **Componente Transformer**

**Situação**: Era apresentado o erro "The entity name must immediately follow the '&' in the entity reference." ao executar o componente DocIdentifier em um XML com o caractere **&** no seu conteúdo, pois esse caractere não é considerado válido para conteúdo de uma tag XML

**Solução**: Realizada correção para substituir o caractere **&** por **E** ao utilizar o componente DocIdentifier e ao utilizar a opção "Remove Special Chars" do componente Transformer.
