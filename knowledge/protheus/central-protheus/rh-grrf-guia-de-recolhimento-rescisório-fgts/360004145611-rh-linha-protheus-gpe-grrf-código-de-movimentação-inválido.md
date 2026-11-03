---
article_id: 360004145611
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 45e286439553d8553cc3e7e7f8f33de0a410e474a263912c14cecd498dedc893
fetched_at: '2026-06-28T22:43:32.370012+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - GRRF Código de Movimentação inválido
type: support-article
updated_at: '2025-10-20T12:27:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004145611-RH-Linha-Protheus-GPE-GRRF-C%C3%B3digo-de-Movimenta%C3%A7%C3%A3o-inv%C3%A1lido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33069464594071) Tempo aproximado para leitura: **00.03:00 min**

**Dúvida**Ao importar a GRRF ocorre erro de Código de Movimentação inválido, como arrumar?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Versão 12.  
  
**Solução**Segue tabela demonstrando os códigos para cada tipo de rescisão:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Tipos de Rescisão** | **"Cod. Afast. FGTS"** | **Cód.Saque ou " Cod. AM."** | **GRRF ou GFIP** | **Seguro Desemprego** |
| Pedido de demissão de empregado Já aposentado | J | 5 | GRRF | N |
| Por dispensa com justa Causa | H | NÃO | GFIP | N |
| Por dispensa sem justa Causa | I1 | 1 | GRRF | S |
| Por dispensa sem justa Causa do empregado doméstico | I4 | (\*) | (\*) | (\*) |
| Rescisão Indireta | I1 | 1 | GRRF | S |
| Término de Contrato Por Período de Experiência | I3 | 4 | GRRF | N |
| Término de Contrato Por Prazo Determinado | I3 | 4 | GRRF | N |
| Rescisão Por Acordo (Reforma Trabalhista) | I5 | 7 | GRRF | N |
| Término de Contrato Por Prazo Determinado (Contrato Intermitente - Reforma Trabalhista) | R1 | 4\* | GRRF | N |
| Antecipação término de Contrato Por Período de Experiência (empregado) | J | NÃO | GFIP | N |
| Antecipação término de Contrato Por Período Experiência (empregador) | I1 | 1 | GRRF | S |
| Antecipação Término de Contrato Por Prazo Determinado (empregado) | J | NÃO | GFIP | N |
| Antecipação Término de Contrato Por Prazo Determinado (empregador) | I1 | 4 | GRRF | S |
| Antecipação Término de Contrato Por Prazo Determinado com justa causa (empregador) | H | NÃO | GFIP | N |
| Dispensa Por culpa reciproca OU Força Maior | I2 | 2 | GRRF | S |
| Extinção da Empresa | I1 | 3 | GRRF | S |
| Morte do empregado | S2\* | 23\* | GFIP | N |
| Pedido de demissão Antes de hum ano Completar | J | NÃO | GFIP | N |
| Pedido de demissão com Mais de hum ano | J | NÃO | GFIP | N |

Após alterar o código na tabela S043, a **rescisão deve ser recalculada** para que o sistema altere a informação no cadastro de Funcionário e também na GRRF. **Saiba mais**  
[RH - Linha Protheus - GPE - Ao validar a GRRF é gerado aviso "Código de Saque Inválido"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020437152-RH-Linha-Protheus-GPE-Ao-validar-a-GRRF-%C3%A9-gerado-aviso-C%C3%B3digo-de-Saque-Inv%C3%A1lido-)

[RH GRRF (Guia de Recolhimento Rescisório FGTS)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010781714-RH-GRRF-Guia-de-Recolhimento-Rescis%C3%B3rio-FGTS)
