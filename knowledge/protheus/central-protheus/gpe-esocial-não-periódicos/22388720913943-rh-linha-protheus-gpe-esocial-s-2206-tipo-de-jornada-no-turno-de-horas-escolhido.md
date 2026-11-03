---
article_id: 22388720913943
category: GPE - eSocial - Não Periódicos
content_hash: 9480cbb5b972f95d73d2845c787976fc067ecfc930aa795671a99a0f36d01207
fetched_at: '2026-06-28T22:45:04.764598+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2206 - Tipo de jornada no turno de
  horas escolhido é invalido. favor verificar o campo R6_TPJOR1
type: support-article
updated_at: '2026-06-16T13:45:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22388720913943-RH-Linha-Protheus-GPE-eSocial-S-2206-Tipo-de-jornada-no-turno-de-horas-escolhido-%C3%A9-invalido-favor-verificar-o-campo-R6-TPJOR1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22388767324695) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**No módulo SIGAGPE, ao tentar realizar uma transferência é apresentada a mensagem **Tipo de jornada no turno de horas escolhido é invalido. favor verificar o campo R6\_TPJOR1****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Esse incidente ocorre, pois o campo R6\_TPJOR1 não está preenchido corretamente ou não foi preenchido o turno no momento da transferência.  
  
**Solução**1. Verifique se os campos **R6\_TPJOR1** e **R6\_ESNOTU** estão preenchidos corretamente, de acordo com o Leiaute do eSocial, no turno da filial origem e da filial destino  
Caminho: **SIGAGPE > Atualizações > Ponto Eletrônico > Turno de Trabalho**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407177458455)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407177490583)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198586647)  
  
2. Verifique se o turno origem e destino foram preenchidos na aba Dados Cadastrais da Transferência  
Caminho: **SIGAGPE > Atualizações > Funcionário > Transferências**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198605335)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198623895)  
Obs.: Caso o campo não esteja aparecendo, habilite o campo Turno Trab. (RA\_TNOTRAB) em **Outras Ações > Config. Campos**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198651671)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198669463)  
  
3. Verifique se os campos **Turno Trab. (RA\_TNOTRAB)**, **Regra Apont. (RA\_REGRA )** e **Seq. Ini. Turn. (RA\_SEQTURN)** estão preenchidos na filial origem no Cadastro do Trabalhador no GPE.  
Caminho: **SIGAGPE > Atualizações > Funcionário > Gestão Funcionários**.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22407198686871)  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
