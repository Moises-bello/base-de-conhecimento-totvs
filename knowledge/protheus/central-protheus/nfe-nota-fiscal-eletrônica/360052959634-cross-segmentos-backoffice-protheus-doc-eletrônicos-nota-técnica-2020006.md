---
article_id: 360052959634
category: NFe - Nota Fiscal Eletrônica
content_hash: bdc5847787ae57c72a5838bc852d98275a2a87899731cb59235d822ab48ff3f1
fetched_at: '2026-06-28T22:40:06.999648+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Nota técnica 2020.006
type: support-article
updated_at: '2025-07-09T11:54:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052959634-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Nota-t%C3%A9cnica-2020-006
---

**Dúvida**Quais são as atualizações e procedimentos necessários para configuração da NT 2020.006 ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões

Cross Segmentos - TSS - a partir da versão 12

**Solução**

* **Importante:**

Para a versão 1.31 não será necessário realizar nenhuma manutenção no Protheus o TSS, foi acrescentada as ***exceções 3 e 4 na regra de validação 523.***

**O prazo previsto para a Nota Técnica 2020.006 v1.31 é:**

* Ambiente de Homologação (ambiente de teste das empresas): até **03/10/2022**
* **Ambiente de Produção:  10/10/2022**

[Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 523 Rejeição : CFOP não é de Operação Estadual e UF emitente igual à UF destinatário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005515481)

Para solucionar as ***versões anteriores*** essa dúvida, realize os seguintes passos:

**1. Atualização do ambiente TSS (repositório e schemas)**

1. Atualizar o **repositório** com o último pacote de **expedição continua do TSS** disponível no link:

[MP - TSS - Atualização do Repositório (RPO) do TSS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500004215981)

    2. Atualizar a pasta **SCHEMAS** presente na estrutura do TSS através do link:

<https://suporte.totvs.com/portal/p/10098/download?e=761857>

**Saiba Mais:** [TSS - Atualização dos SCHEMAS](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025103552)

**2. Atualização do ambiente Protheus:**

1. Aplicar o **Pacote Acumulado Documentos eletrônicos:**

[Clique aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=525010692)

     2. **Compilar RDMAKE NFESEFAZ** (se emitir NF-e) presente no link abaixo:

<https://suporte.totvs.com/portal/p/10098/download?e=1152113>

* **Saiba mais:**

Lembrando que **RDMAKE não possui Release** sendo assim, pode ser aplicada em qualquer uma todos os pacotes.

    3. Rodar o **Dicionário de Dados para a criação dos novos campos :**

<https://suporte.totvs.com/portal/p/10098/download?e=1013133>

Pacote de dicionário centralizado para atendimento da NT 2020.006 referente a intermediador da operação de vendas e compras, com desenvolvimento das **áreas do Protheus: Compras, controle de lojas (SIGALOJA), Faturamento e Callcenter (SIGAFAT), e TSS. Compatível com Release 12.1.23 até 12.1.27.**

Na release ***12.1.33*** o menu e os campos já estão disponíveis, ***não é necessário rodar o dicionário.***

**3. Criação dos Parâmetros:**

1. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar Observação: **Para ambiente homologação** será necessário criar o parâmetro **MV\_NT2006I** com a data de **01/03/2021** conforme documentos disponibilizados pelos módulos abaixo. 

![MV_NT2006I.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/16914066762775)

* **Importante:**

Para os clientes que utilizam Varejo - Controle de lojas ou TOTVSPDV, configurar o parâmetro

**MV\_NT2006P:** 03/05/2021 

Maiores detalhes dos parâmetros abaixo:

[Clique Aqui](https://tdn.totvs.com.br/pages/releaseview.action?pageId=626650334#samples-1)

2.Para inclusão/alteração dos parâmetros, acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /** **Cadastros / Parâmetros** clicar em **incluir** e informar:

**Parâmetro****utilizado em operações de saída (Faturamento):**

Nome de Var.: **MV\_MFATIPR**

Tipo: **1 - Caractere**

Cont. Por: **"Negociacao Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-17.png?version=1&modificationDate=1625007797530&api=v2)

**Parâmetro****utilizado em operações de entrada (Compras):**

Nome de Var.: **MV\_TPAGCOM**

Tipo: **1 - Caractere**

Cont. Por: **"Negociacao Futura"**

![](https://tdn.totvs.com.br/download/attachments/626650334/image2021-6-29_20-3-47.png?version=1&modificationDate=1625007828070&api=v2)

* ***Saiba mais:***

***Para verificar o boletim técnico:***

[Clique Aqui](https://tdn.totvs.com.br/pages/releaseview.action?pageId=626650334)

* **O prazo previsto para a Nota Técnica 2020.006 v1.30 é:**

* Ambiente de Homologação (ambiente de teste das empresas): até **23/08/2021**
* **Ambiente de Produção: 04/04/2022**

 Alterada apenas a regra de validação da rejeição ***434,* regra B25c-10 para exigir o campo indIntermed** para validação apenas de notas de saída.

Para solucionar essa dúvida, realize os seguintes passos:

1. Para solucionar a rejeição ***realizar todas as atualizações,** a*pós as atualizações seguir ***os passos do artigo abaixo:***

[Cross Segmentos - Backoffice Protheus - 434 Rejeição : NF-e sem indicativo do intermediador](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062802333)

     2. ***Exclua a nota*** e gere novamente.

* O boletim **está disponível no link abaixo:**

[https://tdn.totvs.com/pages/releaseview.action?pageId=60453149](https://tdn.totvs.com/pages/releaseview.action?pageId=604531498)

* Para mais informações ***temos o espaço legislação:***

*[Espaço Legislação](https://www.totvs.com/blog/fiscal-clientes/nf-e-nfc-e-nota-tecnica-2021-004-v-1-0-inclui-novas-regras-de-validacao-e-campos/)*

* Haverá até o momento três Viradas de **versão 1.10, 1.20 e 1.30 conforme abaixo:**

![2020.006_v_1.30.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/4405496891159)
