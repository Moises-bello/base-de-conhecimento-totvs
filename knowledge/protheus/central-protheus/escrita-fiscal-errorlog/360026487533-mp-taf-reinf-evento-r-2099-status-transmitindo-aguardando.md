---
article_id: 360026487533
category: Escrita Fiscal - Error.log
content_hash: 3f3de9c5455a0cdea4e4a2f08c30f6a1b0e25f3919d9c8cd2bdfdc34c70d4566
fetched_at: '2026-06-28T22:39:32.947086+00:00'
product: protheus
section_id: 1500001549782
source: central-protheus
title: 'MP - TAF - REINF - Evento R-2099 - Status Transmitindo Aguardando '
type: support-article
updated_at: '2021-04-28T15:43:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026487533-MP-TAF-REINF-Evento-R-2099-Status-Transmitindo-Aguardando
---

**Dúvida**Ao efetuar transmissão do evento R-2099 e em seguida o monitoramento é apresentado o status Transmitindo/Aguardando.  
  
 **Ambiente**  
Protheus – TAF – A partir da versão 12.1.17  
  
**Solução**  
Para solução da ocorrência acima, será necessário avaliar o console.log do TSS se esta sendo gravado os error.logs abaixo:

Erro Console.log do TSS.

Bin do TSS:  
\*\*\*  TOTVS S.A.  \*\*\*  
\*\*\*  [www.totvs.com.br](https://www.google.com/url?q=http://www.totvs.com.br&sa=D&source=hangouts&ust=1562844688518000&usg=AFQjCNGUsa-2F-t3LU_yM-ti565I_VLFPw)  \*\*\*  
\* TOTVS - Build 7.00.131227A - Apr 25 2018 - 09:59:48 NG  
\* Build: 32 bits  
\* RPO Format: 32 bits  
\* SVN Revision: 10774 - 18213 - 2000  
\* Build Version: 13.2.3.34  
  
**[ ERROR: PROCERROR] 0614 [Thread: 10104] [12/06/2019 11:21:27]**  
**[Error:**  
**THREAD ERROR ([10104], IPC\_CONT, THIS)   12/06/2019 11:21:27**  
**Cannot find method SPED500A:SETRECNO on TOFILLENTITY(TSSENTITYMANAGER.PRW) 13/03/2019 10:06:51 line : 345**  
  
[TOTVS build: 7.00.131227A-20180425 NG]  
Called from TOFILLENTITY(TSSENTITYMANAGER.PRW) 13/03/2019 10:06:51 line : 345  
Called from TSSENTITYMANAGER:FINDSENTITY(TSSENTITYMANAGER.PRW) 13/03/2019 10:06:51 line : 171  
Called from CONSLOTEREINF(TSSPROCREINF.PRW) 09/01/2019 17:59:12 line : 619  
Called from TSSREINFCONSULTA(TSSPROCREINF.PRW) 09/01/2019 17:59:12 line : 409  
Called from {|aRecProc|TSSREINFConsulta(aRecProc)}(TSSPROCCONTROL.PRW) 13/03/2019 10:06:51 line : 409  
Called from TSSPROCCONTROL:EXECUTE(TSSPROCCONTROL.PRW) 13/03/2019 10:06:51 line : 228  
Called from TSSREINFEMISSAO(TSSPROCREINF.PRW) 09/01/2019 17:59:12 line : 40  
Called from TSSPROCEXEC(TSSPROCCALL.PRW) 27/02/2019 16:14:33 line : 276  
Called from PREPAREIPCWAIT(TSSIPCWAIT.PRW) 09/01/2019 17:59:12 line : 103  
Called from STATICCALL(TSSIPCWAIT.PRW) 09/01/2019 17:59:12 line : 103  
------------------------------------------------------------------------------  
  
**[ ERROR: PROCERROR] 0614 [Thread: 10104] [12/06/2019 11:21:27]**  
**[Error:**  
**THREAD ERROR ([10104], IPC\_CONT, THIS)   12/06/2019 11:21:27**  
**Cannot find method SPED500A:GETRECNO on TSSENTITYMANAGER:UPDATE(TSSENTITYMANAGER.PRW) 13/03/2019 10:06:51 line : 101**  
  
**[TOTVS build: 7.00.131227A-20180425 NG]**  
**Called from TSSENTITYMANAGER:UPDATE(TSSENTITYMANAGER.PRW) 13/03/2019 10:06:51 line : 101**  

Caso seja apresentado, será necessário seguir os procedimentos abaixo:

1- Verificar o campo STATUS da tabela SPED500 se esta igual a 4 = Transmitindo/Aguardando, se sim, prosseguir para o procedimento 2º.

2- Aplicar atualização contida no link abaixo no repositório do TSS:

[https://suporte.totvs.com/portal/p/10098/download?e=752204](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D752204&sa=D&source=hangouts&ust=1562844688519000&usg=AFQjCNFY1c9AUXMZjrwHTPR6U1336fn-Iw)

3-Efetuar o monitoramento do evento R-2099 no TAF.
