---
content_hash: 9d0930c8a897e547837d200f7d412e1f13ff938d422e9342317195bbba510781
fetched_at: '2026-06-29T00:08:08.438932+00:00'
page_id: '238035005'
product: rm
source: tdn-rm
title: Importacao de Formula Visual com Consulta SQL
type: documentation
url: https://tdn.totvs.com/display/LRM/Importacao+de+Formula+Visual+com+Consulta+SQL
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Este documento objetiva esclarecer o comportamento do sistema durante a importação de uma Fórmula Visual que contenha atividade de consulta SQL como dependência.

# Introdução:

---

      Atualmente, uma fórmula visual na coligada global e sistema "A" (RM Chronus / Totvs Automação de Ponto) com uma atividade contendo consulta SQL vinculada na coligada 1 e sistema "G" (RM Bis / Totvs Serviços Globais), como exemplo.  
   
       Internamente o sistema verifica se a consulta SQL vinculada é uma dependência. Se positivo, automaticamente a importação altera a coligada e o sistema da consulta para o código do objeto "Pai".

      Entendemos que este comportamento é inadequado, pois as referências não são atualizadas, fazendo com que os objetos importados parem de funcionar corretamente.  
   
       Portanto, em virtude deste cenário, foi criada uma opção na importação de Fórmulas Visuais que possibilita a escolha da forma que será feita a importação.

# Exemplificando a Situação:

---

      Para simulação do mencionado, é necessário utilizar uma Fórmula Visual que contenha uma atividade com uma consulta SQL vinculada. Como exemplo, utilizaremos uma Fórmula Visual parametrizada da seguinte forma:

* O opção "Visível a todas as coligadas" deve estar desmarcada;

* Em sua estrutura inclua uma atividade do tipo "Executar Consulta SQL";

* A Consulta SQL vinculada a atividade esta na coligada atual e no Sistema "P" (RM Labore / Totvs Folha de Pagamento), conforme os campos evidenciados;

# Processo de Importação:

---

       Com a implementação desta funcionalidade, durante o processo de importação de objetos gerencias como Fórmulas Visuais, por exemplo. O sistema verificará se o objeto possui Consultas SQL como dependência. Caso positivo, a opção "Importar na Coligada e Sistema Originais da Consulta" será habilitada no registro da consulta:

       

* **Com esta opção Marcada:**  
  A Fórmula Visual será importada no Sistema e Coligada definidos (no caso do exemplo, sistema "G" (RM Bis) e coligada global). A consulta será importada no sistema e coligada definido na criação da consulta (no caso do exemplo, sistema "P" (RM Labore) e coligada 1).

* **Com esta opção Desmarca:**  
  A Fórmula Visual e a Consulta SQL serão importados no Sistema e coligada definidos no processo da importação (no caso do exemplo, ambos serão importados no sistema "G" (RM Bis) e coligada Global).

  Observação

  Como o padrão atual é importar a Consulta SQL na coligada e sistema do Pai, o parâmetro por default estará desmarcado!

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.44 ou Superiores

false

**Processo:** Importação de Fórmula Visual

falsefalse

**Status:** Finalizado

false

**Data:** 02/06/2016

false

**Autores:**
