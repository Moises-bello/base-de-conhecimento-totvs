---
content_hash: b8e4452e2635195c80e61779c108e22687fd4cdc6533239981b6800482b32506
fetched_at: '2026-06-29T00:11:07.091614+00:00'
page_id: '639193851'
product: rm
source: tdn-rm
title: Evento S-2231
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2231
version: 2
---

Leiautes1Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Registro\_eSocial | Campo\_eSocial | Tabela\_RM | Coluna\_RM | Informações\_do\_calculo |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| iniCessao | dtIniCessao | PFHSTAFT | DTINICIO |  |
| iniCessao | cnpjCess | PFHSTAFT | CNPJORGAOCEDIDO |  |
| iniCessao | respRemun |  |  | Caso PFHSTAFT.INFOONUS seja "1 - Ônus do Cedente" ou "3 - Ônus do Cedente e Cessionário" retorna S - Sim. Caso PFHSTAFT.INFOONUS seja "2 - Ônus do Cessionário"  retorna N - Não. |
| fimCessao | dtTermCessao | PFHSTAFT | DTFINAL |  |
