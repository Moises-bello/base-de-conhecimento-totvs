---
content_hash: d770c6016852f8764b683eaf1c1146cd66c09307d42703a324c84b7dcf743ce4
fetched_at: '2026-06-29T00:10:21.285273+00:00'
page_id: '490980276'
product: rm
source: tdn-rm
title: Evento S-2240
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2240
version: 12
---

Leiautes1Leiaute S-1.2

Mapeamento dos campos para o leiaute S-1.2

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
| ideVinculo | codCateg | PFUNC | CODCATEGORIAESOCIAL |  |
| infoExpRisco | dtIniCondicao | |  | A data de início deve ser igual ou posterior à data de início da obrigatoriedade dos eventos de SST. |
| infoAmb | localAmb |  |  | Caso tenha tomador de serviço vinculado na tabela VTOMADORSERVICOVINC que não seja obra própria (PESOCIALCLIFOR.OBRAPROPRIA) retorna 2, caso contrário retorna 1. |
| infoAmb | dscSetor | PSECAO | DESCRICAO |  |
| infoAmb | tpInsc |  |  | Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| infoAmb | nrInsc |  |  | Caso o tipo de inscrição seja 4, retorna o CNO, caso tipo de inscrição seja 3, retorna o CAEPF, caso tipo de inscrição seja 1 retorna o CNPJ. |
| infoAtiv | dscAtivDes | |  | Conforme os parâmetros de profissiografia definidos no parametrizador do sistema TOTVS Segurança e Saúde Ocupacional (SSO) a informação poderá ter como origem:  Caso a profissiografia seja definida por Função: PFUNCAO.DESCRICAOPPP;  Caso a profissiografia seja definida pela Tarefa da Função: VTAREFA.DESCRICAO;  Caso a profissiografia seja definida por Quadro de Lotação: VMEMO.VALMEMO;  Caso a profissiografia seja definida pela Tarefa do Quadro de Lotação: VTAREFA.DESCRICAO;  Caso a profissiografia seja definida pela Função do Posto de Trabalho: VMEMO.VALMEMO;  Caso a profissiografia seja definida pela Tarefa da Função do Posto de Trabalho: VTAREFA.DESCRICAO;  Caso a profissiografia seja definida pela Tarefa do Funcionário: VTAREFA.DESCRICAO;    Caso mais de um parametro seja marcado os valores seram concatenados até o valor máximo permitido pelo campo. |
| agNoc | codAgNoc | VATIVPERIC | CODCLIENTE |  |
| agNoc | dscAgNoc | VTIPOSAGENTE | OBSERVACOES |  |
| agNoc | tpAval | VPPRARISCOS | TIPOMEDICAO |  |
| agNoc | intConc | VPPRAMEDICOES | VALORQUANTITATIVO |  |
| agNoc | limTol | VPPRANIVEISRISCO | LIMITETOLERANCIAQUANTI | |
| agNoc | unMed | VUNIDADEMEDIDA | DESCRICAO |  |
| agNoc | tecMedicao | VPPRATECNICASMEDICAO | DESCRICAO |  |
| agNoc | nrProcJud |  |  |  |
| epcEpi | utilizEPC | VPPRAMEDICOES | UTILIZACAOEPCNAOAPLICAVEL | |
| epcEpi | eficEpc |  |  | Caso VPPRAMEDICOES.UTILIZACAOEPCNAOAPLICAVEL da avaliação de risco seja igual a 1 (NÃO SE APLICA) a tag não será mostrada.   Caso VPPRAMEDICOES.UTILIZACAOEPCNAOAPLICAVEL da avaliação de risco seja igual a 0 e não existirem EPCs cadastrados para os riscos avaliados também não será impresso.  Caso VPPRAMEDICOES.UTILIZACAOEPCNAOAPLICAVEL da avaliação de risco seja igual a 0 e exista EPC cadastrado para o risco avaliado e VHISTEPISEGURANCA.EPIEFICAZ não esteja marcado o valor será 'N'.  Caso VPPRAMEDICOES.UTILIZACAOEPCNAOAPLICAVEL da avaliação de risco seja igual a 0 e exista EPC cadastrado para o risco avaliado e VHISTEPISEGURANCA.EPIEFICAZ esteja marcado o valor será 'S'. |
| epcEpi | utilizEPI | VPPRAMEDICOES | UTILIZACAOEPINAOAPLICAVEL | |
| epcEpi | eficEpi |  |  | Caso VPPRAMEDICOES.UTILIZACAOEPINAOAPLICAVEL da avaliação de risco seja igual a 1 (NÃO SE APLICA) a tag não será mostrada.   Caso VPPRAMEDICOES.UTILIZACAOEPINAOAPLICAVEL da avaliação de risco seja igual a 0 e não existirem EPIs cadastrados para os riscos avaliados também não será impresso.  Caso VPPRAMEDICOES.UTILIZACAOEPINAOAPLICAVEL da avaliação de risco seja igual a 0 e exista EPI cadastrado para o risco avaliado e VHISTEPISEGURANCA.EPIEFICAZ não esteja marcado o valor será 'N'.  Caso VPPRAMEDICOES.UTILIZACAOEPINAOAPLICAVEL da avaliação de risco seja igual a 0 e exista EPI cadastrado para o risco avaliado e VHISTEPISEGURANCA.EPIEFICAZ esteja marcado o valor será 'S'. |
| epi | docAval | VLOTEEPI | CA |  |
| epiCompl | medProtecao | VPPRAMEDICOES | MEDIDAPROTECAOEPI |  |
| epiCompl | condFuncto | VPPRAMEDICOES | CONDICOESFUNCIONAMENTOEPI | |
| epiCompl | usoInint | VPPRAMEDICOES | OBSERVADOUSOININTERRUPTOEPI | |
| epiCompl | przValid | VPPRAMEDICOES | PRAZOVALIDADEEPI |  |
| epiCompl | periodicTroca | VPPRAMEDICOES | PERIOTICIDADETROCAEPI |  |
| epiCompl | higienizacao | VPPRAMEDICOES | HIGIENIZACAOEPI |  |
| respReg | cpfResp | PPESSOA | CPF |  |
| respReg | ideOC | VRESPREGAMBIENTAL | CODORGAOCLASSE |  |
| respReg | dscOC | VORGAOCLASSE | DESCRICAO |  |
| respReg | nrOC | VRESPREGAMBIENTAL | REGCONSELHOCLASSE |  |
| respReg | ufOC | VRESPREGAMBIENTAL | CODUFREGISTRO |  |
| obs | obsCompl |  |  | Recupera valor do campo VINFOEXPRISCOOBS.OBSERVACAO conforme a dtIniCondicao |
