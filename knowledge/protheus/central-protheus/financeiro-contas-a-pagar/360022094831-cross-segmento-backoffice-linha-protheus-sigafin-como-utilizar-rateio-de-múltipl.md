---
article_id: 360022094831
category: Financeiro - Contas a Pagar
content_hash: dc42e85c4ace5f078629dc2dacf965fffe82e160da7d125bbf04f90faf30cfbb
fetched_at: '2026-06-28T22:38:06.937573+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como utilizar rateio
  de múltiplas naturezas por Centro de Custo
type: support-article
updated_at: '2025-10-24T11:52:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022094831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-utilizar-rateio-de-m%C3%BAltiplas-naturezas-por-Centro-de-Custo
---

**Dúvida**Como utilizar rateio de múltiplas naturezas por Centro de Custo?

**Ambiente**Microsiga Protheus  – Financeiro – A partir da versão 12.1.17

**Solução**Para que esta rotina seja validada, devem-se observar os seguintes parâmetros:

* **MV\_MULNATP = T -**Utiliza múltiplas naturezas para contas a pagar

Ao distribuir o valor do título entre múltiplas naturezas, é possível ratear o valor de cada natureza entre diversos centros de custos. Para isto, na coluna**Rat. C. Custos** informe**1**para distribuir o valor da natureza entre centro de custos diferentes ou, caso contrário, informe**2.**

#### Lançamentos Padrão:

* **508 – Rateio Centro de Custo por Natureza - Contas a Pagar**
* **509 – Cancelamento Rateio Centro de Custo Múltipla natureza - Contas a Pagar**
* **510 – Inclusão de títulos - Contas a Pagar**
* **513 - Inclusão de Títulos Pagamento Antecipado (PA)**
* **514 - Exclusão Títulos Pagamento Antecipado (PA)**
* **515 – Exclusão de título - Contas a pagar**
* **537 – Baixas de títulos a Pagar c/Distr. em Mult. Naturezas p/CC**
* **539 – Cancelamento de baixa de títulos a Pagar c/Distr. em Mult. Naturezas p/CC**

Estes lançamentos padrões estão disponíveis para contabilização on-line (508, 509,537,539) ou off-line (508,515,537).

As distribuições de valores por múltiplas naturezas que não utilizarem o rateio por centro de custo são contabilizadas como inclusão.**Lançamentos Padrão 510-Emissão ou 530-Baixa (Pagar)**

Observação: O lançamento padrão **"510/513"** irá contabilizar somente o rateio por múltiplas naturezas (campos E2\_MULTNAT igual a "1" e EV\_RATEICC igual a "2").

As distribuições que utilizarem o rateio por centro de custo tem sua contabilização efetuada pelos lançamentos:**508-Emissão ou 537-Baixa (Pagar).**

Obs: O lançamento padrão **"508"** deve ser utilizado somente para contabilização da combinação dos rateios por múltiplas naturezas e por centro de custo (campos E2\_MULTNAT igual a "1" e EV\_RATEICC igual a "1").

O Lançamento Padrão 508 - Rateio Centro de Custo Múltipla Natureza (Pagar) - não será executado caso não exista o**Lançamento Padrão 510 - Inclusão de Títulos de Contas a Pagar.**

O Lançamento Padrão 537 - Rateio Centro de Custo Múltipla Natureza (Pagar) - não será executado caso não exista o**Lançamento Padrão 530 - Contas a Pagar - Baixa de Títulos.**

Para que exista a contabilização de forma correta, será necessário que o **Lançamento padrão 510/513** tenha a seguinte sintaxe nas definições de obtenção dos valores:

**Na aba Valores do lançamento padrão, o campo Vlr.Moeda1 deve conter a sintaxe abaixo:**

* **Lançamento Padrão 510.**

*IIF(SE2->E2\_MULTNAT == "1", SEV->EV\_VALOR, SE2->E2\_VALOR )*

*Para não duplicar a contabilização dos impostos, pode-se usar, por exemplo, a expressão em **Vlr.Moeda1**:*

*IF(SE2->E2\_MULTNAT == '1' .AND. SEV->EV\_VALOR > 0, 0, SE2->E2\_INSS)*

* **Lançamento Padrão 513.**

*Sequencia 001 - IF(SE2->E2\_MULTNAT=='2',IF(GETMV('[MV\_CTMOVPA](https://tdn.totvs.com/x/wDcPEQ)')=='1',SE2->E2\_VALOR,SE5->E5\_VALOR),0)*

*Sequencia 002 - IF(SE2->E2\_MULTNAT=='1',SEV->EV\_VALOR,0)*

**Nota Importante!**

**LP 513 - Inclusão de PA com rateio de Múltiplas Naturezas X Centro de Custos**  
Este LP será utilizado apenas pela rotina CTBAFIN - Contabilização OffLine.  
No processo OnLine a contabilização se dará pelo LP 510.

#### **ATENÇÃO!**

Caso não seja procedido desta forma, a contabilização está sujeita a duplicidade de valores.

Para execução da contabilização do LP 508 o LP 510 precisa estar cadastrado, porém os dois não serão executados em conjunto.

Para incluir um rateio do valor da natureza entre diversos centros de custo:

1. Na rotina **Contas a Pagar**, inclua um título**.**
2. Informe o campo**Rat. C.Custo**.
3. É apresentada uma janela, onde serão digitados os seguintes dados:  
     
   * **Centro de Custo** – Centro de custo financeiro para o qual será indicado o valor;
   * **Valor a Ratear** – Valor indicado para o referido centro de custo;
   * **Percentual** – Percentual representado pelo valor a ratear no valor indicado para a natureza.
   * Os dados digitados estão disponíveis a qualquer momento, enquanto não for confirmada ou cancelada a distribuição por múltiplas naturezas. Para alterá-los ou visualizá-los, basta digitar 1 no Campo Rat. C. Custo e os dados serão disponibilizados.

**Contabilização da Exclusão de títulos com rateio de múltiplas naturezas por Centro de Custo.**

Para que seja contabilizado a exclusão do título a pagar com múltiplas naturezas e rateio por centro de custo, é necessário a configuração dos LPs 509 e 515.

**Configuração:**

* Lançamento Padrão 515.
* Na aba Valores do lançamento padrão, o campo Vlr.Moeda1 deve conter a sintaxe abaixo:

*IIF(SE2->E2\_MULTNAT == "1", SEV->EV\_VALOR, SE2->E2\_VALOR)*

A contabilização do rateio por centro de custo pelos LPs 508 e 509 deve ser feita pela tabela posicionada SEZ.

Observação: a tabela SE2 também estará posicionada para que possa utilizar informações do título no LP.

**Saiba mais**[Como\_utilizar\_rateio\_de\_múltiplas\_naturezas\_por\_Centro\_de\_Custo](https://tdn.totvs.com/pages/viewpage.action?pageId=229147656)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA070 - Como contabilizar a baixa do contas a receber múltiplas naturezas com Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006350881-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Como-contabilizar-a-baixa-do-contas-a-receber-m%C3%BAltiplas-naturezas-com-Centro-de-Custo)
