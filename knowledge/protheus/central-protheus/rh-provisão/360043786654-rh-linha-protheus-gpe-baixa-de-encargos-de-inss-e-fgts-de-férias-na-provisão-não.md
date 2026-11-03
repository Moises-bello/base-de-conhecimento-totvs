---
article_id: 360043786654
category: RH - Provisão
content_hash: 8e6478af1d44a72a5828c0d943f84ba5f28f2798bea5c3d07839bc3cfecd96cb
fetched_at: '2026-06-28T22:43:55.629617+00:00'
product: protheus
section_id: 360001597311
source: central-protheus
title: RH - Linha Protheus - GPE - Baixa de Encargos de INSS e FGTS de Férias na Provisão
  não é realizada no mês de Desligamento
type: support-article
updated_at: '2025-11-03T12:01:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043786654-RH-Linha-Protheus-GPE-Baixa-de-Encargos-de-INSS-e-FGTS-de-F%C3%A9rias-na-Provis%C3%A3o-n%C3%A3o-%C3%A9-realizada-no-m%C3%AAs-de-Desligamento
---

**![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26279597273239) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Por que os cálculos de Provisão de Férias dos Funcionários que tiveram rescisão com pagamento de férias indenizadas, o sistema não apresenta a baixa dos encargos de INSS e FGTS?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Por padrão, quando o Parâmetro MV\_PROVRES está preenchido com S, o sistema calcula as provisões do mês de desligamento do funcionário, e as Baixas são realizadas conforme os pagamentos da Rescisão.  
Considerando que os pagamento de Férias Indenizadas (Vencidas ou Proporcionais) tem caráter indenizatório e não tem incidência para INSS e FGTS, o sistema não realiza a Baixa destes encargos.

Dessa forma, o sistema apresenta na linha "No Mês" no relatório de provisão, os valores provisionados até o mês anterior em negativo, para que o Saldo Atual seja zerado, como no exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059017194)

Já quando o parâmetro MV\_PROVRES está preenchido com N, o sistema não calcula as provisões do mês de desligamento do funcionário, e as Baixas são realizadas com os valores provisionados até o mês anterior, inclusive as Baixas de INSS e FGTS, como no exemplo abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000003901)

**Saiba Mais:**

[MV\_PROVRES](https://tdn.totvs.com/pages/releaseview.action?pageId=268587066)

[RH - Provisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597311-RH-Provis%C3%A3o)
