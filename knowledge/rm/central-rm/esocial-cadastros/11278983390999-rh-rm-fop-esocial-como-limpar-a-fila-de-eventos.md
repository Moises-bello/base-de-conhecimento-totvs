---
article_id: 11278983390999
category: eSocial - Cadastros
content_hash: af3826b1e61520e8e8a59ff70426857ea978b7cbeaab2a494880535f4fa2e370
fetched_at: '2026-06-28T22:47:14.478229+00:00'
product: rm
section_id: 1500000834341
source: central-rm
title: RH - RM - FOP - eSocial - Como limpar a Fila de Eventos
type: support-article
updated_at: '2022-12-30T18:42:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11278983390999-RH-RM-FOP-eSocial-Como-limpar-a-Fila-de-Eventos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:00:30 min**

**Dúvida**Como limpar a Fila de Eventos no RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**1. Para limpar a fila de eventos, acesse o menu **eSocial | Outros Processos | Limpar Fila de Eventos**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11282620322327)

2. Ao acessar a opção acima, será aberta a seguinte mensagem;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11282919679127)

2. Ao avançar, selecione quais os **Tipos de Arquivos** e **Eventos a serem limpos**;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11283085514007)

**Importante:**

* Antes de **Limpar a Fila Eventos** é imprescindível ter executado o processo **Atualizar Status Integração TAF**;
* Esse processo é **IRREVERSÍVEL**. Sendo assim é importante ter certeza da necessidade da sua execução;
* Caso o tipo de ambiente seja igual a **1-Produção** e existir eventos na fila com status igual a 10-Aceito RET, não será possível concluir o processo limpar a fila de eventos  e será exibida a seguinte mensagem para o usuário. Caso esteja em ambiente diferente do tipo "1-Produção", será possível concluir o processo de limpeza da fila de eventos.

**Saiba Mais**

Para mais informações acesse:  
[Como atualizar o Status de Integração com o TAF?](https://tdn.totvs.com/pages/releaseview.action?pageId=382545297)
