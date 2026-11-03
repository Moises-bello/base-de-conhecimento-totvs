---
content_hash: 5ab057b66628e693c7e7ed35054f4246f880c49e6aa6b057d9fb1f92f1ed7d74
fetched_at: '2026-06-29T00:08:56.074446+00:00'
page_id: '351376058'
product: rm
source: tdn-rm
title: Evento S-1030
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1030
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
| ideCargo | codCargo | PFUNCAO | CODIGO |  |
| ideCargo | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual.. Caso seja incluído manualmente pela fila de eventos assume a competência Informada |
| ideCargo | fimValid |  |  |  |
| dadosCargo | nmCargo | PFUNCAO | NOME |  |
| dadosCargo | codCBO | PFUNCAO | CBO2002 |  |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerrado informada ao executar o processo de Encerrar Atividades da Empresa. |
