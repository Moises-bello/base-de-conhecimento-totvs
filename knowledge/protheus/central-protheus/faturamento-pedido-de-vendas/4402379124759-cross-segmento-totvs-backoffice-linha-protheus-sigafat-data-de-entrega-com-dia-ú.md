---
article_id: 4402379124759
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 1702618e43ff6309df22817cc990b847a44d1506403bc428e832f26013286f19
fetched_at: '2026-06-28T22:38:38.506356+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Data de Entrega
  com Dia Útil
type: support-article
updated_at: '2022-05-11T17:42:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4402379124759-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Data-de-Entrega-com-Dia-%C3%9Atil
---

**Duvida**Como gerar a data de entrega no pedido de vendas para o próximo dia útil?  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Solução**

A data de entrega é automaticamente preenchida com a **data base** do sistema, ao alterar a mesma sendo inferior ou superior à emissão do pedido não haverá alteração nos vencimentos da duplicata, já a planilha financeira será baseada na data gravada no campo **c5\_emissao**, e ao faturar o pedido, o sistema irá gravar a data da Emissão da Nota Fiscal, sendo que este comportamento é Padrão e não opcional no sistema.  
Quando realizar a **cópia** de um pedido de vendas, considerar o parâmetro **MV\_TIPCPDT** para ajustar o Preenchimento da Data de Entrega ( **C6\_ENTREG**) na Cópia do Pedido de Venda.

Por padrão o campo **C5\_FECENT** (**Dt. entrega**), não possui uma validação, ou seja, este campo é preenchido de forma manual, a não ser que crie uma validação personalizada para ele, já o campo **C6\_ENTREG** tem validações e pega a informação da data base do sistema.

**Saiba Mais**Documentação do parâmetro citado acima:  
**[MV\_TIPCPDT - Preenchimento da Data de Entrega na Cópia do Pedido de Venda](https://tdn.totvs.com/pages/viewpage.action?pageId=59441683)**

Documentação onde consta a informação de data entrega para apoio:  
**<https://tdn.totvs.com/pages/releaseview.action?pageId=240310845>**

```
Pontos de Entrada para auxiliar na customização  
  
MTA410 - Validação de toda a tela no Pedido de Venda: https://tdn.totvs.com/pages/viewpage.action?pageId=6784388  
MTA410I - Gravação do pedido: https://tdn.totvs.com/display/PROT/MTA410I  
MT410TOK - Validar confirmação da operação: https://tdn.totvs.com/pages/viewpage.action?pageId=6784353
```
