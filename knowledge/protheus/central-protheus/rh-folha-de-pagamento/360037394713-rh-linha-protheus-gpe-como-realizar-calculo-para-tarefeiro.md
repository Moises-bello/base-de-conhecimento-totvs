---
article_id: 360037394713
category: RH - Folha de Pagamento
content_hash: 52ed20708de3b809aa17fcb93a2ae5416f8fdf84fc3ad6574bc93aca997cf3c4
fetched_at: '2026-06-28T22:44:14.743164+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar calculo para Tarefeiro
type: support-article
updated_at: '2025-04-16T11:40:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037394713-RH-Linha-Protheus-GPE-Como-realizar-calculo-para-Tarefeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31452226869015)Tempo aproximado para leitura: **00:02:50 min**

**Dúvida**Como calcular folha de pagamento para tarefeiro?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**

Os funcionários tarefeiros têm direito à garantia salarial mínima correspondente ao valor do  
salário mínimo, caso o valor de suas tarefas não o atinjam. Esta afirmação tem como base legal o  
artigo 78 da CLT.  
Para atender à legislação temos no Protheus o identificador de cálculo: 0652 – Garantia de tarefas.  
Se não existir a verba o sistema não apresentará nenhum cálculo referente a garantia.  
  
O sistema soma as tarefas executadas no período indicado pela pergunta Taref. Período De/Até?. Em seguida:  
- Calcula o valor do adiantamento, aplicando o percentual de adiantamento do Cadastro de Funcionários sobre o valor do salário base de cálculo do adiantamento;  
- Compõe a Base de Imposto de Renda do adiantamento, somando todas as verbas de provento e subtraindo todas as verbas de desconto com incidência positiva para Imposto de Renda e Referente ao Adiantamento;  
- Calcula o IR do Adiantamento, a partir da base de imposto de renda do adiantamento;  
- Calcula o liquido do adiantamento, somando todas as verbas de provento e subtraindo todas as verbas de desconto com incidência positiva referente ao Adiantamento;  
- Calcula o valor do arredondamento do adiantamento se o parâmetro MV\_ARREDAD estiver preenchido.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049107473)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048238894)  
  
**Cadastro de funcionários**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048254474)  
  
**Cadastro de Tarefas**  
**Atualizações > Definições Cálculo > Manutenção de Tabelas > S070 (tarefas)**  
Cadastrar Cod. Tarefa / Descrição e Valor Unitário ![](https://centraldeatendimento.totvs.com/hc/article_attachments/25253816963095)

**Cadastro da Verba  
Atualizações > Definições de Calculo > Verbas**  
Atrelar a Tarefa no campo Cod. Tarefa - Exemplo Cod tarefa 004 atrelado na verba 387

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25253810754967)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25253810761111)  
  
**Lançamento de Tarefa  
Atualizações > Lançamentos > Tarefas**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25253810768535)  
  
  
**Cálculo da Folha   
Sem garantia de tarefa  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/25253816990487)**

**Saiba Mais**Para informações sobre o cálculo de DSR para categoria tarefeiro, acesse o *link* a seguir:  
 <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021010632-MP-GPE-Como-calcular-DSR-para-Tarefeiro>

[RH - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
