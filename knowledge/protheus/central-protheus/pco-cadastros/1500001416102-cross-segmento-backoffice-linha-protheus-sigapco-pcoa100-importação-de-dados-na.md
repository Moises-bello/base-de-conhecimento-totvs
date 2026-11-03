---
article_id: 1500001416102
category: PCO - Cadastros
content_hash: 96c29ba0f62cb440fb8a5b995389e96cbeaf7d1605cb0ecdc2808cf4dfaed190
fetched_at: '2026-06-28T22:37:12.905005+00:00'
product: protheus
section_id: 1500001550802
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA100 Importação de
  Dados na Planilha Orçamentaria
type: support-article
updated_at: '2025-05-05T14:47:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001416102-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA100-Importa%C3%A7%C3%A3o-de-Dados-na-Planilha-Or%C3%A7amentaria
---

**Dúvida**

**Como Realizar a Importação de Dados da Planilha Orçamentaria**

Esta funcionalidade possibilita a integração do módulo Planejamento e Controle Orçamentário (SIGAPCO), através da Planilha Orçamentária (PCOA100), importando informações de outro ERP, por meio de arquivos XML.  
  
**Ambiente**  
Cross Segmento - Backoffice Linha Protheus  
  
**Solução**

No **Planejamento e Controle Orçamentário (SIGAPCO)**  cadastrar os seguintes itens:

**Menu :  Atualizações → Cadastros;**

* Contas Orçamentárias ->**(PCOA010)**
* Classes Orçamentárias  ->**(PCOA020)**
* Centros de Custos -> **(****CTBA030)**
* Item contábil  -> **(****CTBA040)**
* Classe de Valor -> **(****CTBA060)**
* Operações ->**(PCOA080)**

**Menu :  Atualizações → Planilhas;**

* **Orçamentos -> (PCOA100)**
* OBS: Cadastrar uma planilha orçamentária vinculada a um conta orçamentária que receberá os valores a serem importados

No **FINANCEIRO (SIGAFIN)** cadastrar os seguintes itens:

**Menu : Atualizações → Cadastros**

* Fornecedores ->**(MATA020)**
* Naturezas ->**(FINA010)**

**Menu : Atualizações → Contas a Pagar → Contas a Pagar**

* Contas a Pagar ->**(FINA050)**

**Importação de dados do ERP através do arquivo XML, para a Área de Integração**

1.        No **Planejamento e Controle Orçamentário (SIGAPCO)** acesse **Miscelânea / Reprocessamentos / Lctos. Integração (PCOA009)**.

2.        O sistema apresentara a tela de importação

3.        Clique em **Importar XML**.

**Importação de dados do ERP através dos pontos de lançamentos**

1.         No **Planejamento e Controle Orçamentário (SIGAPCO)** **acesse Atualizações / Lançamentos / Por processo (PCOA040)**.

2.          Habilite o processo que deseja importar.

3.          É permitido o reprocessamento do processo escolhido, que neste caso é a importação de Títulos a Pagar do módulo **Financeiro (SIGAFIN)**.

4.          Selecione o processo 000002, item 01

5.          Altere o campo **Perm. Reproc?** para **Sim**.

2 -  **Importação dos dados da Área de Integração para a Planilha Orçamentária**

1.        No Planejamento **e Controle Orçamentário (SIGAPCO)** acesse  **Planilhas / Orçamentos (PCOA100)**.

2.        Posicione na Conta Orçamentária a receber os dados

3.        Clique em **Ferramentas**.

4.        Clique no item **Importar dados Integração** **(PCOA106)**.

5.        É  exibido o assistente de importação dos dados da Área de Integração.

6.        Deixe em branco os campos **Processo?** e **Item?** para que o assistente identifique a origem nos arquivos XML.

7.        Preencha os demais campos conforme *help* de campo

8.        Clique em **Finalizar**.

**Para utilizar o Assistente para dados do ERP**

1.        No Assistente de Importação preencha os campos **Processo?** e Item? Com o número de processo **000002** e o Item **01**.

2.        Preencha os demais campos conforme *help* de campo

3.        Clique em **Finalizar**.

O Engine de Integração auxilia o desenvolvimento do orçamento, disponibilizado por meio de integração de diferentes módulos do Microsiga Protheus, unificando as informações em apenas um lugar.

É necessário realizar todos os cadastros e configurações padrão do Planejamento e Controle Orçamentário (SIGAPCO), com o cadastro da planilha orçamentária e as entidades. O Engine de integração deve ser configurado para realizar o vínculo entre **Engine** x **Planilha orçamentária** x **Entidades da planilha**. É possível realizar uma carga inicial para atualização dos dados de orçamento da planilha.

