---
content_hash: accb64ce9a0d2378911232a3206a83568eacdb659fa3fe8acc27c500751a1ff5
fetched_at: '2026-06-28T21:35:17.675212+00:00'
page_id: '118882384'
product: fluig
source: tdn-fluig
title: Migração e Conversão de Collation (SQL Server)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118882384
version: 62
---

true.\*ndicenone

# Objetivo

---

O objetivo deste guia é indicar um método de migração dos dados de uma base com agrupamento de caracteres (*collation*) diferente do padrão "Latin1\_General\_CI\_AS" necessário para a correta utilização da base Fluig.

# Procedimento de migração e conversão de dados

---

Atenção!

Esta operação deve ocorrer antes da conversão de uma base TOTVS ECM para TOTVS Fluig Plataforma. Mesmo com a alteração do agrupamento padrão, os campos existentes permanecem incorretos, podendo assim, causar comportamentos inesperados na utilização da plataforma.

Acompanhe a seguir o checklist para a conversão.

false1true1Passo 01

* Gere um **DUMP** desta base de dados do **TOTVS ECM 3.00**, com toda estrutura de tabelas e campos.

* Para o SGBD **Microsoft SQL Server** utilize o procedimento a seguir:  
  1. Clique com o botão direito do mouse sobre a base de dados.
  2. No menu suspenso escolha a opção **Tarefas > Gerar Scripts...**
  3. Clique no botão **Próximo >** para passar a apresentação da Introdução do assistente para **Gerar e Publicar Scripts**.
  4. Deixe selecionada a opção para **Gerar script de todo o banco de****dados** e **todos os objetos de banco de dados** e clique no botão **Próximo >**.
  5. Na tela seguinte, no grupo **Tipo de Saída** e no grupo abaixo selecione a opção **Salvar** na nova janela de consulta.
  6. Clique no botão **Avançado**.
  7. Na tela de **Opções de Script Avançadas** altere a opção **Agrupamento de Scripts** para **True** e clique no botão **OK**.
  8. Ao retornar a tela **Gerar e Publicar Scripts**clique no botão **Próximo >**.
  9. Na etapa a seguir revise as configurações para geração do script da base. Clique no botão **Próximo >**.
  10. Torne à janela do **Microsoft SQL Server Management Studio**.
  11. Na nova janela aberta com o script, altere as seguintes linhas e proceda com as alterações abaixo citadas:

      1. Substituir todas as ocorrências do nome antigo do banco de dados para **fluig**. (Aproximadamente 39 ocorrências).

         sqltrue
      2. Substituir no nome do arquivo .**mdf** e do arquivo .**log** para **fluig**, bem como a label dos arquivos.

         sqltrue
      3. Substituir a ocorrência da versão do banco de dados para o valor **110**.

         sqltrue
      4. Substituir a ocorrência do instantâneo de leitura de commit para **ON**.

         sqltrue
      5. Substituir todas as ocorrências do **collation** antigo pelo novo **Latin1\_General\_CI\_AS**. (Aproximadamente 444 ocorrências).

         Importante!

         Independentemente da **collation** que a base ECM tenha, é necessário converter para '**Latin1\_General\_CI\_AS**', pois é o que o TOTVS Fluig espera como padrão, conforme descrito na documentação .

         1. **CI** significa **Case Insensitive**, não diferenciando letras maiúsculas de minúsculas em suas queries.
         2. **AS** significa **Accept Signal**, diferenciado acentuação nos campos de texto em suas queries.

            sqltrue
  12. Execute o script por inteiro.
  13. Atualize o explorador de objetos do SQL Management Studio.
  14. Deverá aparecer o novo banco **fluig**.
2Passo 02

* Proceda com a desativação das chaves (*constraints*) nas tabelas da base de dados **fluig**. Para o SGBD Microsoft SQL Server utilize a instrução a seguir:
  1. Abra uma janela de Nova Consulta (menu **Arquivo > Novo > Consulta do Mecanismo de Banco de Dados**);.
  2. Insira a consulta abaixo e a execute na nova base de dados.

sqlEclipse -1)
BEGIN
IF (@@FETCH\_STATUS <> -2)
BEGIN
SELECT @TABLENAME\_HEADER = 'ALTER TABLE ' + RTRIM(UPPER(@TABLENAME)) + ' NOCHECK CONSTRAINT ALL;'
--Alterar o NOCHECK para CHECK para depois habilitar as constraints
PRINT @TABLENAME\_HEADER
END
FETCH NEXT FROM TNAMES\_CURSOR INTO @TABLENAME
END
SELECT @TABLENAME\_HEADER = '--\*\*\*\*\*\*\*\*\*\*\*\*\* Fim das Tabelas \*\*\*\*\*\*\*\*\*\*\*\*\*--'
PRINT @TABLENAME\_HEADER PRINT ' '
DEALLOCATE TNAMES\_CURSOR ]]>

