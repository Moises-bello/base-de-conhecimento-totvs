---
content_hash: af453e7b34e397fb3f7f6dd46c4ddfa7e819dae31a4b6a298b9fbf861b024900
fetched_at: '2026-06-29T00:09:37.989608+00:00'
page_id: '425459663'
product: rm
source: tdn-rm
title: Relacionamento entre Tabelas
type: documentation
url: https://tdn.totvs.com/display/LRM/Relacionamento+entre+Tabelas
version: 3
---

**Relacionamento entre Tabelas**

---

Nas Estruturas Origem e Destino é possível adicionar mais de uma tabela para montar as estruturas das conexões criadas.  
    
 A primeira tabela adicionada é considerada como a tabela principal, e será reconhecida normalmente no momento de realizar as correspondências, diferente das outras tabelas que não serão apresentadas. Para que as demais tabelas sejam identificadas é necessário realizar o relacionamento entre as mesmas com a tabela principal.  
    
 Ao clicar no lookup Detalhes, uma visão é aberta para que se possa realizar este relacionamento. No lado esquerdo da visão são mostrados os relacionamentos existentes, e abaixo estão disponíveis os botões Add e Remove, para adicionar um relacionamento ou remover o relacionamento selecionado, respectivamente.  
    
 No lado direito estão disponíveis os campos para configurar o relacionamento. Os campos são:  
    
 **Relacionamento**

* **Campos:** Vincular o campo da tabela com o campo da tabela mestre.  
   Ao clicar no lookup Campos para vincular o campo da tabela com o da tabela mestre, uma visão é aberta para informar os mesmos. No lado esquerdo da visão são mostrados os campos que já foram criadas as correspondências.   
   Abaixo estão disponíveis os botões Add e Remove, para adicionar um campo ou remover o campo selecionado, respectivamente.Do lado direito estão disponíveis os campos:
  + Detalhe:\* Campo da tabela que deverá fazer correspondência com o campo da tabela mestre.
  + Mestre:\* Campo da tabela mestre.
* **Cardinalidade:** Informe se o relacionamento será de um para muitos, ou de um para um.  
  **Tabela**
* Detalhe:\* Informe a tabela que deverá ter um relacionamento com a tabela mestre.

* Nome:\* Campo do tipo somente leitura, onde consta o nome da tabela mestre do relacionamento que está sendo criado

***Observação:***

Para que a configuração possar ser realizada corretamente, é necessário primeiro informar a tabela no campo Detalhe, para depois informar os campos e a cardinalidade em Relacionamento.  
   
***Dica:***

Ao criar mais de uma Conexão Origem, pode-se apontar na aba Estrutura Origem os recursos da segunda conexão, acrescentando as tabelas na estrutura conforme demonstrado.

---

**Como Fazer**

[Blog - Como Fazer: Criando um Relacionamento entre Tabelas Mestre-Detalhe](http://totvsconnect.blogspot.com/2011/07/como-fazer-conceito-com-relacionamento)
