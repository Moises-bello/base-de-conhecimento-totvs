---
article_id: 4413012803735
category: TAF - eSocial - Eventos Não Periódicos
content_hash: 6d0981ff705fa3bcfb08421e666991e3ed5b36f4fadfb5bdd18cb723b958cd28
fetched_at: '2026-06-28T22:45:18.107101+00:00'
product: protheus
section_id: 1500001548002
source: central-protheus
title: Automação Fiscal - Não periódicos - Erro de Schema dscSetor
type: support-article
updated_at: '2022-04-28T17:03:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413012803735-Automa%C3%A7%C3%A3o-Fiscal-N%C3%A3o-peri%C3%B3dicos-Erro-de-Schema-dscSetor
---

**Dúvida**Ao transmitir o evento S-2240 para o e-Social ocorre o erro de SCHEMA dscSetor  
  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Automação Fiscal - À partir da release 12.1.25  
  
**Solução**

1 - Para correção diretamente dentro do TAF deverá ser preenchido o campo **Lg.Adm** dentro da chave **Informações do ambiente do trabalho:**

Print do campo de dscSetor grifado em verde:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012780055/mceclip0.png)  
​  
  
2 - Esse campo é valido com valor de 1 a 100 caracteres e é de uso obrigatório:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4413012792855/mceclip1.png)

3 - Não orientamos com qual valor preencher este campo verifique a validação do layout do e-Social e realize o preenchimento manual.

**Obs:** Estamos orientando o preenchimento manual dentro do TAF, caso deseje que o campo venha do ERP de origem correto realizar a abertura de um chamado ao Setor de geração do XML para orientar na geração desta tag.
