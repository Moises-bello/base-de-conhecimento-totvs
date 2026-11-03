---
article_id: 360024300052
category: Materiais - Compras (SIGACOM)
content_hash: 3e35df20693d4c08fd53daba74b7780a8598966b790436ae19f888420a748990
fetched_at: '2026-06-28T22:41:07.638908+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como Gerar o Log DbTrace
  Para Monitorar Baixa Performance?
type: support-article
updated_at: '2022-05-16T22:20:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024300052-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-Gerar-o-Log-DbTrace-Para-Monitorar-Baixa-Performance
---

**Dúvida**Como gerar o Log DbTrace para monitorar baixa performance ?  
  
**Ambiente**Protheus – Compras – A partir da versão  P11.80  
  
**Solução**Caso esteja enfrentando problemas de baixo desempenho em processamentos, consultas, impressões de relatórios ou mesmo em acesso a rotinas de cadastros, recomendamos a geração do Log DbTrace para avaliação das consultas realizadas em seu banco de dados.

Com o trace gerado o cliente pode verificar os pontos de lentidão em acessos a tabelas do produto Microsiga Protheus e recomendar a otimização de seu banco de dados através do plano de manutenção do database (via DBA), também e possível encaminhar o log para completar avaliações de performance junto a equipe de Suporte Técnico TOTVS.

**Abaixo passo-a-passo para extrair o log:**

1. Acesse o aplicativo *"DbAccess Monitor"* e Informe o IP e Porta para acesso.
2. Clique na aba "Usuários" e selecione o usuário que ira executar a rotina com baixa performance. Clique no Botão "Rastrear" para iniciar o trace do processamento.
3. Ao executar o processamento da rotina as instruções são visualizadas no rastreamento, após o termino do processamento clique no botão "Salvar" para guardar o Log gerado.
4. Após salvar o arquivo com o trace de processamento da rotina você pode realizar uma avaliação da baixa performance e/ou encaminhar o arquivo para avaliação de sua equipe de T.I. ou mesmo solicitar a avaliação do Suporte Técnico TOTVS.

**Saiba Mais:**<http://tdn.totvs.com/pages/viewpage.action?pageId=274851061>
