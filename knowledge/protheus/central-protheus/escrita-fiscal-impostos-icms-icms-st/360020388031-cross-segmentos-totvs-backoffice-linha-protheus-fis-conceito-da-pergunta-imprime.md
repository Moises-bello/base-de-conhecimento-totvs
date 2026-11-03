---
article_id: 360020388031
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 823a5088a06d0300496c7d9ff38b42af3d0c8c653dce94fb863212dcc4c1ffe4
fetched_at: '2026-06-28T22:39:20.448219+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Conceito da pergunta
  "Imprime Crédito ST" na Apuração de ICMS (MATA953)
type: support-article
updated_at: '2021-07-13T18:00:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020388031-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Conceito-da-pergunta-Imprime-Cr%C3%A9dito-ST-na-Apura%C3%A7%C3%A3o-de-ICMS-MATA953
---

**Dúvida**Qual a funcionalidade da pergunta "Imprime Crédito ST" na apuração de ICMS?  
   
 **Ambiente**Protheus - Todas as versões  
   
**Solução**

É de conhecimento geral que não existe o conceito de **crédito** para o valor do ICMS por substituição tributária, porém como existem situações específicas que temos que demonstrar um valor a deduzir do imposto a pagar, o sistema está preparado para esta questão. A pergunta trabalha em conjunto com a configuração do campo Ret. ST (**F4\_CREDST**) do TES - Tipos de Entrada e Saída (Tabela SF4), e, por consequência, com os campos **F3\_CREDST** e **FT\_CREDST**, onde é definido o comportamento do sistema para cada item das notas fiscais. Com este campo é possível configurar se o sistema irá “creditar”, debitar ou se é uma operação onde a empresa foi substituída, e neste caso o valor será calculado, gravado na nota fiscal, porém não haverá efeito algum na apuração de ICMS-ST.

---

## 

## A pergunta "Imprime Crédito ST"

O comportamento da apuração de ICMS em relação ao valor de "crédito" de ICMS-ST é definido pela configuração da pergunta **Imprime Crédito ST**na parametrização da rotina. Esta pergunta possui 3 opções, e conforme a opção selecionada o valor é obtido de uma forma diferente.

Importante

As devoluções de venda são **sempre**consideradas como crédito, independentemente da configuração da pergunta "**Imprime Crédito ST"**e do campo F4\_CREDST, com exceção da opção **"4 - Subst. Trib"**(que faz com que os valores não sejam considerados na apuração) pois sempre é necessário estornar o débito da saída devolvida.

Desta forma, a configuração da pergunta "**Imprime Crédito ST"** não interfere no processamento das devoluções.

### Opção 1 - Sim

Ao selecionar esta opção serão considerados como crédito, além das devoluções de venda, **apenas** os valores correspondentes aos documentos escriturados com a opção **"1 - Credita"**  no TES. Ao utilizar esta opção, documentos de entrada que tenham sido escriturados utilizando-se a opção **"2 - Retido ST"**não serão considerados como geradores de crédito. **Observação:** Nesta configuração o valor de crédito é obtido dos campos **F3\_SOLTRIB** e **FT\_SOLTRIB**.

### 

### Opção 2 - Não

Ao selecionar esta opção serão considerados como crédito, além das devoluções de venda, **apenas** os valores correspondentes aos documentos escriturados com a opção **"2 - Retido ST"**no TES. Ao utilizar esta opção, documentos de entrada que tenham sido escriturados utilizando-se a opção **"1 - Credita"**não serão considerados como geradores de crédito. **Observação:** Nesta configuração o valor de crédito é obtido dos campos **F3\_ICMSRET**e **FT\_ICMSRET.**

### 

### Opção 3 - Devolução

Ao selecionar esta opção serão consideradas como crédito **apenas**as devoluções de venda, independentemente de como os documentos tenham sido escriturados em relação ao campo **F4\_CREDST**. Ao utilizar esta opção nenhum documento de entrada será considerado como gerador de crédito. **Observação:** Nesta configuração o valor de crédito é obtido dos campos **F3\_ICMSRET**e **FT\_ICMSRET.**

## Configuração do campo F4\_CREDST

Abaixo seguem alguns exemplos e recomendações de configuração do campo **F4\_CREDST**conforme a operação realizada.

**Importante:**

Para notas de entrada **não deve ser utilizada** a opção **"2 - Retido ST"** pois desta forma os valores serão considerados como crédito, podendo ocasionar inconsistências na geração das GNRE's (Guias Nacionais de Recolhimento) e títulos a pagar gerados na apuração de ICMS.

**Notas fiscais de entrada nas quais a empresa tenha sido substituída.**

Nesta situação o campo **F4\_CREDST** deve ser configurado com a opção **"4 - Subst. Trib"**, para que o valor seja apenas demonstrado na nota de entrada e não tenha nenhum efeito na apuração do imposto. Esta é a configuração recomendada para documentos de **entrada** em geral, visto que não existe crédito do valor do imposto previamente recolhido por substituição tributária e, portanto, o documento não deve influenciar nos valores apurados.

### 

### **Notas fiscais de entrada com antecipação de ICMS**

Nesta situação o campo **F4\_CREDST**deve ser configurado com a opção**“3 – Debita”.**Esta opção fará com que o valor do ICMS-ST das operações de entrada seja somado nos débitos da apuração.

Deve ser utilizado apenas nos casos que o ST pode ser pago no final do período junto com a apuração de ICMS.

### 

### **Notas fiscais de saída quando a empresa é substituta:**

Nesta situação o campo **F4\_CREDST** deve ser configurado com a opção **"2 - Retido ST"**.

Este é o valor *default*deste campo, e o ICMS-ST será considerado como débito na apuração. É importante ressaltar que esta configuração deve ser utilizada apenas para notas de **saída.**
