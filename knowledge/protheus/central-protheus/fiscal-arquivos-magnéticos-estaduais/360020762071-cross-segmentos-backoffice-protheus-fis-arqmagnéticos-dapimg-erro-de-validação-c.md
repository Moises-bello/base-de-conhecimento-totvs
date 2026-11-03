---
article_id: 360020762071
category: Fiscal Arquivos Magnéticos - Estaduais
content_hash: 018656f8b2308e746c231e3ed254fb282788ab4899b963f4e4219707e9fe838f
fetched_at: '2026-06-28T22:42:10.667854+00:00'
product: protheus
section_id: 1500001546662
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - DAPIMG - Erro
  de validação "Coluna 4 deve ser igual a 0,00 (Linha ??)"
type: support-article
updated_at: '2022-08-17T20:11:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020762071-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-DAPIMG-Erro-de-valida%C3%A7%C3%A3o-Coluna-4-deve-ser-igual-a-0-00-Linha
---

**Ocorrência**Ao importar o arquivo da **DAPIMG** no validador, consta o seguinte erro de validação: "Coluna 4 deve ser igual a 0,00 (Linha ??)"  
  
**Ambiente**Protheus – Livros Fiscais – A partir da versão 11.80  
  
**Causa**Pode ser que o parâmetro **MV\_DAPIC04** esteja com conteúdo.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Verifique o parâmetro **MV\_DAPIC04** e deixe sem conteúdo (em branco);  
2. Gere o arquivo novamente.
