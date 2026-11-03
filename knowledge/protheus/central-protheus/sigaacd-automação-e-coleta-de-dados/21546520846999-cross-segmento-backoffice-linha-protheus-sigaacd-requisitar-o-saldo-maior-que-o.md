---
article_id: 21546520846999
category: SIGAACD - Automação e Coleta de Dados
content_hash: 0bb6c4c97643530ee9464ac28fd596794b45c0f9e742588be45d93ffe9100cf0
fetched_at: '2026-06-28T22:39:13.897463+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAACD- Requisitar o saldo
  maior que o empenho. '
type: support-article
updated_at: '2024-02-22T18:18:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21546520846999-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Requisitar-o-saldo-maior-que-o-empenho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21546491400343) Tempo aproximado para leitura: **00:01:00min****Dúvida**

Na rotina **Requisição(ACDV040)**ao Requisitar um saldo informado uma Ordem de produção(D3\_OP) quando a quantidade empenhada é maior apresenta o HELP **" A quantidade da requisição é maior que o saldo empenhado deste produto para esta OP. Ao requisitar está quantidade o empenho não sera baixado"** Qual o conceito?   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/21546491402007)  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -Estoque/Custos - Todas as versões.  
  
**Solução**

O Help é apresentado quando utiliza um Tipo de Movimentação com o campo Atualiza Empenho **(F5\_ATUEMP) igual a Sim**, nesse caso é um alerta que a operação Devolve ou Requisita com saldo maior que a quantidade empenhada na OP.

Ao fazer uma requisição superior ao saldo empenhado na Ordem de Produção na tabela **SD4,** Nota que se trata apenas de um alerta ou aviso que não impede a operação de realizar a requisição pelo coletor. Por tanto **não se trata de um erro no sistema.**

Segue uma lista de **Pontos de Entrada** para possibilidade de customizar, conforme sua necessidade.

[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV040 - Pontos de entrada da rotina Requisição de Materias por OP/ Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14507268839447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV040-Pontos-de-entrada-da-rotina-Requisi%C3%A7%C3%A3o-de-Materias-por-OP-Centro-de-Custo#:~:text=Quais%20s%C3%A3o%20os%20Pontos%20de,rotina%20de%20Requisi%C3%A7%C3%A3o%20(ACDV040)%3F&text=Cross%20Segmento%20%2D%20TOTVS%20Backoffice%20(Linha,%2FCustos%20%2D%20Todas%20as%20vers%C3%B5es.)

**CBRETEAN - Informa dados das Etiquetas**

<https://tdn.totvs.com/pages/releaseview.action?pageId=6091038>

**Saiba Mais:**

*[Clique aqui e veja mais artigos sobre SIGAACD - Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
