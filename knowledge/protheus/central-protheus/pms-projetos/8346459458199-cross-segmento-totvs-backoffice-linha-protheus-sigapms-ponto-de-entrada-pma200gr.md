---
article_id: 8346459458199
category: PMS - Projetos
content_hash: af7ef400ef2678547bd3cee10f25e897680e47b0f72c55f81949f15c76c39eb7
fetched_at: '2026-06-28T22:37:15.141622+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - Ponto de Entrada
  PMA200GRV
type: support-article
updated_at: '2022-08-22T17:49:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8346459458199-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAPMS-Ponto-de-Entrada-PMA200GRV
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Exemplo de utilização do Ponto de Entrada **PMA200GRV - Valida mudança de fase em projetos**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAPMS - A partir da release 12.  
  
**Solução**

Este Ponto de Entrada é um **validador da mudança de fase de um projeto**. Após a confirmação da nova fase, o ponto de entrada é chamado e deve retornar **.T. (True)** ou **.F. (False)** para gravar (ou não) as informações nos campos **AF8\_FASE** e **AF8\_ENCPRJ**. Também executa (ou não) as **integrações** do módulo **PMS** - Gerenciamento de Projetos com o módulo de **PCO** - Planejamento e Controle Orçamentário.  
  
**Exemplo**

```
User Function PMA200GRV()  
  
    Local lRet := .T. // Permite a gravação dos campos da AF8  
  
    If AEA->AEA_COD == "05"  
        MsgInfo("Entrou no PE - Nao vai alterar para a fase 05", "Ponto de Entrada PMA200GRV")  
        lRet := .F.  // Caso a fase seja "05", não permite a continuação do processo e não grava os campos da AF8 e nem processa a integração com PCO  
    EndIf  
  
Return lRet
```

 **Saiba Mais: [PMA200GRV - Valida mudança de fase em projetos](https://tdn.totvs.com/x/YrBn)**
