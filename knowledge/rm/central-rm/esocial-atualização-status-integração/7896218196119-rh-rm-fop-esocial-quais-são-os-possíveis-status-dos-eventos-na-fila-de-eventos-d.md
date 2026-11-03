---
article_id: 7896218196119
category: esocial - Atualização Status Integração
content_hash: bb83090d2be5137e84efa9fe66e1846623acc0015b4467b2043f6e9d17811d06
fetched_at: '2026-06-28T22:47:11.189524+00:00'
product: rm
section_id: 1500000860962
source: central-rm
title: RH - RM - FOP - eSocial - Quais são os possíveis status dos eventos na Fila
  de Eventos do RM
type: support-article
updated_at: '2024-06-14T13:27:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7896218196119-RH-RM-FOP-eSocial-Quais-s%C3%A3o-os-poss%C3%ADveis-status-dos-eventos-na-Fila-de-Eventos-do-RM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Quais são os possíveis status dos eventos na **Fila de Eventos** do RM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Abaixo relação de **Status** dos eventos na **Fila de Eventos** do RM.

* **0 - Pendente**: Gatilho criado na Fila de Eventos após alguma inclusão de registro ou alteração no cadastro;
* **1 - Gerado**: Evento validado pelo RM e está apto a ser enviado para TAF ou eSocial (quando utiliza Middleware);
* **2 - Erro na geração**: Quando o RM identifica divergência entre os dados incluídos para a geração do XML com o Leiaute vigente;
* **3 - Enviado**: Gatilho foi integrado com TAF ou com eSocial (quando utiliza Middleware);
* **4 - Aceito TAF**: Após validação realizada pelo TAF, o evento está apto para transmissão ao Governo (RET);
* **5 - Erro na integração TAF**: Houve falha na conexão entre ERP (RM) e o TAF. Ou seja, o evento não foi processado e nem validado pelo TAF sendo necessário gerar e integrar novamente o evento;
* **6 - Rejeitado TAF**: Após validação do TAF, foram encontrados informações no XML em desacordo;
* **9 - Rejeitado RET**: Após validação do Governo, o evento é rejeitado por conter alguma inconsistência de acordo com o Leiaute vigente;
* **10 - Aceito RET**: Eventos validados pelo Governo e estão consistentes de acordo com a regra do Leiaute vigente;
* **11 - Excluído RET**: Quando o evento é excluído do ambiente do governo através do S-3000, é retornado o status de excluído no evento original. O evento S-3000 ficará com status Aceito RET.

**Saiba Mais:**  
Para mais informações acesse:  
[- TAF - Como verificar o status do evento para o eSocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037818153-TAF-FUNCIONALIDADES-Como-verificar-o-status-do-evento-para-o-e-Social)
