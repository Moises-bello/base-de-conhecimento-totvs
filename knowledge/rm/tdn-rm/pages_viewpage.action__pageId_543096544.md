---
content_hash: 60ee53427ea55a3da050987499e37f5221a01fc8cb6f7dc2dfcc920cf364c8c1
fetched_at: '2026-06-29T00:10:38.150354+00:00'
page_id: '543096544'
product: rm
source: tdn-rm
title: Encerramento da Subapuração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=543096544
version: 7
---

Os períodos de apuração das Subapurações também devem ser encerrados e os valores calculados e isso deve ocorrer antes do encerramento do tributo principal. Por exemplo, para encerrar o período de apuração do **ICMS** é preciso, primeiro, encerrar suas Subapurações.

#### **Validações realizadas para o Encerramento**

1. O Período de Apuração deve estar Aberto;
2. O período de Sub Apuração imediatamente anterior, de mesmo Identificador, deve estar encerrado;
3. O Lote Fiscal (caso seja utilizado) deve estar Aberto.

**Seleção dos Lançamentos Fiscais**

No Encerramento serão selecionados Lançamentos Fiscais de Entrada e Saída, que atendam aos seguintes critérios:

1. Possuam Ajuste vinculado ao Lançamento ou ao Item;
2. Pertençam à Coligada\Filial do Período de Apuração;
3. Cuja **DATALF** esteja dentro do período da Subapuração;
4. Com Status Normal ou Estornado;
5. Associados a CFOP Fiscal;
6. Cujo Lote Fiscal esteja Liberado (caso utilize Lote Fiscal);

Se o flag **"Considerar somente as Entradas referenciadas em notas de Saída"** estiver marcado somente serão selecionadas as Notas Fiscais de Entrada que estiverem referenciadas a Notas Fiscais de Saída. Esta regra só se aplica caso o Ajuste esteja vinculado ao Item do Lançamento e a referência deve ser realizada no Item. Não afeta a seleção das Notas Fiscais de Saída.

**No processo de encerramento, os seguintes valores serão calculados pelo sistema**

*Valor total dos débitos por Saídas*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Se o identificador for **“3”** devem ser considerados os lançamentos de ajuste onde o **3º** e **4º** caracteres forem **“2”** e **“3”,** respectivamente. Por exemplo: *MG****23****000999*
* Se o identificador for **“4”** devem ser considerados os lançamentos de ajuste onde o **3º** e **4º** caracteres forem **“2”** e **“4”**, respectivamente. Por exemplo: *MG****24****000999*
* E assim sucessivamente.
* Resumindo, o **3º** caractere deve ser **“2”** e o **4º** caractere deve ser igual ao código do Identificador;

*Valor total de Ajustes a débito*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde **3º** e **4º** caracteres do Código de Ajuste informado forem iguais à “**0**”. Por exemplo: *MG****00****9999*.

*Valor total de Ajustes Estornos de créditos*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde **3º** e **4º** caracteres do Código de Ajuste informado forem iguais à “**0**” e “**1**”, respectivamente. Por exemplo: *MG****01****9999****.***

*Valor total dos créditos por Entradas*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Se o identificador for “3” devem ser considerados os lançamentos de ajuste onde o **3º** e **4º** caracteres forem **“5”** e **“3”**, respectivamente. Por exemplo: *MG****53****000999*
* Se o identificador for “4” devem ser considerados os lançamentos de ajuste onde o **3º** e **4º** caracteres forem **“5”** e **“4”**, respectivamente. Por exemplo: *MG****54****000999*
* E assim sucessivamente.
* Resumindo, o **3º** caractere deve ser **“5”** e o **4º** caractere deve ser igual ao código do Identificador;

*Valor total de Ajustes a crédito*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde **3º** e **4º** caracteres do Código de Ajuste informado forem iguais à “**0**” e “**2**”, respectivamente. Por exemplo: *MG****02****9999****.***

*Valor total de Ajustes Estornos de Débitos*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos onde **3º** e **4º** caracteres do Código de Ajuste informado forem iguais à “**0**” e “**3**”, respectivamente. Por exemplo: *MG****03****9999****.***

*Saldo credor do período anterior*

Este campo recebe o saldo credor do período de Subapuração imediatamente anterior, de mesmo Identificador.

*Valor total das Deduções*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos Fiscais/Itens se o **3º** caractere do Código de Ajuste for igual “**6**” e o **4º** caractere for igual à  **“3”, “4” “5”, “6”, “7”** ou **“8”**.

*Saldo apurado no período*

Se o resultado for menor que “0” (zero), representa valor de imposto a pagar.

Já o resultado positivo corresponde a Saldo Credor a transportar para o próximo período.

*Valor total dos débitos especiais*

Somatório do Valor do ICMS informado no **Lançamento de Ajuste** dos Lançamentos Fiscais/Itens que possuam Ajuste com códigos que atendam às seguintes regras:

* Lançamentos Fiscais/Itens se o 3º caracter do Código de Ajuste for igual “**7**” e o 4º caractere for igual à  **“3”, “4” “5”, “6”, “7”** ou **“8”**.

Obs: Ao final dos cálculos os valores são armazenados na tabela e o Status da Subapuração é atualizado para “**Encerrado**”.
