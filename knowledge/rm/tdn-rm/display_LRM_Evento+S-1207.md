---
content_hash: 50ef6ec8caa1784a9e000fe1c04aaf660e9f7c0a9f91c6c7ef173480059f8669
fetched_at: '2026-06-29T00:11:56.389959+00:00'
page_id: '865410747'
product: rm
source: tdn-rm
title: Evento S-1207
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1207
version: 2
---

---

Leiautestrue2Leiaute S-1.3

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
| ideBenef | cpfTrab |  |  |  |
| dmDev | ideDmDev |  |  | Recupera o valor do campo PFFINANC.NROPERIODO. Quando se trata de autônomo do Gestão Financeira ou Externo obtêm o valor de suas respectivas movimentações |
| dmDev | nrBeneficio | PFBENEFICIO | NUMEROBENEFICIO |  |
| dmDev | indRRA |  |  | Caso o valor do campo PFPERFF.NROPERIODO seja igual ao campo "Período folha/férias" ou "Período décimo terceiro" ou "Período rescisão" disponível no parametrizador retorna "S" |
| infoRRA | tpProcRRA | PFHSTRRA | TIPOPROCESSO |  |
| infoRRA | nrProcRRA | PFHSTRRA | NROPROCESSO |  |
| infoRRA | descRRA | PFHSTRRA | NATUREZARRA |  |
| infoRRA | qtdMesesRRA | PFHSTRRA | QTDMESES |  |
| despProcJud | vlrDespCustas | PFHSTRRA | VALORDAJUD |  |
| despProcJud | vlrDespAdvogados |  |  | Retorna o somatório dos valores do campo "VALORPAGOADVOGADO" da tabela "PFHSTRRAADVOGADOS" |
| ideAdv | tpInsc |  |  | Retorna 1 caso seja informado um CNPJ válido no campo "CPFCNPJADVOGADO" da tabela "PFHSTRRAADVOGADOS"  ou retorna 2 caso seja informado um CPF válido no campo "CPFCNPJADVOGADO" da tabela "PFHSTRRAADVOGADOS" |
| ideAdv | nrInsc | PFHSTRRAADVOGADOS | CPFCNPJADVOGADO |  |
| ideAdv | vlrAdv | PFHSTRRAADVOGADOS | VALORPAGOADVOGADO |  |
| ideEstab | tpInsc |  |  | Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Caso PSECAO.TPLOTACAO seja 01, 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso PSECAO.TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso PSECAO.TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ e "4 - CNO" |
| ideEstab | nrInsc |  |  | Caso PSECAO.TPLOTACAO seja 01, 03, 04, 05, 06, 07, 08 ou 09 retorna PSECAO.CGC;  Caso PSECAO.TPLOTACAO seja 02 retorna PSECAO.CNO;  Caso PSECAO.TPLOTACAO seja 10, 21, 24 ou 90 retorna vazio;  Outro caso retorna PSECAO.CGC;  Para esse evento são válidos somente os valores retornados do campo PSECAO.CGC ou PSECAO.CNO |
| itensRemun | codRubr | PEVENTO | CODIGO |  |
| itensRemun | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| itensRemun | qtdRubr | PFFINANC | REF |  |
| itensRemun | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| itensRemun | vrRubr | PFFINANC | VALOR |  |
| itensRemun | indApurIR |  |  | Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0. |
| descFolha | tpDesc |  |  | Caso PFEMPRT.EMPCONSGARANTFGTS seja igual a 2 retorna 1. |
| descFolha | instFinanc | PFEMPRT | MATINSTCONS |  |
| descFolha | nrDoc | PFEMPRT | NUMCONTEMPCONS |  |
| descFolha | observacao | PFEMPRT | OBSERVACAO |  |
