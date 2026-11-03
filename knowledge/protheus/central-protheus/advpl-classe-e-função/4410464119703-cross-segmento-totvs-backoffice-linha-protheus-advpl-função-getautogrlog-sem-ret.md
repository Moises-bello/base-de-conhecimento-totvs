---
article_id: 4410464119703
category: ADVPL - Classe e Função
content_hash: e023f597d384084309dca9214a2393a3fe4664e1b1c745870d4d60600edc8200
fetched_at: '2026-06-28T22:40:16.761451+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - função GetAutoGRlog
  sem retorno.
type: support-article
updated_at: '2021-10-11T13:19:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410464119703-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-fun%C3%A7%C3%A3o-GetAutoGRlog-sem-retorno
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida** A função está retornando vazia quando há erros em uma execução automática.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Somente haverá retorno de informações (log), se a variável **lAutoErrNoFile** estiver declarada como **.T.**

**Algumas formas de uso:**

Declaração das variáveis como *Private****:***

Private **lMsErroAuto** := .F.Private **lAutoErrNoFile** := .T.Private **lMsHelpAuto** :=.T.

**Algumas formas de obter o retorno:**

1. ```
   //Ex =1  
   aLog := GetAutoGRLog()  
   varinfo("TESTE",aLog)
   ```
2. ```
   //Ex =2  
   aEval(GetAutoGrLog(),{|x|ConOut(x)})
   ```
3. ```
   //Ex =3  
   aErroAuto := GetAutoGRLog()  
   For nCount := 1 To Len(aErroAuto)  
      cLogErro += StrTran(StrTran(aErroAuto[nCount], "<", ""), "-", "") + " "  
      ConOut(cLogErro)  
   Next nCount
   ```

**Saiba mais:**[Variáveis de Controle - MsExecAuto](https://tdn.totvs.com/pages/viewpage.action?pageId=566489232)  
[GetAutoGRLog](https://tdn.totvs.com/pages/viewpage.action?pageId=6815090)
