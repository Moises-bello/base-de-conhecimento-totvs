---
content_hash: 1186ea73f9d550b27a6558ecac9d227078e8a14e715f0fb5e1fef77bc037ab33
fetched_at: '2026-06-29T00:08:56.241726+00:00'
page_id: '351376335'
product: rm
source: tdn-rm
title: Evento S-2250
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2250
version: 4
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | nisTrab |  |  | Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;  Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| detAvPrevio | dtAvPrv | PFUNC | DTAVISOPREVIOTRAB |  |
| detAvPrevio | dtPrevDeslig | PFUNC | DTDEMISSAOPREVISTA |  |
| detAvPrevio | tpAvPrevio | PFUNC | TIPOAVISOAVISO |  |
| detAvPrevio | observacao | PFUNC | OBSERVACAOAVISOPREVIO |  |
| cancAvPrevio | dtCancAvPrv | PFUNC | DTCANCELAMENTOAVISO |  |
| cancAvPrevio | observacao | PFUNC | OBSCANCELAMENTOAVISO |  |
| cancAvPrevio | mtvCancAvPrevio | PFUNC | MOTIVOCANCELAMENTOAVISO |  |
