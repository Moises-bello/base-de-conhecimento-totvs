---
article_id: 360005103432
category: GPE - eSocial - Não Periódicos
content_hash: 53589902f0d9250727e751ba5844ba47ee3513504cf0c28b542c33ad1311cefb
fetched_at: '2026-06-28T22:45:04.404875+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200/S-2299 - Como registrar uma rescisão
  complementar no eSocial
type: support-article
updated_at: '2026-06-16T11:27:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360005103432-RH-Linha-Protheus-GPE-eSocial-S-1200-S-2299-Como-registrar-uma-rescis%C3%A3o-complementar-no-eSocial
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41259064355863) Tempo aproximado para leitura: 00:02:00**  
  
**Dúvida**  
Como registrar uma rescisão complementar, complementar por dissidio ou retificação no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) -  Gestão de Pessoal – Todas as versões  
  
**Solução**  
Essa pergunta foi respondida pelo governo no site oficial do eSocial item **04.58 - (23/05/2018).**

Não existe a figura de **Rescisão Complementar** no eSocial. Eventuais pagamentos de diferenças de rescisão devem ser realizados da seguinte forma:

1. Desligamento **ocorreu na vigência** do eSocial: se a diferença decorre de erro no momento da rescisão, o usuário deverá retificar o evento **S-2299**. Serão gerados encargos pelo pagamento em atraso;
2. Desligamento **ocorreu na vigência** do eSocial: se os valores eram devidos **após o** desligamento (ex: pagamento retroativo de *CCT*), o usuário deverá informar os valores no evento **S-1200** com indicação no grupo *InfoPerAnt;*
3. Desligamento **ocorreu antes da vigência** do eSocial: se a diferença decorre de **erro no momento da rescisão**, o usuário deverá utilizar os mesmos sistemas do momento do desligamento (GFIP, GRRF);
4. Desligamento **ocorreu antes da vigência** do eSocial: se os valores eram devidos **após o desligamento** (ex: pagamento retroativo de *CCT*), o usuário deverá enviar o evento **S-2200** com o grupo desligamento preenchido. Informar os valores no evento **S-1200** com indicação no grupo *InfoPerAnt*. Não gera encargos no pagamento de tributos e FGTS.

No Protheus temos duas situação diferentes que devem ser utilizadas observando a resposta do eSocial indicada acima:  
  
**1 -** Nos casos em que o **Período do GPE está ABERTO** a rotina de Rescisão lhe apresenta as três opções abaixo:  
  
**a - Recalcular =** Para reprocessar o cálculo da Rescisão Original, gera uma retificação do S-2299;  
  
**b - Complementar =** Utilizada para pagamento de complementos não calculados na Rescisão Original (com exceção de Diferença de Dissidio), gera uma retificação do S-2299;  
  
**c - Complementar por Dissidio =** Utilizada para pagamento de diferenças de Dissidio não calculadas na Rescisão Original, é necessário utilizar rotina de Dissidio Retroativo (vide [MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)), gera uma retificação do S-2299.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027337231)  
  
**2 -** Nos casos em que o **Período do GPE está FECHADO** a rotina de Rescisão lhe apresenta as três opções abaixo:  
  
**a - Complementar =** Utilizada para pagamento de complementos não calculados na Rescisão Original (com exceção de Diferença de Dissidio), gera um evento S-1200 com informação na tag <infoPerAnt>;  
  
**b - Complementar por Dissidio =** Utilizada para pagamento de diferenças de Dissidio não calculadas na Rescisão Original (vide [MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)), gera um evento S-1200 com informação na tag <infoPerAnt>;  
  
**c - Retificação =** Para reprocessar o cálculo da Rescisão Original, gera uma retificação do S-2299 no período do eSocial do evento S-2299 Original.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027337771)  
  
[RH - Linha Protheus - GPE - eSocial - S-1200- Como calcular **Rescisão para Estagiário** através da rotina de Rescisão do SIGAGPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026466213)  
  
**Atenção:**  
Para gerar o S-1200, será necessário **integrar o roteiro RES e realizar o cálculo da folha de pagamento** para que seja possivel gerar o S-1200 com as informações da rescisão complementar.  
  
**Saiba Mais**  
Para adquirir mais conhecimento, acesse os *links* abaixo:   
[Boletim Técnico - Retificação da Rescisão Original](http://tdn.totvs.com/display/public/PROT/3987786+DRHESOCP-8399+Rescisao+Complementar+-+Retificacao+da+Rescisao+Original)  
[MP - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271)  
[MANUAL GPE - Dissídio Retroativo](http://tdn.totvs.com/pages/releaseview.action?pageId=220889925)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)
