---
article_id: 4403947564567
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e9baadd8d31b4a74dfc1bbc7a91a0d7b55639fd5fa0d3f7f32f7f4ac4e7858b5
fetched_at: '2026-06-28T22:42:47.110999+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Validação da quantidade apontada como
  perda pelas rotinas de produção
type: support-article
updated_at: '2021-08-04T17:54:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403947564567-Manufatura-Linha-Protheus-SIGAPCP-Valida%C3%A7%C3%A3o-da-quantidade-apontada-como-perda-pelas-rotinas-de-produ%C3%A7%C3%A3o
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
**Dúvida**O Sistema não valida a quantidade informada como perda na tela que é apresentada quando o parâmetro **MV\_DIGIPER - Utilizado para informar se o usuário deve digitar classificação de perda ou não** possui o conteúdo **S** com a quantidade de perda informada no campo **D3\_PERDA - Perda do Movimento** quando o apontamento se dá pelo **MATA250 - Produção Simples** ou **H6\_QTDPERD - Quantidade Perdida** quando o apontamento se dá pelo **MATA680 - Produção PCP Mod 1** ou **MATA681 - Produção PCP Mod 2**?  
 **Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Não, no padrão não existe uma validação desses conteúdos.  
Para implementar essa validação, pode-se fazer uso dos pontos de entrada **MT685LOk**ou **DIGPEROK**  
  
**Saiba mais**Para verificar a documentação do ponto de entrada **MT685LOk** acesse a documentação: [MT685LOk - Validações nos apontamentos de perdas](https://tdn.totvs.com/pages/releaseview.action?pageId=330842130)   
E para o ponto de entrada **DIGPEROK** clique no *link* [DIGPEROK - Validação de Perdas](https://tdn.totvs.com/pages/releaseview.action?pageId=6089353).
