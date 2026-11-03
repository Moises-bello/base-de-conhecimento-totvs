---
content_hash: e6a70c744c6725e4cac11334b240e5839b783995a36db27bc4cd87d948b74472
fetched_at: '2026-06-29T00:08:56.294218+00:00'
page_id: '351376475'
product: rm
source: tdn-rm
title: Evento S-3000
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-3000
version: 5
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
| infoExclusao | tpEvento |  |  | Tipo do evento de origem que está sendo excluído. |
| infoExclusao | nrRecEvt |  |  | ID do evento de origem que está sendo excluído. |
| ideTrabalhador | cpfTrab |  | CPF |  |
| ideTrabalhador | nisTrab |  |  | Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;  Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
| ideFolhaPagto | indApuracao |  |  | Indicativo do período de apuração do evento "periódico" que está sendo excluído (1-Mensal / 2-Anual) |
| ideFolhaPagto | perApur |  |  | Período de apuração do evento "periódico" que está sendo excluído (Mês/Ano para eventos mensais, somente Ano para eventos anuais) |

true2Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

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
| infoExclusao | tpEvento |  |  | Tipo do evento de origem que está sendo excluído. |
| infoExclusao | nrRecEvt |  |  | ID do evento de origem que está sendo excluído. |
| ideTrabalhador | cpfTrab |  |  |  |
| ideFolhaPagto | indApuracao |  |  | Indicativo do período de apuração do evento "periódico" que está sendo excluído (1-Mensal / 2-Anual) |
| ideFolhaPagto | perApur |  |  | Período de apuração do evento "periódico" que está sendo excluído (Mês/Ano para eventos mensais, somente Ano para eventos anuais) |
|  |  |  |  |  |
