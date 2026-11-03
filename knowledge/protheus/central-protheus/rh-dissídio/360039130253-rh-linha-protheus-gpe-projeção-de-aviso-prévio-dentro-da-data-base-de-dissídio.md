---
article_id: 360039130253
category: RH - Dissídio
content_hash: 55817ce90f4425d8632e0df102e2d43ca37c33b8a632329a464dd22840a9c7eb
fetched_at: '2026-06-28T22:43:44.312813+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Projeção de aviso prévio dentro da data base de
  dissídio
type: support-article
updated_at: '2025-09-09T12:20:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039130253-RH-Linha-Protheus-GPE-Proje%C3%A7%C3%A3o-de-aviso-pr%C3%A9vio-dentro-da-data-base-de-diss%C3%ADdio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34804837121559) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Como realizar o pagamento da rescisão complementar por dissídio quando apenas a projeção de aviso prévio está dentro da data base de dissídio - competência em que o dissídio deveria ter saído.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**É necessário decidir quais verbas serão pagas dentro da rescisão complementar. Dentro do **cadastro de sindicato**, **aba rescisão** existe as seguintes opções:  Todas as verbas, somente aviso, aviso + verbas rescisórias  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050631954)  
  
Mais informações sobre o campo: <https://tdn.totvs.com/x/TCWWDg>  
  
Dentro desse exemplo, onde somente os dias de aviso prévio caíram dentro da data base de dissídio, dessa maneira é necessário que o campo Verbas Rescisão Comple. localizado dentro do cadastro de dissídio esteja com a opção **Somente aviso** e o mnemônico**P\_DISSPAVP** com o conteúdo igual a **.T.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008125988887)  
Após essa configuração é necessário realizar o cálculo do dissídio através da rotina GPEM690, onde será gerado para esse funcionário apenas a verba 000, que corresponde a atualização salarial.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008126009623)  
  
Após a geração do dissídio é necessário confirmar a atualização salarial dentro das rotinas: Cadastro do funcionário (GPEA010) e Histórico salarial (GPEA250).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008126022807)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008116813079)

Por fim a rescisão complementar deve ser calculada, gerando as diferenças apenas das verbas de aviso prévio.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008346738327)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23008320846103)

Cenário desta projeção:

**Data Admissão:** 04/02/2019  
**Data Demissão:** 21/11/2023  
**Aviso Projetado:** 42 dias  
**Configuração:** Aviso + verbas rescisórias

**Saiba Mais**  
[Pagina Centralizado Dissidio Retroativo](https://www.google.com/url?q=https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%25C3%25ADdio&sa=D&source=hangouts&ust=1572529678699000&usg=AFQjCNFW7PMX5N2Z4WRgKDwi8PLEi62E2g)
