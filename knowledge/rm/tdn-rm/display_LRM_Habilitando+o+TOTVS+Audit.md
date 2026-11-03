---
content_hash: cc424e7b009574ce98e7578fd9a236a7e0274f476b4fb10f015e015e08881264
fetched_at: '2026-06-29T00:11:11.089482+00:00'
page_id: '645473929'
product: rm
source: tdn-rm
title: Habilitando o TOTVS Audit
type: documentation
url: https://tdn.totvs.com/display/LRM/Habilitando+o+TOTVS+Audit
version: 22
---

Esse documento tem a finalidade de ser um guia para a habilitação do TOTVS Audit em sua maquina. 

### **HABILITANDO O TOTVS AUDIT PELA TELA**

**Momentos que serão necessários a  execução dos assistentes do Totvs Audit:**

1. Após execução do RM.Atualizador na base de dados, considere existir modificações estruturais ocasionadas por scripts  que precisam refletir nas triggers e tabelas de auditoria do TOTVS Audit.
2. Ao criar novo campo complementar quando a tabela está sendo auditada, com objetivo de refletir a adição da nova coluna nas triggers e tabela de auditoria do TOTVS Audit.

**Obs:** Ao final do processo de atualização da base de dados executado pelo [Atualizador](https://tdn.totvs.com/pages/viewpage.action?pageId=421385221), será apresentado o botão para iniciar o assistente de configuração do Totvs Audit entretanto, caso o usuário não queira executá-lo naquele momento, poderá acessá-lo na pasta **RM.Net\RM.TotvsAudit.exe.**

**Assistente do TOTVS Audit:**

* **Tela de login:**

 Nesta tela, será necessário informar o usuário/login de banco com requisitos descritos abaixo no respectivo banco de dados:

       \*  ALTER, CREATE, DROP, SELECT, INSERT E UPDATE para ANY TABLE  
       \*  CREATE, DROP PARA ANY INDEX  
       \*  CREATE, DROP, SELECT PARA ANY SEQUENCE

Também será necessário ter QUOTA UNLIMITED ON RM\_DADOS QUOTA UNLIMITED ON RM\_INDICES;

Além do usuário/senha  é necessário estabelecer uma conexão com o banco de dados por meio do Alias.

* **Tela de Requisitos**

       Nesta tela, será necessário **confirmar a leitura dos links** que descrevem detalhes de seu funcionamento e ajustes necessários para sua configuração.

[http://tdn.totvs.com/pages/releaseview.action?pageId=322146156](https://tdn.totvs.com/pages/releaseview.action?pageId=322146156)

[http://tdn.totvs.com/display/public/LRM/Novo+Log+de+Auditoria](https://tdn.totvs.com/display/public/LRM/Novo+Log+de+Auditoria)

* **Tela de Backup**

       Nesta tela, será necessário confirmar a ação de backup antes de iniciar o Assistente de configuração do TotvsAudit Precisamos desta confirmação para prevenir algum erro.

* **Tela de Análise de requisitos**

       Nesta tela, serão listados todos os requisitos para iniciar a criação dos objetos necessários no funcionamento do TotvsAudit, Tais itens estão relacionados ao acesso nas tabelas do CorporeRM, views do Oracle ou Sql Server.

**Obs:**Todos os requisitos validados estão detalhados na pagina **[Requisitos validados no Totvs Audit](https://tdn.totvs.com/display/LRM/Requisitos+validados+no+TOTVS+Audit)**.

* **Tela de Execução do processo**

Nesta tela, são exibidos os botões para ativar e desativar, para executar o TOTVS Audit e Auditar LGPD

Nela são apresentadas as atividades que serão executadas para configuração do TOTVS Audit.

Após a execução do processo, os itens executados serão exibidos com status de sucesso ou erro, caso ocorra.

Se executar com sucesso, o TOTVS Audit está pronto para auditar as tabelas

Se executar com erros, significa que há ajustes na base de Dados a serem executados

O usuário agora tem a opção com esse  novo check-box de escolher se realmente deseja ou não gerar o log de execução do processo no Totvsaudit:

O Log de Auditoria serve como um histórico para que sejam feitas todas as inclusões, alterações e exclusões que vierem a ocorrer na(s) tabela(s) selecionada(s) para serem auditadas. Ele é composto por uma série de Procedures, onde é(são) selecionada(s) uma tabela(s) a ser(em) auditada(s), criando-se uma "**Tabela Espelho**" em um **Schema** exclusivo do Log de Auditoria(**TOTVSAUDIT**) e **Trigger(s)**no banco de dados, dependendo da ação escolhida (**Insert, Update, Delete**).

**Obs:** Caso o usuário opte por gerar o Log de execução do processo, esse log será criado no mesmo diretório do arquivo RM.TOTVSAudit.exe, na pasta TOTVS\_Audit\_Logs, conforme imagem abaixo:

Quando houver transações que utilizam a(s) tabela(s) selecionada(s), a Trigger é disparada e grava na tabela de Log (**ZAUDITCHANGES**) as informações sobre o autor da ação: os dados que foram criados, alterados ou deletados são salvos na "Tabela Espelho"  (Ex.: TOTVSAUDIT.PFUNC, tabela espelho a tabela do sistema RM.PFUNC).

Data Types não auditáveis

Campos do tipo **Memo(Text)**, **ntext**, **image** e **timestamp** por definição da ferramenta não são auditáveis. Estas informações podem ser consultadas através de QUERY´s no banco de dados ou através da interface do usuário do Log de Auditoria.

Estes tipos de campos não podem ser auditáveis porque podem gerar um crescimento de dados na tabela espeilho e pode honerar a performance do sistema e gerar um consumo excessivo de espaço em disco.

Rules Desativadas

Nos bancos de dados SQL Server as rules serão desativadas do Schema TOTVSAUDIT, uma vez que a regra desta rule já foi aplicada na tabela principal.

Atenção

É recomendável utilizar a TAG **<add key="UseRMUser" value="true" />**nos arquivos **RM.Atualizador** e **RM.TotvsAudit.**No caso desta configuração, apenas usuários do sistema RM poderão executar a atualização da base e configurar o TotvsAudit. Usuários do banco de dados não poderão realizar essas ações com a TAG "UseRMUser" ativa.

### **HABILITANDO O TOTVS AUDIT POR API:**

Para configurar o TotvsAudit via request siga esses parâmetros:

**Link usado:**<http://localhost:8051/api/totvs-audit/v1/totvs-audit-config>

Corpo da requisição precisa ser do tipo Raw - Json

**{**  
**"enabled": true,**  
**"enabledLogLGPD": true**  
**}**

A partir da 2205, também é possível utilizar a palavra chave ""NoUseRequirements": true" no corpo da requisição não deseje validar os requisitos para atualização. Exemplo:

{  
 **"Enabled": true,**  
**"EnabledLogLGPD": true,**  
**"NoUseRequirements": true**  
}

Caso esteja com dúvidas de qual alias a API está utilizando, a partir da 2205 é possível utilizar a requisição com a palavra "alias", que a API retornará o nome do alias que está utilizando: <http://localhost:8051/api/totvs-audit/v1/totvs-audit-config/alias>

**Autenticação:**

**Caso queira utilizar o login de banco:**

Adicione o header CustomAuthorization com o valor do login de banco, por exemplo, rm senha rm.

**Caso queira utilizar o login pelo usuário da aplicação:**

Adicione a opção de autenticação básica 'Authorization' com o valor do usuário da aplicação, por exemplo, mestre senha xxxx.

Irá retornar o status de cada passo executado pelo assistente com o valor seguindo a legenda abaixo, sobre status do processo:  
Success = 0, Warning = 1, Error = 2.

Também é possível chamar a API via GET para identificar qual alias de banco ela está utilizando.

Ao ativar o TOTVS Audit as tabelas passam a ser auditadas instantaneamente. O RM armazena a informação sobre o envio do contexto de auditoria em um cache, o qual expira após 10 minutos, sendo aconselhável, desta forma, reiniciar o RM Host após a ativação do TOTVS Audit para limpar os caches.

**Processos do TOTVS Audit**

* [Pré Requisitos para migração e utilização do Novo L](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645486062)[og](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645486062)
* [Habilitando o TOTVS Audit](https://tdn.totvs.com.br/display/LRM/Habilitando+o+TOTVS+Audit)
* [Configurando o TOTVSAudit](https://tdn.totvs.com.br/display/LRM/Configurando+o+TOTVSAudit)
* [Configuração de Proteção de Dados (LGPD)](https://tdn.totvs.com.br/pages/viewpage.action?pageId=645475098)
* [Expurgo de Dados armazenados pelo TotvsAudit](https://tdn.totvs.com.br/display/LRM/Expurgo+de+Dados+armazenados+pelo+TotvsAudit)
