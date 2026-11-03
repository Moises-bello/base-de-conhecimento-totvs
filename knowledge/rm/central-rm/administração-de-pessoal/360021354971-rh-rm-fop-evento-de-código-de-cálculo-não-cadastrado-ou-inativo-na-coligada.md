---
article_id: 360021354971
category: Administração de Pessoal
content_hash: 35faa0a400f9ef2c6c087f2cc170a5a0bc7991371cc7feb85eb458f3b2b4f32e
fetched_at: '2026-06-28T22:47:02.275381+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Evento de código de cálculo não cadastrado ou inativo na coligada
type: support-article
updated_at: '2025-03-12T13:45:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021354971-RH-RM-FOP-Evento-de-c%C3%B3digo-de-c%C3%A1lculo-n%C3%A3o-cadastrado-ou-inativo-na-coligada
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura**: 00:01:00 min****Ocorrência**Ao executar rotinas no módulo Folha de Pagamento como o processamento da folha, lançamento de férias ou grupo de eventos é presentada a seguinte mensagem de erro: **Evento de código de cálculo XX não cadastrado, ou inativo, na Coligada X**  
  
Veja abaixo um exemplo da mensagem de erro:  
  
![kcs.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360018199752/kcs.png)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**Esse incidente ocorre quando não há, na coligada corrente, um evento com o código de cálculo XX.  
  
**Solução**Para solucionar essa ocorrência, realize os passos abaixo:  
  
1. Acesse **Administração Pessoal | Eventos | Eventos**;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444852701847/mceclip0.png)  
  
2. Verifique se já existe um evento com o código de cálculo solicitado cadastrado na Coligada;  
  
3. Caso o evento NÃO esteja cadastrado na base, será necessário cadastrar novo evento com este código de cálculo;  
  
[RH - RM - FOP - Cadastro de Eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412771329815-RH-RM-FOP-Cadastro-de-Eventos)  
  
4. Caso o evento EXISTA, verifique se ele está ATIVO. Se estiver INATIVO, ative-o novamente e salve o evento:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6444885593623/mceclip1.png)  
  
5. Execute novamente o processo realizado e veja se a mensagem será solucionada.  
  
**Saiba mais**  
[Códigos de calculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719279)
