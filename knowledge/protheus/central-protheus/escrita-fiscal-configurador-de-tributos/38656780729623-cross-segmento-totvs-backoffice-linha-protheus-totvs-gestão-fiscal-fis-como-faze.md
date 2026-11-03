---
article_id: 38656780729623
category: Escrita Fiscal - Configurador de Tributos
content_hash: 5e86e4c6e6e80e80f880f86bd8012995f13a461cd5d7919d518b2d4d485d529e
fetched_at: '2026-06-28T22:39:17.610614+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal -
  FIS - Como fazer a devolução de compra com IBS/CBS forma Hibrida?
type: support-article
updated_at: '2026-02-26T12:31:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38656780729623-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-TOTVS-Gest%C3%A3o-Fiscal-FIS-Como-fazer-a-devolu%C3%A7%C3%A3o-de-compra-com-IBS-CBS-forma-Hibrida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780724247) Tempo aproximado para leitura: 05:00**min**  
  
**Dúvida**  
 Como fazer a devolução de compra com IBS/CBS forma Hibrida?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões  
  
**Solução**

A Devolução é o espelho da nota fiscal de origem e nesse caso o imposto deve ser calculado na origem, pois não há regras de devolução no fisa170

MV\_ESTADO = SP

Fornecedor = MG

Cadastro de Produtos

Origem = 0

Aliq IPI = 6,5%

TES da nota fiscal de entradas

CFOP = 2102

Calcula icms = sim

L fiscal icms = tributado

Sit trib icm = 00

Calcula ipi = não

L fiscal ipi = outros

pis/cof = ambos

Cred pis/cof = credita

Sit trib pis = 50

Sit tri cof = 50

IBS/CBS de acordo com a carga inicial

<https://tdn.totvs.com/pages/releaseview.action?pageId=955482625>

Regra de escrituração

Incidencia = tributado

cClasstrib = 000001

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656764947351)  
A regra de escrituração é a responsavel pela gravação dos campos CCT e CST na CJ3

1a) Nota fiscal de entradas

Quantidade 05, valor unitário 200,00 = valor total 1000,00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656764947607)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656764947735)

CJ3 é gerada por item

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780725143)

2a) Nota fiscal de devolução, opção retornar

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780725527)

TES da devolução

CFOP = 6202

Calcula icms = sim

L fiscal icms = tributado

Sit trib icm = 00

Calcula ipi = não

L fiscal ipi = outros

pis/cof = ambos

Cred pis/cof = debita

Sit trib pis = 00

Sit tri cof = 00

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780725783)

Precisa gravar a CJ3 para a transmissão da nota fiscal

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780726295)![](https://centraldeatendimento.totvs.com/hc/article_attachments/38656780726551)
