---
article_id: 23503197928087
category: Financeiro - Reinf
content_hash: 35701ef2aa23f354674faa03bb24327e8595486289c303a9b541944e6bbeabdb
fetched_at: '2026-06-28T22:37:51.687215+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA989 - Extrator Fiscal - Processo
  de Suspensão
type: support-article
updated_at: '2026-02-10T18:22:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/23503197928087-Cross-Segmentos-Backoffice-Linha-Protheus-FINA989-Extrator-Fiscal-Processo-de-Suspens%C3%A3o
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/23511457714583)**Tempo aproximado para leitura: **00:10 min**

**Dúvida**  
Como realizar o processo de suspensão?

**Ambiente**  
Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Reinf - A partir da versão 12.1.2210.

**Solução**

A princípio, será necessário criar alguns cadastrados, sendo:

**Cadastro Complemento do imposto.**

1. No módulo **Financeiro (SIGAFIN)**, acesse **Atualizações -> Cadastro -> Complemento do Imposto (FINA985).**

2. Clique em **Incluir** para um novo cadastro, preencha os campos obrigatórios conforme necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164643607)

Dúvida no preenchimento dos campos, segue abaixo o link da documentação detalhada.

[Complemento Cadastral](https://tdn.totvs.com/pages/releaseview.action?pageId=280734739)

**Cadastro de Processos Referenciados**

1. No módulo **Livros Fiscais (SIGAFIS),** acesse **Atualizações -> SPED -> Processos referenciados (MATA967).**

2. Clique em **Incluir** para um novo cadastro, preencha os campos obrigatórios conforme necessidade.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164647959)

Dúvida no preenchimento dos campos, segue abaixo o link da documentação detalhada.

[Processos referenciados](https://tdn.totvs.com/pages/releaseview.action?pageId=344473870)

**Cadastro Fornecedor**

1. No módulo **Financeiro (SIGAFIN),** acesse **Atualizações -> Cadastro -> Fornecedor -> Localizar -> Alterar.**

2. No cadastro dos **Fornecedores,** clique em **Outras Ações**, **Processos Ref. (REINF)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503197880087)**

Preencha o **número do processo** e **o tipo do processo.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164679319)**

**Documento de Entrada**

Após incluir as informações da nota no **documento de entrada**, ao clicar em **Salvar** será exibida a mensagem abaixo, clique em **“SIM”.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164681879)**

Em seguida, apresentará a tela abaixo para informar a suspensão. Neste cenário, a **suspensão é do COFINS**. Informar o **processo de suspensão**, o **tipo do processo** e a **base de suspensão do COFINS. Por** fim**, salvar.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503197889303)**

Assim que incluída a nota no sistema, serão alimentadas as tabelas **DHR** e **FKW**, deverá constar o número do processo preenchido, conforme imagem abaixo:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164687255)**

**Financeiro**

No **Financeiro,** o processo é diferente. Após incluir as informações do **título**, clique em **Outras Ações,** **complemento do título** e preencha os campos referenciados abaixo.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503197893655)**

Após a inclusão da nota, será gerada a **FKW** com a informação da suspensão.

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164691863)**

**Baixa.**

Ao realizar a baixa, não será apresentado o imposto, caso o parâmetro **MV\_BX10925** seja na baixa, sendo na emissão, não gera o **TX.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/23503164695959)

**Extrator Fiscal**

Após executar o **Extrator Fiscal,** será gerado o registro **T158AC** em casos de s**uspensão do PCC e IRRF** **na baixa.**

|T158|1010||F03IRPC01|20240515|0||20240515|01|||

|T158AA|15002|20000|2||||||

|T158AB|11|20000|200|0|

**|T158AC|97000997|1||11|200|20000|0|0| => Indicando o número do processo da Suspensão e o seu valor**

|T158AB|18|20000|600|0|

|T158AB|10|20000|130|0|

**Saiba mais**

[Fique por dentro das atualizações Reinf Protheus](https://tdn.totvs.com/display/public/PROT/Protheus+-+REINF+Suporte+Financeiro#Eventos--839875140)

[PROCESSOS REINF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19775578473751-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-How-To-Bloco-40-Gera%C3%A7%C3%A3o-dos-layouts-T154-e-T158)

[Reinf Financeiro evento R-4010](https://tdn.totvs.com/pages/releaseview.action?pageId=736178352#Reinf_R4010_inclus%C3%A3o_de_t%C3%ADtulo-05.T%C3%ADtuloapagarcomsuspens%C3%A3odeIR)
