---
article_id: 31453142889879
category: SIGAACD - Automação e Coleta de Dados
content_hash: aa2a27bdfa3b9fc29c80bb700759ee534af54f30d89bc57beb032d1ff007fce2
fetched_at: '2026-06-28T22:39:11.273138+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - ACDV120 - Processo
  de Conferência por Pré-Nota
type: support-article
updated_at: '2026-03-27T18:37:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31453142889879-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-ACDV120-Processo-de-Confer%C3%AAncia-por-Pr%C3%A9-Nota
---

O processo de Conferência Física por Pré-Nota de Entrada no TOTVS Protheus envolve configurar parâmetros do sistema, cadastrar operador, fornecedor, local de estoque, produto e pré-nota. A conferência é realizada via Meu Coletor de Dados, lendo códigos de barras e verificando quantidades. Resultados são visualizados no módulo Estoque/Custos. O código de barras do produto é único e não vincula fornecedor, sendo possível registrar melhorias na Central Colaborativa TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453128025623) Tempo aproximado para leitura: **00:03:12 min**  
  
**Dúvida**  
Como é feito o processo de Conferência Física por Pré-Nota de Entrada?  
  
**Ambiente**  
  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Automação e Coleta de Dados - Todas as versões.  
  
**Solução**  
Esta rotina controla o material recebido, realizando a leitura do código de barras, conferindo com os dados da Pré-Nota de Entrada ou documento de entrada , verificando inconsistências e/ou realizando a entrada física dos materiais.

**Fluxo do Processo:**

![image2019-3-25_8-22-1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31453128026007)

**Configuração do Processo:**

Configurar os parâmetros do sistema

1. Acessar o modulo Configurador
   1. Acessar o Menu > Ambiente > Cadastros > Parâmetros
   2. Pesquise pelo parâmetro MV\_CONFFIS
   3. Edite o parâmetro MV\_CONFFIS
   4. O campo Cont.Por. deve ser preenchido com "S" para que seja ativado a conferencia.  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-18_10-38-57.png?version=1&modificationDate=1550497193753&api=v2)
2. Configurar os parâmetros do sistema  
   1. Acessar o modulo Configurador
   2. Acessar o Menu > Ambiente > Cadastros > Parâmetros
   3. Pesquise pelo parâmetro MV\_TPCONFF
   4. Edite o parâmetro MV\_TPCONFF
   5. O campo Cont.Por. deve ser preenchido com "1" para que seja ativado a conferencia por pré nota

      Esse parâmetro é opcional pois a configuração pode ser feita no cadastro de fornecedor como será demonstrado no exemplo pratico.

      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-18_10-41-4.png?version=1&modificationDate=1550497320047&api=v2)
3. Configurar Operador.
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > ACD> Operadores
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-16-50.png?version=1&modificationDate=1550575066947&api=v2)

**Exemplo prático do processo utilizando o Protheus**

1. Cadastrar Fornecedor
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Fornecedores
   3. Clique Incluir
   4. Informe os campos obrigatórios  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-19-16.png?version=1&modificationDate=1550575213117&api=v2)
   5. Na aba Outros colocar o campo Conf Física colocar igual a 0.  
        
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-19-40.png?version=1&modificationDate=1550575236620&api=v2)
2. Cadastrar local de estoque
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos > Locais de estoque
   3. Clique Incluir
   4. Informe os campos obrigatórios  
        
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-20-51.png?version=1&modificationDate=1550575308163&api=v2)
3. Cadastrar produto
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Atualizações > Cadastros > Produtos >Produto
   3. Clique incluir
   4. Informe os campos obrigatórios e campo de código de barras.  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-26-9.png?version=1&modificationDate=1550575626340&api=v2)  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-3-11_14-48-48.png?version=1&modificationDate=1552326596293&api=v2)
