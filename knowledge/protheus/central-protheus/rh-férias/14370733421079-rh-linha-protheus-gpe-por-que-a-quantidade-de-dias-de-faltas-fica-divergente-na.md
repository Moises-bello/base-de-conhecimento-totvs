---
article_id: 14370733421079
category: RH - Férias
content_hash: b9b726676ad0bfd5d0645cb381a879ea6ec3fe3d80804a6bb7a1d233d874d5c9
fetched_at: '2026-06-28T22:43:59.130712+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Por que a quantidade de dias de faltas fica divergente
  na rotina controle dias de direito e no relatório de demonstrativos de médias, quando
  são lançadas em Horas
type: support-article
updated_at: '2025-09-04T18:03:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14370733421079-RH-Linha-Protheus-GPE-Por-que-a-quantidade-de-dias-de-faltas-fica-divergente-na-rotina-controle-dias-de-direito-e-no-relat%C3%B3rio-de-demonstrativos-de-m%C3%A9dias-quando-s%C3%A3o-lan%C3%A7adas-em-Horas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31969657751319) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Por que a quantidade de dias de faltas fica divergente na rotina controle dias de direito e no relatório de demonstrativos de médias, quando são lançadas em Horas?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - Todas as versões  
  
**Solução**

Para faltas geradas em horas o sistema executa o seguinte cálculo, antes de gravá-las na rotina Controle dias de direito (SRF):

**Horas de faltas / ( Horas mês / 30).**

E desse resultado utiliza apenas a parte inteira do cálculo para gravação no controle de dias de direito SRF, e no Relatório de Demonstrativo de Médias o sistema utiliza o resultado com os decimais.

**Exemplo:**

Foram lançadas 72 horas de faltas para um funcionário que tem uma jornada mensal de 220 horas, o sistema irá realizar o seguinte cálculo:

**72/(220/30) = /7,3333 = 9,81862812**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368488674839)  
  
Na rotina controle dias de direito o sistema irá gravar somente a parte inteira das faltas, nesse caso 9 dias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368582615447)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368623412119)

No demonstrativo de médias o sistema irá apresentar o número real de faltas com os decimais 9,80

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368746809751)  
  
Para que o sistema apresente no controle dias de direito o mesmo resultado que no demonstrativo de médias, foi criado o mnemônico **P\_DECFALT**, cujo conteúdo no padrão é **.F.**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368145801239)  
  
Para que seja possível a gravação dos decimais na rotina Controle dias de direito (SRF) será necessário ativar o mnemônico **P\_DECFALT, alterando** o conteúdo para **.T.**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14368149463063)  
  
Após a ativação do mnemônico as faltas serão apresentadas igualmente na rotina controle dias de direito e no Relatório de Demonstrativos de médias, conforme exemplo abaixo:

**Exemplo:**

Foram lançadas 72 horas de faltas para um funcionário que tem uma jornada mensal de 220 horas, o sistema irá realizar o seguinte cálculo:

**72/(220/30) = /7,3333 = 9,81862812**

Na rotina controle dias de direito o sistema irá gravar somente a parte inteira das faltas, nesse caso 9,8 dias.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14370424464663)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14370467218199)  
  
No demonstrativo de médias o sistema irá apresentar o número real de faltas com os decimais 9,80

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14370526769943)

**Saber Mais:**

[RH - Linha Protheus - GPE - Como gerar o demonstrativo de médias para férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7726351592855-RH-Linha-Protheus-GPE-Como-gerar-o-demonstrativo-de-m%C3%A9dias-para-f%C3%A9rias?source=search)  
[RH - Linha Protheus - GPE - Coluna Valor Original e Valor Atual Demonstrativo de Médias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024606114-RH-Linha-Protheus-GPE-Coluna-Valor-Original-e-Valor-Atual-Demonstrativo-de-M%C3%A9dias?source=search)  
[RH - Linha Protheus - GPE - Pontos de entrada da rotina Controle dias de Direito - GPEA050](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412681997335-RH-Linha-Protheus-GPE-Pontos-de-entrada-da-rotina-Controle-dias-de-Direito-GPEA050?source=search)  
[RH - Linha Protheus - GPE - Como Funciona a Rotina Controle de Dias de Direito](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015671131-RH-Linha-Protheus-GPE-Como-Funciona-a-Rotina-Controle-de-Dias-de-Direito?source=search)
