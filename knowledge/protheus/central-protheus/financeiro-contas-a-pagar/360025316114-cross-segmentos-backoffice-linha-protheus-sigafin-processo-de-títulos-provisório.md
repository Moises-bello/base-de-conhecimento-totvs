---
article_id: 360025316114
category: Financeiro - Contas a Pagar
content_hash: 308722527e93f2d873bf5fb92f848b2f7bb3551fc46fb54837bc97f72f5b6bd5
fetched_at: '2026-06-28T22:38:09.801978+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Processo de títulos provisórios
  (PR)
type: support-article
updated_at: '2026-03-16T11:50:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025316114-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Processo-de-t%C3%ADtulos-provis%C3%B3rios-PR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21714468348055)**Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Como faz o processo de títulos provisórios (PR), substituição e funcionalidade?   
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro  - Todas as versões  
  
**Solução**  
Nós utilizamos as previsões de gastos com contas de consumo (água, luz, telefone) para programar nosso fluxo de caixa, uma vez que não dispomos dos valores exatos. Dessa forma, fazemos uma projeção para o ano inteiro.  
  
**Cenário**

Digamos que o custo mensal com água varia entre 99,00, 100,00 e 102,00, dependendo do consumo. Por isso, provisiono R$ 100,00 por mês, totalizando R$ 1.200,00 ao longo de um ano.  
  
Faço inclusão de um **título tipo PR**, o desmembramento em 12 vezes.  
O sistema baixa o **título tipo PR** 1.200,00 gerando 12 **título PR** de 100,00 a cada mês.

![Gravar_2024_06_26_10_03_33_557.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24443652694167)

A cada mês, ao receber o boleto com o valor correto, substitua o **título tipo PR** de R$ 100,00 pelo valor exato, como por exemplo R$ 102,00, sendo possível alterar as demais dados do título, como tipo, fornecedor e natureza.

![Gravar_2024_06_26_09_49_40_879.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/24443652704663)

**📢️ Importante:**

Os **títulos provisórios (PR)** só podem ser substituídos **pela rotina do módulo Financeiro** do sistema.

Para os casos em que se deseja realizar a **inclusão de títulos provisórios diretamente pela medição de contratos (SIGAGCT)**, é necessário **entrar em contato com o time de referência do módulo de Contratos**, responsável pela análise e direcionamento técnico dessa demanda.

**Saiba Mais**  
[Contas a Pagar - FINA050](https://tdn.totvs.com/pages/releaseview.action?pageId=490636586)

[Cross Segmento - Backoffice Linha Protheus - O PR não volta para o status de aberto quando excluído o PA gerado por substituição do PR](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37730714062871-Cross-Segmento-Backoffice-Linha-Protheus-O-PR-n%C3%A3o-volta-para-o-status-de-aberto-quando-exclu%C3%ADdo-o-PA-gerado-por-substitui%C3%A7%C3%A3o-do-PR)

<https://www.youtube.com/watch?v=1kQBtPUvKiU>
