---
content_hash: 8bc84ad63a8811d0db51d827a8d3ae53c05b3f8ffd0ff390f30c6a6b5479100b
fetched_at: '2026-06-29T00:11:21.393014+00:00'
page_id: '695183782'
product: rm
source: tdn-rm
title: Processo de Material Consignado
type: documentation
url: https://tdn.totvs.com/display/LRM/Processo+de+Material+Consignado
version: 5
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Este processo visa descrever como é tratado o material consignado dentro do sistema.

Desde o cadastro do produto, parametrizações, geração da ordem de compra do material consignado, recebimento de material através da NF de compra até a atualização do preço na Elaboração de Contas

## **02. Configurações**

falseconsignadoCadastro

Cadastrar o produto e informar que o produto é do tipo consignado.  Desta forma, o sistema não irá misturar o estoque do hospital (estoque próprio) com o estoque de terceiros que está consignado no hospital.

Parametrização do tipo de movimento

Parametrizar um tipo de movimento no Gestão de estoque para receber as folhas de salas registradas no sistema (diminuir o estoque de consignado).

Parâmetros de integração

Depois de criado o tipo de movimento, informar este tipo de movimento na gestão hospitalar (Parâmetros de Integração com RM Nucleus) para enviar as movimentações de folha de sala para a gestão do estoque e neste momento

Folha de sala

Processar o movimento de Folha de Sala para o que o mesmo caia no Gestão de Estoque

Recebimento do movimento de baixa de estoque

Na gestão de estoque e compras, o usuário deverá receber o movimento de **Baixa de Estoque** que foi gerada na gestão de estoque (item 03) e gerar a ordem de compra para notificar o fornecedor informando que o mesmo deve enviar a NF DE COMPRA do material utilizado.  Neste momento, o usuário deverá informar o valor negociado com o fornecedor.

Recebimento da NF de compra

Receber a NF DE COMPRA enviada pelo fornecedor através da ordem de compra gerando o financeiro e a contabilidade.

Vínculo da NF com o atendimento

Neste momento, o usuário deverá **LIGAR** a NF recebida ao atendimento do paciente

Selecionar o item que terá o valor atualizado na conta do paciente

Calculo do valor

O valor a ser atualizado na conta do paciente será da seguinte forma:

**Preço unitário da nota X Fator definido na tabela de preço**

Após a execução de processo, o sistema atualizará o preço do OPME de acordo com o valor informado na nota e aplicado o fator da tabela de preço.

Caso na tabela de preço esteja configurado que é "Preço Fixo", o sistema não utiliza o preço da nota e sim o valor do preço fixo.

## **03.** **TABELAS UTILIZADAS**

* SZOPMEPACIENTE
