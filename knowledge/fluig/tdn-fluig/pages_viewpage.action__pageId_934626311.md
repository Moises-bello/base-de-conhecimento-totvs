---
content_hash: 580642979bc30e7ba336e5b4f54794ffbfc2997ed872e3dd19499cbf9164331b
fetched_at: '2026-06-28T21:35:31.443581+00:00'
page_id: '934626311'
product: fluig
source: tdn-fluig
title: Atualização para a nova versão do FLUIG.richeditor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=934626311
version: 13
---

## Atualização do componente

---

Recentemente, foi realizada uma atualização no componente FLUIG.richeditor com o objetivo de aumentar a estabilidade e a segurança da plataforma. A mudança causou alguns breaking changes. Isso significa que algumas inconsistências podem ocorrer para quem utiliza o componente via código, podendo haver a necessidade de realizar ajustes.

## Breaking changes

---

São alterações que podem impactar o código já existente e geralmente causando modificações na interface da API. Podem causar problemas em casos específicos.

| Ação | Alteração |
| --- | --- |
| viewHtml | Após essa alteração, não será mais possível adicionar scripts dentro do componente. O FLUIGC.richeditor sanitiza o HTML por motivos de segurança, especialmente ao visualizar ou editar conteúdo HTML através do modal "View HTML".  Esse processo de sanitização remove certos elementos como as tags `<script>` e `<style>` do conteúdo, por segurança e para prevenir ataques de XSS (Cross-Site Scripting). |
| converFtl e convertFtlAsync | Após essa alteração, não será mais possível carregar o componente dinamicamente, via `converFtl` e `convertFtlAsync`. |

## Alteração na configuração da toolbar do FLUIGC.richeditor

---

Compatibilidade modo escuro

Este recurso ainda não é compatível com o modo escuro lançado na atualização [Voyager 2.0](https://tdn.totvs.com/x/6HxjN). Para mais detalhes, consulte a documentação [Plataforma | Habilitar modo escuro](https://tdn.totvs.com/pages/viewpage.action?pageId=962611032#Plataforma%E2%9D%99Habilitarmodoescuro-Emquais%C3%A1reasn%C3%A3otemosomodoescuro?).

A forma de configurar a barra de ferramentas (toolbar) do `FLUIGC.richeditor` foi alterada. Não é mais possível configurar o `toolbar` e `toolbarGroups` **após** a inicialização do componente.

Agora, os botões e grupos devem ser definidos diretamente no momento da criação do editor, por meio da propriedade `tools`.

**Antes:**

jsRDarkExemplo de uso Rich Editor antes

**Agora:**

jsRDarkExemplo de uso Rich Editor agora

**Importante:**

* A configuração da toolbar **deve** ser feita no momento da inicialização do componente.
* Não há suporte para alterar a toolbar dinamicamente após o editor ser criado.
* Os nomes dos botões e grupos podem ter sofrido ajustes. Consulte a documentação atualizada do `FLUIGC.richeditor` para a lista completa de opções disponíveis em `tools`.

## Alterações de propriedades

---

As propriedades abaixo passaram por alterações ou foram removidas.

| Propriedade | Version | Description |
| --- | --- | --- |
| allowedContent | Removida | Propriedade removida. |
| baseFloatZIndex | Removida | Use `zIndex` do css. |
| disableNativeSpellChecker | Removida | Propriedade removida. |
| extraPlugins | Removida | Propriedade removida. |
| fullPage | Removida | Propriedade removida. |
| pasteFromWordRemoveFontStyles | Trocada | Utilize a propriedade *pasteCleanupAll*. Todas as tags HTML são removidas e deixado apensar o texto. |
| pasteFromWordRemoveStyles | Trocada | Utilize a propriedade *pasteCleanupCss* |
| removePlugins | Removida | Propriedade removida. |
