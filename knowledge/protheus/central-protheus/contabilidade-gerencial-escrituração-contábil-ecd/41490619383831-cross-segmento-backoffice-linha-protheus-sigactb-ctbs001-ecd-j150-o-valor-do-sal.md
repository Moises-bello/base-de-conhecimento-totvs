---
article_id: 41490619383831
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: 98ab882a9a319a4f49c4889461e9c4459e65ca9a28c0aa758d70c6e234f636ce
fetched_at: '2026-06-28T22:40:44.555844+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECD J150 O
  valor do saldo inicial (VL_CTA_INI) do código de aglutinação informado na DRE é
  diferente do saldo final do código (VL_CTA_FIN) informado na DRE do período imediatamente
  anterior.
type: support-article
updated_at: '2026-06-26T20:25:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41490619383831-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-J150-O-valor-do-saldo-inicial-VL-CTA-INI-do-c%C3%B3digo-de-aglutina%C3%A7%C3%A3o-informado-na-DRE-%C3%A9-diferente-do-saldo-final-do-c%C3%B3digo-VL-CTA-FIN-informado-na-DRE-do-per%C3%ADodo-imediatamente-anterior
---

Ao recuperar o arquivo do ano anterior no validador, ocorre erro porque o saldo inicial (VL\_CTA\_INI) no arquivo atual não corresponde ao saldo final acumulado (VL\_CTA\_FIN) do período anterior. Isso ocorre pois o sistema gera demonstrativos trimestrais e um anual acumulado, mas ao gerar o arquivo do ano seguinte considera apenas o último trimestre. Para corrigir, deve-se informar na pergunta "Rev.Anterior?" a revisão que contém o demonstrativo anual, garantindo que o saldo inicial acumulado seja usado.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41490619363607) Tempo aproximado para leitura: **40 min**  
  
**Dúvida**

Ao recuperar o arquivo no validador do ano anterior, no arquivo que está sendo validado, o sistema apresenta erro:  
  
*"8 - VL\_CTA\_INI - O valor do saldo inicial (VL\_CTA\_INI) do código de aglutinação informado na DRE é diferente do saldo final do código (VL\_CTA\_FIN) informado na DRE do período imediatamente anterior."*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41490599863703)

Valor esperado: R$ 4.500,00.  
Conteúdo do campo:  R$ 1500,00.  
  
|J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
DO IRPJ/CSLL|**1500,00**|C|2796015,14|C|R| |  
  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial – A partir da versão 12.  
  
**Causa**

Ao recuperar o arquivo do ano anterior 2024, no arquivo 2025 que está sendo validado, o validador compara no registro J150 o saldo final (VL\_CTA\_FIN) do arquivo de 2024 com o saldo inicial (VL\_CTA\_INI) no arquivo de 2025.

1. No arquivo de 2024, o ECD foi gerado com geração de 5 demonstrativos no arquivo trimestral:    
     
   [Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBS001 - ECD, Geração de 5 demonstrativos quando arquivo trimestral unificado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6141626072855-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBS001-ECD-Gera%C3%A7%C3%A3o-de-5-demonstrativos-quando-arquivo-trimestral-unificado?source=search)  
     
   Foi informada a pergunta com "Sim" e o parâmetro [MV\_ECDTRIA](https://tdn.totvs.com/pages/releaseview.action?pageId=665034639) estava configurado para gerar, além dos 4 conjuntos de demonstração (1 por trimestre), mais 1 referente ao período anual.

   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/41490599866647)

   O sistema gerou o demonstrativo conforme abaixo (4 conjuntos de demonstração - 1 por trimestre, gera +1 referente ao período anual):

   1. |J005|**01012024|31032024**|1||     >>>>1º Trimestre  
      |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
      DO IRPJ/CSLL|0,00|C|**1000,00**|C|R| |
   2. |J005|**01042024|30062024**|1||     >>>>2º Trimestre  
      |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
      DO IRPJ/CSLL|0,00|C|**1000,00**|C|R| |
   3. |J005|**010472024|30092024**|1||    >>>>3º Trimestre  
      |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
      DO IRPJ/CSLL|0,00|C|**1000,00**|C|R| |
   4. |J005|**011072024|31122024|**1||    >>>>4º Trimestre  
      |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
      DO IRPJ/CSLL|0,00|C|**1500,00**|C|R| |
   5. |J005|**01012024|31122024**|1||    >>>>5º Anual   
      |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
      DO IRPJ/CSLL|0,00|C|**4500,00**|C|R| |

   Verifique que o campo de saldo final (**VL\_CTA\_FIN)** :

   * 4 conjuntos de demonstração - 1 por trimestre, = não acumulou o saldo final.

* 1 referente ao período anual = acumulou o saldo dos 4 trimestres.

|  |  |
| --- | --- |
| Saldo final ( **VL\_CTA\_FIN) 2024** | período |
| R$ 1.000,00 | 1º Tri |
| R$ 1.000,00 | 2º Tri |
| R$ 1.000,00 | 3º Tri |
| R$ 1.500,00 | 4º Tri |
| Total: R$   4.500,00 | Anual |

2. Ao gerar o arquivo de 2025 o sistema gerou no campo saldo anterior (VL\_CTA\_INI) somente o valor do 4.º trimestre e não considerou o saldo acumulado do período anual  
     
   |J150|1790|DR200003002001001001004|T|2|DR200003002001001001003|RESULTADO OPERACIONAL ANTES  
   DO IRPJ/CSLL|**1500,00**|C|2796015,14|C|R| |  
     
   Obs.: Para que o erro não seja apresentado, é preciso que o sistema gere o valor de R$ 4.500,00.

**Solução**

Para que o sistema gere no arquivo de 2025 o valor acumulado de 2024 no campo saldo anterior (VL\_CTA\_INI) do DRE (J150), é preciso informar na pergunta "Rev.Anterior?". O número da revisão de 2024, gerada no Protheus com o 5º demonstrativo.

Dessa forma, o sistema irá buscar na revisão de 2024 o valor de saldo final VL\_CTA\_FIN do 5º demonstrativo e compor no arquivo de 2025 o valor de saldo inicial (VL\_CTA\_INI) acumulado.

* Ao gerar o arquivo de 2025

Quando apuração é trimestral no período atual (Ex.2025)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41490599868439)

Quando apuração é Anual no período atual (Ex.2025)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41528461728407)
