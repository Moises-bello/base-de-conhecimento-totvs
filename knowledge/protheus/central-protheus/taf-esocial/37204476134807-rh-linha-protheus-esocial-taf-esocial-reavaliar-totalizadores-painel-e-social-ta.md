---
article_id: 37204476134807
category: TAF eSocial
content_hash: 54cc72b04667984165d3f9d4e7584c8baaeda17b7b7fafff6a8f6525f3a201c6
fetched_at: '2026-06-28T22:43:04.317355+00:00'
product: protheus
section_id: 22558578381847
source: central-protheus
title: RH (Linha Protheus) - eSocial - TAF eSocial - Reavaliar Totalizadores - Painel
  E-social (TAFA552A)
type: support-article
updated_at: '2025-12-26T18:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37204476134807-RH-Linha-Protheus-eSocial-TAF-eSocial-Reavaliar-Totalizadores-Painel-E-social-TAFA552A
---

**Dúvida**  
Como Reavaliar Totalizadores no painel E-social (TAFA552A) ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Reavaliar Totalizadores - Painel E-social (TAFA552A)- Todas as versões  
  
  
**Solução**  
**1. Acesse o menu: Miscelânea | E-social | Esocial do futuro** ou **Painel E-social.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37204476108311)

**2. Selecione as opções abaixo:**

* Filial / Período / Eventos (S-1200, S-1210, S-2299, S-2399).
* Marque a opção Forçar Totalizadores
* Clique em Reavaliar Totalizadores

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37204448623767)

**3. Caso o erro persista, crie um AppServer exclusivo para o Protheus.**

* Como criar um AppServer exclusivo (a partir da versão 12.1.2410):

  [RH - Linha Protheus - TAF - eSocial – Configurações - Como criar um appserver exclusivo a partir da versão 12.1.2410](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33938434213271-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%B5es-Como-criar-um-appserver-exclusivo-a-partir-da-vers%C3%A3o-12-1-2410)
* Diagnostico do TAF.

[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF)

* Reavalie novamente os totalizadores e envie o arquivo console.log da pasta APPSERVER TAF.

**Para clientes TAF-Segregado que utilizam as linhas RM ou Datasul**

* Ative a chave TafConOut=1 em (GENERAL) no appserver.ini do seu taf, pasta APPSERVER.

  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/37204978054295)
* Diagnóstico do TAF.

[RH - Linha Protheus - TAF - eSocial - Rotinas Comuns - Como acessar a tela de diagnóstico no TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17988545143063-RH-Linha-Protheus-TAF-eSocial-Rotinas-Comuns-Como-acessar-a-tela-de-diagn%C3%B3stico-no-TAF)

* Reavalie novamente os totalizadores e envie o arquivo console.log da pasta APPSERVER TAF.
* Enviar dbaccess.log e dbconsole.log.

**Saiba Mais**

Para saber mais consulte os links abaixo:

[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)

[Centralizadora TAF](https://tdn.totvs.com/display/public/TAF/Centralizadora+TAF)

[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)

[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)

Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"

Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
