---
content_hash: 7c18f325c1fc3c8aa628aab5a7e97b7ec39a153127ca745065082d7266133168
fetched_at: '2026-06-29T00:08:56.069578+00:00'
page_id: '351376055'
product: rm
source: tdn-rm
title: Evento S-1020
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-1020
version: 13
---

Leiautestrue2Leiaute 2.5.0.0

Mapeamento dos campos para o leiaute 2.5.00

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideLotacao | codLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODLOTACAO.   Caso contrário recupera valor do campo PSECAO.CODIGO no nível de quebra da filial   ou no nível de quebra do FPAS caso o parâmetro "Utiliza quebra de FPAS" estiver marcado. |
| ideLotacao | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual. |
| ideLotacao | fimValid |  |  |  |
| dadosLotacao | tpLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.TIPOLOTACAOESOCIAL.   Caso contrário recupera valor do campo PSECAO.TPLOTACAO. |
| dadosLotacao | tpInsc |  |  | Caso TPLOTACAO seja 01, 10, 21, 24 ou 90 retorna vazio;  Caso TPLOTACAO seja 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ, "2 - CPF" ou "4 - CNO (Cadastro Nacional de Obra)"  Caso o valor retornado seja vazio, tag não é exibida. |
| dadosLotacao | nrInsc |  |  | Caso tpInsc seja 1 ou 2: se o parâmetro "Utiliza tomadores de serviço"   estiver marcado retorna valor do campo FCFO.CGCCFO.   Caso contrário retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 4: retorna FCFOCEI.CEI. |
| fpasLotacao | fpas |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.FPAS da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.FPAS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.FPAS. |
| fpasLotacao | codTercs |  |  | Caso a classificação tributária for igual a [01, 02, 03, 04] retorna "0000";  Senão Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.CODTERCEIROSINSS da seção informada   neste cadastro, caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCEIROSINSS. |
| fpasLotacao | codTercsSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária estiver   marcado recupera valor do campo PSECAO.CODTERCSSUSP da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROSSUSP.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCSSUSP. |
| procJudTerceiro | codTerc |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODTERCEIROS.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODTERCEIRO. |
| procJudTerceiro | nrProcJud |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.NROPROCESSO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.NRPROCJUD. |
| procJudTerceiro | codSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODINDICSUSPENSAO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODSUSPPROCJUDTERCEIRO. |
| infoEmprParcial | tpInscContrat |  |  | Caso o valor informado no campo FCFO.CGCCFO seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| infoEmprParcial | nrInscContrat | FCFO | CGCCFO |  |
| infoEmprParcial | tpInscProp |  |  | Caso o valor informado no campo PSECAO.CGC seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| infoEmprParcial | nrInscProp |  |  | Caso o campo "Tipo de Lotação Tributária" seja "02" e o campo "Empreitada Parcial" esteja marcado, retorna FCFO.CGCCFO.  Caso o campo "Tipo de Lotação Tributária" seja "02" e o campo "Empreitada Parcial" não esteja marcado, retorna PSECAO.CGC. |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |

true2Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações do Calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideLotacao | codLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODLOTACAO.   Caso contrário recupera valor do campo PSECAO.CODIGO no nível de quebra da filial   ou no nível de quebra do FPAS caso o parâmetro "Utiliza quebra de FPAS" estiver marcado. |
| ideLotacao | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual. |
| ideLotacao | fimValid |  |  |  |
| dadosLotacao | tpLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.TIPOLOTACAOESOCIAL.   Caso contrário recupera valor do campo PSECAO.TPLOTACAO. |
| dadosLotacao | tpInsc |  |  | Caso TPLOTACAO seja 01, 10, 21, 24 ou 90 retorna vazio;  Caso TPLOTACAO seja 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ, "2 - CPF" ou "4 - CNO (Cadastro Nacional de Obra)"  Caso o valor retornado seja vazio, tag não é exibida. |
| dadosLotacao | nrInsc |  |  | Caso parâmetro “Filial é SCP” esteja marcado retorna o valor do campo FCFO.CGCCFO da filial informada no campo DFILIAL.CODFILIALSOCIOSCP, independente do tpInsc;  Caso tpInsc seja 1 ou 2: se o parâmetro "Utiliza tomadores de serviço"   estiver marcado retorna valor do campo FCFO.CGCCFO.   Caso contrário retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 4: retorna FCFOCEI.CEI. |
| fpasLotacao | fpas |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.FPAS da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.FPAS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.FPAS. |
| fpasLotacao | codTercs |  |  | Caso a classificação tributária for igual a [01, 02, 03, 04] retorna "0000";  Senão Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.CODTERCEIROSINSS da seção informada   neste cadastro, caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCEIROSINSS. |
| fpasLotacao | codTercsSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária estiver   marcado recupera valor do campo PSECAO.CODTERCSSUSP da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROSSUSP.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCSSUSP. |
| procJudTerceiro | codTerc |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODTERCEIROS.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODTERCEIRO. |
| procJudTerceiro | nrProcJud |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.NROPROCESSO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.NRPROCJUD. |
| procJudTerceiro | codSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODINDICSUSPENSAO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODSUSPPROCJUDTERCEIRO. |
| infoEmprParcial | tpInscContrat |  |  | Caso o valor informado no campo FCFO.CGCCFO seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| infoEmprParcial | nrInscContrat | FCFO | CGCCFO |  |
| infoEmprParcial | tpInscProp |  |  | Caso o valor informado no campo PSECAO.CGC seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| infoEmprParcial | nrInscProp |  |  | Caso o Tipo de Lotação Tributária seja "02" e o campo "Empreitada Parcial" esteja marcado, retorna o CNPJ do Tomador de Serviço. Caso o Tipo de Lotação Tributária seja "02" e o campo "Empreitada Parcial" não esteja marcado, retorna o CNPJ do cadastro da Lotação Tributária. |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |

