---
article_id: 36728875929751
category: RH - Funcionários
content_hash: 2f5c211acc744eb66a2ca005e211863c8c86d560e5758e4db33464a970113038
fetched_at: '2026-06-28T22:43:28.704572+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Sistema não atualiza o Controle de Dias de Direito
  do funcionário corretamente quando feito reembolso de faltas
type: support-article
updated_at: '2025-12-02T19:48:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36728875929751-RH-Linha-Protheus-GPE-Sistema-n%C3%A3o-atualiza-o-Controle-de-Dias-de-Direito-do-funcion%C3%A1rio-corretamente-quando-feito-reembolso-de-faltas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36728875905815) Tempo aproximado para leitura: 00:01:12 min

**Dúvida**  
Sistema não atualiza o Controle de Dias de Direito do funcionário ao reembolsar faltas descontadas indevidamente

**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões

**Solução**  
Para que o reembolso de faltas descontadas indevidamente seja corretamente considerado no controle de dias de direito do colaborador, é necessário realizar algumas configurações específicas nas verbas de desconto e reembolso.

1. As verbas de **Desconto** e **Reembolso** devem ter as seguintes configurações:
   * Quantidade de **Lançamento**: **9**
   * Lançamento **Diário**: **Sim**
   * **Medias** de férias: **S (ou SP)**
2. O mnemônico **P\_SEGFALT** deve ser definido como verdadeiro (.**T**.).
3. As verbas de **Reembolso** precisam ser lançadas com a **data de referência** em que **ocorreu** o desconto da **falta** e **dentro do período aquisitivo** correspondente.

Ao realizar estas etapas, quando o fechamento dos períodos for realizado, o sistema reconhecerá automaticamente a falta e o reembolso, atualizando assim o controle de dias de direito.

**Saiba Mais**

[RH - Linha Protheus - GPE - Faltas e Reembolsos no cálculo de 13º](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052988053-RH-Linha-Protheus-GPE-Faltas-e-Reembolsos-no-c%C3%A1lculo-de-13%C2%BA)

[RH - Linha Protheus - GPE - Quais são as verbas de Faltas que podem influenciar nos cálculos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4412351039767-RH-Linha-Protheus-GPE-Quais-s%C3%A3o-as-verbas-de-Faltas-que-podem-influenciar-nos-c%C3%A1lculos)

[RH - Linha Protheus - GPE - Como conferir Faltas do Funcionário apresentadas no cálculo de Férias](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053018573-RH-Linha-Protheus-GPE-Como-conferir-Faltas-do-Funcion%C3%A1rio-apresentadas-no-c%C3%A1lculo-de-F%C3%A9rias)
