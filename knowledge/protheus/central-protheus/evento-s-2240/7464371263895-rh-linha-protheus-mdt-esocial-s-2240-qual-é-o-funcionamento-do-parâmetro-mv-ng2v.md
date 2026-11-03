---
article_id: 7464371263895
category: Evento S-2240
content_hash: bf50e6fa47130408bed88e1eea7fb325f0db4e5ecf4c33fd49b858113070e33d
fetched_at: '2026-06-28T22:45:23.745795+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Qual é o funcionamento do parâmetro
  MV_NG2VLAU
type: support-article
updated_at: '2025-03-12T18:34:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7464371263895-RH-Linha-Protheus-MDT-eSocial-S-2240-Qual-%C3%A9-o-funcionamento-do-par%C3%A2metro-MV-NG2VLAU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25676738265623) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Qual é o funcionamento do parâmetro MV\_NG2VLAU?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**No envio do evento S-2240 ao eSocial existe a possibilidade de configuração do parâmetro MV\_NG2VLAU que é responsável por definir se apenas os riscos vinculados a um laudo do tipo PPRA serão comunicados com o governo.  
  
Caso o parâmetro seja definido como 1- Sim, serão considerados para o eSocial apenas os riscos que estejam vinculados a um laudo do tipo PPRA através da tabela Laudos x Risco (TO1), dessa forma todas as informações a serem enviadas no evento S-2240 serão apenas as relacionadas aos riscos vinculados a algum laudo do tipo PPRA. Um exemplo prático são os EPI's a serem enviados ao eSocial, apenas os EPI's vinculados aos riscos que estejam vinculados a algum laudo PPRA serão enviados ao governo.   
  
Já caso o parâmetro MV\_NG2VLAU esteja definido como 2- Não, o sistema não fará essa distinção, considerando as informações relacionadas a qualquer risco cadastrado no sistema, não havendo a necessidade de estar vinculado a um laudo do tipo PPRA para o envio ao governo.

Estrutura do parâmetro:

|  |  |
| --- | --- |
| **Nome da Variável:** | MV\_NG2VLAU |
| **Tipo:** | Caracter |
| **Descrição:** | Indica se somente irá enviar ao TAF Riscos que estejam vinculados a um Laudo PPRA no momento de envio. 1- Sim; 2- Não. |
| **Valor Padrão:** | 2 |

  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
