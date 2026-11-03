---
article_id: 38340873184663
category: Financeiro - Contas a Receber
content_hash: 2d281ae484e2694bfecc31fa4df0c898da4f622bf950293e24dfa6534571a023
fetched_at: '2026-06-28T22:38:13.920211+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Execauto multi naturezas
  não grava novos campos na SEZ e SEV
type: support-article
updated_at: '2026-02-13T11:32:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38340873184663-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Execauto-multi-naturezas-n%C3%A3o-grava-novos-campos-na-SEZ-e-SEV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38340873170199) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**  
Ao utilizar a rotina automática (ExecAuto) de Multi Naturezas, por que o sistema não realiza a gravação de campos adicionais (customizados ou reservados) nas tabelas SEZ e SEV, mesmo enviando as posições corretamente no array da rotina?  
  
 **Ambiente**  
Cross Segmento – TOTVS Backoffice (Linha Protheus) - Financeiro - 12.1.2210  
  
 **Solução**  
Esse comportamento ocorre devido à própria arquitetura da rotina automática. O array de entrada possui apenas posições padrão e fixas, e o motor responsável pela gravação nas tabelas de rateio trabalha com uma estrutura pré-determinada no código fonte (campos estáticos). Dessa forma, campos que não estejam previstos no layout original da rotina não são reconhecidos nem processados durante a execução.

Ou seja, ainda que o campo exista fisicamente no dicionário, a rotina automática de Multi Naturezas não contempla a gravação de informações adicionais nas tabelas SEZ e SEV.

Como alternativa para atender à necessidade de gravação dessas informações, recomendamos:

* **Gravação na origem do título**: Registrar os dados necessários diretamente nas tabelas **SE1 (Contas a Receber)** ou **SE2 (Contas a Pagar)**, que suportam a inclusão de campos customizados via ExecAuto.
* **Relacionamento com o rateio**: Como o vínculo entre as tabelas de título e as tabelas de rateio é nativo e constante, a informação pode ser consultada posteriormente mantendo a integridade do relacionamento.

Veja o exemplo de gravação do contas a pagar, utilizando o campo adicional E2\_TESTE:

```
#Include 'Protheus.ch'
#INCLUDE "TBICONN.CH"

USER FUNCTION RATMULT()

LOCAL aCab      := {} // array que recebera o titulo a receber
LOCAL aAuxEv    :={} // array auxiliar do rateio multinaturezas
LOCAL aRatEvEz  :={} //array do rateio multinaturezas
LOCAL aAuxEz    :={} // Array auxiliar de multiplos centros de custo
LOCAL aRatEz    :={} //Array do rateio de centro de custo em multiplas naturezas



PREPARE ENVIRONMENT EMPRESA '99' FILIAL '01'

PRIVATE lMsErroAuto := .F.

 aadd( aCab ,{"E2_PREFIXO"   , 'TST' , Nil }) 
 aadd( aCab ,{"E2_NUM"       , "000001" , Nil })
 aadd( aCab ,{"E2_PARCELA"   , '1' , Nil })
 aadd( aCab ,{"E2_TIPO"      , 'NF ' , Nil })
 aadd( aCab ,{"E2_NATUREZ"   , 'DINHEIRO        ', Nil })
 aadd( aCab ,{"E2_FORNECE"   , '001   ' , Nil })
 aadd( aCab ,{"E2_LOJA"      , '01' , Nil })
 aadd( aCab ,{"E2_EMISSAO"   , dDataBase , Nil })
 aadd( aCab ,{"E2_VENCTO"    , dDataBase , Nil })
 aadd( aCab ,{"E2_VALOR"     , 2000, Nil })
 aadd( aCab ,{"E2_TESTE"     , "EXECAUTO", Nil }) //Campo Adicionado
 aadd( aCab ,{"E2_MULTNAT"   , '1' , Nil }) //rateio multinaturezs = sim

//#########################################################################################################&
 //Adicionando o vetor da 1º Natureza &
 //#########################################################################################################&

 aadd( aAuxEv ,{"EV_NATUREZ" , padr('DINHEIRO ',tamsx3("EV_NATUREZ")[1]), Nil })//natureza a ser rateada
 aadd( aAuxEv ,{"EV_VALOR" , 1500, Nil })//valor do rateio na natureza
 aadd( aAuxEv ,{"EV_PERC" , "75", Nil })//percentual do rateio na natureza
 aadd( aAuxEv ,{"EV_RATEICC" , "1", Nil })//indicando que há rateio por centro de custo

//###########################################&
 //Adicionando multiplos centros de custo &
 //###########################################&

//primeiro centro de custo
 aAuxEz:={}
 aadd( aAuxEz ,{"EZ_CCUSTO" , '000000001', Nil })//centro de custo da natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 1500 , Nil })//valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)

aadd(aAuxEv,{"AUTRATEICC" , aRatEz, Nil })//recebendo dentro do array da natureza os multiplos centros de custo
 aAdd(aRatEvEz,aAuxEv)//adicionando a natureza ao rateio de multiplas naturezas

// Limpar os Arrays
 aAuxEv:={} // Array auxiliar do rateio multinaturezas
 aAuxEz:={} // Array auxiliar de multiplos centros de custo
 aRatEz:={} // Array do rateio de centro de custo em multiplas naturezas

//#########################################################################################################&
 //Adicionando o vetor da 2º Natureza &
 //#########################################################################################################&

 aadd( aAuxEv ,{"EV_NATUREZ" , padr('CREDITO ',tamsx3("EV_NATUREZ")[1]), Nil })//natureza a ser rateada
 aadd( aAuxEv ,{"EV_VALOR" , 500, Nil })//valor do rateio na natureza
 aadd( aAuxEv ,{"EV_PERC" , "25", Nil })//percentual do rateio na natureza
 aadd( aAuxEv ,{"EV_RATEICC" , "1", Nil })//indicando que há rateio por centro de custo

//###########################################&
 //Adicionando multiplos centros de custo &
 //###########################################&

//primeiro centro de custo
 aadd( aAuxEz ,{"EZ_CCUSTO" , '000000002', Nil })//centro de custo da natureza
 aadd( aAuxEz ,{"EZ_VALOR" , 500 , Nil })///valor do rateio neste centro de custo
 aadd(aRatEz,aAuxEz)


aadd(aAuxEv,{"AUTRATEICC" , aRatEz, Nil })//recebendo dentro do array da natureza os multiplos centros de custo
 aAdd(aRatEvEz,aAuxEv)//adicionando a natureza ao rateio de multiplas naturezas

aAdd(aCab,{"AUTRATEEV", aRatEvEz,Nil})//adicionando ao vetor aCab o vetor do rateio

MsExecAuto( { |x,y,z| FINA050(x,y,z)} , aCab, ,3) //inclusao

If lMsErroAuto
 MostraErro()
 Else
 ConOut("Título incluído com sucesso!")
 Endif

RESET ENVIRONMENT
Return
```

Registro na tabela de origem conforme o array informado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38340873170839)

Relacionamento entre a tabela principal e valores do rateio:

![execauto multinat.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/38340873171223)
