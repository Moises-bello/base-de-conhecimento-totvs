---
article_id: 9782099436311
category: RH - Benefícios
content_hash: d547b2645b10046c5467c1ba877c012762e421a0e941653afd561450b088c079
fetched_at: '2026-06-28T22:44:03.479719+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - Ao realizar a Integração do roteiro VAL com a folha
  gera o valor de desconto integral para o funcionário
type: support-article
updated_at: '2025-08-28T17:05:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9782099436311-RH-Linha-Protheus-GPE-Ao-realizar-a-Integra%C3%A7%C3%A3o-do-roteiro-VAL-com-a-folha-gera-o-valor-de-desconto-integral-para-o-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29537701185303) Tempo aproximado para leitura: **00:01:30min****Ocorrência**Ao realizar o cálculo do Vale Alimentação o valor desconto funcionário está correto porém ao integrar a folha, gera o desconto do beneficio integral para o funcionário.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9781520830231)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois a configuração do Mnemônico **P\_PDVAVAL** está com a verba de desconto funcionário. Dessa forma com a integração é gerado o desconto total do beneficio para o funcionário.   
  
**Solução**Para solucionar o incidente, realize os passos abaixo:

1. Altere a configuração do Mnemônico **P\_PDVAVAL** que estava com a verba parte funcionário em **Atualizações > Definições de Cálculo > Mnemônicos (GPEA300),** deixando o seu conteúdo padrão GETVALTYPE("C") ou informe uma verba de base que corresponderá ao **valor total do benefício,** conforme [MOS do eSocial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14597581804823-RH-Linha-Protheus-GPE-Valor-total-do-benef%C3%ADcio-de-vale-alimenta%C3%A7%C3%A3o-conforme-determina%C3%A7%C3%A3o-do-MOS-da-vers%C3%A3o-S-1-0)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9781623740951)

2. Após os ajustes cancele a integração com a folha em **Miscelânea > Cálculos > Integrações (GPEM019)**;  
  
3. Calcule o beneficio em **Atualizações > Benefícios > VT/VR/VA > Cálculos**;  
  
4. Realize a integração em **Atualizações > benefícios > VT/VR/VA > Integração com a Folha (GPEM015)**.

O cálculo será gerado normalmente e a integração com a folha irá com o valor de desconto corretamente para o funcionário.

**Importante:** Para o cálculo do Vale Alimentação é necessário realizar somente a configuração do Mnemônico **P\_PDVAEMP com a verba parte empresa** e o Mnemônico **P\_PDVADES com a verba parte funcionário.**

**Saiba Mais**[RH - Linha Protheus - GPE - Cadastro e Cálculo do Vale Alimentação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028910152)  
[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)
