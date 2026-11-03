---
article_id: 360010383851
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 1028c008ca78c79adb3a10f09a211cf1db80eb2ea97538abfdf822928efdbe2d
fetched_at: '2026-06-28T22:42:02.402371+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - FIS - Arq. Magnéticos - SPED FISCAL
  - Registro C114: Cupom Fiscal Referenciado'
type: support-article
updated_at: '2025-02-11T21:26:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010383851-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-Registro-C114-Cupom-Fiscal-Referenciado
---

**Dúvida**  
Como gerar o registro C114 - Cupom Fiscal Referenciado.  
  
**Ambiente**  
MP - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:  
1. Realize a emissão do Cupom eletrônico incluído via SIGALOJA, Faturamento ou NF manual de saída com espécie SPED;  
  
2. Faça o lançamento da nota fiscal de devolução via **Compras** ou **Nota Fiscal manual de entrada**;  
  
3. Realize o complemento da nota fiscal de devolução - opção Cupons Fiscais;  
**Caminho:** Módulo de Livros Fiscais > Atualizações > Movimentos > Nf. Entrada Manual ou Nf. Manual de Saída.  
  
4. Selecione a Nota Fiscal;  
  
5. Acesse o botão Ações Relacionadas > Complemento > Cupons Fiscais.

![](http://tdn.totvs.com/download/attachments/238035285/image2016-7-6%2018%3A43%3A34.png?version=1&modificationDate=1467841455000&api=v2)

**Importante:****Complemento de Nota Fiscal Automático**   
Ponto de Entrada MATUCOMP: Utilizado para alterações automáticas nos complementos dos documentos fiscais após a emissão das Notas Fiscais. Para informações sobre o Ponto de entrada MATUCOMP, acesse: [MATUCOMP - Alterações automáticas](http://tdn.totvs.com/pages/releaseview.action?pageId=6077107).  
O parâmetro **MV\_ATUCOMP** deve ser configurado para que seja possível utilizar o **Ponto de Entrada MATUCOMP (MV\_ATUCOMP = T)**.
