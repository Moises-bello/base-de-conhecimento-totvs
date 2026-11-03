---
article_id: 10563957534487
category: Call Center - Dúvidas Gerais
content_hash: 41757fdd0eed68ae138bde85ae251351ce1917aef19c4bd30cb0035eaf5d270b
fetched_at: '2026-06-28T22:41:26.923400+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - EXECAUTO TMKA070
type: support-article
updated_at: '2022-11-29T20:43:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10563957534487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGATMK-EXECAUTO-TMKA070
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do **Execauto TMKA070 - Contatos.**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGATMK - A partir da release 12.  
  
**Solução**Função utilizada para geração de Contatos via rotina automática (ExecAuto).  
  
**Exemplo**

```
#INCLUDE 'Protheus.ch'  
#INCLUDE 'TBICONN.CH'  
  
User Function MyTMK070()  
  
    Local aContato := {}  
    Local aEndereco := {}  
    Local aTelefone := {}  
    Local aAuxDados := {}  
    Private lMsErroAuto := .F.  
  
    PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01"  //Empresa / Filial  
  
        ConOut(Repl("-",80))  
        ConOut(PadC("Teste de Inclusao de Contato"  ,80))  
        ConOut("Incluindo Contato")  
        ConOut("Inicio: " +Time())  
  
        //CONTATO  
        AAdd(aContato,{"U5_FILIAL",xFilial("SU5")        ,Nil}) //Filial  
        AAdd(aContato,{"U5_CODCONT","000020"               ,Nil}) //Código do Contato  
        AAdd(aContato,{"U5_CONTAT","Nome do contato"      ,Nil}) //Nome do Contato  
        AAdd(aContato,{"U5_EMAIL"  ,"inclusao@totvs.com.br",Nil}) //E-mail  
  
        //TELEFONES  
        AAdd(aAuxDados, {"AGB_TIPO"  ,"2"       ,Nil}) //Tipo do Telefone  
        AAdd(aAuxDados, {"AGB_PADRAO","1"       ,Nil}) //Padrão?  
        AAdd(aAuxDados, {"AGB_DDI"   ,""        ,Nil}) //DDI  
        AAdd(aAuxDados, {"AGB_DDD"   ,"11"      ,Nil}) //DDD  
        AAdd(aAuxDados, {"AGB_TELEFO","12349874",Nil}) //Telefone  
  
        AAdd(aTelefone,aAuxDados)  
  
        aAuxDados := {}  
  
        //ENDEREÇOS  
        AAdd(aAuxDados, {"AGA_TIPO"  ,"2"           ,Nil}) //Tipo do Endereço  
        AAdd(aAuxDados, {"AGA_PADRAO","1"           ,Nil}) //Padrão?  
        AAdd(aAuxDados, {"AGA_END"   ,"R. Totvs"    ,Nil}) //Endereço  
        AAdd(aAuxDados, {"AGA_CEP"   ,"12345123"    ,Nil}) //CEP  
        AAdd(aAuxDados, {"AGA_BAIRRO","Bairro Totvs",Nil}) //Bairro  
        AAdd(aAuxDados, {"AGA_MUNDES","Cidade Totvs",Nil}) //Município  
        AAdd(aAuxDados, {"AGA_EST"   ,"SP"          ,Nil}) //Estado  
  
        AAdd(aEndereco,aAuxDados)  
  
        ConOut("Iniciando a inclusao")  
        MSExecAuto({|x,y,z,a,b|TMKA070(x,y,z,a,b)},aContato,3,aEndereco,aTelefone,.F.)   
  
        If lMsErroAuto  
            MsgStop("Erro na inclusao do contato")  
            Mostraerro()  
        Else  
            MsgAlert('Contato incluido com sucesso!')  
        EndIf  
  
        ConOut("Fim: " +Time())  
        ConOut(Repl("-",80))  
  
    RESET ENVIRONMENT      
  
Return
```

**Saiba Mais**

**[TMKA070 - Rotina Automatica de Contatos](https://tdn.totvs.com/x/gJJn)**
