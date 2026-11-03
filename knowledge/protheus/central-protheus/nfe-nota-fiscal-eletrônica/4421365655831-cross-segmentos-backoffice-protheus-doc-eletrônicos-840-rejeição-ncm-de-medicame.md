---
article_id: 4421365655831
category: NFe - Nota Fiscal Eletrônica
content_hash: 1d515410661f266611bd1e075f89ed42d5774389aa1d4759f8118bab4b3efbae
fetched_at: '2026-06-28T22:40:05.336444+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 840 Rejeição :
  NCM de medicamento e não informado o grupo de medicamento (med)'
type: support-article
updated_at: '2025-07-09T12:02:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421365655831-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-840-Rejei%C3%A7%C3%A3o-NCM-de-medicamento-e-n%C3%A3o-informado-o-grupo-de-medicamento-med
---

**Dúvida**Como solucionar a 840 Rejeição : NCM de medicamento e não informado o grupo de medicamento (med)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Importante:**

**NT 2021.004\_V\_1.34 Suspensão da regra K01-10 e alteração na regra K01-20 homologação 23/09/2022 e produção 27/09/2022****Observação 4: Implementação futura**

Os medicamentos são classificados nos ***NCMs*** que começam com ***3001, 3002, 3003, 3004, 3005 e 3006.***

1. Se o produto não for medicamento altere o NCM para diferente de iniciados com  ***3001, 3002, 3003, 3004, 3005 e 3006  no campo*** **Pos.IPI/NCM** **B1\_POSIPI.**

![20220328_085322.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5066824021015)

2. Após isso, ***retransmita a nota.***

3. Se o NCM estiver correto para o grupo de medicamentos iniciado por ***3001, 3002, 3003, 3004, 3005 e 3006.***  Habilitar a rotina de medicamentos,**configurar** o parâmetro  **MV\_MEDICA = (Com o código do grupo de produto) Para alteração do parâmetro, acessar o módulo Configurador (SIGACFG), em seguida em Ambiente / Cadastros / Parâmetros clicar em editar:**

**![20220328_090727.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5067082194199)**

4. **Preencher o campo Grupo B1\_GRUPO  no Cadastro de produto o** conteúdo informado no parâmetro MV\_MEDICA.

![20220328_090955.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5067148660759)

5. Preencha os campos no módulo dos ***Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos > Medicamento***  
  
![20220328_090423.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5067039872663)

**Importante:**

Para o grupo de medicamento é necessário que seja gerado o grupo do rastro na **F0A**  inserir na **T0 um grupo** que já é utilizado no campo **B1\_GRUPO** cadastro de Produto no parâmetro MV\_MEDICA.

No campo **B1\_GRUPO** deve ser informado o código da chave da tabela **T0 da SX5.**

1- Ao entrar no configurador entre em **Bases de Dados -> Dicionário -> Bases de Dados.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347303546135)

2- Selecionar **Tabelas Genéricas:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347256214295)

3- Procurar por **T0 e clicar em editar**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347256215319)

4- O conteúdo da **Chave é o código da T0** que será incluído no campo **B1\_GRUPO,** cadastrar ou utilizar um já existente:

![T0_CONFIGURADOR.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33347303551639)

5- Incluir no cadastro do produto uma Chave existente na **tabela T0 no campo B1\_GRUPO "GRUPO":**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347256218903)

6- Para gerar de forma ***Manual realizar a configuração abaixo:***

Para quem não controla **Lote na SB8** , será habilitada a rotina de rastreabilidade nos Livros Ficais para digitar as informações de forma manual.

Após gerar a nota, acesse: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos.**

* **Na opção Rastreabilidade**

![RASTREABILIDADE.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33347303554455)

7- Para gerar de forma ***automática gerar conforme abaixo:***

* Caso já haja controle de **lote na tabela SB8**, deve ser configurado a **T0 na SX5** e o campo B1\_GRUPO deve ser preenchido e habilitar o parâmetro abaixo para preenchimento automático da F0A .

* Habilitar o parâmetro no configurador **MV\_ATUCOMP =.T.**

* **IMPORTANTE:**

Este campo é preenchido apenas manualmente.

* **F0A\_CODAGR**

Lembrando que a TAG cAgreg **não** é obrigatória.

Este campo faz parte do **Grupo I80 (Rastreabilidade do Produto).** A partir dessa atualização passa a ser **Alfanumérico** e continua sendo não obrigatório, conforme o boletim do link abaixo:

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=624111487)

* Para que o campo seja **Alfanumérico é necessário realizar as atualizações do link abaixo:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714)

**Observação:**

* Para controlar lote no produto **segue abaixo o link da FAQ:**

<https://tdn.totvs.com/pages/viewpage.action?pageId=367232994>

* ***Impressão no Danfe:***

O Lote é gerado apenas no XML.

Não existe até o momento um layout da Sefaz para que seja apresentada a informação do Lote, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA e F4\_FORMULA.**

* **Saiba mais:**

***Observação 1:*** Regra de validação a ***critério da UF.***

***Observação 2:*** Os medicamentos são classificados nos NCMs que começam  
com ***3001, 3002, 3003, 3004, 3005 e 3006***

***Observação 3:*** Para os medicamentos que não possuam código de Produto  
da ANVISA, ***o campo cProdANVISA do Grupo de Medicamentos*** deverá ser preenchido com o literal **“ISENTO”**

1. Para configurar observação 3, preencher o complemento de medicamentos do campo ***Cod. Anvisa CD7\_CODANV = ISENTO.***

**​**

![20220328_094857.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/5067891364247)

* **Saiba mais:**

Conforme o fonte do NFESEFAZ abaixo, os campos que devem estar preenchidos na tabela CD7:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347303555735)

* O campo **CD7\_MOTISE** não é obrigatório, referente a TAG ***xMotivoIsencao.***

* **Saiba mais:**

Para automatizar os complementos, utilize o ***Ponto de Entrada MATUCOMP:***  
   
[Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Ponto de entrada MATUCOMP](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048643294-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Ponto-de-entrada-MATUCOMP?source=search)

O Lote é gerado apenas no XML.

Até o momento, não existe um layout da Sefaz para que seja apresentada a informação do Lote, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um campo padrão para gerar a mensagem em informações complementares, como exemplo ***C5\_MENNOTA e F4\_FORMULA.***

* ***Validação da Sefaz:***

![840_rejei__o.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4421372808471)

**Baixe o vídeo para verificar o preenchimento desde o configurador da forma Manual e automático:**
