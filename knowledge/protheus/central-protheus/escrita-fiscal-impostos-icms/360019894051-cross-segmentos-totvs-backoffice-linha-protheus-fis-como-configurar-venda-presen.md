---
article_id: 360019894051
category: Escrita Fiscal - Impostos - ICMS
content_hash: 3ec0c4eae971c74dd851c704c1ffa1656b99cb8a4c4efceeb2d8f38a27dc06b8
fetched_at: '2026-06-28T22:39:24.178779+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como Configurar
  Venda Presencial Para Consumidor Final? '
type: support-article
updated_at: '2026-01-29T16:11:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019894051-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-Configurar-Venda-Presencial-Para-Consumidor-Final
---

**Dúvida**

MP - FIS - Como configurar venda presencial para consumidor final?

**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Solução**Para que seja utilizada a alíquota Interna e o CFOP tenha seu inicio alterado para 5, em Vendas Presenciais de mercadorias destinada a Consumidor Final , sediado em outro Estado ou País  é necessário realizar as seguintes configurações:

O campo Tipo Frete (C5\_TPFRETE) deve ser igual a S - Sem Frete / F-Fob/ T- Por conta de Terceiros ou D- Por conta do destinatário

O campo Venda Presencial (F4\_VENPRES) deve estar igual a 1 - SIM

A Nota Fiscal deve ser de Saída .

O campo Tipo (A1\_TIPO) deve ser igual a F - Consumidor Final

Caso alguma das condições acima não seja atendida, não será realizada a alteração da alíquota e nem do CFOP.

Caso seja cadastrada uma Nota de Saída pelo módulo de Livros Fiscais(SIGAFIS) a regra não será aplicada
