---
article_id: 360017693291
category: Materiais - Compras (SIGACOM)
content_hash: c5a83cdee277689a0d23feeb2d3b48eb6ce085ea285da3708fbe8d2d4c1fcd57
fetched_at: '2026-06-28T22:41:18.666903+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - FORNECEDOR BLOQUEADO
type: support-article
updated_at: '2022-05-18T20:54:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017693291-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-FORNECEDOR-BLOQUEADO
---

**Ocorrência**

No módulo **Compras**, ao **Analisar Cotação**, caso o campo **A2\_MSBLQL** esteja em branco apresenta mensagem: "Impossível Analisar a Cotação, todos os Fornecedores listados estão bloqueados, por favor execute o desbloqueios de algum fornecedor para executar esta operação"

**Ambiente**

Protheus - Compras - A partir da versão 12.0.017

**Causa**

Essa mensagem ocorre quando o campo **A2\_MSBLQL** fica sem valor preenchido.

**Solução**

Quando o campo no Cadastro de Fornecedor **A2\_MSBLQL** estiver sem valor ao Analisar Cotação, não é possível concluir.

Após acessar a rotina MATA020 - Cadastro de Fornecedor,  **A2\_MSBLQL** modificando o Status para 2 - Não, o cadastro do Fornecedor não vai estar mais bloqueado, permitindo a liberação deste fornecedor.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
