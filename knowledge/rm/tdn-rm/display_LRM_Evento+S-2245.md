---
content_hash: a33e9845a7100a1d60aeace83497951535f688a1a4ebb11ce2c7a881d139c924
fetched_at: '2026-06-29T00:09:10.484662+00:00'
page_id: '398753816'
product: rm
source: tdn-rm
title: Evento S-2245
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2245
version: 6
---

Leiautes2Leiaute 2.5

Mapeamento dos campos para o leiaute 2.5.00

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
| ideVinculo | nisTrab |  |  | Caso seja autônomo e FCFO.NIT estiver preenchido, retorna FCFO.NIT, caso contrário, retorna FCFO.CIAUTONOMO;  Caso não seja autônomo e codCateg diferente de contribuinte individual (721, 722, 723, 731, 734, 738, 761, 771) retorna PFUNC.PISPASEP, caso contrario, retorna PFUNC.CI |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg | PFUNC | CODCATEGORIAESOCIAL |  |
| treiCap | codTreiCap | VCURSOS | CODTREINAMENTOESOCIAL |  |
| treiCap | obsTreiCap | VCURSOS | DESCRICAO |  |
| infoComplem | dtTreiCap |  |  | A data de início deve ser igual ou posterior à data de início da obrigatoriedade dos eventos de SST. |
| infoComplem | durTreiCap |  |  | Duração do treinamento/capacitação, em horas. |
| infoComplem | modTreiCap | VCURSOS | MODALIDADE |  |
| infoComplem | tpTreiCap | VCURSOS | TPTREINAMENTO |  |
| infoComplem | indTreinAnt |  |  | Valor Default definido como 'N'. Implementação se dará em momento posterior. |
| ideProfResp | cpfProf | PPESSOA | CPF |  |
| ideProfResp | nmProf | PPESSOA | NOME |  |
| ideProfResp | tpProf |  |  | Caso professor tenha uma matricula do eSocial atribuída a ele, ou seja, ele ser um funcionário cadastrado no sistema, seu valor será 1. Caso contrário será 2. |
| ideProfResp | formProf | VCURSOSACAD | NOME |  |
| ideProfResp | codCBO | VFORMACAOACAD | CBOFORMACAO |  |
| ideProfResp | nacProf |  |  | Código recuperado através do campo PPESSOA.NACIONALIDADE |
