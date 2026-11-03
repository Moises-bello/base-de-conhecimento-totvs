---
article_id: 12044696025623
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 681a8437dace9eea728655449b716dd0f2e0a5aac5ec368130db8f28a78f3974
fetched_at: '2026-06-28T22:42:01.200029+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Como gerar o registro C174 no Sped Fiscal?
type: support-article
updated_at: '2023-02-01T19:22:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12044696025623-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Como-gerar-o-registro-C174-no-Sped-Fiscal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao gerar o Sped Fiscal o registro **C174 - Operações com arma de fogo** não é apresentado.  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) -  A partir da versão **12.1.25**  
  
**Solução**

Para gerar o registro C174 dentro do Sped Fiscal é necessário que possua um registro do tipo **C170** em operações de **saída**, modelo **01.** O registro contém a qualificação do item do documento fiscal, quando este pertence aos produtos cadastrados como armas de fogo.

Acesse o módulo Configurador (SIGACFG), em seguida em Ambiente /Cadastros / Parâmetros clicar em editar.

Preencha o parâmetro **MV\_ARMFOG** no configurador o parâmetro com o grupo de produto de Armas de fogos:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044237140759)

Preencha no cadastro de produto no campo Grupo **"B1\_GRUPO"**  informado no parâmetro **MV\_ARMFOG**

***![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044295994391)***

Realize a escrituração da sua nota de saída modelo 01.

Acesse a rotina de Livros Fiscais -> Atualizações -> Movimentos -> NF-e Manual de Saída > Complementos.

Preencha todos os campos da aba ***"*****Armas de Fogo":**

***![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044474902039)***

Ao gerar o SPED FISCAL o registro é apresentado:

***![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12044632313623)***
