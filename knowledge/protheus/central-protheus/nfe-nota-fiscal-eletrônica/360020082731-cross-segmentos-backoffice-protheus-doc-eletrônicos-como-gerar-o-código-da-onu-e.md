---
article_id: 360020082731
category: NFe - Nota Fiscal Eletrônica
content_hash: e7ef86082b67064ddd3f7a2e69aa5f10ad42b718a002bdb50eae1977357ca0af
fetched_at: '2026-06-28T22:40:03.616928+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  Como gerar o código
  da Onu em informações complementares ou informações adicionais do produto (ANTT
  / Agência Nacional de Transportes Terrestres)
type: support-article
updated_at: '2025-06-12T18:30:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020082731-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-o-c%C3%B3digo-da-Onu-em-informa%C3%A7%C3%B5es-complementares-ou-informa%C3%A7%C3%B5es-adicionais-do-produto-ANTT-Ag%C3%AAncia-Nacional-de-Transportes-Terrestres
---

**Dúvida**Como gerar o código da Onu em informações complementares (ANTT / Agência Nacional de Transportes Terrestres)?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Importante:**

Para destacar em informações adicionais do Produto o código de produtos ***perigos em Negrito***, baixar o pacote de atualização do link abaixo:

**1. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

     2. **Compilar RDMAKE NFESEFAZ, DANFEII e DANFEIII** presente no link abaixo:

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1152113)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

1- Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar**  ***MV\_IMPADIC = .T.***

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17115453678999)

2- Preencher no cadastro de **Complemento de Produtos** o campo **N° ONU** "**B5\_ONU"** informar o código da ONU

![n_onu.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520934295)

3- Preencher o mesmo na rotina do **TMS em Atualizações -> Cadastros -> Classificações ONU**  no campo **N° ONU** "**DY3\_ONU"**

4- Deixar o campo **Inf. Comp.** "**DY3\_INFCPL" = SIM**Caso o campo **"Inf. Compl" DY3\_INFCPL**esteja preenchido com "1-Sim" a informação do código ONU **também** será levada para a tag <infCpl> do XML.

5- E a descrição que deve ser gerado preencher no campo **Descrição** "**DY3\_DESCRI"**

6- Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar** **MV\_NONUINF** for igual a **1**, neste caso será informado o valor total de peso bruto do produto em quilograma (KG). Para isso deve-se informar o valor do campo de **Peso Bruto**(**B1\_PESBRUT**) em quilos (KG):

![](https://tdn.totvs.com/download/attachments/651268056/image2022-2-22_16-3-25.png?version=1&modificationDate=1645556605500&api=v2&effects=drop-shadow)

* **Exemplo:**

Parâmetro **MV\_NONUINF**for igual a **0**:

**RETRATO:**

![](https://tdn.totvs.com/download/attachments/651268056/DANFE%20Exemplo.jpg?version=1&modificationDate=1637179866887&api=v2&effects=drop-shadow)

**PAISAGEM:**

![](https://tdn.totvs.com/download/attachments/651268056/DANFE%20Exemplo%20Paisagem.jpg?version=1&modificationDate=1637179960700&api=v2&effects=drop-shadow)

Parâmetro **MV\_NONUINF**for igual a **1**:

**RETRATO:**

**![](https://tdn.totvs.com/download/attachments/651268056/image2022-2-22_16-13-22.png?version=1&modificationDate=1645557203080&api=v2&effects=drop-shadow)**

**PAISAGEM:**

**![](https://tdn.totvs.com/download/attachments/651268056/image2022-2-22_16-14-23.png?version=1&modificationDate=1645557263453&api=v2&effects=drop-shadow)**

* **Conforme o boletim do TDN:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=651268056>

* **Saiba mais:**

Existe um parecer da consultoria tributária da TOTVS no link abaixo:

[Parecer](https://tdn.totvs.com/pages/releaseview.action?pageId=287080293)

* **Saiba mais:**

Podem ser utilizados os campos das documentações abaixo, para a gerar a mensagem em informações complementares do XML e do Danfe:

[MP - NFE - Como gerar mensagem em informações complementares (TAG infcpl e infadfisco) do Danfe utilizando fórmula ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026944871)

[MP - NFE - Como gerar informações na TAG infCpl ou infAdFisco no XML e no DANFE](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024950773)
