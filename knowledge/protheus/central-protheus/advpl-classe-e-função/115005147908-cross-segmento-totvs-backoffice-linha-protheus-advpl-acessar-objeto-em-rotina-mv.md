---
article_id: 115005147908
category: ADVPL - Classe e Função
content_hash: 00de82f4769d8210b104159ba24fe0ad476968572c09f690f0b4a95110cae35f
fetched_at: '2026-06-28T22:40:14.329092+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Acessar objeto em
  rotina MVC
type: support-article
updated_at: '2021-11-17T21:20:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005147908-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Acessar-objeto-em-rotina-MVC
---

**Dúvida**Como acessar o objeto em rotina MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – Todas versões  
  
**Solução**

**Passo a passo:**

Em rotinas em MVC, segue exemplo abaixo os objetos a serem tratados e debugando o objeto omodelgrid é possível acessar aCols\*.

Exemplo da Rotina OMSA010:

oModelx := FWModelActive()->Carregando Model Ativo

oModelxDet := oModelx:GetModel('DA1DETAIL') ->Carregando grid de dados a partir o ID que foi instanciado no fonte.  
oModelxDet:SetValue('DA1\_DESCRI','TESTE')-> Utilizando função para atribuir valor ao campo em tempo de execução

Para obter DA1DETAIL verifique a propriedade ADEPENDENCY   
omodelx:ADEPENDENCY

```
(*) Algumas rotinas em MVC o aCols não esta disponível.
```

**Saiba Mais**[FWModelActive](https://tdn.totvs.com/display/framework/FWModelActive)
