---
article_id: 360004971371
category: Materiais - Compras (SIGACOM)
content_hash: 3fa490413d48828bf2990423fa7bae01f91b9bdfc45dbc551fed07ee8e10d8e2
fetched_at: '2026-06-28T22:41:10.107658+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O que fazer quando
  ocorre os Alertas A410UNIDIF / A100VALOR / A410TOTAL nos processos de nota fiscal
  ?
type: support-article
updated_at: '2021-12-06T17:30:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004971371-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-que-fazer-quando-ocorre-os-Alertas-A410UNIDIF-A100VALOR-A410TOTAL-nos-processos-de-nota-fiscal
---

**Dúvida**O que fazer quando ocorre os Alertas A410UNIDIF / A100VALOR / A410TOTAL nos processos de nota fiscal ?

**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**Quando gera um destes Alertas por exemplo o A410UNIDIF a princípio validar os seguintes campos referente ao tamanho e casas decimais:

**1º)** Os principais campos de QUANTIDADE relacionados devem possui o mesmo X3\_TAMANHO, X3\_DECIMAL e X3\_PICTURE: D1\_QUANT, D2\_QUANT, C6\_QTDVEN, C6QTDLIB e C9\_QTDLIB. Caso não possuírem as mesmas propriedades alterar para padronizar.

**2º)** Os principais campos de VALOR UNITÁRIO relacionados devem possui o mesmo X3\_TAMANHO, X3\_DECIMAL e X3\_PICTURE: D1\_VUNIT, D2\_PRCVEN, D2\_PRUNIT, C6\_PRCVEN, C6\_PRUNIT e C9\_PRCVEN. Caso não possuírem as mesmas propriedades alterar para padronizar.

**3º)** Os principais campos de VALOR TOTAL relacionados devem possui o mesmo X3\_TAMANHO, X3\_DECIMAL e X3\_PICTURE: D1\_TOTAL, D2\_TOTAL e C6\_VALOR. Caso não possuírem as mesmas propriedades alterar para padronizar sendo o padrão indicado tamanho 2.

4º) Após executar as verificações anteriores e ter executado as possível correções, tentar novamente realizar o retorno da NF.

Para a mensagem A410UNIDIF numa possível situação de retorno de nota de venda, o procedimento acima resolve.

Para maiores informações referente a outros campos de faturamento, estoque entre outros referente a casas decimais, poderá validar através do link do TDN com o documento completo:

[Aumento de Casas Decimais](http://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)

**Observação:**

Pode ser utilizado o parâmetro MV\_VLDPDEV para que a validação da devolução seja feita pelo Saldo ou Valor Unitário:  
![](https://totvssuporte.zendesk.com/attachments/token/Rq0DM8mzH6XfEMKewyeojeuYd/?name=inline-617330613.png)

***Saiba Mais :***

[Aumento de Casas Decimais](http://tdn.totvs.com/display/public/PROT/FAT0068_Aumento_de_Casas_Decimais_no_ambiente_Faturamento_SIGAFAT)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
