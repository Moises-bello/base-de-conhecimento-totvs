---
content_hash: 4b9c362d2d7bfd90772d2e76821790f1a54eaa11922dfef0df035ea9b5c8c3a8
fetched_at: '2026-06-29T00:08:45.667788+00:00'
page_id: '312153026'
product: rm
source: tdn-rm
title: Exemplo da atividade "Localizar Registro na Tabela"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=312153026
version: 4
---

# Índice:

---

.\*ndice:

# Objetivo

---

     A fórmula visual usada neste exemplo tem como objetivo criar uma coluna na visão do Usuário, preenchida com o retorno de uma consulta SQL.

     Com a atividade FindRecord é possível relacionar o registro corrente da visão e o registro do resultado da consulta através das chaves primárias.

# Exemplo

---

**Insira a atividade Criar Coluna**

     A coluna a ser adicionada na visão de Usuários será a COLUNA\_TESTE.

     Veja mais detalhes sobre a atividade .

**Insira a atividade Executar Consulta SQL**

     É necessário fazer uma Consulta SQL que retorne todos os dados que serão utilizados. Neste exemplo a consulta retornará o código e o nome de todos os usuários.

**Insira a atividade Localizar registro na tabela**

     A atividade de FindRecord (Localizar registro na tabela) deve estar dentro de um foreach para fazer a ligação entre o registro corrente da visão e o registro do resultado da consulta através das PKs;

**Configuração do foreach**:

**Configuração d****a Sequência**:

**Configuração do FindRecord**

     A ligação será feita pela PK CODUSUARIO.

     Tabela: Neste exemplo, a tabela de referência é o resultado da consulta SQL.

     KeyFiels: Os campos chaves para formar o relacionamento entre o resultado da consulta SQL e os registros da visão de usuários. Neste exemplo, o CODUSUARIO. Caso existam mais de um campo, basta separá-los com uma vírgula. Ex.: CODCOLIGADA,IDLAN

     Parâmetros: Após informar o KeyFields, os parâmetros devem ser preenchidos com a PK da visão.

**Insira a atividade Expressão**

     A Expressão irá montar o conteúdo da nova coluna. Neste exemplo a COLUNA\_TESTE será preenchida com o valor "TESTE + NOME DO USUÁRIO".

Veja mais detalhes sobre a atividade .

**Configure o Gatilho**

**Resultado**

     Ao abrir a tela de Usuários, a COLUNA\_TESTE será exibida na visão:

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.17 ou Superior

false

**Processo:** Atividade "Localizar Registro na tabela" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**
