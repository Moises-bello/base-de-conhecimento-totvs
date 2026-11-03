---
content_hash: f205bc3d35cd0af54d2b31a531961499176821aac6e3e7e7595e4a846d616390
fetched_at: '2026-06-29T00:09:10.550932+00:00'
page_id: '398756586'
product: rm
source: tdn-rm
title: Evento S-1202 - Mapeamento
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1202+-+Mapeamento
version: 13
---

---

Leiautestrue2Leiaute S-1.3

Mapeamento dos campos para o leiaute S-1.3

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| Registro\_eSocial | Campo\_eSocial | Tabela\_RM | Coluna\_RM | Informações\_do\_calculo |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | indApuracao |  | INDAPURACAO |  |
| ideEvento | perApur |  |  | Informação recuperada através dos campos 'MESCOMP e ANOCOMP' da Tabela PESOCIALFOLHAMENSAL |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideTrabalhador | cpfTrab | PPESSOA | CPF |  |
| infoComplem | nmTrab | PFUNC | NOME |  |
| infoComplem | dtNascto | PPESSOA | DTNASCIMENTO |  |
| sucessaoVinc | cnpjOrgaoAnt | PFUNC | CNPJEMPRESAANTERIOR |  |
| sucessaoVinc | matricAnt | PFUNC | MATRICULAANTERIOR |  |
| sucessaoVinc | dtExercicio | PFUNC | DTEXERCICIO |  |
| sucessaoVinc | observacao | PFUNC | OBSERVACAOSUCESSAO |  |
| dmDev | ideDmDev |  |  | Recupera o valor do campo PFFINANC.NROPERIODO. Quando se trata de autônomo do Gestão Financeira ou Externo obtêm o valor de suas respectivas movimentações |
| dmDev | codCateg |  |  | As categorias válidas para o funcionário público com regime previdenciário RPPS ou Externo são: 301,302,303,304,305,306,307,308,309,310,311,312,313,401,410 |
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
| ideEstab | tpInsc |  |  | Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ" |
| ideEstab | nrInsc |  |  | Recupera o valor do campo PSECAO.CGC |
| remunPerApur | matricula | PFUNC | MATRICULAESOCIAL |  |
| itensRemun | codRubr | PEVENTO | CODIGO |  |
| itensRemun | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| itensRemun | qtdRubr | PFFINANC | REF |  |
| itensRemun | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| itensRemun | vrRubr | PFFINANC | VALOR |  |
| itensRemun | indApurIR |  |  | Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0. |
| infoPerAnt | remunOrgSuc |  |  | Se estiver marcado o campo 'Pagamento de verbas devidas pela empresa sucessora a empregados   desligados ainda na sucedida' no cadastro do Dissídio/Acordo Coletivo o valor será 'S', caso contrário será 'N'. |
| idePeriodo | perRef |  |  | O sistema buscará o mês e ano que existirem nos campos PFVERBASDIS.ANOREF e PFVERBASDIS.MESREF de acordo com a competência do desligamento. |
| ideEstab | tpInsc |  |  | Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ" |
| ideEstab | nrInsc |  |  | Recupera o valor do campo PSECAO.CGC |
| remunPerAnt | matricula | PFUNC | MATRICULAESOCIAL |  |
| itensRemun | codRubr | PEVENTO | CODIGO |  |
| itensRemun | ideTabRubr |  |  | Caso exista Prefixo para os eventos de tabela, retorna o caractere parametrizado, caso contrário, retorna GCOLIGADA.CODIGO |
| itensRemun | qtdRubr | PFFINANC | REF |  |
| itensRemun | fatorRubr |  |  | Caso PEVENTO.VALHORDIAREF seja Hora ou Referência retorna PEVENTO.PORCINCID, caso contrário retorna vazio |
| itensRemun | vrRubr | PFFINANC | VALOR |  |
| itensRemun | indApurIR |  |  | Se for verba de IRRF RRA (códigos de cálculo 207, 211 ou 215) o valor será 1, caso contrário será 0. |
