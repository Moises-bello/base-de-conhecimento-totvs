---
content_hash: 6ae6087fbd548a4faa4a341ef0b5380c7252f27469da1ee39573b012ed889d9a
fetched_at: '2026-06-29T00:12:09.518537+00:00'
page_id: '947302644'
product: rm
source: tdn-rm
title: 1- Banco de Dados
type: documentation
url: https://tdn.totvs.com/display/LRM/1-+Banco+de+Dados
version: 10
---

## **O que é?**

**Uma Credencial de Banco de Dados** é uma configuração prática e reutilizável que representa os dados necessários para se conectar a uma instância de banco. Com ela, é possível montar strings de conexão de forma didática, segura e centralizada, facilitando a integração com bancos de dados em diferentes Ambientes e cenários de testes.

Além disso, as credenciais podem ser referenciadas dinamicamente em atividades, promovendo a reutilização e a padronização no acesso a bases de dados.

## **Para que serve?**

Ela serve para:

* Declarar conexões com bancos de dados de forma simples, sem repetir informações sensíveis em várias atividades.
* Reutilizar as credenciais em diferentes Ambientes ou versões do RM.
* Aumentar a segurança e organização centralizando o controle de acesso aos bancos.

## **Exemplo de Uso**

Como cadastrarComo Cadastrar 1. Início de Cadastro 

1. Navegue no menu do TOTVS Automação de Testes e clique em **Credenciais.**
2. Então clique em **Banco de Dados.**
3. Na tabela que será mostrada, clique no botão verde em destaque para adicionar **uma credencial de banco de dados**.

2. Preenchimento dos Campos1. Nome de exibição

Aqui você deverá atribuir um nome para identificar sua atividade de credencial de banco de dados.

2. Permissões de Grupos

Os grupos no TOTVS Automação de Testes permitem organizar e controlar o acesso dos usuários às credenciais de banco, garantindo que cada um tenha acesso apenas às credenciais relacionadas ao seu papel ou projeto. Para gerenciar essas permissões de forma eficiente, adicione um grupo à sua credencial.

(Saiba mais sobre o que são os [Grupos](https://tdn.totvs.com/display/LRM/6+-+Grupos) no TOTVS Automação de Testes.)

3. Tipo de Banco

Aqui você deverá informar o tipo de banco que irá utilizar em seus testes. As opções são:

* + - SQL Server
    - Oracle

SQL1. Servidor

**Aqui você deverá informar o servidor e instância de banco de dados onde o SQL Server está instalado.**

2. Nome do Banco

**Aqui você deverá informar o nome exato do banco de dados dentro do SQL Server com o qual você quer se conectar.**

3. Nome do usuário do banco de dados

**Aqui você deverá informar o nome de um usuário que tem permissão para restaurar, remover e acessar o banco de dados.**

4. Senha do usuário do banco de dados

**Aqui você deverá informar a senha correspondente ao nome de usuário, usada para garantir que só pessoas autorizadas tenham acesso.**

Oracle1. Servidor

**Aqui você deverá informar o servidor de banco de dados onde a seu container Oracle está instalado.**

2. Nome do Serviço

**Aqui você deverá informar o** **N****ome do Serviço que identifica o banco de dados Oracle para conexões externas**.

3. Nome do Pluggable

**Aqui você deverá informar o nome exato do pluggable (PDB) dentro do container ao qual deseja se conectar.**

4. Nome do Usuário do Pluggable

**Aqui você deverá informar o nome do usuário que tenha permissões para acessar as tabelas do pluggable (PDB).**  
**Esse usuário é utilizado para trabalhar com os dados daquele PDB específico.**

5. Senha do Usuário do Pluggable

**Aqui você deverá informar a senha correspondente ao usuário dentro do pluggable (PDB).**

6. Nome do Usuário SYSDBA

**Aqui você deverá informar o nome do usuário com privilégios administrativos no container. Ele será usado para clones e para apagar o pluggable (PDB) criado durante a execução.**

7. Senha do Usuário SYSDBA

**Aqui você deverá informar a senha do usuário com privilégios administrativos no container.**
