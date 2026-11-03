---
content_hash: 6336a5ca70d717d1dd1b9bbb6207edde1224bcd061d41ca9e9f62999adc358b6
fetched_at: '2026-06-29T00:09:11.392697+00:00'
page_id: '403746941'
product: rm
source: tdn-rm
title: Códigos de Acesso
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403746941
version: 5
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

  Este cadastro tem como finalidade permitir a inclusão e manutenção de códigos especiais de acesso ao banco de dados. Estes códigos serão informados posteriormente para cada usuário do aplicativo, definindo-se e diferenciando-se assim, o usuário administrador do banco de dados a ser utilizado para a conexão.

Os códigos criados neste cadastro referem-se ao acesso e administração do banco de dados e não usuário do aplicativo, que possui outro cadastro próprio. Desta forma, poderão ser criados no aplicativo diferentes códigos de acesso para diferentes usuários do aplicativo, podendo alguns deles ter maiores liberdades como administradores do banco de dados.

## **02. EXEMPLO DE UTILIZAÇÃO**

**Acesse**:  Serviços Globais > Segurança > Códigos de Acesso

Existe um administrador do banco com o seguinte login:

**Usuário do Banco:** SYSDBA  
**Senha:** masterkey

Este usuário poderá continuar utilizando o mesmo nome e senha para acessar o banco através do aplicativo. Para isso, basta criar um código de acesso com os dados do código e do administrador. Neste caso, teríamos, por exemplo:

**Código de Acesso:** DBA01;

**Descrição:** Administrador 001 do Banco

**Usuário do Banco:** SYSDBA  
**Senha:** masterkey

# **CADASTRO**

       Para a inclusão ou manutenção de Códigos de Acesso, deverão ser cuidadosamente preenchidos os campos abaixo:

### Código de Acesso

Informe um código alfanumérico para identificação do usuário Administrador do Banco de Dados. Este código poderá ser uma referência ao Administrador ou qualquer outro código interno que o identifique.

### Descrição

Digite um título ou descrição para identificação do código de acesso que está sendo incluído.

### Acesso ao Banco de Dados

Os dados a serem informados nos campos seguintes permitirão diferenciar o usuários do banco fora do aplicativo.

Usuário do Banco  
Digitar o nome do usuário do banco de dados. Como por exemplo: SYSDBA.

### Senha

Digitar a senha do usuário administrador do banco que, conforme o usuário SYSDBA acima, poderia ser MASTERKEY.

### Confirmação da Senha

Digite novamente a senha informada no campo anterior para simples confirmação.

Os dados a serem informados nos campos permitirão diferenciar os usuários do banco fora do aplicativo podem ser os mesmos utilizados pelo Administrador ao acessar o Banco fora do aplicativo, ou seja pode-se repetir Usuário do Banco e Senha utilizados pelo Administrador fora do banco, neste código.

Entretanto, sugerimos que o código de acesso seja restrito à mesma pessoa no cadastro de usuários do Aplicativo. Considere-se a situação abaixo para melhor compreender estas informações.

**EXEMPLO:**  
Determinado funcionário da empresa é o Administrador do Banco de Dados e possui portanto, privilégios no acesso que outros não possuem. Para que ele continue utilizando o mesmo Login do Banco no Aplicativo, cria-se um Código de Acesso com o s dados deste Login. No cadastro de usuários, cada um deve possuir um Código de Acesso. Ao cadastrar-se um usuário para esse funcionário (Administrador de Banco do Dados) acessar o aplicativo, deve-se relacioná-lo a este código de acesso. Mas para outros usuários, este código de acesso não deve ser informado, já que possui total flexibilidade no acesso ao banco.

**OBSERVAÇÃO**  
Os aplicativos RM possuem dois usuários default incluídos no banco de dados: SYSDBA (senha MASTERKEY) e RM (senha RM). O usuário SYSDBA só possui acesso às tabelas de controle do sistema: GPARAMS, GUSUARIO, GPERMIS, GACESSO, GSISTEMA, GCOLIGADA e GUSRPERFIL. O usuário RM possui acesso em todas as tabelas do sistema.

Novos usuários poderão ser incluídos e a senha do usuário RM poderá ser alterada no banco de dados. Para isto, consulte seu administrador de banco de dados. Lembre-se que ao alterar a senha no banco de dados, a senha nesta janela também tem que ser alterada para a mesma senha informada.

false

**Versão:** 12.01.XX
