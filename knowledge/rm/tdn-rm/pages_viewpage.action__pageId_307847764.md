---
content_hash: f681ffa89db22cfc1b70b301814bff1a9d38934c7ccf019263005d04417eecd5
fetched_at: '2026-06-29T00:08:44.363496+00:00'
page_id: '307847764'
product: rm
source: tdn-rm
title: LookUp de Itens de Tabela Dinâmica
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=307847764
version: 12
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       O objetivo deste documento é mostrar como criar um LookUp do Metadados para os Itens de uma tabela dinâmica..

# Configuração:

---

      Para criar um LookUp de itens de tabela dinâmica é necessário que o metadados possua campos, para armazenar os campos chaves da tabela dinâmica que será escolhida.

Observação

**Tabelas dinâmicas que possue a coluna "NOMETABELA" a tabela "GCONSIST" é necessário criar os campos chaves abaixo para que o LookUp funcione:**

* **COLIGADA - Tipo INT16**
* **APLICACAO - varchar de tamanho 1**
* **CODIGO -  varchar de tamanho 10**

     Considerando que toda estrutura do metadados esteja criada até a camada de apresentação, acesse a guia Apresentação da camada de apresentação e selecione a coluna "**CODIGO**" e altere o tipo de controle para caixa de pesquisa.

     Selecione o campo "Action fonte de dados" utilize a action "**RMSUserFieldsConsistAction**".

     Após selecionar a action um componente de LookUp para as tabelas dinâmicas será apresentando. Escolha qual tabela dinâmica será utilizada.

     No exemplo foi utilizada a tabela "**SANGUE**".

Agora é necessário adicionar o relacionamento da action que será utilizada no LookUp.

Após configurar o relacionamento caso a tabela dinâmica escolhida utilize a tabela "GCONSIST" é necessário criar um filtro no LookUp para que o memso apresente somente os registros da tabela dinâmica escolhida.

Após configurar o LookUp basta seguir com a criação do projeto Metadados.

LookUp Funcionando o item da tabela dinâmica.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.18.151 ou superiores

false

**Processo:** Lookup Metadados

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
