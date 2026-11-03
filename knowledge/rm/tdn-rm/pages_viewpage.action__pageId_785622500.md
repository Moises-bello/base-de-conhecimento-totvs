---
content_hash: 635d92718002ab3bcbe6a743fa9ca56c12fa21d60a59edd7ffc943e7646f8580
fetched_at: '2026-06-29T00:11:38.879292+00:00'
page_id: '785622500'
product: rm
source: tdn-rm
title: Integração - TOTVS RH - Avaliação e Desempenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=785622500
version: 14
---

O usuário terá a opção de escolher tanto a integração quanto os ambientes a serem utilizados no processo de integração.

A seguir, fornecemos informações detalhadas sobre as configurações necessárias.

11Performance & MetasPerformance & Metas

**Tenant / Client ID / Client Secret**

Dados fornecidos para a conexão com a "Performance & Metas".  Mais detalhes [clique aqui.](https://tdn.totvs.com/pages/viewpage.action?pageId=686464694)

2FeedzFeedz

**Token**

Dados fornecidos para a conexão com a "Feedz". Mais detalhes clique aqui.

**Concatenar Descrição do Cargo (Descrição + Código)**: Ao selecionar esse parâmetro, o sistema irá combinar a descrição da função com o seu código correspondente.

Por exemplo, se o código da função for "0001" e a descrição for "Gerente", após ativar esse parâmetro, o sistema enviará para a Feedz a informação "Gerente 0001". 

Importante ressaltar que, caso o parâmetro não esteja marcado e houver Cargos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.

**Concatenar Descrição do Departamento (Descrição + Código)**: Ao selecionar esse parâmetro, o sistema incluirá tanto a descrição da seção quanto o seu código correspondente.

Por exemplo, se o código da seção for "01.01" e a descrição for "Administrativa", ao ativar esse parâmetro, o sistema enviará para a Feedz a informação "Administrativa 01.01".

Importante ressaltar que, caso o parâmetro não esteja marcado e houver Departamentos com a mesma descrição, ocorrerá um erro na integração. Isso acontece devido à descrição ser um elemento-chave na Feedz.
