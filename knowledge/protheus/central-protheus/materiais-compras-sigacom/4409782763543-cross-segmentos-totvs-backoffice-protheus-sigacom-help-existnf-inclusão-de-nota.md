---
article_id: 4409782763543
category: Materiais - Compras (SIGACOM)
content_hash: f493e7353775e7ee7d8bded4545b16c111f8e1b20ed9c017399d86697e864d83
fetched_at: '2026-06-28T22:41:19.878218+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help: EXISTNF Inclusão
  de nota fiscal no Documento de Entrada (MATA103) com mesmo número'
type: support-article
updated_at: '2023-12-28T12:13:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409782763543-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-EXISTNF-Inclus%C3%A3o-de-nota-fiscal-no-Documento-de-Entrada-MATA103-com-mesmo-n%C3%BAmero
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19634708735255) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Compras, ao tentar realizar a entrada de uma nota fiscal com mesmo numero e serie ocorre Help EXISTNF (Numero de Nota Fiscal Já Cadastrado).  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões]  
  
**Causa**Atualmente o sistema não permite que seja incluída uma mesma numeração de documento de entrada pois existe uma integridade (chave única) na tabela **SF1** (**F1\_FILIAL+F1\_DOC+F1\_SERIE+F1\_FORN+F1\_LOJA+F1\_FORMUL**) que não permite tal processo.  
  
**Solução**Para efetuar o lançamento quando necessário, poderá incluir o documento de entrada seguindo o as informações que constam no documento abaixo:

**[Inclusão de documento de entrada](https://tdn.totvs.com.br/pages/releaseview.action?pageId=789412442)**

***Esse documento foi elaborado pelas equipes de desenvolvimento do produto padrão, baseado em solicitações dos clientes, após análise criteriosa.***

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)

[PCOM12024 - Inclusão de nota fiscal no Documento de Entrada (MATA103) com mesmo número](https://tdn.totvs.com/pages/releaseview.action?pageId=284471056)
