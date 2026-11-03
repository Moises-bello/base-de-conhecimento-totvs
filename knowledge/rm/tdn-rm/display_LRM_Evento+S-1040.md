---
content_hash: 765e363011e3c10c536d4acbe0ecd685923df45de4689f55b3b5f6661f0fb63d
fetched_at: '2026-06-29T00:08:56.080372+00:00'
page_id: '351376155'
product: rm
source: tdn-rm
title: Evento S-1040
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1040
version: 4
---

Leiautestrue1Leiaute 2.5.00

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideFuncao | codFuncao | PFUNCAO | CODIGO |  |
| ideFuncao | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual.. Caso seja incluído manualmente pela fila de eventos assume a competência Informada |
| ideFuncao | fimValid |  |  |  |
| dadosFuncao | dscFuncao | PFUNCAO | NOME |  |
| dadosFuncao | codCBO | PFUNCAO | CBO2002 |  |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |
