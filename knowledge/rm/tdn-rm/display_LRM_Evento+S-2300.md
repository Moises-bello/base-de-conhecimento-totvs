---
content_hash: e118084c0fe6e0f9767050ff98773dc95093c034e397a78befd3406612fb2f94
fetched_at: '2026-06-29T00:08:56.390770+00:00'
page_id: '351376487'
product: rm
source: tdn-rm
title: Evento S-2300
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2300
version: 18
---

Leiautestrue1Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| trabalhador | cpfTrab |  |  |  |
| trabalhador | nmTrab | PFUNC | NOME |  |
| trabalhador | sexo | PPESSOA | SEXO |  |
| trabalhador | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| trabalhador | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| trabalhador | grauInstr |  |  | Caso PPESSOA.GRAUINSTRUCAO seja "1" retorna "1 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou";  Caso PPESSOA.GRAUINSTRUCAO seja "2" retorna "2 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular";  Caso PPESSOA.GRAUINSTRUCAO seja "3" retorna "3 - 5º ano completo do Ensino Fundamental";  Caso PPESSOA.GRAUINSTRUCAO seja "4" retorna "4 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)";  Caso PPESSOA.GRAUINSTRUCAO seja "5" retorna "5 - Ensino Fundamental Completo";  Caso PPESSOA.GRAUINSTRUCAO seja "6" retorna "6 - Ensino Médio incompleto";  Caso PPESSOA.GRAUINSTRUCAO seja "7" retorna "7 - Ensino Médio completo";  Caso PPESSOA.GRAUINSTRUCAO seja "8" retorna "8 - Educação Superior incompleta";  Caso PPESSOA.GRAUINSTRUCAO seja "9", "A" ou "C" retorna "9 - Educação Superior completa";  Caso PPESSOA.GRAUINSTRUCAO seja "B" retorna "10 - Pós-graduação completa";  Caso PPESSOA.GRAUINSTRUCAO seja "D" ou "E" retorna "11 - Mestrado completo";  Caso PPESSOA.GRAUINSTRUCAO seja "F", "G" ou "H" retorna "12 - Doutorado completo" |
| trabalhador | nmSoc | PPESSOA | NOMESOCIAL |  |
| nascimento | dtNascto | PPESSOA | DTNASCIMENTO |  |
| nascimento | paisNascto |  |  | Codificação de País obtida através do campo PPESSOA.ESTADONATAL |
| nascimento | paisNac |  |  | Código recuperado através do campo PPESSOA.NACIONALIDADE |
| brasil | tpLograd |  |  | Código recuperado através do campo PPESSOA.CODTIPORUA |
| brasil | dscLograd | PPESSOA | RUA |  |
| brasil | nrLograd | PPESSOA | NUMERO |  |
| brasil | complemento | PPESSOA | COMPLEMENTO |  |
| brasil | bairro | PPESSOA | BAIRRO |  |
| brasil | cep | PPESSOA | CEP |  |
| brasil | codMunic |  |  | Código recuperado através dos campos PPESSOA.ESTADO e PPESSOA.CODMUNICIPIO |
| brasil | uf | PPESSOA | ESTADO |  |
| exterior | paisResid |  |  | Código recuperado através do campo PPESSOA.IDPAIS |
| exterior | dscLograd | PPESSOA | RUA |  |
| exterior | nrLograd | PPESSOA | NUMERO |  |
| exterior | complemento | PPESSOA | COMPLEMENTO |  |
| exterior | bairro | PPESSOA | BAIRRO |  |
| exterior | nmCid | PPESSOA | CIDADE |  |
| exterior | codPostal | PPESSOA | CEP |  |
| trabImig | tmpResid |  |  | Caso PPESSOA.TIPOPRAZORESIDENCIA seja VERDADEIRO retorna "1" - Prazo indeterminado. Caso contrário, retorna "2" - Prazo determinado |
| trabImig | condIng |  |  | Recupera o valor do campo PPESSOA.CODCLASSIFTRABESTRANG |
| infoDeficiencia | defFisica |  |  | Caso PPESSOA.DEFICIENTEFISICO ou PPESSOA.DEFICIENTEFALA seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defVisual |  |  | Caso PPESSOA.DEFICIENTEVISUAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defAuditiva |  |  | Caso PPESSOA.DEFICIENTEAUDITIVO seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defMental |  |  | Caso PPESSOA.DEFICIENTEMENTAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defIntelectual |  |  | Caso PPESSOA.DEFICIENTEINTELECTUAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | reabReadap |  |  | Caso PPESSOA.BRPDH seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | observacao |  |  | Composto pelos campos PPESSOA.RECURSOREALIZACAOTRAB e PPESSOA.RECURSOACESSIBILIDADE |
| dependente | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| dependente | nmDep | PFDEPEND | NOME |  |
| dependente | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| dependente | cpfDep | PFDEPEND | CPF |  |
| dependente | depIRRF |  |  | Caso PFDEPEND.INCIRRF seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| dependente | depSF |  |  | Caso PFDEPEND.INCSALFAM seja VERDADEIRO  retorna "S";  Caso o dependente seja MENOR de 7 anos e PFDEPEND.CARTAOVACINA seja VERDADEIRO retorna "S";  Caso o dependente seja MAIOR de 7 anos e PFDEPEND.FREQESCOLAR seja VERDADEIRO retorna "S";  Caso o dependente seja MENOR de 1 ano e o parâmetro "Paga Salário Família Menor de 1 Ano Sem Cartão Vacina" seja VERDADEIRO retorna "S";  Para os demais casos, retorna "N". |
| dependente | incTrab |  |  | Se o grau de parentesco for '3 - Filho(a) Inválido' ou 'N - Irmã(o) Inválido' o valor será 'S', caso contrário será 'N'. |
| contato | fonePrinc | PPESSOA | TELEFONE1 |  |
| contato | emailPrinc | PPESSOA | EMAIL |  |
| infoTSVInicio | cadIni |  |  | Caso PESOCIALEVENTOS.TPOPERACAO seja "0 - Carga Inicial" retorna "S", caso contrário retorna "N" |
| infoTSVInicio | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoTSVInicio | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| infoTSVInicio | dtInicio | PFUNC | DATAADMISSAO |  |
| infoTSVInicio | nrProcTrab | PFUNC | NROPROCESSOTRABADMISSAO |  |
| infoTSVInicio | natAtividade |  |  | Caso PFUNC.ESOCIALNATATIVIDADE seja "2" retorna "2 - Trabalho Rural" caso contrário, retorna "1 - Trabalho Urbano" |
| cargoFuncao | nmCargo |  |  | Recupera o valor do campo PFUNCAO.NOME. |
| cargoFuncao | CBOCargo |  |  | Recupera o valor do campo PFUNCAO.CBO2002. |
| cargoFuncao | nmFuncao |  |  | Recupera o valor do campo PFUNCAO.NOME de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| cargoFuncao | CBOFuncao |  |  | Recupera o valor do campo PFUNCAO.CBO2002 de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| remuneracao | vrSalFx |  |  | Caso o funcionário utilize salário composto, retorna a soma que compõe o total do salário do histórico salarial.  Caso o parametro "Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas" esteja marcado, retorna o maior salário hora cadastrado conforme data do histórico salarial.  Caso contrário, retorna o salário do histórico salarial |
| remuneracao | undSalFixo |  |  | Se PFUNC.CODTIPO for igual a "O" ou "F" retorna "7 - Não se aplica", caso contrário será verificado o tipo de recebimento conforme a serguir:   Caso PFUNC.CODRECEBIMENTO seja "D - Diarista" retorna "2 - Por Dia";  Caso PFUNC.CODRECEBIMENTO seja "H - Horista" ou "P - Professor Horista" retorna "1 - Por Hora";  Caso PFUNC.CODRECEBIMENTO seja "M - Mensalista" ou "O - Outros" retorna "5 - Por Mês";  Caso PFUNC.CODRECEBIMENTO seja "Q - Quinzenalista" retorna "4 - Por Quinzena";  Caso PFUNC.CODRECEBIMENTO seja "S - Semanalista" retorna "3 - Por Semana";  Caso PFUNC.CODRECEBIMENTO seja "T - Tarefeiro" retorna "6 - Por Tarefa"; |
| remuneracao | dscSalVar |  |  | Recupera valor do campo PFUNC.DESCRICAOSALVARIAVEL |
| FGTS | dtOpcFGTS | PFUNC | DTOPCAOFGTS |  |
| infoDirigenteSindical | categOrig |  |  | Recupera o valor do campo PFUNC.CODCATEGORIAEMPRESAORIGEM |
| infoDirigenteSindical | tpInsc |  |  | Caso o campo PFUNC.CNPJEMPRESAORIGEM esteja preenchido com um CNPJ válido retorna 1.  Caso o campo PFUNC.CNPJEMPRESAORIGEM esteja preenchido com um CPF válido retorna 2 |
| infoDirigenteSindical | nrInsc |  |  | Recupera o valor do campo PFUNC.CNPJEMPRESAORIGEM |
| infoDirigenteSindical | dtAdmOrig |  |  | Recupera o valor do campo PFUNC.DATAADMISSAOEMPRESAORIGEM |
| infoDirigenteSindical | matricOrig |  |  | Recupera o valor do campo PFUNC.MATRICULAEMPRESAORIGEM |
| infoDirigenteSindical | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGTRABDIRIGENTESINDICAL |
| infoDirigenteSindical | tpRegPrev | PFUNC | TIPOREGPREVDIRIGENTESINDICAL |  |
| infoTrabCedido | categOrig | PFUNC | CODCATEGORIATRABCEDIDO |  |
| infoTrabCedido | cnpjCednt | PFUNC | CNPJCEDENTE |  |
| infoTrabCedido | matricCed | PFUNC | MATRICULACEDENTE |  |
| infoTrabCedido | dtAdmCed | PFUNC | DATAADMISSAOCEDENTE |  |
| infoTrabCedido | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGIMETRABALHISTACEDIDO |
| infoTrabCedido | tpRegPrev | PFUNC | TIPOREGIMEPREVIDENCIARIOCEDIDO |  |
| infoMandElet | categOrig | PFUNC | CODCATEGORIAMANDATOELETIVO |  |
| infoMandElet | cnpjOrig | PFUNC | CNPJMANDATOELETIVO |  |
| infoMandElet | matricOrig | PFUNC | MATRICULAMANDATOELETIVO |  |
| infoMandElet | dtExercOrig | PFUNC | DTEXERCICIOMANDATOELETIVO |  |
| infoMandElet | indRemunCargo |  |  | Recupera o valor do campo PFUNC.INDICATIVOREMUNERACAOCARGO |
| infoMandElet | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGTRABMANDATOELETIVO |
| infoMandElet | tpRegPrev | PFUNC | TIPOREGPREVMANDATOELETIVO |  |
| infoEstagiario | natEstagio | PFUNC | NATUREZAESTAGIO |  |
| infoEstagiario | nivEstagio | PFUNC | CODNIVELESTAGIO |  |
| infoEstagiario | areaAtuacao | PFUNC | AREAATUACAOESTAGIO |  |
| infoEstagiario | nrApol | PFUNC | NUMEROAPOLICEESTAGIO |  |
| infoEstagiario | dtPrevTerm | PFUNC | DTPREVTERMINOESTAGIO |  |
| instEnsino | cnpjInstEnsino | VENTIDADES | CGCCPF |  |
| instEnsino | nmRazao | VENTIDADES | RAZAOSOCIAL |  |
| instEnsino | dscLograd | VENTIDADES | LOGRADOURO |  |
| instEnsino | nrLograd | VENTIDADES | NUMERO |  |
| instEnsino | bairro | VENTIDADES | BAIRRO |  |
| instEnsino | cep | VENTIDADES | CEP |  |
| instEnsino | codMunic |  |  | Código recuperado através dos campos VENTIDADES.ESTADO e VENTIDADES.LOCALIDADE |
| instEnsino | uf | VENTIDADES | ESTADO |  |
| ageIntegracao | cnpjAgntInteg | VENTIDADES | CGCCPF |  |
| supervisorEstagio | cpfSupervisor | PFUNC | CPFCOORDENADORESTAGIO |  |
| afastamento | dtIniAfast | PFHSTAFT | DTINICIO |  |
| afastamento | codMotAfast |  |  | Caso o afastamento for de férias, retorna "15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso";  Caso exista informação no parametrizador do eSocial no De/Para de afastamento retorna o valor do campo Cód. Motivo eSocial;  Caso PFHSTAFT.TIPO seja "T - Af.Ac.Trabalho" ou PFHSTAFT.TIPO seja "O - Doença Ocupacional"retorna "01 - Acidente/Doença do trabalho";  Caso PFHSTAFT.TIPO seja "P - Af.Previdência" retorna "03 - Acidente/Doença não relacionada ao trabalho";  Caso PFHSTAFT.TIPO seja "Apos. Incapac. Permanente" retorna "06 - Apos. por Incapacidade Permanente";  Caso PFHSTAFT.TIPO seja "R - Licença Remun." retorna "16 - Licença remunerada - Liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho";  Caso PFHSTAFT.TIPO seja "W - Licença Mater. Compl. 180 dias" retorna "18 - Licença Maternidade - a partir de 120 dias até 180 dias";  Caso PFHSTAFT.TIPO seja "L - Licença s/venc" retorna "21 - Licença não remunerada ou Sem Vencimento";  Caso PFHSTAFT.TIPO seja "S ou N - Mandato Sindical" retorna "24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical";  Caso PFHSTAFT.TIPO seja "C - Contrato de Trabalho Suspenso" retorna "27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT";  Caso PFHSTAFT.TIPO seja "M - Serv.Militar" retorna "29 - Serviço Militar - Afastamento temporário"  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTADOCAO seja VERDADEIRO retorna "20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTABORTONAOCRIME seja VERDADEIRO retorna "19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTANTECIPACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTPRORROGACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 120 retorna "17 - Licença Maternidade - 120 dias";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 15 e seja falso os parâmetros MOTIVOAFASTANTECIPACAO e MOTIVOAFASTPRORROGACAO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "K-Cessão / Requisição " retorna "14 - Cessão / Requisição ";  Caso PFHSTAFT.TIPO seja "Q - Prisão / Cárcere" retorna "11 - Cárcere". |
| termino | dtTerm | PFUNC | DTDESLIGAMENTO |  |

