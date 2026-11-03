---
article_id: 360026774631
category: Comércio Exterior - Easy Import Control - Tabelas
content_hash: 2b223759fff5121228355ee48634d43502f93d2bd1f65942148ab40ea06b0cc7
fetched_at: '2026-06-28T22:39:47.795142+00:00'
product: protheus
section_id: 1500001549562
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Redução de ICMS
type: support-article
updated_at: '2024-06-03T12:07:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026774631-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Redu%C3%A7%C3%A3o-de-ICMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21798922386583)Tempo aproximado para leitura: **00:05:00 min  
  
Dúvida**Como configurar redução de ICMS?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – *Easy Import Control* – A partir da versão 11.80  
  
**Solução**Essa é uma regra de diminuição de tributação que beneficia operações e prestações específicas, reduzindo em determinado percentual o valor que serve para base de cálculo do ICMS.  
  
**Utilizando Carga Tributária Equivalente****Exemplo:** Base de cálculo do ICMS cheia = R$ 200.000,00  
Percentual a tributar de 12% para 8,80% = 100 / 12% = 8,333333 x 8,80% = 73,333333  
Base de cálculo do ICMS cheia = R$ 200.000,00 x 73,333333% = Base reduzida = R$ 146.666,66 Valor do ICMS = R$ 146.666,66 x 12% = R$ 17.600,00   
  
**Comprovação do cálculo:**Para achar o valor do ICMS, basta multiplicar base cheia pela a carga tributária:   
R$ 200.000,00 x 8,80% = R$ 17.600,00   
Para achar a base de cálculo do ICMS, basta dividir o valor do ICMS pela alíquota da operação: R$ 17.600,00 / 12% = R$ 146.666,66  
  
**Aplicando o percentual de Redução na Base de Cálculo**   
Base de cálculo do ICMS cheia = RS 200.000,00   
Percentual de Redução de Base de Cálculo = 26,666666   
Valor de redução da base de cálculo= R$ 200.000,00 x 26,666666= R$ 53.333,33   
Base de cálculo do ICMS cheia = R$ 200.000,00 – R$ 53.340,00 = Base Reduzida = R$ 146.666,66   
Valor do ICMS = R$ 146.666,66 x 12% = R$ 17.600,00  
  
Para redução de ICMS é necessário ter no Cadastro de CFO uma operação de redução onde alguns campos precisam ser configurados em Atualizações \ tabelas \ C.F.O.:

O cadastro do CFO, determina a natureza de cada operação referente à circulação de bens ou mercadorias. Estas operações são utilizadas nas notas fiscais de entrada e devem ser configuradas com base na legislação vigente. Esta tabela tem uso obrigatório quando:

* Houver redução da base do ICMS;
* Uso de sistemas integrados
* Além da redução do ICMS o sistema permite colocar outra alíquota de ICMS para o cálculo do PIS e COFINS;
* Para os cenários de Conta e Ordem permitirá configurar se o IPI da Importação irá compor a base do ICMS na nota fiscal de transferência, através do campo IPI Imp. NFT(WZ\_BASENFT);
* Para os cenários de Conta e Ordem permitirá configurar se o IPI da própria nota de transferência irá compor a base do ICMS na nota fiscal de transferência através do campo IPI NFT Base(WZ\_IPINFT).
* Foi criado o campo B.C. ICMS que possibilita configurar como será realizada a redução da base de cálculo do ICMS:

**Regras para apuração da redução da base de cálculo do ICMS:**

**1-CTE:** Será utilizada a alíquota da carga tributária equivalente (campo "Carga Tr.Eq.") para apuração da base de cálculo inicial e para apuração do fator de redução, juntamente com a alíquota do ICMS, a ser aplicada sobre a base de cálculo inicial.

**Exemplo:** BC ICMS = Valor Mercadoria / (1-Carga Tr.Eq.) x (Carga Tr.Eq./ Alíq. ICMS).

**2-Red. BC:** Será utilizado o percentual de redução da base de cálculo (campo "Red. B.C.") para apuração da base reduzida.

**Exemplo:** BC ICMS = Valor Mercadoria/ (1-Alíq. ICMS) x Red. B.C.

**3-CTE + Red. BC:** Será utilizada a alíquota da carga tributária equivalente (campo "Carga Tr.Eq.") para apuração da base de cálculo inicial e será aplicado o percentual de redução da base de cálculo (campo "Red. B.C." - WZ\_RED\_ICM) para apuração da base de cálculo final.

**Exemplo:** BC ICMS = Valor Mercadoria / (1-Carga Tr.Eq.) x Red. B.C.

**4-CTE + Alíq. ICMS**: Será utilizada a alíquota do ICMS (campo "Alíq. ICMS") para apuração da base de cálculo inicial e a alíquota da carga tributária equivalente para apuração do fator de redução, juntamente com a alíquota do ICMS, a ser aplicada sobre a base de cálculo inicial.

**Exemplo:** BC ICMS = Valor Mercadoria / (1 - Alíq. ICMS) x (Carga Tr.Eq./ Alíq. ICMS).

5-Sem Redução

Exemplo: Utilizando Carga Tributária Equivalente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21799409739415)

**Observações gerais:**

* No cadastro de CFO deve-se usar a carga tributária equivalente ou a redução de ICMS, nunca os dois campos preenchidos juntos.
* Criado campo B.C. ICMS para realizar a configuração de redução de base de cálculo do  ICMS.
* Descontinuado o parâmetro MV\_EIC0029.

**Saiba mais:**

[C.F.O. (EICOP100 - SIGAEIC)](https://tdn.totvs.com/pages/releaseview.action?pageId=306858507)

[Criar campo configuração da redução da base do ICMS no cadastro de CFOP](https://tdn.totvs.com/pages/releaseview.action?pageId=725727891)
