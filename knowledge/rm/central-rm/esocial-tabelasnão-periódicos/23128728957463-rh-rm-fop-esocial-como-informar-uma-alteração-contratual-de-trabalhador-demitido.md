---
article_id: 23128728957463
category: eSocial - Tabelas/Não Periódicos
content_hash: e367f887771d28c0b4284c7d60f002650734f43a232d32252075259bc5a807f5
fetched_at: '2026-06-28T22:47:10.294466+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Como informar uma alteração contratual de trabalhador
  demitido devido ordem judicial
type: support-article
updated_at: '2026-06-01T14:09:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23128728957463-RH-RM-FOP-eSocial-Como-informar-uma-altera%C3%A7%C3%A3o-contratual-de-trabalhador-demitido-devido-ordem-judicial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23128728931863) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como informar uma alteração contratual de trabalhador demitido devido ordem judicial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
A partir da Simplificação do leiaute eSocial é possível retificar informações de um trabalhador demitido devido a ordem judicial sem a necessidade de excluir eventos enviados posteriormente a sua admissão(S-2200).  
A correção da informação é feita através do envio do S-2200 de retificação, após ajuste o histórico do funcionário corretamente. No exemplo abaixo, iremos alterar o cargo do funcionário como exemplo.  
  
1. Acessar o **histórico de função** do colaborador em **Administração de Pessoal | Funcionários | Anexos | Histórico de Função** e alterar para a função correta o histórico com data de admissão do funcionário:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23128708716823)  
  
2. Acessar o cadastro do funcionário em **Administração de Pessoal | Funcionários | Registro**e alterar o indicativo de admissão para 'Decorrente de decisão judicial e incluir no campo Nro Processo Trabalhista com o número do processo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23128728934423)  
  
3. Acessar a fila de eventos em  eSocial | Fila de Eventos e Incluir manualmente o evento S-2200 do funcionário com o tipo de operação Retificação(é necessário possuir o S-2200 de inclusão/carga inicial na fila de eventos):  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23128728935959)  
  
4. Gerar o xml e enviar o gatilho manual ao esocial.
