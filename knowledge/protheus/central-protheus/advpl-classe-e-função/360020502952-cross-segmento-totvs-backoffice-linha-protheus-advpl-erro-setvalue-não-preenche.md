---
article_id: 360020502952
category: ADVPL - Classe e Função
content_hash: b782f60e54a0dfe87094d001e715b38191fac20fd50cb9b706321ed1a1b16247
fetched_at: '2026-06-28T22:40:16.683520+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Erro: Setvalue
  não preenche campo memo em mvc'
type: support-article
updated_at: '2022-02-21T12:20:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020502952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Erro-Setvalue-n%C3%A3o-preenche-campo-memo-em-mvc
---

**Ocorrência**Ao utilizar o método SetValue() em uma rotina em MVC para preencher um campo do tipo Memo, o mesmo não é preenchido.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Causa**Dependendo do momento em que se estiver tentando realizar a inserção de dados em um submodelo de uma rotina MVC, está ação pode não ser replicada para *view*.  
  
**Solução**Após atribuir o valor ao campo desejado utilize o método *Refresh*() da classe FwFormView() passando o identificador da *subview* que se deseja atualizar.  
  
**Fonte**

```
oModel:SetValue("ZA0_NOTAS", AllTrim(oModel:GetValue("ZA0_NOME"))) // ALTERA CAMPO MEMO  
oView:Refresh("VW_MASTERZA0") // ATUALIZAÇÃO A SUBVIEW ONDE O CAMPO ESTÁ CONTIDO
```

**Saiba mais**  
[FWFormView](http://tdn.totvs.com/display/framework/FWFormView)