Esta atualização acontece da seguinte forma:

**Leitura do arquivo XML**

O sistema utilizado gera o arquivo XML com o *layout* definido e o disponibiliza na pasta desejada pelo usuário.

**Layout do Arquivo XML**

***ESSE LAYOUT É OBRIGATORIO!***

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001336982)***

* **IdProcesso**: Número de identificação da importação,  campo **Chave** (AMJ\_CHAVE);
* **DtMovimento**: Data da importação do arquivo -> **Data**(AMJ\_DATA);
* **DtPlanej**: Data do registro-> **Data Planej.** (AMJ\_DATPLA);
* **Valor**: Valor do item -> **Vlr. Lancto** (AMJ\_VALOR1);
* **CO**: conta orçamentária ->  **Conta Orçam.** (AMJ\_CO);
* **Classe**: classe orçamentária -> **Classe Orc.** (AMJ\_CLASSE);
* **Oper**: operação -> **Operação**(AMJ\_OPER);
* **CC**: centro de custo  -> **Centro Custo**(AMJ\_CC);
* **ItCtb**: item contábil -> **It. Contábil** (AMJ\_ITCTB);
* **ClVlr**: classe de valor ->  **Classe Valor**(AMJ\_CLVLR);
* **IdRef**:  é o número sequencial  item de cada lote -> **Item** (AMJ\_ID);
* **Tipo**: define se o lançamento é **1**=Crédito/**2**=Débito ->  **Tipo**(AMJ\_TIPO);.

 O Engine de Integração decodifica este arquivo XML e grava suas informações na tabela **AMJ – Área de Integração do PCO**.

**Importação dos dados via Pontos de Lançamento**

O Engine de Integração busca a configuração dos pontos de lançamento e através delas, insere a tabela da área de integração.

A configuração do Engine de Integração deve ser realizada para todas as planilhas orçamentárias que dependam de resultados de processamento de outros ERPs.

**Exemplo : Arquivo de interação  xml para integração ( Processo 000001 - Contas a Receber).**

**Arquivo de interação xml para integração**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001337042)

Entrar na tela de Integração

No **Planejamento e Controle Orçamentário (SIGAPCO)** acesse :

Miscelânea / Reprocessamentos / Lctos. Integração (PCOA009).

**IMPORTANTE :** Antes de iniciar a execução certifique-se que todas as informações a serem importadas estejam pré cadastradas no sistema :

No exemplo acima utilizamos : Conta Orçamentaria,  Classe, Item Contábil, Classe de valor e a Planilha orçamentária vinculada  a Conta Orçamentaria.

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_11-52-5.png?version=1&modificationDate=1543589525087&api=v2)

**Clicar no Botão -> Importar xml,**  preencher parâmetros de acordo com dados que estão disponíveis no  aquivo xml.

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_11-53-49.png?version=1&modificationDate=1543589629570&api=v2)

Será exibido tela de reprocessamento com sucesso

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_13-38-8.png?version=1&modificationDate=1543595888857&api=v2)

Após efetuado os processos acima entrar em Planilhas Orçamentária **PCOA100**  e seguir os processos abaixo:

**Menu ->**  Atualizações / Planilhas / Orçamento

Alterar planilha

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_13-40-41.png?version=1&modificationDate=1543596042003&api=v2)

Posicionar na conta orçamentaria que receberá os valores

Pressionar Outras Ações / Ferramentas / Importar dados de Integração

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_13-42-33.png?version=1&modificationDate=1543596153110&api=v2)

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_13-43-46.png?version=1&modificationDate=1543596226403&api=v2)

![](https://tdn.totvs.com/download/attachments/439706297/image2018-11-30_13-44-43.png?version=1&modificationDate=1543596283600&api=v2)

Veja abaixo que os Itens Orçamentários são preenchidos de acordo com arquivo xml importado

![](https://tdn.totvs.com/download/attachments/439706297/image2019-5-7_15-10-40.png?version=1&modificationDate=1557252640470&api=v2)

![](https://tdn.totvs.com/download/attachments/439706297/image2019-5-7_15-10-12.png?version=1&modificationDate=1557252612387&api=v2)

**IMPORTANTE:** Caso necessitar que estes movimentos sejam inclusos na rotina **PCOA050  Lançamentos**  configurar o processo 000252.

### Veja no link abaixo o vídeo demonstrativo de como importar a planilha orçamentária:

**[HOW TO - Como importar planilha orçamentária](https://youtu.be/nagrXJ3ELk4)**
