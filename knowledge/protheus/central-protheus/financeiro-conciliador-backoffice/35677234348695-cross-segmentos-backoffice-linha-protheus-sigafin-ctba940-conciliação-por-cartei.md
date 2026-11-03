---
article_id: 35677234348695
category: Financeiro - Conciliador Backoffice
content_hash: 136e905268b3896c3b6f4f867e14e09fce9f60840112ccf75f356a9bea726bae
fetched_at: '2026-06-28T22:37:47.293912+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliação
  por carteira
type: support-article
updated_at: '2026-06-10T13:25:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35677234348695-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Concilia%C3%A7%C3%A3o-por-carteira
---

⏱️Tempo aproximado para leitura: 00:05:00 min

**Dúvida**  
Como realizar a conciliação separadamente em contas a pagar e contas a receber?

**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Financeiro - a partir da release 12.1.2310

**Solução:**

Atualmente, o sistema conta com o **facilitador do filtro “REC/PAG Contido em:”**, que permite ao cliente **definir a carteira desejada** para exibição na conciliação bancária.

Por meio desse filtro, é possível utilizar as variáveis **“R”** (a receber) e **“P”** (a pagar), simplificando a visualização dos registros conforme a carteira selecionada.

No campo **“Rec/Pag está contido em”**, o sistema permite filtrar os movimentos de acordo com a carteira (**FK5\_RECPAG**) que se deseja conciliar, conforme abaixo:

* **Em branco** – exibe todos os movimentos, independente da carteira;
* **R** – exibe somente os movimentos **a receber** do período selecionado;
* **P** – exibe somente os movimentos **a pagar** do período  selecionado.

**Passo a passo:**

1. Acesse a rotina de conciliação (CTBA940);
2. Localize os processos bancários **0023** e **0024**;
3. Informe os **dados obrigatórios** do filtro conforme o cenário desejado;

No campo **“Rec/Pag está contido em”**, selecione a **carteira desejada** (“R”, “P” ou em branco);  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/35677265486615)

**Processe os dados** para que o sistema traga as informações conforme os critérios definidos.

#### **Saiba Mais:**

[**Conciliador BackOffice - Conciliação Bancária Automática**](https://tdn.totvs.com/pages/releaseview.action?pageId=753654798)
