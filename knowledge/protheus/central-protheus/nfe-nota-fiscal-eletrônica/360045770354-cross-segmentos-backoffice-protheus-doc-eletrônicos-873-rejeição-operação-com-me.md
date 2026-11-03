---
article_id: 360045770354
category: NFe - Nota Fiscal Eletrônica
content_hash: c8a7833b90b744ab84bfa1efa3731f4b8eb384e109ab0aba688d3143adaeebe7
fetched_at: '2026-06-28T22:40:03.312965+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos -  873 Rejeição :
  Operação com medicamentos não informado os campos de rastreabilidade'
type: support-article
updated_at: '2025-07-09T12:00:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045770354-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-873-Rejei%C3%A7%C3%A3o-Opera%C3%A7%C3%A3o-com-medicamentos-n%C3%A3o-informado-os-campos-de-rastreabilidade
---

**Dúvida**Como resolver a rejeição abaixo:

873 Rejeição : Operação com medicamentos não informado os campos de rastreabilidade ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

**Importante:**

Pode ser criado um **novo grupo** ou inserir na **T0 um grupo** que já é utilizado no campo **B1\_GRUPO** no cadastro de Produto.

No campo **B1\_GRUPO** deve ser informado o código da chave da tabela **T0 da SX5.**

1. Ao entrar no configurador entre em **Bases de Dados -> Dicionário -> Bases de Dados.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347229138839)

2. Selecionar **Tabelas Genéricas:**

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347276407063)

3. Procurar por **T0 e clicar em editar**

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347229141143)

4. O conteúdo da **Chave é o código da T0** que será incluído no campo **B1\_GRUPO,** cadastrar ou utilizar um já existente:

![T0_CONFIGURADOR.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33347276408471)

5. Incluir no cadastro do produto uma Chave existente na **tabela T0 no campo B1\_GRUPO "GRUPO":**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347229145751)

**6. Opção Manual**

Para quem não controla **Lote na SB8** , será habilitada a rotina de rastreabilidade nos Livros Ficais para digitar as informações de forma manual.

Após gerar a nota, acesse: **Livros Fiscais > Atualizações > Movimentos > NF-e Manual de Entrada / Saída > Complementos.**

* **Na opção Rastreabilidade**

![RASTREABILIDADE.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/33347229146647)

7. Opção Automático:

* Caso já haja controle de **lote na tabela SB8**, deve ser configurado a **T0 na SX5** e o campo B1\_GRUPO deve ser preenchido e habilitar o parâmetro abaixo para preenchimento automático da F0A .

* Habilitar o parâmetro no configurador **MV\_ATUCOMP =.T.**

**IMPORTANTE:**

De forma automático apenas um campo deve ser preenchido manualmente.

* **F0A\_CODAGR**

Lembrando que a TAG cAgreg **não** é obrigatória.

**Observação:**

* **Para controlar lote no produto segue abaixo o link da FAQ:**

<http://tdn.totvs.com/display/public/PROT/PEST10008+-+RASTREABILIDADE+CONTROLE+DE+LOTE>

* **Impressão no Danfe:**

O Lote é gerado apenas no XML.

Não existe até o momento um layout da Sefaz para que seja apresentada a informação do Lote, ou seja, não foi criado um novo campo no Danfe, e não há nenhuma informação na nota técnica sobre a obrigatoriedade de mensagem.

Caso seja uma solicitação da Sefaz do seu estado, poderá utilizar um padrão para gerar a mensagem em informações complementares, como exemplo **C5\_MENNOTA e F4\_FORMULA.**

* **Saiba mais:**

Caso tenha gerado o grupo das **TAGS do med** indevidamente segue abaixo a documentação para revisão do cadastro:

*[MP - NFE - Como gerar as TAGs rastro e med (Detalhamento Específico de Medicamento e de matérias-primas farmacêuticas)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004922252)*

* **Importante:**

**NT 2021.004\_V\_1.34  Alteração na regra K01-20 homologação 23/09/2022 e produção 27/09/2022**

* Se tiver gerado o grupo de **TAGS med** no XML deve ser gerado também o grupo de **TAGS do rastro.**

***Exceção 1:*** Regra de Validação não se aplica para

NF-e de devolução ***(finNFe = 4)***

1. Para nota de devolução **retirar o CFOP** do parâmetro **MV\_DEVCFOP** caso tenha informado.

2. Verificar se a nota foi **referenciada ao documento**de origem corretamente:

D2\_ITEMORI, D2\_SERIORI, D2\_NFORI **(nota de saída)**  
  
D1\_ITEMORI, D1\_SERIORI, D1\_NFORI **(nota de entrada)**

**Importante:**

Lembrando que a nota só é **referenciada no XML** caso exista no sistema.

Se a mesma for referenciada manualmente deve se preencher os campos **NF . Ori , Serie Ori e Item Ori** .   
  
Se for preenchido automaticamente pelo gatilho **F4 (Nota de saída) ou F7 (Nota entrada)** os campos são alimentados automaticamente.

3. Verificar  se o campo na TES **F4\_AJUSTE -> Ajuste CIAP = N**, pois se estiver como Sim irá gerar **FINNFE = 3.**

4. Após isso, exclua a nota e gere novamente.

**Saiba mais:**

É possível consultar a **nota técnica 2013.005\_v\_1.22** página 130 para saber quais são os CFOPs com finalidade de devolução.

<http://www.nfe.fazenda.gov.br/portal/listaConteudo.aspx?tipoConteudo=tW+YMyk/50s=>

NF-e de Ajuste ***(finNFe=3)***

1. Preencher o campo na TES **F4\_AJUSTE -> Ajuste CIAP = N**, pois se estiver como Sim irá gerar **FINNFE = 3.**

2. Após isso, exclua a nota e gere novamente.

NF-e Complementar ***(finNFe=2)***

***Exceção 2:***Regra de Validação não se aplica para NF-e de venda não  
presencial ***(indPres = 2 ou 3)***

1. No pedido de vendas preencher o campo **Presença Com C5\_INDPRES  2=Operação não presencial, pela Internet; ou 3=Operação não presencial, Teleatendimento;**

**![indpres_1.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/33347276411159)**

***Exceção 3:*** Regra de validação não se aplica para CFOP de venda para  
entrega futura (CFOPs 5116 e 6116) (CFOPs 5922, 6922) ou CFOP de  
Venda à Ordem (5118, 6118, 5119, 6119, 5120 e 6120)

1. Preencher o campo **Cod. Fiscal F4\_CF venda para entrega futura (CFOPs 5116 e 6116) (CFOPs 5922, 6922) ou CFOP de Venda à Ordem (5118, 6118, 5119, 6119, 5120 e 6120)**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33347276411543)

***Exceção 4:*** Regra de validação não se aplica para NF-e de entrada (tpNF=0)
