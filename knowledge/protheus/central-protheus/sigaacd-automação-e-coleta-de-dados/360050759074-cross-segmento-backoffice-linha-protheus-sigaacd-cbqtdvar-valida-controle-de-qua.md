---
article_id: 360050759074
category: SIGAACD - Automação e Coleta de Dados
content_hash: f5234a1b1564c9a12f832d059b7979892f218b71afd53ce23697a1e9e71d0f13
fetched_at: '2026-06-28T22:39:12.496200+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - CBQTDVAR - Valida
  Controle de Quantidade Variável
type: support-article
updated_at: '2025-03-12T12:45:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050759074-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-CBQTDVAR-Valida-Controle-de-Quantidade-Vari%C3%A1vel
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28794129616791) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como utilizar o controle de saldos, para validação de quantidades nas movimentações das rotinas do processo de ACD?

**Ambiente**Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Todas as versões  
  
**Solução**

Alguns documentos tratados pelo módulo **ACD - Automação de Coleta de Dados** onde são digitadas quantidades para os produtos assumem quantidade 1 independentemente da informação digitada.

O módulo **ACD - Automação de Coleta de Dados** utiliza alguns campos do cadastro **SB5 - Complemento de Produto** para configurar determinados comportamentos de alguns programas.

Um destes campos é o **B5\_QTDVAR** que verifica se o produto tem quantidade variável.

Por padrão do sistema, ao configurar este campo como Sim o tratamento das quantidades dos produtos informados em determinados programas irá obedecer à quantidade digitada, do contrário, caso não exista nenhuma outra configuração específica para o produto será considerada a quantidade 1 para os produtos.

Entre os programas com tratamento afetado por este campo estão os listados abaixo:

| Programa | Descrição |
| --- | --- |
| ACDA032 | Programa de monitoramento do inventário do ACD |
| ACDA035 | Programa de atualização de Lançamento de Inventário |
| ACDI010 | Impressão de etiquetas de produto |
| ACDV035 | Programa principal do VT100 para o inventário |
| ACDV040 | Requisição de materiais por OP / Centro de Custo |
| ACDV125 | Recebimento de mercadoria por Pedido de Compra |
| ACDV165 | Pré-separação |
| ACDV170 | Movimentação interna de produtos |

É possível ainda definir se o produto tem quantidade variável através do ponto de entrada [**CBQTDVAR**](https://tdn.totvs.com/x/_-Bc).  
Neste caso o ponto de entrada prevalece sobre o campo **B5\_QTDVAR**.

**Saiba mais:**

[Meu Coletor de Dados : Guia de Referência](https://tdn.totvs.com/x/kh44Hg)

[*Clique aqui e veja mais artigos sobre Automação e Coleta de Dados*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)
