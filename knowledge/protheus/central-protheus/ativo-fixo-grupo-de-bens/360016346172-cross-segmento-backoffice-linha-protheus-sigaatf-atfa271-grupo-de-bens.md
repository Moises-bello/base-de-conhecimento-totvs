---
article_id: 360016346172
category: Ativo Fixo - Grupo de Bens
content_hash: 9389fdf55245309f452206d46ab6a069f10002d5a9f348b74e56937292ed15b0
fetched_at: '2026-06-28T22:41:41.094427+00:00'
product: protheus
section_id: 1500001536521
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF- ATFA271 Grupo de Bens
type: support-article
updated_at: '2023-05-24T17:51:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016346172-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA271-Grupo-de-Bens
---

**Dúvida**Como cadastrar Grupo de Bens no ativo fixo ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Ativo Fixo - Todas as versões

**Solução**

Esta rotina permite adicionar os dados contábeis do bem e também um conjunto padrão de sistemas de cálculo, como por exemplo tipo de ativo associado a método de depreciação, a taxa anual, além de agrupar os bens, facilita o preenchimento da ficha de um bem em Ativos que é exibido no momento da inclusão.

**Procedimentos**

Para Incluir um Grupo de Bens:

1. Em **Grupo de Bens** clique em**Incluir**.
2. O sistema apresenta a tela de Cadastro de Grupo de Bens. Note que a tela esta divida em duas partes:
   * **Cabeçalho (campos)**: com os campos relacionados ao **Código do Grupo**, **Descrição** e **Dados Contábeis**;
   * **Itens (Grid)**: . com os campos referentes aos sistemas de cálculo (tipo de ativo associado a método de depreciação, a taxa anual).
   * Para os itens pode ser cadastrado um único item do tipo 01 – Aquisição e um ou mais itens do Tipo 10 – Depreciação Fiscal/Gerencial, sendo estes com o **Tipo de Saldo** diferente.
3. Confira os dados e  **Confirme**.

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14816101579159)

 Informações relacionadas ao compartilhamento das tabelas SNG e FNG do cadastro de grupos

* **Ao informar código de Grupo através da classificação (ATFA240) de um bem o sistema não gatilha as informações**
* **Ao informar código de Grupo através do cadastro (ATFA012) de um bem o sistema não gatilha as informações**

* Necessário que as tabelas FNG e SNG tenham o mesmo compartilhamento
* Necessário que "SNG - Grupo de Bens " e "FNG -Itens  do Grupo de Bens" estejam populadas
* Ao informar no cadastro os dados "Grupo  De Bens" o Sistema Irá gatilhar para  "Itens do Grupo de Bens

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012502171/mceclip0.png)
