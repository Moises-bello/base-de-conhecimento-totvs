---
article_id: 28388090865303
category: Materiais - Compras (SIGACOM)
content_hash: d97a7e9ca9ebdbc1e8242f4f627e5894c5a80daa5b4cbd1c16befa4bc3a74272
fetched_at: '2026-06-28T22:41:11.842322+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Contabilização - Não permite sair da
  Linha e não conclui o Lançamento
type: support-article
updated_at: '2024-12-09T18:25:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28388090865303-Cross-Segmentos-Backoffice-Protheus-Contabiliza%C3%A7%C3%A3o-N%C3%A3o-permite-sair-da-Linha-e-n%C3%A3o-conclui-o-Lan%C3%A7amento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28388102302743) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**

Ao incluir a Nota Fiscal com Contabilização On-Line, a tela de Lançamentos Contábeis é aberta, mas não é possível sair da linha de lançamento e o processo de lançamento não é concluído  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Gestão de Compras - Versão 12

**Solução**

Essa ocorrência ocorre quando falta alguma informação obrigatória, como Centro de Custo, Item Contábil ou Classe de Valor, e o parâmetro **MV\_CT105MS** responsável por definir se a mensagem de erro será acionada está desabilitado.

Vale ressaltar que a validação do parâmetro **MV\_CT105MS** só é ativada quando o parâmetro **MV\_ALTLCTO** está configurado com o valor **"S"**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/28388090835479)**

***Saiba Mais***

[Lançamentos Padronizados do Documento de Entrada MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017681331-Cross-segmentos-Totvs-Backoffice-Protheus-SIGACOM-Lan%C3%A7amentos-Padronizados-do-Documento-de-Entrada-MATA103)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
