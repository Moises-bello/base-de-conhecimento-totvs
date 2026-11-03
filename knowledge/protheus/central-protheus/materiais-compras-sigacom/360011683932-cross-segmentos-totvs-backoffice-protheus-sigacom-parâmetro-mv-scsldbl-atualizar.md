---
article_id: 360011683932
category: Materiais - Compras (SIGACOM)
content_hash: fd7d13139a39660b9f327ede84306ef8aaeae6fa6304f7d2fc7f297ed0053008
fetched_at: '2026-06-28T22:41:10.144484+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetro MV_SCSLDBL
  - Atualizar Quantidade Entrada Prevista do Produto ao liberar Solicitação de Compras
type: support-article
updated_at: '2021-12-15T11:45:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011683932-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metro-MV-SCSLDBL-Atualizar-Quantidade-Entrada-Prevista-do-Produto-ao-liberar-Solicita%C3%A7%C3%A3o-de-Compras
---

**Dúvida**Parâmetro MV\_SCSLDBL – Atualizar Quantidade Entrada Prevista do Produto ao liberar Solicitação de Compras  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Realizada melhoria na rotina de Solicitação de Compras (MATA110) com a criação do parâmetro MV\_SCSLDBL que possibilita a atualização do campo Qtd. Prevista (B2\_SALPEDI) somente quando a solicitação de compras estiver liberada.

**Procedimentos para Configuração**  
1. No Configurador (SIGACFG), acesse Ambientes / Cadastros / Parâmetros (CFGX017). Crie e/ou altere o parâmetro a seguir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008581791/mceclip0.png)

**Procedimentos para Utilização**  
1. No módulo Configurador (SIGACFG), acesse Ambiente / Cadastro / Parâmetros (CFGX017) e ajuste o conteúdo do parâmetro MV\_SCSLDBL com o valor .T.  
2. No módulo de Compras (SIGACOM) acesse Atualizações / Solicitar/Cotar / Solicitação de Compras (MATA110). Ao gerar uma solicitação de compras bloqueada, o campo Qtd. Prevista (B2\_SALPEDI) não será atualizado.  
3. Ao liberar a solicitação de compras, é feita a atualização do campo Qtd. Prevista (B2\_SALPEDI)

**Informações Técnicas  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/360008546132/mceclip1.png)**

**Importante:**  
Antes de ativar o parâmetro, todas as solicitações de compra pendentes de aprovação devem ser liberadas para não resultar em duplicidade no conteúdo do campo Qtd. Prevista (B2\_SALPEDI).

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
