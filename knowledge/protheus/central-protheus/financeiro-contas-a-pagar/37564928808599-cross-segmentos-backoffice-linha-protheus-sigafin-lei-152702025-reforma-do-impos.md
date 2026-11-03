---
article_id: 37564928808599
category: Financeiro - Contas a Pagar
content_hash: 0aeb808357b2ffc4ca04a27e84e3a5800f79646d7bc875cd46a1946f19cf76a5
fetched_at: '2026-06-28T22:38:09.772904+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Lei 15.270/2025 - Reforma
  do Imposto de Renda 2026 para titulo com o origem do modulo Financeiro
type: support-article
updated_at: '2026-03-26T16:41:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37564928808599-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Lei-15-270-2025-Reforma-do-Imposto-de-Renda-2026-para-titulo-com-o-origem-do-modulo-Financeiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37564968128535) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
Lei 15.270/2025 - Reforma do Imposto de Renda **2026** como será tratado com registro de **origem no modulo Financeiro** ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Visão geral**  
A **Lei 15.270/2025**promove uma ampla **reestruturação**no**Imposto de Renda da Pessoa Física (IRPF)**. A partir de **1º** **de janeiro de 2026** passam a vigorar as novas regras, que estabelecem:

* **Redução** do imposto para quem recebe até **R$ 5.000,00 mensais**;
  + **Redução**do imposto para quem recebe entre **R$ 5.000,01 e R$ 7.350,00**. O valor a deduzir sobre o imposto já apurado conforme a tabela vigente do IRRF deverá ser calculado pela seguinte fórmula:
    - R$ 978,62 – (0,133145 × rendimentos tributáveis sujeitos à incidência mensal);

* Tributação de 10% sobre a distribuição de **lucros e dividendos**, para valores que excederem R$ 50 mil por beneficiário/fornecedor;

**Parametrização via legado**  
**Isenção/Redução do imposto de renda**

**Importante:**  Essa parametrização não é valida para cenários onde a origem do título a pagar é o Documento de Entrada (MATA103) e o tributo configurado com fato **gerador competência**

Para parametrizar o modulo Financeiro **SIGAFIN** com as mudanças sobre isenção/redução sobre o imposto de renda de pessoa física **IRPF**, realize os passos a seguir:

**1.** Configure as faixas da tabela progressiva do **IRRF** com os valores vigentes: [IRRF - Tabela Progressiva de Cálculo de Imposto de Renda Pessoa Física](https://tdn.totvs.com/pages/viewpage.action?pageId=695202577)

**2.** Através do Configurador **SIGACFG** podem ser ajustadas algumas configurações através dos parâmetros (**SX6**),**mas há essa necessidade de ajuste somente em caso de futuras mudanças envolvendo essa legislação,** caso contrário não há necessidade de cria-los ou altera-los. Para mais informações, consulte: [Utilização dos parâmetros MV\_F15270A, MV\_F15270B, MV\_F15270C, MV\_F15270D e MV\_F15270E](https://tdn.totvs.com/pages/viewpage.action?pageId=1027818954)  
  
Seguem abaixo os parâmetros:

* **MV\_F15270A = 5000** (Valor máximo do rendimento para entrar na 1ª faixa de desconto)
* **MV\_F15270B = 7350** (Valor máximo do rendimento para entrar na 2ª faixa de desconto)
* **MV\_F15270C = 312.89** (Valor máximo de desconto da 1ª faixa)
* **MV\_F15270D = 978.62** (Valor máximo de desconto da 2ª faixa)
* **MV\_F15270E = 0.133145** (Fator para cálculo da redução da 2ª faixa)

**Importante:** Os valores de cada faixa não têm relação com o **desconto simplificado**. Esses valores representam um **redutor** previsto em Lei. Ou seja, independentemente da configuração do parâmetro **MV\_FMP1171**, o sistema irá calcular o valor das faixas. Essa orientação está publicada no Portal TDN, no item 4.1: [Orientações Consultoria de Segmentos - Novo Cálculo do IRRF](https://tdn.totvs.com/pages/viewpage.action?pageId=1019343450)  
  
**3.**Caso o calculo do **IRPF** tenha que ser realizado considerando a dedução simplificada (**MP 1.171/2023**), verifique as configurações necessárias no link a seguir: [IRRF de autônomo com dedução simplificada (MP 1.171/2023)](https://tdn.totvs.com/pages/viewpage.action?pageId=773900973);

**4.** Verifique se a data do fato gerador do **IRRF** está dentro da vigência da lei (a partir de 01/01/2026);

a. Caso o fato gerador seja pela competência/emissão (**A2\_CALCIRF = 1**), verifique se o título possui data de emissão (**E2\_EMISSAO**) igual ou superior a **01/01/2026**;

b. Caso o fato gerador seja pelo regime de caixa/pagamento (**A2\_CALCIRF = 2**), verifique se o título possui data de baixa (**E5\_DATA/FK2\_DATA**) igual ou superior a **01/01/2026**;

**Solução**

**1.** Necessário o ambiente estar com os patchs de atualização segue os links;   
  
12.1.2210:<https://r.totvs.io/p/1233206> ;   
12.1.2310:<https://r.totvs.io/p/1233207> ;   
12.1.2410:<https://r.totvs.io/p/1233208> ;   
12.1.2510:<https://r.totvs.io/p/1233205> ;

**Saiba mais:**  
[Lei 15.270/2025 - Reforma do Imposto de Renda 2026](https://tdn.totvs.com/pages/viewpage.action?pageId=1027817283)  
<https://www.totvs.com/blog/fiscal-clientes/nova-lei-do-irpf-reducao-para-baixa-renda-e-tributacao-minima-para-altas-rendas/>

[Cálculo de IRRF para fornecedor pessoa física s/ tabela progressiva (ED\_JURCAP)](https://tdn.totvs.com/pages/viewpage.action?pageId=756477961)

[IRRF de autônomo com dedução simplificada (MP 1.171/2023)](https://tdn.totvs.com/pages/viewpage.action?pageId=773900973)

[IRRF - Tabela Progressiva de Cálculo de Imposto de Renda Pessoa Física](https://tdn.totvs.com/pages/viewpage.action?pageId=695202577)

[Utilização dos parâmetros MV\_F15270A, MV\_F15270B, MV\_F15270C, MV\_F15270D e MV\_F15270E](https://tdn.totvs.com/pages/viewpage.action?pageId=1027818954)
