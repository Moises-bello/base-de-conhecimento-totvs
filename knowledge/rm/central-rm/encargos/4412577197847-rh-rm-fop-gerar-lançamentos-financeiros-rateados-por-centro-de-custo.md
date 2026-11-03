---
article_id: 4412577197847
category: Encargos
content_hash: a2aac00f23acbdec1d0ebc5be15649fb63ed184277e3d7984ded6c0dafb0ccd7
fetched_at: '2026-06-28T22:46:53.223417+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Gerar lançamentos financeiros rateados por Centro de Custo
type: support-article
updated_at: '2025-03-05T19:41:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412577197847-RH-RM-FOP-Gerar-lan%C3%A7amentos-financeiros-rateados-por-Centro-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Ao gerar os lançamentos financeiros, não há a opção para fazê-la rateada por centro de custo. Como faço para habilitar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Na rotina **Geração de Lançamentos Financeiros**, presente em Encargos | Geração dos Lançamentos, há um espaço onde é possível habilitar a opção **Gerar lanctos rateados por centro de custo**:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10780906382615)  
  
Para que esta opção fique disponível, é necessário acessar o módulo BackOffice | Gestão Financeira | Parâmetros | TOTVS Gestão Financeira | 02.01.02 - Baixa | Recursos Adicionais | e marcar a Obrigatoriedade como Não Obrigatório:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10780853383447)  
  
Ao concluir a parametrização e acessar novamente a rotina no módulo Folha de Pagamento, a opção Gerar lanctos rateados por centro de custo estará disponível:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10780911827607)  
  
**Importante**  
Por se tratar da parametrização de outro módulo, verifique com sua equipe encarregada se a parametrização causará algum impacto em sua rotina.
