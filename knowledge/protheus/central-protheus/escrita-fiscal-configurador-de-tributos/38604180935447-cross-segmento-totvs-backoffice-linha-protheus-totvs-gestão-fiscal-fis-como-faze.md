---
article_id: 38604180935447
category: Escrita Fiscal - Configurador de Tributos
content_hash: b420b7385383bcacedd0beeb76cdcd2fe2be200e1bac4d1ae43e16a057bc2e58
fetched_at: '2026-06-28T22:39:17.619367+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS Como fazer devolução de Saidas com calculo IBS/CBS forma Hibrida ?
type: support-article
updated_at: '2026-02-24T14:30:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38604180935447-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-fazer-devolu%C3%A7%C3%A3o-de-Saidas-com-calculo-IBS-CBS-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171043351) Tempo aproximado para leitura: 08:00**min**  
  
**Dúvida**  
Como fazer devolução de Saidas com calculo IBS/CBS forma Hibrida ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**  
A nota fiscal de devolução é o espelho da nota fiscal de origem, sendo assim deve verificar se na origem os impostos IBS/CBS foram calculados de forma correta.

Nota fiscal de saidas - calculo de forma Hibrida

MV\_ESTADO = SP

MV\_TXPIS = 1.65%

MV\_TXCOFIN = 7.6%

MV\_ICMPAD = 18%

Cliente = SP

Cadastro de Produtos

Origem = 0

Aliq ipi = 6,5%

TES

Calcula icms = sim

L fiscal icms = tributado

Sit trib icm = 00

Calcula ipi = sim

L fiscal ipi = tributado

Cod trib IPI = 50

pis/cofins = ambos

cred pis/cofis = debita

sit trib pis =01

sit trib cof = 01

IBS/CBS = de acordo com a carga inicial

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

TR0001

TR0002

1a) Pedido de Vendas

Quantidade 10 - valor unitário = 100,00 = valor total = 1000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171043863)

Após faturar NF fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171045655)

CJ3

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171046679)

2a) Devolução - Documento de entradas botão retornar

No TES da nota fiscal de saidas deve ter o TES da devolução

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171047831)

TES

Calcula icms = sim

L fiscal icms = tributado

Sit trib icm = 00

Calcula ipi = sim

L fiscal ipi = tributado

Cod trib IPI = 00

pis/cofins = ambos

cred pis/cofis = credita

sit trib pis =50

sit trib cof = 50

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171048343)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38604171049623)
