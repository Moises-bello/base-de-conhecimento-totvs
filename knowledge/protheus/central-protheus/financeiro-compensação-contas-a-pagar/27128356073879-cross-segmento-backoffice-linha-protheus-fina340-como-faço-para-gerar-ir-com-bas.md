---
article_id: 27128356073879
category: Financeiro - Compensação Contas a Pagar
content_hash: a9459dbfd7b1f7a487f7cbe4d227620630e7311b30ced48f32b80da821f5d377
fetched_at: '2026-06-28T22:37:33.630136+00:00'
product: protheus
section_id: 35057559197335
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - FINA340 - Como faço para gerar
  IR com base no saldo de um NF, onde essa NF já teve o seu saldo consumido por uma
  compensação de um tipo:PA
type: support-article
updated_at: '2026-03-04T17:49:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27128356073879-Cross-Segmento-Backoffice-Linha-Protheus-FINA340-Como-fa%C3%A7o-para-gerar-IR-com-base-no-saldo-de-um-NF-onde-essa-NF-j%C3%A1-teve-o-seu-saldo-consumido-por-uma-compensa%C3%A7%C3%A3o-de-um-tipo-PA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27128356067479) Tempo aproximado para leitura: **00:10 min**  
  
**Dúvida**  
Como faço para gerar IR com base no saldo de uma NF, onde essa NF já teve o seu saldo consumido por uma compensação de um tipo: PA?

**Ambiente**  
Cross Segmento - TOTVS Backoffice Linha Protheus - Financeiro - FINA340 - Todas as versões.  
  
**Solução**

Para esse processo, temos como premissa a regra de cumulatividade, seja mensal ou diária.

Lembrando que variam dependendo do tipo de prestação de serviços e da estrutura tributária escolhida (Simples Nacional, Lucro Presumido, etc.).

Para calcular o **IR pessoa física** com a dedução da tabela simplificada, realize as seguintes parametrizações:

1. Considere a **tabela progressiva do IRRF** com valores vigentes do ano de 2024.

Acesse pelo **Configurador (SIGACFG > Ambiente > Cadastros > Tabela IRRF).**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27128311632023)**

2. Configure através do **Configurador (SIGACFG)** os parâmetros da dedução simplificada e da compensação de **PA (FINA340)**:

**MV\_FMP1171=.T.**

**MV\_FVL1171=564,80**

**Configurar o fornecedor para geração do IRPF na baixa do título.**

**CENÁRIO  A**

**MV\_PABRUTO=2**

**MV\_COMPCP=.T.**

**MV\_BP10925=2**

**MV\_PAPRIME=1**

 - **FINA050** 10/2024 incluir um título tipo: **PA** no valor de R$ 10.000,00 com a retenção do IRPF, e será gerado um título tipo: TX de R$ 1.698,68 e o valor líquido do **tipo: PA** será de R$ 8.301.32

 - **FINA050** 10/2024 incluir um título do **tipo: NF** no valor de R$ 20.000,00 parametrizado também para gerar o **IRPF** no momento da baixa.

 - **FINA340** 10/2024 compensar o tipo: NF com o tipo **PA** de R$ 10.000,00.

- **FINA080** **10/2024,** realizar a baixa do saldo do título do **tipo: NF** de R$ 10.000,00, e calcular a **retenção do IRPF** no valor de **R$ 2.700,00.**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/27128311633815)](https://centraldeatendimento.totvs.com/hc/article_attachments/27128311633815)

**Cálculo**

**NF.** R$ 20.000,00 / **IRRF** = R$ 4.448,68

**IRRF** do **PA** = R$ 1.698,68

**IRRF** sobre o saldo da nota sem desconto simplificado (10.000,00) = R$ 2.750,00.

Soma: 1.698,68 + 2.750,00 = R$ 4.448,68

**Importante**  
Neste cenário, gerou um tipo: **TX** referente ao tipo **IRPF** no valor de R$ 2750,00, pois ocorreu a cumulatividade, já que as ações ocorreram tudo dentro do mesmo mês.

**Exemplo 2**  
Como faço para gerar **IRPF** com base no saldo de uma **NF** que seria R$ 10.000,00, ao invés de gerar o **IRPF** com base no valor total R$ 20.000,00?

**CENÁRIO B**

**MV\_PABRUTO=2**

**MV\_COMPCP=.T.**

**MV\_BP10925=2**

**MV\_PAPRIME=1**

* **FINA050** 10/2024 incluir um título tipo: **PA** no valor de R$ 10.000,00 com a **retenção do IRPF**, e será gerado um título **tipo: TX** de R$ 1.698,68 e o valor líquido do tipo: **PA** será de R$ 8.301,32.
* FINA050 10/2024 incluir um título do tipo: NF no valor de R$ 20.000,00 parametrizado também para gerar o **IRPF** no momento da baixa.
* **FINA340** 10/2024 compensar o tipo:NF com o tipo **PA** de R$ 10.000,00.
* **FINA080** **11/2024**, pela rotina **FINA080 - Baixas a pagar manual,, é feita** a baixa do restante do saldo do tipo: **NF** de R$ 10.000,00 com a **retenção do IRPF** e o valor será de **R$ 1.698,68.**

[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27128311632535)**](https://centraldeatendimento.totvs.com/hc/article_attachments/27128311632535)

**Cálculo**

**NF.** R$ 20.000,00 /  IRRF total =R$ 3.397,36

**IRRF** do **PA** (10.000,00) = R$ 1.698,68

**IRRF** sobre o saldo da nota com desconto simplificado (10.000,00) = R$ 1.698,68

Soma: 1.698,68 + 1.698,68 = R$ 3.397,36

**IRRF com desconto simplificado.**[**![](https://centraldeatendimento.totvs.com/hc/article_attachments/27128356069399)**](https://centraldeatendimento.totvs.com/hc/article_attachments/27128356069399)

**Explicação da Solução:**

Foi gerado um **IRPF** no valor de **R$ 1.698,68** ao invés de **R$ 2.700,00, pois** a baixa do saldo do título tipo: **NF** realizado pela rotina **FINA080** **- Baixa manual a pagar** ocorreu em um mês diferente da inclusão do tipo: **PA**, e não houve cumulatividade do **IRPF** dentro do mesmo mês.

**Saiba mais**

[Tabela Progressiva IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=695202577)

[IRRF Dedução Simplificada (MP 1.171/2023)](https://tdn.totvs.com/pages/releaseview.action?pageId=773900973)

[Compensação de PA com impostos distintos (FINA340)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019492591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-utilizados-na-Compensa%C3%A7%C3%A3o)

[Configuração dos parâmetros compensação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019492591-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA340-Configura%C3%A7%C3%A3o-dos-par%C3%A2metros-utilizados-na-Compensa%C3%A7%C3%A3o)

#
