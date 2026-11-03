---
content_hash: a4ee1f2a38cdd691e2d07a46dacb93ff818d5d5ef10fa77fd67bde31aaa9fef6
fetched_at: '2026-06-29T00:09:37.486928+00:00'
page_id: '425459618'
product: rm
source: tdn-rm
title: TOTVS Business Connect - Conexões Origem
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459618
version: 2
---

**Conexões Origem**

---

Na aba Conexões Origem são criadas as conexões com a aplicação origem. Ao criar uma conexão, é necessário informar o nome da mesma e o tipo e preencher os dados correspondentes.

A conexão de origem pode ser do tipo:

* Arquivo Texto
* Arquivo XML
* Banco de Dados
* Data Server RM.Net
* MS CRM (Microsoft CRM)
* Web Service

No quadro abaixo seguem mais detalhes sobre cada uma das conexões de origem.  
    
 ***Nota:****Sentenças personalizadas só podem ser utilizadas em conexões de banco de dados na origem.*

|  |  |
| --- | --- |
| **Arquivo Texto** | * **Nome:** Nome para identificar a estrutura que está sendo criada. É aconselhável preencher com o nome da tabela, para facilitar a identificação. * **Continuar execução em caso de erros**: O processamento continua caso algum erro seja apresentado. * **Tipo de Arquivo:** Arquivo separado por delimitador ou Arquivo de tamanho fixo. Quando o tamanho dos campos for fixo (sem delimitador), é necessário ao informar o conjunto de tabelas e criar os campos, configurar o parâmetro "Tamanho" referente ao campo que está sendo criado. * **Delimitador**: Caracteres ou conjunto de caracteres que marca o limite entre dois campos. Caso o caractere seja de tabulação, deve se digitar 'TAB'. * **Arquivo:** Nome do arquivo que deve alimentar a conexão. |
| **Arquivo XML** | Na conexão do tipo Arquivo XML estão disponíveis para parametrização os campos:   * **Texto XSD:** Informe o texto schema no formato XSD. Ao clicar no lookup para informar o texto XSD é aberta uma visão na qual é possível digitar o texto schema, ou abrir o arquivo XSD para que o texto seja carregado. * **Arquivo XML:** Informe o caminho completo e o nome do arquivo XML. * **Tabela Principal:** Selecione a tabela principal, apenas para conexão de origem. * **Nó Raiz**: Caso a consulta de origem tenha como retorno múltiplo registros, informe neste campo o nó raiz. |
| **Banco**   **de Dados** | **Nome:** Nome para identificar a estrutura de banco de dados que está sendo criada.   *Flag´s:*   * **Permitir atualização dos registros:** Atualiza registros se necessário. * **Continuar execução em caso de erros:** Permite que o processo continue sendo executado em caso de erros.         *Aba Conexão* * **Provedor:** Informe o provedor de acesso ao banco de dados. * **Suporta Transações:** Informe se o banco de dados suporta transações. * **Testar:** Testa se as informações do banco de dados estão corretas. * **Conexão:** Informe os dados do banco de dados e o servidor.         *Aba Tabelas*   Pode ser utilizada uma **tabela** ou uma **setença SQL**.   Quando for uma setença, O nome deve sempre começar com 'qry\_' .       *Aba Parâmetros* * **Sem Filtro:** Não realiza nenhuma seleção prévia dos registros. * **Parâmetro:** Utiliza o parâmetro para realizar seleção dos registros. * **Fixo:** Utiliza filtro fixo para selecionar os registros. |
| **Data**   **Server RM.Net** | * **Nome:** Nome para identificar a estrutura do Data Server que está sendo criada.     *Flag´s:* * **Permitir atualização dos registros:** Atualiza registros se necessário. * **Continuar execução em caso de erros:** Permite que o processo continue sendo executado em caso de erros.     *Aba Conexão* * **Servidor:** Informe o nome do Data Server a ser utilizado pela conexão. * **Owner Data:** Informe o owner data. * **Usar conexão padrão:** utiliza a conexão em ativo. * **Alias:** Informe o alias do CORPORE que deve representar o processo de importação. Este Alias já deve ser previamente cadastro (no Alias Manager ou no módulo de Globais). * **Usuário:** Informe nome do usuário do CORPORE que deve representar o processo de importação. * **Senha:** Informe a senha de autenticação ao CORPORE. * **Usar contexto padrão:** Informe se o Data Server irá utilizar a conexão corrente, atribuindo o valor "True". Caso contrário (valor igual a "False"), os campos Usuário CORPORE, Senha do CORPORE e Alias CORPORE devem ser preenchidos. * **Contexto:** Permite selecionar manualmente a Chapa do Funcionário, Coligada, Filial, Código Externo, Sistema, Unidade, Usuário, Usuário de Serviço, Data, Exercício Fiscal entre outros.     *Aba Parâmetros* * **Sem Filtro:** Não realiza nenhuma seleção prévia dos registros. * **Parâmetro:** Utiliza o parâmetro para realizar seleção dos registros. * **Fixo:** Utiliza filtro fixo para selecionar os registros. |
| **MS CRM**   **(Microsoft**   **CRM)** | A conexão do tipo MS CRM deve ter configurados os seguintes campos:   * **Server URL:** Informe o endereço da conexão, por exemplo: <http://crmserver> * **Domínio:** Informe o nome do domínio. * **Usuário:** Informe o nome do usuário do CRM. * **Senha:** Informe a senha do usuário CRM. * **Organização:** Informe o nome da organização para integração. * **Entidade CRM:** Informe o nome da entidade CRM. * **ID CRM:** Informe o nome do identificador de registro da entidade do CRM. |
| **Web**   **Services** | * **Nome:** Nome para identificar a estrutura Web Service que está sendo criada.     *Flag:* * **Continuar execução em caso de erros:** O processamento continua caso algum erro seja apresentado.     *Aba Conexão:* * **Endereço WSDL:** Informe o endereço do Web Service. Exemplo: [{+}](http://localhost/ToTvcBusinessConnect/wsProcess.asm?wsdl)<http://localhost/ToTvcBusinessConnect/wsProcess.asm?wsdl+> * **Protocolo:** Selecione o tipo de protocolo para auteticação. * **Usar autenticação padrão:** Informe o nome do servidor do proxy caso seja necessário para acessar o Web Service. * **Usuário:** Informe o usuário de domínio caso seja necessário autenticar o Web Service. * **Senha:** Informe a senha de domínio caso seja necessário autenticar o Web Service. * **Domínio:** Informe o nome do domínio caso seja necessário para autenticar o Web Service. * **Usar proxy padrão:** informe se será utilizado o proxy padrão ou não. * **Proxy:** Informe o nome de servidor do proxy caso seja necessário acessar o Web Service. * **Usar autenticação do proxy padrão:** informe se será utilizado autenticação padrão ou não. * **Usuário:** Informe o usuário do proxy caso seja necessário acessar o Web Service. * **Senha:** Informe a senha do proxy caso seja necessário acessar o Web Service. * **Domínio:** Informe o nome do domínio do proxy caso seja necessário acessar o Web Service. * **Método :** Informe o método do Web Service, caso seja necessário.     *Aba Parâmetros* * **Sem Filtro:** Não realiza nenhuma seleção prévia dos registros. * **Parâmetro:** Utiliza o parâmetro para realizar seleção dos registros. * **Fixo:** Utiliza filtro fixo para selecionar os registros. |
