---
article_id: 360022575671
category: Escrita Fiscal - Impostos - Cálculos
content_hash: 69cdf9da37a7005f0d9da95d7bc39a930920ac6221f77ad4b82d73bf52cbdad1
fetched_at: '2026-06-28T22:39:30.616222+00:00'
product: protheus
section_id: 1500001538621
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Nota fiscal de Importação
  pelo Documento de Entrada
type: support-article
updated_at: '2021-07-29T14:39:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022575671-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Nota-fiscal-de-Importa%C3%A7%C3%A3o-pelo-Documento-de-Entrada
---

**Dúvida**Como emitir nota fiscal de Importação pelo Documento de Entrada ?  
  
**Ambiente**Protheus – Fiscal – A partir da versão 11.80]  
  
**Solução**

Está disponível nas rotinas **Nota Fiscal Manual de Entrada (MATA910)** e **Documento de Entrada (MATA103)**, um tratamento para inclusão de notas fiscais de importação para clientes que não utilizam o módulo SIGAEIC.

Para o tratamento correto do sistema é necessário observar a configuração:

**Cadastro de Fornecedor**

|  |  |
| --- | --- |
| **Campo** | **Preenchimento** |
| Estado (A2\_EST) | EX |
| Tipo (A2\_TIPO) | X – Outros |
| Pais (A2\_PAIS) | Código correspondente |

# **Cadastro de TES – Tipo de Entrada ou Saída**

|  |  |
| --- | --- |
| **Campo** | **Preenchimento** |
| Calcula ICMS (F4\_ICM) | Sim |
| Calcula IPI (F4\_IPI) | Sim |
| Cod.Fiscal (F4\_CF) | Algum Iniciado por “3” Ex: 3101 |
| L. Fisc. ICMS (F4\_LFICM) | Tributado |
| L.Fisc. IPI (F4\_LFIPI) | Tributado |
| IPI na base (F4\_INCIDE) | Sim |
| Agrega Valor (F4\_AGREG) | I – ICMS+Merc |
| PIS/COFINS (F4\_PISCOF) | 3- Ambos |
| Cred. PIS/COF (F4\_PISCRED) | 1 – Credita |
| Agr. Cofins (F4\_AGRCOF) | C – COF+Merc |
| Agr. PIS (F4\_AGRPIS) | P – PIS+ Merc |
| PS/CF Import (F4\_INTBSIC) | 3 - Ambos |
| Calc.Ipi.Frete (F4\_IPIFRET) | N - Não |

# **Cadastro de TES – Tipo de Entrada ou Saída**

# **Despesas Acessórias**

Em relação ao valor das despesas (Siscomex, Frete, Despesas, Seguro e AFRMM - Adicional ao Frete para Renovação da Marinha Mercante) compor ou não a base de cálculo dos impostos, observar a configuração:

|  |  |
| --- | --- |
| **Imposto** | **Campo** |
| ICMS | Desp. Ac. ICMS (F4\_DESPICM) |
| IPI | Desp. Ac. IPI (F4\_DESPIPI) |
| PIS | Desp. Ac. PIS (F4\_DESPPIS) |
| COFINS | Desp. Ac. COF (F4\_DESPCOF) |

**PIS Majorado e COFINS Majorado**

Para o cálculo do Pis Majorado e Cofins Majorado, informar o percentual de acréscimo a ser aplicado na alíquota, nos campos correspondentes, localizados na aba “Outros” da TES:

|  |  |
| --- | --- |
| **Campo** | **Preenchimento** |
| Aliq. COF M.(F4\_MALQCOF) | % da Alíquota. Ex.: 1,00 |
| Aliq. PIS M.(F4\_MALQPIS) | % da Alíquota. Ex.: 2,00 |

```
Ao lançar a nota fiscal, observar a descrição dos impostos calculados. Se a configuração foi efetuada conforme indicação, os impostos serão demonstrados da seguinte maneira:
```

**![](http://tdn.totvs.com/download/attachments/6076840/majorado.PNG?version=3&modificationDate=1450695524000&api=v2)**

**Importante:**Caso a nota tenha sido lançada incorretamente é necessário realizar a **exclusão**e incluir novamente após o ajuste das configurações. A rotina de reprocessamento (MATA930) **não refaz os cálculos dos tributos**.

**Importação com Redução de Base de ICMS**

Para notas fiscais de importação com **Redução de Base de ICMS**, seguir a configuração abaixo:

* **Parâmetros:**

MV\_REDIMPO = .T.  Indica se o cálculo da base de ICMS considera a redução de base nas notas de importação.

**O parâmetro abaixo deverá ser criado manualmente:**

MV\_EIC0064

Tipo: Lógico

Descrição: Permite a subtração do valor do II (D1\_II) do valor total do item (D1\_TOTAL). Habilitado (.T.), Desabilitado (.F.)

Valor: .T. ou .F. conforme necessidade da empresa.

Atenção: Com este parâmetro habilitado, significa que o valor informado no item da NF de importação não estará com o Valor de II. Com o parâmetro desabilitado, significa que o valor informado no item da NF de importação estará com o Valor de II. Cabe ao usuário informar ou não o Valor dos Produtos com o Valor de II, lembrando sempre considerando a definição do parâmetro citado.

*Este parâmetro deve ser criado manualmente.*

* **Campo da TES:**

% Red. do ICMS (F4\_BASEICM)

**Procedimento para lançamento da nota de importação:**

**1º** Acesse a rotina MATA103 e preencha o cabeçalho da nota;

**2º** Some o valor Aduaneiro e o Imposto de Importação e informe o resultado nos campos: Valor do item (D1\_VUNIT) e Valor total (D1\_TOTAL);

**3º** Insira a TES com a configuração específica;

**4º** Informe a alíquota do Imposto de Importação e o valor do Imposto de Importação nos campos Aliq Import (D1\_ALIQII) e  Vlr. I.I. (D1\_II);

**5º** Informe as despesas acessórias, na aba “Descontos/Frete/Despesas”.

**![(seleção)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/check.png) Exemplo prático**

* **Declaração de Importação (DI)**

**![](http://tdn.totvs.com/download/attachments/6076840/di.PNG?version=1&modificationDate=1450364554000&api=v2)**

* **Preencha os campos Valor Unitário e Valor Total**  
  **![(estrela vermelha)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/star_red.png) É necessário somar o valor aduaneiro e o valor do imposto de importação (R$ 28.554,87 + R$5.710,97 = R$34.265,84).**

**![](http://tdn.totvs.com/download/attachments/6076840/1.PNG?version=1&modificationDate=1450365478000&api=v2)**

* **Preencha os campos Aliq Import (D1\_ALIQII) e  Vlr. I.I. (D1\_II) com os valores correspondentes**

**![](http://tdn.totvs.com/download/attachments/6076840/2.PNG?version=1&modificationDate=1450365665000&api=v2)**

* **Informe as despesas acessórias**

![](http://tdn.totvs.com/download/attachments/6076840/desp.PNG?version=2&modificationDate=1450695918000&api=v2)

**Confira os valores**

![4.PNG](http://tdn.totvs.com/download/attachments/6076840/4.PNG?version=1&modificationDate=1450365923000&api=v2)

***Boletim em Anexo***
