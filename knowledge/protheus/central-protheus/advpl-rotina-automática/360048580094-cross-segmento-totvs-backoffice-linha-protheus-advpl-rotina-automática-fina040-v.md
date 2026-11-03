---
article_id: 360048580094
category: ADVPL - Rotina Automática
content_hash: f257b6c7c9922107082785c6e4cbcfa255ff91222ee1e7cdbf9b5af873095570
fetched_at: '2026-06-28T22:40:25.027147+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Rotina automática
  Fina040: valores acessórios'
type: support-article
updated_at: '2021-06-14T20:22:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048580094-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Rotina-autom%C3%A1tica-Fina040-valores-acess%C3%B3rios
---

**Dúvida**Como informar valores acessórios na ExecAuto **FINA040?**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**

Para realizar esse processo, siga as orientações abaixo:  
  
Criar um *array* de duas posições e alimentar conforme exemplo/explicações abaixo:

```
aAdd(aVAAut, {cValAce1, nValAce1})
```

**cValAce1:**  é o código do valor acessório cadastrado na FKC  
**nValAce1:** é valor ou percentual do valor acessório a ser aplicado no titulo.

 Enviar esse *array* na oitava posição da ExecAuto da FINA040

```
MsExecAuto( { |x,y,z,w,k,a,b,c| FINA040(x,y,,,,,,c)}, aArray, nOpc,,,,,,aVAAut)
```

 Funciona tanto para inclusão de títulos (opção 3) como para alteração (opção 4).  
  
**Saiba Mais:**  
[**Valores Acessórios no Contas a Receber**](https://tdn.totvs.com/pages/releaseview.action?pageId=311631483)
