---
content_hash: a0f4a8d0bb57c20ad46925beaa74e95dd569e48122e4753567eb83d5b365ec1b
fetched_at: '2026-06-29T00:08:45.574263+00:00'
page_id: '311632309'
product: rm
source: tdn-rm
title: Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=311632309
version: 38
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é esclarecer as funcionalidades da tela de Parâmetros.

# Introdução:

---

       Nesta tela visualizamos e cadastramos os parâmetros utilizados no relatório. Eles poderão ser utilizados como filtros em consultas SQL ou mensagens informativas no relatório. Acesse o documento [Tipos de Parâmetros](https://tdn.totvs.com/x/9BJ0Ig) para mais informações sobre os tipos disponíveis.

Observação

Os parâmetros são utilizados como filtros apenas em Fontes de dados do tipo SQL. No caso de Tabelas, devem ser utilizados [Filtros](http://tdn.totvs.com/x/xyGTEg).

# Como criar:

---

       Para criar um novo parâmetro, basta clicar em "Adicionar" e informar os campos abaixo:

***Nome ***do parâmetro***:***Informe o nome do parâmetro, deve ser um nome único e é por ele que o parâmetro será identificado (Não é permitido espaços ou caracteres especiais no nome do parâmetro, com exceção do underline "\_").

***Descrição:***Informe uma descrição para o parâmetro.

***Tipo:*** Nesse campo o usuário deve informar de qual tipo será o parâmetro (Ex: Alfanumérico, Data/Hora, Decimal, Inteiro, entre outros).

***Valor:*** Informe qual valor o parâmetro irá assumir.

Os parâmetros podem ser salvos sem valores. Quando este parâmetro for utilizado em uma consulta SQL será compreendido o valor “null” em sua execução.

Para campos do tipo "Data/Hora", será automaticamente disponibilizado um calendário para que a data possa ser selecionada.

O valor default para a hora é 00:00:00, mas pode ser alterado manualmente.

***Interno:*** Quando essa opção estiver marcada como "Não", significa que o parâmetro pode receber valores vindos de fora. Caso esteja marcada como "Sim", isso não acontece, o valor será buscado na propriedade "Valor do parâmetro".

Quando a opção "Parâmetro interno" deve ser marcada?

Quando o valor do parâmetro deve ser exclusivamente o valor definido na propriedade "Valor do parâmetro".

Exemplo: Imagine que o Protheus esteja chamando o método “ExecuteReports” via API. Se existir algum parâmetro marcado com essa opção, o Protheus não poderá passar nenhum valor para esse parâmetro. O mesmo será buscado da propriedade “Valor do parâmetro” que está nessa mesma tela.

***Exemplo prático abaixo:***

Em seguida, basta clicar em "Salvar" e vincular o parâmetro à uma consulta SQL na tela [Fonte de Dados](http://tdn.totvs.com/x/uCGTEg).

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.22 ou Superior

false

**Processo:** Parâmetros

falsefalse

**Status:** Concluído

false

**Data:**

false

**Autores:**
