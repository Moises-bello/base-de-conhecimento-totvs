---
article_id: 25977474343959
category: Financeiro - Contabilização
content_hash: bca474b069a057069d19a56566f27af80b61eb507419aa10c82a8a41fc3ceb42
fetched_at: '2026-06-28T22:38:05.284109+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Qual a funcionalidade
  do Bloqueio por Processo
type: support-article
updated_at: '2024-08-29T14:16:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25977474343959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-funcionalidade-do-Bloqueio-por-Processo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25993841789207)** Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**Qual a funcionalidade do Bloqueio por Processo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

O objetivo desta funcionalidade é facilitar o processo de **fechamento contábil**, permitindo ao usuário bloquear a movimentação de outros módulos, além da contabilidade, de forma unificada. Isso garante a integridade do fechamento contábil.

Os processos e módulos disponíveis para bloqueio são:

* **Ativo Fixo**
* **Compras**
* **Contábil**
* **Estoque**
* **Financeiro – Contas a Pagar**
* **Financeiro – Contas a Receber**

**Processo**

Mesmo com o calendário fechado, é possível **excluir**/**estornar**, **alterar** e **incluir** o registro com data retroativa. Para impedir esse processo, deve-se realizar o bloqueio por processo.

**![Gravar_2024_08_28_16_23_51_28.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25977488746263)**

Após a implementação do bloqueio, qualquer processo com data retroativa dentro do mês bloqueado para a rotina bloqueada será restrito.

![Gravar_2024_08_28_16_35_57_204.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25977474300311)

**Importante**

1º O parâmetro **MV\_BXDTFIN** deve ficar com conteúdo **2**, para acatar o bloqueio.

2º Possuir a amarração do **cadastro de moeda** x **calendário contábil**.

3º Para o correto funcionamento e necessário que as tabelas abaixo estejam com o mesmo compartilhamento

**CTE - Moeda X Calendário**  
**CTG - Calendário Contábil**  
**CQD - Bloqueio do calendário Contábil**  
**CTO - Moeda cadastrada**

4º O parâmetro **MV\_CTBCACH** foi criado para atender à rotina de **Lançamentos Contábeis Automáticos (CTBA102)**. Determina se o **calendário contábil, a moeda, o câmbio e as entidades contábeis (Plano de Contas, Centro de Custos, Item Contábil e Classe de Valor)** devem utilizar informações em cache, visando otimizar a performance.
