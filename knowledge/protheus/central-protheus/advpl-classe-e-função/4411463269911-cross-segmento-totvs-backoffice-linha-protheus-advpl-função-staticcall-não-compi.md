---
article_id: 4411463269911
category: ADVPL - Classe e Função
content_hash: d44e80c6efad1304905c4e54d822859378e33e0610587362e528bcc672d54e26
fetched_at: '2026-06-28T22:40:14.176113+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Função StaticCall()
  não compila/mudou o comportamento
type: support-article
updated_at: '2023-06-16T00:53:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411463269911-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Fun%C3%A7%C3%A3o-StaticCall-n%C3%A3o-compila-mudou-o-comportamento
---

**Ocorrência**Utilizo a função StaticCall() mas não está compilando ou teve seu comportamento alterado.  
  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) – ADVPL – A partir da versão 12.1.33  
  
**Causa**Funções, classes e variáveis restritas em fontes customizados não estão previstas pelo suporte padrão, dado ao fato de que as mesmas não estão documentadas, assim sendo, podem vir a ser descontinuadas ou sofrer alterações de comportamento sem prévio aviso.

A função STATICCALL() é de uso interno e restrito, para ações específicas, por isso não existe documentação oficial sobre ela ou recomendação de uso da mesma.

**Solução**Se uma função foi criada com o escopo de STATIC FUNCTION, ela foi pensada inicialmente para ter o escopo de uso somente no fonte em que está criada, e não no sistema todo.  
Se esta utilizando STATICCALL() para chamadas de funções estáticas de customizações, a solução é trocar o escopo da função chamada pela STATICCALL() de STATIC FUNCTION para **USER FUNCTION**, assim ela pode ser usada em qualquer ponto do sistema através do uso de **U\_<função>***.***Saiba mais**  
[Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Funções, classes e variáveis de propriedade interna](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016461772)
