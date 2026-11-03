---
article_id: 1500000930661
category: MDT - PPRA
content_hash: c1ac2606c308cf402268ddbcb7ff58f9a254d0f5f2def2037e7fdd83e21155b9
fetched_at: '2026-06-28T22:44:27.531631+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: RH - Linha Protheus - MDT - Quando o Plano de Ação (SGAA090) é finalizado ou
  cancelado o registro não aparece na tela (Browser)
type: support-article
updated_at: '2025-08-14T13:25:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000930661-RH-Linha-Protheus-MDT-Quando-o-Plano-de-A%C3%A7%C3%A3o-SGAA090-%C3%A9-finalizado-ou-cancelado-o-registro-n%C3%A3o-aparece-na-tela-Browser
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19636562708887)**Tempo aproximado para leitura **00:02:00 min****Ocorrência**Quando o **Plano de Ação** (SGAA090) é finalizado ou cancelado o registro não aparece na tela (**Browser**).  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso ocorre devido o parâmetro **MV\_NG3STPL** não estar configurado para apresentar registros do Plano de Ação finalizados ou cancelados.  
  
**Solução**O parâmetro **MV\_NG3STPL** permite indicar quais os status de plano de ação deverão ser exibidos na **Browser**.   
Os status disponíveis são: 1=Pendente; 2=Finalizado; 3=Cancelado. Para deixar visível na rotina todos os Status eles devem ser separados por “**;**”. Exemplo: **1;2;3** e caso o parâmetro não exista, será exibido no **Browser** apenas os planos Pendentes.  
  
Para alterar o parâmetro acesse o modulo Configurador (SIGACFG) no caminho: Ambiente > Cadastro > Parâmetros.  
![2020-12-29_15-10-46.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360102161233)  
  
E para acessar a rotina Plano de Ação (**SGAA090**) acesse no modulo 35 Medicina e Segurança do Trabalho (SIGAMDT) o caminho: Atualizações > Ohsas > Ação > Plano de Ação.  
![2020-12-29_15-01-26.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001081362)  
  
**Observação**  
A rotina Plano de Ação **MDTA615** e **SGAA090** foram unificadas, para saber mais consulte o artigo: **[MP - MDT - Para que server a rotina Plano de Ação (MDTA615) e (SGAA090) e como incluir](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057396294-MP-MDT-Para-que-server-a-rotina-Plano-de-A%C3%A7%C3%A3o-MDTA615-e-SGAA090-e-como-incluir)****Saiba Mais**[Artigos PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
