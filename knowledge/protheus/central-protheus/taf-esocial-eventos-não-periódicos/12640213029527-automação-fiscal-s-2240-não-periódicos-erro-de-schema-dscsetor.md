---
article_id: 12640213029527
category: TAF - eSocial - Eventos Não Periódicos
content_hash: bc833bca9bbb065eb14b4bdc8e10b3f38659878e7405b3b3e57d11342f4b19a6
fetched_at: '2026-06-28T22:45:17.914526+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: Automação Fiscal - S-2240 - Não Periódicos - Erro de Schema dscSetor
type: support-article
updated_at: '2024-05-23T20:40:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12640213029527-Automa%C3%A7%C3%A3o-Fiscal-S-2240-N%C3%A3o-Peri%C3%B3dicos-Erro-de-Schema-dscSetor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Ao transmitir o evento S-2240 para o e-Social ocorre o erro de *SCHEMA <dscSetor>*

*Erro de schema:*

*Element '{[http://www.esocial.gov.br/schema/evt/evtExpRisco/v\_S\_01\_00\_00}dscSetor':](http://www.esocial.gov.br/schema/evt/evtExpRisco/v_S_01_00_00%7DdscSetor':) [facet 'minLength'] The value has a length of '0'; this underruns the allowed minimum length of '1'. Element '{<http://www.esocial.gov.br/schema/evt/evtExpRi>*  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação Fiscal - e-Social - Medicina - S-2240 -Condições Ambientais do Trabalho – Fatores de Risco (TAFA264)- Todas as versões  
  
**Solução**

1 - Para correção diretamente dentro do TAF deverá ser preenchido o campo **Lg.Adm**dentro da chave **Informações do ambiente do trabalho:**

Print do campo de **dscSetor** grifado em verde:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012780055/mceclip0.png)

2 - Esse campo é valido com valor de 1 a 100 caracteres e é de uso obrigatório:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012792855/mceclip1.png)

3 - Não orientamos com qual valor preencher este campo verifique a validação do layout do e-Social e realize o preenchimento manual. 

**Obs:** Estamos orientando o preenchimento manual dentro do TAF, caso deseje que o campo venha do ERP de origem correto realizar a abertura de um chamado ao Setor de geração do XML para orientar na geração desta tag.
