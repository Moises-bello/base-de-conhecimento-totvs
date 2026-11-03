---
article_id: 360021653112
category: Escrita Fiscal - Impostos - ISS
content_hash: a7b55f44c74e7dba8cf6482a72755b14a2fdee549d974fff47a60a1693d25d70
fetched_at: '2026-06-28T22:39:35.069209+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: MP - FIS - Utilização do Parâmetro MV_MUNIC na Geração do Título de ISS
type: support-article
updated_at: '2024-10-08T21:15:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021653112-MP-FIS-Utiliza%C3%A7%C3%A3o-do-Par%C3%A2metro-MV-MUNIC-na-Gera%C3%A7%C3%A3o-do-T%C3%ADtulo-de-ISS
---

**Dúvida**É possível definir a loja do fornecedor definido no parâmetro MV\_MUNIC para geração do título de ISS?  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução**Não é possível definir o código da loja para o fornecedor definido no parâmetro MV\_MUNIC. A loja por padrão é fixo "00" conforme tamanho do campo loja.   
  
Portanto, ao gerar título de imposto ISS no contas a pagar, o fornecedor utilizado para este será o conteúdo do parâmetro MV\_MUNIC+ Loja 00.  
O sistema atualmente utiliza-se da loja 00 para tratar / localizar o fornecedor do ISS.  
Neste caso, teríamos 2 opções:   
  
Se avaliar o desbloqueio do fornecedor com loja 00, ou a criação de um novo fornecedor com o código de loja 00 e parametrizar o sistema.
