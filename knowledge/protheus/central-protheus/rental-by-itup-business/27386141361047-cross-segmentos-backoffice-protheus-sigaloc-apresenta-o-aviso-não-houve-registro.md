---
article_id: 27386141361047
category: Rental by ItUp Business
content_hash: 8cf6454899127bb3a9ff6f6f5bd280178e5bfe91f238b0b1c086fddf670df17e
fetched_at: '2026-06-28T22:36:20.505825+00:00'
product: protheus
section_id: 25916336867863
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGALOC - Apresenta o aviso "Não houve
  registro para a seleção!"
type: support-article
updated_at: '2026-04-09T12:53:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27386141361047-Cross-Segmentos-Backoffice-Protheus-SIGALOC-Apresenta-o-aviso-N%C3%A3o-houve-registro-para-a-sele%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27386119048599) Tempo aproximado para leitura: **00:05:00 min**  
  
**Ocorrência**  
Na rotina LOCA021 ao efetuar a Faturamento Automático apresenta a mensagem "Não houve registro para a seleção!"  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGALOC - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a parametrização do sistema está incorreta para efetuar a apuração automática.  
  
**Solução**

Para solucionar a ocorrência, siga os passos abaixo:

1. **Verifique o Campo FPA\_GERAEM:**
   * Acesse a rotina **LOCA001** - **Orçamento** e valide o campo **FPA\_GERAEM** (Gera em).
   * Confirme se o campo está em branco.
2. **Acesse a Rotina LOCA021 - Faturamento Automático:**
   * Navegue até a rotina **LOCA021** - **Faturamento Automático** no sistema.
   * Verifique os parâmetros **MV\_PAR18** (**Gera em de?**) e **MV\_PAR19** (**Gera em até?**).
   * Assegure-se de que ambos os parâmetros estão em branco.

Se ambos os critérios forem atendidos, a ocorrência deve ser considerada resolvida.
