---
article_id: 360019491411
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 23fe14166ba11c8e5f2d6a2b61cd6a8a1aee4830e94d6dc1c9eb9e65c40eb16c
fetched_at: '2026-06-28T22:37:22.893017+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CN300PLVTO - Total
  Inválido ao incluir uma revisão de Aditivo e alterar a quantidade
type: support-article
updated_at: '2022-05-19T21:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019491411-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CN300PLVTO-Total-Inv%C3%A1lido-ao-incluir-uma-revis%C3%A3o-de-Aditivo-e-alterar-a-quantidade
---

**Ocorrência**Help CN300PLVTO - Total Inválido ao incluir uma revisão de Aditivo e alterar a quantidade**Ambiente**Microsiga Protheus – Gestão de Contratos – A partir da versão 12  
  
**Causa**No módulo Gestão de Contratos, ao tentar realizar uma revisão de aditivo, é apresentada a ocorrência "CN300PLVTO - Valor total inválido, revise a planilha: Informe um valor total de acordo com a quantidade e preço unitários informados!"Esse incidente ocorre, pois não existe gatilho criado para o campo Quantidade (CNB\_QUANT) com contradomínio o campo Valor Total (CNB\_VLTOT).  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Acesse o módulo configurador (SIGACFG);  
2. Acesse o caminho Base de Dados - Dicionário - Base de Dados;  
3. Na opção Gatilhos, crie o gatilho para o campo CNB\_QUANT com contradomínio CNB\_VLTOT;  
4. Informe a regra: Round(M->CNB\_QUANT\*M->CNB\_VLUNIT,TamSX3("CNB\_VLTOT")[2])  
  
**Saiba Mais**[Ao realizar revisão para alterar um produto, exibe o help CN300PLVTO](http://tdn.totvs.com/pages/viewpage.action?pageId=405701576)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
