---
article_id: 10599806014103
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 5fa70195b649b046834ec6d53ad01673ecc4cb9d3f3fd0d701366a329bcd2e4d
fetched_at: '2026-06-28T22:39:20.323138+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - Como emitir Nota
  Fiscal de complemento de ICMS ST / FECP ST RJ?
type: support-article
updated_at: '2022-11-30T17:51:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10599806014103-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Como-emitir-Nota-Fiscal-de-complemento-de-ICMS-ST-FECP-ST-RJ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:05**min** **Dúvida**Como emitir Nota Fiscal de complemento de ICMS ST / FECP ST RJ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**O complemento do ICMS ST com base de calculo e FECP ST será realizado na rotina nota fiscal manual (  mata920 ) para as notas fiscais de saídas

Verificar as configurações abaixo:

1a) Rotina UF x UF - fisa080

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10598655755927)

O campo CFC\_FCPAJT = para o estado do RJ sempre = 1

Se não tiver o campo criar através do compatibilizador UPDDISTR

2a) Configuração da TES

Calcula icms = não

L fiscal icms = observações ou zerado

CST = 10 ( exceto 60/90 que não faz impressão no danfe )

MKP ICM COMP = sim

Marg solid = nunca

Agrega valor = não

Agrega solid = sim

Isen fecp = em banco

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10598939167639)

Acessar a rotina mata920 para fazer o complemento com base de calculo

Exemplo

Venda de SP para RJ - complemento de 60,00 de ICMS ST e 20,00 FECP ST

Tipo da nota fiscal = complemento de ICMS

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10599468318231)

No valor da mercadoria deve ser levado a soma do ICMS ST + FECP ST = 80,00

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10599483894423)

Livro fiscal

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10599545584791)

CD2

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10599578204055)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10599607197079)

O campo CD2\_FCPAJT para o RJ deve estar com o conteúdo = 1 para não gerar rejeição 610

Boletim

<https://tdn.totvs.com/pages/releaseview.action?pageId=701693062>

<https://tdn.totvs.com/display/public/PROT/CADUF+-+UFxUF>
