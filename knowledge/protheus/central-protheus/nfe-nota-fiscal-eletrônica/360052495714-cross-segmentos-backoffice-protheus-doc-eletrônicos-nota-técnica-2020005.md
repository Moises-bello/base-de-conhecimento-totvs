---
article_id: 360052495714
category: NFe - Nota Fiscal Eletrônica
content_hash: 33aa27bcd69931c46829b9377d76f7d2e175bfbc63665d586cc983624d3c78fc
fetched_at: '2026-06-28T22:40:06.987038+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.005
type: support-article
updated_at: '2025-06-18T14:39:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052495714-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2020-005
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2020.005 ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Documentos Eletrônicos - Todas as versões.

**Solução**Liberado o pacote de implementação **da versão 1.10 e 1.20:**

**O prazo previsto para a Nota Técnica 2020.005 v1.20 é:**

* Ambiente de Homologação (ambiente de teste das empresas): até **02/08/2021**
* **Ambiente de Produção: 04/10/2021**

Para solucionar essa dúvida, realize os seguintes passos:

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

**Saiba mais:** <https://tdn.totvs.com.br/pages/releaseview.action?pageId=203755888>

    2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:  
[Cross Segmentos - TSS Transmissão de Documentos Eletrônicos - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Documentos Eletrônicos NFe (Rdmake NFESEFAZ, DANFE) / NFSe / MDFe / MDe](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043005493)

     2. Aplicar  a patch e **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

[Rdmake - NFESEFAZ](https://suporte.totvs.com/portal/p/10098/download#detail/1152113%20)

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

    3. Atualização do **dicionário de dados,** para isso você irá baixar o **Expedição Contínua do módulo fiscal, e executar o UPDDISTR.**

Informações sobre a Expedição Contínua, acessar: [Pacotes de Atualização - Fiscal - P12](https://tdn.totvs.com/pages/viewpage.action?pageId=525823851)

Informações sobre UPDDISTR: [Atualizador de dicionário e base de dados - UPDDISTR](https://tdn.totvs.com/pages/viewpage.action?pageId=181965468)

**3. Criação do Parâmetro:**

1.Para inclusão/alteração do parâmetro, acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar:

Nome de Var.: **MV\_NT2005**

Tipo: **1 - Caractere**

Cont. Por: **"04/10/2021"  -**Informe data menor, caso deseje realizar o envio das alterações em ambiente de Homologação.

![PrintScreen da janela que é utilizada para a criação de parâmetros no módulo SIGACFG](https://tdn.totvs.com/download/attachments/636521118/image2021-8-30_18-14-53.png?version=1&modificationDate=1630358093377&api=v2&effects=drop-shadow "SIGACFG")

Caso não seja criado o parâmetro o PROTHEUS passará a enviar as novas informações à partir de **04/10/2021.**

Se for criado, a validação do preenchimento dos campos se iniciará na data informada, que**não deve ser superior a 02/08/2021.**

**Importante:**a criação do parâmetro não faz distinção entre ambiente de homologação e produção, ou seja, caso o parâmetro esteja criado o preenchimento dos campos também ocorrerá para o ambiente de produção.

* ***Saiba mais:***

***Para verificar o boletim técnico:***

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=636521118)

* Parecer da **Consultoria tributária, relacionada a NT:**

[Clique Aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=624413254)

* **Saiba mais:**

Caso seja necessário gerar as **Tags cBarra e cBarraTrib:**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em incluir **MV\_CAMPBAR**

O parâmetro deverá ser do tipo *string* (1- Caractere) para que sejam adicionados **dois campos customizados** da tabela **SB1.**Os campos deverão ser separados por pipe  "|".

**Exemplo:**  MV\_CAMPBAR  = B1\_BARRA|B1\_BARTRIB

![](https://tdn.totvs.com/download/attachments/649997342/image2021-11-16_10-51-52.png?version=1&modificationDate=1637070713130&api=v2&effects=drop-shadow)

**DEMAIS INFORMAÇÕES**

*Criação* de **Parâmetros manual**no arquivo **SX6 – Parâmetros .**

| **Nome da Variável** | MV\_CAMPBAR |
| --- | --- |
| **Tipo** | CARACTERE |
| --- | --- |
| **Descrição** | Informa campo na tabela SB1 que contem os campos para pegar  as informação para preenher a tag(cBarra) e a tag (cBarraTrib) |
| **Valor Padrão** |  |

**Criação do campo de Manual na Tabela SB1 -conforme exemplo abaixo: B1\_BARRA e B1\_BARTRIB**

**Observação:** poderá ser criado com outros nomes ou aproveitar campos existentes na SB1 caso se enquadre nos requisitos dos campos cBarra e cBarraTrib.

|  |  |
| --- | --- |
| **Campo** | B1\_BARRA |
| **Tipo** | Caractere |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | B1\_BARRA |
| **Descrição** | Código de barras diferente do padrão GTIN |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Preencher com o Código de Barras próprio ou de terceiros que seja diferente do padrão GTIN |

|  |  |
| --- | --- |
| **Campo** | B1\_BARTRIB |
| **Tipo** | Caractere |
| **Tamanho** | 30 |
| **Decimal** | 0 |
| **Formato** | @! |
| **Título** | B1\_BARTRIB |
| **Descrição** | Código de Barras da unidade tributável que seja diferente do padrão GTIN |
| **Usado** | Não |
| **Obrigatório** | Não |
| **Browse** | Sim |
| **Help** | Preencher com o Código de Barras próprio ou de terceiros, que seja diferente do padrão GTIN, correspondente àquele da menor unidade comercializável identificado por Código de Barras |

* Referente as Viradas de **versão 1.10 e 1.20  conforme abaixo****:**

![2020.005_prazo.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4408067100951)

**O prazo previsto para a Nota Técnica 2020.005 v1.21 é:**

* Ambiente de Homologação:**20/10/2021**
* **Ambiente de Produção: 25/10/2021**

* Referente as Viradas de **versão 1.21  conforme abaixo****:**

**![2020.005_V.1.20.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4411028558359)**

* **Importante:**

Para está versão não será necessário realizar nenhum ajuste **em nossos fontes.**
