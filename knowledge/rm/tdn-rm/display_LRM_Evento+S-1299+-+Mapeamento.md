---
content_hash: b08e090543444eb373d7fbec93e975e4fc63ee1e9543d8e06d7ea35ff57e84c2
fetched_at: '2026-06-29T00:08:56.473116+00:00'
page_id: '351376552'
product: rm
source: tdn-rm
title: Evento S-1299 - Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1299+-+Mapeamento
version: 16
---

Leiautes2Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | indGuia |  |  | Campo gerado com valor fixo '1' apenas para empregador com natuzera jurídica 402-2 - Segurado Especial |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoFech | evtRemun |  |  | É verificado se existe na fila de eventos para o mês/ano competência selecionado o evento S1200, S1202, S1207, S2299, S2399.  Caso exista, será atribuído o valor S [Sim], do contrário o valor será N [Não]. |
| infoFech | evtComProd |  |  | É verificado se existe na fila de eventos para o mês/ano competência selecionado o evento S1260.  Caso exista, será atribuído o valor S [Sim], do contrário o valor será N [Não]. |
| infoFech | evtContratAvNP |  |  | É verificado se existe na fila de eventos para o mês/ano competência selecionado o evento S1270.  Caso exista, será atribuído o valor S [Sim], do contrário o valor será N [Não]. |
| infoFech | evtInfoComplPer |  |  | É verificado se existe na fila de eventos para o mês/ano competência selecionado o evento S1280.  Caso exista, será atribuído o valor S [Sim], do contrário o valor será N [Não]. |
| infoFech | indExcApur1250 |  |  | Quando precisar retificar um S-1250 a partir de 19/07/2021, deverá enviar a retificação/exclusão pelo REINF com essa tag preenchida |
| infoFech | transDCTFWeb |  |  | O valor S [Sim] é atribuído se o campo "Transmissão Imediata da DCTFWeb" estiver marcado no cadastro de "Período de Apuração". |
| infoFech | naoValid |  |  | Recupera valor do campo PESOCIALFOLHAMENSAL.INDICATIVONAOVALIDAFECHAMENTO  Indicativo de não validação das regras de fechamento, para que os grandes contribuintes possam reduzir o tempo de processamento do evento. O não preenchimento deste campo ou seu preenchimento com [S] implica a não execução da REGRA\_VALIDA\_FECHAMENTO\_FOPAG. Para executá-la, informar [N]. **Valores válidos:** **S** - Sim **N** - Não |
| infoFech | evtPgtos |  |  | É verificado se existe na fila de eventos para o mês/ano competência selecionado o evento S1210.  Caso exista, será atribuído o valor S [Sim], do contrário o valor será N [Não]. |
