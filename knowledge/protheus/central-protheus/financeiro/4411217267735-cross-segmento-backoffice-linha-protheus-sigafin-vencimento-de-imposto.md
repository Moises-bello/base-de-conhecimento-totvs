---
article_id: 4411217267735
category: Financeiro
content_hash: 321a6aa4eed83e166fac8477fa77d9d2c16d75713ac71272c85eaaa0e84fd5c7
fetched_at: '2026-06-28T22:38:01.033351+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAFIN  -  Vencimento de imposto
type: support-article
updated_at: '2025-09-12T12:52:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411217267735-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Vencimento-de-imposto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32565365292567) Tempo aproximado para leitura: **00:05:00**

**Dúvida**Quais os principais parâmetros para calcular a data de vencimento dos impostos do financeiro (PCC, INSS, ISS, IR)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Solução**

**Parâmetros que definem a data de vencimento do PCC:**

O vencimento dos impostos referentes ao PCC varia conforme o momento da retenção:

**Retenção na Emissão do Título:** vencimento do imposto no dia 20 do mês seguinte ao vencimento do título.

**Retenção na Baixa do Título:** vencimento no dia 20 do mês seguinte à data de baixa.

**MV\_BX10925**: Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. (Contas à Pagar)

**MV\_BR10925**: Define o momento do tratamento da retenção dos impostos PIS COFINS e CSLL. (Contas à Receber)

**Para mais detalhes sobre o imposto, acesse:**[Retenção\_ de\_ PIS\_ COFINS\_ CSLL](http://tdn.totvs.com/pages/releaseview.action?pageId=6076816)  
  
**Importante:**

Os parâmetros **MV\_BX10925 e MV\_BR10925** **não deve ser alterados, uma vez que no momento da implantação do *Protheus*, foi definido como a empresa irá tratar o imposto.**

**Parâmetros que definem a data de vencimento do INSS:**

**MV\_MP447**: Indica se o vencimento de IRRF e INSS deve ser calculado segundo a Medida Provisória 447.

**MV\_VENCINS**: Parametrização do cálculo do vencimento dos títulos de INSS.

**MV\_INSBXCP**: Define momento do tratamento da retenção do imposto INSS.

**Para mais detalhes sobre o imposto, acesse:**[INSS - Configurações para Retenção de INSS](https://tdn.totvs.com/pages/releaseview.action?pageId=697252452)  
  
**Parâmetros que definem a data de vencimento do IR:**

**MV\_MP447**: Indica se o vencimento de IRRF e INSS deve ser calculado segundo a Medida Provisória 447.

**MV\_VENCIRF**: Indica se o título de IRRF será gerado a partir da data de (E)emissão, (V)vencimento ou (C)contabilização.

**MV\_VC11196**: Determina se fará o cálculo de data dos impostos IRRF, PIS, COFINS, CSLL conforme Lei 11196.

**Para mais detalhes sobre o imposto, acesse:**[IRRF - Retenção de Imposto de Renda Pessoa Jurídica ou Física](https://tdn.totvs.com.br/pages/releaseview.action?pageId=531009057)

Observação: É verificado se o IR é calculado na emissão ou na baixa através do cadastro do cliente e do fornecedor

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411211171095)

**Parâmetros que definem a data de vencimento do ISS:**

**MV\_VENCISS**: Define o tipo de vencimento de ISS. As opções validadas são: E=Emissão; Q=Quinzenal/Emissão; V=Vencimento.

**MV\_MRETISS**: Modo de retenção do ISS nas aquisições de serviços. Conteúdo 1 = na emissão do titulo principal. 2 = na baixa do título principal.

**MV\_DIAISS**: Dia padrão para gerar os títulos de ISS.

**Importante**

Se houver necessidade de outro tipo de alteração no vencimento, isso poderá ser feito por meio do ponto de entrada ***F050MDVC***. Esse ponto de entrada permite que o cliente defina sua própria data de vencimento para os impostos.  
[F050MDVC - Cálculo da data de vencimento de impostos](https://tdn.totvs.com/pages/releaseview.action?pageId=6070892)  
  
**Saiba mais**[Retenção\_de\_ISS](https://tdn.totvs.com/pages/releaseview.action?pageId=6076798)
