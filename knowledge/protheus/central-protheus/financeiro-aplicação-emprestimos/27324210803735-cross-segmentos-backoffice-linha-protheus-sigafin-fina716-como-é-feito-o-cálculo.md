---
article_id: 27324210803735
category: Financeiro - Aplicação / Emprestimos
content_hash: 89d8caa3fdee2da703e23ce1e5cd71d88343005548550e62c14644be3825d6f8
fetched_at: '2026-06-28T22:37:59.539860+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA716 Como é feito
  o cálculo dos juros compostos em uma aplicação ou empréstimo?
type: support-article
updated_at: '2024-10-25T12:09:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27324210803735-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-feito-o-c%C3%A1lculo-dos-juros-compostos-em-uma-aplica%C3%A7%C3%A3o-ou-empr%C3%A9stimo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27324241754391) Tempo aproximado para leitura: **00:10:00 min****Dúvida**Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA716 Como é feito o cálculo dos juros compostos em uma aplicação ou empréstimo?  
  
**Ambiente**  
Exemplo:  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro - Todas as versões]  
  
**Solução**Esse exemplo é válido, quando os valores de uma aplicação ou empréstimo no protheus não batem com o extrato do banco.

O primeiro ponto a ser verificado se o rendimento desta operação foi calculada corretamente

Pois se esse valor do rendimento desta operação não esteja correto, os outros valores também não ficaram por consequência como:

 - Valor de IR

 - Valor de IOF

 - Saldo Final

Neste documentação iremos mostrar como é feito o cálculo dos juros compostos que é feito no protheus e também é feito no mercado.

Exemplo:

Tenho uma aplicação ou empréstimo que foi inclusa no dia

22/08/2024  
No valor de R$ 700.000,00

Com uma taxa de 10,40% anual

No dia 30/08/2024

Qual será o seu rendimento, após **8 dias** corridos?

Iremos aplicar a formula de mercado abaixo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27324210790295)

M = Montante ou valor final  
P = Capital Aplicado = **R$ 700.000,00**  
i = Taxa  = **10,40%**  
n = tempo, período ou prazo = **8 dias corridos**

**Passo 1)**

Mas primeiro temos que converter o variável "**i**" (Taxa) que está 10,40% **anual** para uma taxa **diária,** antes de aplicarmos a formula do juros compostos

Segue a formula de mercado para conversão do juros anual para diário

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27324241755671)

Segue a formula já convertida para excel

=(1+10,4%)^(1/**360**)-1

= **0,0274871%**

O conteúdo da formula "**360**", poderá ser alterado no parâmetro MV\_DIASCTB do protheus

**MV\_DIASCTB** = Indica a quantidade de dias do ano contábil, e essa informação irá afetar no cálculo do juros compostos.

A quantidade de dias, deve ser informada no seu contrato oficial, caso contrário a empresa deverá entrar em contato com a instituição responsável pela operação para obter a quantidade de dias.

**Passo 2)**

Aplicando a formula do Juros compostos

Segue a formula já convertida para excel

=700000\*(1+0,0274871%)^8

= R$ 701.540,76

Logo o seu rendimento será de:

= R$ 701.540,76 - 700.000,00

= **1.540,76**

E após encontrar o rendimento, será calculado em cima do rendimento taxa de IR e IOF e calculado o saldo final da sua operação.

Caso a formula passada não esteja batendo com o seu extrato oficial da sua instituição, a sugestão será que entre em contato com a sua instituição responsável pela operação, solicitando o mesmo cálculo que demostramos aqui, passo a passo para que seja compartilhado com o atendimento do suporte protheus

Saiba mais:

[Aplicações e empréstimos - FINA716 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=680254799)

[Aplicações - FINA716](https://tdn.totvs.com/pages/releaseview.action?pageId=684987286)

[FINA716 - Como é efetuado o calculo do juros nas parcelas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/13782176773527-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Como-%C3%A9-efetuado-o-calculo-do-juros-nas-parcelas)
