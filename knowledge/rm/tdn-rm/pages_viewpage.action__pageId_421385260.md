---
content_hash: fcbeb87d4f5ec0e9ec3567d649bee90ec726519a66249ff66d0a744e8f216d6e
fetched_at: '2026-06-29T00:09:14.802214+00:00'
page_id: '421385260'
product: rm
source: tdn-rm
title: Estado/municípios do contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385260
version: 3
---

A funcionalidade medição por trecho consiste na criação de um rateio por estado/município para as medições de períodos de contratos onde, ao serem faturados, os impostos sejam apurados corretamente para cada estado/município, ou seja, cada município terá a emissão do faturamento em separado.

Pode-se definir o rateio por estado/município por contrato. Esta tela é um anexo de contratos. Ao acionar o anexo e incluir um estado/município estarão disponíveis as opções de Estado, Código do município e o percentual de rateio para o Município, o percentual total do rateio deve fechar em 100%.

O rateio por estado/município também pode ser definido na edição do item de medição e na liberação de contrato, para o mesmo deve acionar o processo de Medição do item de contrato ou o processo de Liberação de medição, editar o item e na aba Rateio por Estado e Município, basta inserir as informações de Estado, Município e o percentual de rateio para cada Município. Podem ser feitos quantos rateios por Município forem necessários desde que o percentual feche em 100%.

Quando define-se os estados e municípios que serão filtrados na medição através do check "% informado na medição", que esta no Anexo "Estados/Municípios do Contrato" da visão de cadastro de , o Totvs Obras e Projetos não listará os estados e municípios na edição da medição no grupo "Rateio Default". Os estados e municípios não estarão no grupo "Rateio Default", pois quando o check é marcado o percentual de rateio é zero, assim o usuário precisará informar qual será o percentual de rateio do estado e município na edição da medição.

**Passos:**

Para realizar o cadastro pelo anexo de contrato basta informar o estado, código do município, %de rateio e  habilitar a opção se será informado na medição.

Informações

Para Gerar integração com suprimentos/faturamento será considerado o estado/município informado no item da medição, não possuindo será utilizado o inserido no anexo Estado/municípios do contrato e se não existir estado/município em nenhum destes locais, será utilizado o informado no projeto.
