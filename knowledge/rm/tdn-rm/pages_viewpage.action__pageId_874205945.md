---
content_hash: c889d58707b77f446cd388c348be9dfca4d0eca19248f8115a3ac8f1e6de45dc
fetched_at: '2026-06-29T00:11:59.606934+00:00'
page_id: '874205945'
product: rm
source: tdn-rm
title: Cópia de 2.3.1 - Restauração de Banco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=874205945
version: 1
---

# O que é?

Esta atividade consiste na **Restauração de uma Base de Dados** (SQL ou Oracle) para utilização em um **Projeto de Teste**. O objetivo é restaurar uma base a partir de um backup, clonando-a para garantir que os testes possam ser realizados sem modificar a base original.

# Para que serve?

Serve para garantir que a base de dados utilizada nos testes esteja configurada corretamente e atualizada, sem interferir em bases já existentes no servidor. Ao restaurar uma base para testes, pode-se trabalhar de forma segura e isolada, com opções de nomes randômicos ou fixos para evitar conflitos.

# Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TestFlow e clique em: **Atividades** → **Banco de Dados**→ **Restauração de Banco.**

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

String de Conexão

Escreva os parâmetros de conexão com o seu banco de dados.

1. No caso da opção selecionada anteriormente for **Usar Contexto**, escreva os parâmetros de conexão com o banco de dados que será utilizado para recuperar o mock das informações, ou seja, do banco de dados em que os valores retornados pelo script Sql serão os valores de referência para comparar com a base restaurada pelo projeto de teste.
2. No caso da opção selecionada anteriormente for **Usas bases específicas**, forneça os parâmetros de conexão da sua base de dados de **Teste** (onde será executada a automação) e da base de dados **Gabarito** (base que conterá os valores de referência que servirão para realizar a comparação).

Os parâmetros mais comuns são:

* **Data Source**: SERVIDOR DO BANCO
* **User ID**: USUÁRIO DE CONEXÃO
* **Password**: SENHA DE CONEXÃO

Estes parâmetros devem ser informados separados por ponto e vírgula.

Se preferir não criar a string manualmente, você pode utilizar o Gerador de Strings de Conexão disponível ao lado deste campo. Basta abri-lo, selecionar a opção **+PADRÃO SQLSERVER**, preencher os valores e salvar para criar sua conexão.

Caso precise adicionar parâmetros adicionais à sua string de conexão, clique no botão **+Adicionar Parâmetro**.

Além disso, também é possível excluir qualquer parâmetro adicionado anteriormente clicando no ícone 

Nome do BancoRandômico 

Quando a opção **Randômico** é selecionada, o sistema gera automaticamente um nome para a base de dados restaurada. Esse nome é único e aleatório, evitando conflitos com bases de dados que já estejam presentes no servidor.

Fixo

Ao selecionar a opção **Fixo**, você pode definir manualmente o nome da base de dados a ser restaurada. Um campo será habilitado para que você insira o nome desejado, que será usado consistentemente durante o processo de restauração.

Se escolher a opção **Fixo**, será necessário informar um nome para a base de dados. **Atenção**: Certifique-se de que não exista outro banco com o mesmo nome no servidor onde a restauração será realizada, para evitar conflitos.

Tipo de Banco

Escolha o tipo do seu banco de dados:

1. SQL;
2. Oracle
Caminho de Backup

Informe o diretório onde o arquivo de backup está armazenado. Certifique-se de que o diretório esteja compartilhado com permissões de leitura e gravação. O caminho a ser informado deve ser o do compartilhamento de rede no formato: **\SERVIDOR\DIRETORIO\BASE.BAK**.

Variáveis de ambiente

As variáveis de ambiente na comparação de arquivos no TestFlow são utilizadas para configurar e personalizar o comportamento da atividade de comparação. Elas permitem definir valores específicos que podem ser usados durante a execução dos testes, assegurando que a comparação ocorra conforme o ambiente em que o teste está sendo executado.

Consulte as variáveis de ambiente permitidas nessa Atividade:

[Restauração de Banco - Variáveis de Ambiente.](https://tdn.totvs.com/pages/releaseview.action?pageId=863909804)

Saiba mais sobre [Ambientes](https://tdn.totvs.com/display/LRM/4+-+Ambientes).

Exemplo prático

Imagine que você faz parte da equipe de Fiscal e precisa realizar um teste para o **cadastro de uma nova moeda no sistema**. Para garantir que o processo foi realizado corretamente, é necessário restaurar uma base de dados e verificar se o registro da nova moeda foi inserido na base restaurada após o teste automatizado.

Após a base de dados ter sido restaurada com sucesso, inicie o **Projeto de teste automatizado**. Esse projeto realiza uma chamada HTTP para o sistema, inserindo os dados da nova moeda.

---

# Saiba mais

Você pode montar a string de conexão de três maneiras: *1 - Digitando manualmente a string;* *2 - Através do gerador de conexão informando os campos necessários*; *3 - Através do gerador de conexão carregando o padrão do SQLServer*.

Sempre que utilizar uma Atividade de Restauração de Banco de Dados, deixe a limpeza automatica do TestFlow apagar a base. Isso ajudará a preparar o seu ambiente para uma próxima execução das automações.

Nunca utilize "select \*" para validar a comparação dos bancos de dados. Pode haver campos de datas que irá comprometer seu resultado.

# FAQ

**P: Como posso excluir a base restaurada após os testes?**

R: Configure a limpeza automática no TestFlow para remover a base restaurada após a conclusão dos testes, liberando espaço no servidor.

**P: Posso restaurar uma base de dados diretamente no ambiente de produção?**

R: Não é recomendado restaurar diretamente em produção, pois pode haver riscos de corromper os dados. Use ambientes de teste para garantir a segurança.

**P: Posso agendar a restauração de uma base de dados?**

R**:** É possível programar a restauração para ser executada em horários específicos
