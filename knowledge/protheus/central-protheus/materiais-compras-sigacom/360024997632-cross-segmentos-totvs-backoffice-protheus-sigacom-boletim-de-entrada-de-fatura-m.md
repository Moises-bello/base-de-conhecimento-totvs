---
article_id: 360024997632
category: Materiais - Compras (SIGACOM)
content_hash: 75141b61de8a417581b9c9fec0a282bb42d3e0eb8091196dcc5f9fa90a20cae5
fetched_at: '2026-06-28T22:41:07.476148+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Boletim de Entrada
  de Fatura (MATR170)
type: support-article
updated_at: '2025-05-06T16:48:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024997632-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Boletim-de-Entrada-de-Fatura-MATR170
---

**Dúvida**Orientações sobre o Relatório "Boletim de Entrada" (MATR170)

**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Solução:**

1) No relatório de Boletim de Entrada (**MATR170**), por qual motivo no tipo de impressão "Planilha", não está disponível no "Tipo de Planilha", a opção "Formato de Tabela"?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16969727275927)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16969658060311)

A disposição do layout de impressão do relatório do Boletim de Entrada de Fatura, não foi desenvolvida para atender a essa finalidade, diante disso a mesma não está disponível no fonte padrão.

Abaixo artigo link de disponível com informação:

[PCOM18002 - MATR170 | Não funciona em planilha excel - formato tabela](https://tdn.totvs.com/x/Lw4wGg)

2) Para que o layout do relatório visualizado pelo **MATA103** **> Outras Ações > Imprimir** apresente algumas informações ex: "Ordem dos itens do documento de entrada" Deve ser colocado no parâmetro de configuração dentro da rotina do relatório. Segue:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409627222423)![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409640997143)

Após colocar suas preferencias de como quer que o Boletim seja apresentado salvar, e entrar via rotina e posicionar no documento que deseja imprimir:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409641051671)

3) Na rotina Documento de Entrada (**MATA103**) a opção de impressão do boletim de entrada disponível através do botão **Ações** **Relacionadas**\**Imprimir**, por padrão o relatório impresso é o **MATR170**.

Muitos clientes questionam se é possível alterar o relatório impresso ou incluir um relatório customizado ao invés do relatório **MATR170.**

Para utilizar um novo relatório na rotina **MATA170** é possível alterando o nome do relatório através do parâmetro **MV\_PIMPNFE**.

4) Significado das Siglas da Coluna Div do Relatório MATR170 , segue na documentação a seguir -  [PCOM170001 - Informações coluna Div (Divergência)](https://tdn.totvs.com/pages/releaseview.action?pageId=940291796)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
