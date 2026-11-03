---
content_hash: cdeab51f9c3e0ff0b48a94c80bc08f3d9bee1314834f1d75ccde465542f792b4
fetched_at: '2026-06-29T00:09:35.254997+00:00'
page_id: '425459283'
product: rm
source: tdn-rm
title: TOTVS Business Analytics  - Configurador
type: documentation
url: https://tdn.totvs.com/display/LRM/TOTVS+Business+Analytics++-+Configurador
version: 3
---

**Configurador**

---

A configuração da integração do TOTVS Business Analytics proporciona aos clientes que importem todos os Conceitos a serem utilizados na integração fazendo uso de um recurso rápido e prático.  
    
 O preenchimento da Stage Area irá acontecer via Conceitos. Para importar os mesmos o cliente irá entrar na visão de Configurar, apontar o diretório onde se localizam os Conceitos, preencher a conexão de Destino que será utilizada para configurar todos os Conceitos e concluir a importação.   
    
 Abaixo segue maiores detalhes da visão de Configurar:  
     
 **Diretórios Conceitos:** Apontar onde estão localizados os Conceitos de uso **exclusivo** para esta integração.  
     
 **Não importar Conceitos:** Ao marcar esta opção o usuário está abstraindo de importar os conceitos, esta opção tem o intuito **exclusivamente** de atualizar as Views e as tabelas da Stage Area, é importante destacar que os conceitos já importados não serão alterados. Nos dados de configuração do banco de dados do BI, o usuário deve informar os dados da base referente a Stage Area, evitando assim que sejam criadas ou atualizadas as tabelas da Stage Area em outro banco.  
    
 Vale ressaltar que quando está opção estiver desmarcada os Conceitos não **serão** duplicados e sim substituídos.  
    
 ***Observação*:** Para os usuários que não importaram os conceitos é **obrigatório** a importação pela primeira vez.  
     
 **Configurações do Banco de Dados RM:**  
    
 Neste contexto são exibidos os parâmetros de configuração da base de dados da Linha RM, que são:

* Tipo (Driver)
* Nome do servidor
* Nome do Banco
* Usuário
* Senha

**Configurações do Banco de Dados do BI:**

* **Tipo (Driver):** Informar o tipo de banco de dados do BI. Pode ser selecionado Sqlserver ou Oracle.

* Banco de dados do tipo Sqlserver:  
    
  + **Nome do Servidor:** Informar o nome ou endereço IP, onde está hospedado o banco de dados do BI.
  + **Nome do banco**: Informar a database que será utilizada pela integração.

* Banco de dados do tipo Oracle:  
    
  + **Base de dados:** Informar o Alias de conexão a base de dados Oracle.
  + **Usuário:** Informar usuário.
  + **Senha:** Informar senha do usuário.

* **Testar Conexão:** Recurso que autentica os dados de conexão.

Ao concluir a Configuração, a aplicação irá importar todos os Conceitos, tomando como base a conexão de destino informada na visão de "Configurar". Também serão excluídas/criadas as Views na conexão de Origem e as tabelas referente a Stage Area na conexão de Destino.   
    
 É importante destacar que quando este processo de importação de Conceitos acontecer novamente, a aplicação irá substituir todos os Conceitos (Não serão duplicados os Conceitos).   
    
 Desta maneira, caso seja customizado algum Conceito relacionado à Integração TOTVS Business Analytics, é **necessário** que seja realizado o backup e o mesmo deve ser movido para o diretório onde serão importados. Além de realizar todas as parametrizações, a visão também cria as Views e as tabelas da Stage Area.
