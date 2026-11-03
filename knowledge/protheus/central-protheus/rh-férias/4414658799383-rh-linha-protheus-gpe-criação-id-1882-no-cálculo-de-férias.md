---
article_id: 4414658799383
category: RH - Férias
content_hash: c23dfa40fa6cbdbcfc73d1aceb5c37eccea385e2f1dbb7bb96b87c1603ecf4f7
fetched_at: '2026-06-28T22:43:58.229942+00:00'
product: protheus
section_id: 360001597291
source: central-protheus
title: RH - Linha Protheus - GPE - Criação ID 1882 no Cálculo de Férias
type: support-article
updated_at: '2025-09-12T16:51:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414658799383-RH-Linha-Protheus-GPE-Cria%C3%A7%C3%A3o-ID-1882-no-C%C3%A1lculo-de-F%C3%A9rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22009889148311) Tempo aproximado para leitura: 00:01:00 min**

**Dúvida**Criação ID 1882 no Cálculo de Férias - Base Desconto de Fgts 13º.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Criado ID de cálculo **1882**, para que seja gerado **a contra partida no Cálculo de Férias** quando há **adiantamento da 1ª parcela do 13º salário** nas Férias.  
  
O cálculo das verbas deve ser incluído no roteiro de **Férias**, porém, elas **não devem transitar pela Folha de Pagamento.**  
  
Deverá ser criada uma verba relacionada ao **ID 1882** conforme modelo:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Id Verba** | **Tipo da Verba** | **Natureza** | **Cd. Inc. CP** | **Cd. Inc. FGTS** | **Cd. Inc. IRRF** | **Incidências Folha** |
| 1882 | Base (Desconto) | 9989 | 00 | 12 | Sem tributação | Não |

**OBS:** essa verba **não será integrada para a Folha de Pagamento.**

**- Exemplo de cálculo:  
>** Verba 182 - ID 1882:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22009814221975)

**>** Verba 350 - ID 0022:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22009792986775)

**Saiba Mais**[Boletim Técnico](https://tdn.totvs.com/display/PROT/14477238+DRHCALCPRT-4940+DT+Ajuste+nas+Bases+INSS+Ferias+e+FGTS+no+leiaute+S-1.0+do+eSocial)  
[RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS, FGTS e IR ficam incorretos no eSocial (DCTFWEB) quando existe Férias no mês](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-FGTS-e-IR-ficam-incorretos-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs)
