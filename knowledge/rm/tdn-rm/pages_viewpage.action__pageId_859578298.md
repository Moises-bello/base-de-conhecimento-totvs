---
content_hash: e70540d553b177570194a39bbd0029204a134118487da523d44b17f188b90e70
fetched_at: '2026-06-29T00:11:54.967772+00:00'
page_id: '859578298'
product: rm
source: tdn-rm
title: Webservice FopFuncData - Mapeamento Campos obrigatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859578298
version: 10
---

A lista abaixo apresenta apenas as tags obrigatórias para o cadastro de admissão através do webservice. Outros campos podem ser adicionados conforme necessidade no processo de admissão.

**ATENÇÃO:**

* Dependendo da parametrização da base, pode haver variação nos campos obrigatórios, o que pode levar o webservice a validar outros campos além dos listados.
* Devido a limitações das requisições REST, ressaltamos que o comportamento para o campo "CHAPA" pode variar. O campo "CHAPA" é uma **chave**, portanto **não pode ser nulo**. Para atender a parametrização de chapa autoincremento, é necessário enviar o campo vazio. Por exemplo:

> {  
>     "CODCOLIGADA": 1,  
>     **"CHAPA": "",**  
>     "CODSITUACAO": "A"  
> }

| TAG WEBSERVICE | DESCRIÇÃO | CAMPO |
| --- | --- | --- |
| <CODCOLIGADA></CODCOLIGADA> | Coligada | PFUNC.CODCOLIGADA |
| <CHAPA></CHAPA> | Chapa | PFUNC.CHAPA |
| <NROFICHAREG></NROFICHAREG> | Nº da Ficha de Registro | PFUNC.NROFICHAREG |
| <CODRECEBIMENTO></CODRECEBIMENTO> | Código de Recebimento | PFUNC.CODRECEBIMENTO |
| <CODSITUACAO></CODSITUACAO> | Código de Situação | Código de Situação |
| <HSTSIT\_MOTIVO></HSTSIT\_MOTIVO> | Data da Mudança de Situação | PFHSTSIT.DATAMUDANCA |
| <CODTIPO></CODTIPO> | Código do Tipo do Funcionário | PFUNC.CODTIPO |
| <CODSECAO></CODSECAO> | Código da Seção | PFUNC.CODSECAO |
| <MOTMUDANCASECAO></MOTMUDANCASECAO> | Motivo da Mudança de Seção | PFHSTSEC.MOTIVO |
| <CODFUNCAO></CODFUNCAO> | Código da Função | PFUNC.CODFUNCAO |
| <MOTMUDANCAFUNCAO></MOTMUDANCAFUNCAO> | Motivo da Mudança de Função | PFHSTFCO.MOTIVO |
| <CODSINDICATO></CODSINDICATO> | Código do Sindicato | PFUNC.CODSINDICATO |
| <JORNADA></JORNADA> | jornada | PFUNC.JORNADA |
| <CODHORARIO></CODHORARIO> | Código do Horário | PFUNC.CODHORARIO |
| <SALARIO></SALARIO> | Salário | PFUNC.SALARIO |
| <MOTMUDANCASALARIO></MOTMUDANCASALARIO> | Motivo da Mudança de Salário | PFHSTSAL.MOTIVO |
| <SITUACAOFGTS></SITUACAOFGTS> | Situação de FGTS | PFUNC.SITUACAOFGTS |
| <CONTRIBSINDICAL></CONTRIBSINDICAL> | Contribuição Sindical | PFUNC.CONTRIBSINDICAL |
| <APOSENTADO></APOSENTADO> | Aposentado | PFUNC.APOSENTADO |
| <TEMMAIS65ANOS></TEMMAIS65ANOS> | Tem Mais de 65 Anos | PFUNC.TEMMAIS65ANOS |
| <DATAADMISSAO></DATAADMISSAO> | Data de Admissão | PFUNC.DATAADMISSAO |
| <TIPOADMISSAO></TIPOADMISSAO> | Tipo de Admissão | PFUNC.TIPOADMISSAO |
| <MOTIVOADMISSAO></MOTIVOADMISSAO> | Motivo da Admissão | PFUNC.MOTIVOADMISSAO |
| <TEMPRAZOCONTR></TEMPRAZOCONTR> | Contrato tem Prazo Determinado | PFUNC.TEMPRAZOCONTR |
| <TEMAVISOPREVIO></TEMAVISOPREVIO> | Tem Aviso Prévio | PFUNC.TEMAVISOPREVIO |
| <QUERABONO></QUERABONO> | Quer Abono | PFUNC.QUERABONO |
| <QUER1APARC13O></QUER1APARC13O> | Quer 1ª Parcela de 13º | PFUNC.QUER1APARC13O |
| <FERIASCOLETIVAS></FERIASCOLETIVAS> | Férias Coletivas / Globais | PFUNC.FERIASCOLETIVAS |
| <SITUACAORAIS></SITUACAORAIS> | Situação RAIS | PFUNC.SITUACAORAIS |
| <MEMBROSINDICAL></MEMBROSINDICAL> | Membro Sindical | PFUNC.MEMBROSINDICAL |
| <MUDOUENDERECO></MUDOUENDERECO> | Mudou Endereço | PFUNC.MUDOUENDERECO |
| <MUDOUCARTTRAB></MUDOUCARTTRAB> | Mudou Carteira de Trabalho | PFUNC.MUDOUCARTTRAB |
| <MUDOUNOME></MUDOUNOME> | Mudou Nome | PFUNC.MUDOUNOME |
| <MUDOUPIS></MUDOUPIS> | Mudou PIS | PFUNC.MUDOUPIS |
| <MUDOUCHAPA></MUDOUCHAPA> | Mudou Chapa | PFUNC.MUDOUCHAPA |
| <MUDOUADMISSAO></MUDOUADMISSAO> | Mudou Data de Admissão | PFUNC.MUDOUADMISSAO |
| <MUDOUDTOPCAO></MUDOUDTOPCAO> | Mudou Data de Opção | PFUNC.MUDOUDTOPCAO |
| <MUDOUSECAO></MUDOUSECAO> | Mudou Seção | PFUNC.MUDOUSECAO |
| <MUDOUDTNASCIM></MUDOUDTNASCIM> | Mudou Data de Nascimento | PFUNC.MUDOUDTNASCIM |
| <FALTAALTERFGTS></FALTAALTERFGTS> | Falta Alterar FGTS | PFUNC.FALTAALTERFGTS |
| <DEDUZIRRF65></DEDUZIRRF65> | Deduzir IRRF Mais 65 | PFUNC.DEDUZIRRF65 |
| <CODFILIAL></CODFILIAL> | Código identificador da filial | PSECAO.CODFILIAL |
| <NOME></NOME> | Nome | PPESSOA.NOME |
| <INDINICIOHOR></INDINICIOHOR> | Índice de Início de Horário | PFUNC.INDINICIOHOR |
| <MEMBROCIPA></MEMBROCIPA> | Funcionário é membro da CIPA | PFUNC.MEMBROCIPA |
| <USASALCOMPOSTO>/USASALCOMPOSTO> | Usa Salário Composto | PFUNC.USASALCOMPOSTO |
| <REGATUAL></REGATUAL> | Funcionário é o atual? (0-Não/1-Sim)  ATENÇÃO:  Este campo sempre deverá ser preenchido com o valor "1", mesmo quando existir mais de um registro (múltiplos vínculos) na mesma coligada, exceto na situação onde o funcionário é transferido, neste caso o registro demitido deverá ficar com "Zero" e o registro ativo ficará "1". | PFUNC.REGATUAL |
| <JORNADAMENSAL></JORNADAMENSAL> | Jornada | PFUNC.JORNADAMENSAL |
| <CODOCORRENCIA>/CODOCORRENCIA> | Código da Ocorrência | PFUNC.CODOCORRENCIA |
| <ESUPERVISOR></ESUPERVISOR> | Funcionário tem status de supervisor? | PFUNC.ESUPERVISOR |
| <USACONTROLEDESALDO>/USACONTROLEDESALDO> | Usa Controle de Saldo de Verbas? | PFUNC.USACONTROLEDESALDO |
| <MUDOUCI></MUDOUCI> | Mudou Código Contribuinte Individual | PFUNC.MUDOUCI |
| <FGTSMESANTRECOLGRFP>/FGTSMESANTRECOLGRFP> | FGTS mês anterior será recolhido na GRFC | PFUNC.FGTSMESANTRECOLGRFP |
| <POSSUIALVARAMENOR16>/POSSUIALVARAMENOR16> | Tem alvará judicial p/func menor 16 anos | PFUNC.POSSUIALVARAMENOR16 |
| <POSICAOABONO></POSICAOABONO> | Posição Abono | PFUNC.POSICAOABONO |
| <QUERADIANTAMENTO></QUERADIANTAMENTO> | Quer adiantamento nas férias | PFUNC.QUERADIANTAMENTO |
| <SEXO></SEXO> | Sexo | PPESSOA.SEXO |
| <GRAUINSTRUCAO></GRAUINSTRUCAO> | Grau de Instrução | PPESSOA.GRAUINSTRUCAO |
| <NATURALIDADE></NATURALIDADE> | Naturalidade | PPESSOA.NATURALIDADE |
| <DTNASCIMENTO></DTNASCIMENTO> | Data de Nascimento | PESSOA.DTNASCIMENTO |
| <NIT></NIT> | NIT - Tipo de Carteira de Trabalho | PPESSOA.NIT |
| <CPF></CPF> | CPF | PPESSOA.CPF |
| <Jornada\_Mensal></Jornada\_Mensal> | Jornada | - |
| <ESTADONATAL></ESTADONATAL> | Estado Natal | PPESSOA.ESTADONATAL |
| <CODCATEGORIAESOCIAL></CODCATEGORIAESOCIAL> | Código Categoria eSocial | PFUNC.CODCATEGORIAESOCIAL |
| <FUMANTE></FUMANTE> | Fumante | PPESSOA.FUMANTE |
| <CONJUGEBRASIL></CONJUGEBRASIL> | Cônjuge Brasil | PPESSOA.CONJUGEBRASIL |
| <NATURALIZADO></NATURALIZADO> | Naturalizado | PPESSOA.NATURALIZADO |
| <FILHOSBRASIL></FILHOSBRASIL> | Filhos no Brasil | PPESSOA.FILHOSBRASIL |
| <DTMUDANCASALARIO></DTMUDANCASALARIO> | Data da Mudança de Salário | PFHSTSAL.DTMUDANCA |
| <DTMUDANCAFUNCAO></DTMUDANCAFUNCAO> | Data da Mudança de Função | PFHSTFCO.DTMUDANCA |
| <HSTSIT\_DATAMUDANCA></HSTSIT\_DATAMUDANCA> | Data da Mudança de Situação | PFHSTSIT.DATAMUDANCA |
| <DTMUDANCASECAO></DTMUDANCASECAO> | Data da Mudança de Seção | PFHSTSEC.DTMUDANCA |
| <HSTSEFIP\_DTMUDANCA></HSTSEFIP\_DTMUDANCA> | Data da Mudança das Informações SEFIP | PHSTOCORRENCIA.DTMUDANCA |
| <HSTBANCO\_DTMUDANCA>/HSTBANCO\_DTMUDANCA> | Data da Mudança dos Dados Bancários | PFHSTCPGTO.DTMUDANCA |
| <DTMUDANCAHORARIO></DTMUDANCAHORARIO> | Data da Mudança de Horário | PFHSTHOR.DTMUDANCA |
