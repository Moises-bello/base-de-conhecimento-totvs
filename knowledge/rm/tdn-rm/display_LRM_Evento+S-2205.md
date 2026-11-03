---
content_hash: bb110bd51d99063f0652143af132327a17aa2c9722f6d9e30a58f33be7874359
fetched_at: '2026-06-29T00:08:56.189176+00:00'
page_id: '351376270'
product: rm
source: tdn-rm
title: Evento S-2205
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2205
version: 9
---

Leiautestrue2Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

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
| ideTrabalhador | cpfTrab |  |  |  |
| alteracao | dtAlteracao |  | DATAEVENTO | Se o campo alterado possuir histórico busca a data de mudança do histórico, caso contrário é gerado conforme data atual |
| dadosTrabalhador | nmTrab | PFUNC | NOME |  |
| dadosTrabalhador | sexo | PPESSOA | SEXO |  |
| dadosTrabalhador | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| dadosTrabalhador | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| dadosTrabalhador | grauInstr |  |  | Caso PPESSOA.GRAUINSTRUCAO seja "1" retorna "1 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou";  Caso PPESSOA.GRAUINSTRUCAO seja "2" retorna "2 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular";  Caso PPESSOA.GRAUINSTRUCAO seja "3" retorna "3 - 5º ano completo do Ensino Fundamental";  Caso PPESSOA.GRAUINSTRUCAO seja "4" retorna "4 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)";  Caso PPESSOA.GRAUINSTRUCAO seja "5" retorna "5 - Ensino Fundamental Completo";  Caso PPESSOA.GRAUINSTRUCAO seja "6" retorna "6 - Ensino Médio incompleto";  Caso PPESSOA.GRAUINSTRUCAO seja "7" retorna "7 - Ensino Médio completo";  Caso PPESSOA.GRAUINSTRUCAO seja "8" retorna "8 - Educação Superior incompleta";  Caso PPESSOA.GRAUINSTRUCAO seja "9", "A" ou "C" retorna "9 - Educação Superior completa";  Caso PPESSOA.GRAUINSTRUCAO seja "B" retorna "10 - Pós-graduação completa";  Caso PPESSOA.GRAUINSTRUCAO seja "D" ou "E" retorna "11 - Mestrado completo";  Caso PPESSOA.GRAUINSTRUCAO seja "F", "G" ou "H" retorna "12 - Doutorado completo" |
| dadosTrabalhador | nmSoc | PPESSOA | NOMESOCIAL |  |
| dadosTrabalhador | paisNac |  |  | Código recuperado através do campo PPESSOA.NACIONALIDADE |
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
| infoDeficiencia | infoCota | PFUNC | COTAPCD |  |
| infoDeficiencia | observacao |  |  | Composto pelos campos PPESSOA.RECURSOREALIZACAOTRAB e PPESSOA.RECURSOACESSIBILIDADE |
| dependente | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| dependente | nmDep | PFDEPEND | NOME |  |
| dependente | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| dependente | cpfDep | PFDEPEND | CPF |  |
| dependente | sexoDep | PFDEPEND | SEXO |  |
| dependente | depIRRF |  |  | Caso PFDEPEND.INCIRRF seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| dependente | depSF |  |  | Caso PFDEPEND.INCSALFAM seja VERDADEIRO  retorna "S";  Caso o dependente seja MENOR de 7 anos e PFDEPEND.CARTAOVACINA seja VERDADEIRO retorna "S";  Caso o dependente seja MAIOR de 7 anos e PFDEPEND.FREQESCOLAR seja VERDADEIRO retorna "S";  Caso o dependente seja MENOR de 1 ano e o parâmetro "Paga Salário Família Menor de 1 Ano Sem Cartão Vacina" seja VERDADEIRO retorna "S";  Para os demais casos, retorna "N". |
| dependente | incTrab |  |  | Se o grau de parentesco for '3 - Filho(a) Inválido' ou 'N - Irmã(o) Inválido' o valor será 'S', caso contrário será 'N'. |
| contato | fonePrinc | PPESSOA | TELEFONE1 |  |
| contato | emailPrinc | PPESSOA | EMAIL |  |

