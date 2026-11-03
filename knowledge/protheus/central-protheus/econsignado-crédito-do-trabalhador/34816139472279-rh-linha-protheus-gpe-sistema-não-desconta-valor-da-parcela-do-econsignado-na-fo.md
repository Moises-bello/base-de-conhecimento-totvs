---
article_id: 34816139472279
category: eConsignado (Crédito do Trabalhador)
content_hash: f84fef93fd95210df8be8bd64b65c968b617159209e6b6d01335c0cf44e7ac9f
fetched_at: '2026-06-28T22:43:07.392085+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não desconta valor da parcela do eConsignado
  na folha de forma correta quando funcionário esteve de férias
type: support-article
updated_at: '2026-05-22T18:56:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34816139472279-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-desconta-valor-da-parcela-do-eConsignado-na-folha-de-forma-correta-quando-funcion%C3%A1rio-esteve-de-f%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34816132894743) Tempo aproximado para leitura: **00:03:00min**  
  
**Ocorrência**  
Quando um funcionário esteve de férias, o Sistema não calcula o desconto do eConsignado corretamente na folha de pagamento, descontando um valor menor que a parcela devida.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
A ausência do desconto ou desconto parcial do eConsignado na folha de pagamento quando o funcionário este de férias ocorre devido o funcionário não ter Margem suficiente.  
Atualmente o Sistema **não utiliza** as verbas de férias na **Margem** do eConsignado devido a diversas opiniões de diferentes clientes sobre a utilização ou não das verbas de férias, mesmo estando com sim para INSS.

Sendo assim, optamos por deixar a critério/ entendimento do cliente se serão incluídas ou não na Margem de cálculo, sendo necessário informá-las no mnemônico **P\_ADICONS** e reprocessar o cálculo da folha.  
  
**Solução**  
**Conceito:** O mnemônico **P\_ADICONS**, permite incluir outras verbas de provento a serem somadas à margem de consignação total, antes da aplicação do percentual máximo de desconto.  
  
Ele foi criado para que a verba contida no campo **RCM\_PDSUP**possa ser adicionada ao mnemônico, assim como as  **VERBAS DE FÉRIAS** (caso ocorra) permitindo que seu valor seja somado à margem utilizada no cálculo do eConsignado.  
  
**Utilização:** As verbas informadas no **P\_ADICONS**devem ser separadas com barras. Exemplo: **"001/002/003"**  
  
Para ajustar o Mnemônico acesse **Atualizações > Definição de calculo > Mnemônicos**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/40673361871639)

Após incluir as verbas no Mnemônico calcule a folha.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34816139430807)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34816132896663)  
  
Observe que o sistema considerou para a Margem as verbas de Salario + verbas incluídas no Mnemônico P\_ADICONS que são Férias + 1/3 de férias + Auxilio doença 15 dias realizando o desconto dos dois contratos em sua totalidade.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34816132897687)  
  
**Importante**  
A verba de id **1973**, que refere-se a **devolução** do valor **provisionado nas férias** (soma dos id's **1971** e **1972**) **não será considerada na Margem** para desconto do eConsignado em folha de pagamento, pois não tem caráter **remuneratório**.  
  
**Observação:** Caso as verbas de férias (férias, 1/3 de férias, férias mês seguinte, 1/3 de férias mês seguinte, médias, etc.) que entraram no cálculo das férias não sejam adicionadas neste mnemônico, o Sistema **Não as utilizará na margem da folha de pagamento**. É de entendimento do cliente incluí-las ou não para composição da margem do eConsignado.  
  
**Saiba mais:**

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)

[Manual Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)
