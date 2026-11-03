---
content_hash: d0dd7b845ea1ec69acf75671eb4f1286d8e10937adc63977cf34a7fe5269e90c
fetched_at: '2026-06-29T00:08:16.226584+00:00'
page_id: '244930613'
product: rm
source: tdn-rm
title: Segurança por linha e por coluna na Consulta SQL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244930613
version: 34
---

# Índice:

---

.\*ndice:

# Objetivo:

---

        Mostrar como e porque utilizar as configurações "Não considerar segurança por linha" e "Não considerar segurança por coluna", disponíveis no cadastro de Consultas SQL.

# Introdução:

---

        A aplicação de segurança em consultas SQL ocorre da seguinte forma:

* **Segurança por linha**: é aplicada mediante o cadastro de [Filtro por Perfil/Usuário](https://tdn.totvs.com/x/68vSHg).
* **Segurança por coluna**: refere-se à configuração de Acesso a Campos, definida em Perfis.

        Na tela de cadastro de consultas SQL é possível determinar, para cada consulta, se ela deve considerar ou não a segurança por perfil/usuário ou segurança de campos. Basta marcar as opções:

**Não considerar segurança por linha:** Quando marcada, a Consulta SQL será executada para todos os usuários, independente da segurança por perfil ou por usuário configurada.

**Não considerar segurança por coluna:** Quando marcada, a Consulta SQL será executada sem validar a segurança de acesso a campos configurada no perfil do usuário logado.

   

Limitação na aplicação de Segurança

* Para que os filtros de segurança sejam aplicados corretamente é requerido que a query utilizada viabilize a identificação das tabelas e colunas de Origem. Operações SQL como **UNION ALL** podem afetar a capacidade de se identificar com sucesso a origem do dado projetado no select.

* Pode ser aplicada segurança por usuário/perfil à [views](https://www.w3schools.com/sql/sql_view.asp), porém a utilização de **UNION ALL com views** ***não é suportada*** pois, por não viabilizar a identificação das colunas/tabela de origem, a aplicação de segurança é impossibilitada.

* A partir da versão 12.1.23 o sistema aceita Alias em colunas projetadas. O sistema proritariamente buscará colunas projetadas com o nome configurado no filtro por perfil/usuário para aplicação de segurança. Caso não seja encontrada nenhuma coluna projetada com o nome dos campos utilizados nos campos de expressão de filtro de segurança, o sistema então buscará identificar as colunas-origem de cada coluna projetada e escolherá a primeira que possuir o mesmo nome do filtro de expressão.

* A partir da versão 12.1.23.284, resultados de funções, tais como ***pipes** ( **| |** ), **CONCAT,****CASE**, **DECODE**, **LPAD*** entre outros ***não sofrerão aplicação de segurança***. O sistema cobrará a inclusão do campo fora desta função para aplicação da segurança, semelhante ao funcionamento da segurança para o campo [CODCOLIGADA](https://tdn.totvs.com/x/vARsEw).

  Abaixo estão descritos alguns exemplos dessas configurações.

# Configuração: Não considerar segurança por linha

---

        Para exemplificarmos essa configuração, foi criado um usuário 'segurancaSQL' associado ao perfil 'TesteSQL'. Ao criarmos o usuário, configuramos o seguinte filtro: chapa <> 00001, conforme imagem abaixo:

      Veja abaixo a consulta SQL que será utilizada neste exemplo:

sql

     A seguir, foram descritas as diferenças entre utilizar ou não esta configuração:

falseSegurança por Linha'Não considerar segurança por linha' desmarcado'Não considerar segurança por linha' desmarcado'Não considerar segurança por linha' desmarcado

        Considerando a seguinte consulta, com o campo '**Não considerar segurança por linha**' desmarcado:

        Após logar no sistema com o usuário segurancaSQL e executar a consulta criada anteriormente, todos os funcionários solicitados no select serão retornadas, **exceto** o de chapa = 00001, pois o filtro de perfil e de usuário **serão** **considerados:**

'Não considerar segurança por linha' marcado'Não considerar segurança por linha' marcado'Não considerar segurança por linha' marcado

        Se criarmos uma consulta idêntica à consulta anterior, porém com o campo '**Não considerar segurança por linha**' marcado, os filtros configurados no perfil ou em usuário, não serão considerados e o usuário logado conseguirá visualizar todos os registros da consulta.

        Após logar no sistema com o usuário ConsultaSQL e executar essa consulta, todos os registros solicitados no select serão retornadas, inclusive o registro de chapa = 00001, pois filtros por perfil e filtros por usuário **não** serão considerados:

# Configuração: Não considerar segurança por coluna

---

      Para exemplificarmos essa configuração, foi criado um usuário 'Teste' associado ao perfil 'SegColuna'. Ao criarmos o perfil, configuramos a seguinte restrição a campos: Não pode consultar, nem alterar o campo CODFUNCAO, da tabela PFUNC, conforme imagem abaixo:

      Veja abaixo a consulta SQL que será utilizada neste exemplo:

sql

     A seguir, foram descritas as diferenças entre utilizar ou não esta configuração:

falseSegurança por Coluna'Não considerar segurança por coluna' desmarcado'Não considerar segurança por coluna' desmarcado'Não considerar segurança por coluna' desmarcado

        Considerando a seguinte consulta, com o campo '**Não considerar segurança por coluna**' desmarcado:

        Após logar no sistema com o usuário Teste e executar a consulta criada anteriormente, todas as colunas solicitadas no select serão retornadas, **exceto** CODFUNCAO, pois a permissão configurada nos campos do perfil **será** **considerada:**

'Não considerar segurança por coluna' marcado'Não considerar segurança por coluna' marcado'Não considerar segurança por coluna' marcado

        Se criarmos uma consulta idêntica à consulta anterior, porém com o campo '**Não considerar segurança por coluna**' marcado, as configurações feitas no perfil, em acesso a campos, não serão consideradas e o usuário logado conseguirá visualizar todas as colunas da consulta.

        Após logar no sistema com o usuário Teste e executar essa consulta, todas as colunas solicitadas no select serão retornadas, inclusive CODFUNCAO, pois a configuração de acesso a campos do perfil **não** será considerada:

falsefalse

**Produto:** Framework

false

**Versão:** 11.82.XX e 12.1.XX

false

**Processo:** Configurar Segurança por linha e por coluna na Consulta SQL

falsefalse

**Status:** Finalizado

false

**Data:** 29/08/2016

false

**Autores:**
