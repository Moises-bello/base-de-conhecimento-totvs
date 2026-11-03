---
article_id: 360004877552
category: Materiais - Compras (SIGACOM)
content_hash: d4344a93865db903f4f973aa05e57a7e23be49d56edcad0c3f15891ea8d47e20
fetched_at: '2026-06-28T22:41:14.159679+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao incluir o Documento
  de Entrada com rateio ocorre o Help GETOBG para Conta Contábil ou Centro de Custo
type: support-article
updated_at: '2022-05-16T21:14:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004877552-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-incluir-o-Documento-de-Entrada-com-rateio-ocorre-o-Help-GETOBG-para-Conta-Cont%C3%A1bil-ou-Centro-de-Custo
---

**Dúvida**

Ao incluir o Documento de Entrada com rateio ocorre o Help **GETOBG** para Conta Contábil ou Centro de Custo

**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Solução**

No processo de rateio é informado o centro de custo e/ou a conta contábil deixando o centro de custo ou conta em branco na linha do item e quando um dos campos ou ambos estão como obrigatórios o sistema emite a mensagem de Help **GETOBG** no momento da confirmação conforme tela abaixo:

![Capturar1.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006334991/Capturar1.JPG)

A mensagem é apresentada devido o campo de conta contábil D1\_CONTA ou até mesmo o D1\_CC estarem como obrigatórios e no padrão Protheus os campos não são obrigatórios.  
Para solucionar essa dúvida e ajustar o sistema para que não apresente mais a mensagem siga os seguintes passos para retirar a obrigatoriedade do campo:

1. Acessar o configurador

2. Acessar a tabela SD1 - Itens da nota de entrada

3. Pesquisar pelo campo D1\_CC e/ou D1\_CONTA

4. Verificar na aba "Uso" que a opção Obrigatório está "flegado"

5. Neste caso desmarcar a opção Obrigatório

6. Salvar a alteração pelo "disquete" no menu do configurador.
