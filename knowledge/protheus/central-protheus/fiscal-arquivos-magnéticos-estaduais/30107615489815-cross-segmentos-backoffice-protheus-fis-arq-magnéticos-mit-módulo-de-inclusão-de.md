---
article_id: 30107615489815
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 64c72a7d5ae63e192c221f5c9b9f4e71bf6e79aeb64c86f3501ded3cd379eda3
fetched_at: '2026-06-28T22:42:09.202223+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - MIT (Módulo
  de Inclusão de Tributos)
type: support-article
updated_at: '2025-02-20T20:17:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30107615489815-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-MIT-M%C3%B3dulo-de-Inclus%C3%A3o-de-Tributos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30107615483415) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como gerar o arquivo **MIT (Módulo de Inclusão de Tributos)**?

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - A partir da versão **12.1.2310**

**Solução:**

Para configurar o sistema para geração do arquivo **MIT-Módulo de Inclusão de Tributos** é preciso seguir o processo abaixo:

**1 - Atualização:**

O pacote para implantação do MIT trata-se da **expedição contínua do TAF**, que está  
centralizado no link abaixo, de acordo com as releases:  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=634272553>

**OBS:** Para habilitação do **MIT** dentro do **Painel Reinf** é preciso aplicar o pacote acima e rodar o **UPDDISTR.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/30107652114327)

**2 - Configuração** completa da rotina conforme boletim:

<https://tdn.totvs.com/pages/viewpage.action?pageId=904594705>

**Obs**: Para cadastrar dados **"Contabilistas"** - acesse Rotina **TAFA052** - **Contabilistas:**Modulo 84>>Atualizações >>Config.TAF >>Contabilistas.

Para cadastrar dos **"Formas de tributação**" - acesse Rotina **TAFA372** - **Cadastro de Parâmetros de Abertura ECF:**Modulo 84>>Atualizações >Config.TAF >Parâmetros de cálculos.

**Importante:**  
Neste primeiro momento, os dados para a geração do **MIT** serão informados **manualmente** no sistema, não havendo por enquanto, um meio de integração. A rotina de integração será disponibilizada futuramente.

Assuntos relacionados:  
<https://www.totvs.com/blog/fiscal-clientes/dctfweb-melhoria-na-usabilidade-e-novas-funcionalidades/>

<https://www.totvs.com/blog/fiscal-clientes/dctfweb-leiaute-do-modulo-de-inclusao-de-tributos-mit/>