true2Leiaute S-1.1

Mapeamento dos campos para o leiaute S-1.1

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações do Calculo** |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideLotacao | codLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODLOTACAO.   Caso contrário recupera valor do campo PSECAO.CODIGO no nível de quebra da filial   ou no nível de quebra do FPAS caso o parâmetro "Utiliza quebra de FPAS" estiver marcado. |
| ideLotacao | iniValid |  |  | Se o tipo da operação for Carga Inicial, retorna a data de obrigatoriedade parametrizada, caso contrário, retorna a competência atual. |
| ideLotacao | fimValid |  |  |  |
| dadosLotacao | tpLotacao |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.TIPOLOTACAOESOCIAL.   Caso contrário recupera valor do campo PSECAO.TPLOTACAO. |
| dadosLotacao | tpInsc |  |  | Caso TPLOTACAO seja 01, 10, 21, 24 ou 90 retorna vazio;  Caso TPLOTACAO seja 04, 05, 06, 08 ou 09 retorna "1 - CNPJ";  Caso TPLOTACAO seja 03 ou 07 retorna "2 - CPF";  Caso TPLOTACAO seja 02 retorna "4 - CNO (Cadastro Nacional de Obra)";  Outro caso retorna "1 - CNPJ";  Para esse evento são válidos somente os códigos "1 - CNPJ, "2 - CPF" ou "4 - CNO (Cadastro Nacional de Obra)"  Caso o valor retornado seja vazio, tag não é exibida. |
| dadosLotacao | nrInsc |  |  | Caso parâmetro “Filial é SCP” esteja marcado retorna o valor do campo FCFO.CGCCFO da filial informada no campo DFILIAL.CODFILIALSOCIOSCP, independente do tpInsc;  Caso tpInsc seja 1 ou 2: se o parâmetro "Utiliza tomadores de serviço"   estiver marcado retorna valor do campo FCFO.CGCCFO.   Caso contrário retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 4: retorna FCFOCEI.CEI. |
| fpasLotacao | fpas |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.FPAS da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.FPAS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.FPAS. |
| fpasLotacao | codTercs |  |  | Caso a classificação tributária for igual a [01, 02, 03, 04] retorna "0000";  Senão Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária   estiver marcado recupera valor do campo PSECAO.CODTERCEIROSINSS da seção informada   neste cadastro, caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROS.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCEIROSINSS. |
| fpasLotacao | codTercsSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado:   se o parâmetro "Considera dados da seção" no cadastro de lotação tributária estiver   marcado recupera valor do campo PSECAO.CODTERCSSUSP da seção informada neste cadastro,   caso contrário recupera valor do campo PESOCIALLOTACAOTRIBUTARIA.CODTERCEIROSSUSP.   Caso o parâmetro "Utiliza tomadores de serviço" estiver desmarcado:   recupera valor do campo PSECAO.CODTERCSSUSP. |
| procJudTerceiro | codTerc |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODTERCEIROS.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODTERCEIRO. |
| procJudTerceiro | nrProcJud |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.NROPROCESSO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.NRPROCJUD. |
| procJudTerceiro | codSusp |  |  | Caso o parâmetro "Utiliza tomadores de serviço" estiver marcado   recupera valor do campo PESOCIALLOTACAOPROCESSOS.CODINDICSUSPENSAO.   Caso contrário recupera valor do campo PPROCJUDTERCEIRO.CODSUSPPROCJUDTERCEIRO. |
| infoEmprParcial | tpInscContrat |  |  | Caso o valor informado no campo FCFO.CGCCFO seja um CNPJ válido   retorna "1 - CNPJ". Caso o valor informado seja um CPF válido retorna "2 - CPF". |
| infoEmprParcial | nrInscContrat | FCFO | CGCCFO |  |
| infoEmprParcial | nrInscProp |  |  | Caso o Tipo de Lotação Tributária seja "02" e o campo "Empreitada Parcial" esteja marcado, retorna o CNPJ do Tomador de Serviço. Caso o Tipo de Lotação Tributária seja "02" e o campo "Empreitada Parcial" não esteja marcado, retorna o CNPJ do cadastro da Lotação Tributária. |
| novaValidade | iniValid |  |  |  |
| novaValidade | fimValid |  |  | Campo será preenchido com a data de encerramento informada ao executar o processo de Encerrar Atividades da Empresa. |
