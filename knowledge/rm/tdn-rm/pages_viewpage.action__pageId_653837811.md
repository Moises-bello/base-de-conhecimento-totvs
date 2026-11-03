---
content_hash: 45b47d759a3dbd438354bb5975350e3e96a3b498091bbc53f6b9ca41f247d812
fetched_at: '2026-06-29T00:11:12.509325+00:00'
page_id: '653837811'
product: rm
source: tdn-rm
title: Integração Hermes Pardini
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653837811
version: 13
---

## **Conteúdo**

1. **Visão Geral**
2. **Configuração de Exame**
3. **Tela Prestador**
4. **Tela Locais De Execução**
5. **Tela Pedido de Exame**
6. **Gestão de Lotes**
7. **Resultados Laboratoriais**
8. **Impressão / Emitir**
9. **Resultados Exames de Curva para Integração com Hermes Pardini**

itensVisão Geral

## **01. VISÃO GERAL**

Fluxo para atendimento aos laboratórios de apoio nesse caso com o Hermes Pardini

Configuração de Exame

## **02.****CONFIGURAÇÃO DE EXAME (NOVA MDI)**

Caminho: Cadastro > Unidades de Diagnóstico > Exames e Serviços > Selecione o Exame desejado > Anexo > Parametrização Hermes Pardini Exames

1.Clicar em "novo" - Cadastrar os dados do Exame junto ao cadastro do Laboratório Hermes Pardini (nesse exemplo usamos o exame Hemograma)

2. Configurar o exame para execução externa  
 Caminho: Cadastro > Unidades de Diagnóstico > Exames e Serviços > Selecione o Exame desejado >Laboratórios de Execução Externa

Selecionar no 'Local' o laboratório Hermes Pardini previamente cadastrado em Locais de Execução Externa.

Tela Prestador

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

3.3 Não é necessário clicar em "Incluir" nessa ação somente salvar.

Tela Locais de Execução Externa

## **04. TELA LOCAIS DE EXECUÇÃO EXTERNA**

Caminho: Cadastros > Unidade de Diagnóstico > Locais de Execução Externa

1.Incluir ou alterar um Local de execução vinculando o prestador cadastrado anteriormente

Legenda Status Integração

Os exames que serão realizados em Local de Execução externa possuem os seguintes status:

**T**: Execução Externa (status inicial)

**P:** Saiu para coleta

**S:** Triado no Laboratório 

**CC:**Coleta Concluída

**AR:** Aguardando retirada do laboratório de Apoio

Tela Pedido de Exame

## **05. TELA PEDIDO DE EXAMES**

Pedido de exames pode ser realizado pelo registro de atendimento no menu lateral Pedido de Exames ou no Caminho: Unidade de Diagnóstico > Pedido de Exames

1 Após incluir o exame configurado com um laboratório padrão o sistema já apresenta o campo de local de execução externa preenchido, podendo ser alterado caso haja necessidade.

2 Após selecionar o Local de Execução externa (Hermes Pardini) o campo Material Biológico deve ser alterado selecionando o material Biológico Cadastrado no passo 1 das configurações do exame.

3 **Após a confirmação do pedido**, o sistema exibe uma mensagem informando a **impressão da etiqueta**.  
A etiqueta **não possui pré-visualização de impressão** e é **enviada diretamente para a impressora Zebra configurada** no ambiente.

5. Logo após o exame estará visível na tela de resultados laboratoriais.

Gestão de Lotes

## **06. GESTÃO DE LOTES**

Caminho: Unidade de Diagnóstico > Resultados Laboratoriais > Processo > Gestão de Lotes > Processo de Inclusão de Lote Pedido de Exames

Status: **AR**

Ao clicar no link 'Lote de Pedidos' são exibidos os itens contidos no lote.

Ao Finalizar o processo o lote é gerado e assim pode ser enviado ao Laboratório Hermes Pardnini.

Caminho: Unidade de Diagnóstico > Resultados Laboratoriais > Processo > Gestão de Lotes > Processo de Envio Lote Pedido de Exames

Ao finalizar o processo de envio o Status do exame passa automaticamente para **EE** (Entregue laboratório de apoio).

Resultados Laboratoriais

## **07. RESULTADOS LABORATORIAS**

Caminho: Unidade de Diagnóstico > Resultados Laboratoriais > Processo > Processo Resultado Exames Integração

Status: **EE**

É Exibido uma tela com os dados do Lote criado e enviado ao laboratório Hermes Pardini.

**Fluxos de retorno resultado**

1. **Resultado por período de liberação**
   1. Após preencher a data de inicio e fim do período de liberação do laboratório Hermes Pardini o RM Saúde irá buscar os resultados dos exames enviados no lote e passará o status dos exames para **L** (Liberado).
2. **Resultado por pedido exame**
   1. Ao selecionar o checkbox  o sistema solicitará ao laboratório Hermes Pardini que envie **todos** os resultados disponíveis para os exames contidos no pedido selecionado na tela anterior com status **EE** e passará o status dos exames para **L** (Liberado)
3. **Regra**
   1. Ao selecionar o checkbox supracitado os campos "Período de busca" serão desabilitados.
   2. Ao desmarcar o checkbox supracitado os campos "Período de busca" serão habilitados e a busca seguira o passo 1 do Fluxo de retorno resultado *(Resultado por período de liberação)*.

Impressão / Emitir Resultados

## **08. IMPRESSÃO / EMITIR RESULTADOS**

Para emitir relatório de resultados para laboratórios de execução externa é necessário definirmos qual o relatório que será utilizado na emissão.

Caminho: Cadastros > Unidades de Diagnóstico > Locais de Execução Externa

Edite ou crie o laboratório desejado e selecione qual relatório será utilizado para impressão.

Geralmente cada laboratório possui seu respectivo relatório, identificado pelo nome. Após definir o relatório será possível imprimir resultados.

Exames de Curva para Integração com Hermes Pardini

## **09.** **Exames de Curva para Integração com Hermes Pardini**

A funcionalidade de exames de curva para integração Pardini, em primeira instância, vai funcionar **somente** para o exame Insulina, pois de acordo com o próprio laboratório, cada exame possui uma peculiaridade e devem ser tratados de maneiras diferentes.

* Cadastro do exame de insulina:

* No pedido de exame, será inserido normalmente os tempos de curva que desejo para o retorno do exame:

* Nos resultados desse exame, após executar a integração normalmente, teremos o seguinte retorno, com os tempos determinados no pedido:

Anexos e Processos
