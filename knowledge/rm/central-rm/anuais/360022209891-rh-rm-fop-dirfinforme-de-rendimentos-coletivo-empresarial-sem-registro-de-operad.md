---
article_id: 360022209891
category: Anuais
content_hash: 3ce1267c7966511690c6924a4f2c44d06428f37ee6d6549d8e2aee56e9c76087
fetched_at: '2026-06-28T22:46:51.213576+00:00'
product: rm
section_id: 1500000861142
source: central-rm
title: 'RH - RM - FOP - DIRF/Informe de Rendimentos: Coletivo empresarial sem registro
  de operadora (OPSE)'
type: support-article
updated_at: '2025-03-05T18:10:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022209891-RH-RM-FOP-DIRF-Informe-de-Rendimentos-Coletivo-empresarial-sem-registro-de-operadora-OPSE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min  
  
Ocorrência**Ao gerar a rotina DIRF, ocorre a mensagem de aviso: **Declarante com indicativo de plano privado de assistência à saúde - coletivo empresarial sem registro de operadora (OPSE)**.  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**A mensagem ocorre quando houve pagamento de plano de saúde tanto para o titular quanto para o dependente e não foi informado corretamente no cadastro do declarante.  
  
**Solução**Para correção deste aviso, acesse:  
  
1. Acesse **Anuais | DIRF/Informe de Rendimentos | DIRF/Informe de Rendimentos** e avance até os **Parâmetros da Coligada**;  
2. Edite a coligada desejada e vá em **Geral | DIRF em Arquivo | Declarante**;  
3. No campo Indicador de assistência a saúde coletivo empresarial, selecione a opção **2 - Existe pagamento de valor pelo titular/dependente do plano de saúde**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11148972688407)  
  
**Importante**  
Caso selecione a opção **1 - Não existe pagamento de valor titular/dependente** o sistema não levará para o arquivo da DIRF as informações referentes ao plano de saúde, prestadoras de saúde cadastradas e valores das deduções por titulares e dependentes.
