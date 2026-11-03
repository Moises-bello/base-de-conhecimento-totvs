---
article_id: 4411589885335
category: RH - Rescisão
content_hash: 8a73b0db3d33f1ae3fbcba937216fd691e7f95a0b7a3261c6568174ccef178ba
fetched_at: '2026-06-28T22:43:48.573819+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar a data de demissão na rescisão complementar
  usando o parâmetro MV_MDDTDEM
type: support-article
updated_at: '2025-05-05T20:50:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411589885335-RH-Linha-Protheus-GPE-Como-alterar-a-data-de-demiss%C3%A3o-na-rescis%C3%A3o-complementar-usando-o-par%C3%A2metro-MV-MDDTDEM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19110634254871) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como alterar a data de demissão na rescisão complementar usando o parâmetro MV\_MDDTDEM?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Solução**Com o parâmetro MV\_MDDTDEM = S, é possível alterar na rescisão complementar a data de desligamento da rescisão original nos casos de rescisão por acordo judicial onde o juiz determina que a data de demissão seja um período já fechado.  
  
Para isso, siga o passo a passo abaixo:

**1.** No **Configurador SIGACFG**, na rotina **Parâmetros**, pelo caminho **Ambiente > Cadastros > Parâmetros**, localize o parâmetro **MV\_MDDTDEM** e altere o conteúdo para **S**:

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411584540311)**

**2.** Na rotina de **Rescisão**, pelo caminho **Miscelânea > Cálculos > Rescisão (GPEM040)**, calcule a **rescisão** **original** com data de demissão dentro do período em aberto da folha.  
No exemplo abaixo, o período em aberto é 10/2021, então a demissão é 24/10/2021:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411584390039)

**3.** Ainda na rotina de Rescisão, calcule a **rescisão complementar** normal, nesta complementar o sistema permitirá alterar a data de demissão.  
No exemplo abaixo, foi alterada a data de demissão para 24/07/2018:![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411584401303)

**OBSERVAÇÃO:** Na rescisão complementar os campos **Dt.Homologação** e **Data Geração** devem ser do período ativo atual.  
 **4.** Ao confirmar a complementar, no cadastro do funcionário a data de demissão será a informada na rescisão complementar: **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9035865443735)**

Para que seja possível calcular rescisão complementar editando a data de demissão é necessário que o funcionário  esteja ativo em folha folha de pagamento porém afastado sem vencimentos, caso a rescisão original esteja calculada em folha de pagamento fechada, não é possível nenhuma mudança em cabeçalho (SRG).

Caso a mudança na data demissão em rescisão complementar não atenda a necessidade, é necessário reabrir a folha dos períodos retroativos referente a data de demissão e calcular a rescisão.

**Saiba mais**  
[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)

[RH - Linha Protheus - GPE - Orientação sobre Reabertura de Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017683991-RH-Linha-Protheus-GPE-Orienta%C3%A7%C3%A3o-sobre-Reabertura-de-Folha-de-Pagamento?source=search)

[RH - Linha Protheus - GPE - Como calcular uma rescisão com valores zerados (Acordo Judicial) rescisão indireta](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017555492)
