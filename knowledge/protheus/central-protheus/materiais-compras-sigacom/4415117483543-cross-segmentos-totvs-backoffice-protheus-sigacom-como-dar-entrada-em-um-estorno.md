---
article_id: 4415117483543
category: Materiais - Compras (SIGACOM)
content_hash: f43a6420d4de742e7ad0ac064843f1153f96c4462cb8988693a4a64e9e454f93
fetched_at: '2026-06-28T22:41:14.559955+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como dar entrada em
  um Estorno de Devolução de Compras ?
type: support-article
updated_at: '2022-04-11T14:32:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4415117483543-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-dar-entrada-em-um-Estorno-de-Devolu%C3%A7%C3%A3o-de-Compras
---

**Dúvida**Quando é emitida Nota de Devolução de Compra (NF Saída) com erros e o Destinatário Rejeitou. Não é mais possível Cancelar esta Nota pois passou do prazo.

Como gerar uma nota que **estorne**essa nota de devolução?

**OBS: CASOS QUE IRÁ ESTORNAR SOMENTE NOTA FISCAL (sem produto) POIS SERÁ CORRIGIDO A NOTA FISCAL DE SAÍDA**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões

**Solução**

Emissão de Nota DE ENTRADA (Ou seja, Estorno de uma Devolução de Compra) no cenário:

A) Foi gerada Nota de Entrada - Compra

B) Posteriormente foi gerada Nota de Saída - Devolução da Compra (Emitida com erros)  
  
C) Agora precisa **gerar uma Nota de Entrada - Estorno da Devolução de Compra:**

- Configurar o parâmetro  **MV\_VLDNFO = F,** Assim não haverá validação de nota fiscal origem.

- Incluir um Documento de Entrada do Tipo **Devolução**;

- Cadastrar um novo **Cliente** com os mesmos dados do **Fornecedor**, e selecioná-lo;

- Registrar nas linhas de item os produtos da nota de devolução (da nota de Saída), e referenciar a Nota de Devolução **digitando manualmente os campos D1\_NFORI, D1\_SERIORI e D1\_ITEMORI** (com caracteres exatos, inclusive quantidades de zeros à esquerda);

- Utilizar o TES de Saída devidamente configurado juntamente ao Depto Fiscal da Empresa de acordo com as incidências desta operação (sem movimentar estoque/financeiro para não devolver uma operação que já foi devolvida com a primeira nota de devolução).

***Obs:***

**1)** Neste TES deve estar registrado o campo "Ajuste CIAP" = Sim, para que o xml seja gerado com a Tag FinNFe = 3

**2)** Fonte MATA103 devem estar com data superior a **03/11/2021.**

D) Posteriormente, emitir uma nova nota de Saída - MATA920 - Devolução (correta) da Compra. 

***Saiba Mais :***

[Inclusão de Nota de Estorno da Devolução](https://tdn.totvs.com/pages/releaseview.action?pageId=56754330)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
