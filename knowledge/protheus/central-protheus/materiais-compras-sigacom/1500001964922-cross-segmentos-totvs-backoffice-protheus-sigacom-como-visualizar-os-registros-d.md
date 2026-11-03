---
article_id: 1500001964922
category: Materiais - Compras (SIGACOM)
content_hash: 5f29d74eeb80fa28b2ba691dc18eee86998b26e1312cb0a43478d0a313e7e999
fetched_at: '2026-06-28T22:41:16.114370+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como visualizar os
  registros de todas filiais na Liberação de Documento ( MATA094 ) ?
type: support-article
updated_at: '2025-10-24T20:12:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001964922-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-visualizar-os-registros-de-todas-filiais-na-Libera%C3%A7%C3%A3o-de-Documento-MATA094
---

**Dúvida**  
Como visualizar os registros de todas / outras filiais na Liberação de Documento (MATA094)?  
  
**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**Nativamente, a rotina de ***Liberação de Documentos (MATA094)*** lista somente os registros da filial logada.

Porém, através do ponto de entrada ***MT094LBF*** é possível listar os registros de todas filiais.

**Exemplo de configuração do ponto de entrada MT094LBF:**

#Include '[Protheus.ch](http://protheus.ch/)'

User Function MT094LBF()

Local lRet := .F. //Não filtrar por filial

Return lRet

![TESTE-NFC-MENSAGEM-DE-EMAIL-‐-Feito-com-o-Clipchamp-_2_.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/22899882845719)

Para maiores informações, [clique aqui.](https://tdn.totvs.com/display/public/PROT/TTT879_DT_PONTO_ENTRADA_MT094LBF)

Para dúvidas na utilização do ponto de entrada, verificar juntamente à Equipe de suporte ao ADVPL.

***Saiba Mais :***

[Ponto de Entrada MT094LBF](https://tdn.totvs.com/display/public/PROT/TTT879_DT_PONTO_ENTRADA_MT094LBF)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
