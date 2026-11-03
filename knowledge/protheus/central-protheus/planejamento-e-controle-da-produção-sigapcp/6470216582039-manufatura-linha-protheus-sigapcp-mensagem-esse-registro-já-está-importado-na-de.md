---
article_id: 6470216582039
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 90c17eaf43c0c66e9068d8e45452b27d04839694aa5e777fc0291efabcee9c81
fetched_at: '2026-06-28T22:42:44.461954+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: 'Manufatura - Linha Protheus - SIGAPCP - Mensagem Esse registro já está importado
  na demanda: XXXXXX'
type: support-article
updated_at: '2022-06-01T16:40:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6470216582039-Manufatura-Linha-Protheus-SIGAPCP-Mensagem-Esse-registro-j%C3%A1-est%C3%A1-importado-na-demanda-XXXXXX
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min  
  
Ocorrência**Na rotina **PCPA136 - Demandas do MRP**, ao importar um **documento** apresenta a mensagem **Esse registro já está importado na demanda: XXXXXX  
  
Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Causa**Essa situação ocorre quando o **documento** a ser **importado**, já foi importado em outra **demanda**.   
Pode ocorrer casos onde foi realizado a **importação**, e o usuário fechou a **demanda** sem **salvar**, mesmo assim o registro de **importação** será **salvo**, pois ao fazer uma **importação** as informações já serão **salvas** na tabela e quando volta para a tela, o programa já está em modificação, ou seja, somente disponível se o usuário deseja realizar alguma alteração no que foi **importado**.  
O programa emite uma **mensagem** antes da importação informando que os dados já serão **salvos**.  
Impedindo dessa forma a **importação** do **documento** em outra **demanda**.  
  
**Solução**  
Para solucionar essa ocorrência, é necessário excluir a **demanda** onde o **documento** foi **importado**, para fazer a **importação** em outra **demanda**.
