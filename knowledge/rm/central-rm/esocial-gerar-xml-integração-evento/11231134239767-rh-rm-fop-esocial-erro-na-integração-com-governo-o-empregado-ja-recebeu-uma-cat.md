---
article_id: 11231134239767
category: eSocial - Gerar XML/ Integração Evento
content_hash: 7ce46c7f88e9f4ef7f0a6681949f74dc45daf59023c5d93e8325f54cd9ac2eee
fetched_at: '2026-06-28T22:47:12.958716+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração com governo: O Empregado ja recebeu
  uma CAT por motivo de obito'
type: support-article
updated_at: '2025-07-02T20:47:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11231134239767-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-com-governo-O-Empregado-ja-recebeu-uma-CAT-por-motivo-de-obito
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao transmitir o evento S-2299 ou S-2399 para o governo é retornado a inconsistência **Erro código 1332: O Empregado ja recebeu uma CAT por motivo de óbito.**  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre quando a data de desligamento do funcionário, está igual ou posterior a **Data de Óbito** enviado no evento **S-2210 - Comunicação de Acidente de Trabalho**.

**Solução**Havendo evento de CAT por motivo de óbito do trabalhador **indCatObito = [S]**, não é  
permitido nenhum evento para o mesmo trabalhador cuja data de referência seja posterior  
ao óbito.

*Regra de validação eSocial*

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11301248616855)

Dessa forma, será necessário alterar a data do Desligamento para um dia anterior a data de Óbito conforme passos abaixo:  
1. Para isso, acesse o cadastro da rescisão do funcionário, no campo **Data de Desligamento** informe a nova data;

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11301888514839)

2. Em seguida, regere o XML do evento S-2299 e envie ao eSocial.
