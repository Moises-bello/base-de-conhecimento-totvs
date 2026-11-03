---
article_id: 12471161611287
category: Anuais
content_hash: b60e66a58b5dc55bbaf3e409ced399b189677833c3db88e5e1b61fa74945139e
fetched_at: '2026-06-28T22:46:50.906219+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Erro validador DIRF 2023 ano
  base 2022 "Registro não está de acordo com o leiaute do arquivo de importação"'
type: support-article
updated_at: '2025-01-21T19:39:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12471161611287-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Erro-validador-DIRF-2023-ano-base-2022-Registro-n%C3%A3o-est%C3%A1-de-acordo-com-o-leiaute-do-arquivo-de-importa%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:31 min****Dúvida**

Como realizar a correção do erro Registro não está de acordo com o leiaute do arquivo de importação - Não foi encontrada sequencia valida de registros DIRF + RESPO + DECPJ + ou DECPF no inicio do arquivo, apresentado na validação da DIRF?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**O problema ocorre pois o ambiente não esta atualizado para a DIRF 2023, dessa forma, no arquivo magnético é gerado o identificador de estrutura de *layout* de anos anteriores, e ao importar no PGD 2023, o erro é apresentado  
Para solucionar essa dúvida, realize os seguintes passos:

1. Aplique o pacote de atualização para as versões que contemplem a DIRF 2023;  
2. Gere a DIRF novamente no menu Anuais | DIRF;  
3. Verificar na linha 1 se o registro passou a ser **ARNZRXP**;  
4. No arquivo DIRF a primeira linha deve ficar **DIRF|2023|2022|N||ARNZRXP|**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12470828579607)**

Saiba quais versões contemplam a DIRF 2023:

[RH - RM - FOP - DIRF/Informe de Rendimentos: Versões que contemplam a DIRF 2023 ano base 2022](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042587253-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Vers%C3%B5es-que-contemplam-a-DIRF-2023-ano-base-2022)
