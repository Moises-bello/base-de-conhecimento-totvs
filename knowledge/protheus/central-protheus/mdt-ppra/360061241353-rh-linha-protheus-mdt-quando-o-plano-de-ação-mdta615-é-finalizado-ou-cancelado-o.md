---
article_id: 360061241353
category: MDT - PPRA
content_hash: 5856b9d83bb26d43441261050a93769465e5e954a23dc00da868a17bd41bfb2a
fetched_at: '2026-06-28T22:44:27.527787+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Quando o Plano de Ação (MDTA615) é finalizado ou
  cancelado o registro não aparece na tela (Browser)
type: support-article
updated_at: '2025-08-14T14:11:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061241353-RH-Linha-Protheus-MDT-Quando-o-Plano-de-A%C3%A7%C3%A3o-MDTA615-%C3%A9-finalizado-ou-cancelado-o-registro-n%C3%A3o-aparece-na-tela-Browser
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19641683855767)**Tempo aproximado para leitura **00:02:00 min****Ocorrência**Quando o **Plano de Ação** (MDTA615) é finalizado ou cancelado o registro não aparece na tela (**Browser**).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre devido o parâmetro **MV\_NG2STPL** não estar configurado para apresentar registros do Plano de Ação finalizados ou cancelados.  
  
**Solução**O parâmetro **MV\_NG2STPL** permite indicar quais os status de plano de ação deverão ser exibidos na **Browser**.   
Os status disponíveis são: 1=Pendente; 2=Finalizado; 3=Cancelado. Para deixar visível na rotina todos os Status eles devem ser separados por “**;**”. Exemplo: **1;2;3** e caso o parâmetro não exista, será exibido no **Browser** apenas os planos Pendentes.  
  
Para alterar o parâmetro acesse o modulo Configurador (SIGACFG) no caminho: Ambiente > Cadastro > Parâmetros.  
  
![2020-12-29_15-10-08.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360099982154)  
  
E para acessar a rotina Plano de Ação (**MDTA615**) acesse no modulo 35 Medicina e Segurança do Trabalho (SIGAMDT) o caminho: Atualizações > PPRA > Plano de Ação.  
  
![2020-12-29_15-01-26.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001080902)  
  
**Observação**  
A rotina Plano de Ação **MDTA615** e **SGAA090** foram unificadas, para saber mais consulte o artigo: **[MP - MDT - Para que server a rotina Plano de Ação (MDTA615) e (SGAA090) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057396294-MP-MDT-Para-que-server-a-rotina-Plano-de-A%C3%A7%C3%A3o-MDTA615-e-SGAA090-e-como-incluir)**  
**Saiba Mais**[Artigos PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
