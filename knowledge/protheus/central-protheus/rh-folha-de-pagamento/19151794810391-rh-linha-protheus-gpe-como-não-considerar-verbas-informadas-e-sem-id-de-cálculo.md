---
article_id: 19151794810391
category: RH - Folha de Pagamento
content_hash: 413b4f86b57185dd5dee6547fc0e6ce4b09950265a0061ec049cd86995c46cd1
fetched_at: '2026-06-28T22:44:13.563838+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como não considerar verbas informadas e sem id
  de cálculo na base de cálculo para Imposto de Renda Simpificado
type: support-article
updated_at: '2025-04-15T14:03:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19151794810391-RH-Linha-Protheus-GPE-Como-n%C3%A3o-considerar-verbas-informadas-e-sem-id-de-c%C3%A1lculo-na-base-de-c%C3%A1lculo-para-Imposto-de-Renda-Simpificado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19151825074711) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Cálculo de IRRF com a utilização do mnemônico **P\_NDEDIRSI**.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

Eventuais verbas **lançadas, sem identificador de cálculo** e **com** incidência para **IR,** mas que subentenda-se que não devem ser consideradas na base de cálculo do IR simplificado, como por exemplo, "Diferença de Pensão Alimentícia", deverão ser informadas no mnemônico **P\_NDEDIRSI**.

Para configurar o mnemônico **P\_NDEDIRSI**, acesse **Atualizações > Definições de cálculos > Mnemônicos (GPEA300) >** **Pesquise pelo P\_NDEDIRSI > Clique em Alterar**.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310633590167)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28310633600279)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19151808127383)

**Importante**

As verbas informadas no mnemônico devem ser separadas por barras.   
Exemplo: **ZZ1/ZZ2/ZZ3**.

**Saiba Mais:**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[17841458 DRHCALCPRT-10231 DT Base IR incorreta quando existe verba sem identificador de cálculo lançada](https://tdn.totvs.com/pages/releaseview.action?pageId=786562489)
