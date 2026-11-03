---
article_id: 360026661411
category: Gestão de Transportes (TMS)
content_hash: 19edc14d3f977351fbb8c8fdd8e75f939e2e6e42ec678f45e3c98db1d6d4068b
fetched_at: '2026-06-28T22:45:27.666097+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Emissão  de CT-e Complementar de valor
type: support-article
updated_at: '2023-11-30T19:19:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026661411-Log%C3%ADstica-Linha-Protheus-TMS-Emiss%C3%A3o-de-CT-e-Complementar-de-valor
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19249836123415)***Tempo aproximado para leitura: **00:02:00 min****Dúvida**Como emitir **CT-e Complementar** de valor ?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões  
  
**Solução**Documento gerado a partir de um **CT-e - Conhecimento de Transporte Eletrônico**, original que caracteriza o complemento de valor.  
  
**Cadastros necessários:**

* **Configuração de Documentos**Acessar a rotina **TMSA150 - Configuração de Documentos** localizada em:  
  **Atualizações /> Doctos e Regras /> Config. Documentos**.  
  Realizar o cadastro para o documento do tipo complemento - **8**.

![Capturar.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025872931)

Caso deseje utilizar uma série diferente da utilizada no **CT-e** original, não esquecer de ajustar o parâmetro **MV\_ESPECIE**, conforme exemplo:

![Capturar2.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025864972)

* **Regras por Cliente:**Acessar a rotina **TMSA600 - Regras por Cliente** localizada em:  
  **Atualizações / Doctos e Regras / Regras por Cliente**.  
  Realizar um cadastro contendo uma regra para o cliente, ou definir a informação para o cliente genérico para o documento do tipo **CT-e** de Complemento.

![Capturar3.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025876051)

* **Manutenção de Documentos:**Acessar a rotina **TMSA500 - Manutenção de Documentos** localizada em:  
  **Atualizações / Transporte / Manutenção Doctos**.  
  Selecionar o **CT-e** **original / Outras ações / Complemento / Outras ações / Complem.** Informe o valor complementar.

![Capturar4.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360025877411)

Para realizar a transmissão do **CT-e Complementar** para **SEFAZ - Secretaria de Estado da Fazenda** via monitor de transmissão - **TMSAE70**, acesse:

* **Atualizações/Transportes/Manutenção de Documentos - TMSA500:**Selecione o **CT-e** de origem, botão **Outras Ações** a opção **CT-e**, para acessar o **Monitor do CT-e** e filtrar o**CT-e de Complemento**. Na tela de **Parâmetros**, configure a pergunta **Tipo de Documento** com a opção **8 – CTRC Complemento**. Selecione o documento gerado e clique em **Transmitir**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19460319100055)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8270531135639)
