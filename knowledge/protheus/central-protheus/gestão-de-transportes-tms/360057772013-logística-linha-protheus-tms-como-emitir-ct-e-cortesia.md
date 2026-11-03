---
article_id: 360057772013
category: Gestão de Transportes (TMS)
content_hash: 72eab997f83552b4ac457bc425279dd6889bcc03698d3b58b58274aa8cd75ea2
fetched_at: '2026-06-28T22:45:27.419622+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Como Emitir CT-e Cortesia
type: support-article
updated_at: '2022-07-19T12:57:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057772013-Log%C3%ADstica-Linha-Protheus-TMS-Como-Emitir-CT-e-Cortesia
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura:**00:01:50 min**  
**Dúvida**Como emitir **CT-e - Conhecimento de Transporte Eletrônico Cortesia** no **TOTVS Logística TMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Para emitir o **CT-e** **Cortesia**, realize os seguintes passos:  
  
Cadastre o **Tipo de Serviço** no **Configurador - SIGACFG,**  em **Tabelas Genéricas**, Tabela **L4 - Tipos de Serviço**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097109993/mceclip0.png)

Inclua o código e descrição do serviço que utilizará para **CT-e** de **Cortesia**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094808874/mceclip1.png)

No **TOTVS Logística TMS**, acesse a rotina **Atualizações/ Serviços/ Serviço x Tarefas - DLGA070** e inclua o serviço cadastrado na tabela genérica. Informe o campo **Categ. Servic - DT5\_CATSER**como **1 - Negociação** e o campo **DC5\_DOCTMS - Docto. Transp**como **A - CRTC CORTESIA.**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094809694/mceclip2.png)

Informe o serviço criado no contrato do cliente em **Atualizações/ Comercial/ Contrato Cliente - TECA250.**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094810934/mceclip3.png)

Cadastre a configuração de documento para o documento **A - CTRC CORTESIA** em **Atualizações/ Doctos e Regras/ Config. Documentos - TMSA150.**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360097112033/mceclip4.png)

Com todos os cadastros listados acima efetuados, para gerar o **CT-e Cortesia,** basta informar o campo **Serviço - DTC\_SERVIC** com o serviço vinculado ao contrato do cliente.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094811974/mceclip5.png)

Após a inclusão do documento, calcule-o e transmita-o à **SEFAZ - Secretaria de Estado da Fazenda.** Para transmitir, atente-se ao filtro do **Monitor de transmissão**, informando o **Tipo do Documento** como **A - CRTC CORTESIA**.

**![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094813514/mceclip6.png)**

Após o cálculo, será gerado o documento de transporte. Para consultá-lo, acesse a rotina em **Atualizações/ Transporte/ Manutenção Doctos - TMSA500**.  
  
O documento de transporte será do tipo **A - CTRC CORTESIA**, a série será a definida no cadastro da **Configuração de Documentos** e os valores de frete e a composição do frete serão calculados e serão maiores que zero.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360094818014/mceclip7.png)
