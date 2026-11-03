---
content_hash: 03fbf9b8a9720f5c82b1defe29d17aa244f48d855f979b61e597ed56b4d89905
fetched_at: '2026-06-29T00:10:51.429508+00:00'
page_id: '567754701'
product: rm
source: tdn-rm
title: Operação - Numero Sequencial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567754701
version: 8
---

### **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

**01. VISÃO GERAL**

      Documento criado para demostrar como utilizar a Operação "**Número Sequencial**" ao criar um Conceito.

      A operação "**Número Sequencial**", é utilizado para iniciar uma sequencia numérica em um determinado arquivo, respectivamente com o valor determinado pelo usuário.

**02. EXEMPLO DE UTILIZAÇÃO**

      Neste exemplo iremos utilizar o Data Server de Usuário (GlbUsuarioData) como conexão de Origem, um Arquivo de Texto como Conexão de Destino, e a operação "**Numero****Sequencial**".

falseExemplo de Utilização1º Passo:

Crie um novo conceito, preencha as informações necessárias e crie uma "Conexão de Origem".

Para criar a conexão siga o passo a passo abaixo:

* Clique em "Conexões | Conexão de Origem | Data Server RM.NET".

* Em seguida na tela de conexões, preencha o campo "Nome", e o campo "Servidor" com o Data Server "GlbUsuarioData" (utilizado em nosso exemplo). Clique em OK.

2º Passo:

Crie uma "Conexão de Destino".

É necessário criar um arquivo de texto vazio (.txt) e coloca-lo em uma pasta compartilhada em seu computador.

O arquivo será utilizado para gravar as informações do Data Server criado anteriormente.

Para criar a conexão siga o passo a passo abaixo:

* Clique em "Conexões | Conexão de Destino| Arquivo de Texto".

* Em seguida na tela de conexões, preencha o campo "Nome", e o campo "Arquivo (Selecione a opção "Arquivo Fixo" no lookup)", adicione o caminho compartilhado onde se encontra o arquivo de texto criado.

* Em seguida selecione a aba "Tabelas" e adicione uma nova tabela com as seguintes colunas: "Sequencial", "Codigo", "Status" e "Nome", elas serão utilizadas na ligação entre seus repercutidos campos da tabela de usuário. Clique em OK.

3º Passo:

Acesse a aba "Operações" e adicione a operação "**Numero Sequencial**".

* Em seguida na tela de operação, preencha o campo "Nome" e o campo "Valor Inicial" com número "10" por exemplo. Este numero será o valor inicial da sequencia de números do arquivo de texto.

4º Passo:

Agora, é necessário realizar as ligações dos campos com a tabela.

Acesse a aba "Ligações" e arraste a tabela criada na conexão de destino (DestinoUsuário), para o meio da tela, imagem demonstrativa abaixo:

* Feito isso é arraste a conexão de origem (Tabela GSUARIO) na onde está sendo solicitado, imagem demonstrativa abaixo:

5º Passo:

Para o preenchimento do campo "Sequencial", clique em operações e arraste a operação (Sequencial Usuário) criada anteriormente para o campo "Sequencial" da tabela DestinoUsuário, imagem demonstrativa abaixo:

* Em seguida, ligue os campos da tabela "GUSUARIO" em seus respectivos nomes da tabela de DestinoUsuário, imagem demonstrativa abaixo:

6º Passo:

Após salvar e executar o conceito, abra seu arquivo de texto, e verifique que a sequencia numérica foi iniciada com o valor determinado na operação (10).
