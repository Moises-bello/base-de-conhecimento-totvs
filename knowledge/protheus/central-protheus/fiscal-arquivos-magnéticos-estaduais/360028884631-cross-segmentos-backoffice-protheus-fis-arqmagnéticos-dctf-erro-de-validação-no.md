---
article_id: 360028884631
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: f4c317c87ca12dabe8ebe3e593c49a61a77ef02571d1756f44f9cdad70286187
fetched_at: '2026-06-28T22:42:10.697409+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DCTF - Erro
  de validação no logradouro
type: support-article
updated_at: '2022-08-17T20:15:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028884631-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DCTF-Erro-de-valida%C3%A7%C3%A3o-no-logradouro
---

**Ocorrência**Ao importar o arquivo da **DCTF,** ocorre o erro de validação:

**Campo 08 logradouro - Campo com valor Inválido**

![](http://tdn.totvs.com/download/attachments/331861545/image2018-1-22_16-22-10.png?version=1&modificationDate=1516646575000&api=v2)  
  
**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Causa**O problema ocorra pelo preenchimento incorreto dos dados cadastrais da empresa (**SIGAMAT**).  
  
**Solução**Para correção do erro, é necessário preencher o logradouro no cadastro de empresas (**Sigamat.emp**), conforme o exemplo abaixo:

**Logradouro(rua, avenida) sem abreviação + nome da rua sem abreviação + , +(espaço) + número da rua**

Exemplo: Rua Brasil, 100  
  
Caso o endereço seja por exemplo: Rodovia Castelo branco KM 35  
A informação KM 35 deve ser informada em Complementos e o campo Endereço deve ser preenchido como Rodovia Castelo Branco, S/N
