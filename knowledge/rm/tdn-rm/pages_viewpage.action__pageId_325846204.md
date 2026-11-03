---
content_hash: 68114dcdd42255512bb37e773b92b16051d958bbeff7e373094f31e2b80df585
fetched_at: '2026-06-29T00:08:48.146418+00:00'
page_id: '325846204'
product: rm
source: tdn-rm
title: Segurança por Usuário - Coligada
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=325846204
version: 11
---

# Índice:

---

.\*ndice:

# Objetivo:

---

      Esse documento tem como objetivo trazer uma visão do que é e como funciona o parâmetro de "Filtrar resultado por coligada permitidas para o usuário".

# Introdução:

---

     Na tela de Parâmetro Globais, aba de Consultas SQL é possível marcar a opção "Filtrar resultado por coligada permitidas para o usuário".

Essa opção vem por default desmarcada.

       Abaixo explicaremos melhor as funcionalidades dessa opção marcada ou desmarcada.

# Opção desmarcada:

---

       Com a opção desmarcada, ao executar qualquer consulta SQL, o usuário terá acesso aos dados de todas as coligadas, independente dele ter acesso à elas ou não.

       Por exemplo:

       O usuário "A" só tem acesso à Coligada 7, porém ao executar uma consulta SQL que retorne dados de coligadas, ele terá acesso aos dados de todas as coligadas.

# Opção marcada:

---

        Caso a opção esteja marcada, ao executar uma consulta SQL contendo o campo "CODCOLIGADA", os resultados retornados serão somente referentes às coligadas que o usuário tem acesso.

       Por exemplo:

       O usuário "A" só tem acesso à Coligada 7 executa a consulta:

***SELECT CODCOLIAGADA, NOME, CHAPA FROM PFUNC***

       Os resultados obtidos serão referentes somente aos funcionários da Coligada 7.

Consulta sem o campo "CODCOLIGADA"

Ao tentar salvar uma consulta sem o campo CODCOLIGADA, a seguinte mensagem de aviso será exibida, informando que a segurança não será aplicada:

Caso o mesmo Usuário "A" execute a seguinte consulta:

***SELECT NOME, CHAPA FROM PFUNC***

Como a consulta não trás o campo "CODCOLIGADA", os resultados não serão filtrados e os dados de todas as coligadas serão mostrados.

O mesmo ocorre ao executar uma consulta com uma tabela que não possui o campo "CODCOLIGADA", como por exemplo, PPESSOA.

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.19 ou Superior

false

**Processo:** Visões de Dados

falsefalse

**Status:** Pendente

false

**Data:** 22/12/2017

false

**Autores:**
