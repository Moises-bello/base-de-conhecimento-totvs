---
content_hash: 1bbeb0f4a67cbafdd8a81865d6f2abf0d81349f245be4122c27082a38e50bd8e
fetched_at: '2026-06-29T00:11:10.049270+00:00'
page_id: '641155747'
product: rm
source: tdn-rm
title: Evento S-2405
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2405
version: 5
---

Leiautes1Leiaute S-1.0

Mapeamento dos campos para o leiaute S-1.0

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
| ideBenef | cpfTrab |  |  |  |
| alteracao | dtAlteracao | PFUNC | DATAADMISSAO |  |
| beneficiario | nmBenefic | PFUNC | NOME |  |
| beneficiario | sexo | PPESSOA | SEXO |  |
| beneficiario | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| beneficiario | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| beneficiario | incFisMen |  |  |  |
| brasil | tpLograd |  |  | Código recuperado através do campo PPESSOA.CODTIPORUA |
| brasil | dscLograd | PPESSOA | RUA |  |
| brasil | nrLograd | PPESSOA | NUMERO |  |
| brasil | complemento | PPESSOA | COMPLEMENTO |  |
| brasil | bairro | PPESSOA | BAIRRO |  |
| brasil | cep | PPESSOA | CEP |  |
| brasil | codMunic |  |  | Código recuperado através dos campos PPESSOA.ESTADO e PPESSOA.CODMUNICIPIO |
| brasil | uf | PPESSOA | ESTADO |  |
| dependente | tpDep |  |  | É recuperado a idade do dependente a partir do campo PFDEPEND.DTNASCIMENTO;  Caso PFDEPEND.GRAUPARENTESCO seja "5 - Conjuge" retorna "1 - Cônjuge.";  Caso PFDEPEND.GRAUPARENTESCO seja "C - Companheiro" retorna "2 - Companheiro(a) com o(a) qual tenha filho ou viva há mais de 5 (cinco) anos ou possua Declaração de União Estável.";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" retorna "3 - Filho(a) ou enteado(a).";  Caso PFDEPEND.GRAUPARENTESCO seja "1 - FilhoValido" ou "D - Enteado" ou "3 - FilhoValido" e PFDEPEND.UNIVERSITARIO seja VERDADEIRO e IDADE menor ou igual a 24 retorna "4 - Filho(a) ou enteado(a) universitário(a) ou cursando escola técnica de 2º grau, até 24 (vinte e quatro) anos.";  Caso PFDEPEND.GRAUPARENTESCO seja "I - IrmaoValido" ou "N = IrmaoInvalido" ou "T - Neto" retorna "6 - Irmão(ã), neto(a) ou bisneto(a) sem arrimo dos pais, do(a) qual detenha a guarda judicial.";  Caso PFDEPEND.GRAUPARENTESCO seja "6 - Pai", "7 - Mae" ou "A - Avo" retorna "9 - Pais, avós e bisavós.";  Caso PFDEPEND.GRAUPARENTESCO seja "M - Menor Pobre" retorna "10 - Menor pobre do qual detenha a guarda judicial."  Caso PFDEPEND.GRAUPARENTESCO seja "B - Incapaz" retorna "11 - A pessoa absolutamente incapaz, da qual seja tutor ou curador."  Caso PFDEPEND.GRAUPARENTESCO seja "G - ExConjuge" retorna "12 - Ex-cônjuge."  Caso PFDEPEND.GRAUPARENTESCO seja diferente dos códigos acima, retorna "99 Agregado/Outros". |
| dependente | nmDep | PFDEPEND | NOME |  |
| dependente | dtNascto | PFDEPEND | DTNASCIMENTO |  |
| dependente | cpfDep | PFDEPEND | CPF |  |
| dependente | sexoDep | PFDEPEND | SEXO |  |
| dependente | depIRRF |  |  | Caso PFDEPEND.INCIRRF seja VERDADEIRO retorna "S" caso contrário, retorna "N" |
| dependente | incFisMen |  |  |  |

1Leiaute S-1.2

Mapeamento dos campos para o leiaute S-1.2

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Registro\_eSocial** | **Campo\_eSocial** | **Tabela\_RM** | **Coluna\_RM** | **Informações\_do\_calculo** |
| ideEvento | indRetif |  |  | Conforme manual |
| ideEvento | nrRecibo |  | PROTOCOLO |  |
| ideEvento | tpAmb |  |  | Campo do parametrizador Etapa 1 - eSocial: Configurações Gerais (ESOCIALTPAMBIENTE) |
| ideEvento | procEmi |  |  | Valor válido 1 (Valor Fixo) |
| ideEvento | verProc |  |  | Versão do RM |
| ideEmpregador | tpInsc |  |  | 21 ou 22 pessoa física, demais, pessoa jurídica |
| ideEmpregador | nrInsc | GCOLIGADA | CGC |  |
| ideBenef | cpfTrab |  |  |  |
| alteracao | dtAlteracao | DATAEVENTO |  |  |
| dadosBenef | nmBenefic | PFUNC | NOME |  |
| dadosBenef | sexo | PPESSOA | SEXO |  |
| dadosBenef | racaCor |  |  | Caso PPESSOA.CORRACA seja "0" retorna "5 - Indigena";  Caso PPESSOA.CORRACA seja "2" retorna "1 - Branca";  Caso PPESSOA.CORRACA seja "4" retorna "2 - Negra";  Caso PPESSOA.CORRACA seja "6" retorna "4 - Amarela";  Caso PPESSOA.CORRACA seja "8" retorna "3 - Parda";  Outro caso retorna "6 - Não Informado" |
| dadosBenef | estCiv |  |  | Caso PPESSOA.ESTADOCIVIL seja "S" retorna 1 - Solteiro";  Caso PPESSOA.ESTADOCIVIL seja "C" retorna 2 - Casado";  Caso PPESSOA.ESTADOCIVIL seja "D" ou "I" retorna 3 - Divorciado";  Caso PPESSOA.ESTADOCIVIL seja "P" retorna 4 - Separado";  Caso PPESSOA.ESTADOCIVIL seja "V" retorna 5 - Viúvo";  Caso PPESSOA.ESTADOCIVIL seja "E" ou "O" verifica o valor informado no de-para no parametrizador;  Demais casos retorna vazio |
| dadosBenef | incFisMen |  |  |  |
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
