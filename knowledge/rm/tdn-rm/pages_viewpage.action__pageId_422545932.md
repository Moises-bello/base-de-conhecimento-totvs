---
content_hash: 5d5d395b8b9869d55a2a2e064a63355b07b09f4171738f309b929d08be049123
fetched_at: '2026-06-29T00:09:21.957116+00:00'
page_id: '422545932'
product: rm
source: tdn-rm
title: Bloco 0 (Livro e-DOC)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545932
version: 3
---

**0000: Abertura do Arquivo Digital e Identificação do Contribuinte**   
As informações dessa linha são retiradas do Cadastro da Filial selecionada na rotina. Campos 03 e 04 - Data de início e de fim devem estar contidas em um mesmo ano e correspondem ao período das informações contidas no bloco I.

**0001: Abertura do Bloco 0**   
Preenchido pela Rotina.

**0005: Dados Complementares do Contribuinte**   
Informações do Responsável e do endereço dos dados fiscais do cadastro da Filial.

**0030: Perfil do Contribuinte**   
Essa linha será gerada de acordo com os dados informados pelo usuário na tela da rotina.

**0100: Contabilista**   
Essa linha será gerada com as informações do Contador - Anexo "Dados Fiscais", pasta "Contador" do cadastro da Filial.

**0150: Tabela de Cadastro do Participante**   
Gerado com as informações do Cadastro de Cli/For que foram movimentados no período.

**0200: Tabela de Identificação do Item**   
Gerado com as informações dos produtos/serviços movimentados no período.

**0205: Código Anterior do Item**   
Este registro tem como objetivo registrar alterações ocorridas na Descrição e/ou Código do Produto existente no registro 0200.

**0210: Item Composto ou Relação Insumo/Produto**   
Não é gerado

**0450: Tabela de Informações Complementares/Registro de Observações**   
Esse registro aglutinou os registros 0450 e 0460 do SPED Fiscal.

**0455: Norma Referenciada**   
As normas são referenciadas nos lançamentos fiscais ou nas naturezas associadas aos lançamentos e nas guias de ICMS (tipo Normal).

**0460: Documento de Arrecadação**   
Referenciado Documento de Arrecadação é referenciado nos lançamentos fiscais.

**0465: Documento Fiscal Referenciado**   
O Documento Fiscal é referenciado nos lançamentos fiscais.   
   
**0470: Cupom Fiscal Referenciado**   
Considera itens referenciados em lançamento onde o código de modelo de documento seja igual a 02 ou 2D.

**0990: Encerramento do Bloco 0**   
Preenchido pela rotina.
