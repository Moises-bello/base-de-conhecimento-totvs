---
article_id: 40240530824343
category: SIGAACD - Automação e Coleta de Dados
content_hash: b31028f19049b7b129bb7270c7f13cb4aa35a85f970ee093b47397534aa0e81f
fetched_at: '2026-06-28T22:39:11.202700+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDA100 - Ordem de
  Separação por Ordem de Produção
type: support-article
updated_at: '2026-05-05T16:24:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40240530824343-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDA100-Ordem-de-Separa%C3%A7%C3%A3o-por-Ordem-de-Produ%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40240530814359) Tempo aproximado para leitura: **00:04:30 min**  
  
**Dúvida**  
Como gerar Ordem de Separação por Ordem de Produção?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
A rotina Ordens de separação tem por objetivo gerar documentos para separação de materiais no estoque. Utilizada para separação de materiais que serão utilizados para fabricação de um produto acabado, vinculado a uma Ordem de Produção.

**Requisitos:**

1. Configurar os parâmetros do sistema
   1. Acessar o modulo Configurador
   2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
   3. Pesquise pelo parâmetro MV\_CBPE007
   4. Edite o parâmetro MV\_CBPE007
   5. Gravação das tabelas de Ordens de Separação do ACD com os dados da Nota Fiscal quando a mesma for gerada pelo Protheus.  
        
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-2-28_14-7-41.png?version=1&modificationDate=1552303997307&api=v2)  
        
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-2-28_14-12-35.png?version=1&modificationDate=1552303997407&api=v2)
2. Configurar Operador.

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > ACD> Operadores
   3. Clique Incluir
   4. Informe os campos obrigatórios

   ![](https://tdn.totvs.com/download/attachments/464947620/image2019-2-19_8-16-59.png?version=1&modificationDate=1552303987100&api=v2)

**Fluxo do Processo:**

1. Cadastrar local de estoque
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-2-19_8-32-26.png?version=1&modificationDate=1552303986437&api=v2)
   5. Clique Confirmar
2. Cadastrar produto
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
   3. Clique Incluir
   4. Informe os campos obrigatórios para o produto acabado  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_11-31-26.png?version=1&modificationDate=1552304001717&api=v2)
   5. Clique Confirmar
   6. Informe os campos obrigatórios para o produto Mataria Prima.  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-22_9-7-31.png?version=1&modificationDate=1553256527337&api=v2)
   7. Clique Confirmar
3. Cadastrar tipo de movimentação
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Movimentações > Internas
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-42-11.png?version=1&modificationDate=1552304002650&api=v2)
   5. clique Salvar
4. Cadastrar estrutura
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Engenharia  > Estruturas > Estruturas
   3. Clique Incluir
   4. Informe os campos obrigatórios para o produto acabado  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_11-42-14.png?version=1&modificationDate=1552304002240&api=v2)
   5. Clique Incluir
   6. Informe os campos obrigatórios para matéria prima.  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_11-42-48.png?version=1&modificationDate=1552304002337&api=v2)
   7. Clique em salvar, visualize na sequencia.  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_11-46-50.png?version=1&modificationDate=1552304002443&api=v2)
5. Cadastrar saldo.  
   a. Acessar o modulo Estoque/Custo  
   b. Acessar o Menu > Atualizações > Saldos > Inicial  
   c.Clique incluir

   ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-39-10.png?version=1&modificationDate=1552304002540&api=v2)

   d.Clique Salvar
6. Cadastrar ordem de produção

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Movimentações > Produção > Ordens de Produção
   3. Clique Incluir
   4. Informe os campos obrigatórios

   ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-44-56.png?version=1&modificationDate=1552304002747&api=v2)  
   e.clique salvar
7. Gerar Ordem de Separação.
   1. Acessar Modulo de Planejamento e controle de produção
   2. Acessar o Menu > Atualizações > ACD > Ordem de Separação
   3. Clique em Gerar.
   4. Será apresentado a tela de parâmetros selecione Ordem de Produção informe as opções.  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-54-18.png?version=1&modificationDate=1552304003390&api=v2)
   5. Clique em OK
   6. será apresentado segunda tela de parâmetros  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-54-49.png?version=1&modificationDate=1552304003490&api=v2)
   7. confirme OK
   8. Selecione a Ordem de Produção e clique em gerar.  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-1_13-56-5.png?version=1&modificationDate=1552304003587&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-8_15-23-33.png?version=1&modificationDate=1552304052923&api=v2)

      Inventário

1. A separação será realizada pelo Meu Coletor de dados.
2. Acessar Meu coletor de dados
   1. Acessar informando Login do operador.
   2. selecionar ordem de separação.  
        
      ![](https://tdn.totvs.com/download/attachments/464947620/transferenciainicio.gif?version=1&modificationDate=1552304053030&api=v2)
   3. realizar a conferencia do item.
3. ![](https://tdn.totvs.com/download/attachments/464947620/transferenciarealizada2.gif?version=1&modificationDate=1552304054200&api=v2)

8. Visualizar documento de entrada via Microsiga Protheus

1. Acessar o modulo Planejamento e controle de produção
2. Acessar o Menu > Atualizações> ACD> Ordem de Separação
3. Clique visualizar, verifique a separação realizada.  
     
   ![](https://tdn.totvs.com/download/attachments/464947620/image2019-3-11_14-55-38.png?version=1&modificationDate=1552327006097&api=v2)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
