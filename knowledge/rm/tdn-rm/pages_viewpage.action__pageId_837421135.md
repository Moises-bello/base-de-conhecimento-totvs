---
content_hash: cfb7dcf7df29fc898621490fae3de9f7bf97d8736ca46095b55167313a6eee7a
fetched_at: '2026-06-29T00:11:49.687637+00:00'
page_id: '837421135'
product: rm
source: tdn-rm
title: Controle de produto por número de série - Apoio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=837421135
version: 3
---

## 

## **CONTEÚDO**

1. **Visão Geral**
2. **Configuração**
3. **Processo**

PainelVisão Geral

## **Visão Geral**

É um processo de controle e rastreabilidade de produtos, cada produto é identificado por um número de série único gerado para todos os produtos cadastrados no TOTVS RM.

Configuração

## **Configuração**

O backoffice precisa está configurado também para que o processo funcione.

Configurar o tipo de movimento para pera aceitar a movimentação por número de série, conforme documentação: [Lote / Grade Numerada / Número de Série](https://tdn.totvs.com/pages/viewpage.action?pageId=423937995)

Configurar o parâmetro de produtos para permitir número de série e lote simultaneamente, conforme imagem:

Após a configuração do backoffice a configuração abaixo precisa ser realizado no TOTVS RM Saude.

Ambientes→ Parâmetros → Parâmetros Hospitalar → Integração Backoffice

Habilitar a configuração **Utiliza número de série do produto para controle de rastreabilidade**

No cadastro do produto que será controlado por número de série habilitar a opção **Controla número de série**

Processo

## **Processo**

Após realizar a configuração necessária e alimentar o saldo do item com seus lotes e números de séries devidamente associados, o usuário deverá no TOTVS RM Saúde acessar o TOTVS RM Saúde → Apoio → Estoque → Assistente de gerenciamento de número de série.  
Deverá escolher a opção Imprimir etiqueta, informar o produto e local de estoque, lote, selecionar os números de série e o relatório de etiquetas de código de barras, por padrão será sugerido o definido em parâmetro.

Após esse processo serão gerados e impressos os códigos de barras dos números de série selecionados.
