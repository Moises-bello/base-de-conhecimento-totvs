---
article_id: 4423745553175
category: MDT - PCMSO
content_hash: 6eb338695bb70d74fe765012e7a4e62a00aab04a559004fa76fc9da98e394c48
fetched_at: '2026-06-28T22:44:28.280956+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Ao gerar o PCMSO existe alguma configuração para
  os exames serem gerados somente em dias úteis
type: support-article
updated_at: '2025-10-06T18:01:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4423745553175-RH-Linha-Protheus-MDT-Ao-gerar-o-PCMSO-existe-alguma-configura%C3%A7%C3%A3o-para-os-exames-serem-gerados-somente-em-dias-%C3%BAteis
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372648730007) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao gerar o PCMSO existe alguma configuração para os exames serem gerados somente em dias úteis?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Se o médico possuir calendário de atendimento aos finais de semana, e se o parâmetro **MV\_NG2PFDS** estiver ativo, a data de seus exames poderá ser gerada em dia não útil.  
  
Para os exame não serem gerado em dias não úteis, o seu parâmetro **MV\_NG2PFDS** deve esta desativado com conteúdo = N ( Não).  
  
Para conferir o conteúdo do parâmetro, acesse o Configurador (*SIGACFG*), no caminho: *Ambiente - Cadastro - parâmetros* - localize e edite conforme exemplo abaixo.  
  
![](https://totvssuporte.zendesk.com/attachments/token/iq59Z8Q8CA4V9NhviIzip0mIi/?name=inline1169863934.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/24QXJjocsgIrOQ5AQ8p4dPCLH/?name=inline-721936057.png)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos sobre PCMSO](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945214-MDT-PCMSO)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
