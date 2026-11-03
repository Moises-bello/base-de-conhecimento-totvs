---
article_id: 31453503005079
category: SIGAACD - Automação e Coleta de Dados
content_hash: 3d98e62e0e740f0120b2eb6aa47fa1ccb29bc1afe3566dc74a8946ae9e42bc86
fetched_at: '2026-06-28T22:39:11.290897+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV121 - Conferência
  Física por Documento de Entrada
type: support-article
updated_at: '2025-04-16T13:52:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31453503005079-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV121-Confer%C3%AAncia-F%C3%ADsica-por-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453502997399) Tempo aproximado para leitura: **00:03:10 min** **Dúvida**Como efetuar o processo de Conferência Física por Documento de Entrada?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**Esta rotina controla o material recebido, realizando a leitura do código de barras, conferindo com os dados da Pré-Nota de Entrada ou documento de entrada , verificando inconsistências e/ou realizando a entrada física dos materiais.

**Fluxo do Processo:**

**![image2019-3-25_8-22-43.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453502997527)**

**Configuração do Processo:**

Configurar os parâmetros do sistema

1. Acessar o modulo Configurador
2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
3. Pesquise pelo parâmetro MV\_CONFFIS
4. Edite o parâmetro MV\_CONFFIS
5. O campo Cont.Por. deve ser preenchido com "S" para que seja ativado a conferencia.  
   ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-18_10-38-57.png?version=1&modificationDate=1552075908423&api=v2)  
     
     

   Configurar os parâmetros do sistema

   1. Acessar o modulo Configurador
   2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
   3. Pesquise pelo parâmetro MV\_TPCONFF
   4. Edite o parâmetro MV\_TPCONFF
   5. O campo Cont.Por. deve ser preenchido com "2" para que seja ativado a conferência por pré-nota   
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-18_10-43-52.png?version=1&modificationDate=1552075908617&api=v2)

   Configurar Operador.

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > ACD> Operadores
   3. Clique Incluir
   4. Informe os campos obrigatórios

   ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-16-59.png?version=1&modificationDate=1552075909463&api=v2)

**Exemplo prático do processo utilizando o Protheus**

1. Cadastrar Fornecedor
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Fornecedores
   3. Clique Incluir
   4. Informe os campos obrigatórios![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-48-13.png?version=1&modificationDate=1552075910397&api=v2)  
   Na aba Outros colocar o campo Conf Fisica igual a 2.  
     
   ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-49-12.png?version=1&modificationDate=1552075910487&api=v2)
   1. Clique em confirmar.
2. Cadastrar condição de pagamento
   1. Acessar o modulo Faturamento
   2. Acessar o Menu > Atualizações > Cadastros > Condições de pagamentos
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-31-1.png?version=1&modificationDate=1552075910110&api=v2)
   5. Clique Confirmar
3. Cadastrar local de estoque

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-32-26.png?version=1&modificationDate=1552075910193&api=v2)
   5. Clique Confirmar
4. Cadastrar produto
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
   3. Clique Incluir
   4. Informe os campos obrigatórios para o produto acabado e configure produto com Lote.  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-34-0.png?version=1&modificationDate=1552075910263&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-3-8_17-22-25.png?version=1&modificationDate=1552076612487&api=v2)
   5. Clique Confirmar
5. Cadastrar TES
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Movimentações > Fiscais > Tes
   3. Clique Incluir
   4. Informe os campos obrigatórios, informando os campos Tipo do TES igual a E-Entrada, Atu.Estoque igual a S-Sim e Poder Terc. igual a N-Não Controla  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2018-10-15_18-21-20.png?version=1&modificationDate=1552075905900&api=v2)
   5. clique confirmar
6. Cadastrar documento de entrada
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Movimentações > Fiscais > Documento de entrada
   3. Clique Incluir
   4. Informe os campos obrigatórios para o tipo da nota escolhido.
   5. Na grade de produtos deve ser informado o item que foi recebido, e o lote do produto.  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-2-19_8-52-13.png?version=1&modificationDate=1552075910557&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-3-6_8-36-4.png?version=1&modificationDate=1552075931717&api=v2)
   6. clique salvar
   7. posicione no registro cadastrado.
   8. clique em visualizar
   9. observe que na aba de conferencia física o status da nota esta como não conferida.  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-3-11_14-45-9.png?version=1&modificationDate=1552326377573&api=v2)

      Conferência

      A conferência de item será realizada pelo Meu Coletor de dados.
7. Acessar Meu Coletor de dados.

   1. Acessar a opção conferência.
   2. Verificar as notas e selecionar

      Podendo selecionar o código de Chave de acesso Danfe pela pesquisa
   3. selecione a Doc/Danfe.  
      ![](https://tdn.totvs.com/download/attachments/464945570/DocConflogin.gif?version=1&modificationDate=1552075930017&api=v2)
   4. Selecionado o documento

      E possível realizar a seleção de vários documentos para uma conferência futura e seja online e offline.
   5. informe quantidade e lote encontrado  
      ![](https://tdn.totvs.com/download/attachments/464945570/DocConfrealizada.gif?version=1&modificationDate=1552075931790&api=v2)
8. Visualizar documento de entrada via Microsiga Protheus

   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Movimentações > Fiscais > Documento de entrada
   3. Clique visualizar, verifique a conferência na aba inferior da nota a quantidade conferida.  
      ![](https://tdn.totvs.com/download/attachments/464945570/image2019-3-11_14-46-20.png?version=1&modificationDate=1552326449173&api=v2)

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
