---
content_hash: 212fcb0381e1cc38e14ec1447be18228499baf80e38eee2a657db8581db0bfb9
fetched_at: '2026-06-29T00:11:10.237187+00:00'
page_id: '642851136'
product: rm
source: tdn-rm
title: Integração Álvaro Alvim
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642851136
version: 11
---

sumarioVisão Geral

## **01. VISÃO GERAL**

Fluxo para atendimento aos laboratórios de apoio nesse caso com o Álvaro Alvim

Parâmetros

## **02.****TELA PARÂMETROS GERAIS DELPHI**

Caminho: Parâmetros > Parâmetros Gerais > aba Unidade de Diagnóstico II 

1.Marcar o parâmetro Utiliza Fluxo de Triagem de Amostras

Prestador

## **03. TELA****PRESTADOR**

Caminho: Cadastros > Prestador

| Ação | Descrição |
| --- | --- |
| Incluir | Cadastro de Prestador |
| Editar | Cadastro de Prestador |
| Inativar | Cadastro de Prestador |

 1. Cadastrar o Laboratório de Apoio como um prestador;

2. Na aba Tipo de Prestador a classe deve ser Laboratório de Apoio

## 

3.   Na aba Endereço de envio prestador incluir o tipo TOKEN , usuário e senha ou Login, usuário , senha e as ações .

3.1 Não é permitido cadastrar os dois tipos ou será TOKEN ou LOGIN

3.2 As ações cadastradas não podem estar duplicadas mas a url pode ser a mesma para todas

* Incluir a ação "**Incluir**", para enviar os exames para a integração
* Incluir a ação "**Obter**", para receber os resultados. Para essa integração, utilizar a url padrão, seguido de **/v2/resultados**
Locais de Execução Externa

## **04. TELA LOCAIS DE EXECUÇÃO EXTERNA**

Caminho: Cadastros > Unidade de Diagnóstico > Locais de Execução Externa

1.Incluir ou alterar um Local de execução vinculando o prestador cadastrado anteriormente

Exames e Serviços

## **05. TELA EXAMES E SERVIÇOS**

Caminho: Cadastros > Unidade de Diagnóstico > Exames e Serviços

1 No cadastro do exame , na aba Laboratórios de Execução Externa devem ser incluídos todos os laboratórios de apoio que realizam esse exame, podendo configurar um laboratório como padrão, método e tempo mínimo de execução e a entrega em dias método para ele vir default no pedido de exame após a inclusão do exame.

Pedido de Exames

## **06. TELA PEDIDO DE EXAMES**

Pedido de exames pode ser realizado pelo registro de atendimento no menu lateral Pedido de Exames ou no Caminho: Unidade de Diagnóstico > Pedido de Exames

1 Após incluir o exame configurado com um laboratório padrão o sistema já apresenta o campo de local de execução externa preenchido, podendo ser alterado caso haja necessidade.

2 Após a confirmação do pedido, o exame estará visível na tela de resultados laboratoriais

Resultados Laboratoriais

## **07. RESULTADOS LABORATÓRIAS**

Caminho: Unidade de Diagnóstico > Resultados Laboratoriais

Os exames que serão realizados em Local de Execução externa possuem os seguintes status:

**T**: Execução Externa (status inicial)

**P:** Saiu para coleta 

**S:** Triado no Laboratório 

**CC:**Coleta Concluída

**AR:** Aguardando retirada do laboratório de Apoio

Ao passar para o status **EE -**Entregue laboratório de Apoio o sistema irá exibir uma tela para inclusão dos dados do responsável pela busca e **realiza a integração dos exames**.

Selecionar o exame para obter resultado e clicar em '**Solicitar Resultados de Exames Álvaro**'.

Caso o pedido possua mais de um exame, não é necessário selecionar todos os exames do pedido. A integração solicitará todos os resultados dos exames que ainda estão pendentes de resultado.

Somente os exames que tiverem resultado é que terão a status alterado para Liberado. Os demais permanecerão com o mesmo status.

Se caso o exame não tenha sido integrado ou já tenha resultado será exibido a informação acima, caso contrario irá buscar o resultado.

Impressão/ emitir resultados

## **08. IMPRESSÃO / EMITIR RESULTADOS**

Para emitir relatório de resultados para laboratórios de execução externa é necessário definirmos qual o relatório que será utilizado na emissão.

Caminho: Cadastros > Unidades de Diagnóstico > Locais de Execução Externa

Edite ou crie o laboratório desejado e selecione qual relatório será utilizado para impressão.

Geralmente cada laboratório possui seu respectivo relatório, identificado pelo nome. Após definir o relatório será possível imprimir resultados.
