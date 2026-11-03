---
content_hash: b5351734907c7c9ce698ce829adcc18e15dc88bc6d6cca14cb1b87c66ff365c1
fetched_at: '2026-06-29T00:05:52.809925+00:00'
page_id: '1060234333'
product: rm
source: tdn-rm
title: API Aditivo
type: documentation
url: https://tdn.totvs.com/display/LRM/API+Aditivo
version: 3
---

## 📊 APIs do Aditivo de Venda – DataServers (SOAP)

**🔑 Chave primária:** CODCOLIGADA, NUMVENDA, NUMADIT, CODTIPOADIT

| DataServer | Classe | Descrição |
| --- | --- | --- |
| ImbVendaAditivoData | ImbVendaAditivoData | Listagem geral de aditivos da venda. Visão principal com todos os tipos de aditivos |
| ImbVendaAditivoAltValorParcelaData | ImbVendaAditivoAltValorParcelaData | Aditivo de Alteração de Valor de Parcela. Retorna as tabelas XADITALTERACAOVR, XADITALTERACAOVRPARC e XADITALTERACAOVRPARCCOMPN |
| ImbVendaAditivoVencimentoData | ImbVendaAditivoVencimentoData | Aditivo de Vencimento. Permite alterar datas de vencimento das parcelas |
| ImbVendaAditivoRenegociacaoData | ImbVendaAditivoRenegociacaoData | Aditivo de Renegociação. Renegociação de parcelas da venda |
| ImbVendaAditivoTrocaCompradorData | ImbVendaAditivoTrocaCompradorData | Aditivo de Troca de Comprador. Substitui o comprador na venda |
| ImbVendaAditivoTrocaSubunidadeData | ImbVendaAditivoTrocaSubunidadeData | Aditivo de Troca de Subunidade/Lote. Troca a subunidade vinculada à venda |
| ImbVendaAditivoFiadorData | ImbVendaAditivoFiadorData | Aditivo de Fiador. Inclusão/alteração de fiador na venda |
| ImbVendaAditivoOutrosData | ImbVendaAditivoOutrosData | Aditivo de Outros. Aditivos sem tipo específico |
| ImbVendaAditivoGlobalData | ImbVendaAditivoGlobalData | Aditivo Global. Visão para aditivos executados em lote (globais) |

## 📊 APIs do Aditivo de Venda – Processos (SOAP / RMSProcess)

| Processo | Classe | Descrição |
| --- | --- | --- |
| ImbVendaAditivoEfetivarProc | ImbVendaAditivoEfetivarProc | Efetivar aditivo. Altera status para "Efetivado", gera atendimento e aplica alterações no financeiro |
| ImbVendaAditivoDesfazerProc | ImbVendaAditivoDesfazerProc | Desfazer aditivo. Reverte um aditivo efetivado ao estado anterior |
| ImbVendaAditivoCancelarProc | ImbVendaAditivoCancelarProc | Cancelar aditivo. Cancela aditivo em preparação e exclui atendimentos vinculados |
| ImbVendaExcluirAditivoProc | ImbVendaExcluirAditivoProc | Excluir aditivo. Remove fisicamente do banco |
| ImbVendaAditivoAditivoAltValorParcelaGlobalProc | ImbVendaAditivoAditivoAltValorParcelaGlobalProc | Calcular aditivo de alteração de valor (global). Cria aditivo em lote aplicando fórmula ou valor fixo |
| ImbVendaAditivoAltValorParcelaReajusteProc | ImbVendaAditivoAltValorParcelaReajusteProc | Reajustar aditivo de alteração de valor. Aplica reajuste nas parcelas |
| ImbVendaAditivoVencimentoCalcularProc | ImbVendaAditivoVencimentoCalcularProc | Calcular aditivo de vencimento. Gera novas datas de vencimento |
| ImbVendaAditivoGlobalRenegociadorProc | ImbVendaAditivoGlobalRenegociadorProc | Renegociação global. Executa renegociação em lote, podendo efetivar ou desfazer |
| ImbVendaAditivoContabilizarProc | (contabilização) | Contabilizar aditivo. Gera lançamentos contábeis |
| ImbVendaAditivoExcluirContabilizacaoProc | (excluir contabilização) | Excluir contabilização. Remove lançamentos contábeis |

---

## 📊 XADITALTERACAOVR – Totais do Aditivo - TAGS

| Tag XML | Descrição | Cálculo |
| --- | --- | --- |
| VRTOTALPARCALTATUAL | Valor total bruto atual das parcelas | VRPARCATUAL de cada parcela |
| VRTOTALPARCALTNOVO | Novo valor total bruto após alteração | VRPARCNOVO de cada parcela |
| VRTOTALPRINCIPALALTATUAL | Valor total do principal (sem reajuste) | ValorOriginal de cada parcela |
| VRTOTALPRINCIPALALTNOVO | Novo valor total do principal | ValorOriginalNovo de cada parcela |
| VRTOTALREAJALTATUAL | Reajuste atual (Juros Contrato + CM) | ValorJuros + ValorCM) de cada parcela |
| VRTOTALREAJALTNOVO | Novo reajuste após alteração | (ValorJurosNovo + ValorCMNovo) de cada parcela |
| VRTOTALMULTAATRASOPARCALT | Multa por atraso total | ValorMultaAtraso de cada parcela |
| VRTOTALJUROSMORAPARCALT | Juros de mora total | ValorJurosMora de cada parcela |

## 📊 XADITALTERACAOVRPARC – Detalhe por Parcela - TAGS

| Tag XML | Descrição | Cálculo |
| --- | --- | --- |
| VRPARCATUAL | Valor bruto atual (Principal + CM + Juros Contrato – Descontos) | Carregado do lançamento financeiro |
| VRPARCNOVO | Novo valor bruto após alteração | componente.ValorComponenteNovo × Sinal(TipoComponente) |
| VRLIQUIDOPARCALT | Valor líquido atual (pode incluir multa e juros mora) | RetornoCalculoValorLiquido.ValorLiquido |
| VRLIQUIDOPARCALTNOVO | Novo valor líquido da parcela | VRLIQUIDOPARCALT - (VRPARCATUAL - VRPARCNOVO) |
| VRCMPARCALT | Correção Monetária da parcela | ValorCM - ValorCMBaixado |