3. Copie o resultado e cole em uma janela de Nova Consulta e execute (na nova base de dados) usando o bando de dados **TOTVS Fluig Plataforma**.

3Passo 03

* Exclua o índice **CENTRAL\_TC** que fica na tabela **TAR\_CTRAL**. Para excluir o índice pelo SQL Studio:
  1. Abra o **SQL Server Management Studio (SSMS)**.
  2. Conecte-se ao servidor de banco de dados.
  3. No painel do **Object Explorer**, localize a base de dados onde a tabela está armazenada.
  4. Expanda a base de dados e navegue até a tabela chamada **TAL\_CTRAL**.
  5. Clique com o botão direito na tabela **TAL\_CTRAL** e selecione a opção **Indexes**.
  6. A lista de índices associados à tabela será exibida.
  7. Identifique o índice **CENTRAL\_TC**.
  8. Clique com o botão direito sobre o índice selecionado e escolha a opção **Delete**.
  9. Confirme a exclusão para apagar o índice atrelado à tabela.

* Realize a importação dos dados a partir da base de dados antiga, com um assistente de importação e exportação de dados, por exemplo. Para o SGBD Microsoft SQL Server utilize o procedimento:
  1. Clique com o botão direito do mouse sobre a nova base de dados.
  2. No menu suspenso selecione a opção **Tarefas > Importar Dados...**
  3. Na tela de apresentação do Assistente de Importação e Exportação do SQL Server clique no botão **Avançar >**.
  4. No campo **Fonte** de dados selecione a opção **SQL Server Native Client** (ao final é exibido o número da versão, utilize a mesma equivalente à versão do serviço de banco de dados).
  5. No campo **Nome** do servidor indique (digite ou selecione na caixa suspensa) o servidor e instância que possui a base de dados anterior (que deverá ser compatibilizada / normalizada).
  6. No grupo **Autenticação** utilize o método que permite acesso a todos os dados desta base de dados anterior. É recomendado o uso de um usuário com permissão de **db\_owner**.
  7. Selecione ou digite, no campo **Banco de dados**, a base antiga e clique no botão **Avançar >**.
  8. Na tela com título (para) **Escolher um Destino** devem vir preenchidos os campos com informações de acesso a esta nova base de dados. Se as informações estiverem incorretas ou incompletas, corrija-as, e clique no botão **Avançar >**.
  9. A seguir na tela com título **Especificar Cópia** ou **Consulta de Tabela** selecione a opção **Copiar** dados de uma ou mais tabelas ou exibições e clique no botão **Avançar >**.
  10. Na tela de título **Selecionar Tabelas** e **Exibições de Origem**, clique na primeira caixa de seleção que está nos títulos da listagem de **Tabelas e exibições**.
  11. Com todos selecionados clique no botão **Editar Mapeamentos...**
  12. Na caixa **Configurações de Transferência**marque a caixa de seleção **Habilitar inserção de identidade** e, então, no botão OK.

      Atenção!

      Não deixe de marcar esta opção para que não ocorram falhas na cópia dos dados.
  13. Retornando à janela anterior, **Selecionar Tabelas** e **Exibições de Origem**, clique no botão **Avançar >**.
  14. Na tela com título **Revisar Mapeamento** de **Tipo de Dados** clique no botão **Avançar**.
  15. Na tela com título **Executar Pacote**marque a caixa de seleção **Executar imediatamente** e clique no botão **Avançar >**.
  16. Na tela com título **Concluir Assistente**, após revisar as ações clique no botão **Avançar**.
  17. Na tela a seguir de execução das ações ao final deve ser exibida a informação de que a importação foi realizada com sucesso.
  18. Execute o *script* para habilitar as *constraints* que foram desativadas no **Passo 02**alterando de **NOCHECK** para **CHECK**.
4Passo 04

* Conferir procedimentos para o serviço/instância do SGBD Microsoft SQL Server, descritos na página , a partir da sessão **Configuração do banco**.
5Passo 05

* As configurações de agrupamento de caracteres (*Collate/Collation*) das bases de dados podem ser consultadas utilizando a instrução:

sqlEclipseIMPORTANTE

* Verificar o nome do proprietário (owner) do novo banco criado. Deverá ser o mesmo usuário a ser informado na instalação do **Fluig.**
6Passo 06

* Verificar o repasse das permissões de acesso aos devidos usuários na nova base de dados. Estas podem ter sido perdidas.
7Passo 07

* Instalar a **versão 1.5.13 (Última EP)** do **Fluig** e configurar para apontar para esta base de dados (**fluig**).
8Passo 08

* Inicializar o serviço **Fluig**, e acompanhar o LOG, para se certificar de que toda a inicialização foi bem sucedida, sem erros graves, como falha na conexão com o SGBD.
9Passo 09

* Retornar ao processo de conversão **TOTVS ECM 3.00 para TOTVS Fluig Plataforma** se for este o caso, ou então, realizar as validações desejadas e uso da nova instalação.
