---
article_id: 360035975093
category: RH - Contrato Intermitente
content_hash: 1e74935308498d9f8653a6692d17e827a2189fbe6bfc28a0c941a3c6c0b19e7d
fetched_at: '2026-06-28T22:43:40.008760+00:00'
product: protheus
section_id: 360003139951
source: central-protheus
title: RH - Linha Protheus - GPE - Cálculo de DSR para funcionário intermitente considerando
  o mês completo
type: support-article
updated_at: '2025-04-15T12:46:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035975093-RH-Linha-Protheus-GPE-C%C3%A1lculo-de-DSR-para-funcion%C3%A1rio-intermitente-considerando-o-m%C3%AAs-completo
---

#### time.png Tempo aproximado para leitura: **00:01:30 min**

#### **Dúvida** Ao calcular folha de um funcionário que possui contrato intermitente, o sistema considera o mês completo para cálculo do DSR.

#### **Ambiente** TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17 **Solução**

#### Isso acontece porque o parâmetro **MV\_TPCALEND** está com **2-Sintético**. Sendo assim, ao cadastrar os períodos, o calendário do período é gerado de forma sintética, conforme abaixo, então **não** gerará o calendário dia a dia na aba **Cadastro de Calendário**. Desta forma, o sistema não tem onde buscar os dias de DSR, então calcula de acordo com o **total** de DSR do **cabeçalho** do período:

#### mceclip4.png Aba Cadastro do Calendário mceclip2.png **1.** Altere o parâmetro MV\_TPCALEND para 1-Analítico mceclip3.png **2.** Acesse a rotina de períodos em **Atualizações > Definições de Cálculos > Períodos** **(GPEA400)** clique em **Alterar** nos períodos em aberto e clique em **SIM** na mensagem abaixo (esse processo deve ser realizado para todos os períodos que ainda estão em aberto) mceclip5.png **3.** Na aba **Cadastro Calendário** será gerado o calendário analítico do mês, e o sistema terá de onde buscar o DSR correto de acordo com cada convocação mceclip6.png **Saiba Mais**

[RH - Contrato Intermitente](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003139951-RH-Contrato-Intermitente)
