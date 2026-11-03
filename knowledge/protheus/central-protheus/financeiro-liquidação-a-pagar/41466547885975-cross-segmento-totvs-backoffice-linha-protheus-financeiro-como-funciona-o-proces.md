---
article_id: 41466547885975
category: 'Financeiro - Liquidação a Pagar '
content_hash: fc8cad0920114ae43ff4b3995ca47c07660c665b3c901284e9e5b5fae343f3ff
fetched_at: '2026-06-28T22:37:32.449348+00:00'
product: protheus
section_id: 35057594361879
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Como funciona
  o processo de baixa de títulos na liquidação em moeda estrangeira
type: support-article
updated_at: '2026-06-25T12:16:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/41466547885975-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Financeiro-Como-funciona-o-processo-de-baixa-de-t%C3%ADtulos-na-liquida%C3%A7%C3%A3o-em-moeda-estrangeira
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41466537620503) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Qual o conceito para a baixa dos títulos na liquidação em moeda estrangeira?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.

**Solução**  
A taxa informada na tela de liquidação é considerada exclusivamente para os títulos que serão gerados na liquidação. Dessa forma, a alteração ou definição da taxa nesse momento não impactará nos títulos que serão baixados em decorrência da liquidação.

Para os títulos baixados por meio desse processo, o sistema utilizará como referência a taxa definida para a moeda correspondente no cadastro de moedas ou, quando existente, a taxa contratada informada no momento da inclusão do título.

Sendo assim, a taxa informada na liquidação possui efeito apenas sobre os títulos que serão gerados na liquidação, que será criado com a taxa negociada na operação. Já a baixa dos títulos seguirá a cotação do dia registrada na tabela de moedas (SM2), utilizada para a apuração de eventual variação cambial, conforme a regra padrão do sistema.

**Exemplo de liquidação de título em moeda estrangeira.**

Foi incluído um título em **02/02** utilizando a **Moeda 2 (Dólar)**, com a seguinte cotação:

* Data de inclusão: 02/02
* Moeda: 2 (Dólar)
* Taxa de câmbio na inclusão (**SM2**): **5,0000**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478317667607)

Com taxa do dólar 5.0000

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478317667991)

Posteriormente, é realizada a liquidação do título em **17/03**. Na data da liquidação (17/03), a taxa cadastrada para a moeda no cadastro de moedas (**SM2**) é:

* Taxa cadastrada na SM2: **4,9000**

Entretanto, durante o processo de liquidação, foi informada manualmente a taxa:

* Taxa informada na liquidação: **4,5000**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478317669783)

O título gerado pela liquidação utilizará a **taxa informada no momento da liquidação**, ou seja, **4,5000**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478353414807)

Por outro lado, para o título baixado por meio da liquidação, o sistema considerará a **taxa vigente cadastrada na tabela SM2 na data da liquidação**, neste exemplo **4,9000**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41478317670551)

Como existe divergência entre a taxa utilizada na inclusão do título (**5,0000**) e a taxa considerada na baixa (**4,9000**), o sistema realizará automaticamente a apuração da **variação cambial gerando a correção monetária.**

**Saiba mais**

[Liquidação a Pagar - FINA565](https://tdn.totvs.com/pages/releaseview.action?pageId=312167645#tabs-passo4)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA565 - Pontos de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25141673054103-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA565-Pontos-de-Entrada)
