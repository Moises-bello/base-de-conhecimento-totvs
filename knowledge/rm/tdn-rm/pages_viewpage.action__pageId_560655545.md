---
content_hash: 67a1511386d2e878212d8e12646b666c41be2957cefdc484d68b44b37343d945
fetched_at: '2026-06-29T00:10:47.824006+00:00'
page_id: '560655545'
product: rm
source: tdn-rm
title: Conexão de Destino Utilizando a Carol
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=560655545
version: 7
---

# Índice:

---

.\*ndice:

# Objetivo:

---

   O objetivo desse documento é esclarecer o uso de conexão destino usando a [Carol](https://www.totvs.com/inteligencia-artificial/). Disponível a partir da versão 12.1.29.

# Introdução:

---

    TOTVS Carol é a plataforma de dados e inteligência artificial da TOTVS. Leia mais sobre a [Carol](https://www.totvs.com/inteligencia-artificial/).

    Nas versões mais recentes do RM é possível enviar dados para a Carol, através da ferramenta de Conceito (ETL). São suportadas todos os tipos de Conexões de Origem disponíveis no Conceito. E Para a conexão de destino é necessário configurar uma conexão Carol.

   É importante ter uma conta válida no sistema da Carol.

# Conexão:

---

    Veja abaixo um exemplo de como criar uma conexão com a Carol.

    Neste exemplo, o objetivo é enviar toda a tabela de Funcionários (PFUNC) para a Carol. Para isso, usamos uma conexão de origem de Banco de Dados, selecionando a tabela PFUNC e todos seus campos. Veja mais sobre esse tipo de conexão: .

   Passos para criar a conexão de destino com a Carol:

false1Conexão Carol

As informações a seguir deverão ser recuperadas do ambiente Carol.

O Token pode ser obtido conforme link a seguir: .

No exemplo acima não foi usado o token, mas um usuário e senha para autenticação. 

Os dados preenchidos foram obtidos diretamente da Carol, no connector:

Conexão Carol - Mensagem

Na aba Mensagem será configurado o schema da tabela do connector da Carol, onde os dados serão enviados.

**Dica:** Deixe a opção Formato gzip habilitada para melhorar o desempenho do processamento do conceito.  
Quando selecionado, os pacotes serão compactados para serem trafegados.

* Se o a tabela já existir no connector, basta clicar no botão 'Buscar Schema', que o schema da stagging será retornado:

* Se ele não existir, será retornada uma mensagem ao realizar o passo anterior: "Tabela não encontrada na staging!".

Para criar a tabela na staging, clique em 'Criar Schema'. O sistema listará todos os campos da conexão de Origem:

Selecione a(s) PK(s), remova os campos indesejados e clique em Criar Schema. Nesse momento, aguarde a confirmação que a tabela foi criada corretamente no connector da Carol.

Ligações

Por último, configure as ligações entre a tabela destino e origem.

Arraste primeiro a tabela de destino, depois a de Origem. Em seguida, clique no ícone 3, em destaque na imagem abaixo, para que as associações de campos sejam feitas automaticamente baseando-se no nome.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Conexões Destino: Carol

falsefalse

**Status:** Finalizado

false

**Data:** 25/08/2020
