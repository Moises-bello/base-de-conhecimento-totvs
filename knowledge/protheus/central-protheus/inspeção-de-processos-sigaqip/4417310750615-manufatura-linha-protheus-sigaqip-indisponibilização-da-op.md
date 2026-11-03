---
article_id: 4417310750615
category: Inspeção de Processos (SIGAQIP)
content_hash: 563902a40e4d7bed26f35f848ce109c8642ab39401096fc455afd86fc23e524c
fetched_at: '2026-06-28T22:42:25.808458+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Indisponibilização da OP
type: support-article
updated_at: '2022-01-10T11:21:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417310750615-Manufatura-Linha-Protheus-SIGAQIP-Indisponibiliza%C3%A7%C3%A3o-da-OP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:10 min** **Dúvida**Na rotina **QIPA215 - Resultados**, ao finalizar uma inspeção ocorre a abertura da janela de **Indisponibilização da OP - Ordem de Produção**. Qual o parâmetro de controle para exibição desta janela?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Para o controle da exibição da janela de **Indisponibilização da OP** há o parâmetro **MV\_QPINDIS -** **Informa o laudo que indisponibiliza a Ordem de Produção** que possui sua aplicabilidade conforme o conteúdo:

* Ao configurar o parâmetro como **E**, é direcionada para opção **Encerramento**. Isto é, caso ainda estiver em aberto, a **OP** será encerrada automaticamente, desde que existam apontamentos parciais;
* Ao configurar o parâmetro como **S**, é direcionada para a opção **Suspensão**, a produção será suspensa temporariamente, até que seja reativada manualmente na rotina **MATA650 - Ordem de Produção**;
* Ao manter o conteúdo do parâmetro como **vazio**, não será solicitado nenhuma ação, nem **Suspensão**, nem **Encerramento** da **OP**, permitindo que o usuário realize o processo conforme sua necessidade.
