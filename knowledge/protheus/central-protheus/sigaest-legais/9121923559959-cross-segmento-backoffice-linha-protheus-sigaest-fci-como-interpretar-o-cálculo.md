---
article_id: 9121923559959
category: SIGAEST - LEGAIS
content_hash: 6df75d24b3e43bcaac1905ceb882c82a86b29254a746cf9d86b48f037d0c21aa
fetched_at: '2026-06-28T22:38:51.656239+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar
  o cálculo do Valor Importado (A8_VLRVI) em Importações?
type: support-article
updated_at: '2025-01-29T11:09:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9121923559959-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FCI-Como-interpretar-o-c%C3%A1lculo-do-Valor-Importado-A8-VLRVI-em-Importa%C3%A7%C3%B5es
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:17 min** **Dúvida**Como interpretar o cálculo do Valor Importado(A8\_VLRVI) em Importações?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

**FCI (Ficha de Conteúdo de Importação)** é o documento responsável por reunir as informações necessárias para que se possa determinar qual a participação ou percentual de um insumo importado sobre o valor total de uma mercadoria, além de identificar o contribuinte e a mercadoria.

Para mais informações conceituais do FCI, veja a documentação abaixo:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI (Ficha de Conteúdo de Importação) - Método 3 - Conceito e Informações](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004679892)

**Definição dos Produtos da Exemplificação**

Para exemplificar a maneira de se analisar, vamos usar os seguintes produtos:

**◼ MPIMPORTADO01**

**◼ MPIMPORTADO02**

**Observação**: **MP** **= Matéria Prima**

Os produtos serão Importados, ambos os produtos terão **Origem 1 (Estrangeira - Importação Direta)**

**Qual a Fórmula do FCI?**

Resumidamente, a fórmula do Valor da Taxa Importada por item é:

**Valor Importado = Fator Agrega Valor (VL) \* Fator Situação Tributária ( FST)**

Colocando em siglas, ficaria:

**VI = VL \* FST**

Iremos entender nos próximos passos o que é o Fator Agrega Valor e o Fator Situação Tributária.

**Definição do Fator Agrega Valor (VL)**

No nosso exemplo, os produtos **MPIMPORTADO01** e **MPIMPORTADO02** terão Importação Direta (via rotina MATA103) com **F4\_AGREG = S e Origem 1** (conforme dito anteriormente). Então eles irão cair neste cálculo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127286561175/mceclip1.png)

Para saber mais Fatores de Agregação para checar qual fórmula seu produto se enquadrará, acesse ao link completo da documentação **[clicando aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=235589761)**

**Onde são cadastrados o Fator de Agregação de Valor e Origem**

Estas definições são feitas através dos cadastros de TES (Tipo de Entrada e Saída - MATA080) e Cadastro de Produto (MATA010), conforme prints abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127406493207/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127467340951/mceclip3.png)

OBS: Para mais detalhes sobre estes campos, basta acessá-los e pressionar o botão F1 para que seja aberto o Help do Campo.

**Efetivando a Importação Direta e conferindo o Agrega Valor**

Vamos entrar com a Nota via MATA103 (***Módulo 02 - Compras -> Atualizações -> Movimentos -> Documento de Entrada***). Note que os produtos terão a mesma quantidade, porém valores diferentes. O Frete será de R$ 300,00 que será rateado proporcionalmente para cada item da NF.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127654169879/mceclip5.png)

Aplicando a Fórmula:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127286561175/mceclip1.png)

Agrega Valor **MPIMPORTADO01 =**  (D1\_TOTAL + D1\_VALFRE + D1\_SEGURO) - (D1\_II)

Agrega Valor **MPIMPORTADO01 =** (3500 + 91,3 + 0) - (0)

Agrega Valor **MPIMPORTADO01 = 3591,3**

Agrega Valor **MPIMPORTADO02 =**  (D1\_TOTAL + D1\_VALFRE + D1\_SEGURO) - (D1\_II)

Agrega Valor **MPIMPORTADO02 =** (8000 + 208,7 + 0) - (0)

Agrega Valor **MPIMPORTADO02 = 8208,7**

Query que confirma que o cálculo está correto:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127703759639/mceclip6.png)

**Definição do Fator Situação Tributária (FST)**

De acordo com a [**documentação**](https://tdn.totvs.com/pages/releaseview.action?pageId=235589761) que já havíamos indicado anteriormente, o FST consiste em validar qual o fator de multiplicação baseado no **código de Origem** do produto, sendo:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9127917873943/mceclip8.png)

Desta forma, tanto o **MPIMPORTADO01** quanto o **MPIMPORTADO02**, pelo fato de ambos terem Origem 1 (e consequentemente iniciam-se com 1), se enquadrarão o fator de multiplicação 1, conforme destacado na imagem acima.

Informações Importantes:

* **Cálculo por Item**  
  O **VI** do Item da Nota Fiscal é o resultado do **Fator Agrega Valor** multiplicado pelo **Fator Situação Tributária** **VI = VL \* FST**.
* **Cálculo para o Período**  
  Para cada Item válido das Notas Fiscais de Entradas do período, será realizado o cálculo do **VI** descrito. Os valores calculados são acumulados por produto e no momento da gravação do registro do produto na tabela de **Pré-Apuração FCI**(**SA8**), ocorre a divisão dos valores acumulados dos **VI’s** e quantidades de cada Item válido das Notas Fiscais do período

**Descobrindo o Valor da Parcela Importada dos produtos MPIMPORTADO01 e MPIMPORTADO02**

Vamos relembrar o cálculo do VI?

**VI = VL \* FST**.

Aplicando para o **MPIMPORTADO01**:

VI = 3591,3 \* 1

VI = 3591,3

Aplicando para o **MPIMPORTADO02**:

VI = 8208,7 \* 1

VI = 8208,7

A soma do VI é divido pela soma da quantidade (importada) apurada no período e o valor é gravado no campo A8\_VLRVI (considerando possíveis arredondamentos). Esse cálculo só acontecerá após o processamento da rotina FISA061.

| **A8\_VLRVI do MPIMPORTADO01** |
| --- |
| 3591,3/100= 35,91 |

| A8\_VLRVI do MPIMPORTADO02 |
| --- |
| 8208,7/100= 82,09 |

**Conferindo os resultados via Relatório no Protheus**

Vamos começar usando o Relatório FCIR001 (Relação FCI Sintético), que é acessado pelo ***Módulo 04 - Estoque/Custos -> Relatórios -> Genéricos -> Relação FCI Sint.***

***![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128162384407/mceclip9.png)***

Podemos ver que para ambos os produtos o Valor da VI bateu com nossos cálculos.

Observação: É importante parametrizar a primeira pergunta "Tipo de Impressão" = Pré Apuração, que é o método que o Estoque trata (tabela SA8). A opção "Ficha" engloba registros da tabela CFD, que levam em consideração informações de vendas. Caso tenha dúvidas sobre os registros da tabela CDD, recomendamos acionar a equipe de Protheus Fiscal.

Agora vamos utilizar o Relatório FCIR002 (Relação FCI Analítico de Entrada), que é acessado pelo ***Módulo 04 - Estoque/Custos -> Relatórios -> Genéricos -> Relação FCI An. Entr.***

***![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128211584791/mceclip10.png)***

***![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9128172140439/mceclip11.png)*** Podemos confirmar que os valores bateram.

**Saiba mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Produções?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9129246051479)*

[*Clique aqui e veja mais artigos sobre Legais no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)
