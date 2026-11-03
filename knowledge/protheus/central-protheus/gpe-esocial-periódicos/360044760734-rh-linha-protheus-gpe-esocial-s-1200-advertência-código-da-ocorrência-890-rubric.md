---
article_id: 360044760734
category: GPE - eSocial - Periódicos
content_hash: 0fc22d923e9638c91b00b7614085fc581071a920f8b70ec8ddef86c600c1e0f7
fetched_at: '2026-06-28T22:45:07.645870+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-1200 - Advertência - Código da ocorrência
  890: Rubrica incompatível'
type: support-article
updated_at: '2025-07-21T20:27:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044760734-RH-Linha-Protheus-GPE-eSocial-S-1200-Advert%C3%AAncia-C%C3%B3digo-da-ocorr%C3%AAncia-890-Rubrica-incompat%C3%ADvel
---

**Ocorrência**Sequência: 000001 - Tipo: Advertência - Código da ocorrência: 890  
Localização: /eSocial/evtRemun/dmDev[x]/infoPerApur/ideEstabLot/remunPerApur/itensRemun[x]/codRubr  
Descrição: Rubrica incompatível. Ação Sugerida: Utilize somente rubricas cujo código de incidência do FGTS seja compatível com evento de remuneração (código de incidência do FGTS diferente de 21).  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as Versões  
  
**Causa**O erro de validação no **Evento S-1200** ocorre quando existe alguma **rubrica** na remuneração do funcionário com incidência para **FGTS** indevida.  
O **eSocial** realizar a validação das rubricas de acordo com a **Natureza Tributária** e identifica quais as rubrica precisam conter incidência 21 e as que não deverão conter a **incidência** de **FGTS** retornando o erro acima.  
  
Conforme leiaute do eSocial abaixo, o código de incidência **21** é referente a **Base de cálculo do FGTS aviso prévio indenizado.** Normalmente rubricas com incidência FGTS **21** é utilizada no evento de **Desligamento (S-2299)**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33620186083351)  
<https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-versao-1-3-nt-03-2025/index.html#evtTabRubrica>  
  
**Solução** **1.** Verificar no S-1200 se é devido ter verbas com incidência FGTS **21**;  
Para validação da incidência no GPE das verbas do evento S-1200, é possível gerar o Relatório de Conferência do S-1200 e validar a coluna "**Incidência FGTS eSocial**"  
[RH - Linha Protheus - GPE - eSocial - S-1200 - Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334-RH-Linha-Protheus-GPE-eSocial-S-1200-Como-gerar-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-S-1200-no-m%C3%B3dulo-GPE?source=search)  
**Obs.:** Também é importante validar que não haja divergência na configuração das verbas entre Protheus e eSocial.  
  
**2.** Caso não seja devido, realizar o ajuste da rubrica alterando a incidência no GPE;  
[Como ajustar incidência e validade de rubricas no governo, TAF e GPE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024360512)  
  
**3.** Após ajuste, integrar o evento S-1010 com o TAF e transmitir ao eSocial, verifique a data base que esta logado no sistema, ou ajuste o período inicial de vigência, pois a partir dessa data a rubrica irá ter sua data de inicio de validade, ou seja, não pode ser posterior a folha que esta sendo enviada.  
  
**4.** Por fim, após ajustes na configuração das verbas, exclua o S-1200 no TAF, integre novamente e valide a transmissão.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes)  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"  
Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade****WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
