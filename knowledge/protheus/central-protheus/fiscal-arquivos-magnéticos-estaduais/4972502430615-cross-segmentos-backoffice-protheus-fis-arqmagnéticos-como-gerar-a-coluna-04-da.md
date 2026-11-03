---
article_id: 4972502430615
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 7e7a19213ecad6218a1deba2a9551f9b93c9cfd0a37faa5b207783a022d6eb99
fetched_at: '2026-06-28T22:42:10.301050+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Como gerar a
  coluna 04 da DAPIMG?
type: support-article
updated_at: '2022-08-17T19:38:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4972502430615-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Como-gerar-a-coluna-04-da-DAPIMG
---

**Dúvida**Como gerar a coluna 04 da DAPIMG?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais – A partir da versão 12  
  
**Solução**Configuração como gerar a coluna 04 da **DAPIMG**.  
O sistema verifica a configuração da TES, através dos campos:

**Sit.Trib.ICM (F4\_SITTRIB)** = 90 - Outras.

**Livro Fiscal ICMS (F4\_LFICM)** = Outros

Caso, no cadastro da TES o campo Calcula ICMS (**F4\_ICM**) esteja preenchido com SIM, o sistema irá verificar o parâmetro **MV\_DAPIC04** e compara com o campo de CFOP (**D1\_CF**) do documento de entrada.
