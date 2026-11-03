---
article_id: 360006849812
category: Contabilidade Gerencial - Escrituração Contábil - ECF
content_hash: 4d96bd2cc5e02bc921d66dbea4ddc8a5e1d84d066149d18f9d5cb750389812a3
fetched_at: '2026-06-28T22:40:47.349496+00:00'
product: protheus
section_id: 1500001537721
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECF - Erro Descritor
  Validador '
type: support-article
updated_at: '2022-02-28T13:44:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006849812-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECF-Erro-Descritor-Validador
---

**Ocorrência**Ao validar o arquivo do ECF no PGE (Programa Gerador de Escrituração) é apresentado erro.

"O descritor utilizado na escrituração não é suportado nesta versão do SPED ECF. Favor instalar a versão mais atual."

![erro_pge.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360007386472/erro_pge.png)  
  
**Ambiente**

Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.

**Causa**Este incidente ocorre devido a quantidade de caracteres utilizados no registro Y800 (Outras Informações).  
  
**Solução**É necessário avaliar as informações descritas no registro Y800 (Outras Informações), verifique o arquivo .RTF que está utilizando na geração da Escrituração Contábil.
