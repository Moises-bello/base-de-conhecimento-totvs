---
article_id: 360057428314
category: RH - Ponto Eletrônico
content_hash: d3559bcc59ad7618a1ff7c4ff74390ed80133d1a303d44d92bdf615d2c691219
fetched_at: '2026-06-28T22:44:58.195087+00:00'
product: protheus
section_id: 206956208
source: central-protheus
title: RH - Linha Protheus - PON - Como customizar o Espelho de Ponto - PONR010
type: support-article
updated_at: '2025-04-03T14:38:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057428314-RH-Linha-Protheus-PON-Como-customizar-o-Espelho-de-Ponto-PONR010
---

**Dúvida**Como **customizar o Espelho de Ponto - PONR010?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**O fonte **PONR010 - Espelho de Ponto** possui um ***RDMAKE*** chamado **IMPESP** que está disponível para customização no Portal de *Download* e Atualizações da TOTVS, basta buscar por Protheus - Artefatos Gerais de Produto - **RDMAKE** Padrão.  
  
No link abaixo, temos todos os *RdMakes* padrões, disponíveis no RH.  
[RH - Linha Protheus - GPE - Como fazer o download (baixar) os RDMAKES de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044814174-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-os-RDMAKES-de-RH?source=search)  
  
O *RDMAKE* deve ser **customizado** conforme necessidade **e não o PONR010**, pois na impressão do Espelho de Ponto, **esse *RDMAKE* será chamado**, considerando assim **customizações efetuadas**.   
Caso precise de auxílio na customização, indicamos o **agendamento de um analista in loco.**

Para que o **RDMAKE seja executado** ao gerar o relatório de espelho de ponto, será necessário **incluí-lo no menu do módulo**, conforme abaixo:  
  
Acesse o Configurador e siga no caminho: Ambiente - Cadastros - Menus e marque apenas o módulo de Ponto Eletrônico:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6044927876119)  
  
Clique em Adicionar para enviar todos os menus do Ponto Eletrônico para a direita:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6044844102807)  
  
Clique no menu onde deseja que a rotina seja incluída e em Novo Item (ela pode estar em qualquer menu, a imagem abaixo é apenas um exemplo):  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6044836829207)  
  
Insira a descrição do modo que preferir e os demais campos deixe como o exemplo abaixo:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6044877721623)

**Observação:** O módulo do Ponto Eletrônico atende a Portaria1.510 e a Portaria 671, portarias aplicadas a todos que utilizam o controle de ponto. Para casos pontuais de decisão judicial, MTE, etc., que diferem das portarias 1.510 e 671, o produto não tem a obrigatoriedade de atender, visto que não se aplica a todas as situações.

**Informações importantes**Pacote de Expedição Contínua do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854>  
Pacote de Expedição Contínua do eSocial: [https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051585234-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-acumulado-do-eSocial)  
  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
