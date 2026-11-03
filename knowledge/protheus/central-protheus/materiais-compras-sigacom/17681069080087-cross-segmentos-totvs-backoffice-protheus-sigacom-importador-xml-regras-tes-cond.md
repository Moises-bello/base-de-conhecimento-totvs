---
article_id: 17681069080087
category: Materiais - Compras (SIGACOM)
content_hash: 543948325d7460c43d1b0c6d0f4c90d118350b94b3f3df3eb836c738a2c1a661
fetched_at: '2026-06-28T22:41:19.942976+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Importador XML - Regras
  TES / Condição de pagamento
type: support-article
updated_at: '2026-03-03T14:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17681069080087-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Importador-XML-Regras-TES-Condi%C3%A7%C3%A3o-de-pagamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17681101124247) Tempo aproximado para leitura: **00:03:SS min**  
  
**Dúvida**

Como é feita a busca pelas informações de TES e condição de pagamento durante o processo de geração do documento a partir do monitor ?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - VERSÃO 12

**Solução**

## TES:

Quando configurado para geração automática para documento classificado ( **MV\_COMCOL1 = 2 ou MV\_CTECLAS = .T.** ) , ao gerar documento será utilizado o campo D1\_TES.

Quando configurado para geração automática para documento a classificar ( **MV\_COMCOL1 = 1** ), ao gerar documento será utilizado o campo D1\_TESACLA

Quando configurado ( **MV\_COMCOL1 = 0** ), utilizar parâmetro **MV\_COLTEG** para definir campo ( **T = D1\_TES / F = D1\_TESACLA** )

Quando o parâmetro **MV\_COLTEG** estiver configurado como **T**, **toda geração de documento será interpretado como uma geração de documento classificado** e dependendo da regra por documento pode ser apresentado alguma inconsistência na geração, pois não foi encontrada nenhuma TES, caso queria que **NÃO** seja apresentada essa inconsistência ao não encontrar a TES e sim gerar uma pre-nota, deve-se configurar o parâmetro **MV\_ERRCTEG** como **T,** assim o documento não apresentara inconsistência de TES e gera documento como pre-nota.

**Obs: Se o campo DT\_TES estiver preenchido, vai automaticamente para o campo D1\_TES independente de como estiver configurado o parâmetro MV\_COLTEG.**

## Condição de pagamento:

**Como é feita a busca pela Condição de Pagamento?**

Se for complemento de frete:

1. Busca se há informação na origem (NF Origem / Série Origem / Item Origem).
2. Busca no parâmetro (MV\_XMLCPCT).
3. Utiliza o ponto de entrada A140ICOND.

Artigo Ponto de Entrada A140ICOND :  [A140ICOND - Ponto que permite alterar e validar a condição de pagamento no monitor do Totvs Colaboração.](https://tdn.totvs.com.br/pages/releaseview.action?pageId=505755731)

Vídeo na Integra sobre o Ponto de Entrada A140ICOND: [Aqui !!](https://centraldeatendimento.totvs.com/hc/pt-br/articles/22836290927511-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Ponto-de-Entrada-A140ICOND)

***Saiba Mais:***

[IX08004 - Importador XML - Regras TES / CFOP(Config.Tributos) / Condição de pagamento](https://tdn.totvs.com.br/pages/releaseview.action?pageId=546695598#tabs-ID2)

[TC07010 - Totvs Colaboração - Regras TES / Condição de pagamento](https://tdn.totvs.com/pages/releaseview.action?pageId=546695574)

[Cross Segmento - Backoffice (Linha Protheus) - SIGACOM - Integração Importador XML x TOTVS Transmite](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7557934491159-Cross-Segmento-Backoffice-Linha-Protheus-SIGACOM-Integra%C3%A7%C3%A3o-Importador-XML-x-TOTVS-Transmite)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
