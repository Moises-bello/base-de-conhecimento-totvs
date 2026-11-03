---
article_id: 360019494951
category: Materiais - Compras (SIGACOM)
content_hash: f78c44b0c19694dc08cb47dc5899fcc14b03b3c094999d865d6dce20e2f779c0
fetched_at: '2026-06-28T22:41:18.859095+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A116CHVNFE ao
  informar Chave NFe ao incluir Conhecimento de Transporte MATA116
type: support-article
updated_at: '2022-05-18T20:57:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019494951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-A116CHVNFE-ao-informar-Chave-NFe-ao-incluir-Conhecimento-de-Transporte-MATA116
---

**Ocorrência**

Help A116CHVNFE ao informar Chave NFe ao incluir Conhecimento de Transporte MATA116

**Ambiente**

No módulo **Compras**, ao tentar realizar a inclusão de um Conhecimento de Transporte Eletrônico via rotina Nt Conhec. Frete (MATA116), informando o campo Chave NFE (F1\_CHVNFE), é apresentada a ocorrência A116CHVNFE - Chave NFE informada não confere com a nota que está sendo digitada.

Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Causa**

Esse incidente ocorre, pois a chave informada não confere com os dados da nota que foi digitado, validando Número da Nota + Série + CNPJ do Fornecedor.  
  
**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Separar os números da chave conforme regra abaixo;  
  
![Resultado de imagem para composiÃ§Ã£o chave nfe](http://www.javac.com.br/javac/images/chave-nfe.png)  
  
2. Acessar o cadastro do fornecedor e verificar se o CNPJ informado confere com o CNPJ do Emitente, que compõe a chave da NFE;  
  
3. Verificar se o Número da Nota e Série digitados, conferem com o que está compondo a Chave da NFE.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
