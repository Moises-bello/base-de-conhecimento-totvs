---
article_id: 4576473715735
category: Materiais - Compras (SIGACOM)
content_hash: 2203d5a8ef3632ed4f332ef8995d040c69b4f5159649cb6b015717d46771040a
fetched_at: '2026-06-28T22:41:14.413107+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Comissão Negativa
type: support-article
updated_at: '2022-05-16T22:38:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4576473715735-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Comiss%C3%A3o-Negativa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02 min** **Dúvida**

Como gerar Comissão Negativa ao realizar uma devolução ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12

**Solução**

Quando realizada uma venda, porém o cliente devolve a nota, é possível gerar uma comissão negativa para abater a comissão gerada pela venda.  
Para isso, basta habilitar o parâmetro **MV\_COMIDEV = T**, ao realizar a devolução de uma nota fiscal de venda, o sistema irá inserir um registro de Comissão Negativa para o vendedor na tabela de comissões (**SE3**) **Observação:**Para geração da Comissão Negativa é necessário que os campos **E1\_VEND(x)** e **E1\_COMIS(x)** do título a receber estejam preenchidos. 

![20220303_185039.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4576423520919/20220303_185039.gif)

**IMPORTANTE :** Para que seja gerada uma NCC (Nota de Crédito do Cliente) no Financeiro, a devolução da nota fiscal de venda com TES que gera duplicada deverá estar relacionada com um TES de Devolução com o campo F4\_DUPLIC=SIM (Gera. Dupl).

***Saiba Mais:***

* [Configuração das Comissões dos Vendedores](Configura%C3%A7%C3%A3o%20das%20Comiss%C3%B5es%20dos%20Vendedores)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
