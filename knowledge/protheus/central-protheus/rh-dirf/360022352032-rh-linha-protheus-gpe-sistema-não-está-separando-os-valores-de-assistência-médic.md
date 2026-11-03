---
article_id: 360022352032
category: RH – DIRF
content_hash: bfbf1da325bd74e0f1aa790807493869acc4e7ce56cc671efcb2172e3cc3720b
fetched_at: '2026-06-28T22:44:07.199991+00:00'
product: protheus
section_id: 360000030307
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não está separando os valores de assistência
  médica e reembolso no quadro 07
type: support-article
updated_at: '2025-09-05T10:29:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022352032-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-est%C3%A1-separando-os-valores-de-assist%C3%AAncia-m%C3%A9dica-e-reembolso-no-quadro-07
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26984284547351) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Sistema não está separando os valores de assistência médica e reembolso no informe de rendimento quadro 07, o que verificar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Deverá verificar a  rotina Coparticipação e reembolso tabela (RHP)  - o campo RHP\_TPLAN, se para a verba de reembolso estiver como 1 sistema irá somar. Para não somar o conteúdo deste campo tem que ser 2.  
  
Esta informação vem da tabela RHO - Co-participação e reembolso - RHO\_TPLAN: 1. Co-participação, 2.Reembolso. Para verificar a rotina e lançamento acesse **Atualizações > Benefícios > Plano de Saúde > Co-participação/Reembolso (GPEA003)**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26984313947159)

Ao gerar as informação para a tabela RCS - Informação complementar da dirf - sistema grava no campo Espec. Outros o código que irá diferenciar para o sistema realizar a separação, exemplo FMED01REEMBOLSO .

**Saiba Mais**

[RH - Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
