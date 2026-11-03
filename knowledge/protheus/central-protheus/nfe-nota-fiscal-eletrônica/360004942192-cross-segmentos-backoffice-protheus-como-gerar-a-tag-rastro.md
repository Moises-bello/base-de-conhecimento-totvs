---
article_id: 360004942192
category: NFe - Nota Fiscal Eletrônica
content_hash: edf6dc8456c6c3aa120df85f1189ce08156c11275b4e32fdd271398d5f643a32
fetched_at: '2026-06-28T22:39:59.971201+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Como gerar a TAG rastro
type: support-article
updated_at: '2025-12-05T13:59:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004942192-Cross-Segmentos-Backoffice-Protheus-Como-gerar-a-TAG-rastro
---

**Dúvida**

Como gerar o Grupo de TAGS de Rastro (tabela F0A) ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Importante:**

Pode ser criado um **novo grupo** ou inserir na **T0 um grupo** que já é utilizado no campo **B1\_GRUPO** no cadastro de Produto.

No campo **B1\_GRUPO** deve ser informado o código da chave da tabela **T0 da SX5.**

1- Ao entrar no configurador entre em **Bases de Dados -> Dicionário -> Bases de Dados.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046865873)

2- Selecionar **Tabelas Genéricas:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046866593)

3- Procurar por **T0 e clicar em editar**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046866713)

4- O conteúdo da **Chave é o código da T0** que será incluído no campo **B1\_GRUPO,** cadastrar ou utilizar um já existente:

![T0_CONFIGURADOR.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006789432)

5- Incluir no cadastro do produto uma Chave existente na **tabela T0 no campo B1\_GRUPO "GRUPO":**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046009134)

6- Para gerar de forma ***Manual realizar a configuração abaixo:***

Para quem não controla **Lote na SB8** , será habilitada a rotina de rastreabilidade nos Livros Ficais para digitar as informações de forma manual.

Após gerar a nota, acesse: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos.**

* **Na opção Rastreabilidade**

![RASTREABILIDADE.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360006825071)

7- Para gerar de forma ***automática gerar conforme abaixo:***

* Caso já haja controle de **lote na tabela SB8**, deve ser configurado a **T0 na SX5** e o campo B1\_GRUPO deve ser preenchido e habilitar o parâmetro abaixo para preenchimento automático da F0A .

Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em **editar** **MV\_ATUCOMP =.T.**

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
