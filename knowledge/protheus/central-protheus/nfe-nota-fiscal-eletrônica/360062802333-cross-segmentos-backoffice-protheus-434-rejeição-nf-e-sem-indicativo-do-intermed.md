---
article_id: 360062802333
category: NFe - Nota Fiscal Eletrônica
content_hash: c2738442151b2dad5648acc8009566444d478f0ddd357efe3acd86fdf09bc701
fetched_at: '2026-06-28T22:40:03.075650+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - 434 Rejeição : NF-e sem indicativo
  do intermediador'
type: support-article
updated_at: '2025-06-13T12:03:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062802333-Cross-Segmentos-Backoffice-Protheus-434-Rejei%C3%A7%C3%A3o-NF-e-sem-indicativo-do-intermediador
---

**Dúvida**Como corrigir a rejeição 434 Rejeição : NF-e sem indicativo do intermediador ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se Informado indicativo de presença, tag: **indPres, IGUAL a  2, 3, 4 ou 9**  
- Obrigatório o preenchimento do campo Indicativo do Intermediador **(tag:**  
**indIntermed)**

Observação 1: **Regra válida a partir de e 23/08/2021 para homologação e 04/04/2022 para produção**

* ***Importante:***

*Realizar as atualizações do link abaixo:*

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

    2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552-Cross-Segmentos-TSS-Transmiss%C3%A3o-de-Documentos-Eletr%C3%B4nicos-Atualiza%C3%A7%C3%A3o-dos-SCHEMAS)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Clique Aqui](https://suporte.totvs.com/portal/p/10098/download#detail/1031444)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

    3. Rodar o **Dicionário de Dados para a criação dos novos campos :**

<https://suporte.totvs.com/portal/p/10098/download?e=1013133>

Pacote de dicionário centralizado para atendimento da NT 2020.006 referente a intermediador da operação de vendas e compras, com desenvolvimento das **áreas do Protheus: Compras, controle de lojas (SIGALOJA), Faturamento e Callcenter (SIGAFAT), e TSS. Compatível com Release 12.1.23 até 12.1.27.**

Na release ***12.1.33*** o menu e os campos já estão disponíveis, ***não é necessário rodar o dicionário.***

**3. Criação dos Parâmetros:**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar Observação: **Para ambiente homologação** será necessário criar o parâmetro **MV\_NT2006I** com a data de **01/03/2021** conforme documentos disponibilizados pelos módulos abaixo. 

![MV_NT2006I.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500006934161)

* A TAG ***indPres*** pode ter os conteúdos abaixo:

**0=**Não se aplica (por exemplo, Nota Fiscal complementar ou de ajuste);   
**1=**Operação presencial;   
**2=**Operação não presencial, pela Internet;   
**3=**Operação não presencial, Teleatendimento;   
**4=**NFC-e em operação com entrega a domicílio;   
**5=**Operação presencial, fora do estabelecimento;   
**9=**Operação não presencial, outros. 

Para que não seja necessário **preencher a TAG indIntermed a TAG *indPres pode ser 0, 1 ou 5:***

**1-** No pedido de vendas preencher o campo **Presença Com C5\_INDPRES =  0**

**![indpres.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003743222)**

**ou**

**1-** No pedido de vendas preencher o campo **Presença Com C5\_INDPRES =  1**

**![indpres_1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4402830635799)**

**ou**

**1-** No pedido de vendas preencher o campo **Presença Com** **C5\_INDPRES =  5**

**![venda_presencial_fora.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939027424535)**

2- Caso seja preenchido como **Presença Com** **C5\_INDPRES =  5 no** pedido de vendas é necessário haver uma nota referenciada que gere o grupo **refNFe ou refNF.**

* **refNFe =** Modelo 55 Espécie = SPED
* **refNF=** Modelo 01, 01A, 02 Espécie = NF, NFe, NFA ou **NFCF (modelo novo incluído na 4.00)**

3- No pedido de venda será necessário preencher os campos **NF . Ori , Serie Ori e Item Ori .**

Para referenciar a nota de origem os três campos precisam estar preenchidos:

**D2\_ITEMORI, D2\_SERIORI, D2\_NFORI (nota de saída)**

![referenciar_a_nota.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939027426967)

4- Quando for referenciar duas notas de saída do tipo normal para gerar a chave além de referenciar será necessário incluir os **CFOPS da nota no parâmetro:**

![MV_REFNFE.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/16939027431191)

* **Parâmetro MV\_REFNFE = Informar o CFOP separado por vírgula.**

![MV_REFNFE.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939015501975)

Para que não seja necessário preencher a TAG **indIntermed a TAG *indPres pode ser***  utilizado os CFOPS 5205, 5206, 5207, 5251, 5252, 5253, 5254, 5255, 5256, 5257, 5258, 5301, 5302, 5303, 5304, 5305, 5306, 5307.

1- No**TES** na Aba **Impostos** preenchao campo F4\_CF  **Cod. Fiscal**com um dos CFOPS mencionados acima

![F4_CF.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4405502248599)

2- Após isso, **exclua** a nota e gere novamente.

Para ***gerar o intermediador*** realizar os passos abaixo:

* **Importante:**

Se precisar informar o**intermediador,** no pedido de vendas preencher o campo **Presença Com C5\_INDPRES =** **1, 2, 3 ou 9.**

Para ***gerar o intermediador*** realizar os passos abaixo:

1. Preencher o intermediador em  Faturamento -> Cadastros -> Intermediadores **Nome "A1U\_NOME" e CNPJ "A1U\_CGC"**

**![20220401_150016.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939015508375)**

        2.  Preencher o  no pedido de vendas **Presença Com** "**C5\_INDPRES"**  igual a  **2**, **3**,ou **9;**

**![20220401_150932.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939015515159)**

    3.  Preencher no **Pedido de Venda Cod. Intermed** "**C5\_CODA1U";**

**![20220401_151123.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16939027450263)**

         4. Após isso, ***transmita novamente a Nota fiscal eletrônica.***

Obs: Abaixo segue vídeo dos campos que é ***necessário o preenchimento.***

* **Importante:**

Lembrando que opção  **4=*NFC-e em operação com entrega a domicílio,*** não é apresentada no pedido de vendas, apenas no módulo do loja.

Se o campo não for preenchido, caso seja nota do tipo normal, **conforme o fonte do NFESEFAZ**, será levado como **9- Operação não presencial, outros.**

Caso seja **nota de devolução, conforme o fonte do NFESEFAZ abaixo:**

![indpres_fonte.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/16939108289815)

1- Para nota de devolução  preencher o campo do TES **"Venda Pres."****F4\_VENPRES=1** na montagem da tag **indPres=1 – Operação Presencial**.

![venda_presencial_TES.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002491502)

2- Após isso, **exclua a nota e gere novamente.**

3- Se não for preenchido será gerado como **0=*Não se aplica.***

* **Saiba mais:**

Para a TAG **indPres** **2**, **3**, ou **9 notas de entrada ou transferência entre filias ou solicitação de transferência:**

* O boletim **está disponível no link abaixo:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=604531498>

**Obs:** **Transferência entre Filiais ou Solicitação de Transferência** os fontes devem ser atualizados, desta forma será levado automaticamente como  **0 sem intermediador.**

* **Validação da Sefaz:**

**![434_rejei__o.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405489962263)**
