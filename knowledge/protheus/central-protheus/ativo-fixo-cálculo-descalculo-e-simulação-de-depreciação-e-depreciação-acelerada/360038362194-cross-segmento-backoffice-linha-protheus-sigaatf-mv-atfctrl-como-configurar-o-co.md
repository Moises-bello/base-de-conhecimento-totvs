---
article_id: 360038362194
category: Ativo Fixo - Cálculo, Descalculo e Simulação de Depreciação e Depreciação
  acelerada
content_hash: 1e7f807a16d30c8a519b58c7a569cb54ffbb24e548336b514914bb894cb4ab0e
fetched_at: '2026-06-28T22:41:43.283147+00:00'
product: protheus
section_id: 1500001536401
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - MV_ATFCTRL - Como configurar
  o controle de transações no cálculo de depreciação dos ativos?
type: support-article
updated_at: '2023-11-30T19:15:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038362194-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-MV-ATFCTRL-Como-configurar-o-controle-de-transa%C3%A7%C3%B5es-no-c%C3%A1lculo-de-deprecia%C3%A7%C3%A3o-dos-ativos
---

**Dúvida**Como configurar o controle de transações no cálculo de depreciação dos ativos? **Ambiente**Protheus – Ativo fixo   – A partir da versão 11.80 **Solução**

A configuração do controle de transação é feita através do parâmetro **MV\_ATFCTRL.**

**MV\_ATFCTRL ->**Faz controle de transações para calculo de depreciação dos ativos .

Caso ativado. o parâmetro permite que o inicio do processamento as informações possam ser arquivadas para que em caso de falha possam ser automaticamente restauradas.

**Importante:** Caso este parâmetro esteja ativado  ao realizar o Cálculo Mensal**(ATFA050)** sempre será executada em **TODAS as FILIAIS**

Para maiores informações consulte a documentação técnica completa: <https://tdn.totvs.com/pages/viewpage.action?pageId=514750832>
