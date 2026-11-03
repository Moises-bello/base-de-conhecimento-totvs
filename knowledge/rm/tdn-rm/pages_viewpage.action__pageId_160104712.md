---
content_hash: fbac04d031d46abfd92482758e915b890a0f896b9637bd77c37f314ff528321a
fetched_at: '2026-06-29T00:05:56.910824+00:00'
page_id: '160104712'
product: rm
source: tdn-rm
title: Configuração para visualização de cubo no RM Portal - ODBC
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160104712
version: 4
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo desse documento é demonstrar a configuração para visualizar um cubo no RM Portal.

# Procedimentos:

---

   Para configuração da visualização de Cubos no RM Portal siga as orientações abaixo:

* No Painel de Controle | Ferramentas Administrativas, clique na opção **Fontes de dados (ODBC)**;

* Selecione a guia **Fonte de Dados do Sistema** ou **System DSN**, clique em **Adicionar** ou **ADD** para criar uma nova fonte de dados:

* Selecione um driver para o qual deseja configurar uma fonte de dados, em seguida clique em **Concluir:**

Informe o **Nome** da fonte de dados ODBC, obrigatoriamente **CORPORERMCOM**, e o **Servidor** onde a base de dados está localizada, depois clique em **Avançar:**

* Selecione a opção de autenticação do Banco de Dados (Exemplo com SQL Server) com LoginID e Senha fornecidos pelo usuário, informe o **Login ID** e **Senha** **RM/rm**, respectivamente, e clique em **Avançar:**

* Marque a opção **Alterar o Banco de Dados Padrão** e selecione a base de dados desejada, em seguida clique em **Avançar:**

* Marque a opção **Usar configurações regionais ao exibir unidade monetária, números, datas e horas**, em seguida clique Avançar:

* Clique no botão **Testar Fonte de Dados:**

* Clique no botão **OK** após o teste ter sido concluído com sucesso:

* Verifique que o ODBC **CORPORERMCOM** foi criado, em seguida clique no botão **OK** para concluir;

* Nas opções - parâmetros - RM BIS e defina a fonte de dados ODBC conforme abaixo:

 

* Após Configuração acima, é importante verificar as questões abaixo.

Entrar no IIS > selecionar pasta CorporeRM > Propriedades > tipo de MIME

Exclua o .Cube caso tenha.

falsefalse

**Produto:** Framework

false

**Versão:** 11.XX

false

**Processo:** Configuração para visualização de cubo no RM Portal - ODBC

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
