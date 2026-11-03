---
content_hash: 896fe19276897f68279ba49c7bda1f388260c917eac93343fb05fe6fa9943606
fetched_at: '2026-06-29T00:09:22.005029+00:00'
page_id: '422545945'
product: rm
source: tdn-rm
title: Bloco C (Livro e-DOC)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545945
version: 3
---

**C001: Abertura do Bloco C**   
Preenchido pela rotina.

**C020: Documento - Nota Fiscal (Código 01), Nota Fiscal de Produtor (Código 04) e Nota Fiscal Eletrônica (Código 55)**   
Seleciona lançamento de entrada e saída com código modelo de documento 01, 04 e 55 com a natureza do tipo "Fiscal".

**C040: Complemento do Documento – ISS**   
Seleciona lançamentos que possuem o tributo ISS informado no lançamento e que foram gerados no registro C020.

**C300: Itens do Documento**   
Esse registro e gerado com as informações dos Itens associados aos lançamentos gerados no registro C020.

**C310: Complemento do Item – ISS**   
É gerado caso exista o tributo ISS no item gerado no registro C300.

**C550: Documento - Nota Fiscal de Venda a Consumidor (Código 02)**   
Seleciona lançamentos de entrada e saída, com código modelo de documento 02 e onde a natureza é do tipo "Fiscal".

**C560: Itens do Documento**   
Considera os itens dos lançamentos selecionados na geração do registro

**C600: Documento - Cupom Fiscal/ICMS (Código 2D e Código 02)**   
Considera lançamentos com código modelo de documento 2D e 02.

**C605: Complemento do Documento – ISS**   
Não é gerado.

**C610: Itens do Documento**   
Considera os itens dos lançamentos gerados no registro C600.

**C615: Complemento do Item – ISS**   
Não é gerado.

**C990: Encerramento do Bloco C**   
Gerado pela rotina.
