---
article_id: 33860793254295
category: SIGAEST - SALDOS
content_hash: d32bf6d323b3702ba6b3c1639c6d8cd69a1087b130371154d71aaebeb26b0859
fetched_at: '2026-06-28T22:39:14.793685+00:00'
product: protheus
section_id: 1500001538801
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Qual a diferença entre
  os campos B2_QFIM/B2_QATU/B2_VATU1/B2_VFIM1 ?
type: support-article
updated_at: '2025-08-06T17:28:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33860793254295-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Qual-a-diferen%C3%A7a-entre-os-campos-B2-QFIM-B2-QATU-B2-VATU1-B2-VFIM1
---

O artigo aborda a diferença entre o saldo final (B2\_QFIM) e o saldo atual (B2\_QATU) no sistema de estoque da TOTVS Protheus. A divergência ocorre devido ao processamento do custo médio, que considera movimentações até uma data específica, enquanto o saldo atual reflete todas as movimentações até a data presente. No exemplo dado, uma entrada e duas saídas de estoque são consideradas, mostrando como o saldo final pode ser diferente do saldo atual. A igualdade entre ambos os saldos ocorre quando o cálculo do custo médio é feito até a data corrente sem movimentações posteriores. Isso também se aplica aos valores monetários, como B2\_VFIM1 e B2\_VATU1.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33860788443031) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Avaliando meus saldos, verifiquei que o valor contido no saldo/valor final(B2\_QFIM/B2\_VFIM1) do meu KARDEX difere do meu saldo atual(B2\_QATU/B2\_VATU1) em estoque, porque isso acontece?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Solução**  
Considerando um cenário hipotético, estamos no mês de **julho de 2025**, que possui **31 dias**. A data atual do **sistema operacional** está configurada como **31/07/2025**, entretanto, o ambiente de execução (**database**) em que o usuário está logado corresponde à data **30/07/2025**.

O analista de estoque, devidamente ciente do ciclo de fechamento, informa que o **último período fechado de estoque ocorreu em 30/06/2025**, o que implica que o **período aberto vigente** compreende o intervalo de **01/07/2025 até a data corrente (31/07/2025)**, incluindo quaisquer movimentações posteriores a essa data.

**Exemplo prático:**  
Suponha os seguintes lançamentos de movimentações no período como se fosse notas de entrada e saida:

* Entrada de estoque em **01/07/2025**: `+100 unidades`
* Saída de estoque em **15/07/2025**: `-50 unidades`
* Saída de estoque em **31/07/2025**: `-25 unidades`

### **Cálculo do saldo atual (B2\_QATU) mediante movimentações:**

```
100 (entrada) - 50 (saída) - 25 (saída) = 25 unidades
```

Ou seja, o valor presente no campo **B2\_QATU** refletirá o **saldo atual real do produto**, considerando todas as movimentações registradas até a data corrente **(inclusive 31/07/2025)**.

### **Cenário de processamento do custo médio:**

Caso seja executada a rotina de **cálculo de custo médio**, informando como **"Data Limite Final" o dia 30/07/2025**, o sistema desconsiderará as movimentações posteriores a essa data. Portanto, a movimentação de saída do dia **31/07/2025** não será considerada neste cálculo.

**Saldo final gravado (B2\_QFIM):**

```
100 (entrada) - 50 (saída) = 50 unidades
```

Neste caso, o campo **B2\_QFIM** será atualizado com o valor de **50 unidades**, pois este corresponde ao saldo final acumulado **até 30/07/2025**, conforme o intervalo de data definido no processamento da rotina de custo médio.

### **Conclusão:**

O campo **B2\_QFIM** (Saldo Final) representa o saldo apurado até a data informada ***(Suas movimentações, por exemplo SD1/SD2/SD3)*** no processamento do custo médio, enquanto o campo **B2\_QATU** (Saldo Atual) reflete a totalização das movimentações **realmente lançadas até o momento presente**, independentemente de fechamento ou cálculo de custo médio.

Portanto, **B2\_QFIM pode divergir de B2\_QATU**, e essa divergência é considerada **comportamento esperado e tecnicamente justificável pelo calculo dos periodos e existencia das movimentações.**

### **Quando ambos os saldos serão equivalentes?**

A igualdade entre os campos **B2\_QFIM** e **B2\_QATU** ocorrerá **somente quando o cálculo de custo médio for executado até a data corrente real (sem movimentações posteriores)**. Assim, o saldo final calculado refletirá exatamente o mesmo saldo atual existente, sem defasagens.

Esse mesmo princípio se aplica também aos campos de **valores monetários**, tais como:

* **B2\_VFIM1**: Valor Final
* **B2\_VATU1**: Valor Atual

O entendimento claro desses conceitos é fundamental para a correta análise de saldos e valores nos processos de controle de estoque e auditoria.

### **E como é que eu valido esses saldos no sistema?**

Basta voce configurar o relatorio de movimentações calculadas no periodo, o KARDEX POR PERIODO MATR900, conforme boletim, importante configurar exatamente conforme boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR900 - Como configurar corretamente o relatório Kardex para análise de Custos e Movimentações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011930291-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR900-Como-configurar-corretamente-o-relat%C3%B3rio-Kardex-para-an%C3%A1lise-de-Custos-e-Movimenta%C3%A7%C3%B5es)

### **Mas e como é que eu posso comparar oque gravou nos movimentos, com um relatorio que valida apenas o saldo final calculado dos movimentos?**

Basta voce configurar o relatorio de saldos analiticos MATR260, conforme boletim, importante configurar exatamente conforme boletim:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Importância da pergunta "Saldo do produto a considerar?" para correta emissão do relatório](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018559171-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Import%C3%A2ncia-da-pergunta-Saldo-do-produto-a-considerar-para-correta-emiss%C3%A3o-do-relat%C3%B3rio)

**Saiba mais:**  
[*Clique aqui e veja mais artigos sobre Cadastros e Configurações no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)
