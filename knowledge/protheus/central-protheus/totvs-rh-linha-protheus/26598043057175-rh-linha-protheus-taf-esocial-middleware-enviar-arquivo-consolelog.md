---
article_id: 26598043057175
category: TOTVS RH (Linha Protheus)
content_hash: 14453f1f6381cb017a349a4e06b8a1f09563080485b5f5b8a1ea9a23c88e664f
fetched_at: '2026-06-28T22:42:50.576736+00:00'
product: protheus
section_id: 360011673454
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Middleware - Enviar arquivo console.log
type: support-article
updated_at: '2026-06-17T19:17:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26598043057175-RH-Linha-Protheus-TAF-eSocial-Middleware-Enviar-arquivo-console-log
---

**Dúvida**Como enviar arquivo console.log TAF/TSS?   
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Rotinas Comuns - Todas as versões.

**Solução**

1. Localize o servidor do TAF/TSS. (em serviços do Windows)

2. Pare o serviço do TAF/TSS.

\*Os nomes dos serviços podem estar diferente dos exemplos deste documento,

Exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26598043028759)

3. Apague o arquivo console.log da pasta TAF-WS e TSS.

Exemplo: **TAF\bin\app.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26598064319639)**

**TSS\BIN\appserver**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26598064322199)

4. Reinicie o serviço e tente realizar a integração novamente, caso o problema continue, somente enviar os arquivos console.log da pasta TAF-WS e TSS.

5.  Caso seu ambiente seja **CLOUD**, envie um print do parametrizador.

Integração via RM.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26598064325271)

Integração via Datasul, rotina FP0560.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26598043044375)

**Saiba Mais**

**Para saber mais consulte os links abaixo:**

**[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)**  
**[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)**  
**[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)**

**Para conhecimento dos eventos futuros, acessa a nossa página [TOTVS Informa](https://informa.totvs.com/) selecione em categorias a área e pesquise por "Eventos"**

**Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus)**
