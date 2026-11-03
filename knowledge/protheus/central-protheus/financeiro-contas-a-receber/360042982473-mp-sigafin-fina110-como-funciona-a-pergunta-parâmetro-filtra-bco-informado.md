---
article_id: 360042982473
category: Financeiro - Contas a Receber
content_hash: 91cd8358ee2106b3f4dddf3461b38b24b21c6683b92ec9b61950520cd740dd45
fetched_at: '2026-06-28T22:38:15.043530+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: MP - SIGAFIN - FINA110 - Como funciona a pergunta parâmetro "Filtra Bco Informado"
type: support-article
updated_at: '2021-04-28T15:17:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042982473-MP-SIGAFIN-FINA110-Como-funciona-a-pergunta-par%C3%A2metro-Filtra-Bco-Informado
---

**Dúvida**Como funciona a pergunta parâmetro "Filtra Bco Informado?"  
  
 **Ambiente**  
Microsiga Protheus – Financeiro – A partir da versão 11.80  
   
**Solução**

**Exemplo:**

Tenho os seguintes títulos e coloco os títulos no borderô X no banco agencia e conta  001 / 0001 / 0000001

Titulo A001 no valor R$ 1000,00

Titulo A002 no valor R$ 2000,00

Coloco os títulos no borderô Y no banco agencia e conta  002 / 0002 / 0000002

Titulo A003 no valor R$ 3000,00

Titulo A004 no valor R$ 4000,00

Ao inserir o banco 003 / 0003 / 0000003 para baixar todos os títulos no banco  003 / 0003 / 0000003

Se na pergunta parâmetro estiver com o conteúdo**Filtra Bco Informado?= SIM**

Cada título será baixado no banco que foi amarrado no borderô

**Exemplo:**

**E5\_BANCO**| **E5\_AGENCIA**| **E5\_CONTA** | **E5\_NUMERO** | **E5\_VALOR**

001|0001|000000001| A001 | 1000.00

001|0001|000000001| A002 | 2000.00

002|0002|000000002| A003 | 3000.00

002|0002|000000002| A004 | 4000.00

Se na pergunta parâmetro estiver com o conteúdo **Filtra Bco Informado?= NÃO**

Ao inserir o banco 003 / 0003 / 0000003 para baixar todos os títulos no banco  003 / 0003 / 0000003

Todos os títulos serão baixados no banco informado na rotina **FINA110**

**Exemplo:**

**E5\_BANCO** | **E5\_AGENCIA** | **E5\_CONTA** | **E5\_NUMERO** | **E5\_VALOR**

003|0003|000000003| A001 | 1000.00

003|0003|000000003| A002 | 2000.00

003|0003|000000003| A003 | 3000.00

003|0003|000000003| A004 | 4000.00
