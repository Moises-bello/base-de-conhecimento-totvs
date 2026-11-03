---
article_id: 31293744179479
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: 94c38cae9e29b1c9c9a6cb23a86ffbf61fa9fafcde792fbc69d41d19afbe8341
fetched_at: '2026-06-28T22:39:09.562989+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 Limite de
  350 campos na tabela SB1
type: support-article
updated_at: '2025-04-09T19:32:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31293744179479-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Limite-de-350-campos-na-tabela-SB1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31293714528919) Tempo aproximado para leitura: **00:02:45 min** **Dúvida**

O que fazer quando atinge o **limite de campos** na rotina **CADASTRO DE PRODUTOS (MATA010)** e precisamos incluir novos campos customizados?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**

No padrão para o Cadastro de Produtos temos duas alternativas, vamos destacar abaixo:

***- 1 -*** Conforme [***documentação do framework***](https://tdn.totvs.com/x/WAPbAg) o número máximo de campos que podem ser criados em uma tabela é de 350. Essa é uma limitação estrutural do Protheus para garantia do funcionamento e compatibilidade com os bancos de dados homologados.

Caso seja necessário a utilização de um número maior de campos, é recomendável o uso de tabelas auxiliares. As tabelas auxiliares criadas por usuário devem possuir tratamento para ser consultada / alimentada via pontos de entrada contidos na rotina em questão, para desta forma, servir como auxiliar no tratamento da regra desejada.

**Importante:** Toda criação e manutenção de tabelas deve ser realizada exclusivamente pelas ferramentas disponibilizadas no módulo Configurador, bem como, toda manipulação de dados nas tabelas, exclusivamente via processamento. Não se recomenda quaisquer procedimentos diretamente no banco de dados.

No caso de criação de novos campos por parte da TOTVS, os mesmos serão adicionados na tabela através do UPDDISTR, podendo assim ultrapassar o limite de 350, tornando a tabela indisponível para criação de novos campos customizados.

***- 2 -*** É possível utilizar também a **tabela SB5** da rotina de **Complemento de Produtos (MATA180)** para inclusão de novos campos conforme necessidade específica, uma dica, utilizar em conjunto com o **[parâmetro MV\_CADPROD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)** informando a tabela SB5 para que o Cadastro de Complemento seja exibido no Cadastro do produto, facilitando assim a visualização dos campos desejados.

Saiba Mais:

[SIGAEST - MATA010 - Quais são os Pontos de Entrada da rotina de Cadastro de Produtos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003591241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Produtos)

[Clique aqui e veja mais artigos sobre CADASTROS E CONFIGURAÇÕES GERAIS no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)

[SIGAEST - Utilidade e configuração do parâmetro MV\_CADPROD](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016068032-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Utilidade-e-configura%C3%A7%C3%A3o-do-par%C3%A2metro-MV-CADPROD)
