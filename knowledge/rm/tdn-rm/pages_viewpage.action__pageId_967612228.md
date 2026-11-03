---
content_hash: 8041d89459e9def480885594145a72fda773ca791b44475e3319fa576c56a8af
fetched_at: '2026-06-29T00:12:14.484985+00:00'
page_id: '967612228'
product: rm
source: tdn-rm
title: 'Envio de NFS-e TotvsColaboração: Mascara do código de serviço federal'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=967612228
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio  de NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26343 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar NFS-e a Tag itemlistaserv, não considerava o campo código de serviço federal do Anexo: Tributos do produto no município, no cadastro do produto.

E não aplicava a mascara cadastrada para o código de serviço federa quando buscado do Anexo: Dados Fiscais, no cadastro do produto.

## **03. SOLUÇÃO**

Realizado ajuste para que o código de serviço federal do Anexo: Tributos do produto no município seja considerado e caso não esteja preenchido, utilize o campo código de serviço federa quando buscado do Anexo: Dados Fiscais e aplicando a respectiva mascara, quando necessário.

Disponível à partir da biblioteca 12.1.2506
