---
content_hash: 427297084817adb35600fd200068f125410cb668c666eb646208f419246f6b77
fetched_at: '2026-06-29T00:08:56.113192+00:00'
page_id: '351376174'
product: rm
source: tdn-rm
title: Evento S-1070
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1070
version: 8
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
| ideProcesso | tpProc |  |  | Se o valor do campo VPROCESSOS.TIPOPROCESSO for A - Administrativo, retorna 1, se for J - Judicial, retorna 2, se for N - Número do Benefício do INSS, retorna 3 , se for F - Processo FAP, retorna 4. |
| ideProcesso | nrProc | VPROCESSOS | NUMPROCESSO |  |
| ideProcesso | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual.. Caso seja incluído manualmente pela fila de eventos assume a competência Informada |
| ideProcesso | fimValid |  |  |  |
| dadosProc | indAutoria | VPROCESSOS | INDAUDITORIA |  |
| dadosProc | indMatProc | VPROCESSOS | INDMATPROC |  |
| dadosProc | observacao | VPROCESSOS | OBSERVACAO |  |
| dadosProcJud | ufVara | VJUNTAS | ESTADO |  |
| dadosProcJud | codMunic |  |  | Código recuperado através dos campos VJUNTAS.ESTADO e VJUNTAS.CODMUNICIPIO |
| dadosProcJud | idVara |  |  | Caso VJUNTAS.IDVARAESOCIAL exista então VJUNTAS.IDVARAESOCIAL senão VJUNTAS.CODJUNTA. |
| infoSusp | codSusp | VSUSPENSAOTRIB | CODINDSUSP |  |
| infoSusp | indSusp |  |  | Código recuperado através do campo VSUSPENSAOTRIB.INDSUSPENSAO. |
| infoSusp | dtDecisao | VSUSPENSAOTRIB | DATADECISAO |  |
| infoSusp | indDeposito |  |  | Caso VSUSPENSAOTRIB.DEPOSITOINTEGRAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |

true2Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideProcesso | tpProc |  |  | Se o valor do campo VPROCESSOS.TIPOPROCESSO for A - Administrativo, retorna 1, se for J - Judicial, retorna 2, se for N - Número do Benefício do INSS, retorna 3 , se for F - Processo FAP, retorna 4. |
| ideProcesso | nrProc | VPROCESSOS | NUMPROCESSO |  |
| ideProcesso | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual.. Caso seja incluído manualmente pela fila de eventos assume a competência Informada |
| ideProcesso | fimValid |  |  |  |
| dadosProc | indAutoria | VPROCESSOS | INDAUDITORIA |  |
| dadosProc | indMatProc | VPROCESSOS | INDMATPROC |  |
| dadosProc | observacao | VPROCESSOS | OBSERVACAO |  |
| dadosProcJud | ufVara | VJUNTAS | ESTADO |  |
| dadosProcJud | codMunic |  |  | Código recuperado através dos campos VJUNTAS.ESTADO e VJUNTAS.CODMUNICIPIO |
| dadosProcJud | idVara |  |  | Caso VJUNTAS.IDVARAESOCIAL exista então VJUNTAS.IDVARAESOCIAL senão VJUNTAS.CODJUNTA. |
| infoSusp | codSusp | VSUSPENSAOTRIB | CODINDSUSP |  |
| infoSusp | indSusp |  |  | Código recuperado através do campo VSUSPENSAOTRIB.INDSUSPENSAO. |
| infoSusp | dtDecisao | VSUSPENSAOTRIB | DATADECISAO |  |
| infoSusp | indDeposito |  |  | Caso VSUSPENSAOTRIB.DEPOSITOINTEGRAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |
