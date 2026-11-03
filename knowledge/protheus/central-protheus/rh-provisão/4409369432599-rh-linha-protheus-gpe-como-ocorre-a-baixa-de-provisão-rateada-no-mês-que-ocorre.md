---
article_id: 4409369432599
category: RH - Provisão
content_hash: 0fb126a8a911280300106c74e6bf13544aa05536fff985711d1e3ed34268fc97
fetched_at: '2026-06-28T22:43:55.833557+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como ocorre a baixa de provisão rateada no mês
  que ocorre alteração do percentual ou centro de custos
type: support-article
updated_at: '2025-10-24T12:34:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409369432599-RH-Linha-Protheus-GPE-Como-ocorre-a-baixa-de-provis%C3%A3o-rateada-no-m%C3%AAs-que-ocorre-altera%C3%A7%C3%A3o-do-percentual-ou-centro-de-custos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998253824535) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como ocorre a baixa de provisão rateada no mês que ocorre alteração do percentual ou centro de custos?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões.  
  
**Solução**Uma vez cadastrada a programação de rateio, qualquer alteração (mudança de centro de custos, item, classe valor ou programação de rateio diferente da competência anterior) o sistema usará uma nova referência do cálculo anterior, baixando o valor do centro de custos que não fará parte da programação daquela competência, executando o próximo como sendo o primeiro cálculo de rateio e gerando os lançamentos de provisão rateada como acumulados.

Abaixo, um exemplo de movimentações de programação de rateio diferentes para cada competência.

Na primeira competência o primeiro cálculo não possui programação de rateio cadastrada , sendo desta forma calculada no centro de custos de cadastro (Centro de custos 001):

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125168660375/mceclip1.png)

Na competência 02/2022 , efetuamos uma programação de rateio 100% para um centro de custos diferente do cadastro e do cálculo da competência anterior:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125238475927/mceclip2.png)

Geração do Relatório de provisão "Imprimir Mensal de Férias":   
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125580783127/mceclip5.png)

Veja que na geração do relatório, o sistema baixa o valor total que o centro de custos anterior possui (essa baixa acontece como BAIXA DE TRANSFERÊNCIA) e provisiona todo o valor devido no novo centro de custos. **O centro de custos do rateio daquela competência receberá o valor cheio.**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125623520791/mceclip6.png)

Na competência 03/2022, realizamos uma programação de rateio, mantendo o centro de custos 002 e rateando apara mais 2 centros de custos (001 e 003):

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125926497943/mceclip8.png)

Vamos começar a analise do relatório pelo **Centro de custos 002:**  
O sistema baixa a provisão já ajustando o valor que corresponde ao rateio na linha do mês (R$ 200,00) e baixa todo o histórico referente ao saldo anterior (R$ 400,00).

Já nos demais centros de custos , os valores são apresentados na linha "no Mês" com seus respectivos valores :

R$ 2.400,00 / 12 X 3 avos = R$ 600,00

R$ 600,00 / 3 Centros de custos (mesmo percentual de rateio=33,33333) = R$ 200,00 no Mês

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6125954981911/mceclip9.png)

**Importante:**

1) Quando já existir cálculo de provisão e não estiver configurada a programação de rateio , para que passe a utilizar a rotina, será necessário realizar na competência anterior o primeiro mês de cálculo , de modo que a rotina busque referência  da tabela de provisão rateada (RHT). Para isto é necessário apenas habilitar o parâmetro MV\_RATPROV.

2) As verbas de baixa de transferência **não serão apresentadas no acumulado de provisão**. Serão geradas apenas em memória e no relatório. A contabilização dessas verbas ocorrerá normalmente , caso tenha configurado a contabilização de baixas de transferência.

**Saiba mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

<https://tdn.totvs.com/pages/releaseview.action?pageId=382561210>  
<https://tdn.totvs.com/pages/releaseview.action?pageId=330834695>
