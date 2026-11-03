---
article_id: 360053496854
category: RH - FGTS / SEFIP
content_hash: 0d581b58b12a82a6ba63667c6a8ce29f0cb4eb931c5afc629e1ebde227b78b26
fetched_at: '2026-06-28T22:43:41.354271+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Ao gerar a SEFIP por centro de custo e tomador
  está levando todos os centros de custo em um único tomador.
type: support-article
updated_at: '2025-09-04T20:19:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053496854-RH-Linha-Protheus-GPE-Ao-gerar-a-SEFIP-por-centro-de-custo-e-tomador-est%C3%A1-levando-todos-os-centros-de-custo-em-um-%C3%BAnico-tomador
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34708448666519) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao gerar a SEFIP por centro de custo e tomador está levando os funcionários de outros centos de custo  em um único tomador.

**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  A partir da Versão 12.1.17

**Solução**O motivo por estar trazendo no centro de custo incorreto  é que todos podem estar com o mesmo CNPJ, o arquivo SEFIP.RE esta aglutinando, **pois o layout SEFIP não vai aceitar CNPJ iguais no registro 20 (tomador)**.   
  
Lembrando que o tomador representa 1 empresa 1 cnpj, dentro desse tomador(centro de custo) você aloca o funcionário que esta prestando serviço. Cada tomador (centro de custo ) tem que estar com um CNPJ diferente.  
  
Verifique abaixo:

Quando tenho outros centros de custo com o CNPJ diferente na aba tomador verifique que trás corretamente  a linha  20 do primeiro tomador abaixo os funcionários que sempre começam com 30 e depois novamente a linha de registro 20 outro tomador   
![](https://lh3.googleusercontent.com/-IWEyHfEsr4Q/X1JQV2xPUkI/AAAAAAAAAzI/xXG80C2NVcAKpBDo_yjriQ9SqQoOxBN0ACK8BGAsYHg/s0/2020-09-04.png)  
  
Se eu tiver o mesmo CNPJ nos tomadores  irá alocar todos no mesmo tomador trazendo somente uma linha de registro 20 conforme abaixo:  
  
![](https://tdn.totvs.com/download/attachments/561852887/image2020-9-3_14-38-33.png?version=1&modificationDate=1599155365517&api=v2)  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.**Faça uma verificação em todos os centros de custo na aba tomador e verifique se os CNPJ está de acordo com centro de custo para que possa trazer corretamente na SEFIP.

Segue abaixo documentação de como gerar a SEFIP por tomador

[MP - GPE - Como gerar a SEFIP por tomador código 150 ou 155 ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051779433-MP-GPE-Como-gerar-a-SEFIP-por-tomador-c%C3%B3digo-150-ou-155-?source=search)  
  
**Saiba Mais: <https://tdn.totvs.com/display/public/PROT/FGTS>**
