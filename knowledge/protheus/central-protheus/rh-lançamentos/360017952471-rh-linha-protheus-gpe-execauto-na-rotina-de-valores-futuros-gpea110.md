---
article_id: 360017952471
category: RH - Lançamentos
content_hash: 33faa2587cdd1b7d3cbf7c7c6a09883338b5a24e9d618ea119cb1b6ee4969ba2
fetched_at: '2026-06-28T22:43:31.273532+00:00'
product: protheus
section_id: 360010781734
source: central-protheus
title: RH - Linha Protheus - GPE - ExecAuto na rotina de Valores Futuros GPEA110
type: support-article
updated_at: '2025-07-24T17:14:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017952471-RH-Linha-Protheus-GPE-ExecAuto-na-rotina-de-Valores-Futuros-GPEA110
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26164257394711)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Rotina Automática na rotina de Valores Futuros.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**  
A rotina automática (***ExecAuto***) na rotina de cadastro de **valores futuros** (**GPEA110**) torna possível realizar **inclusão, alteração** e **exclusão** de informações.  
  
**1.** Na chamada da Função **GPEA110** devem ser passados os **parâmetros.**  
***nOpcAuto*** - Indica a operação que será realizada, 3 - **Inclusão**, 4 - **Alteração**; 5 - **Exclusão**  
***aCab*** - *Array* com as informações para posicionar no funcionário  
***aItens*** - *Array* com os lançamentos  
  
**2.**Exemplo de chamada da rotina automática.#*Include* 'Protheus.ch'  
  
User Function GP110\_Exec()  
   Local aCab      := {}  
   Local aItem     := {}  
   Local aItens    := {}  
   Local aLog      := {}  
   Local lOk       := .T.  
  
   Private lMsErroAuto := .F.  
  
        Aadd(aCab, {"RA\_FILIAL" , "D MG 01 ",NIL})  
        Aadd(aCab, {"RA\_MAT"    , "999975"  ,NIL})  
  
        Aadd(aItem,{ "RK\_PD"            , "005"     ,nil})  
        Aadd(aItem,{ "RK\_DOCUMEN"       , "000002"  ,nil})  
        Aadd(aItem,{ "RK\_VALORTO"       , 500.00   ,nil})  
        Aadd(aItem,{ "RK\_PARCELA"       , 1         ,nil}  
  
        aAdd(aItens,aItem)  
  
        MSExecAuto({|a, b, c| GPEA110(a, b, c) }, 3, aCab, aItens) //Inclusão  
        //MSExecAuto({|a, b, c| GPEA110(a, b, c) }, 4, aCab, aItens) //Alteração  
        //MSExecAuto({|a, b, c| GPEA110(a, b, c) }, 5, , ) //Exclusão  
  
        If !lMsErroAuto  
            ConOut("\*\*\*\* Incluido com sucesso! \*\*\*\*")  
        Else  
            aLog := getAutoGrLog()  
            MostraErro()  
            ConOut("Erro na Alteracao!")  
        EndIf  
Return aLog

Tabelas Utilizadas:

* **SRK** - Movimento de Valores Futuros
* **SRA** - Funcionários

**Importante**  
Para informações sobre a estrutura do *array* **aItens** consulte a página <http://tdn.totvs.com/x/bv1n>

Tabelas Utilizadas:

* **SRK** - Movimento de Valores Futuros
* **SRA** - Funcionários

**Saiba mais:**Documentação sobre o ExecAuto: <https://tdn.totvs.com/pages/releaseview.action?pageId=521997032>  
Pacote acumulado do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848>
