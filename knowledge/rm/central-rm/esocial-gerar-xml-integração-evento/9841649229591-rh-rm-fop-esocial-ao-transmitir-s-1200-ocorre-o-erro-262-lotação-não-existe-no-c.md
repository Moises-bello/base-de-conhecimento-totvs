---
article_id: 9841649229591
category: eSocial - Gerar XML/ Integração Evento
content_hash: 924d38e631925e70124184aad50ae0fe005fcf0a502d43b280e3c30cdd3a47c9
fetched_at: '2026-06-28T22:47:11.993048+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao transmitir S-1200 ocorre o erro 262: Lotação
  não existe no cadastro do empregador para o período'
type: support-article
updated_at: '2024-12-30T12:54:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9841649229591-RH-RM-FOP-eSocial-Ao-transmitir-S-1200-ocorre-o-erro-262-Lota%C3%A7%C3%A3o-n%C3%A3o-existe-no-cadastro-do-empregador-para-o-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23910235457047) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir o evento S-1200 para o governo é retornado a inconsistência **Lotacao[#39](https://totvssuporte.zendesk.com/agent/tickets/39);XXXX#39; nao existe no cadastro do empregador para o periodo[#39](https://totvssuporte.zendesk.com/agent/tickets/39);AAAA-MM#39;**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**Este erro ocorre quando é gerado no evento **S-1200** uma lotação tributaria cujo o início de validade não contempla o período de apuração indicado na *tag* **infoPerApur** ou o período de referência indicado na *tag* **perRef**  
  
**Solução**

Para correção da ocorrência favor realizar os passos abaixo:  
1. Verifique na mensagem de erro o código da lotação tributaria e o período de referência indicados;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9840997073943)

2. Acesse **Folha de Pagamento | eSocial | Fila de Eventos** filtre os eventos **S-1020** e pesquise pela lotação tributaria no erro;  
3. Verifique qual o início de validade enviados ao RET para a rubrica nos XML's **S-1020;**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9841183814551)**

4. Caso não possua um XML **S-1020** vigente para o período acesse **Folha de Pagamento | eSocial | Fila de Evento** se realize a inclusão do XML ajustando a competência para que contemple o período indicado no erro. Gere, integre e transmita o evento;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9841421639831)

5. Após o evento **S-1020** estiver com o status de **Aceito RET**, envie o XML**S-1200** novamente.  
  
**Saiba mais**  
Para mais informações acesse:   
  
[S-1020 - Lotações Tributarias](https://tdninterno.totvs.com/pages/releaseview.action?pageId=452719836)
