---
article_id: 360016589071
category: Materiais - Compras (SIGACOM)
content_hash: b08e7e52eb6101dcaa4e687ed130c70155a142b2845a484cd563a6f0fe9f2efc
fetched_at: '2026-06-28T22:41:07.716769+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Nota Fiscal
  de Importação pelo MATA103?
type: support-article
updated_at: '2023-03-06T11:01:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016589071-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-incluir-Nota-Fiscal-de-Importa%C3%A7%C3%A3o-pelo-MATA103
---

**Dúvida**Como incluir Nota Fiscal de Importação pelo MATA103?  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Está disponível nas rotinas **Nota Fiscal Manual de Entrada (MATA910)** e **Documento de Entrada (MATA103)**, um tratamento para inclusão de notas fiscais de importação para clientes que não utilizam o módulo SIGAEIC.

Para o tratamento correto do sistema é necessário observar a configuração:

**Cadastro de Fornecedor**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012509012/mceclip5.png)

**Cadastro de TES - Tipo de Entrada ou Saída**

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012508652/mceclip4.png)**

**Despesas Acessórias**

Em relação ao valor das despesas (Siscomex, Frete, Despesas, Seguro e AFRMM - Adicional ao Frete para Renovação da Marinha Mercante) compor ou não a base de cálculo dos impostos, observar a configuração:

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012518731/mceclip9.png)

**PIS Majorado e COFINS Majorado**

Para o cálculo do Pis Majorado e Cofins Majorado, informar o percentual de acréscimo a ser aplicado na alíquota, nos campos correspondentes, localizados na aba “Outros” da TES:

Ao lançar a nota fiscal, observar a descrição dos impostos calculados. Se a configuração foi efetuada conforme indicação, os impostos serão demonstrados da seguinte maneira:

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012509152/mceclip8.png)

**Importante:**Caso a nota tenha sido lançada incorretamente é necessário realizar a **exclusão**e incluir novamente após o ajuste das configurações. A rotina de reprocessamento (MATA930) **não refaz os cálculos dos tributos**.

**Importação com Redução de Base de ICMS**

Para notas fiscais de importação com **Redução de Base de ICMS**, seguir a configuração abaixo:

* **Parâmetros:**

MV\_REDIMPO = .T.  Indica se o cálculo da base de ICMS considera a redução de base nas notas de importação.

**O parâmetro abaixo deverá ser criado manualmente:**

MV\_EIC0064

Tipo: Lógico

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

Exemplo Prático:

**Declaração de Importação - DI**

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519271/mceclip10.png)

**Preencha os campos Valor Unitário e Valor Total**  
**![(estrela vermelha)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/star_red.png) É necessário somar o valor aduaneiro e o valor do imposto de importação (R$ 28.554,87 + R$5.710,97 = R$34.265,84).**

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012510492/mceclip11.png)**

**Preencha os campos Aliq Import (D1\_ALIQII) e  Vlr. I.I. (D1\_II) com os valores** **correspondentes:**

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519651/mceclip12.png)**Informe as despesas acessórias:**

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012519771/mceclip13.png)**Conferir os valores:**

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360012511112/mceclip14.png)

# **Informações Complementares**

Especificações para criação do campo D1\_II, acesse o link abaixo:

#### Boletim Técnico: [Importação\_MATA103.pdf](http://tdn.totvs.com/download/attachments/6076840/Importa%C3%A7%C3%A3o_MATA103.pdf?version=1&modificationDate=1450368876000&api=v2)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
