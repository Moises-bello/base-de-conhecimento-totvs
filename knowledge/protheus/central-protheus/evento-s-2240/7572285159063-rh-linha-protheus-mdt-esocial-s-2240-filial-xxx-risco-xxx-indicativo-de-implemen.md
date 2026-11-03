---
article_id: 7572285159063
category: Evento S-2240
content_hash: 22b5eabbca9a7d6026ba52dd4545e0f03f4ddca2dac7a14e3a3b75267b8a03c3
fetched_at: '2026-06-28T22:45:23.651833+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: 'RH - Linha Protheus - MDT - eSocial - S-2240 - Filial: XXX / Risco: XXX /
  Indicativo de Implementação de EPC deve ser igual a 0- Não se aplica, 1- Não implementa
  ou 2- Implementa'
type: support-article
updated_at: '2024-11-27T10:54:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7572285159063-RH-Linha-Protheus-MDT-eSocial-S-2240-Filial-XXX-Risco-XXX-Indicativo-de-Implementa%C3%A7%C3%A3o-de-EPC-deve-ser-igual-a-0-N%C3%A3o-se-aplica-1-N%C3%A3o-implementa-ou-2-Implementa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25514338297879) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Relatório de inconsistência na geração do evento S-2240: Filial: XXX / Risco: XXX / Indicativo de Implementação de EPC deve ser igual a 0- Não se aplica, 1- Não implementa ou 2- Implementa, o que conferir?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**O indicativo de implementação de EPC do risco (TN0\_EPC) deve ser igual a "Sim", "Não" ou estar em branco. Caso esteja em branco será enviado como 0- Não se aplica.  
  
No módulo SIGAMDT, acesse o menu Atualizações - PPRA - Riscos (MDTA180), ao incluir o Risco além dos campos obrigatórios, o campo "Utiliza EPC?" (TN0\_EPC) também deve ser preenchido:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7572265158295)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
