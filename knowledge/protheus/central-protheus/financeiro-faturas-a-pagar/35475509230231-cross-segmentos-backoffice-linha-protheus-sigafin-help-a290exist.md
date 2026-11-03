---
article_id: 35475509230231
category: Financeiro - Faturas a Pagar
content_hash: 006fa1d6bd40779bb6cff2e5a9e2c6a0aa86b72201a5fa25e811f526baf364a2
fetched_at: '2026-06-28T22:37:34.274485+00:00'
product: protheus
section_id: 35057532916375
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - HELP: A290EXIST'
type: support-article
updated_at: '2025-10-08T11:21:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35475509230231-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-HELP-A290EXIST
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35475471285655) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Ao tentar realizar uma fatura a pagar, sistema retorna o **Help:** **A290EXIST**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução:**

O Help está relacionado ao uso de **condições de pagamento com mais de dois dígitos no campo Parcela**.  
Atualmente, o campo **"parcela"** na tabela de referência possui **apenas uma posição (1 carácter)**, o que limita essa configuração e impede o uso de parcelas com numeração superior.

Para corrigir o comportamento e permitir a utilização de mais parcelas, é necessário **alterar o tamanho do campo PARCELA** por meio do **Configurador**, conforme o passo a passo abaixo:

1. Acesse: **Base de dados > Dicionário > Base de dados**.
2. Clique em **Dicionário de dados** e expanda o menu **Grupo de Campos**.
3. Localize **Descrição – Parcela** e selecione **Editar**.
4. No campo **Descrição – Parcela**, altere o **tamanho para 2**.

![Design sem nome.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/35475509207319)

**Importante**

Caso o **desdobramento ultrapasse 3 caracteres**, ajuste o tamanho do campo **PARCELA para 4**.

Após essa modificação, o sistema passará a reconhecer corretamente parcelas com mais de dois dígitos, garantindo o funcionamento esperado das condições de pagamento.
