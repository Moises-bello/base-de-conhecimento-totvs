---
article_id: 360034774574
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 566286a8ecc55f10ad7b53830360c53e133d96df3917901bafbec10ac91d55e0
fetched_at: '2026-06-28T22:42:03.856026+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'MP - FIS- Apuração de ISS - EFD ICMS/IPI - Bloco B: Como o sistema identifica
  se o estabelecimento Não é Contribuinte do ICMS'
type: support-article
updated_at: '2021-04-30T13:22:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034774574-MP-FIS-Apura%C3%A7%C3%A3o-de-ISS-EFD-ICMS-IPI-Bloco-B-Como-o-sistema-identifica-se-o-estabelecimento-N%C3%A3o-%C3%A9-Contribuinte-do-ICMS
---

**Dúvida**

Como o sistema identifica se o estabelecimento Não é Contribuinte do ICMS?

**Ambiente**Microsiga Protheus - a partir da versão 12.1.17  
  
**Solução**

O estabelecimento será considerado como NÃO Contribuinte do ICMS se:

A Inscrição Estadual não estiver preenchida no cadastro da filial(campo M0\_INSC) ou;  
Se o conteúdo da Inscrição Estadual do cadastro da filial estiver preenchido como conteúdo “ISENTO” ou “ISENTA”, ou;

Se o conteúdo do parâmetro MV\_SM0CONT estiver com conteúdo igual a “2”  
Se qualquer umas das três hipóteses acima for verdadeira, será considerado como Não Contribuinte do ICMS, caso contrário será considerado como Contribuinte do ICMS.
