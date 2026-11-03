---
article_id: 360005104852
category: RH - Cadastros
content_hash: a2d59a16c1f93fdfa3de20024a43dc2ae42a1eefeca52a1d42b3f0db9245bc88
fetched_at: '2026-06-28T22:44:52.875296+00:00'
product: protheus
section_id: 32419135703319
source: central-protheus
title: RH - Linha Protheus - PON - Como funciona o parâmetro MV_SUMINTA
type: support-article
updated_at: '2025-12-10T16:55:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005104852-RH-Linha-Protheus-PON-Como-funciona-o-par%C3%A2metro-MV-SUMINTA
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36917666677527)****Tempo aproximado para leitura: 00:01:00 min**  
  
**Dúvida**  
Como funciona o parâmetro MV\_SUMINTA?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
O parâmetro **MV\_SUMINTA,** permite que os minutos aleatórios da entrada do intervalo sejam somados com a verificação da duração do intervalo, ou seja, a diferença entre a saída para o intervalo e a entrada dele não deve ser inferior a sua duração.  
  
Procedimentos para configuração:  
**1.** No **Configurador (SIGACFG);**  
**2.** Acesse **Ambientes/Cadastros/Parâmetros;**  
**3.** Pesquise o parâmetro **MV\_SUMINTA;**  
**4.** Defina se serão somados os minutos aleatórios à duração total do intervalo: **1= Soma ou 2- Não Soma**.  
  
A configuração do parâmetro permite as seguintes opções:  
**1.** Soma os minutos aleatórios com a duração total do intervalo;  
**2.** Não considera a duração total do intervalo, exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/31755439078039)  
  
**Importante**: Este atendimento atende exclusivamente aos casos de saída de intervalo com entrada aleatória.  
  
  
**Saiba mais:**  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
