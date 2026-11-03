---
article_id: 1500002037821
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 5bebd655c0f1c45aaa01478be2ba764ea96cfa61460481539d82364980af3b3b
fetched_at: '2026-06-28T22:38:54.417710+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como gerar Autorização
  de Entrega na Geração da Pré-Requisição?
type: support-article
updated_at: '2025-05-23T17:53:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002037821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-gerar-Autoriza%C3%A7%C3%A3o-de-Entrega-na-Gera%C3%A7%C3%A3o-da-Pr%C3%A9-Requisi%C3%A7%C3%A3o
---

**Dúvida**Como gerar a Autorização de Entrega através da rotina da Pré-Requisição ao Armazém (MATA106)?   
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**Veja nosso vídeo instrutivo sobre como Configurar Autorização de Entrega na Geração da Pre-Requisição no Protheus:**

Para que a Geração da Pré-Requisição venha gerar a Autorização de Entrega, efetue os seguintes passos:

Acessar o **Configurador** e habilitar o parâmetro **MV\_SOLICSA**

**1° Passo -**Via Cadastro de Produtos (MATA010), preencha os campos "Contrato" (B1\_CONTRAT) = Ambos e  "Fornecedor Padrão" (B1\_PROC), selecionando o mesmo fornecedor do contrato;

**2° Passo** - Via Amarração de Produtos x Fornecedor (MATA061), selecione o produto e o fornecedor para gerar a devida amarração;

**3° Passo -**No momento de gerar a Pré-Requisição (MATA106), dentro da rotina pressione o [F12] do teclado e configure o campo "Gera Sol. Compras/Atu. Entrega" = Sim, conforme a imagem abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100847354)

**4° Passo** - Será gerado Autorização de Entrega(SC7) através da rotina de Pedido de Compras.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31783355507863)

**5° Passo** - Para dar baixa na solicitação ao armazém, deve-se amarrar o pedido de compras gerado na nota de entrada, atualizando estoque na TES de entrada.

**6° Passo** - Acessar a rotina Baixa da Pré-Requisição (MATA185) e efetuar a baixa da solicitação ao armazém normalmente.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Movimentações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000033422-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
