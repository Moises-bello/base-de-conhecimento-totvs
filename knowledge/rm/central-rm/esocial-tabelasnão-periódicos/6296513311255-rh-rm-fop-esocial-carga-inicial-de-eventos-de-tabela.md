---
article_id: 6296513311255
category: eSocial - Tabelas/Não Periódicos
content_hash: 027e4e646473f36f115d8d132cf1aeb118bb44d45df9ae4915ad833f4e37d678
fetched_at: '2026-06-28T22:47:10.275501+00:00'
product: rm
section_id: 1500000834421
source: central-rm
title: RH - RM - FOP - eSocial - Carga Inicial de eventos de Tabela
type: support-article
updated_at: '2024-06-05T11:32:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296513311255-RH-RM-FOP-eSocial-Carga-Inicial-de-eventos-de-Tabela
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21787452762775) Tempo aproximado para leitura: **02:00:00 min****Dúvida**Como gerar o gatilho de carga inicialdos eventos de tabelas?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial- Todas as Versões  
  
**Solução**Para geração de Carga Inicial dos eventos eventos de Tabelas, siga os passos abaixo:  
1. Verifique se no menu **Configurações | Parametrizador | eSocial | Configurações Gerais 1/5**, as [Datas de Obrigatoriedade/Adesão ao eSocial](https://www.gov.br/esocial/pt-br/acesso-ao-sistema/cronograma-de-implantacao)estão corretamente preenchidas, principalmente das **Tabelas**;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296058725911)

2. Selecione o menu **eSocial | Gerar Gatilhos Eventos Iniciais** e selecione **1ª Fase** na área **Faseamento eSocial**;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296134108183)

3. Após os gatilhos de carga inicial serem criados, poderá ser gerado o XML de duas formas:  
  3.1. No menu **eSocial** | **Gerar XML** para gerar os arquivos em lote:

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6296423283991)**

  3.2. Na **Fila de Eventos** selecione os registros e clique em **Gerar XML**:

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6297142530199)

**Atenção:** Caso existam eventos de tabela na fila de eventos, independente do tipo da operação ou status, estes não serão considerados neste processo.  
  
**Saiba mais**[RH - RM - FOP - eSocial - Competência de evento de tabela](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6301634460567-RH-RM-FOP-eSocial-O-funcion%C3%A1rio-chapa-xxxx-est%C3%A1-demitido-e-possui-eventos-de-remunera%C3%A7%C3%A3o-que-n%C3%A3o-se-referem-a-pagamentos-de-diss%C3%ADdio-ou-conven%C3%A7%C3%A3o-coletiva?source=search)
