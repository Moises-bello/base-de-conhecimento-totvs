---
article_id: 360016084231
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: d8dde8dfca1d659abb14e3b2a25daa494760c797c6043cc105fdfaddafaf3e00
fetched_at: '2026-06-28T22:37:20.246028+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT  - Como informar um Desconto
  na Medição de Contratos?
type: support-article
updated_at: '2025-12-16T13:53:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016084231-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-informar-um-Desconto-na-Medi%C3%A7%C3%A3o-de-Contratos
---

**Dúvida**

Como Configurar Tipos de Descontos na Medição ?

**Ambiente**

Microsiga Protheus – Gestão de contratos – A partir da versão 12

**Solução**

No módulo Gestão de Contratos, pode-se informar um desconto na medição através da Aba "Descontos" da rotina de Medições.

Na versão 12 acesse a rotina de Medições CNTA121 na aba Descontos conforme imagem abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5095077640599)

Preencha o campo "Tipo de Desconto" da Aba "Descontos" e o "Valor" do desconto que poderá ser visualizado posteriormente na Aba "Totais" da Medição:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9702043386391)

O Tipo de Desconto pode ser cadastrado na rotina de Tipos de Descontos informando um  Código, uma Descrição e Interf. Ped (Sim/Não).

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9701536492695)

***Atenção:*** O campo "Interf. Ped." do Cadastro de Tipo de Desconto, definirá se o valor informado na medição irá refletir ou não no valor do pedido.

Caso configure este campo como "Não", o desconto será apenas informativo, não alterando o valor do pedido gerado.

***Obs1:***

Os descontos informados na medição são levados para o título através dos campos E1\_MDDESC/E2\_MDDESC e são abatidos do valor total do título somente no momento de baixa.

***Obs2:***

Foi implementado o parâmetro “**MV\_CNRATE**”, que permite configurar o tipo de rateio aplicado aos itens do pedido.

O parâmetro “**MV\_CNRATE**” pode ser configurado com:

1 - Para ratear os valores e subtrair do valor unitário dos itens proporcionalmente na geração do pedido de compra ou venda.

2 – Para ratear os valores e somar no valor de desconto dos itens proporcionalmente na geração do pedido de compra ou venda.

***Obs3:***

É possível conceder desconto em apenas um dos pedidos gerados na mesma medição?

**R:** Ao gerar dois pedidos ou mais no encerramento da mesma medição no exemplo de ser medida mais de uma planilha na mesma medição, o desconto informado na Aba de desconto da medição será refletido em todos os pedidos, atualmente não possui uma forma de aplicar desconto apenas para um dos pedidos gerado na medição pra mais planilhas.

Uma possibilidade/alternativa é se gerar medições separadas pra cada planilha, concedendo o desconto apenas para uma das planilhas e pedido gerado conforme o desejado.

***Saiba Mais:***

* [GCT0034\_Como\_configurar\_o\_tipo\_de\_desconto\_na\_medição?](https://tdn.totvs.com/pages/releaseview.action?pageId=239037294)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ao realizar o desconto na medição os campos de % de Desconto do Contrato (CNE\_PDESC) e Valor de desconto do Contrato (CNE\_VLDESC) ficam bloqueados para preenchimento em contratos Fixo e Semi-Fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025465372-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ao-realizar-o-desconto-na-medi%C3%A7%C3%A3o-os-campos-de-de-Desconto-do-Contrato-CNE-PDESC-e-Valor-de-desconto-do-Contrato-CNE-VLDESC-ficam-bloqueados-para-preenchimento-em-contratos-Fixo-e-Semi-Fixo?source=search)
* [DT Inconsistência no processo de desconto da medição](https://tdn.totvs.com/pages/releaseview.action?pageId=729236468)
* [GCT0117 - Processo de desconto](http://tdn.totvs.com/display/PROT/GCT0117+-+Processo+de+desconto)
* [MP - SIGAGCT - Como são considerados os descontos no financeiro em títulos gerados pelo encerramento da medição ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025642971-MP-SIGAGCT-Como-s%C3%A3o-considerados-os-descontos-no-financeiro-em-t%C3%ADtulos-gerados-pelo-encerramento-da-medi%C3%A7%C3%A3o)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Pontos de entrada para rotina de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Pontos-de-entrada-para-rotina-de-Medi%C3%A7%C3%A3o?source=search)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
