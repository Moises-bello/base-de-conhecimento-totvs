---
article_id: 4416023965975
category: MDT - EPI
content_hash: 6ad7ef82c815a820f3fab024f3b4faa07e4699e69661502bd5b79087c4e5cc09
fetched_at: '2026-06-28T22:44:25.288141+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Ao tentar incluir um EPI o campo Epi Eficaz (TNF_EPIEFI)
  fica bloqueado
type: support-article
updated_at: '2025-03-03T18:10:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416023965975-RH-Linha-Protheus-MDT-Ao-tentar-incluir-um-EPI-o-campo-Epi-Eficaz-TNF-EPIEFI-fica-bloqueado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372642274199) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**Ao tentar incluir um **EPI** o campo **Epi Eficaz** (TNF\_EPIEFI) fica bloqueado.  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Causa**Isso acontece devido ao parâmetro **MV\_NG2CEPI** (Indica se a empresa consiste o EPI) está com **N:**![EPI_Eficaz_Bloqueado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4416007944727)  
  
**Solução**Para liberar o campo **Epi Eficaz** (TNF\_EPIEFI) siga os procedimentos abaixo:  
1. Acesse o modulo Configurador (SIGACFG) no caminho: ambiente > cadastros > parâmetros e busque pela parâmetro **MV\_NG2CEPI** e depois faça a alteração do parâmetro para **S**.  
  
![EPI_Eficaz_configurador.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4416001177367)  
  
2. Depois que alterar o parâmetro abra novamente a rotina de **Funcionário x EPI** (MDTA695) no SIGAMDT e efetue a inclusão.  
  
![EPI_Eficaz_Liberado.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4416001176983)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
