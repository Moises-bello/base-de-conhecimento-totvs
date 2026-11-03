---
article_id: 360011967491
category: Materiais - Compras (SIGACOM)
content_hash: 934c2402be63bc909dd97b115f8c07c55c8831d41adbf882705eb5755d4fa684
fetched_at: '2026-06-28T22:41:07.651831+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gerar Solicitação
  de Compras/Pedido de Compras por ponto de pedido?
type: support-article
updated_at: '2025-11-28T19:47:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011967491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-Solicita%C3%A7%C3%A3o-de-Compras-Pedido-de-Compras-por-ponto-de-pedido
---

**Dúvida**Como gerar Solicitação de Compras/Pedido de Compras por ponto de pedido ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Solução**

Ponto de Pedido é a quantidade em estoque que uma vez atingida, pode iniciar o processo de compra a partir da **Geração de Solicitações de Compras por ponto de pedido.**

Toda vez que o Sistema detectar a falta de um material, somando saldo em estoque, pedidos e solicitações de compras em aberto e esta for menor que o Ponto de Pedido definido em seu cadastro de Produto é gerado uma **Solicitação de Compras**.

**Configuração do Ponto de Pedido no cadastro de Produto:**

**![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008595311)**

Os campos B1\_EMIN e B1\_ESTSEG definirão sua configuração para Ponto de Pedido. O campo B1\_EMIN define a quantidade mínima pré-estabelecida que, uma vez atingida, ao processar a rotina de Solicitações por Ponto de Pedido, gera emissão de uma solicitação de compras, já o campo B1\_ESTSEG irá definir a quantidade mínima do produto em estoque para evitar a falta do mesmo entre a solicitação de compra e o seu recebimento.  
Após o produto entrar na condição de **Estoque de Segurança**, poderá ser processada a rotina **Reposição por Ponto de Pedido (MATA170).**A rotina **MATA170** tem por finalidade gerar automaticamente a Solicitação de Compras.

![Sem_t_tulo.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360008561372)

***Obs.1:***

Caso seja utilizada a opção ser gerado Pedido de Compras na rotina **MATA170** (imagem abaixo), deve -se fazer a amarração Produto x Fornecedor na rotina **MATA061**e também amarrar uma condição de pagamento no cadastro do fornecedor.

Caso tenha mais de um fornecedor no Cadastro do produto x fornecedor , o sistema irá escolher o Fornecedor que tiver a maior Nota para geração do Pedido.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8533387704215)

Assim ao selecionar no parâmetro a opção Pedido de Compras será gerado o pedido:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4414749329815)

***Obs.2:***

Ao informar um centro de custo no cadastro de produto será carregado para a SC ou PC a informação.

***Obs.3:***

Existe a possibilidade de configurar a rotina Solicitação por Ponto de Pedido MATA170 para ser executada automaticamente. Dessa forma, o usuário de compras não terá que acessar a rotina e executá-la manualmente. Caso se deseje, pode-se utilizar o agendamento da rotina pelo Schedule do Configurador para automatizar o processamento, conforme a necessidade. Com isso ela será executada de forma automática.

**[Framework - Linha Protheus - Schedule: agendando a execução de rotinas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028340252-Framework-Linha-Protheus-Schedule-agendando-a-execu%C3%A7%C3%A3o-de-rotinas)**

**[Configurando Schedule para a MATA170](https://tdn.totvs.com/display/public/PROT/PCOM10003+-+Configurando+Ponto+de+Pedido+-+Schedule#tabs-ID4)**

**Obs.4:** Quais informações o Protheus considera no cálculo da solicitação de compras por ponto de pedido e como o cálculo é efetuado:

[**Cálculo ponto de pedido**](https://tdn.totvs.com/pages/viewpage.action?pageId=893433046)

**Obs.5:** Geração de solicitação de compras, produto importado, por ponto de pedido:

**[Ponto de Pedido produto importado](https://tdn.totvs.com/pages/releaseview.action?pageId=715822248)**

**Obs.6:** Geração de solicitação por ponto de pedido considerando as filiais definidas na tabela SBZ

**[Solicitação por ponto de pedido considerando filiais na SBZ](https://tdn.totvs.com/pages/releaseview.action?pageId=967622877)**

**Obs.7:** A "DATA LIMITE PARA EMPENHO" é um campo utilizado para definir até quando uma quantidade de um produto deve permanecer reservada (empenhada) no estoque para atender a um Pedido de Venda, Solicitação de Compras ou Ordem de Produção.

O principal objetivo é liberar automaticamente o estoque que foi reservado, mas cujo faturamento ou atendimento não ocorreu até a data estipulada. Isso evita que o estoque fique "preso" indefinidamente por pedidos antigos ou cancelados, melhorando a disponibilidade de produtos para novas vendas.

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é realizado o cálculo de necessidade na rotina Ponto de Pedido?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27256450694935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-necessidade-na-rotina-Ponto-de-Pedido)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não está considerando Solicitação de Compras bloqueadas para o cálculo da necessidade na Rotina de solicitação de Compras por Ponto de Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27310881678615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-est%C3%A1-considerando-Solicita%C3%A7%C3%A3o-de-Compras-bloqueadas-para-o-c%C3%A1lculo-da-necessidade-na-Rotina-de-solicita%C3%A7%C3%A3o-de-Compras-por-Ponto-de-Pedido)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
