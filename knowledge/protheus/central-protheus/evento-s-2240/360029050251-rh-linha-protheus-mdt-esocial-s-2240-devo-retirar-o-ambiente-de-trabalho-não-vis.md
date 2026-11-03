---
article_id: 360029050251
category: Evento S-2240
content_hash: c0fac86c30d54401e8ca1957a90ac2a7abbe3bb9dbea27ad8b1e0f0734e91222
fetched_at: '2026-06-28T22:45:23.618634+00:00'
product: protheus
section_id: 8260550695703
source: central-protheus
title: RH - Linha Protheus - MDT - eSocial - S-2240 - Devo retirar o ambiente de trabalho
  não visitado no mês do eSocial no modulo SIGAMDT. E como fica o grau de exposição
type: support-article
updated_at: '2024-08-22T21:40:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029050251-RH-Linha-Protheus-MDT-eSocial-S-2240-Devo-retirar-o-ambiente-de-trabalho-n%C3%A3o-visitado-no-m%C3%AAs-do-eSocial-no-modulo-SIGAMDT-E-como-fica-o-grau-de-exposi%C3%A7%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25844235841943)**Tempo aproximado para leitura:**00:02:00 min  
  
Dúvida**Devo retirar o ambiente de trabalho não visitado no mês do eSocial no modulo Medicina e Segurança do Trabalho?  
**Por Exemplo:**O trabalhador vai a 04 empresas diferentes por mês, mas em um determinado mês, ele só foi em 03 empresas.  
  
E como fica o grau de exposição?   
**Por exemplo:** Destas 04 empresas, uma tem o pior cenário em termos de risco (Ex. Exposição ao benzeno, tolueno, etc.). Entretanto, o trabalhador fica em média 01 dia e, outros 19 dias úteis do mês ele divide nas outras 03 empresas.   
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O evento responsável pela exposição é o **S-2240**, onde vai ser enviado os locais no qual incidem essa exposição, se houver essa alteração deve ser enviado esse evento. O envio do S-2240 vai considerar a exposição ao grau de risco no qual incide sobre o funcionário, quando ele sair dessa exposição, deverá enviar uma nova exposição, retificando o valor.  
  
Então se em cada dia ele estiver em um ambiente diferente, será necessario enviar um **S-2240**, essa situação pode ser controlada via **Tarefa**, onde a cada dia ele entrará em uma tarefa específica naquele local, desta forma, prevemos um **Schedule** que poderá ser configurado para essas situações.  
  
**Observação**  
Para configurar o Schedule de Tarefas acesse: [MP - MDT - eSocial - S-2240 - Como utilizar a rotina Schedule (JOB) de Tarefas para envio do S-2240 para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033184593-MP-MDT-eSocial-S-2240-Como-utilizar-a-rotina-Schedule-JOB-de-Tarefas-para-envio-do-S-2240-para-o-TAF)  
  
**Saiba Mais**[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
