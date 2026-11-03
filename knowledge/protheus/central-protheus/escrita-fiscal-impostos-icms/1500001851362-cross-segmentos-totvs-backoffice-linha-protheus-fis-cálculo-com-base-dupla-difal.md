---
article_id: 1500001851362
category: Escrita Fiscal - Impostos - ICMS
content_hash: 0af614e26f545ff75fbf6653d34ff06c5da2ce4273d24838c019fe9dfe180297
fetched_at: '2026-06-28T22:39:24.297796+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Cálculo com Base Dupla
  Difal EC 87- Destinatário Não Contribuinte
type: support-article
updated_at: '2024-08-27T11:41:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001851362-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-C%C3%A1lculo-com-Base-Dupla-Difal-EC-87-Destinat%C3%A1rio-N%C3%A3o-Contribuinte
---

**Dúvida**Qual configuração para realizar o cálculo do difal com base dupla destinatário não contribuinte?  
  
**Ambiente**  
Microsiga Protheus – Fiscal – A partir da versão 11.80  
  
**Solução**

Caso seja necessário calcular com base de cálculo do destinatário diferente da base de cálculo de origem, deve ser habilitado o parâmetro **MV\_BASDUPL = .T.;**

Nota de Saída: Ao alterar o parâmetro todas as operações seguirão a mesma regra, não sendo possível fazer para estados de destino específicos;

Para realizar o cálculo **base dupla** por estado, precisa ser informada a UF de destino que deseja que a base do ICMS Complementar seja diferente da base do ICMS Próprio no parâmetro **MV\_UFBASDP;**

**MV\_UFBASDP** - Parâmetro para serem informadas as siglas das unidades federativas (UF) que terão calculo com base dupla. **Recomenda-se separar as siglas com barra( / )**.

Exemplo:  
**MV\_BASDUPL** = .F.

**MV\_UFBASDP** = PR

Com essa configuração o sistema vai realizar o cálculo de base dupla somente para o estado destino PR;

Exemplo:  
Valor de Mercadoria = R$ 1.000,00  
ICMS Próprio= 1.000,00 \* 12% = 120,00  
Base de cálculo de Difal = R$ 1.000,00 - ICMS Próprio / 0,82 (alíquota interna Destino) = 1.073,17  
Valor Difal = 1.073,17 \* 18% - ICMS Próprio= 73,17

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102735853)

**Importante!**

**Para os Estados que calculam DIFAL considerando a diferença entre alíquota interestadual e interna**

Informe os Estados que calculam DIFAL considerando a diferença entre alíquota interestadual e interna no parâmetro **MV\_UFALCMP.**

**Exemplo:** MV\_UFALCMP =BA/MG

Base de cálculo de Difal =1073,17 \* a diferença entre alíquota interestadual e interna =64,39

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7578391016215)

**ASSUNTOS RELACIONADOS**<https://tdn.totvs.com.br/pages/releaseview.action?pageId=699815598>

<https://tdn.totvs.com/display/public/PROT/3511428+DSERFIS1-8154+DT+Tratamento+DIFAL+base+dupla>

<https://tdn.totvs.com/pages/releaseview.action?pageId=465386313>
