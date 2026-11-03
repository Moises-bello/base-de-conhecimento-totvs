---
content_hash: 6e4e422b66c56c33d2784db3da343a6eaaf5cbe3237c6eeb3d6d8c70bd683af2
fetched_at: '2026-06-29T00:11:11.198393+00:00'
page_id: '64651469'
product: rm
source: tdn-rm
title: Conversão de Cubo Delphi para .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=64651469
version: 4
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   Esse documento tem como intuito descrever o processo de conversão de Cubos Delphi para .Net.

# Conversão de Cubos:

---

    Esse procedimento pode ser realizado pelo Módulo Inteligência de Negócios da Nova MDI ou pelo RM BIS em Delphi. Para esse documento, será realizado via Nova MDI.

    Na aba Gestão Estratégica, do módulo Inteligência de Negócios, acesse o menu de cubos e aplique o filtro de acordo com sua preferência. No exemplo abaixo, foi utilizado o Filtro de onde o Código da Categoria é igual a 4.

     Na tela de Cubos, através do Menu de Processos, clique em assistente de conversão de Cubos Delphi.

   
    Após acessar esse Menu, será exibida uma tela com todos os Cubos Delphi da base de dados, onde basta escolher qual ou quais cubos serão convertidos nesse processo. Nesse exemplo, optei por converter apenas o Cubo FluxoDeCaixa.

     Ao clicar em executar, o Processo de conversão será iniciado.

     Processo concluído com êxito:

     Reparem que no Log do processo, o cubo foi convertido para Categoria código 18 (Financeiro). Após alterar o filtro da tela de Categoria 4 para Categoria 18, o cubo foi visualizado.

     Cubo executado:

Existe uma restrição a esse procedimento de conversão. Por se tratar de uma ferramenta Delhpi e essa linguagem não ser homologada para ambientes 64 bits, essa conversão deve ser realizada em estações 32 bits.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conversão de Cubos Delphi para .Net

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
