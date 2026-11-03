---
content_hash: 39f18986cc3d74bab0301190e47cb7f292a71a9de7f15e319ad9d891dfe5de10
fetched_at: '2026-06-29T00:09:09.779496+00:00'
page_id: '394201961'
product: rm
source: tdn-rm
title: 3615516 FISCAL01-6223 DT NF-e - Geração das TAGs cEan e cEanTrib com SEM GTIN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394201961
version: 4
---

# NF-e - Geração das TAGs cEan e cEanTrib com SEM GTIN

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Serviços |
| **Módulo:** | Gestão Fiscal |
| **Função:** | Emissão de NF-e |
| **Situação/Requisito:** | Possibilitar a geração das TAGs cEan e cEanTrib com SEM GTIN antes de 01/12/2018 |
| **Solução/Implementação:** | De acordo com a NT 2017.001 v\_1.30 a obrigatoriedade de gerar as TAGs **cEan** e **cEanTrib** com a literal "**SEM** **GTIN**" no ambiente de **produção** é apenas após **01/12/2018**. Contudo, alguns estados já estão obrigando a geração desta informação no ambiente de produção antes do prazo e por este motivo estamos flexibilizando a geração destas TAGs conforme abaixo.  Para os estados que já estão obrigando a geração da literal "SEM GTIN" deverá ser preenchido no cadastro da Filial o "**Campo** **Livre** **2**" com a literal "**SEM** **GTIN**".  Cadastro da Filial >> Anexos >> Dados Fiscais >> Dados Adicionais >> Campo Livre 2    Com esta configuração, ao enviar uma NF-e com itens que não possuem código GTIN cadastrado, o XML será gerado com a literal "SEM GTIN" nas TAGs cEan e cEanTrib.  Após 01/12/2018 o processo enviará **automaticamente a** **literal "SEM GTIN"** independente do cadastro da Filial.  Ressaltamos que **não** **é necessário cadastrar um código de barras "SEM GTIN" no produto**. |
