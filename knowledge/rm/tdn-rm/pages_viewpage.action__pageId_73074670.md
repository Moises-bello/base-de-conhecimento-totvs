---
content_hash: 82dd314bd8bedc36b09822cdcc22b7c525027997e6c54e58681d456c36b7305c
fetched_at: '2026-06-29T00:11:28.342410+00:00'
page_id: '73074670'
product: rm
source: tdn-rm
title: Configurações ODBC - Server 2008 & Seven
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73074670
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | RM Portal                    **Versão:**11.00 |
| **Processo** | **:** | Geração de Cubos via RM Portal |
| **Subprocesso** | **:** | Configurações ODBC - Server 2008 & Seven |
| **Data da publicação** | **:** | 26/07/2013 |

**Para** **que** **seja** **possível** **gerar** **Cubos.Net** **e Delphi** **através** **do** **RM** **Portal** **se** **torna necessário** **a** **criação** **do** **Tipe** **Mime** **DCube.**

**Para** **criar** **este** **Tipe** **Mime,** **acesse** **o servidor** **onde** **está** **instalado** **o** **RM** **Portal** **e clique** **no** **botão** **"Iniciar"** **e** **digite** **o comando** **"IIS".** **Na** **tela** **principal** **do** **seu** **IIS** **selecione** **a** **conexão principal do seu IIS e dê dois cliques no ícone "Tipos de MIME" no grupo "IIS".**

**Será** **listado** **na** **tale** **seguinte** **os** **Mimes** **já** **existentes.** **Clique** **com** **o** **botão** **direito** **do mouse** **em** **uma** **superfície** **qualquer** **da** **visão.** **Clique** **na** **opção** **"Adicionar"** **que** **será apresentada.**  
   
   
   
   
 **Preencha** **os** **campos** **conforme** **exemplo** **abaixo** **na** **adição** **do** **MIME.**

**Depois** **de** **criado** **o Tipo** **Mime** **DCube** **clique** **no** **botão** **"Iniciar"** **e digite** **o comando "ODBC"** **(sem** **aspas).** **Será** **apresentada** **o** **formulário** **"Administrador** **de** **fonte** **de** **dados ODBC". Para criamos a fonte de dados DCube clique no botão "Adicionar".**

**Selecione** **em** **seguida** **qual** **o drive** **de** **conexão** **referencia** **o seu** **SGBD** **(Baco** **de** **Dados Oracle ou SQL). No exemplo abaixo estarei escolhendo a opção "SQL Server". Clique em** **"Concluir".**

**No** **formulário** **seguinte** **preencha** **as** **informações** **solicitadas** **para** **o nome** **e descrição da** **fonte** **de** **dados** **ODBC** **que** **você** **irá** **criar.** **No** **exemplo** **abaixo atribuí** **a** **mesma nomenclatura** **do** **MIME** **criado** **anteriormente.** **Na** **ultima** **opção** **especifique** **escolha** **na aba** **o seu** **servidor** **de** **Banco** **de** **dados.** **Depois** **de** **preenchido** **as** **informações** **e selecionado** **o servidor** **clique** **em** **"Avançar".**

**No** **formulário** **seguinte** **você** **deverá** **desmarcar** **a** **opção** **"Com** **autenticação** **do** **Windows** **NT** **usando** **ident.** **De** **login** **na** **rede."** **e** **marcar** **a** **opção** **"Com** **autenticação** **do** **SQL** **Server usando** **Ident.** **De** **login** **e senha** **inseridos** **pelo** **usuário".** **Especifique** **o usuário** **e** **senha**  
 **de** **conexão** **com** **o** **seu** **banco** **de** **dados.** **Clique** **em** **"Avançar".**   
   
   
   
 **No** **formulário** **seguinte** **as** **informações** **deverão** **estar** **conforme** **exemplo** **abaixo.** **Clique** **em** **"Avançar".**  
   
   
   
 **Novamente** **as** **informações** **deverão** **ser** **default.** **Clique** **em** **"Concluir".**

**Teste** **a** **conexão** **ODBC** **na** **próxima** **etapa.**

**Tendo** **êxito** **na** **conexão** **clique** **no** **botão** **"OK".** **E** **ok** **novamente** **no** **formulário** **de** **testes de** **conexão.**

**Clique** **em** **OK** **para** **finalizar** **a** **criação** **da** **conexão** **ODBC.**   
   
   
   
   
   
 **Em** **seguida** **você** **deverá** **acessar** **o aplicativo** **"RM** **Bis".** **Ir** **ao** **menu** **"Opções** **| Parâmetros** **| RM** **Bis".**

**E** **defina** **o nome** **da** **conexão** **ODBC** **criada.** **No** **nosso** **exemplo** **"DCube".** **Salve** **as alterações** **e tente** **gerar** **o Cubo** **novamente** **no** **RM** **Porta.**
