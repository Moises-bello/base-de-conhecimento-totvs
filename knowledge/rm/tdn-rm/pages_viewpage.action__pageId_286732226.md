---
content_hash: aa69e219b46ed3a65b7d3f041ebd3ee32e23848b5638a25f454951903bf15969
fetched_at: '2026-06-29T00:08:41.509933+00:00'
page_id: '286732226'
product: rm
source: tdn-rm
title: Importação de objeto gerencial contendo consulta SQL como dependência.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286732226
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento objetiva esclarecer o comportamento do sistema durante a importação de um objeto gerencial, como por exemplo: importação de Planilha, Gráfico, Fórmula Visual, Relatório ou qualquer outro objeto gerencial que contenha atividade de consulta SQL como dependência.

# Introdução:

---

      Vamos usar como exemplo, uma Fórmula Visual na coligada global e sistema "A" (RM Chronus / Totvs Automação de Ponto) contendo consulta SQL vinculada na coligada 1 e sistema "G" (RM Bis / Totvs Serviços Globais).

      Internamente o sistema verifica se a consulta SQL vinculada é uma dependência. Se positivo, automaticamente a importação altera a coligada e o sistema da consulta para o código do objeto "Pai".

     Entendemos que este comportamento é inadequado, pois as referências não são atualizadas, fazendo com que os objetos importados parem de funcionar corretamente.

     Portanto, em virtude deste cenário, foi criada uma opção na importação de objetos gerenciais que possibilita a escolha da forma que será feita a importação

# Processo de Importação:

---

       Com a implementação desta funcionalidade, durante o processo de importação de objetos gerencias, o sistema verificará se o objeto possui Consultas SQL como dependência. Caso positivo, a opção "Importar na Coligada e Sistema Originais da Consulta" será habilitada no registro da consulta:

* **Com esta opção Marcada:**  
  O objeto gerencial será importado no Sistema e Coligada definidos (no caso do exemplo, sistema "G" (RM Bis) e coligada global). A consulta será importada no sistema e coligada definido na criação da consulta (no caso do exemplo, sistema "P" (RM Labore) e coligada 1).

  Observação

  Para que o objeto gerencial funcione corretamente ao ser importado e tenha suas referências atualizadas, recomendamos que a opção seja marcada.

* **Com esta opção Desmarcada:**  
  O objeto gerencial e a Consulta SQL serão importados no Sistema e coligada definidos no processo da importação (no caso do exemplo, ambos serão importados no sistema "G" (RM Bis) e coligada Global).

  Observação

  Caso o cliente deseje que todas as suas consultas relacionadas à um determinado módulo (ex: sistema "G" (RM Bis)), fiquem naquele módulo, recomendamos que a opção seja desmarcada.

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Importação de consulta SQL com dependência.

falsefalse

**Status:** Finalizado

false

**Data:** 05/09/2017

false

**Autores:**
