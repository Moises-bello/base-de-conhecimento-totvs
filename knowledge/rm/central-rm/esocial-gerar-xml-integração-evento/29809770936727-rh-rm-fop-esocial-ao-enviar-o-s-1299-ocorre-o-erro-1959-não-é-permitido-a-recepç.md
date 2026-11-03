---
article_id: 29809770936727
category: eSocial - Gerar XML/ Integração Evento
content_hash: 66a1d9c3d9de575f161cba593565c836751b3ced103b3cdd476aa87275eeaeb2
fetched_at: '2026-06-28T22:47:11.903364+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Ao enviar o S-1299 ocorre o erro 1959: Não é permitido
  a recepção do evento referente a período de apuração maior ou igual a 01/2025 com
  indicador de tributação sobre a folha de pagamento - PIS e PASEP(indTribFolhaPisPasep)'
type: support-article
updated_at: '2026-02-20T19:46:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29809770936727-RH-RM-FOP-eSocial-Ao-enviar-o-S-1299-ocorre-o-erro-1959-N%C3%A3o-%C3%A9-permitido-a-recep%C3%A7%C3%A3o-do-evento-referente-a-per%C3%ADodo-de-apura%C3%A7%C3%A3o-maior-ou-igual-a-01-2025-com-indicador-de-tributa%C3%A7%C3%A3o-sobre-a-folha-de-pagamento-PIS-e-PASEP-indTribFolhaPisPasep
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29809810667031) Tempo aproximado para leitura: **00:02:30 min****Ocorrência****Erro código 1959: Não é permitido a recepção do evento referente a período de apuração maior ou igual a 01/2025 com indicador de tributação sobre a folha de pagamento - PIS e PASEP (indTribFolhaPisPasep) em S-1000 = [S] nesta versão, pois há outros eventos remuneratórios em versão incompatível. Ação sugerida: Envie os eventos remuneratórios e o fechamento na versão 1.2 ou todos os eventos em versão igual ou posterior a S-1.3..**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - A partir das versões 12.1.2402.245; 12.1.2406.185; 12.1.2410.121 e Superiores.  
  
**Causa**O erro ocorre pois foi encaminhado algum evento de remuneração no leiaute S-1.2 e o evento de fechamento (S-1299) está sendo encaminhado no leiaute S-1.3, sendo que no S-1000 consta informação de tributação sobre a folha de pagamento - PIS e PASEP.

**Solução**Visto que o governo não está mais recepcionando eventos no leiaute S-1.2, para solucionar essa ocorrência, realize os seguintes passos:  
1. Envie o evento **S-3000 de exclusão de todos os eventos S-1210 do período 01/2025 em** Processos | Gerar eventos de Exclusão, daquelas as remunerações foram enviadas no leiaute S-1.2;  
2. Identifique na **fila de eventos periódicos, 01/2025, todos os eventos S-1200, S-1202 e S-1207**. Gere a retificação **P**rocessos | Gerar Retificação Arquivo eSocial e envie ao governo;  
3. Após acesse a fila de eventos não periódicos e identifique todos os **S-2299 e S-2399, que possuem rescisão em 01/2025 e que o evento foi encaminhado no leiaute S-1.2**. Gere a retificação Processos | Gerar Retificação Arquivo eSocial e envie ao governo;  
4. Envie novamente todos os eventos S-1210 de 01/2025;  
5. Envie o S-1299 de fechamento do período 01/2025.  
  
**Importante**Nem todos os eventos S-2399 possuem remunerações vinculadas, porém o governo está validando o leiaute deste evento, para recepcionar o S-1299.

É importante validar as datas dos eventos citados acima, e caso necessário enviar o S-3000 do mesmo e enviar ele novamente no leiaute S-1.3 Através do filtro abaixo é possível verificar no RM a coluna de versão de leiaute que os eventos a partir de 01/2025 foram gerados.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/29956110444183)

**Saiba mais**  
Para mais informações acesse:  
- [RH - RM - FOP - eSocial - Como informar o PIS/PASEP que incide sobre a folha na DCTFWEB através do S-1000](https://centraldeatendimento.totvs.com/hc/pt-br/articles/20036140486679-RH-RM-FOP-eSocial-Como-informar-o-PIS-PASEP-que-incide-sobre-a-folha-na-DCTFWEB-atrav%C3%A9s-do-S-1000#:~:text=Para%20que%20o%20governo%20acate,o%20momento%20n%C3%A3o%20houve%20altera%C3%A7%C3%A3o.);  
- [RH - RM - FOP - eSocial - Leiaute S-1.3](https://centraldeatendimento.totvs.com/hc/pt-br/articles/26091695488919-RH-RM-FOP-eSocial-Leiaute-S-1-3)
