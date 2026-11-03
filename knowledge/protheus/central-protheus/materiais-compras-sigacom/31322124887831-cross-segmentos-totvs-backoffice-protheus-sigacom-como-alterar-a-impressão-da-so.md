---
article_id: 31322124887831
category: Materiais - Compras (SIGACOM)
content_hash: f7bf3535f5543a9e221f839e96159284c03f1a6930adfc865712a2bca70922cc
fetched_at: '2026-06-28T22:41:07.538547+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como alterar a impressão
  da solicitação de compras por um relatório customizado na rotina MATA110 ?
type: support-article
updated_at: '2025-04-10T19:04:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31322124887831-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-alterar-a-impress%C3%A3o-da-solicita%C3%A7%C3%A3o-de-compras-por-um-relat%C3%B3rio-customizado-na-rotina-MATA110
---

**Dúvida**

Como alterar a impressão da solicitação de compras por um relatório customizado na rotina MATA110 ?  
  
**Ambiente**

Protheus – Compras – A partir da 12.1.17

**Solução**

Na rotina solicitação de compras (**MATA110**) a opção de impressão da solicitação de compras disponível através do botão **Outras Ações**->**Imprimir**, por padrão o relatório impresso é o **MATR100**.

Muitos clientes questionam se é possível alterar o relatório impresso ou incluir um relatório customizado ao invés do relatório **MATR100**.

Para utilizar um novo relatório na rotina **MATA110** é possível alterando o nome do relatório através do parâmetro **MV\_SOLIMPR**.

Exemplo de configuração:

Acesse o configurador e siga os seguintes passos:

* Ambiente -> Cadastro -> Parâmetros -> Pesquisar -> MV\_SOLIMPR

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31322134215831)

**IMPORTANTE** :

* Não deve ser informado "U\_" ou  "( )" no conteúdo do parâmetro para que funcione.
* O botão "**Outras Ações->Imprimir Browse"**, é um botão da interface do **Protheus** e não pode ser alterado, pois é existente em quase todas as rotinas e tem a função de realizar a impressão das informações do Browse da rotina em questão.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Fontes de Relatórios de Compras para personalização](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022534771)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
