---
article_id: 38714800109463
category: Escrita Fiscal - Configurador de Tributos
content_hash: 071195f29828edfb0c21a2a88dbca1f2355c371512f6956c1c8964e64badf9d4
fetched_at: '2026-06-28T22:39:17.663030+00:00'
product: protheus
section_id: 26791332087191
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - FISA170 - Cálculo
  de IRRF utilizando a tabela progressiva, com desconto simplificado ou desconto normal
type: support-article
updated_at: '2026-03-05T13:05:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38714800109463-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-FISA170-C%C3%A1lculo-de-IRRF-utilizando-a-tabela-progressiva-com-desconto-simplificado-ou-desconto-normal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814720279) Tempo aproximado para leitura: **15:00 min**  
  
**Dúvida**  
Como realizar o cálculo do IRRF considerando a nova tabela progressiva vigente a partir de 2026 no Protheus?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - FIS - a partir da 12.1.2210  
  
**Solução**  
[Exemplo:  
Para que o cálculo do IRRF seja efetuado corretamente conforme a nova tabela progressiva de 2026, é necessário atualizar o ambiente e realizar a configuração através da rotina **FISA170 – Configurador de Tributos**.

### **1. Atualizações obrigatórias antes da aplicação do patch**

Antes de aplicar o patch correspondente à sua versão, é imprescindível realizar as seguintes atualizações:

* Atualização da **Expedição Contínua do Fiscal**
* Atualização da **LIB**
* Atualização do **Dicionário de Dados**
* Aplicação do **Pacote Acumulado Fiscal**
* Execução da rotina **UPDDISTR**

📌 Link do Pacote Acumulado Fiscal:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=525823851>

### **2. Aplicação do Patch por Versão**

Aplicar o patch correspondente à sua release:

* **12.1.2210** → <https://r.totvs.io/p/1239183>
* **12.1.2310** → <https://r.totvs.io/p/1239180>
* **12.1.2410** → <https://r.totvs.io/p/1239181>
* **12.1.2510** → <https://r.totvs.io/p/1239182>

**3. Configuração a ser realizada**

3.1 Tabela progressiva

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800086423)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38822770998935)

3.2 Dedução de dependente

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800087319)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814724631)

Deve ser cadastrado o valor unitário por dependente, para que na execução da regra de cálculo, a rotina multiplique o valor pela quantidade de dependentes informado no cadastro de fornecedor (A2\_NUMDEP na tabela SA2).

3.3 Regra de Base de Cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814724887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814725271)

3.4 Rendimento tributável

1. Regra de Alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814729623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814730519)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800096023)

  2. Regra de Cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800096535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814733079)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800096919)

**Com a regra de cálculo do rendimento tributável criada, agora podemos criar as regras do IRRF em si.**

3.5 Regra de Base de Cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814724887)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814733591)

* **VAL:RENDME**: Valor do rendimento tributável do item do documento (nome do operando vai ser de acordo com qual o código da **regra de cálculo do Rendimento Tributado** que foi criada, nesse exemplo criamos ela no passo anterior como "**RENDME"**).

3.6 Regra de Base de Cálculo (Descontando outros imposto/deduções)

Se houver a necessidade de efetuar descontos de certos impostos na Base de Cálculo, como por exemplo descontar o INSS na Base do IRRF, isso pode ser feito durante a edição da fórmula.  
Basta selecionar no campo **Tipo de Regras a ser consultada** a opção **05 - Regras de Tributo.**

No campo **Tributo para filtrar a consulta** selecionar o imposto que deseja descontar da Base de Cálculo que está sendo configurada e por fim selecionar o operando daquele imposto que deve ser subtraído.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814733847)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814734231)

3.7 Regra de Alíquota

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814729623)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800097303)

3.8 Regra de Escrituração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800092439)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814727703)

3.9 Regra de Cálculo

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800096535)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714929916055)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800097687)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814734871)

Exemplos de cálculo:

Nota com o valor de R$ 5.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714800101655)

Nota com o valor de R$ 6.000,00:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714814735767)

Para a criação de títulos no Contas a Pagar, deve ser vinculada uma Regra Financeira.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38714902834711)

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FISA170 - Cumulatividade do imposto IRRF com a regra financeira para o contas a receber e pagar](https://centraldeatendimento.totvs.com/hc/pt-br/articles/35870209956631-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FISA170-Cumulatividade-do-imposto-IRRF-com-a-regra-financeira-para-o-contas-a-receber-e-pagar)

**Documentações de referencia:**

[CFGTRIB - Cálculo de IRPF utilizando a tabela progressiva, com desconto simplificado ou desconto normal](https://tdn.totvs.com/pages/viewpage.action?pageId=1028926771)

[Orientações Consultoria de Segmentos - Novo Cálculo do IRRF](https://tdn.totvs.com/pages/releaseview.action?pageId=1019343450)
