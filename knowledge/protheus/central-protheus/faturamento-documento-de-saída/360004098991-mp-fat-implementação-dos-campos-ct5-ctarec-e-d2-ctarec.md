---
article_id: 360004098991
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: c28b0d54882dadfa1a4064242e2a8d7bfc73f603dff0948208e2b4bd3d842697
fetched_at: '2026-06-28T22:38:45.210116+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: MP-FAT- Implementação dos campos CT5_CTAREC e D2_CTAREC
type: support-article
updated_at: '2021-04-28T15:13:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004098991-MP-FAT-Implementa%C3%A7%C3%A3o-dos-campos-CT5-CTAREC-e-D2-CTAREC
---

**Dúvida**

Implementação dos campos CT5\_CTAREC e D2\_CTAREC.

**Ambiente**

Microsiga Protheus - a partir da versão 12.1.17

**Solução**

Foi implementado os campos CT5\_CTAREC e D2\_CTAREC, referente a um requisito de tratamento EFD  Contribuições da nota de saída, gostaria do pacote para aplicação no ambiente.

 Para solucionar esta questão:

1. Aplique o pacote da issue **DSERFIS1-3560:**

**<https://suporte.totvs.com/portal/p/10098/download?e=680398>**;

2. Aplique o **SDFBRA diferencial** contido na issue na pasta Systemload do Protheus;

3. No programa inicial do Protheus, rode o compatibilizador **UPDDISTR** para ajustar o dicionário aos novos campos em questão.

Para mais detalhes, acesse a documentação técnica: **[DSERFAT-4521 DT Nota Fiscal Saida - Conta Receita EFD Contribuições - LP610](http://tdn.totvs.com/pages/releaseview.action?pageId=341219769)**

Obs: Para efetuar a aplicação de pacote , bem como executar o tratamento de dicionário de dados, é necessário um conhecimento técnico em estrutura Protheus, em caso de dúvida na aplicação do pacote ou no ajuste do dicionário, contate a equipe de Frame Work para auxiliar.
