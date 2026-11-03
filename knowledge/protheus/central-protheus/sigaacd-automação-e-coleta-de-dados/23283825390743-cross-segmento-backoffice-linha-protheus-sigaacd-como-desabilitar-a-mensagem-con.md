---
article_id: 23283825390743
category: SIGAACD - Automação e Coleta de Dados
content_hash: 29162079ad00b0cdb8f7aeeae3396f88368c7f4a4312c8247eb48f095dc4a4e1
fetched_at: '2026-06-28T22:39:12.555889+00:00'
product: protheus
section_id: 1500001550002
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAACD - Como desabilitar a
  mensagem "Confirma transferência? (S/N)" na rotina ACDV150
type: support-article
updated_at: '2024-05-06T16:44:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23283825390743-Cross-Segmento-Backoffice-Linha-Protheus-SIGAACD-Como-desabilitar-a-mensagem-Confirma-transfer%C3%AAncia-S-N-na-rotina-ACDV150
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23283825362199) Tempo aproximado para leitura: **00:01:00 min****Dúvida**

Como desativar a mensagem na rotina ACDV150 "Confirma transferência? (S/N)"?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

A mensagem de confirmação da transferência é dinâmica de acordo com o tipo da etiqueta lida no coletor, e pode ser apresentada em dois eventos: No preenchimento do produto ou do endereço.

Sempre que for lida/bipada a etiqueta de endereço (**CB0\_TIPO=2**) ou pallet, a rotina irá apresentar a mensagem de confirmação da transferência. Não há possibilidade de customizar esse cenário na função  (GravaTransf).

Na leitura da etiqueta de produto, a mensagem será apresentada somente se o parâmetro [**MV\_ACDTRLT**](https://tdn.totvs.com/pages/releaseview.action?pageId=235596446) estiver ativo. Esse parâmetro possibilita a mudança / transferência entre lotes de produtos.

Caso não lhe atenda esse parâmetro, a alternativa ficaria por conta da solicitação da criação de um Ponto de Entrada pela nossa área de [Desenvolvimento Participativo](https://tdn.totvs.com/pages/releaseview.action?pageId=589518919).

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Automação e Coleta de Dados](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550002-SIGAACD-Automa%C3%A7%C3%A3o-e-Coleta-de-Dados)*
