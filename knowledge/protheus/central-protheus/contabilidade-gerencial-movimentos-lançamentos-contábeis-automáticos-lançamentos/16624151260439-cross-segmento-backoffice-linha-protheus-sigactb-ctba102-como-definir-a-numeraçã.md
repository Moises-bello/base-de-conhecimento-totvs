---
article_id: 16624151260439
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: 4ad56fb9eea0912b7bf10dd51e13e1a0da8c5e53ebf0806d17f39972f55a7275
fetched_at: '2026-06-28T22:40:32.439001+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 - Como definir
  a numeração inicial para o lote contábil.
type: support-article
updated_at: '2023-08-08T20:33:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16624151260439-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-Como-definir-a-numera%C3%A7%C3%A3o-inicial-para-o-lote-cont%C3%A1bil
---

**Dúvida :**

Como definir uma numeração inicial para o lote contábil.

**Solução**

A numeração do lote é o identificador do lançamento contábil. As informações nela inseridas, são utilizadas para localizar o lançamento contábil posteriormente.

Para definir um lote especifico na inclusão manual ou via integração de um lançamento contábil devera seguir os passos abaixo:

**1°** Configurar o parametro MV\_LOTECONT, para que busque a informação definida na tabela 09.

Conteúdo do parâmetro **MV\_LOTECON** = .**T**. O número do lote é gerado a partir da Tabela 09.

Conteúdo do parâmetro**MV\_LOTECON** = .**U**. O número do lote é o último número disponível no arquivo de Lançamentos Contábeis mais 1 para a data informada.

**2°** Definir e a numeração desejada na tabela 09 que serão posteriormente levadas para o lançamento contábil.

Acessar o configurador em:

Base de dados -> Dicionario -> Base de dados :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16623848823959)

Na tela aberta selecionar tabelas genéricas e filtrar por 09 :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16623853506839)

Ao realizar o filtro será exibida a tabela 09 onde ficam gravadas as informações padrões dos lotes de integração.

Após o filtro, basta selecionar o módulo que deseja definir a numeração inicial dos lotes dos Lançamento Contábil e selecionar editar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16623991228823)

Após a tela aberta selecionar Itens:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16624059451799)

Alterar a numeração do lote que deseja e selecionar salvar :

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16624035288983)

Após alteração conforme acima o sistema ira iniciar a numeração do lote contábil, para lançamentos manuais com 0001.

Saiba mais:

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102/ CTBA101 Campos da capa do Lote contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019073652-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-CTBA101-Campos-da-capa-do-Lote-cont%C3%A1bil?source=search)
