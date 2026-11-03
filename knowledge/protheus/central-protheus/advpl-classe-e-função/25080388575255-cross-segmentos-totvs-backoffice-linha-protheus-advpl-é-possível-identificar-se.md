---
article_id: 25080388575255
category: ADVPL - Classe e Função
content_hash: 96404f6173da42c016f0bbb3f8da1bb443972ea1c54088793ac7721cd1db01ad
fetched_at: '2026-06-28T22:40:21.603628+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - ADVPL - É possível identificar
  se a execução do sistema ocorre via Smart Client desktop ou webapp?
type: support-article
updated_at: '2024-07-22T17:49:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25080388575255-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-ADVPL-%C3%89-poss%C3%ADvel-identificar-se-a-execu%C3%A7%C3%A3o-do-sistema-ocorre-via-Smart-Client-desktop-ou-webapp
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25080367342615) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**É possível identificar se a execução do sistema ocorre via Smart Client desktop ou webapp?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas as versões  
  
**Solução**

Para identificar se a execução ocorre via Smart Client desktop ou webapp, pode ser utilizado a função

*GetRemoteType,* no qual identifica o tipo e a versão do Smart Client em execução.

0 = Smart Client das versões 6 e 7 em ambiente Windows.

1 = Smart Client das verões 8 e 10 em ambiente Windows (\*).

2 = Smart Client das verões 8 e 10 em ambiente Linux /MacOS (\*).

3 = Não utilizado.

4 = Sessão TELNET do módulo 4GL.

5 = Smart Client versão HTML.

6 = Não utilizado.

7 = TOTVS Smart Client versão Windows CE (experimental, não homologado)

**Saiba mais:**

[GetRemoteType](https://tdn.totvs.com/display/tec/GetRemoteType)