true2Leiaute S-1.2

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
| ideTrabalhador | cpfTrab |  |  |  |
| alteracao | dtAlteracao | DATAEVENTO |  | Se o campo alterado possuir histórico busca a data de mudança do histórico, caso contrário é gerado conforme data atual |
| dadosTrabalhador | nmTrab | PFUNC | NOME |  |
| dadosTrabalhador | sexo | PPESSOA | SEXO |  |
| dadosTrabalhador | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| dadosTrabalhador | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| dadosTrabalhador | grauInstr |  |  | Caso PPESSOA.GRAUINSTRUCAO seja "1" retorna "1 - Analfabeto, inclusive o que, embora tenha recebido instrução, não se alfabetizou";  Caso PPESSOA.GRAUINSTRUCAO seja "2" retorna "2 - Até o 5º ano incompleto do Ensino Fundamental (antiga 4ª série) ou que se tenha alfabetizado sem ter frequentado escola regular";  Caso PPESSOA.GRAUINSTRUCAO seja "3" retorna "3 - 5º ano completo do Ensino Fundamental";  Caso PPESSOA.GRAUINSTRUCAO seja "4" retorna "4 - Do 6º ao 9º ano do Ensino Fundamental incompleto (antiga 5ª a 8ª série)";  Caso PPESSOA.GRAUINSTRUCAO seja "5" retorna "5 - Ensino Fundamental Completo";  Caso PPESSOA.GRAUINSTRUCAO seja "6" retorna "6 - Ensino Médio incompleto";  Caso PPESSOA.GRAUINSTRUCAO seja "7" retorna "7 - Ensino Médio completo";  Caso PPESSOA.GRAUINSTRUCAO seja "8" retorna "8 - Educação Superior incompleta";  Caso PPESSOA.GRAUINSTRUCAO seja "9", "A" ou "C" retorna "9 - Educação Superior completa";  Caso PPESSOA.GRAUINSTRUCAO seja "B" retorna "10 - Pós-graduação completa";  Caso PPESSOA.GRAUINSTRUCAO seja "D" ou "E" retorna "11 - Mestrado completo";  Caso PPESSOA.GRAUINSTRUCAO seja "F", "G" ou "H" retorna "12 - Doutorado completo" |
| dadosTrabalhador | nmSoc | PPESSOA | NOMESOCIAL |  |
| dadosTrabalhador | paisNac |  |  | Código recuperado através do campo PPESSOA.NACIONALIDADE |
| brasil | tpLograd |  |  | Código recuperado através do campo PPESSOA.CODTIPORUA |
| brasil | dscLograd | PPESSOA | RUA |  |
| brasil | nrLograd | PPESSOA | NUMERO |  |
| brasil | complemento | PPESSOA | COMPLEMENTO |  |
| brasil | bairro | PPESSOA | BAIRRO |  |
| brasil | cep | PPESSOA | CEP |  |
| brasil | codMunic |  | Código recuperado através dos campos PPESSOA.ESTADO e PPESSOA.CODMUNICIPIO |  |
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
| infoDeficiencia | defAuditiva |  | Caso PPESSOA.DEFICIENTEAUDITIVO seja VERDADEIRO retorna "S" caso contrário, retorna "N" |  |
| infoDeficiencia | defMental |  | Caso PPESSOA.DEFICIENTEMENTAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |  |
| infoDeficiencia | defIntelectual |  | Caso PPESSOA.DEFICIENTEINTELECTUAL seja VERDADEIRO retorna "S" caso contrário, retorna "N" |  |
| infoDeficiencia | reabReadap |  | Caso PPESSOA.BRPDH seja VERDADEIRO retorna "S" caso contrário, retorna "N" |  |
| infoDeficiencia | infoCota | PFUNC | COTAPCD |  |
| infoDeficiencia | observacao |  | Composto pelos campos PPESSOA.RECURSOREALIZACAOTRAB e PPESSOA.RECURSOACESSIBILIDADE |  |
| dependente | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| dependente | nmDep | PFDEPEND | NOME |  |
| dependente | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| dependente | cpfDep | PFDEPEND | CPF |  |
| dependente | sexoDep | PFDEPEND | SEXO |  |
| dependente | depIRRF |  |  | Caso PFDEPEND.INCIRRF seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| dependente | depSF |  |  | Caso PFDEPEND.INCSALFAM seja VERDADEIRO  retorna "S";  Caso o dependente seja MENOR de 7 anos e PFDEPEND.CARTAOVACINA seja VERDADEIRO retorna "S";  Caso o dependente seja MAIOR de 7 anos e PFDEPEND.FREQESCOLAR seja VERDADEIRO retorna "S";  Caso o dependente seja MENOR de 1 ano e o parâmetro "Paga Salário Família Menor de 1 Ano Sem Cartão Vacina" seja VERDADEIRO retorna "S";  Para os demais casos, retorna "N". |
| dependente | incTrab |  |  | Se o grau de parentesco for '3 - Filho(a) Inválido' ou 'N - Irmã(o) Inválido' o valor será 'S', caso contrário será 'N'. |
| dependente | descrDep | PFDEPEND | DESCRICAODEPENDENCIA |  |
| contato | fonePrinc | PPESSOA | TELEFONE1 |  |
| contato | emailPrinc | PPESSOA | EMAIL |  |