4. Cadastrar Pré Nota de entrada  
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Movimentações > Fiscais > Pré-Nota
   3. Clique Incluir
   4. Informe os campos obrigatórios e o fornecedor cadastrado para a conferencia por Pré-nota de entrada
   5. Na grade de produtos deve ser informado o item criado para conferência.  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-2-19_8-28-28.png?version=1&modificationDate=1550575765023&api=v2)
   6. Confirme.
   7. Posicione no registro cadastrado.
   8. Clique Visualizar
   9. Observe que na aba de conferencia física o status da nota esta como não conferida.  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-3-11_14-49-45.png?version=1&modificationDate=1552326653803&api=v2)

      Conferencia

      A conferencia de item será realizada pelo Meu Coletor de dados.
5. Acessar o Meu Coletor de dados

   1. Acessar o Conferência
   2. Verificar as notas e selecionar

      Podendo selecionar o código de Chave de acesso Danfe pela pesquisa.
   3. Clique na Danfe.  
      ![](https://tdn.totvs.com/download/attachments/455809138/LoginACD.gif?version=4&modificationDate=1551467797117&api=v2)
   4. Selecione o documento.
   5. Realize a conferência
   6. Clique no código de barras informe a quantidade e finalize a conferencia.

      ![](https://tdn.totvs.com/download/attachments/455809138/ConferenciaMobile%20-%20Copia.gif?version=1&modificationDate=1551469158913&api=v2)

      Nova Funcionalidade

      A partir da versão 1.0.34 é possível informar a data de validade do lote do produto na conferência através do campo Data de Validade, adicionado ao formulário de conferência.
6. Visualizar documento de entrada via Microsiga Protheus.
   1. Acessar o modulo Estoque/Custos
   2. Acessar o Menu > Movimentações > Fiscais > Pré-Documento de Entrada
   3. Clique visualizar, verifique a conferência realizada na aba conferência no rodapé e a quantidade conferida.  
      ![](https://tdn.totvs.com/download/attachments/455809138/image2019-3-11_14-51-21.png?version=1&modificationDate=1552326749533&api=v2)

Observação: 

O campo código de barras da rotina Produto x Fornecedor não está sendo realizado a leitura, na rotina de conferência ACDV120, como resolver para ler o código de barras do Produto x Fornecedor?

**Resposta:** Hoje no padrão, não é possível realizar o processo solicitado. O campo utilizado para código de barras do produto é o B1\_CODBAR, e nele só é possível incluir um único código de barra para o produto. Onde esse não possui vínculo com o fornecedor.  
   
Para vínculo com o fornecedor, somente o código do Produto x Fornecedor com o campo A5\_CODPRF na rotina de Compras. **Porém, esse não tem relação com o código de barras do produto.**  
   
Segue documentação para mais informações:  
<https://tdn.totvs.com/display/public/PROT/Campo+B1_CODBAR+do+Cadastro+de+Produtos>

Segue os pontos de entrada do cadastro do produto.  
   
[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA010 - Quais são os Pontos de Entrada da rotina de Cadastro de Produtos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003591241-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA010-Quais-s%C3%A3o-os-Pontos-de-Entrada-da-rotina-de-Cadastro-de-Produtos)  
   
E segue também os pontos de entrada do cadastro do produto x fornecedor.   
   
[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Pontos de Entrada Produto x Fornecedor - MATA060 e MATA061](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038803433-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Pontos-de-Entrada-Produto-x-Fornecedor-MATA060-e-MATA061)

Caso deseje pode registrar uma melhoria na  [**Central Colaborativa TOTVS**](https://centraldeatendimento.totvs.com/hc/pt-br/community/topics), segue para maiores informações:

Para conhecer mais sobre as suas **funcionalidades** clique [**AQUI**](https://www.youtube.com/watch?v=LTqWbDsBb6s&list=PLYQXMbUS13r-xtKThVYHMFsLK3ezvpo3q&index=13)e assista o nosso vídeo ou acesse nosso artigo [**Central Colaborativa - Funcionalidades Disponíveis**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039466814-Funcionalidades-Dispon%C3%ADveis-na-Central-Colaborativa-TOTVS)**​**.

Você pode acompanhar as suas **sugestões** e **comentários** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/contributions/posts?locale=pt-br)**.**

Acompanhe as **Novidades da Release** clicando [**AQUI**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360009734433-Ciclo-de-Vida-Relat%C3%B3rio-de-Releases).

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
