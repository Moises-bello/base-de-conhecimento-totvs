---
content_hash: 32dcd0ebdbfbe4b714c74db61093b538439059ca0d2d5a7632c82cf07cc30b6b
fetched_at: '2026-06-29T00:10:26.914191+00:00'
page_id: '515305934'
product: rm
source: tdn-rm
title: Regras de Exclusão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=515305934
version: 16
---

# Índice:

---

.\*ndice:

# Objetivo:

---

          O objetivo desse documento é esclarecer o funcionamento do recurso Regras de Exclusão, disponível para Conexões de Destino dos tipos Banco de Dados ou DataServer.

# Introdução:

---

         Para habilitar a aba "Regras de Exclusão", deve ser marcada a opção "Permitir a exclusão dos registros" na configuração da Conexão de Destino.

         A Regra de Exclusão serve para definir quais campos preenchidos com determinado valor não serão executados pelo Conceito.

         Por exemplo, para uma conexão de Destino DataServer, posso usar a Regra de Exclusão para **não inserir** os registros da origem com descrição igual a "1234", ou até mesmo **deletar** da conexão de destino os registros com esse mesmo valor.

# Exemplo:

---

         Ao marcar a propriedade "**Excluir os dados de acordo com a seguinte regra**", serão habilitados os recursos "Valor do Campo" e "Campos de Controle" para edição.

***Valor do Campo:***Onde será digitado o texto a ser aplicado pela regra de exclusão.

***Campos de Controle:***Campos que irão validar o texto digitado em Valor do Campo.

         No exemplo, foram utilizados campos da tabela TUND, informados na Conexão de Origem de um Arquivo TXT.

         Dessa forma, de acordo com a regra imposta, somente os registros de código NISTA e LJOST serão importados, uma vez que a regra será aplicada **apenas** quando a descrição informada for "**1234**".

         Serão **excluídos** os registros **já existentes** na Conexão de Destino que respeitem a condição definida na Regra de Exclusão.

         Os id’s considerados para exclusão serão buscados no destino e caso existam serão deletados. (*No exemplo, acima:  Registros de id 1 e 2, deveriam ser excluídos conforme a regra. Entretanto, como no destino só existe o registro de id 1, somente este será excluído*)

         Mesmo que no destino a regra de exclusão seja verdadeira (*id’s 3, 4 e 5*), eles não serão excluídos! Já que na origem eles possuem valor que não atende a regra de exclusão.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.XX

false

**Processo:** Regras de Exclusão

falsefalse

**Status:** Finalizado

false

**Data:** 18/09/2019

false

**Autores:**
