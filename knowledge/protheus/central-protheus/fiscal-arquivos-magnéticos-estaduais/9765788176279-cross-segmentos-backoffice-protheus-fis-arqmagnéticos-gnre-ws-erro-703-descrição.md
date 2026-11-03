---
article_id: 9765788176279
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: a37d2742a5523fe78a8440372adad4e24b868c316735cebc8068203fa8d85634
fetched_at: '2026-06-28T22:42:11.700978+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - GNRE WS - ERRO
  703 - DESCRIÇÃO: FALHA NA VALIDAÇÃO DO RETORNO DA UF: CVC-TYPE.3.1.2:ELEMENT #39,MENSAGEM#39...'
type: support-article
updated_at: '2023-10-02T18:11:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9765788176279-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-GNRE-WS-ERRO-703-DESCRI%C3%87%C3%83O-FALHA-NA-VALIDA%C3%87%C3%83O-DO-RETORNO-DA-UF-CVC-TYPE-3-1-2-ELEMENT-39-MENSAGEM-39
---

**Ocorrência****GNRE WS** - Como corrigir ERRO 703 - DESCRIÇÃO: FALHA NA VALIDAÇÃO DO RETORNO DA UF: CVC-TYPE.3.1.2:ELEMENT #39,MENSAGEM#39....  
**Ambiente**TOTVS Backoffice (Linha Protheus) - Livros Fiscais - A partir da versão **12.1.25**.  
  
**Causa**

Esse incidente ocorre, por falta ou desatualização das **informações extras** na configuração da rotina **FISA095**

**Solução**  
Para corrigir esse erro é preciso configurar as informações extras a rotina **GNREWS** conforme boletim abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=700503940>

 - Para os códigos extras de ambiente Homologação da **GNREWS** temos disponível o **CSV** anexo para importação

 - Para os códigos extras de ambiente Produção da **GNREWS** é preciso sincronizar as informações extras da **UF + receita usada**  
  
**OBS-** Só é possível sincronizar se tiver pelo menos uma linha cadastrada na rotina, ou seja.. o ideal é **IMPORTAR primeiro o CSV** dos códigos de homologação, e **depois SINCRONIZAR** os códigos de produção.
