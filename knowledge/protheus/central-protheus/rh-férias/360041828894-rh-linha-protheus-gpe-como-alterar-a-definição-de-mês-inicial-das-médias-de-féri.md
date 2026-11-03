---
article_id: 360041828894
category: RH - Férias
content_hash: 3c178feeeb393a24c456130b5d9dc7f669bda6381643c9969dabb0f846be68dd
fetched_at: '2026-06-28T22:43:58.024178+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Como Alterar a Definição de Mês Inicial das Médias
  de Férias
type: support-article
updated_at: '2025-07-28T17:23:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041828894-RH-Linha-Protheus-GPE-Como-Alterar-a-Defini%C3%A7%C3%A3o-de-M%C3%AAs-Inicial-das-M%C3%A9dias-de-F%C3%A9rias
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16747237080599) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como Alterar a Definição de Mês Inicial das Médias de Férias?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Foi criado o Parâmetro **MV\_BUSMEDI**, que permite que o usuário defina qual será o mês de início das médias de Férias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/16747141525399)

O Parâmetro poderá ser configurado conforme as opções abaixo:

"1" - Buscará a partir do mês inicial do período aquisitivo, sem checagem de dias;  
"2" - Buscará a partir do mês seguinte ao inicio do período aquisitivo;  
"3" - Se no mês Inicial houver mais de 14 dias trabalhados utiliza o mês inicial, caso contrário utilizará a partir do mês seguinte.

Para alterar o conteúdo do Parâmetro, siga os passos abaixo:  
1. Acesse o **Configurador > Ambiente > Cadastros > Parâmetros**;  
2. Localize o Parâmetro**MV\_BUSMEDI** e clique no ícone **"Alterar"**;  
3. Altere o conteúdo do parâmetro no campo **"Cont. Por."** e Clique em **"Salvar"**.

À Partir do Release 12.1.25, os parâmetros referentes à médias poderão ser convertidos em mnemônicos. Caso realize a conversão, a configuração deverá ser diretamente no mnemônico **P\_BUSMEDI**, e o parâmetro será inutilizado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/16747180881943)

**Saiba Mais:**

[RH - Linha Protheus - GPE - Cálculo de médias 13º sobre aviso e médias férias sobre aviso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026383053-MP-GPE-C%C3%A1lculo-de-m%C3%A9dias-13%C2%BA-sobre-aviso-e-m%C3%A9dias-f%C3%A9rias-sobre-aviso?source=search)

[RH - Linha Protheus - GPE - Como é calculado férias e média férias em rescisão de comissionado puro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053106014-RH-Linha-Protheus-GPE-Como-%C3%A9-calculado-f%C3%A9rias-e-m%C3%A9dia-f%C3%A9rias-em-rescis%C3%A3o-de-comissionado-puro?source=search)

[RH - Linha Protheus - GPE - Como conferir média de férias dentro do cálculo de dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054370694-RH-Linha-Protheus-GPE-Como-conferir-m%C3%A9dia-de-f%C3%A9rias-dentro-do-c%C3%A1lculo-de-diss%C3%ADdio?source=search)

[RH - Linha Protheus - GPE - O que analisar quando o Relatório de Médias de Férias apresenta valor diferente do Cálculo das Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041858674-RH-Linha-Protheus-GPE-O-que-analisar-quando-o-Relat%C3%B3rio-de-M%C3%A9dias-de-F%C3%A9rias-apresenta-valor-diferente-do-C%C3%A1lculo-das-F%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-m%C3%A9dias-para-f%C3%A9rias?source=search)

[RH - Linha Protheus - GPE - Utilizando parâmetro MV\_DTMDFER = 1, Sistema não calcula as médias baseando-se na data base, conforme fazia na versão 11](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017515832-RH-Linha-Protheus-GPE-Utilizando-par%C3%A2metro-MV-DTMDFER-1-Sistema-n%C3%A3o-calcula-as-m%C3%A9dias-baseando-se-na-data-base-conforme-fazia-na-vers%C3%A3o-11?source=search)

[RH - Linha Protheus - GPE - Como calcular o DSR sobre médias no cálculo das férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418618747799-RH-Linha-Protheus-GPE-Como-calcular-o-DSR-sobre-m%C3%A9dias-no-c%C3%A1lculo-das-f%C3%A9rias?source=search)
