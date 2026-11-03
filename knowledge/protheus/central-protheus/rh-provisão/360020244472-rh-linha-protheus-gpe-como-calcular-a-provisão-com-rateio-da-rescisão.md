---
article_id: 360020244472
category: RH - Provisão
content_hash: ca2ee90179bf4f90411ee6b657d98229a8c466a46a2c56c8527eac5c3c9e1894
fetched_at: '2026-06-28T22:43:55.706161+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular a provisão com rateio da rescisão
type: support-article
updated_at: '2025-10-24T11:58:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020244472-RH-Linha-Protheus-GPE-Como-calcular-a-provis%C3%A3o-com-rateio-da-rescis%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32998821591703)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida** **GPEM070** - Como calcular a provisão com rateio da rescisão?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.

**Solução**Manter o ambiente atualizado:  
- Acumulados: [Clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)- Lib: [MP- BD0054 - Procedimento para atualizar Lib no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007717731-MP-BD0054-Procedimento-para-atualizar-Lib-no-Protheus?source=search)- Binário: [PSIGABD0053 - Procedimento para atualizar o binário do Protheus](http://tdn.totvs.com/pages/viewpage.action?pageId=224123650)Para que o sistema efetue o rateio dos valores calculados na rescisão do empregado, deverá ser realizado o lançamento da programação do rateio, após, calcular a rescisão e depois efetuar o cálculo da provisão.  
  
Parâmetros: **SIGACFG- Ambiente/Cadastros/Parâmetros**  
**MV\_PROVRES**![](https://totvssuporte.zendesk.com/attachments/token/pCbOEYxVhh6koJqLOg47YPfYx/?name=inline-452832091.png)

**MV\_RATPROV**![](https://totvssuporte.zendesk.com/attachments/token/Mge12zztqIGvNYqMmCWahzpOp/?name=inline-342201011.png)

Verbas: **Atualizações/Cadastros/Verbas:**  
- Ter os identificadores de cálculo cadastrados conforme abaixo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/M3hwxQ0SpnKku3yBlwlI8QpSZ/?name=inline-679954977.png)

Ter as verbas configuradas conforme abaixo:  
SRV - **RV\_TIPOCOD** = 1 (provento), logo, o campo **RV\_ENCARCC** = B  
SRV - **RV\_TIPOCOD** = 2 (desconto), logo, o campo **RV\_ENCARCC** = S  
SRV - **RV\_TIPOCOD** = 3 e 4 (base provento, base desconto), logo, o campo **RV\_ENCARCC** = S  
  
Programação de Rateio: **Atualizações/Funcionários/Programação de Rateio**:

![](https://totvssuporte.zendesk.com/attachments/token/I0z7kahAXRNe2EpcOaAepTaHi/?name=inline745292560.png)

Rescisão: **Miscelânea/Cálculos/Rescisão:**

![](https://totvssuporte.zendesk.com/attachments/token/Rw0cvkLZ0IGNPyVXj0noVzKEg/?name=inline866681498.png)

Provisão: **Miscelânea/Provisões/Provisão Férias e décimo/Outra Ações/Provisão Rateada:**

![](https://totvssuporte.zendesk.com/attachments/token/O3ReedwukvovPEobx3UKWE39z/?name=inline1788638864.png)

**Saiba Mais:**

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)

[MP - GPE - Como conferir o cálculo da provisão de férias com baixa de férias?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006903791-MP-GPE-Como-conferir-o-c%C3%A1lculo-da-provis%C3%A3o-de-f%C3%A9rias-com-baixa-de-f%C3%A9rias-?source=search)
