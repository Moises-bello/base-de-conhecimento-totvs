---
content_hash: 22fecc386da130d8c3a2b8c65c6f9392a1595c84035350c4c370e43b644963e1
fetched_at: '2026-06-29T00:09:35.944265+00:00'
page_id: '425459446'
product: rm
source: tdn-rm
title: Criar Fonte de Dados ODBC
type: documentation
url: https://tdn.totvs.com/display/LRM/Criar+Fonte+de+Dados+ODBC
version: 9
---

**Criar Fonte de Dados ODBC**

---

O ODBC é uma interface de programação que permite que os aplicativos acessem dados em sistemas de gerenciamento de bancos de dados que usam a linguagem sql como padrão de acesso a dados

**Criando uma fonte de dados ODBC**

Acesse o executar do Windows e digite o comando abaixo de acordo com a versão do DBAccess instalado no servidor onde está instalado o TOTVS Protheus

* **32 bits:** %systemdrive%\Windows\SysWoW64\odbcad32.exe
* **64 bits:** %systemdrive%\Windows\System32.

**1**- Acesse a aba **[DSN do Sistema]**

**2**- Clique em [incluir]

**3**- Selecione o driver **[Sql Server]** e clique em concluir

**4**- Informe os campos abaixo e clique em **[Avançar]:**

• **Nome:** Nome da base de dados que o odbc atenderá

• **Descrição**

• **Servidor:** Servidor onde a base de dados está localizada

**5**- Selecione a opção:  **[Com autenticação do Sql Server usando id de logon e senha inseridos pelo usuário]**

**6**- Informe os campos a seguir e clique em [avançar]:

• **Conectar-se ao Sql Server para obter as configurações padrão das opções de configuração adicionais**: checkbox selecionado

• **Id de logon:** SA

• **Senha:** Senha do SA do Sql Server

Selecione o checkbox [**Alterar banco de dados padrão para** e informe o banco de dados no comboBox localizado logo abaixo do checkbox.

Após clicar em **[Avançar]**, clique em **[Concluir]**

Clique em **[Testar Fonte de Dados]**. Se a mensagem \*+"testes concluídos com êxito!"+\* for exibida, as configurações foram executadas com sucesso

Clique em **[Ok]** até finalizar o wizard de configuração da fonte de dados ODBC