1Leiaute 1.2

Mapeamento dos campos para o leiaute 1.2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro eSocial** | **Campo eSocial** | **Tabela RM** | **Coluna RM** | **Informações do cálculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| trabalhador | cpfTrab |  |  |  |
| trabalhador | nmTrab | PFUNC | NOME |  |
| trabalhador | sexo | PPESSOA | SEXO |  |
| trabalhador | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| trabalhador | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| trabalhador | grauInstr |  |  | Caso PPESSOA.GRAUINSTRUCAO seja "1" retorna "1 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou";  Caso PPESSOA.GRAUINSTRUCAO seja "2" retorna "2 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular";  Caso PPESSOA.GRAUINSTRUCAO seja "3" retorna "3 - 5º ano completo do Ensino Fundamental";  Caso PPESSOA.GRAUINSTRUCAO seja "4" retorna "4 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)";  Caso PPESSOA.GRAUINSTRUCAO seja "5" retorna "5 - Ensino Fundamental Completo";  Caso PPESSOA.GRAUINSTRUCAO seja "6" retorna "6 - Ensino Médio incompleto";  Caso PPESSOA.GRAUINSTRUCAO seja "7" retorna "7 - Ensino Médio completo";  Caso PPESSOA.GRAUINSTRUCAO seja "8" retorna "8 - Educação Superior incompleta";  Caso PPESSOA.GRAUINSTRUCAO seja "9", "A" ou "C" retorna "9 - Educação Superior completa";  Caso PPESSOA.GRAUINSTRUCAO seja "B" retorna "10 - Pós-graduação completa";  Caso PPESSOA.GRAUINSTRUCAO seja "D" ou "E" retorna "11 - Mestrado completo";  Caso PPESSOA.GRAUINSTRUCAO seja "F", "G" ou "H" retorna "12 - Doutorado completo" |
| trabalhador | nmSoc | PPESSOA | NOMESOCIAL |  |
| nascimento | dtNascto | PPESSOA | DTNASCIMENTO |  |
| nascimento | paisNascto |  |  | Codificação de País obtida através do campo PPESSOA.ESTADONATAL |
| nascimento | paisNac |  |  | Código recuperado através do campo PPESSOA.NACIONALIDADE |
| brasil | tpLograd |  |  | Código recuperado através do campo PPESSOA.CODTIPORUA |
| brasil | dscLograd | PPESSOA | RUA |  |
| brasil | nrLograd | PPESSOA | NUMERO |  |
| brasil | complemento | PPESSOA | COMPLEMENTO |  |
| brasil | bairro | PPESSOA | BAIRRO |  |
| brasil | cep | PPESSOA | CEP |  |
| brasil | codMunic |  |  | Código recuperado através dos campos PPESSOA.ESTADO e PPESSOA.CODMUNICIPIO |
| brasil | uf | PPESSOA | ESTADO |  |
| exterior | paisResid |  |  | Código recuperado através do campo PPESSOA.IDPAIS |
| exterior | dscLograd | PPESSOA | RUA |  |
| exterior | nrLograd | PPESSOA | NUMERO |  |
| exterior | complemento | PPESSOA | COMPLEMENTO |  |
| exterior | bairro | PPESSOA | BAIRRO |  |
| exterior | nmCid | PPESSOA | CIDADE |  |
| exterior | codPostal | PPESSOA | CEP |  |
| trabImig | tmpResid |  |  | Caso PPESSOA.TIPOPRAZORESIDENCIA seja VERDADEIRO retorna "1" - Prazo indeterminado. Caso contrário, retorna "2" - Prazo determinado |
| trabImig | condIng |  |  | Recupera o valor do campo PPESSOA.CODCLASSIFTRABESTRANG |
| infoDeficiencia | defFisica |  |  | Caso PPESSOA.DEFICIENTEFISICO ou PPESSOA.DEFICIENTEFALA seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defVisual |  |  | Caso PPESSOA.DEFICIENTEVISUAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defAuditiva |  |  | Caso PPESSOA.DEFICIENTEAUDITIVO seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defMental |  |  | Caso PPESSOA.DEFICIENTEMENTAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | defIntelectual |  |  | Caso PPESSOA.DEFICIENTEINTELECTUAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | reabReadap |  |  | Caso PPESSOA.BRPDH seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| infoDeficiencia | observacao |  |  | Composto pelos campos PPESSOA.RECURSOREALIZACAOTRAB e PPESSOA.RECURSOACESSIBILIDADE |
| dependente | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| dependente | nmDep | PFDEPEND | NOME |  |
| dependente | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| dependente | cpfDep | PFDEPEND | CPF |  |
| dependente | depIRRF |  |  | Caso PFDEPEND.INCIRRF seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| dependente | depSF |  |  | Caso PFDEPEND.INCSALFAM seja VERDADEIRO  retorna "S";  Caso o dependente seja MENOR de 7 anos e PFDEPEND.CARTAOVACINA seja VERDADEIRO retorna "S";  Caso o dependente seja MAIOR de 7 anos e PFDEPEND.FREQESCOLAR seja VERDADEIRO retorna "S";  Caso o dependente seja MENOR de 1 ano e o parâmetro "Paga Salário Família Menor de 1 Ano Sem Cartão Vacina" seja VERDADEIRO retorna "S";  Para os demais casos, retorna "N". |
| dependente | incTrab |  |  | Se o grau de parentesco for '3 - Filho(a) Inválido' ou 'N - Irmã(o) Inválido' o valor será 'S', caso contrário será 'N'. |
| dependente | descrDep | PFDEPEND | DESCRICAODEPENDENCIA |  |
| contato | fonePrinc | PPESSOA | TELEFONE1 |  |
| contato | emailPrinc | PPESSOA | EMAIL |  |
| infoTSVInicio | cadIni |  |  | Caso PESOCIALEVENTOS.TPOPERACAO seja "0 - Carga Inicial" retorna "S", caso contrário retorna "N" |
| infoTSVInicio | matricula | PFUNC | MATRICULAESOCIAL |  |
| infoTSVInicio | codCateg |  |  | Caso seja autônomo do Gestão Financeira retorna o campo 'CODCATEGORIAESOCIAL' da tabela 'FCFO';    Caso seja autônomo Externo retorna o campo 'CATEGORIAESOCIAL' da tabela 'PPAGTOAUTONOMOEXT'. Não tendo informação ou sendo zero será o de/para  do campo 'CATAUTONOMO' da tabela  'PPAGTOAUTONOMOEX' que armazena a categoria do SEFIP e faz o de/Para para categoria do eSocial.;    O sistema irá buscar o código da categoria do campo PFMULTVINCULOSEXTERNO.CODCATEGORIA se existir registro na tabela PFMULTVINCULOSEXTERNO, caso contrário, buscará do campo PFUNC.CODCATEGORIAESOCIAL. |
| infoTSVInicio | dtInicio | PFUNC | DATAADMISSAO |  |
| infoTSVInicio | nrProcTrab | PFUNC | NROPROCESSOTRABADMISSAO |  |
| infoTSVInicio | natAtividade |  |  | Caso PFUNC.ESOCIALNATATIVIDADE seja "2" retorna "2 - Trabalho Rural" caso contrário, retorna "1 - Trabalho Urbano" |
| cargoFuncao | nmCargo |  |  | Recupera o valor do campo PFUNCAO.NOME. |
| cargoFuncao | CBOCargo |  |  | Recupera o valor do campo PFUNCAO.CBO2002. |
| cargoFuncao | nmFuncao |  |  | Recupera o valor do campo PFUNCAO.NOME de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| cargoFuncao | CBOFuncao |  |  | Recupera o valor do campo PFUNCAO.CBO2002 de acordo com o valor de PFUNC.CODFUNCAOCONF. |
| remuneracao | vrSalFx |  |  | Caso o funcionário utilize salário composto, retorna a soma que compõe o total do salário do histórico salarial.  Caso o parametro "Considerar maior valor de salário-hora na tag vrSalFx para professores/horistas" esteja marcado, retorna o maior salário hora cadastrado conforme data do histórico salarial.  Caso contrário, retorna o salário do histórico salarial |
| remuneracao | undSalFixo |  |  | Se PFUNC.CODTIPO for igual a "O" ou "F" retorna "7 - Não se aplica", caso contrário será verificado o tipo de recebimento conforme a serguir:   Caso PFUNC.CODRECEBIMENTO seja "D - Diarista" retorna "2 - Por Dia";  Caso PFUNC.CODRECEBIMENTO seja "H - Horista" ou "P - Professor Horista" retorna "1 - Por Hora";  Caso PFUNC.CODRECEBIMENTO seja "M - Mensalista" ou "O - Outros" retorna "5 - Por Mês";  Caso PFUNC.CODRECEBIMENTO seja "Q - Quinzenalista" retorna "4 - Por Quinzena";  Caso PFUNC.CODRECEBIMENTO seja "S - Semanalista" retorna "3 - Por Semana";  Caso PFUNC.CODRECEBIMENTO seja "T - Tarefeiro" retorna "6 - Por Tarefa"; |
| remuneracao | dscSalVar |  |  | Recupera valor do campo PFUNC.DESCRICAOSALVARIAVEL |
| FGTS | dtOpcFGTS | PFUNC | DTOPCAOFGTS |  |
| infoDirigenteSindical | categOrig |  |  | Recupera o valor do campo PFUNC.CODCATEGORIAEMPRESAORIGEM |
| infoDirigenteSindical | tpInsc |  |  | Caso o campo PFUNC.CNPJEMPRESAORIGEM esteja preenchido com um CNPJ válido retorna 1.  Caso o campo PFUNC.CNPJEMPRESAORIGEM esteja preenchido com um CPF válido retorna 2 |
| infoDirigenteSindical | nrInsc |  |  | Recupera o valor do campo PFUNC.CNPJEMPRESAORIGEM |
| infoDirigenteSindical | dtAdmOrig |  |  | Recupera o valor do campo PFUNC.DATAADMISSAOEMPRESAORIGEM |
| infoDirigenteSindical | matricOrig |  |  | Recupera o valor do campo PFUNC.MATRICULAEMPRESAORIGEM |
| infoDirigenteSindical | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGTRABDIRIGENTESINDICAL |
| infoDirigenteSindical | tpRegPrev | PFUNC | TIPOREGPREVDIRIGENTESINDICAL |  |
| infoTrabCedido | categOrig | PFUNC | CODCATEGORIATRABCEDIDO |  |
| infoTrabCedido | cnpjCednt | PFUNC | CNPJCEDENTE |  |
| infoTrabCedido | matricCed | PFUNC | MATRICULACEDENTE |  |
| infoTrabCedido | dtAdmCed | PFUNC | DATAADMISSAOCEDENTE |  |
| infoTrabCedido | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGIMETRABALHISTACEDIDO |
| infoTrabCedido | tpRegPrev | PFUNC | TIPOREGIMEPREVIDENCIARIOCEDIDO |  |
| infoMandElet | categOrig |  |  |  |
| infoMandElet | cnpjOrig |  |  |  |
| infoMandElet | matricOrig |  |  |  |
| infoMandElet | dtExercOrig |  |  |  |
| infoMandElet | indRemunCargo |  |  | Recupera o valor do campo PFUNC.INDICATIVOREMUNERACAOCARGO |
| infoMandElet | tpRegTrab |  |  | Recupera o valor do campo PFUNC.TIPOREGTRABMANDATOELETIVO |
| infoMandElet | tpRegPrev |  |  |  |
| infoEstagiario | natEstagio | PFUNC | NATUREZAESTAGIO |  |
| infoEstagiario | nivEstagio | PFUNC | CODNIVELESTAGIO |  |
| infoEstagiario | areaAtuacao | PFUNC | AREAATUACAOESTAGIO |  |
| infoEstagiario | nrApol | PFUNC | NUMEROAPOLICEESTAGIO |  |
| infoEstagiario | dtPrevTerm | PFUNC | DTPREVTERMINOESTAGIO |  |
| instEnsino | cnpjInstEnsino |  |  |  |
| instEnsino | nmRazao | VENTIDADES | RAZAOSOCIAL |  |
| instEnsino | dscLograd | VENTIDADES | LOGRADOURO |  |
| instEnsino | nrLograd | VENTIDADES | NUMERO |  |
| instEnsino | bairro | VENTIDADES | BAIRRO |  |
| instEnsino | cep | VENTIDADES | CEP |  |
| instEnsino | codMunic |  |  | Código recuperado através dos campos VENTIDADES.ESTADO e VENTIDADES.LOCALIDADE |
| instEnsino | uf | VENTIDADES | ESTADO |  |
| ageIntegracao | cnpjAgntInteg | VENTIDADES | CGCCPF |  |
| supervisorEstagio | cpfSupervisor | PFUNC | CPFCOORDENADORESTAGIO |  |
| localTrabGeral | tpInsc |  |  | Caso o parâmetro "Considera CNO nas tags localTrabGeral do S-1005 para funcionários alocados em um único tomador obra própria"  esteja marcado e o funcionário possua somente um tomador de serviço que seja obra própria retorna "4 - CNO";   Caso PSECAO.CAEPF esteja preenchido retorna "3 - CAEPF (Cadastro de Atividade Econômica de Pessoa Física)";  Caso PSECAO.CGC esteja preenchido retorna "1 - CNPJ". |
| localTrabGeral | nrInsc |  |  | Caso tpInsc seja 1: retorna valor do campo PSECAO.CGC;  Caso tpInsc seja 3: retorna valor do campo PSECAO.CAEPF;  Caso tpInsc seja 4: retorna valor do campo FCFOCEI.CEI. |
| afastamento | dtIniAfast | PFHSTAFT | DTINICIO |  |
| afastamento | codMotAfast |  |  | Caso o afastamento for de férias, retorna "15 - Gozo de férias ou recesso - Afastamento temporário para o gozo de férias ou recesso";  Caso exista informação no parametrizador do eSocial no De/Para de afastamento retorna o valor do campo Cód. Motivo eSocial;  Caso PFHSTAFT.TIPO seja "T - Af.Ac.Trabalho" ou PFHSTAFT.TIPO seja "O - Doença Ocupacional"retorna "01 - Acidente/Doença do trabalho";  Caso PFHSTAFT.TIPO seja "P - Af.Previdência" retorna "03 - Acidente/Doença não relacionada ao trabalho";  Caso PFHSTAFT.TIPO seja "Apos. Incapac. Permanente" retorna "06 - Apos. por Incapacidade Permanente";  Caso PFHSTAFT.TIPO seja "R - Licença Remun." retorna "16 - Licença remunerada - Liberalidade da empresa ou Acordo/Convenção Coletiva de Trabalho";  Caso PFHSTAFT.TIPO seja "W - Licença Mater. Compl. 180 dias" retorna "18 - Licença Maternidade - a partir de 120 dias até 180 dias";  Caso PFHSTAFT.TIPO seja "L - Licença s/venc" retorna "21 - Licença não remunerada ou Sem Vencimento";  Caso PFHSTAFT.TIPO seja "S ou N - Mandato Sindical" retorna "24 - Mandato Sindical - Afastamento temporário para exercício de mandato sindical";  Caso PFHSTAFT.TIPO seja "C - Contrato de Trabalho Suspenso" retorna "27 - Qualificação - Afastamento por suspensão do contrato de acordo com o art 476-A da CLT";  Caso PFHSTAFT.TIPO seja "M - Serv.Militar" retorna "29 - Serviço Militar - Afastamento temporário"  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTADOCAO seja VERDADEIRO retorna "20 - Licença Maternidade - Afastamento temporário por motivo de licença-maternidade decorrente de adoção ou guarda judicial de criança";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTABORTONAOCRIME seja VERDADEIRO retorna "19 - Licença Maternidade - Afastamento temporário por motivo de aborto não criminoso";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTANTECIPACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e parâmetro MOTIVOAFASTPRORROGACAO  seja VERDADEIRO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 120 retorna "17 - Licença Maternidade - 120 dias";  Caso PFHSTAFT.TIPO seja "E - Licença Mater." e quantidade de dias de afastamento igual a 15 e seja falso os parâmetros MOTIVOAFASTANTECIPACAO e MOTIVOAFASTPRORROGACAO retorna "35 - Licença Maternidade - Antecipação e/ou prorrogação mediante atestado médico";  Caso PFHSTAFT.TIPO seja "K-Cessão / Requisição " retorna "14 - Cessão / Requisição ";  Caso PFHSTAFT.TIPO seja "Q - Prisão / Cárcere" retorna "11 - Cárcere". |
| termino | dtTerm | PFUNC | DTDESLIGAMENTO |  |
