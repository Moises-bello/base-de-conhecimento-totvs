---
content_hash: e6c20e74204de435cd8fab3a16f9f12adbf222cedbffee65569aba8f49b373a9
fetched_at: '2026-06-28T21:35:18.801613+00:00'
page_id: '185738869'
product: fluig
source: tdn-fluig
title: Internacionalização (i18n)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=185738869
version: 21
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é apresentar os procedimentos necessários para adaptar a plataforma Fluig para ser traduzida para outros idiomas.

# Conceito e configuração

O conceito de internacionalização ou i18n *(*que, por vezes, também é chamado de "Localização"*)* consiste no desenvolvimento e/ou adaptação de um produto para o idioma de um ou mais países. O acrônimo *"*i18n*"* origina-se do inglês "*internationalization*", onde 18 é o número de letras entre o primeiro *"*i*"* e o último *"*n*"*.

Na plataforma Fluig, o i18n é suportado na forma de arquivos de propriedades distintos para cada idioma. Sempre que for [criado um projeto a partir do Fluig Studio](http://tdn.totvs.com/display/fluig/Criando+um+projeto+Fluig+no+Studio), a estrutura de *i18n* será apresentada conforme o exemplo a seguir:

Não se engane!

O nome do componente *(widget, layout etc.)* em questão coincide com o prefixo dos arquivos i18n. Este é o comportamento padrão do Studio, mas não é isso que fará com que as funções de i18n funcionem corretamente em seu componente. Dentro do  deve existir uma propriedade chamada [locale.file.base.name](http://tdn.totvs.com/display/fluig/Arquivo+application.info#Arquivoapplication.info-locale.file.base.name). O importante é que o valor desta propriedade - esse sim - seja o mesmo que o prefixo dos arquivos i18n.

# Utilização no desenvolvimento

Nos arquivos i18n o cadastro deve ser feito da seguinte forma:

text

## Arquivos de fontes *freemarker* (.ftl) e *javascript* (.js)

Quando é necessário referenciar o valor da tradução desejada, deve-se utilizar o código *"${i18n.getTranslation('codigo.da.label')}"*.

Em arquivos .js a partir da versão **1.8.3** é possível utilizar o código *"[=i18n.getTranslation('codigo.da.label')]"* para evitar conflitos com template string.

### Arquivo .ftl:

xml
${i18n.getTranslation('codigo.da.label')}
