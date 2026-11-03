---
article_id: 360034283234
category: esocial - Periódicos
content_hash: fa7234695108292a7f7e868799546a753336469a5b2f60db056159cce7961ea5
fetched_at: '2026-06-28T22:47:09.507277+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Transportador autônomo categoria 712 no TOTVS Folha
  de Pagamento
type: support-article
updated_at: '2024-06-17T12:37:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034283234-RH-RM-FOP-eSocial-Transportador-aut%C3%B4nomo-categoria-712-no-TOTVS-Folha-de-Pagamento
---

**Dúvida**Como informar a categoria **712 Transportador Autônomo** na Folha de Pagamento?  
  
 **Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**A parametrização necessária para a correta inclusão do autônomo carreteiro é:  
1. Acesse **Administração de Pessoal | Funcionário | Registro** e determine a categoria do funcionário como como **712 - Transportador Autônomo de Carga**;  
 2. Acesse **Administração de Pessoal | Eventos;**2.1. Inclua os eventos com os seguintes códigos de cálculo;

* [Código de Cálculo 399 - REMUNERAÇÃO FRETE AUTÔNOMO](http://tdn.totvs.com.br/pages/releaseview.action?pageId=461921339)
* [Código de Cálculo 400 - REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM IRRF](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921371)
* [Código de Cálculo 401 - REMUNERAÇÃO FRETE AUTÔNOMO COM INCIDÊNCIA EM INSS](http://tdn.totvs.com.br/pages/viewpage.action?pageId=461921386)

2.2. Associe em cada evento cadastrado a Rubrica de acordo com a Tabela 3 do *layout* eSocial.  
  
**Importante**1. Os cálculos dos valores referente a cada evento cadastrado para esse fim, deverá ser feito por fórmula.  
2. O lançamento desses eventos na folha de pagamento dos autônomos poderá ser realizada através do grupo de eventos ou códigos fixos.  
  
**Saiba Mais**Para mais informações acesse:   
- [Eventos S-1200 e S-1210 - Transportador autônomo](https://tdn.totvs.com/pages/releaseview.action?pageId=496796713)
