---
content_hash: 0f822ca74b5e5e2710cf0b60570a4c5e58d58ceb7789883ce4bc5ef5148d67d8
fetched_at: '2026-06-29T00:05:55.681577+00:00'
page_id: '145362237'
product: rm
source: tdn-rm
title: RMFIN00005_Como identificar as baixas parciais de um Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=145362237
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM - TOTVS Gestão Financeira - V11.82.34 |
| **Processo** | : | Identificação das baixas parciais pelo lançamento de origem |
| **Data da publicação** | : | 30/05/2014 |

Disponibilizado no TOTVS Gestão Financeira um recurso que tem o objetivo de tornar mais dinâmica a identificação dos lançamentos derivados de uma baixa parcial, em que eram gerados lançamentos derivados deste processo.

A princípio este recurso será liberado por meio de execução de script, que será liberado juntamente com a release.

**Usabilidade: Lançamentos de origem TOTVS Incorporação - TIN**

Desenvolvimento/Procedimento

Acesse:  TOTVS Gestão Financeira | Serviços Globais | Perfis | Acessar o perfil do usuário | Aba Acesso a menus | [07] Utilitários | [07.01] Impactos de Conversão | [07.01.05] Preencher Em Lançamentos a Ref. Lançamento Pai:.

Habilite a opção “Preencher Em Lançamentos a Ref. do Lançamento Pai”.

2. Para execução do processo, siga os passos abaixo: Acesse o TOTVS Gestão Financeira | Utilitários | Preencher Em Lançamentos a Ref. Lançamento 

2. Clicar em [Executar], o sistema exibirá mensagem, clicar em [Sim] e aguardar até que o processo seja finalizado.

3. Feito isso, irá conter na tabela o campo  IDLANPAI preenchido com o IDLAN do lançamento. Sempre que for inserido um novo lançamento na FLAN, o ID deste também será inserido na FRELLANPAI.
