---
article_id: 20897652096407
category: Faturamento - Cadastros
content_hash: c4939f09fb2e5440eba224fd2a2f6d7d42bb96faab4313b87be66897d2a867a7
fetched_at: '2026-06-28T22:38:36.843675+00:00'
product: protheus
section_id: 1500001539221
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT (Faturamento)
  - Cadastro de Segmentos
type: support-article
updated_at: '2024-10-18T12:52:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20897652096407-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Faturamento-Cadastro-de-Segmentos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20897652074263) Tempo aproximado para leitura: **00:02:30** **min****Dúvida**Como cadastrar o segmento para os clientes na aba vendas nos campos segmentos.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS SIGAFAT(FATURAMENTO) - Todas as versões.  
  
  
**Solução:**Para permitir que o cadastro de clientes tenha segmentos diferentes dos utilizados no padrão, é necessário criar um novo campo. Este exemplo demonstra como realizar esse processo.  
  
1. Entrar no módulo **SIGACFG**(Configurador).  
2. Acessar Ambiente, cadastros, tabelas e filtrar pela consulta a tabela T3 e clicar em alterar.  
3. Após clicar em alterar, o sistema exibirá todos os segmentos disponíveis.  
4. Para incluir um novo campo, desça até a última linha do campo e pressione uma vez para baixo.  
5. Isso permitirá a inclusão de um novo segmento. Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20897667935511)  
  
6. Realizado a inclusão, volte para a rotina de **Cadastro de Clientes** (**CRMA980**) e (**MATA030**). Vá até a aba "Vendas" e desça até o título "**Segmentos**". Na opção "**Segmento1**", você poderá consultar o novo campo criado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/20897667936279)

**Observações:**   
Os campos **Cod**.**Segmento** (**A1\_CODSEG**) e Segmento 1 (2, 3, 4, 5, 6, 7 e 8) são completamente distintos, cada um com especificações e tabelas diferentes.

Em saiba mais:  
[Cadastro de Segmento CRMA610](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011288781/preview/eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MTUwMDAxMTI4ODc4MSwicmV2aXNpb25faWQiOiIwMUhOQU45WVFURDRCOVNISEZSTUg2UFhZVCIsImV4cCI6MTcwNjUzNzI0OX0.zzxFVGNdOgMgZ0ydO6_Dgq2QydMlna7HJP4jo2_9zT4)
