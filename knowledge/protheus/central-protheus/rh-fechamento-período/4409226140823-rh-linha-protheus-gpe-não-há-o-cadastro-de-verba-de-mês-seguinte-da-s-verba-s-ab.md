---
article_id: 4409226140823
category: RH - Fechamento Período
content_hash: 3737429a0be2516c293ec0d2b70e46eb4856b72ea335a8bdc18315987db8f453
fetched_at: '2026-06-28T22:43:24.475687+00:00'
product: protheus
section_id: 360011909793
source: central-protheus
title: 'RH - Linha Protheus - GPE - Não há o cadastro de verba de mês seguinte da
  (s) verba (s) abaixo: Filial: xxxx xxx/xxx/xxx/xxx/xxx/xxx'
type: support-article
updated_at: '2025-04-16T12:01:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409226140823-RH-Linha-Protheus-GPE-N%C3%A3o-h%C3%A1-o-cadastro-de-verba-de-m%C3%AAs-seguinte-da-s-verba-s-abaixo-Filial-xxxx-xxx-xxx-xxx-xxx-xxx-xxx
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24909289638935) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No fechamento do período da Folha de Pagamento, Sistema emite no log de ocorrências alerta: Não há o cadastro de verba de mês seguinte da (s) verba (s) abaixo: Filial: xxxx xxx/xxx/xxx/xxx/xxx/xxx, mas estas verbas já possuem verba de mês seguinte cadastradas para todas as filiais ativas.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409226069015)  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12

**Causa**Este incidente ocorre quando existem empresas e/ ou filiais **excluídas**, pois o fonte de **Fechamento de Período**, GPEM120, valida as informações contidas na tabela **SM0 - Cadastro de Empresas**. Se em algum momento existiu uma filial com movimentação e consequentemente registros de funcionários, ele vai acusar a inconsistência devido comparativo da **SRA - Funcionários** com esta Filial inativa.  
  
**Solução**

Para identificar qual a Filial deve ser restaurada no Sigamat, é necessário analisar os registros da **SRA - Funcionários** e comparar com as filiais ativas no Sistema. Caso tenha algum funcionário correspondente a uma empresa/ filial inativa, basta restaurar seu cadastro na **SM0 - Cadastro de Empresas**.

**Sabia mais:**[RH - Fechamento Período](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360011909793-RH-Fechamento-Per%C3%ADodo)
