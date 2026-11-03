---
article_id: 9783092249879
category: eSocial - Tabelas/Não Periódicos
content_hash: 1f7f7015336d607750a727d90a57667a3ba08b310e9721c352b2087825a1a006
fetched_at: '2026-06-28T22:47:10.332264+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 536 na integração com Governo: Informações
  de Empregador, trabalhador e/ou período de apuração incompatíveis'
type: support-article
updated_at: '2026-01-09T12:01:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9783092249879-RH-RM-FOP-eSocial-Erro-536-na-integra%C3%A7%C3%A3o-com-Governo-Informa%C3%A7%C3%B5es-de-Empregador-trabalhador-e-ou-per%C3%ADodo-de-apura%C3%A7%C3%A3o-incompat%C3%ADveis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19976334390167)Tempo aproximado para leitura: **00:01:30 min**  
  
**Ocorrência**  
Ao transmitir o evento S-3000 é apresentado a inconsistência **Código** **536 - Informações de Empregador, trabalhador e/ou período de apuração incompatíveis. Ação Sugerida: O Empregador, trabalhador e/ou período de apuração informados no evento de exclusão deverão ser os mesmos que constam do evento a ser excluído.**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9779371790615)**

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**  
O erro ocorre quando o Governo não localizou o evento no eSocial Web com as mesmas informações que constam no registro do S-3000. Sendo assim, considera como se o evento não existisse no ambiente do eSocial.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Abra o XML do evento S-3000 e verifique se o ID e o número de recibo do evento a ser excluído corresponde ao evento original ou retificação que consta no eSocial;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9852745468695)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9852737141655)

2. Caso o ID não corresponda ao evento que realmente deseja excluir, deverá localizar o evento correto na Fila de Eventos e o rejeitado poderá [excluir da fila](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017738251-RH-RM-FOP-eSocial-Exclus%C3%A3o-de-eventos-da-fila-independente-do-status?source=search);  
3. Selecione o evento devido e acesse **Processos | Gerar eventos de Exclusão (S-3000).**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9853323717399)**

4. Após gere o XML e envie ao eSocial.  
  
**Saiba mais:**

* [Utilização do S-3000 para exclusão de eventos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034224074-RH-RM-FOP-eSocial-Utiliza%C3%A7%C3%A3o-do-S-3000-para-exclus%C3%A3o-de-eventos)
* [RH - RM - FOP - eSocial - Regerar eventos periódicos excluídos por meio do evento S-3000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004784551-RH-RM-FOP-eSocial-Regerar-eventos-peri%C3%B3dicos-exclu%C3%ADdos-por-meio-do-evento-S-3000)
