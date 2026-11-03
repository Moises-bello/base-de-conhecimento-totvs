---
content_hash: 4271484e7d2711c343c1a89ced327130d148a3245e0c7777b3781732faff03ee
fetched_at: '2026-06-29T00:11:26.739615+00:00'
page_id: '719675959'
product: rm
source: tdn-rm
title: Evento S-3500
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-3500
version: 5
---

Leiautes1Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Registro\_eSocial | Campo\_eSocial | Tabela\_RM | Coluna\_RM | Informações\_do\_calculo |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| infoExclusao | tpEvento |  |  | Tipo do evento de origem que está sendo excluído. |
| infoExclusao | nrRecEvt |  |  | ID do evento de origem que está sendo excluído. |
| ideProcTrab | nrProcTrab |  |  | Número do processo trabalhista |
| ideProcTrab | cpfTrab |  |  | CPF do trabalhador do evento S-2500 que está sendo excluído |
| ideProcTrab | perApurPgto |  |  | Período de apuração do evento S-2501 ou do evento S-2555 que está sendo excluído (Mês/ano em que é devida a obrigação de pagar a parcela prevista no acordo/sentença) |
| ideProcTrab | ideSeqProc |  |  | Número sequencial do conjunto de dados de tributos do evento S-2501 ou número sequencial de múltiplos eventos S-2500 que estão sendo excluídos |
