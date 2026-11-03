---
article_id: 39324472216471
category: PCO - Cubos
content_hash: c8332c05b4b6bccdd821c191540c1b2263e55f3bd4283ec021d52bc39cc6c5b6
fetched_at: '2026-06-28T22:37:11.556311+00:00'
product: protheus
section_id: 1500001550862
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Planejamento e Controle
  Orçamentário - Composição dos campos Saldo Previsto e Saldo Realizado na tela de
  contingência
type: support-article
updated_at: '2026-03-30T15:00:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39324472216471-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Planejamento-e-Controle-Or%C3%A7ament%C3%A1rio-Composi%C3%A7%C3%A3o-dos-campos-Saldo-Previsto-e-Saldo-Realizado-na-tela-de-conting%C3%AAncia
---

A demonstração dos campos "Saldo Previsto" e "Saldo Realizado" na tela de contingência do PCO depende das configurações de bloqueio no cubo orçamentário, definidas na rotina PCOA193. Se o saldo for acumulado, considera todos os saldos desde a implantação até o período atual; se for por período, considera o saldo do período definido, como mensal.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39324472212119) Tempo aproximado para leitura: 00:10 min  
  
**Dúvida**  
**Como é composta a demonstração de valores dos campos "Saldo Previsto" e "Saldo Realizado" na tela de contingência do Planejamento e Controle Orçamentário (PCO)?**  
  
**Ambiente**  
**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Planejamento e Controle Orçamentário (SIGAPCO) - A partir da versão 12**  
  
**Solução**  
O saldo apresentado na tela de contingência (como Saldo Previsto e Saldo Realizado) depende diretamente das configurações de bloqueio definidas no cubo orçamentário, na opção de tipo de bloqueio nos campos: Tp **Apuração (AKJ\_TPSALD)** e **Consid Saldo (AKJ\_SLDPER).**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39324461910551)

Se na configuração de bloqueio do cubo, realizada na rotina **Cubos Gerenciais (****PCOA193)**, a opção de **Consid Saldo (AKJ\_SLDPER)**estiver como acumulada, o sistema irá considerar o saldo das entidades desde a implantação até o período em que se está realizando a integração.

Se a opção estiver como período, o sistema irá considerar também o campo **Tp Apuração (AKJ\_TPSALD)**, indicando qual período o sistema deve considerar. Caso esteja como mensal, o sistema irá demonstrar o saldo do mês em que estiver realizando a validação e assim por diante.

Sendo assim, quando o cubo está parametrizado para considerar o saldo acumulado, a tela de contingência aglutina todos os saldos (por exemplo, do tipo "RE" - Realizado) encontrados para a entidade até o período atual da operação.

|  |  |
| --- | --- |
|  |  |

**Saiba mais**  
[PCOA193 Exemplo de como configurar um Cubo Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810031-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA193-Exemplo-de-como-configurar-um-Cubo-Gerencial)  
[How To PCO - Planejamento e Controle Orçamentário - Suporte Técnico Protheus - Linha Microsiga Protheus - TDN](https://tdn.totvs.com/pages/viewpage.action?pageId=763235880&draft=true)
