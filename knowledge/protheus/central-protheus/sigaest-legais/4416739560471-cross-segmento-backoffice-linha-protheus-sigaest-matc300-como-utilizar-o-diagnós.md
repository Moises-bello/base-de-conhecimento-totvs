---
article_id: 4416739560471
category: SIGAEST - LEGAIS
content_hash: 462bb7e5ab084c732c832059fb66550ac3fc3204b1ac611653b455a056eda141
fetched_at: '2026-06-28T22:38:51.733781+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC300 - Como utilizar
  o Diagnóstico do Bloco K?
type: support-article
updated_at: '2021-12-22T12:03:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416739560471-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC300-Como-utilizar-o-Diagn%C3%B3stico-do-Bloco-K
---

**Dúvida**Como utilizar o Diagnóstico do Bloco K para análise de possíveis problemas na geração do mesmo no SPED?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**Introdução**

O rotina Diagnóstico do Bloco K ajuda na detecção de possíveis problemas que possam gerar divergências na geração dos registros do Bloco K referentes ao arquivo SPED FISCAL a ser enviado para o governo.

Para a geração do Bloco K, o Protheus se baseia em diversos processos padrões e se estes não estiverem devidamente estruturados ou forem usados inadequadamente é possível que sejam encontradas divergências ao gerar o arquivo.

Na tela são exibidas as possíveis divergências baseadas em regras especificas, as quais permitem ao usuário avaliar e tomar as medidas necessárias para realizar as correções.

Para acessar o programa basta entrar no módulo de Estoque/Custos, no menu **Consultas** > **Cadastros**> **Diagnóstico Bloco K (MATC300)**.

**Importante:** este programa não identifica problemas na transmissão do arquivo, apenas possíveis divergências na consistência dos dados, parametrização e processos referentes ao Bloco K

**Processamento paralelo**

Por se tratar de um grande volume de dados, cada regra é executada em uma thread de processamento diferente. Com isso é possível consultar os dados, não somente ao fim do processamento, mas durante a coleta.

Note no exemplo abaixo que, ao clicar no botão **Processar** na opção do menu **Início,** ainda é possível interagir com as regras disponíveis no menu.

![](https://tdn.totvs.com/download/attachments/442045336/03%20Processamento.gif?version=1&modificationDate=1544648698617&api=v2)

**Ícones de status**

![](https://tdn.totvs.com/download/thumbnails/442045336/image2018-12-10_18-8-28.png?version=1&modificationDate=1544476434153&api=v2) Carregando: Indica que existe uma thread processando os registros da regra.

![](https://tdn.totvs.com/download/thumbnails/442045336/image2018-12-10_18-9-50.png?version=1&modificationDate=1544476434097&api=v2) Alerta: Indica que o processamento terminou e encontrou ocorrências referentes à regra.

![](https://tdn.totvs.com/download/thumbnails/442045336/image2018-12-10_18-10-58.png?version=1&modificationDate=1544476434053&api=v2) Correto: Indica que o processamento terminou e não foram encontradas ocorrências referentes à regra.

*Observação*: No caso da regra **Configurações Para Envio** o status apenas poderá ser **Carregando** ou **Correto** pois trata-se de uma regra informativa, não apontando nenhuma inconsistência, conforme será visto mais adiante.

**Página Inicial e Filtros**

### Início

Ao acessar o programa será exibida a tela de início.

Basta preencher os filtros e clicar no botão **Processar**.

![](https://tdn.totvs.com/download/attachments/442045336/01%20Abertura.gif?version=1&modificationDate=1544646977353&api=v2)

### 

### Filtros

**Período:**o período diz respeito ao mês da apuração, ou seja, para as regras que utilizam periodicidade será considerado o mês informado nesse parâmetro.

Exemplo: **Fev**

**Ano:** espera como entrada o ano que será considerado na apuração das divergências. Deve ser inserido no formato de 4 (quatro) dígitos (aaaa).

Exemplo: **2018**

**Data De/Até:** Os campos de data são apenas informativos. Eles exibem as datas que correspondem ao período, ou seja, o primeiro e o último dia do mês.

Exemplo: no período de fevereiro do ano de 2021, o campo **Data de** exibirá **01/02/2021** e o campo **Data até** exibirá **28/02/2021**.

**Regras**

Com exceção de **Configurações Para Envio,** cada regra representa uma possível inconsistência e todas elas estão disponíveis para consulta durante e após o processamento do diagnóstico.

Em cada regra é possível navegar entre os itens com divergências e os pontos a serem verificados.

**Configurações para Envio**

Esta regra exibe os parâmetros que impactam nos processos envolvidos no Bloco K. Para cada parâmetro é possível ver sua descrição conforme o cadastro de parâmetros, o seu conteúdo e os detalhes de uso e impactos no sistema.

Diferentemente do cadastro de parâmetros no configurador, esta regra não permite alterações no conteúdo dos parâmetros, ou seja, é apenas informativa.

No lado esquerdo da tela é exibida uma tabela contendo a lista de parâmetros e no lado direito é exibida a descrição padrão do parâmetro selecionado, o conteúdo atual e o detalhe da aplicação do parâmetro no sistema.

![](https://tdn.totvs.com/download/attachments/442045336/04%20Configuracoes%20Para%20Envio.gif?version=1&modificationDate=1544827208113&api=v2)

**Estoque Negativo**

Esta regra exibe os itens que estão com o saldo negativo no estoque no período de apuração informado.

No centro da tela é exibida uma tabela contendo o armazém, o código do item e o saldo negativo do item. Na parte inferior esquerda é exibida a descrição do problema e na parte inferior direita são exibidos os itens a serem verificados.

![](https://tdn.totvs.com/download/attachments/442045336/02%20Regras.gif?version=1&modificationDate=1544647441017&api=v2)

**Amarração do Produto**

Esta regra exibe as ordens de produção de terceiros que não possuem amarração, isto é, produto diretamente relacionado ao cliente ou produto amarrado utilizando a rotina de **Produção de Terceiros (MATA037).**

No centro da tela é exibida uma tabela contendo o código da ordem de produção e a legenda informando o status da amarração. Na parte inferior esquerda é exibida a descrição do problema e na parte inferior direita são exibidos os itens a serem verificados.

![](https://tdn.totvs.com/download/attachments/442045336/05%20Amarracao%20do%20Produto.gif?version=1&modificationDate=1544827477297&api=v2)

**Desmontagem**

Esta regra exibe os itens que foram desmontados e possuem alguma divergência.

No centro da tela é exibida uma tabela contendo o documento de movimento, o item, o código sequencial do movimento e a legenda informando o status da desmontagem. Na parte inferior esquerda é exibida a descrição do problema e na parte inferior direita são exibidos os itens a serem verificados.

**Importante:** para esta regra são considerados apenas os itens desmontados pelo processo padrão, isto é, no programa **Desmontagem (MATA242)**.

![](https://tdn.totvs.com/download/attachments/442045336/06%20Desmontagem.gif?version=1&modificationDate=1544827645823&api=v2)

**OP. de Retrabalho**

Esta regra exibe as ordens de produção que foram cadastradas com o tipo de produção igual a retrabalho, tiveram apontamentos no período parametrizado, porém, não foram identificadas movimentações para um produto de retrabalho.

No centro da tela é exibida uma tabela contendo o código e o produto da ordem de produção. Na parte inferior esquerda é exibida a descrição do problema e na parte inferior direita são exibidos os itens a serem verificados.

![](https://tdn.totvs.com/download/attachments/442045336/op_retrabalho_validador.PNG?version=1&modificationDate=1549458485347&api=v2)

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
