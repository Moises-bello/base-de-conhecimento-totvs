---
article_id: 22924131355159
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 4d90fed01e38e14089febaa46544f36ac0ad010158e6ccdba2f3d9552528bef7
fetched_at: '2026-06-28T22:38:57.276942+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Por que ao excluir
  o Documento de Entrada o lote não é excluído da SB8?
type: support-article
updated_at: '2024-04-19T16:53:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22924131355159-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Por-que-ao-excluir-o-Documento-de-Entrada-o-lote-n%C3%A3o-%C3%A9-exclu%C3%ADdo-da-SB8
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131303191) Tempo aproximado para leitura: **00:03:00min****Dúvida**Ao excluir nota percebi que ela não exclui o lote na SB8. E ao dar entrada novamente é exibido o help "A240DTVALI". O que fazer?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Por conceito nativo de Rastreabilidade, quando criamos o lote na entrada da nota, é iniciado o seu rastreamento deste então, por esse motivo, ao excluir o documento de entrada que criou o lote, o mesmo não será excluído no arquivo SB8 pois isso seria contra o conceito da rastreabilidade. O usuário até pode entrar com nota com o mesmo lote, desde que inserida a mesma data de validade de quando o lote foi criado (através da primeira nota) e, posteriormente, via Manutenção de Lotes - MATA390 - efetuar ajustes na data de validade do Lote caso julgue necessário. Abaixo demonstramos o cenário e o comportamento do Sistema.

**1-** Incluir um Produto novo com controle de Lote, conforme exemplo do print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924161642391)

**2-**Incluir um Documento de Entrada, informando o produto e colocando um Lote e uma Data de Validade. Vamos salvar o documento, conforme exemplo do print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131309207)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131311255)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131313815)

**3-**Acessar a rotina MATC040 e rastrear a Movimentação da Nota, naquele determinado Lote (selecionar antes o F12 para configurar os parâmetros da rotina conforme exemplo do print abaixo):

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131315607)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924161663255)

**3.1 -**Perceba que já iniciou a rastreabilidade do lote.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924161666839)

**4-**Acessamos novamente à rotina Documento de Entrada (MATA103), clicamos em Outras Ações Excluir, conforme do print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924161672855)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131324823)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924161677079)

**5-** Perceba pela consulta a rotina MATC040, que o lote não foi excluído da tabela SB8, conforme exemplo do print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131329815)

**6-** Vamos incluir a Nota de Entrada novamente e vai apresentar o Help "A240DTVALID" (mudando a data de validade do lote), conforme exemplo do print abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131331095)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22924131332759)

Esse movimento só é permitido se for imputada a mesma validade da criação do lote (no nosso exemplo 31/12/2025), e posteriormente, caso usuário precise alterar a validade, pode-se efetuar via Manutenção de Lotes.

Mais detalhes da rotina Manutenção de Lotes:

**Saiba Mais:**

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação do Help A240DTVALI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404325353239-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Valida%C3%A7%C3%A3o-do-Help-A240DTVALI?source=search)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
