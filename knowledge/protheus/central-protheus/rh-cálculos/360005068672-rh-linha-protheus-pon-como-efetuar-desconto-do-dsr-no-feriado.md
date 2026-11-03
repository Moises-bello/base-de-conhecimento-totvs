---
article_id: 360005068672
category: RH - Cálculos
content_hash: 9028ddf82b1ff1f839582a8f1cfa1f1c1fb4c47c314ce31aee5f636de94c2dab
fetched_at: '2026-06-28T22:44:51.625864+00:00'
product: protheus
section_id: 32419138773655
source: central-protheus
title: RH - Linha Protheus - PON - Como efetuar desconto do DSR no feriado
type: support-article
updated_at: '2026-02-10T19:08:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005068672-RH-Linha-Protheus-PON-Como-efetuar-desconto-do-DSR-no-feriado
---

##### **time.png Tempo aproximado para leitura: 00:01:00 min** **Dúvida** Como definir se o feriado será considerado para o desconto do DSR (Descanso Semanal Remunerado)? **Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões **Solução** As ausências de um trabalhador devem ser consideradas no cálculo do desconto de DSR - Descanso Semanal Remunerado.  Isso significa que um atraso poderá resultar em desconto dos dias de descanso, inclusive do feriado, quando houver. No entanto, existe entendimento de que o dia referente ao feriado não deverá sofrer o desconto.  Para atender a essa necessidade, implementou-se o parâmetro que possibilita determinar que o dia de feriado não será considerado no cálculo do desconto do DSR. Acessar o **modulo Configurador (SIGACFG)**na opção **Ambiente> Cadastros> Parâmetros** buscar pelo parâmetro **MV\_DDSRFER:**

##### Configurar conforme a necessidade da empresa: - Se o parâmetro for configurado com a informação **1** o sistema descontará tanto o DSR quanto o feriado. - Se o parâmetro for configurado com a informação **2** o sistema descontará apenas o DSR. Para demais parâmetros que são repensáveis por controlar o DSR [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018605091-RH-Linha-Protheus-PON-Par%C3%A2metros-que-controlam-o-DSR-no-m%C3%B3dulo-SIGAPON). **Saiba mais:** [Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373) [Pacote de Expedição Contínua Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus) [RH - Linha Protheus - PON - Descontar 2 DSR em semana de feriado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058920513-RH-Linha-Protheus-PON-Descontar-2-DSR-em-semana-de-feriado) [RH - Linha Protheus - PON - Parâmetros que controlam o DSR no módulo SIGAPON](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018605091-RH-Linha-Protheus-PON-Par%C3%A2metros-que-controlam-o-DSR-no-m%C3%B3dulo-SIGAPON)
