---
content_hash: bc704ab2c3b0a6bdb43ef9565922ad6ca2af6db0020fa25203370cad1480792b
fetched_at: '2026-06-29T00:09:10.868687+00:00'
page_id: '403049584'
product: rm
source: tdn-rm
title: Evento S-2220
type: documentation
url: https://tdn.totvs.com/display/LRM/Evento+S-2220
version: 9
---

Leiautestrue1Leiaute S-1.1

Mapeamento dos campos para o leiaute S-1.1

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
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg | PFUNC | CODCATEGORIAESOCIAL |  |
| monit | tpExame |  |  | Caso VCONSULTASPRONT.TIPO seja 1 retorne 0.  Caso VCONSULTASPRONT.TIPO seja 2 o valor não será utilizado pelo esocial.  Caso VCONSULTASPRONT.TIPO seja 4 retorne 1. |
| exMedOcup | tpExameOcup |  |  | Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja A retorna 0.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja P retorna 1.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja R retorna 2.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja M retorna 3.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja N retorna 4.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja D retorna 9. |
| aso | dtAso | VCONSULTASPRONT | DATAASO |  |
| aso | resAso |  |  | Caso VCONSULTASPRONT.APTO retorne '1' OU '3' será considerado '1 - Apto'  Caso VCONSULTASPRONT.APTO retorne '2' será considerado '2 - Inapto'  Caso VCONSULTASPRONT.APTO retorne outro valor este NÃO será considerado |
| exame | dtExm | VEXAMESPRONT | DATAEXAME |  |
| exame | procRealizado | VEXAMESPRONT | CODPROCEDIMENTO |  |
| exame | obsProc | VEXAMESPRONT | OBSERVACAO |  |
| exame | ordExame |  |  | Caso VEXAMESPRONT.RESULTNORMAL seja igual a 0 retorne 1. Caso VEXAMESPRONT.RESULTNORMAL seja 1 retorne 2. |
| exame | indResult |  |  | Caso VCONSULTASPRONT.RESULTNORMAL seja 0 retorna 1  Caso VCONSULTASPRONT.RESULTNORMAL seja 0 e VCONSULTASPRONT.TIPOANORMALIDADE seja vazio retorna 2  Caso VCONSULTASPRONT.TIPOANORMALIDADE seja 0 retorna 3  Caso VCONSULTASPRONT.TIPOANORMALIDADE seja 1 retorna 4 |
| medico | nmMed | VPROFISSIONALSAUDE | NOMEPROFISSIONAL |  |
| medico | nrCRM | VPROFISSIONALSAUDE | NUMEROREGISTRO |  |
| medico | ufCRM | VPROFISSIONALSAUDE | CODUFREGISTRO |  |
| respMonit | cpfResp | PPESSOA | CPF |  |
| respMonit | nmResp | PPESSOA | NOME |  |
| respMonit | nrCRM | VRESPMONBIOLOGICA | REGCONSELHOCLASSE |  |
| respMonit | ufCRM | VRESPMONBIOLOGICA | UFREGCONSELHO |  |

true2Leiaute S-1.2

Mapeamento dos campos para o leiaute S-1.2

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
| ideVinculo | cpfTrab | PPESSOA | CPF |  |
| ideVinculo | matricula | PFUNC | MATRICULAESOCIAL |  |
| ideVinculo | codCateg | PFUNC | CODCATEGORIAESOCIAL |  |
| monit | tpExame |  |  | Caso VCONSULTASPRONT.TIPO seja 1 retorne 0.  Caso VCONSULTASPRONT.TIPO seja 2 o valor não será utilizado pelo esocial.  Caso VCONSULTASPRONT.TIPO seja 4 retorne 1. |
| exMedOcup | tpExameOcup |  |  | Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja A retorna 0.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja P retorna 1.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja R retorna 2.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja M retorna 3.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja N retorna 4.  Caso VCONSULTASPRONT.CODTIPOCONSULTAESOCIAL seja D retorna 9. |
| aso | dtAso | VCONSULTASPRONT | DATAASO |  |
| aso | resAso |  |  | Caso VCONSULTASPRONT.APTO retorne '1' OU '3' será considerado '1 - Apto'  Caso VCONSULTASPRONT.APTO retorne '2' será considerado '2 - Inapto'  Caso VCONSULTASPRONT.APTO retorne outro valor este NÃO será considerado |
| exame | dtExm | VEXAMESPRONT | DATAEXAME |  |
| exame | procRealizado | VEXAMESPRONT | CODPROCEDIMENTO |  |
| exame | obsProc | VEXAMESPRONT | OBSERVACAO |  |
| exame | ordExame |  |  | Caso VEXAMESPRONT.RESULTNORMAL seja igual a 0 retorne 1. Caso VEXAMESPRONT.RESULTNORMAL seja 1 retorne 2. |
| exame | indResult |  |  | Caso VCONSULTASPRONT.RESULTNORMAL seja 0 retorna 1  Caso VCONSULTASPRONT.RESULTNORMAL seja 0 e VCONSULTASPRONT.TIPOANORMALIDADE seja vazio retorna 2  Caso VCONSULTASPRONT.TIPOANORMALIDADE seja 0 retorna 3  Caso VCONSULTASPRONT.TIPOANORMALIDADE seja 1 retorna 4 |
| medico | nmMed | VPROFISSIONALSAUDE | NOMEPROFISSIONAL |  |
| medico | nrCRM | VPROFISSIONALSAUDE | NUMEROREGISTRO |  |
| medico | ufCRM | VPROFISSIONALSAUDE | CODUFREGISTRO |  |
| respMonit | cpfResp | PPESSOA | CPF |  |
| respMonit | nmResp | PPESSOA | NOME |  |
| respMonit | nrCRM | VRESPMONBIOLOGICA | REGCONSELHOCLASSE |  |
| respMonit | ufCRM | VRESPMONBIOLOGICA | UFREGCONSELHO |  |
