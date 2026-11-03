---
article_id: 115005356867
category: ADVPL - Classe e Função
content_hash: 2f0b8592c1bb2fcaf318373e770e849a3a1bb40b468220988fc50ea04807e97c
fetched_at: '2026-06-28T22:40:20.561672+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - AxCadastro usuário
  administrador
type: support-article
updated_at: '2021-09-01T19:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115005356867-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-AxCadastro-usu%C3%A1rio-administrador
---

**Dúvida**Ao Executar a rotina customizada com **AxCadastro** só roda se o usuário for administrador ou estiver no grupo de Administrador, usuário comum não consegue executar rotina, como proceder?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL – Todas versões  
  
**Solução**Verifique no arquivo XNU a chamada de uma função de usuário se está com # ((#FITFIN37) e TYPE como 01(função Protheus). Isso porque antigamente não existia opção 03 (função de usuário).  
Neste Caso basta alterar no arquivo SIGAXXX.XNU a chamada e tipo no aquivo com por exemplo:

Errado:  
<Function>#FITFIN37</Function>  
<Type>01</Type>  
  
Observação:  
Esta forma era utilizada devido não existir o Tipo (TYPE) = 3 função de usuário.  
  
Certo:  
<Function> FITFIN37</Function>  
<Type>03</Type>

**Saiba mais**  
[ADV0006 Erro Checknewx em rotinas customizadas](https://tdn.totvs.com/display/public/PROT/ADV0006_FUN_Erro_Checknewx_em_Rotinas_Customizadas)
