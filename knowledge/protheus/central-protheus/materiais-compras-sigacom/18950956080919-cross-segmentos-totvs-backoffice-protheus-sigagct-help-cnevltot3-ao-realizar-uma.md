---
article_id: 18950956080919
category: Materiais - Compras (SIGACOM)
content_hash: 80283cc24d55a7e24b250537d61de8e781bdb524c22c5258b2846b0ca7c55e67
fetched_at: '2026-06-28T22:41:25.476427+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Help CNEVLTOT3 ao realizar
  uma Medição de um Contrato
type: support-article
updated_at: '2024-05-06T11:38:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18950956080919-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Help-CNEVLTOT3-ao-realizar-uma-Medi%C3%A7%C3%A3o-de-um-Contrato
---

**Dúvida**Ao Confirmar a inclusão de uma medição está apresentando o Help CNEVLTOT3.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18950902473751)

**Ambiente**Protheus – Gestão de Contratos – A partir da versão 12.1.23

**Solução**

Para a necessidade de realização de medições com valor maior que o programado na parcela do Cronograma do Contrato, há disponível no módulo Gestão de Contratos a configuração dos campos de "Limite de Medição" existentes no cadastro do Tipo de Contrato (**CN1\_LMTMED**) e no Tipo de Planilha (**CNL\_LMTMED**) a serem utilizados no Contrato, onde se define o percentual de limite a maior.

Campo no Tipo de Contrato (CN1\_LMTMED):

![](https://totvssuporte.zendesk.com/attachments/token/EQK9vj32WdwWlaurFOCbjCNZk/?name=inline429210754.png)

Campo no Tipo de Planilha (CNL\_LMTMED):

![](https://totvssuporte.zendesk.com/attachments/token/01dIEamWTLJEh05F29mwtB5VZ/?name=inline-747370048.png)

Lembrando que a configuração realizada no campo do Tipo de Planilha sobrepõe a configuração realizada no campo do Tipo de Contrato, na utilização de configurações diferentes em um mesmo contrato.

No caso de Contratos cadastrados com configuração **que possui Cronograma Financeiro**, o valor previsto da medição/Parcela é o contido no campo "Vl.PrevParc. (CNF\_VLPREV) e assim nos campos referenciados no artigo pode-se informar um percentual a mais do previsto que pode ser realizado no total dos itens da medição. Caso ultrapasse este percentual limite, ocorre  o help CNEVLTOT3.

No caso da ocorrência do Help CNEVLTOT3 em Contratos cadastrados com configuração **que não possui Cronograma Financeiro**, ela pode ser devida a quando o valor total dos itens da medição, ultrapassar o saldo da planilha (CNA\_SALDO).

**Obs1:**

Na utilização do campo de "Limite Med" informado, e realização de medições com valores maiores que o Previsto na Parcelas do Cronograma Finanaceiro, como será consumido um saldo do contrato maior que o Previsto, posteriormente, se as parcelas posteriores não forem medidas com valores menores que os seus previstos, o contrato precisará sofrer revisão para inclusão de Saldo Total, para haver este saldo no montante total disponível no Contrato para realização das medições dessas parcelas posteriores.

***Saiba Mais:***

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)

[SIGAGCT - Como realizar medições com valores maior que o previsto no Cronograma Financeiro do Contrato ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051964674-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-realizar-medi%C3%A7%C3%B5es-com-valores-maior-que-o-previsto-no-Cronograma-Financeiro-do-Contrato-?source=search)
