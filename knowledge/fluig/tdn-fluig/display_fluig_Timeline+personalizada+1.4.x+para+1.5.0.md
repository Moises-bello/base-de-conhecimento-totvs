---
content_hash: ca8ac511f5f1df1632930ca641f906e079243f3c92f2be9bb55199e0fd22bf24
fetched_at: '2026-06-28T21:35:19.086363+00:00'
page_id: '189315826'
product: fluig
source: tdn-fluig
title: Timeline personalizada 1.4.x para 1.5.0
type: documentation
url: https://tdn.totvs.com/display/fluig/Timeline+personalizada+1.4.x+para+1.5.0
version: 37
---

# Índice

none.\*ndicetrue

# Objetivo

Este guia é destinado aos desenvolvedores internos e externos do fluig. O objetivo é identificar e mapear todas as diferenças da *Timeline* personalizada entre as versões 1.4.x e 1.5.0.

Dica

Sugerimos que ao seguir este guia seja utilizado um programa de comparação (diff), que permita visualizadas as diferenças entre as versões 1.4.x e 1.5.0.

# application.info

Na versão 1.5.0 foi melhorado o componente de compartilhamento, sendo necessário adicionar estas dependências para *widget*.

As linhas abaixo, da versão 1.5.0, devem ser **ADICIONADAS** para a versão 1.4.x:

xmlAtenção!

Não esquecer de substituir o 'X' pela sequência dos componentes já configurados.

# edit.ftl

Na versão 1.5.0 foi adicionado mais um tipo de ordenação (mais *likes*), causando uma pequena alteração na estrutura do HTML.

Copiar o bloco abaixo que se encontra a partir da linha 34 da versão 1.5.0 e **SUBSTITUIR** na versão 1.4.x:

xml

${i18n.getTranslation('options.ordenation')}

${i18n.getTranslation('last.publications')}
${i18n.getTranslation('recently.publication')}
${i18n.getTranslation('more.like')}
