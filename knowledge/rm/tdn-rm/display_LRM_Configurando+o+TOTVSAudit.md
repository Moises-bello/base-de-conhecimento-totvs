---
content_hash: 706b8a2942808eba02d1182d8936c820ef078b826338ec6d73b7cf5bbb3ca9b3
fetched_at: '2026-06-29T00:11:11.093445+00:00'
page_id: '645474984'
product: rm
source: tdn-rm
title: Configurando o TOTVSAudit
type: documentation
url: https://tdn.totvs.com/display/LRM/Configurando+o+TOTVSAudit
version: 4
---

Após a execução do assistente do TOTVS Audit ser executado com sucesso, o usuário deverá acessar

* **Acessar Serviços Globais/ Administração/ Log de Auditoria - Configurações**

* **Após realizado os passos acima, aparecerá a tela do Log de Auditoria.**

* **Nesta tela escolhemos a tabela que queremos auditar e pressionamos CTRL + F para localizar a tabela ou, se preferir, busque a mesma na lista de tabelas. Feito isso, escolhemos qual o tipo de auditoria deverá ser realizado.**

1. Update – serve para quando um registro é alterado na tabela.
2. Delete – serve para quando um registro é excluído da tabela.
3. Insert – serve para quando um registro é inserido na tabela.

* **Após a marcação das tabelas, deve pressionar o botão "Salvar e Configurar TOTVS Audit" e  inicia-se o configurador e realiza-se os passos para a configuração do TOTVSAudit;**

Tabelas auditadas automaticamente

As tabelas abaixo são auditadas automaticamente, o flag de auditoria virá marcado default.

ZAUDITCONFIG  
ZAUDITCONFIGHISTORICOEXECUCAO  
ZAUDITEXCEPTION  
ZAUDITITEMS  
ZAUDITPENDCHANGES  
GDIC  
GDICDATAPROTECTION

**Trabalhando com exceções:**

Caso 1:  Cadastrando uma exceção para uma ou mais colunas de uma tabela:

Coloque a tabela no domínio e marque qual coluna você quer que seja exceção.

No nosso exemplo, qualquer alteração feita no campo "NOME", não será registrada pela auditoria.

Alterei o nome de um campo já existente.

Em log de alterações na aba do log de auditoria.

Filtrando por objeto.

Não ocorreu registro de alteração conforme esperado.

Caso 2:  Cadastrando uma exceção para o "Cadastro de Calendários", por exemplo:

Esta configuração nos permite não mais registrar alterações feitas diretamente no cadastro de calendários, contudo ações feitas diretamente no banco ou se o calendário for submetido a outros processos da aplicação, tais informações serão gravadas.

Confirmando via banco de dados que o delete foi registrado quando feito pelo Management:
