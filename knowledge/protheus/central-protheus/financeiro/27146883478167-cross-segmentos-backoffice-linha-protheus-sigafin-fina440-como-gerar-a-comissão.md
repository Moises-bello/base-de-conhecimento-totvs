---
article_id: 27146883478167
category: Financeiro
content_hash: 87cd67149092fc2226b5a71bd3b326ef8152059f16a41ccef0300ac981ef5dd5
fetched_at: '2026-06-28T22:38:03.025182+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA440 Como gerar
  a comissão no valor bruto do título mesmo tendo impostos na emissão e na baixa
type: support-article
updated_at: '2024-10-17T19:01:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27146883478167-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA440-Como-gerar-a-comiss%C3%A3o-no-valor-bruto-do-t%C3%ADtulo-mesmo-tendo-impostos-na-emiss%C3%A3o-e-na-baixa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891368599) Tempo aproximado para leitura: **00:15:00 min****Dúvida**FINA440 Como gerar a comissão que está configurada 100% na baixa, ser gerada no valor bruto do título , mesmo que esse tipo:NF tenha impostos gerados na emissão e impostos que serão gerados na baixa do titulo  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões  
  
**Solução**No exemplo a seguir   
Temos uma nota fiscal que tem impostos de:

IR que seja gerado somente na baixa do título NF

INSS que será gerado na emissão do título

PIS, COFINS e CSLL que será gerado na emissão do título

Terei que ter as seguintes parametrizações

MV\_COMISIR = S

MV\_COMIINS = S

MV\_COMIPIS = S

MV\_COMICOF = S

MV\_COMICSL = S

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891374871)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891374871)

MATA040 - Cadastro de Vendedor

Terei que ter as configurações abaixo:

A3\_ICM='S' ,

A3\_ICMSRET='S',

A3\_BASEIR=2 ,

A3\_IPI='S',

A3\_ISS='S',

A3\_PISCOF=4

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883419799)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883419799)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891378839)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891378839)

Segue exemplo prático:

MATA410 - Pedido de venda  
Incluir um pedido no valor R$ 12.000,00 com impostos de IR, INSS e PCC

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891380375)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891380375)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891382551)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891382551)

E estou utilizando uma condição de pagamento que será gerado 3 títulos tipo:NF no contas a receber.

Titulo 1 parcela 0001 = R$ 4.000,00

Titulo 1 parcela 0002 = R$ 4.000,00

Titulo 1 parcela 0003 = R$ 4.000,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891384727)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891384727)

FINA040 - Contas a Receber

Será gerado os impostos abaixo:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883435927)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883435927)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891387287)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146891387287)

MATA490 - Manutenção de Comissões

Veja que o valor base para a comissão gerou no valor de bruto de R$ 4.000,00

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883439895)](https://centraldeatendimento.totvs.com/hc/article_attachments/27146883439895)

Sabia mais:

[FAT0052 Configuração das Comissões dos Vendedores](https://tdn.totvs.com/pages/viewpage.action?pageId=235598457#EXEMPLOS-1194431850)

[FINA440 - Calculo de comissões de títulos com impostos.](https://tdn.totvs.com/pages/viewpage.action?pageId=550308062)

[FIN0016 Cálculo de comissão com impostos](https://tdn.totvs.com/pages/viewpage.action?pageId=244444762)
