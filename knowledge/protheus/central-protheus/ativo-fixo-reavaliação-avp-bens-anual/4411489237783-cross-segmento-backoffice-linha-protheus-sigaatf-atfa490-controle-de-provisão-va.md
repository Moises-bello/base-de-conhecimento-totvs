---
article_id: 4411489237783
category: Ativo Fixo - Reavaliação AVP, BENS, ANUAL
content_hash: 7d7d8bf869ea34de70445a27b3df23bd2e93c1555c2fa508cca91b1c174cc826
fetched_at: '2026-06-28T22:41:45.433059+00:00'
product: protheus
section_id: 1500001536361
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA490 - Controle de
  Provisão Valor Presente (AVP)
type: support-article
updated_at: '2021-12-06T13:04:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411489237783-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA490-Controle-de-Provis%C3%A3o-Valor-Presente-AVP
---

**Dúvida**Controle de Provisão Valor Presente (AVP) no ativo fixo  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - Ativo Fixo - Todas as versões  
  
**Solução**

FINA017- cadastro de Índices Financeiros  
Período= Mensal  
![](https://totvssuporte.zendesk.com/attachments/token/FVziJJfTdemI0cjRVVQMCYM40/?name=inline-1261292800.png)​  
  
FINA018- Atualização de Índices.  
![](https://totvssuporte.zendesk.com/attachments/token/1u3JHFCy4Lmmoq9Eif6CUtbsd/?name=inline-1305350234.png)

ATFA490- Controle de Provisão.  
No cadastro de provisão relacionamos o índices AVP, cadastrado no financeiro.  
Tipo de calculo= 1 curva de demanda  
No campo VALOR BRUTO informamos o valor BRUTO do BEM e o sistema calcula o VALOR PRESENTE automaticamente da seguinte forma:  
Valor Presente =Valor Bruto /( taxa diária ^ Quantidade de Dias da Provisão)  
A quantidade de dias da provisão é a quantidade de meses entre o inicio da provisão e a data fim do  
item de provisão multiplicado por 30.

![](https://totvssuporte.zendesk.com/attachments/token/zhuK1QBxzqbKI0YphDwJ1t8yS/?name=inline1925723797.png)

. Tabelas utilizadas

* FNU e FNV Controle de Provisão
* FIT    Cadastro de Índice Financeiro
* FIU   Atualização de Índices

**Saiba Mais**

[ATFA490 - Exemplo de utilização, Controle de Provisão Valor Presente (AVP)](https://tdn.totvs.com/pages/releaseview.action?pageId=561068794)

[Configuração de Lançamento Padrão 881 - Movimentos de provisão](https://tdn.totvs.com/pages/releaseview.action?pageId=589517933)

[ATFA490 - Controle de Provisão](https://tdn.totvs.com/pages/releaseview.action?pageId=312160000)

[ATFA490 - SIGAATF](https://tdn.totvs.com/pages/releaseview.action?pageId=312160678)

[DEPRECIAÇÃO POR CURVA DE DEMANDA - ICPC 01 - Contratos de Concessão (IFRIC 12)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015070772-MP-SIGAATF-DEPRECIA%C3%87%C3%83O-POR-CURVA-DE-DEMANDA-ICPC-01-Contratos-de-Concess%C3%A3o-IFRIC-12-?source=search)

[ATFA430 - Projeto Imobilizado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411566751127-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA430-Projeto-Imobilizado?source=search)

<https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa440_aprovacao_alteracao_avp_imobilizados.htm>

<https://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/atfa440_revisar_avp.htm>
