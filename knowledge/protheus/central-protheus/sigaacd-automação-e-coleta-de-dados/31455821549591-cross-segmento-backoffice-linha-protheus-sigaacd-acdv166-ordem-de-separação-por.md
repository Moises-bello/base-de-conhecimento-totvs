---
article_id: 31455821549591
category: SIGAACD - Automação e Coleta de Dados
content_hash: ebc6e84b7e79c5688eea8aca24edd0e7503bd421f410c1a441dca790bfc5fe30
fetched_at: '2026-06-28T22:39:11.331481+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV166 - Ordem de
  Separação por Documento de Saída
type: support-article
updated_at: '2025-04-16T18:11:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31455821549591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV166-Ordem-de-Separa%C3%A7%C3%A3o-por-Documento-de-Sa%C3%ADda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31455775612183) Tempo aproximado para leitura: **HH:06:57 min** **Dúvida**O que é e como realizar a Ordem de Separação por Documento de Saída?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.

**Solução**

A rotina Ordens de separação tem por objetivo gerar documentos para separação de materiais no estoque.

- Nota Fiscal de Saída:  
- Utilizada para separar materiais de documentos já faturados.

**Fluxo do Processo:**

**![image2019-3-25_8-10-46.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31455775613975)**

**Configuração do Processo:**

Atenção

**Recursos Disponibilizado(s):**

Separação dos itens para posterior geração de Documento de saída via módulo de Faturamento

**Recursos não disponibilizado(s):**

Embalagem Simultânea

Embalagem

Gera Nota Via Coletor

Imprimir Nota

Imprimir Etiq. Volume

Embarque.

1. Configurar os parâmetros do sistema
   1. Acessar o modulo Configurador
   2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
   3. Pesquise pelo parâmetro MV\_CBPE007
   4. Edite o parâmetro MV\_CBPE007
   5. Gravação das tabelas de Ordens de Separação do ACD com os dados da Nota Fiscal quando a mesma for gerada pelo Protheus.  
        
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_14-7-41.png?version=1&modificationDate=1552303466967&api=v2)  
        
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_14-12-35.png?version=1&modificationDate=1552303467070&api=v2)
2. Configurar Operador.

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > ACD> Operadores
   3. Clique Incluir
   4. Informe os campos obrigatórios

   ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-19_8-16-59.png?version=1&modificationDate=1552303456770&api=v2)

**Exemplo prático utilizando o Protheus**

1. Cadastrar Cliente
   1. Acessar o modulo Faturamento
   2. Acessar o Menu > Atualizações > Cadastros > Clientes
   3. Clique Incluir
   4. Informe os campos obrigatórios![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_14-27-15.png?version=1&modificationDate=1552303467163&api=v2)
   1. Clique Salvar
2. Cadastrar condição de pagamento
   1. Acessar o modulo Faturamento
   2. Acessar o Menu > Atualizações > Cadastros > Condições de pagamentos
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-19_8-31-1.png?version=1&modificationDate=1552303455983&api=v2)
   5. Clique Confirmar
3. Cadastrar local de estoque

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-19_8-32-26.png?version=1&modificationDate=1552303456053&api=v2)Clique Confirmar
4. Cadastrar TES
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Movimentações > Fiscais > Tes
   3. Clique Incluir
   4. Informe os campos obrigatórios, informando os campos Tipo do TES igual a S-Saída, Atu.Estoque igual a S-Sim e Poder Terc. igual a N-Não Controla  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_14-42-49.png?version=1&modificationDate=1552303467730&api=v2)
   5. Clique Salvar
5. Cadastrar produto
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
   3. Clique Incluir
   4. Informe os campos obrigatórios para o produto acabado e o campo código de barras  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-3-22_9-59-38.png?version=1&modificationDate=1553259654950&api=v2)
   5. Clique Confirmar
6. Cadastrar saldo.  
   a. Acessar o modulo Estoque/Custo  
   b. Acessar o Menu > Atualizações > Saldos > Inicial  
   c.Clique incluir  
   ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-0-41.png?version=1&modificationDate=1552303467817&api=v2)  
   d.Clique Salvar
7. Cadastrar Pedido de venda
   1. Acessar o modulo Faturamento
   2. Acessar o Menu > Atualizações > Pedidos > Pedido de Venda
   3. Clique Incluir
   4. Informe os campos obrigatórios para o tipo de nota escolhido.
   5. Na grade de produtos deve ser informado a o item que será vendido .  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-13-14.png?version=1&modificationDate=1552303467953&api=v2)
   6. Faturar o Item  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-24-13.png?version=1&modificationDate=1552303468063&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-24-46.png?version=1&modificationDate=1552303468163&api=v2)![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-25-6.png?version=1&modificationDate=1552303468250&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-25-54.png?version=1&modificationDate=1552303468337&api=v2)![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-26-17.png?version=1&modificationDate=1552303468420&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-26-47.png?version=1&modificationDate=1552303468507&api=v2)
   7. ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-27-45.png?version=1&modificationDate=1552303468687&api=v2)
8. Gerar Ordem de Separação.  
   1. Acessar Modulo de Faturamento
   2. Acessar o Menu > Atualizações > ACD > Ordem de Separação
   3. Clique em Gerar.
   4. Será apresentado a tela de parâmetros selecione Nota fiscal informe as opções.  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-32-18.png?version=1&modificationDate=1552303468790&api=v2)  
        
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-33-29.png?version=1&modificationDate=1552303469073&api=v2)![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-33-52.png?version=1&modificationDate=1552303469170&api=v2)
   5. Clique em OK
   6. Será apresentado novo conjunto de parâmetros para o Meu Coletor de dados vamos deixar as configurações conforme abaixo:  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-35-13.png?version=1&modificationDate=1552303469273&api=v2)
   7. Selecione a ordem de separação e cliente em Gerar  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-2-28_15-36-38.png?version=1&modificationDate=1552303469377&api=v2)
   8. Visualize a Ordem de separação por documento de saída  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-3-8_15-53-56.png?version=1&modificationDate=1552303549437&api=v2)

      Inventário

      A separação será realizada pelo Meu Coletor de dados.
9. Acessar Meu coletor de dados
   1. Acessar informando login do operador.
   2. Selecionar ordem de separação.  
      ![](https://tdn.totvs.com/download/attachments/464946966/ordemdeseparadoclogin.gif?version=1&modificationDate=1552303493120&api=v2)
   3. Realizar a separação do item e finalizar ordem de separação.  
   ![](https://tdn.totvs.com/download/attachments/464946966/ordemdconferenciadoc.gif?version=1&modificationDate=1552303496350&api=v2)

9. Visualizar documento de entrada via Microsiga Protheus

1. 1. Acessar o modulo de Faturamento
   2. Acessar o Menu > Atualizações> ACD> Ordem de Separação
   3. Clique visualizar, verifique a separação realizada, no campo Status e Sld Separar.  
      ![](https://tdn.totvs.com/download/attachments/464946966/image2019-3-11_14-53-47.png?version=1&modificationDate=1552326895760&api=v2)

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 - Ordem de Separação por Pedido de Venda](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408423317399-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Ordem-de-Separa%C3%A7%C3%A3o-por-Pedido-de-Venda)*

[*Clique aqui e veja artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
