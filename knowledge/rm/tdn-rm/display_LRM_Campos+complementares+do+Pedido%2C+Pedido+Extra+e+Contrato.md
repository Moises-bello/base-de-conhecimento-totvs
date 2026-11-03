---
content_hash: 5d26f883b2d91fe6e9c58990fec1789faf1023d221784b5ecd857e2a96d5d304
fetched_at: '2026-06-29T00:10:15.254462+00:00'
page_id: '463822019'
product: rm
source: tdn-rm
title: Campos complementares do Pedido, Pedido Extra e Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Campos+complementares+do+Pedido%2C+Pedido+Extra+e+Contrato
version: 19
---

Os campos complementares nos Pedidos, Pedidos Extras e Contratos no Totvs Obras e Projetos, são utilizados para controles de projetos, quando enviados ao Suprimentos/Faturamento. Desta forma com o objetivo de facilitar a comunicação entre equipes e possuir um melhor controle de seus processos os campos complementares podem ser habilitados no Totvs Obras e Projetos e no Totvs Gestão de Estoque, Compras e Faturamento  facilitando a comunicação entre equipes.

10CadastroCadastro dos campos complementares

## **Pedido , Pedido Extra**

Os campos complementares cadastrados para o pedido quando habilitados são visualizados no anexo de "Pedido de Faturamento Direto" do contrato, Pedidos e Pedidos Extra.

Importante

Para que os campos complementares sejam enviados para o Totvs Gestão de Estoque, Compras e Faturamento é necessário que os mesmos campos estejam cadastrados no Totvs Gestão Obras e Projetos.

* Os campos complementares no **Totvs Gestão de Estoque, Compras e Faturamento** são cadastrados em Cadastros | Estoque, Compras e Faturamento | Mais... | Campos complementares | Movimentos.

Após cadastrar os campos complementares no Totvs Gestão de Estoque, Compras e Faturamento é necessário que sejam habilitados no tipo de movimento para isso, acesse Ambiente | Configurações | Parâmetros | Gestão de Estoque, Compras e Faturamento | Abra o local que se encontra o tipo de movimento | Depois edite o tipo de movimento | Etapa Mov - Campos Complementares.

* Os campos complementares no**Totvs Gestão de Obras e Projetos** são cadastrados em Cad. Gerais | Básicos | Campos complementares | Pedidos (Movimento Backoffice)

Campos cadastrados no Totvs Obras e Projetos igual ao do Totvs Gestão de Estoque, Compras e Faturamento:

0CadastroEnviar campos complementares de medição para o Nucleus

# **Contrato**

**Enviar campos complementares de medição para o Totvs Gestão de Estoque Compras e Faturamento**

1 - No menu Cadastros -> Campos complementares -> Medição, foi criado um campo complementar "VENC" do tipo Data na tabela de Medição.

2 - No BackOffice Suprimentos/Faturamento -> Para o tipo de movimento informado ao executar o processo, foi criado um campo complementar de mesmo nome "VENC" e tipo Data.

3 - Ao executar o processo "Gerar integração com Suprimentos/Faturamento", o campo complementar foi copiado para o movimento.

1Processo

**Identificação**

A aba de identificação, possui campos referentes a identificação do Pedido.

****Necessidades do pedido****

Esta aba contém as informações necessárias para atender as necessidades do pedido.

**Campos complementares**

Esta aba somente será habilitada caso seja cadastrado os campos complementares no Totvs Obras e Projetos.

Os campos complementares são utilizados para melhor controle de informações pertinentes para o envio do pedido ao movimento.

Com os campos complementares preenchidos no Pedido ou Pedido Extra, o movimento na aba Informações Adicionais | Campos complementares, serão devidamente preenchidos com as informações descritas no pedido.
