---
article_id: 360050394474
category: RH - FGTS / SEFIP
content_hash: 35788d997df05e0785ec785d633a02f19ff925fdc7c80e3bdee1824121015f00
fetched_at: '2026-06-28T22:43:41.480125+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Recolhimento e cálculo do FGTS em caso de dispensa
  sem justa causa, quando há prorrogação da data de vencimento
type: support-article
updated_at: '2025-08-19T12:18:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050394474-RH-Linha-Protheus-GPE-Recolhimento-e-c%C3%A1lculo-do-FGTS-em-caso-de-dispensa-sem-justa-causa-quando-h%C3%A1-prorroga%C3%A7%C3%A3o-da-data-de-vencimento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34187239560855) Tempo aproximado para leitura: 00:01:30 min****Dúvida**Recolhimento e cálculo do FGTS em caso de dispensa sem justa causa, quando há prorrogação da data de vencimento.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**

A Medida Provisória n° 927/2020 possibilitou ao empregador a suspensão e o parcelamento, sem multa e encargos, do recolhimento de FGTS referente às competências de março, abril e maio de 2020.

Essas competências poderão ser recolhidas ao FGTS parceladamente entre julho e dezembro de 2020, sem impacto na regularidade dos empregadores junto ao FGTS (CRF). Esse processo será efetuado 100% online que posteriormente a Caixa Econômica Federal (CEF) informará o passo a passo a ser realizado.

Para o caso de desligamento do colaborador, a CEF disponibilizou através da Conectividade Social um comunicado informando a disponibilidade da tabela de Índices de FGTS em atraso com vigência 10/04/2020 a 09/05/2020.

Essa tabela foi ajustada para permitir o cálculo do FGTS referente ás competências de março e abril de 2020 sem a incidência de juros e multa.

Neste comunicado, a CEF veta a utilização da GRRF para a geração dos cálculos do FGTS referentes ao mês anterior à rescisão e o mês atual, quando estes compreenderem as competências de março, abril e maio de 2020.

Essa geração deverá ocorrer por meio do programa Conectividade Social ou através do SEFIP, conforme desejado pelo empregador.

No caso de geração pelo SEFIP. como já houve o envio da competência de março de 2020, será necessário restaurar o backup e alterar a modalidade dos funcionários desligados para os quais é necessário recolher o FGTS. Para esta situação, a modalidade de recolhimento será em branco (Recolhimento FGTS e Declaração para Previdência).

Para os demais funcionários, considerar a modalidade  9 (Confirmação de informações anteriores - Recolhimento FGTS e Declaração para Previdência/Declaração para FGTS e Previdência).

Nos casos dos funcionários que solicitaram demissão, o processo para recolhimento do FGTS será junto com os demais, através do parcelamento, já que esse não terá direito ao saque do FGTS.

Atenção quando ocorrer o envio do parcelamento: os desligados precisam ser informados na modalidade 9 (Confirmação de informações anteriores - Recolhimento FGTS e Declaração para Previdência/Declaração para FGTS e Previdência) para não ocorrer o recolhimento em duplicidade e nem serem pagadas as informações já declaradas.

Por se tratar de uma nova medida que ainda não ter um respaldo abrangente, orientamos sempre a adotar a regra mais benéfica ao trabalhador.

**Como fazer o parcelamento**

Os empregadores ou empregadores domésticos que efetivarem a suspensão do recolhimento das competências de março, abril e maio de 2020, terão o valor declarado via SEFIP ou DAE, desde que dentro do prazo previsto na MP 927/20, automaticamente parcelado para pagamento entre julho e dezembro de 2020.

A CEF divulgará oportunamente as orientações para quitação das parcelas.

**Rescisão de Contrato de Trabalho**

Caso ocorra a rescisão do contrato de trabalho, o empregador está obrigado ao recolhimento das verbas rescisórias, se devidas, e o valor total das competências suspensas no prazo de 10 dias após a rescisão, via SEFIP.

Se a rescisão ocorrer durante o pagamento do parcelamento das competências suspensas, as parcelas vincendas devem ser antecipadas e pagas no mesmo prazo de pagamento da rescisão.

Caso algum desses valores não seja pago no referido prazo, sobre eles incidirão multa e juros conforme a Lei nº 8.036/90.

Para maiores informações, [acesse aqui o site da CEF](http://www.caixa.gov.br/beneficios-trabalhador/fgts/suspensao-recolhimento-fgts/Paginas/default.aspx).

Aviso

A CEF não está aceitando o pagamento da GRRF com informações do mês anterior que se refere-se à competência suspensa, instruindo que o pagamento do FGTS da competência suspensa deve ser via SEFIP.

Contra partida não localizamos nenhuma informação de como proceder esse envio no site da CEF.

O procedimento, que já é de conhecimento dos usuários da conectividade social, trata-se da existência de apenas um único arquivo sefip.re por competência, ou seja, todos os funcionários que foram enviado com modalidade 1 - Declaratória para as competências suspensas, precisam continuar no arquivo e, para os funcionários desligados no período da suspensão do recolhimento, é necessário pegar o arquivo sefip.re do mês de Março (por exemplo) e alterar a modalidade para zero(0), e o FGTS da rescisão será pago via GRRF.  Para maiores informações orientamos entrar em contato com o suporte da CEF.

|  |  |
| --- | --- |
| TIPO | FINALIDADE |
| Branco | Recolhimento ao FGTS e Declaração à Previdência |
| 1 | Declaração ao FGTS e à Previdência |
| 9 | Confirmação Informações anteriores – Rec/Decl ao FGTS e Decl à Previdência |

Guia passo a passo

1. Opção: Gerar novamente a SEFIP dos meses em questão e fazer o recolhimento dos valores acumulados
2. Opção: Restaurar o backup dos meses anteriores

Gerar o arquivo da SEFIP normalmente de forma retroativa, como declaratória, e no validador mover o trabalhador para o recolhimento ao FGTS e Previdência

Selecione o funcionário que esta na aba de DECLARAÇÃO AO FGTS:

**![](https://tdn.totvs.com/download/attachments/546691786/image2020-4-24_15-49-13.png?version=1&modificationDate=1587754707763&api=v2)**

Realize a movimentação dele até a parte de RECOLHIMENTO:

![](https://tdn.totvs.com/download/attachments/546691786/image2020-4-24_15-52-1.png?version=1&modificationDate=1587754707617&api=v2)

Caso necessário, após mover o trabalhador faça a manutenção dos valores, pois o validador da SEFIP não sofreu nenhuma alteração para aceitar a movimentação e pagamento de FGTS em casos de demissão sem justa causa.

**Saiba mais:**

[RH - FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
