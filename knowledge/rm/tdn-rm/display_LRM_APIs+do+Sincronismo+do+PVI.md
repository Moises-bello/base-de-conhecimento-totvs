---
content_hash: 520570f3f3fe8681e72b5441a668a8ae8788679f65272fd6c6b6c5a61e395385
fetched_at: '2026-06-29T00:05:47.838104+00:00'
page_id: '1018565566'
product: rm
source: tdn-rm
title: APIs do Sincronismo do PVI
type: documentation
url: https://tdn.totvs.com/display/LRM/APIs+do+Sincronismo+do+PVI
version: 6
---

### Nome dos DataServers do TCGI para usar na [API de DataServer](https://tdn.totvs.com/display/LRM/API+de+DataServer) e detalhes de cada cadastro [TOTVS Construção Gestão de Imóveis](https://tdn.totvs.com/pages/viewpage.action?pageId=198948892)

* #### Empreendimentos

1. ImbVendaEmpreendimentoData
2. ImbVendaEmpreendimentoUnidadeData
3. ImbVendaEmpreendimentoUnidadeSubunidadeData
4. ImbVendaEmpreendimentoUnidadeSubunidadeVagaData - Tabela com a situação: XSITUACAOSUBUNIDADE

* #### Modalidade/Tabela Preço

1. ImbVendaEmpreendimentoModalidadeData
2. ImbVendaModalidadeData
3. ImbVendaModalidadeRegraData
4. ImbVendaTabelaPrecoData  CODSITUACAOTABPRECO: EmPreparacao = 0,  Efetivada = 1, Revogada = 2, Cancelada = 3
5. ImbVendaTabelaPrecoSubUnidadeData

* #### Contratos

1. ImbVendaContratoData - Tabela com a situação: XSITUACAOVENDA
2. ImbVendaCompradorData
3. ImbVendaEmpreendimentoUnidadeSubunidadeData
4. ImbVendaFiadorData
5. ImbVendaContratoRegraData

* #### Comissões

1. ImbComissaoVisaoData
   1. STATUS => EmPreparacao = 0, Calculada = 1,  EmIntegracao = 2,
   2. TIPOCONTRATO => Venda = 0
   3. TIPOORIGEM =>  Conversor = 4,
2. ImbComissaoVisaoItemData
   1. STATUS => EmPreparacao = 0, Calculada = 1,  EmIntegracao = 2,
   2. TIPOQUEMRECEBE =>  Corretor = 0,  Imobiliaria = 1, SDR = 2, Fornecedor = 3, AvulsoPI = 4
   3. TIPOCOMISSAO =>  Percentual = 0,  ValorFixo = 1,  FormulaValor = 2,  FormulaPercentual = 3
   4. TIPOQUEMPAGA => Empresa = 0, Cliente = 1,
   5. TIPOCOMISSAOEMPRESA =>  ValorFixoNaoVinculadoAoRecebimentoParcelas = 0,  PercentualMaximoVinculadoAoRecebimentoParcelas = 1, ValorParcelaFormula = 2
   6. TIPOCOMISSAOCLIENTE => Decrescente = 0, ParcelasIguais = 1,  Proporcional = 2
   7. TIPOINTEGRACAO => TOTVSGestaoEstoqueComprasFaturamento = 0, TOTVSFolhaDePagamento = 1, TOTVSFinanceiro = 2, SemIntegracao = 3
3. ImbComissaoVisaoItemParcelaData

* #### Aditivos

1. ImbVendaAditivoData - Situação => CODSITADIT: EmPreparacao = 1, Efetivado = 2, Cancelado = 3,
2. ImbVendaAditivoFiadorData
3. ImbVendaAditivoAltValorParcelaData
4. ImbVendaAditivoOutrosData
5. ImbVendaAditivoRenegociacaoData
6. ImbVendaAditivoTrocaCompradorData
7. ImbVendaAditivoTrocaSubunidadeData
8. ImbVendaAditivoVencimentoData

* #### Distrato

1. ImbVendaDistratoData - Tabela com a situação: XSITUACAODISTRATO
2. ImbSituacaoDistratoData
3. ImbVendaMotivoDistratoData
4. ImbVendaTipoDistratoData

* #### Compradores/Corretores

1. #### [API de Cliente/Fornecedor](https://tdn.totvs.com/pages/viewpage.action?pageId=947313428)

* #### Consulta SQL

1. ####
