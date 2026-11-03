---
article_id: 4405488721175
category: Call Center - Dúvidas Gerais
content_hash: 29fb61dc983779a631a855835074309544acd375faa7e2ce465e66ecbde727a4
fetched_at: '2026-06-28T22:41:26.953567+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGATMK - Histórico de Ligações TMKA271
type: support-article
updated_at: '2025-01-10T19:15:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405488721175-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Hist%C3%B3rico-de-Liga%C3%A7%C3%B5es-TMKA271
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17201808907159) Tempo aproximado para leitura: **00:08:00 min** **Dúvida**  
Qual índice é utilizado no Histórico de Ligações referente as cobranças, vendas e ao marketing na rotina TMKA271?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGATMK - A partir da release 12  
  
**Solução**

Segue abaixo os índices relacionados as rotinas de telecobrança, televendas e telemarketing.  **Telecobrança**   
  
A ordenação utilizada no histórico de ligações referente a **cobrança** é feito com base no Índice 2 da tabela ACF.  
  
(ACF\_CLIENT+ACF\_LOJA).                               
  
  
A ordenação dos itens utilizados no histórico de ligações referente as **cobranças** é feito com base no Índice 2 da tabela ACG**Itens de Telecobrança**         
  
(ACG\_FILIAL+ACG\_PREFIX+ACG\_TITULO+ACG\_PARCEL+ACG\_TIPO+ACG\_FILORI).

Tabelas utilizadas pelo fonte **TKC020A** (Fonte responsável pelo histórico de cobrança)  
ACF - Telecobrança  
ACG - Itens Telecobrança  
SU7 - Operadores  
SU9 - Ocorrências  
SA1 - Clientes  
SE1 - Contas a Receber  
  
Pontos de entrada:

* [TK062LIS - Manipulação do itens de lista de cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=107940080)
* [TK062SK1 - Filtro na lista de Cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=309397045)
* [TKC20Hist - Botão Histórico de Cobrança.](https://tdn.totvs.com/pages/releaseview.action?pageId=6787761)

**Televendas**

A ordenação utilizados no histórico de ligações referente as **Vendas** é feito com base no Índice 7 da tabela SUA **Orçamento Televendas**         
  
(UA\_FILIAL+UA\_CLIENTE+UA\_LOJA+STR(UA\_DIASDAT,8,0)+STR(UA\_HORADAT,8,0)

A ordenação dos itens utilizados no histórico de ligações referente as **V****endas** é feito com base no Índice 1 da tabela SUB **Itens do Orçamento Televendas**

(UB\_FILIAL+UB\_NUM+UB\_ITEM+UB\_PRODUTO)  
  
Pontos de entrada:

* [TMKVHI - Botão de Histórico na tela de Televendas](https://tdn.totvs.com/pages/viewpage.action?pageId=721725356).

**Telemarketing**

A ordenação utilizada no histórico de ligações referente ao **Marketing** é feito com base no Índice 2 da tabela SUC **Cabeçalho do Telemarketing**   
  
(UC\_FILIAL+UC\_ENTIDAD+UC\_CHAVE)

A ordenação dos itens utilizados no histórico de ligações referente ao **Marketing** é feito com base no Índice 1 da tabela SUD **Itens do Telemarketing**

(UD\_FILIAL+UD\_CODIGO+UD\_ITEM)
