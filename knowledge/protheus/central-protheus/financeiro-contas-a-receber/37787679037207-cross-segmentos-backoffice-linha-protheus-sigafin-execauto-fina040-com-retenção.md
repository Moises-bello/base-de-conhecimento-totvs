---
article_id: 37787679037207
category: Financeiro - Contas a Receber
content_hash: 233af9a255f2ab10e1e864e8f26d209464f331fcf1d7219b327b14034fcc4745
fetched_at: '2026-06-28T22:38:12.614484+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Execauto FINA040 com
  retenção PCC
type: support-article
updated_at: '2026-01-20T12:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37787679037207-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Execauto-FINA040-com-reten%C3%A7%C3%A3o-PCC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37787662321175) Tempo aproximado para leitura: **00:06 min**  
  
**Dúvida**  
Como realizar a inclusão de títulos de Contas a Receber com retenção de impostos (PIS, COFINS e CSLL) via rotina automática (ExecAuto) FINA040?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.33.  
  
**Solução:**

Para que o ExecAuto da rotina FINA040 (Contas a Receber) realize o cálculo e a retenção automática dos impostos federais (PCC), é necessário que as configurações de cadastro (Natureza e Cliente) e os parâmetros de sistema estejam devidamente alinhados.

##### Passos

1. **Configuração da Natureza (SED):** Acesse o cadastro de Naturezas e certifique-se de que os campos de cálculo de imposto estejam habilitados:

   * **Calcula PIS (ED\_CALCPIS)** = Sim
   * **Percentual de PIS (ED\_PERCPIS)** = Informe a alíquota correspondente.
   * **Calcula COFINS (ED\_CALCCOF)** = Sim
   * **Percentual de COFINS (ED\_PERCCOF)** = Informe a alíquota correspondente.
   * **Calcula CSLL (ED\_CALCCSL)** = Sim
   * **Percentual de CSLL (ED\_PERCCSL)** = Informe a alíquota correspondente.  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37787679032599)
2. **Configuração do Cliente (SA1):** No cadastro de Clientes, configure a obrigatoriedade da retenção:

   * **Rec. PIS (A1\_RECPIS)** = Sim
   * **Rec. COFINS (A1\_RECCOFI)** = Sim
   * **Rec. CSLL (A1\_RECCSLL)** = Sim
   * **Modo de abatimento do imposto (A1\_ABATIMP)** = Cálculo do sistema.  
     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37787662322839)
3. **Verificação de Parâmetros (Configurador):** O parâmetro **MV\_BR10925** define o momento da geração e o tipo do título de imposto.

   > **Importante:** Este parâmetro não deve ser alterado após o início da operação do sistema para evitar inconsistências nos saldos e tipos de títulos.

   * **Conteúdo = 2 (Default):** A retenção ocorre na **Emissão**. O sistema gera títulos de abatimento (PI-, CF- e CS-). Na consulta, esses valores são somados ao campo "Abatimentos".
   * **Conteúdo = 1:** A retenção ocorre na **Baixa**. O sistema gera títulos que não são de abatimento (PIS, COF e CSL).
4. **Execução via ExecAuto:** Ao montar o Array do ExecAuto da FINA040, utilize a Natureza e o Cliente configurados nos passos anteriores. O sistema processará as validações de cadastro e gerará automaticamente os títulos de impostos vinculados ao título principal.

```
#INCLUDE "TOTVS.CH"
#INCLUDE "TBICONN.CH"
 
Function U_F40INC()
 
LocAL nX   
LOCAL aArray := {}
PRIVATE lMsErroAuto := .F.
 
PREPARE ENVIRONMENT EMPRESA "99" FILIAL "01" MODULO "FIN"
 
Conout("----Inicio da Rotina Automatica!------")
 
For nX := 1 To 1 //1 titulos NF
 
    aArray := { { "E1_PREFIXO"  , "TST"                , NIL },;
                { "E1_NUM"      , StrZero(nX,9)        , NIL },;
                { "E1_TIPO"     , "BOL"                , NIL },;
                { "E1_NATUREZ"  , "PCC CR    "         , NIL },;
                { "E1_CLIENTE"  , "PCC   "             , NIL },;
                { "E1_LOJA"     , "01"                 , NIL },;
                { "E1_EMISSAO"  , CtoD("19/01/2026")   , NIL },;
                { "E1_VENCTO"   , CtoD("19/01/2026")   , NIL },;
                { "E1_VENCREA"  , CtoD("19/01/2026")   , NIL },;
                { "E1_IDCNAB "  , StrZero(nX,10)       , NIL },;
                { "E1_VALOR"    , 500000                    , NIL }}
 
    MsExecAuto( { |x,y| FINA040(x,y)} , aArray, 3,,)  // 3 - Inclusao, 4 - Alteração, 5 - Exclusão
 
    If !lMsErroAuto
    ConOut(" Incluido!")
    Else // EM ESTADO DE JOB
      cError := MostraErro("/dirdoc", "error.log") // ARMAZENA A MENSAGEM DE ERRO
      ConOut(cError)
    EndIf
 
Next nX
 
Return
```

**Importante**  
O teste deve ser efetuado conforme o exemplo publicado pelo Desenv. no TDN variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado ao fato de que as mesmas não estão documentadas, assim sendo, podem ser descontinuadas ou sofrer alterações de comportamento sem aviso
