---
content_hash: 022ebbe9e98bfb6960980388cec6a96e3719aa10246198c3ffcadc99c0a11cc7
fetched_at: '2026-06-29T00:10:32.448424+00:00'
page_id: '525815085'
product: rm
source: tdn-rm
title: Registros por Transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=525815085
version: 2
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Este documento tem por finalidade esclarecer a funcionalidade da propriedade “Registros por Transação”

# Introdução:

---

       Ao criarmos uma conexão de “Destino” em um conceito, em suas propriedades há a opção “Registros por Transação”. Esta propriedade tem por finalidade definir o número de "blocos" de execução para que o usuário possa controlar o lote de inserção em caso de possíveis erros.

       O ***seu valor default é 0 o que faz com que o os valores sejam tratados como um único bloco*** e em caso de erro nenhum registro irá persistir. Caso o usuário altere esse valor o conceito passará a trabalhar com blocos de acordo com o valor definido na propriedade.

false

       Para exemplificarmos as variações desta propriedade, vamos utilizar a seguinte estrutura de um arquivo txt:

       01;Conceito - Novo 01;1;Acesso01  
       02;Conceito - Novo 02;2;Acesso02  
       03;Conceito - Novo 03;3;Acesso03  
       04;Conceito - Novo 04;4;Acesso04  
       05;Conceito - Novo 05;5;Acesso05  
       06;Conceito - Novo 06;6;Acesso06  
       07;Conceito - Novo 07;7;Acesso07  
       08;Conceito - Novo 08;8;Acesso08  
       09;Conceito - Novo 09;9;Acesso09  
       10;Conceito - Novo 10;10;Acesso10

Exemplos de Valores1Alterando seu valor para 2

       Caso o usuário altere o valor padrão do campo para 2 o conceito irá agrupar os dados acima em 5 grupos de 2 itens:

**Grupo01**:  
01;Conceito - Novo 01;1;Acesso01  
02;Conceito - Novo 02;2;Acesso02  
  
**Grupo02**:  
03;Conceito - Novo 03;3;Acesso03  
04;Conceito - Novo 04;4;Acesso04  
  
**Grupo03: - ERRO**  
05;Conceito - Novo 05;5;Acesso05  
06;Conceito - Novo 06;6;Acesso06  
  
**Grupo04**:  
07;Conceito - Novo 07;7;Acesso07  
08;Conceito - Novo 08;8;Acesso08  
  
**Grupo05:**  
09;Conceito - Novo 09;9;Acesso09  
10;Conceito - Novo 10;10;Acesso10

false

Caso o grupo 3 apresente erro, não irá afetar os registros que já foram salvos anteriormente. Mas todos os registros do grupo 3 não serão atualizados.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Propriedade Registros por Transação - Novo Conceito

falsefalse

**Status:** Finalizado

false

**Data:** 

false

**Autores:**
