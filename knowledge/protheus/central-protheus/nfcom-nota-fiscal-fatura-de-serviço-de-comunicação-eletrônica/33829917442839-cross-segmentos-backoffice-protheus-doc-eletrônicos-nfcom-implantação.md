---
article_id: 33829917442839
category: NFCOM - Nota Fiscal Fatura de Serviço de Comunicação Eletrônica
content_hash: 027eeb12db16fd2ec993dff1e4c5533e9920dcf187f77b4d7b3c5c52b270592f
fetched_at: '2026-06-28T22:39:55.153749+00:00'
product: protheus
section_id: 33828030194199
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Implantação
type: support-article
updated_at: '2025-11-14T01:25:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/33829917442839-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Implanta%C3%A7%C3%A3o
---

**Dúvida**  
Como realizar a implantação da NFCOM (Nota Fiscal Fatura de Serviço de Comunicação Eletrônica) no Protheus?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - Todas as versões      
  
**Solução**  
Primeiramente, o que seria a NFCOM?

> *O Projeto NFCom tem como objetivo a implantação de um modelo nacional de documento fiscal eletrônico (modelo 62) que venha substituir a sistemática atual de emissão da Nota Fiscal de Serviço de Comunicação/Telecomunicações (modelos 21 e 22), com validade jurídica garantida pela assinatura digital do emitente, simplificando as obrigações acessórias dos contribuintes e permitindo, ao mesmo tempo, o acompanhamento da emissão em tempo real pelo Fisco.*

Para realizar a implantação no Protheus se fazem necessários os seguintes passos detalhados abaixo:  
  
**1.** Providenciar todos os **pré-requisitos de atualizações** (TSS e Protheus):  
- [Clicando aqui.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33719999024279)  
  
**2.** Configurar a espécie do documento como NFCOM, exemplo: **MV\_ESPECIE = 353=NFCOM,** através do Configurador (SIGACFG).  
  
**3.** Configurar o parâmetro **MV\_CODREG** com *1-Simples Nacional - 2-Simples Nacional-Excesso de sub-limite de receita bruta ou 3- Regime Nacional,* de acordo com o regime da empresa.  
  
**4.** Gerar um documento de saída ou entrada, além de **obrigatoriamente ter que gerar o Complemento Fiscal** com as devidas informações sobre o serviço prestado**,** caso contrário, o documento não será apresentado dentro da rotina SPEDNFE:  
  
Exemplo abaixo para uma nota de saída:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33830531075863)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33830734510615)  
  
Campos a serem preenchidos: [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Complemento Fiscal (SFX) x XML](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35545503729559-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Complemento-Fiscal-SFX-x-XML).  
  
**5.** Ter o acesso à rotina **SPEDNFE**, responsável por: **transmissão, monitoramento, consulta, cancelamento, impressão, consulta de chave e impressão** da NFCOM:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33830098030231)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33830098033815)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/33830123243543)

**Seguem abaixo todas as funcionalidades para a NFCOM, com os links individuais e todos os devidos detalhes (passo a passo):**  
  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Transmissão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33933216495511-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Transmiss%C3%A3o)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Monitoramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33933636487319-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Monitoramento)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Cancelamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33934461505815-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Cancelamento)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Impressão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33935739942167-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Impress%C3%A3o-DANFCom)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Consulta de Chave](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33934983649687-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Consulta-de-Chave)  
- [Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFCOM - Envio de E-mail](https://centraldeatendimento.totvs.com/hc/pt-br/articles/33936116643607-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-NFCOM-Envio-de-E-mail)  
  
**Documentação com todas as tags disponíveis no layout da NFCOM:**  
- [https://tdn.totvs.com/pages/releaseview.action?pageId=947303730](https://tdn.totvs.com/display/TSS/XML+NFcom)  
  
**IMPORTANTE**  
Abaixo um escopo de atendimento para cada tipo de cenário e a equipe responsável que deve ser acionada:  
- TSS: Protheus SPED  
- Escrituração: Fiscal  
- Documento de Saída: Faturamento  
- Documento de Entrada: Compras  
- Complemento Fiscal: Arquivos Magnéticos
