---
article_id: 360028451352
category: RH - Calculo Autonomo/Prolabore
content_hash: d80cc418302cb6c7414ffffa86f883cfc41177eca96871699ee90f826d83b2a2
fetched_at: '2026-06-28T22:43:15.103570+00:00'
product: protheus
section_id: 360011983113
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de Autônomo Freteiro de passageiro
type: support-article
updated_at: '2025-05-07T14:27:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028451352-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-Aut%C3%B4nomo-Freteiro-de-passageiro
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25081307844375)** Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**Cálculo de Autônomo Freteiro de passageiro.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12  
  
**Solução**Hoje para calcular a folha de autônomo Freteiro de passageiros com base do cálculo do encargos reduzida, é necessário realizar as seguintes configurações:

- A verba que será informada na tabela RGB é a com Id 0218, porém devido a exigências do e-social o valor da prestação de serviço será desmembrada em 3 outros Identificadores de Cálculo, que são:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029250531)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029250631)

- No **Cadastro do Autônomo** se atentar nas informações dos campos RA\_CATEG preenchido com 15, RA\_CATEFD preenchido com 711, RA\_CATFUNC preenchido com A;

- Determinar o **processo** que o **autônomo** será amarrado, onde se o pagamento da prestação de serviço for mensal o processo será o 00003 e o RA\_TIPOPGT = M, ou se o pagamento for semanal  o processo será o 00004 e o RA\_TIPOPGT = S;

- O campo **RA\_INSSAUT** (da aba estrangeiros) determinará se  será recolhido o INSS do autônomo.

- Para configurar o percentual de desconto do INSS do autônomo é através do **mnemônico** P\_PERCAUTO, onde na sua configuração deverá ter o conteúdo 0.11 caso seja 11% (exemplo);

- Para a **Base de IR** é utilizado o mnemônico P\_PERBCIR2 onde na sua configuração deverá ter o conteúdo 0.60 caso seja 60% (exemplo);

- Se houver pagamento de **autônomo de Carga** na mesma folha, deverá configurar também o mnemônico P\_TRANSPAP, pois nele deverá amarrar a verba com Id 0218, desta forma o sistema não se perderá no percentual que refere-se ao transportador de passageiros com os de cargas;

Exemplo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029252551)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029252731)

Cadastro de autônomo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029251452)

Lançamentos > Por funcionários

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029253632)

Cálculo da folha

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360029256371)

**Saiba Mais**

[RH - Calculo Autonomo/Prolabore](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011983113-RH-Calculo-Autonomo-Prolabore)
