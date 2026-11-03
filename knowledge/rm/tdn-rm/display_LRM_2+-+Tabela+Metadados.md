---
content_hash: 3622e117f15e5f1a4419d2f52390f7c52749e3add1f732a2aa23986eb97dd861
fetched_at: '2026-06-29T00:10:46.622532+00:00'
page_id: '555264690'
product: rm
source: tdn-rm
title: 2 - Tabela Metadados
type: documentation
url: https://tdn.totvs.com/display/LRM/2+-+Tabela+Metadados
version: 6
---

## **ÍNDICE**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Restrições de atualização da tabela**

**01. VISÃO GERAL**

Neste documento será exibido a forma de se criar ou alterar uma tabela.     

É possível criar tabelas que serão usadas no projeto de Metadados. Essas tabelas serão criadas/atualizadas fisicamente no banco de dados após o passo de "Gerar o Projeto de Metadados".

Antes de criar a tabela é necessário que os Tipos de Dados estejam previamente cadastrados no sistema.

Veja mais em: . 

**02. EXEMPLO DE UTILIZAÇÃO**

      O cadastro de tabelas disponibilizado no RM é a abstração da criação, edição e exclusão de tabelas e colunas no banco de dados.

      Para acessar o cadastro acesse o menu: **Serviços Globais > Metadados > Tabela**.

      A seguir será mostrado como criar uma nova tabela, para isso clique em **Incluir:**

      Na imagem acima foi criada a tabela chamada DOCUMENTACAO. Toda tabela criada para projetos de metadados tem seu nome iniciado automaticamente com ZMD. Ou seja, essa tabela será criada fisicamente no banco como: ZMDDOCUMENTACAO, veja o campo mostrado na tela: Nome Físico no banco.

      No cadastro de Atributos, devem ser cadastrados os campos da tabela. Para cada campo criado deve ser indicado o seu tipo de dados. (ver mais em: ).

      Ao selecionar um campo (atributo) serão exibidos no agrupador Geral itens de configuração para o campo em foco.

      Observe que as propriedades de Tamanho e Escala podem variar de acordo com o tipo de campo. Para campos do tipo Varchar, por exemplo, é obrigatório informar o seu tamanho. Campos do tipo Decimal devem ser informados o Tamanho e a Escala. 

      **Obs.:** Uma tabela deve ter pelo menos 1 campo que seja chave primária. E após o projeto ter sido gerado não será permitido desmarcar o campo 'Chave Primária'. O ícone mostrado a frente do campo Rótulo identifica se o projeto já foi gerado e consequentemente se a tabela já foi criada no banco de dados. Caso seja um , a tabela não existe. Caso seja um verde, a tabela existe. 

      As abas Dicionário de Dados e Proteção de Dados do agrupador Geral referem-se a proteção de dados. Veja mais em: .

**03. RESTRIÇÕES DE ATUALIZAÇÃO DA TABELA**

      Antes de gerar o projeto de metadados e a tabela ser criada fisicamente no banco de dados pode-se alterar tudo que for necessário no cadastro de Tabelas

      Após gerar o projeto e a tabela existir no banco de dados o sistema não permite que algumas alterações sejam feitas, com a finalidade de manter a integridade dos dados e das tabelas. 

* Não é possível alterar o tipo de dados de um campo. Ex.: Mudar um campo do tipo inteiro para string. Uma alternativa é criar uma nova coluna e remover a errada. Se o tipo for alterado na tela, a mudança não será replicada para o banco.
* Não é possível alterar um índice, após ser criado na primeira geração do projeto, o índice não pode ser alterado ou removido.  
  Na geração do projeto caso a tabela não exista é gerado um script para criar o índice. Caso a tabela já exista, nenhum script será gerado para o índice.
* **Atenção:** Ao renomear um campo que já existe na base de dados, ao regerar esse projeto de metadados é feito uma exclusão (drop) da coluna antiga e criada uma nova coluna. Isso fará com que os dados da coluna antiga sejam deletados.
* Adicionar ou remover colunas são permitidos.
* Não é possível remover colunas com Valor Padrão definido.
* Não é possível alterar o Valor Padrão de colunas existentes de projetos gerados.
