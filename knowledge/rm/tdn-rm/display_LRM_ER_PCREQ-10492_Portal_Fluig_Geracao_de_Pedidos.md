---
content_hash: 23263d01fd129ecc10c979dd618901758fa6324b7c41bcaf9f42b8b7a6281bff
fetched_at: '2026-06-29T00:08:03.397484+00:00'
page_id: '235320288'
product: rm
source: tdn-rm
title: ER_PCREQ-10492_Portal_Fluig_Geracao_de_Pedidos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-10492_Portal_Fluig_Geracao_de_Pedidos
version: 161
---

Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.
Informações Gerais
Especificação
Produto
TOTVS Obras e Projetos
Módulo
Pedido de Material
Segmento Executor
Construção e Projetos
Projeto
R_C&P_TOP011
IRM
PCREQ-10491
Requisito
PCREQ-10492
Subtarefa
PDR_CP_TOP011-72
Release de Entrega Planejada
12.1.11
Réplica
Não
País
( X ) Brasil  (  ) Argentina  (  ) México  (  ) Chile  (  ) Paraguai  (  ) Equador
(  ) USA  (  ) Colômbia   (  ) Outro _____________.
Outros
Pré-requisitos para melhor entendimento da especificação
Entidade
Link para o Wikihelp
Pedidos de Material
http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJGeracaoPedidosSuprFat.aspx
Objetivo
Migração da funcionalidade de Geração de Pedido de Material para o ambiente Fluig utilizando o TOTVS HTML Framework.
Definição da Regra de Negócio
TOTVS HTML
Framework
O TOTVS | HTML
Framework
foi concebido para tratar apenas a camada de interface das aplicações, confiando que os produtos por trás da interface irão conceder a infraestrutura e a implementação mínima dos serviços para utilização do
Framework
.
Ela tem como objetivo:
Fornecer uma Infraestrutura de componentes visuais e de serviços (de interface) HTML5;
Prover uma IDE de desenvolvimento HTML5, baseada no TDS (
TOTVS Developer Studio
);
Disponibilizar um Template de CRUD responsivo com respectivo acelerador no TDS, baseado em Serviços providos pelos produtos;
Estruturar um ambiente de desenvolvimento compatível com o Fluig e que possa ser utilizado por todos os produtos TOTVS.
A arquitetura pode ser resumida de acordo com a imagem a baixo:
Mais informações sobre o TOTVS HTML Framework:
tec:TOTVS
Fluig
No mundo dos negócios, onde as empresas precisam ter controle sobre suas operações e, ao mesmo tempo, agilidade para atender aos diversos processos que acontecem simultaneamente, a forma de interação mudou. A comunicação e os procedimentos são determinados, mas não rígidos, e a única constância é justamente a mudança e tudo precisa estar em nossas mãos.
Entendendo a mudança no comportamento dos indivíduos no ambiente corporativo e as demandas tecnológicas, a TOTVS criou a plataforma fluig com o objetivo de centralizar em uma única tela todos os processos, documentos e sistemas com um único login em uma interface de comunicação colaborativa.
Em resumo Fluig é uma plataforma de produtividade e colaboração que unifica a gestão de processos, documentos e identidades.
Mais informações sobre o Fluig nos links:
http://tdn.totvs.com/display/public/fluig/Sobre+o+Fluig
http://www.fluig.com/
Geração de Pedido de Material - Cadastros e Anexos
O modulo de Requisição de Material permite gerar movimentos do tipo Requisição de Material no TOTVS Gestão de Estoque, Compras e Faturamento dos produtos e serviços necessários para execução da Ordem de serviço caso não exista os produtos em estoque. Através desse modulo é possível gerar uma solicitação de compra ou uma ordem de compra para o sistema TOTVS Gestão de Estoque, Compras e Faturamento.
Migração
Para a funcionalidade de cadastro do Pedido de Material no TOTVS Obras e Projetos s
erão desenvolvidas telas Web utilizando o TOTVS HTML Framework.
Uma vez que as telas Web forem desenvolvidas, estas serão inseridas na plataforma Fluig para que o usuário possa ter um acesso mais ágil e prático da funcionalidade.
Serão desenvolvidas todos os cadastros e visões de anexo para o Pedido de Material da seguinte forma:
Tela com a listagem dos pedidos salvos na base de dados com opções
para editar, visualizar e excluir ;
Tela com os detalhes do Pedido;
Histograma Discriminado
Histograma Agrupado
Histograma Resumo
Item de Pedido de Material
Movimento
A
página
com um formulário para Editar os itens do Pedido.
Listagem de Pedidos
Na tela de listagem dos Pedidos serão mostradas as seguintes informações (
):
Código do Pedido
Data da Requisição
Status Geração
Tipo de Requisição
Todas as informações na listagem estarão ordenadas pela data de Requisição de forma decrescente e haverá um campo para pesquisar pelo campo Código do Pedido. A partir da página de listagem de pedidos será possível editar ou excluir os pedidos (
).
Detalhes do Pedido
Quando o usuário estiver visualizando um Pedido de Material haverá os Anexos na própria página de detalhes:
Item de Pedido de Material -
-   Caso o usuário queira editar um Item do pedido basta clicar no ícone
que aparecerá um pop-up, de acordo com o
Histograma discriminado -
Histograma Agrupado -
Protótipo 04
Histograma Resumo -
Protótipo 05
Movimento
-
Protótipo 06
A página de detalhes mostra as informações do pedido de Material, observando que em nenhum anexo terá a execução de processo como é feito no Winform.
A página com um formulário para Editar os itens do Pedido
Com o pedido já criado, a página web redirecionará para pagina de edição do pedido, com as informações mostradas no
.
Geração de
Pedido de Material - Processos
Para os processos do Pedido de Material no TOTVS Obras e Projetos serão desenvolvidas telas Web utilizando o TOTVS HTML Framework.
Serão migados todos os processos que envolvem o Pedido de Material:
Pedido de Material
Processo: Criação do Pedido de Material
Processo: Rateio de Produtos
Processo: Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) movimento.
Processo: Importar preços cotados
Processo: Excluir Movimentos
Processo: Envia pedido para  Suprimentos/Faturamento gerando 1 (um) mov. por data de entrega
Anexo Histograma Agrupado
Processo: Agrupar
Anexo Histograma Resumo
Processo: Alterar dados do item
Anexo Item do Pedido de Material
Processo: Pedido de Material Extra
Processo: Alterar dados de Itens
Processo: Atualização da Quant. Solicitada em grupo
Processo: Rateio de Contrato
Movimento
Processo: Rastreamento de movimento
Processos do Pedido de Materia
l
Criação do Pedido de Material
Na  migração deste processo para HTML, foi proposto a mudança de usabilidade do modulo, esta mudança visa maximar a produtividade do usuário na criação do pedido de material. O processo de criação do pedido pela plataforma Windows é composto de 6 passos:
Origem dos dados
Intervalo de períodos, tarefas e tipo de requisição
Seleção de tarefas
Seleção do Grupo de custo
Visão de insumo não utilizados (caso contenha este tipo de estrutura)
Seleção de insumos que farão parte do pedido
Para a migração deste processo foi definido 3 passos:
Origem dos dados, Períodos, Tipo de requisição(
)
Seleção das tarefas(
)
Seleção de Grupo de Custo e Insumos (
).
É importante reforçar que todas as regras definidas na plataforma Windows, também estarão embutidas no Totvs HTML Framework.
Rateio de produto
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML e para sua execução na web seguirá os seguintes passos:
Acesso ao Rateio (
)
Filtro de Insumo, Tarefa, Período e Rateio de produto (
)
Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) movimento.
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML:
Acesso ao processo(
)
Envia pedido para Suprimentos/Faturamento gerando apenas 1 (um) mov. por data de entrega
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML.
Acesso ao processo(
)
Excluir Movimento
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML.
Acesso ao processo(
)
Importar preços cotados.
Na  migração deste processo para HTML, foi proposto a mudança de usabilidade do modulo, esta mudança visa maximizar a produtividade do usuário na importação de preço cotado. O processo de importar preços cotados pela plataforma Windows é composto de 2 passos:
Tipos de Cotação
Seleção de insumo.
Para a migração deste processo foi definido apenas 1 passo:
Tipos de cotação e Seleção de insumo (
).
Processo do Anexo de Histograma Agrupado
Agrupar
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML. (
e
)
Processo do Anexo de Histograma Resumo
Alterar dados do item
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML. (
e
)
Processos do Item do Pedido de Material
Pedido de Material Extra
Na  migração deste processo para HTML, foi proposto a mudança de usabilidade do modulo, esta mudança visa maximizar a produtividade do usuário na geração do Pedido Extra. O processo de Gerar Pedido Extra pela plataforma Windows é composto de no máximo 4 passos:
Seleção de Filtro
Caso o usuário selecione  o filtro de Tarefas
Caso o usuário selecione o Filtro de Períodos
Seleção dos itens de Pedido
Para a migração deste processo, definimos apenas 1 passo:
Seleção de Filtros (
e
)
Alterar dados de Itens
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML.
(
P
rotótipo 13.1
e
13.2
)
Atualização da Quant. Solicitada em grupo
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML. (
e
)
Rateio de Contrato
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML. (
e
)
Processo do Anexo de Movimento
Rastreamento de movimento
Este processo seguirá a mesma estrutura tanto na plataforma Windows quanto no ambiente HTML. (
e
)
Protótipo de Tela
Protótipo 01
Protótipo 02
Protótipo 02.1
Protótipo 03
Protótipo 04
Protótipo 05
Protótipo 06
Protótipo 07
Protótipo 08
Protótipo 08.1
Protótipo 08.2
Protótipo 09
Protótipo 09.1
Protótipo 10
Protótipo 10.1
Protótipo 10.2
Protótipo 11
Protótipo 12
Protótipo 12.1
Protótipo 13
Protótipo 13.1
Protótipo 13.2
Protótipo 14
Protótipo 14.2
Protótipo 15
Protótipo 15.2
Protótipo 16
Protótipo 16.2
Protótipo 17
Protótipo 17.2
Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.
divs
