---
article_id: 8998679574807
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 2d993b9cb32b46fedb4cf1a788e38fd838172ed07ef0966c4295d441f446297b
fetched_at: '2026-06-28T22:42:00.971322+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - Por que o Bloco
  G apresenta valores diferentes do Relatório CIAP?
type: support-article
updated_at: '2024-04-25T12:06:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8998679574807-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Por-que-o-Bloco-G-apresenta-valores-diferentes-do-Relat%C3%B3rio-CIAP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22892118156311) Tempo aproximado para leitura: **00:03:00 min** **Dúvida** Por que o **Bloco G** apresenta valores diferentes do **Relatório CIAP**?  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) -Livros Fiscais – A partir da versão 25  
  
**Solução**

Quando o fator de apropriação é diferente de 1, os valores do **Bloco G** e do **Relatório CIAP** não batem 100% porque se referem à legislações diferentes.

Os registros do **Bloco G** e o **Relatório CIAP** não podem ser comparados, pois se referem a legislações diferentes com regras distintas.  
  
O valor constante  no **Relatório CIAP** e **Tabela SFA - Estorno Mensal CIAP** é sobre o crédito mensal a apropriar e considera o seguinte cálculo:  
  
**Valor do total do crédito, dividido pela quantidade de parcelas (48) e multiplicado pelo coeficiente.**  
  
Já o cálculo do **Bloco G** segue as orientações do  guia prático do **Sped Fiscal:**  
  
![](https://totvssuporte.zendesk.com/attachments/token/74GABc3x4pXTu6QdUMJoDdLct/?name=inline-1604340701.png)​​  
  
Dessa forma, o campo **10 - VL\_PARC\_PASS** do **G125 - Movimentação do bem** faz a soma dos campos **5 - VL\_IMOB\_ICMS\_ OP** + **6 VL\_IMOB\_ICMS\_ ST** +**7 VL\_IMOB\_ICMS\_ FRT** +**8 VL\_IMOB\_ICMS\_ DIF,** conforme os campos abaixo da tabela **SF9 - Manutenção CIAP** que podem ser visualizados via rotina **MATA905** e divide pela quantidade de **parcelas (48),** o que resulta em um valor diferente no constante no Relatório **CIAP** e **SFA**  
  
**G125 Campo 5: Icms Próprio -  F9\_VALICMP**  
**G125 Campo 6: ICMS ST - F9\_VALICST**  
**G125 Campo 7:ICMS Frete F9\_VALFRET**  
**G125 Campo 8: ICMS Comple -  F9\_VALICCO**  
  
Assim, no campo **5- SOM\_PARC do G110** o valor fica diferente do relatório, pois a validação deste campo  é segundo o guia prático.  
  
![](https://totvssuporte.zendesk.com/attachments/token/SZl6FV9twU5lohWuSmaJwTH25/?name=inline-1493810724.png)​​  
  
Foi liberado o retorno da Consultoria Tributária da TOTVS abrangendo o assunto no tópico 3.3.2, segue FAQ para mais informações sobre a diferença e cálculo:

<https://tdn.totvs.com.br/pages/releaseview.action?pageId=821573988#EFDICMS/IPI%E2%80%93ConceitodeCIAPeBlocoGNT-3.3.2G110-ICMS%E2%80%93AtivoPermanente%E2%80%93CIAP>
