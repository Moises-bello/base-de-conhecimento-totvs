---
article_id: 34432234051991
category: eConsignado (Crédito do Trabalhador)
content_hash: 68e05459a901fab0d4a31a64c4009b513d62dea4e8eb451a318566d08d36ec99
fetched_at: '2026-06-28T22:43:07.167230+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE -  Provisão do eConsignado nas férias quando há pagamento
  de Abono Pecuniário
type: support-article
updated_at: '2026-06-26T14:35:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34432234051991-RH-Linha-Protheus-GPE-Provis%C3%A3o-do-eConsignado-nas-f%C3%A9rias-quando-h%C3%A1-pagamento-de-Abono-Pecuni%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34432217847703) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Qual o cálculo correto para o eConsignado / Credito do Trabalhador quando há pagamento de abono pecuniário.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - a partir da versão 12.1.2210  
  
**Conceito**  
O valor pago no Abono Pecuniário tem natureza **indenizatória** e não salarial, e por esse motivo, ele não integra o salário, não sofre desconto de INSS e não compõe a base de cálculo da contribuição previdenciária.

Além disso, conforme o [**Manual do Crédito Consignado do Trabalhador**](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf), no quadro **exemplificativo de rubricas** que **não** devem ser consideradas para o cálculo da remuneração disponível, consta expressamente que o item **Férias – Abono Pecuniário** **não** deve ser incluído na base de cálculo da remuneração disponível.

Dessa forma, **o abono pecuniário não integra a remuneração disponível nem deve ser considerado para fins de cálculo da margem consignável utilizada no desconto ou provisão do crédito do trabalhador**, sob pena de descumprimento das normas vigentes e comprometimento da proteção legal do salário.

**Solução**  
Conforme descrito no conceito acima, no cálculo das férias o Sistema fará o cálculo da provisão do eConsignado utilizando **somente os dias de férias**.  
  
No exemplo abaixo temos:  
  
**Valor da parcela:** R$ 7.453,04  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432234027927)**  
  
**Dias de Férias:** 20  
**Dias de Abono:** 10  
**Fórmula para cálculo da provisão:** Valor da Parcela / 30 \* Dias de Férias  
  
**Cálculo da Provisão:**  
7.453,04 / 30 \* 20 =   
248,43 \* 20 = 4.968,69  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432234029591)  
  
Após **integração** do roteiro **FER** na folha, o **valor provisionado** nas férias (verba com id **1971**) será **devolvida** no provento (verba com id **1973**) e **somado** ao valor do **líquido** das **férias** (verba com id **0102**) para que o valor devolvido **não interfira no líquido da folha de pagamento, caso não exista verba vinculada ao id 1979 - Dev. eConsignado Férias.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34432217851159)  
  
Para que, no momento da integração do roteiro **FER** a verba de líquido de férias seja apresentada na folha com o mesmo valor do recibo de férias, siga os passos do artigo: [RH - Linha Protheus - GPE - Verba de líquido das férias é demonstrada na folha com valor maior que o calculado no recibo de férias para funcionários que tiveram provisão do eConsignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34732356784279-RH-Linha-Protheus-GPE-Verba-de-l%C3%ADquido-das-f%C3%A9rias-%C3%A9-demonstrada-na-folha-com-valor-maior-que-o-calculado-no-recibo-de-f%C3%A9rias-para-funcion%C3%A1rios-que-tiveram-provis%C3%A3o-do-eConsignado)  
  
**Saiba Mais**  
[Manual do Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)  
[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)  
[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)  
[RH - Linha Protheus - GPE - Como cadastrar as verbas de Provisionamento nas Férias e Adiantamento referente ao eConsignado (Programa Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32292447017239-RH-Linha-Protheus-GPE-Como-cadastrar-as-verbas-de-Provisionamento-nas-F%C3%A9rias-e-Adiantamento-referente-ao-eConsignado-Programa-Cr%C3%A9dito-do-Trabalhador)
