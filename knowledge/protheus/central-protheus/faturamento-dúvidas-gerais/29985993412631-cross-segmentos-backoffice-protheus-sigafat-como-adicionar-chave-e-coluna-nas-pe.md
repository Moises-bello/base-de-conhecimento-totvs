---
article_id: 29985993412631
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: d21da8005cbac334bfa2b64fd65fc0ed62f50c73d9cf950732e8dbc827d06794
fetched_at: '2026-06-28T22:38:28.812250+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Como adicionar chave e coluna
  nas pesquisas das rotinas do faturamento (SIGFAFAT)
type: support-article
updated_at: '2025-02-17T11:18:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29985993412631-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Como-adicionar-chave-e-coluna-nas-pesquisas-das-rotinas-do-faturamento-SIGFAFAT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29985993401367) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como adicionar chave e coluna nas pesquisas das rotinas do faturamento (SIGFAFAT)?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

1 - Saiba qual é a tabela do Browser. (para isso, basta visualizar algum registro, ir em algum campo do cabeçalho e apertar F1, os campos tem o nome da tabela no começo, antes do '\_')

2 - Vá no configurador (SIGACFG), no caminho "Base de dados" > "Dicionário" > "Base de dados"  
  
3 - Expandir empresa teste > Procurar a tabela (no exemplo, "SA1") > Editar:

> **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdLJ8NIjYKmEpDjdBL7idpc4L-S9glUkxDgWevpcWr5hUAl31KGusM6UVkSl_fAn28EnRpLVwaEHKOZ1K9ddC7tkBzAN2WrmxViy-BW1olwH8yyg4fJMnP-ZGFR239XWxKl3ds9?key=KsRGKWrVpGY266zH1UUl7_X4)**

4 - Expandir menu esquerdo > "Índices" > Criar um novo:

> **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeEwfFfaubB9wToIX65mShsBP6OArnHpH88tcteMUhMjAobCK1mUkg7DHvCvkWJAy_pQ5kqgUJOhuyTIWu9HlWOYkeJKqEA4bj8RKnTNjNQrq02WBp1rvdzT_Ak6OEDsW_UMIyA-w?key=KsRGKWrVpGY266zH1UUl7_X4)**

5 - Crie o novo índice. Colocando as colunas (campos) acrescentado entre '+' na parte "Chave", esses campos é o que aparecerão como coluna para pesquisa no Browse:

> **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfyQz3drokDncOfQV2-rlt28PpxZFauKvaxGA40oRjEKv9KZCFAva7r3aNhSKsqINsjmXr_oyNpZUADeqJXJokVOJOjzjIFj6R1p_0_SZx-t_IEC8oqnOr0wGwrP-DcLNFFSChB1g?key=KsRGKWrVpGY266zH1UUl7_X4)**

OBSERVAÇÃO: Lembrando sempre de marcar "Mostra pesq.", para mostrar na pesquisa do Browse.  
  
6 - Salvar duas vezes:

> **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd2ByHvzlKmHEvdgmSpfiwreyuBgsHADyq2WlwDSwP6o3TMuaghwXnfSO3qNHKdT170l9weOETv6oAW8-BTSBt6mQHM9KcI6FO-25LGGNj7nCX3fRlGqj4CmPnWQL__ntNtheq-Bw?key=KsRGKWrVpGY266zH1UUl7_X4)**

**7 - Resultado: (na pesquisa dentro da rotina (Browse))**

> **![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXd8gaGnvjk1q-ZxZt21Cuo6U1RlpGeMnGgOpY8nfUJs3vq13rp-Hnarw02GttLzGSUqvFUs7_7Yc3Po0NF_-kgATXgibWQfmqPWNttaiajCeVKKyRkWvah5uI1O41j942uiTCZaeQ?key=KsRGKWrVpGY266zH1UUl7_X4)**
