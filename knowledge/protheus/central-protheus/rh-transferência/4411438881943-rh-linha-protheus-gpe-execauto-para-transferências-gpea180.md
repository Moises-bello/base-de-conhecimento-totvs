---
article_id: 4411438881943
category: RH - Transferência
content_hash: ee39a3421ec5497f0b8dfa5e9582cef6651fbf371ac16fa5724e78d0ab00e51d
fetched_at: '2026-06-28T22:43:23.337369+00:00'
product: protheus
section_id: 360010781974
source: central-protheus
title: RH - Linha Protheus - GPE - Execauto para Transferências - GPEA180
type: support-article
updated_at: '2025-07-11T17:59:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411438881943-RH-Linha-Protheus-GPE-Execauto-para-Transfer%C3%AAncias-GPEA180
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33408555563159) Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**Execauto para Transferências - GPEA180  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Essa rotina tem por objetivo realizar a **transferência** de um ou mais Funcionários.

**Sintaxe:**   
GPEA180( nOpcAuto, aAutoItens, dDataTransf , lAutomato )  
  
**Parâmetros:   
  
nOpcAuto -** Operação - 6 (Transferir)  
  
**aAutoItens -**Array com as informações dos funcionários a serem transferidos:

aAutoItens[x][1] - Filial Origem do funcionário

aAutoItens[x][2] - Matrícula Origem do funcionário

aAutoItens[x][3] - Array com os campos do funcionário cuja transferência será efetuada

aAutoItens[x][3][y][1] - Nome do campo que sofrerá transferência (SRA)

aAutoItens[x][3][y][2] - Novo conteúdo - Destino

Onde todos os conteúdos serão em formato String e:  
x = número de funcionários da filial logada a serem transferidos e,  
y = número de campos a serem transferidos de cada funcionário.

**dDataTransf -** Data da transferência (opcional)  
Formato: data  
Caso não seja passada por parâmetro, a data utilizada será a data base do sistema.

**lAutomato -** Valor lógico que deve ser enviado com valor **'.T.'** caso não seja desejada a exibição de nenhuma interação com o usuário .  
  
  
**Exemplo de ExecAuto da rotina de Transferência - GPEA180:**

```
#INCLUDE "PROTHEUS.CH"  
#INCLUDE "TBICONN.CH"  
  
/*  
Array com as informações dos funcionários a serem transferidos:  
aAutoItens[x][1] - Filial Origem do funcionário  
aAutoItens[x][2] - Matrícula Origem do funcionário  
aAutoItens[x][3] - Array com os campos do funcionário cuja transferência será efetuada  
aAutoItens[x][3][y][1] - Nome do campo que sofrerá transferência (SRA)  
aAutoItens[x][3][y][2] - Novo conteúdo - Destino  
  
Onde todos os conteúdos serão em formato String e:  
x = número de funcionários da filial logada a serem transferidos e,  
y = número de campos a serem transferidos de cada funcionário.  
  
dDataTransf  
Data da transferência (opcional)  
Formato: data  
  
Caso não seja passada por parâmetro, a data utilizada será a data base do sistema.  
lAutomato Valor lógico que deve ser enviado com valor '.T.' caso não seja desejada a exibição de nenhuma interação com o usuário.  
  
*/  
  
User Function TRANSF()  
Local aAutoItens := {}  
Local aCampos := {}  
Local aLogAuto := {}  
Local dDataTransf := CtoD("//")  
Private lMsErroAuto := .F.  
  
PREPARE ENVIRONMENT EMPRESA "01" FILIAL "M SP 01 " MODULO "GPE"  
  
ConOut(Repl("-",80))  
ConOut("Inicio: "+Time())  
ConOut(PadC("Rotina Automatica Transferencia de funcionarios - SRA",80))  
  
dDataTransf := StoD("20241015")  
aAdd( aCampos, { "RA_FILIAL", "D RJ 01 " } ) //Filial Destino  
aAdd( aCampos, { "RA_MAT" , "000077" } ) //Matrícula Destino  
aAdd( aCampos, { "RA_CC", "01" } ) //Centro de Custo Destino  
aAdd( aCampos, { "RA_PROCES", "00006" } ) //Processo Destino  
aAdd( aAutoItens, { "M SP 01 ", "000077", aCampos } ) //Filail e Matrícula origem + aCampos  
  
//chamada ExecAuto  
MSExecAuto( {|x,y,z,w| GPEA180(x,y,z,w)}, 6, aAutoItens, dDataTransf, .T. )  
  
If !lMsErroAuto  
ConOut("Transferencia efetuada!")  
Else  
If !IsBlind()  
aLogAuto:= MostraErro('Null')  
varinfo("aLogAuto",aLogAuto)  
Else  
MostraErro() //caso acionada via interface.  
EndIf  
ConOut("Erro na Transferencia!")  
EndIf  
  
ConOut("Fim : "+Time())  
ConOut(Repl("-",80))  
  
RESET ENVIRONMENT  
  
Return NIL
```

**Observações:**Os nomes dos campos a serem passados na terceira dimensão do array seguem o padrão dos campos da **SRA**: RA\_FILIAL, RA\_MAT,... ( **RA\_xxx** ), exceto o campo correspondente a grupo de empresas, cujo nome a ser passado será M\_EMPRESA.

Os períodos nos processos Origem e Destino devem estar correspondentes, e os lançamentos do funcionário a ser transferido devem estar de acordo, para não necessitar de informação adicional de transferência de processo.

Necessário inicializar o array aCampos a cada funcionário

**Saiba Mais**[Exemplo Rotina Automática (ExecAuto) - GPEA180](https://tdn.totvs.com/pages/viewpage.action?pageId=429197280)  
[Execução de rotinas via MILE - GPE](https://tdn.totvs.com/display/public/PROT/Mile+-+Rotinas+GPE)
