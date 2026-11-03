---
article_id: 5911882833815
category: RH - Reajuste Salarial
content_hash: 620be3a7ae9c75ccac68cd5af1bdd684fa123b720812c0e9c622da8d85a47265
fetched_at: '2026-06-28T22:43:15.913698+00:00'
product: protheus
section_id: 360010855214
source: central-protheus
title: RH - Linha Protheus - GPE  - Como realizar o reajuste salarial parcelado
type: support-article
updated_at: '2025-09-12T20:01:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5911882833815-RH-Linha-Protheus-GPE-Como-realizar-o-reajuste-salarial-parcelado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31720259305495) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar o reajuste salarial parcelado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões.

**Solução**Para realizar o reajuste de forma parcelada, **acesse a rotina GPER200** em Miscelânea / Reajuste / Salarial.

Para as perguntas:

**Aumento sobre:** Informe **Dissídio**

**Atualiza cadastro: Sim** (o sistema irá atualizar o campo salário "RA\_SALARIO")

**Atual. Base Dissídio: Não** (o sistema não irá atualizar o campo salário dissídio "RA\_ANTEAUM")

Quando realizar o segundo ou último reajuste a pergunta Atual. Base Dissídio ficará com Sim.

O sistema irá atualizar o campo salário e salário dissídio, se o valor do campo salário for menor que do campo salário dissídio o sistema irá deixar igual o campo salário dissídio.

Exemplificando:

O sindicato determinou um reajuste de 10,80% deverá ocorrer em duas parcelas, primeiro 7% e o segundo 3,80%.

No cadastro de funcionários tabela SRA temos:

campo Salário "RA\_SALARIO" R$1.000,00 e o campo Salário Dissídio "RA\_ANTEAUM" R$1.000,00.

**1ª reajuste - folha de maio**

Acesse a **rotina GPER200** em Miscelânea / Reajuste / Salarial.

**Aumento sobre:** deverá informar **Dissídio**

**Atualiza cadastro: Sim**

**Atual. Base Dissídio: Não**

**% Aumento: 7%**

O salário será reajustado para R$1.070,00 e o salário dissídio não sofrerá ajuste, permanecerá com o valor de R$1.000,00:

**2º Reajuste - folha de junho**

Novo reajuste 3,80%

**Atenção:** O novo reajuste (em junho) de 10,8% (deverá ser colocado o percentual TOTAL pois o reajuste será sobre o valor do **salário dissídio na SRA**, desta forma a diferença será calculada corretamente.

Desta vez (caso seja a última “parcela”), a **base de dissídio deve ser atualizada**:

**Aumento sobre:** deverá informar **Dissídio**

**Atualiza cadastro: Sim**

**Atual. Base Dissídio: Sim**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5911810569239)

O salário e salário dissídio será reajustado para R$1.108,00

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5911830362903)

**Observação:** Caso deseje realizar primeiro **a emissão do relatório** **para conferencia,** as perguntas deverão ficar desta forma:

**Aumento sobre:** Dissídio

**Atualiza cadastro:** Não

**Atual. Base Dissídio:** Não

**Saiba Mais**

[RH - Linha Protheus - GPE - Como conferir o reajuste salarial antes de efetivá-lo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028751191-RH-Linha-Protheus-GPE-Como-conferir-o-reajuste-salarial-antes-de-efetiv%C3%A1-lo)

[Pagina Centralizadora Reajuste Salarial](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010855214-RH-Reajuste-Salarial)
