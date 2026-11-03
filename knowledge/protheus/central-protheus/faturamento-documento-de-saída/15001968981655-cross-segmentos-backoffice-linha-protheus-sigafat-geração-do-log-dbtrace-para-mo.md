---
article_id: 15001968981655
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 04210d977886a0a39f439c0fa824aa06de534437bcc4fad8ba993ccb8286f3a9
fetched_at: '2026-06-28T22:38:45.308242+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) – SIGAFAT – Geração do Log DbTrace
  para monitoramento de performance
type: support-article
updated_at: '2023-06-01T20:55:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/15001968981655-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-Gera%C3%A7%C3%A3o-do-Log-DbTrace-para-monitoramento-de-performance
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como gerar o Log DbTrace para monitorar baixa performance?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões.

**Solução**Caso esteja enfrentando problemas de baixo desempenho em processamentos, consultas, impressões de relatórios ou mesmo em acesso a rotinas de cadastros, recomendamos a geração do Log DbTrace para avaliação das consultas realizadas em seu banco de dados.

Com o trace gerado o cliente pode verificar os pontos de lentidão em acessos a tabelas do Protheus e recomendar a otimização de seu banco de dados através do plano de manutenção do banco de dados (via DBA), também e possível encaminhar o log para completar avaliações de performance junto a equipe de Suporte Técnico TOTVS.

**Abaixo o passo-a-passo para extrair o log:**

1. Acesse o aplicativo *"DbAccess Monitor"* e Informe o IP e Porta para acesso.
2. Clique na aba "Usuários" e selecione o usuário que ira executar a rotina com baixa performance. Clique no Botão "Rastrear" para iniciar o trace do processamento.
3. Ao executar o processamento da rotina as instruções são visualizadas no rastreamento, após o termino do processamento clique no botão "Salvar" para guardar o Log gerado.
4. Após salvar o arquivo com o trace de processamento da rotina você pode realizar uma avaliação da baixa performance e/ou encaminhar o arquivo para avaliação de sua equipe de T.I. ou mesmo solicitar a avaliação do Suporte Técnico TOTVS.

**Saiba Mais:**<http://tdn.totvs.com/pages/viewpage.action?pageId=274851061>
