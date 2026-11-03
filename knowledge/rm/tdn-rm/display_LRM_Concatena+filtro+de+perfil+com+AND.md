---
content_hash: a0da0982916c4fade853d4fc9f7fb2fe5c6eeb013275d75f70ab281f3496c2f0
fetched_at: '2026-06-29T00:11:06.229892+00:00'
page_id: '63278118'
product: rm
source: tdn-rm
title: Concatena filtro de perfil com AND
type: documentation
url: https://tdn.totvs.com/display/LRM/Concatena+filtro+de+perfil+com+AND
version: 15
---

# Índice:

---

.\*ndice:

# Objetivo:

---

     Neste post explicaremos a finalidade do parâmetro global “**Concatena filtro de perfil com AND**”. Este parâmetro pode ser ativado nas configurações globais do sistema. As configurações globais estão localizadas em “**Ambiente | Configuração | Parâmetros | Globais**”. No formulário de Parâmetros Globais selecione a guia

# Introdução:

---

          Quando o parâmetro “**Concatena filtro de perfil com AND**” está **DESMARCADO** qual o comportamento do sistema para leitura dos filtros de perfil?

          Imaginemos que o usuário possua dois perfis;

**Perfil A        e        Perfil B**

          Cada um com as seguintes condições;

Perfil **A** ( CODCOLIGADA = 1 )

Perfil **B** ( CODCOLIGADA = 2 )

          Quando executamos uma visão do sistema, a seguinte condição do filtro de perfil é incluída na consulta SQL para retornar os registros.

**AND (** CODCOLIGADA = **1 ) OR (**CODCOLIGADA = **2 )**

          Neste caso, o resultado será a listagem de todos os registros de ambas as coligadas.

---

          Agora vejamos como seria o comportamento nas mesmas condições com o parâmetro “**Concatena filtro de perfil com AND**” **MARCADO**.

          Imaginemos que o usuário possua dois perfis;

**Perfil A        e        Perfil B**

          Cada um com as seguintes condições;

Perfil **A** ( CODCOLIGADA = 1 )

Perfil **B** ( CODCOLIGADA = 2 )

          Quando executamos uma visão do sistema, a seguinte condição do filtro de perfil é incluída na consulta SQL para retornar os registros.

**Obs.:** Note que a condição **OR** foi alterada para **AND**.

**AND (** CODCOLIGADA = **1 ) AND (** CODCOLIGADA = **2 )**

          Nesta condição, o sistema **NÃO** retornará resultado, pois o seu resultado será **false**! Sendo assim em qual situação podemos utilizar o parâmetro marcado?

          Imaginemos que o usuário possua dois perfis;

**Perfil** **A** e**Perfil** **B**

          Cada um com as seguintes condições;

Perfil **A** ( CODCOLIGADA = 1 )

Perfil **B** ( CODFILIAL = 2 )

          Quando executamos o sistema o mesmo irá montar a condição da seguinte forma;

**AND (** CODCOLIGADA = **1 ) AND (** CODFILIAL = **2 )**

          O sistema retornará todas as informações **corretamente** que sejam da **coligada um (1)** e da **filial dois (2)**. Nesta situação, se não tivéssemos a opção de parâmetro **AND** o sistema retornaria todas as filiais de código dois (2), mesmo que estas fossem das coligadas 2, 3, 4 e assim sucessivamente.

---

Para maiores informações:

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).

falsefalse

**Produto:** Framework

false

**Versão:** 11.80.XX ou Superiores

false

**Processo:** Parâmetros Globais / Concatena filtro de perfil com AND

falsefalse

**Status:** Finalizado

false

**Data:** 25/06/2013

false

**Autores:**
