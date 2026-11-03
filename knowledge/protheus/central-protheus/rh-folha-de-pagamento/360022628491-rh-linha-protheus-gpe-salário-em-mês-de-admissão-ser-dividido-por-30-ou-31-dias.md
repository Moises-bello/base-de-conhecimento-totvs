---
article_id: 360022628491
category: RH - Folha de Pagamento
content_hash: e59d7d2ba8554d4641edef346290906edda1fa5c74cf1a4e9a9d2f46d6b19cc2
fetched_at: '2026-06-28T22:44:16.305630+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Salário em mês de admissão ser dividido por 30
  ou 31 dias
type: support-article
updated_at: '2025-05-16T20:20:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022628491-RH-Linha-Protheus-GPE-Sal%C3%A1rio-em-m%C3%AAs-de-admiss%C3%A3o-ser-dividido-por-30-ou-31-dias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26357782139159)**Tempo aproximado para leitura:**00:01:00 min**

**Dúvida**É possível escolher o fator de divisão do salário no mês de admissão do funcionário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões   
  
**Solução**É possível escolher o fator de divisão do salário no mês de admissão do funcionário. Abaixo demonstrarei a configuração e cálculo escolhendo o fator de divisão pelos dias do mês ou 30 dias.

1. Cálculo de folha, considerando 31 dias (dias do mês) como fator de divisão do salário:

1.1 Cadastro do período:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019808592)
```

1.2 Cadastro do mnemônico P\_DIASADM:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019677631)
```

1.3 O cálculo do salário será correspondente a formula: (salario / 31) \* dias trabalhados

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019808632)
```

2. Cálculo de folha, considerando 30 dias (sempre 30) como fator de divisão do salário:

2.1 Cadastro de período:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019808672)
```

 2.2 Cadastro do mnemônico:

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019808872)
```

2.3 O cálculo do salário será correspondente a formula: (salario / 30) \* dias trabalhados (será considerado como dias trabalhados em meses de 31 dias, o dia 31, mesmo tratando-se de Mensalista)

```
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360019677811)
```

**Observação:**

A referência da verba de salário é de acordo com quantos dias o funcionário trabalhou dentro do período 01/01/2019 - 31/01/2019 e essa contagem independe dos dias de cálculo definido no cadastro de período e o conteúdo do mnemônico P\_DIASADM.   
Por esse motivo a escolha do fator de divisão nunca vai alterar a **referência** da verba de salário.   
  
Veja que são coisas diferentes:

Fator de divisão = Valor pago pelos dias trabalhados

Referência da verba de salário = Dias trabalhados dentro do mês de cálculo

**Saiba mais:**

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)
