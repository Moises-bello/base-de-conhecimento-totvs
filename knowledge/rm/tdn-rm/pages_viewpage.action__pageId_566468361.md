---
content_hash: 7f2c4863f1c20afef63b607f0b7488cf0b52067005c23ddec6268eda5b16dc3a
fetched_at: '2026-06-29T00:10:51.314100+00:00'
page_id: '566468361'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Unidade de Diagnóstico > Laudos e resultados > Reemitir
  Pedido Exame
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=566468361
version: 9
---

## **ÍNDICE**

1. **Visão Geral**
2. **Condições de exibição do relatório**
3. **Configuração do relatório**

itensVisão Geral

## **01. VISÃO GERAL**

O usuário poderá reemitir o pedido de exame a qualquer momento através do Processo : Imprimir pedido de exame e através do ícone Reemitr o pedido de exame (reemitir pedido de exame)

      

Condições de exibição do relatório

## **02. CONDIÇÕES DE EXIBIÇÃO DO RELATÓRIO**

**1 -** Será exibido o relatório(Novo) cadastrado na unidade de atendimento do **pedido do exame**.

**Figura 1: Menu Cadastros/Unidade Atendimento - aba Outros dados**

**2** -  Caso o relatório cadastrado seja Antigo, ao clicar em reemitir exame será exibida a mensagem de erro abaixo:

**Figura 2: Mensagem de erro para relatório antigo**

**3** - Caso tenha integração PACS e o recurso não seja informado, sistema irá exibir a mensagem: O pedido de exame não pôde ser impresso pois o recurso   
não foi informado (Obrigatório para a Unidade de Atendimento)

 - Caso não tenha cadastro de relatório nas opções: Unidade Atendimento e Parâmetros Gerais, será exibida a mensagem:

**Figura 3: Mensagem de erro quando não há relatório cadastrado**

  **4 -** O relatório padrão "**SAUREL0013 - Lista de Exames do Pedido"** foi atualizado e deverá ser cadastrado pelo usuário na unidade de atendimento

**Figura 4: Exemplo da exibição do relatório**

Configuração do relatório

## **03. CONFIGURAÇÃO DO RELATÓRIO**

**Regras:**  
 - Será impresso apenas os relatórios criados no RM Reports(Novo)
