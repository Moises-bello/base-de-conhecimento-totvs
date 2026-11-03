---
content_hash: 1442ceed51963907e5aa21fcf2df72b52366e82bf151920d85a3c5b16bf98cc0
fetched_at: '2026-06-29T00:11:21.211270+00:00'
page_id: '689067189'
product: rm
source: tdn-rm
title: 2.3.1 - Restauração de Banco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=689067189
version: 31
---

## O que é?

Esta atividade consiste na **Restauração de uma Base de Dados** (SQL ou Oracle) para utilização em um **Projeto de Teste**. O objetivo é restaurar uma base a partir de um backup, clonando-a para garantir que os testes possam ser realizados sem modificar a base original.

## Para que serve?

Serve para garantir que a base de dados utilizada nos testes esteja configurada corretamente e atualizada, sem interferir em bases já existentes no servidor. Ao restaurar uma base para testes, pode-se trabalhar de forma segura e isolada, com opções de nomes randômicos ou fixos para evitar conflitos.

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em: **Atividades** → **Banco de Dados**→ **Restauração de Banco.**

 2. Na tabela que será mostrada, clique no botão verde em destaque para iniciar o cadastro.

2. Link para Definir cabeçalho (Nome e nível de acesso)

[Clique aqui para obter as informações do cabeçalho](https://tdn.totvs.com/pages/viewpage.action?pageId=859591806)

3. Preenchimento dos CamposVersão

Especifica a versão da atividade em questão. O objetivo de versionar uma atividade é para quando necessitamos ter mais de uma atividade em versões diferentes. Isso irá nos auxiliar a ter um histórico de atualizações e assegurar que as mudanças feitas sejam rastreáveis e reversíveis, se necessário.

Se for necessário utilizar mais de uma versão do RM no seu ambiente, é recomendado que a versão da atividade seja compatível com o sistema RM em uso. Caso contrário, pode-se optar por uma versão padrão de sua preferência.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

Fornece uma descrição detalhada da atividade, explicando seu propósito e operações, facilitando a compreensão e manutenção futura.

Credencial de banco de dados

Selecione uma [Credencial de Banco de Dados](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados) existente, caso não tenha uma deverá ser criada antes de continuar.

Nome do BancoRandômico 

Quando a opção **Randômico** é selecionada, o sistema gera automaticamente um nome para a base de dados restaurada. Esse nome é único e aleatório, evitando conflitos com bases de dados que já estejam presentes no servidor.

Fixo

Ao selecionar a opção **Fixo**, o nome que será utilizado para a restauração será o nome definido dentro da [Credencial de Banco de Dados](https://tdn.totvs.com.br/display/LRM/1+-+Banco+de+Dados), para SQL será utilizado o valor definido no campo "Nome do banco" e para Oracle será utilizado o valor do campo "Nome do pluggable".

**Atenção**: Certifique-se de que não exista outro banco com o mesmo nome no servidor onde a restauração será realizada, para evitar conflitos.

Origem da restauração para SQL Server e Oracle

Aqui será falado sobre os campos **Caminho de Backup** para SQL Server e **Nome do PDB de origem a ser clonado** para Oracle.

Caminho de Backup

Informe o diretório e o arquivo de backup. Certifique-se de que o diretório esteja compartilhado com permissões de leitura e gravação. O caminho a ser informado deve ser o do compartilhamento de rede no formato: **\\SERVIDOR\DIRETORIO\BASE.BAK**.

Nome do PDB de origem a ser clonado

Informe o nome do PDB (*Pluggable Database*) que será usado como origem para a criação do clone. No seu banco Oracle, é essencial que exista uma base restaurada específica para servir como modelo. Essa base será clonada e deve ser utilizada exclusivamente para a execução dos testes.

Variáveis de ambiente

As Variáveis de Ambiente são utilizadas para configurar e personalizar o comportamento da Atividade. Elas permitem definir valores específicos ou dinâmicos que podem ser usados durante a execução dos testes, assegurando que o teste execute conforme o ambiente em que o mesmo é executado. As Variáveis de Ambiente são cadastradas no cadastro de Ambiente onde informamos os valores fixos ou de forma dinâmica no cadastro de Script SQL.

Consulte quais campos permitem o uso das Variáveis de Ambiente nessa Atividade:

[Restauração de Banco - Variáveis de Ambiente.](https://tdn.totvs.com/pages/viewpage.action?pageId=873219509)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

Imagine que você faz parte da equipe de Fiscal e precisa realizar um teste para o **cadastro de uma nova moeda no sistema**. Para garantir que o processo foi realizado corretamente, é necessário restaurar uma base de dados e verificar se o registro da nova moeda foi inserido na base restaurada após o teste automatizado.

Após a base de dados ter sido restaurada com sucesso, inicie o **Projeto de teste automatizado**. Esse projeto realiza uma chamada HTTP para o sistema, inserindo os dados da nova moeda.

---

# Saiba mais

Sempre que utilizar uma Atividade de Restauração de Banco de Dados dentro de um [Projeto de Teste](https://tdn.totvs.com/display/public/LRM/2.5+-+Projetos), deixe a limpeza automática do TOTVS Automação de Testes ativada para a base ser apagada após a execução do teste. Isso ajudará a preparar o seu ambiente para uma próxima execução das automações.

# FAQ

**P: Minha restauração será SQL ou Oracle?**

R: O tipo de banco da restauração será definido com base no tipo escolhido dentro da Credencial de Banco de Dados selecionada.

**P: Como posso excluir a base restaurada após os testes?**

R: Deixe a limpeza automática do TOTVS Automação de Testes ativada para remover a base restaurada após a conclusão dos testes, liberando espaço no servidor.

**P: Posso restaurar uma base de dados diretamente no ambiente de produção?**

R: Não é recomendado restaurar diretamente em produção, pois pode haver riscos de corromper os dados. Use ambientes de teste para garantir a segurança.

**P: Posso agendar a restauração de uma base de dados?**

R**:** É possível programar a restauração para ser executada em horários específicos
