---
article_id: 19804481955351
category: Materiais - Compras (SIGACOM)
content_hash: abc8554afbaf6858062482c71972c917b98578a2cfa308dbbcb3ed87000034cf
fetched_at: '2026-06-28T22:41:15.779191+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é definido o bloqueio
  simples da Solicitação de Compras ( MATA110 ) no Módulo de Compras ?
type: support-article
updated_at: '2025-12-11T11:25:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19804481955351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-definido-o-bloqueio-simples-da-Solicita%C3%A7%C3%A3o-de-Compras-MATA110-no-M%C3%B3dulo-de-Compras
---

**Dúvida**

Como é definido o bloqueio simples da Solicitação de Compras ( MATA110 ) no Módulo de Compras ?

**Ambiente**

Microsiga Protheus a partir da versão 11

**Solução**

Para definir o bloqueio simples da Solicitação de Compra é necessário habilitar o paramêtro **MV\_APROVSC = T**e o paramêtro **MV\_APRSCEC** deve estar desabilitado **(F)**, ou seja, o Bloqueio Simples não funciona caso a alçada de SC esteja Ativada.

Caso não deseje ultilizar o cadastro de solicitantes, o paramêtro **MV\_CHKSOLI** também deve estar desabilitado (F), caso o paramêtro esteja habilitado será obrigatório realizar o cadastro de solicitantes na rotina **MATA084**.

Ao ultilizar o bloqueio simples a liberação da Solicitação de Compras é realizada diretamente na rotina, ao acessar o menu Outras Ações>Aprovação:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19804466442135)

**Obs1:**

Por padrão a Solicitação de Compra deve ser aprovada por item, ou seja, caso a SC possua 5 itens será necessário realizar 5 aprovações, porém ao acessar os paramêtros da rotina, teclando F12 existe a opção de selecionar se a aprovação deve ser realizada por item ou por SC, caso seja escolhido a aprovação por SC não é nessário aprovar diversas vezes o mesmo registro.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19804449963799)

**Obs2:**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como impedir o Solicitante de aprovar a própria Solicitação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018354991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-impedir-o-Solicitante-de-aprovar-a-pr%C3%B3pria-Solicita%C3%A7%C3%A3o-de-Compras-)

**Obs3:**

No **Bloqueio Simples** da Solicitação de Compra, não é gerado registro na tabela SCR. E a aprovação deve ser realizada na própria rotina da Solicitação de Compras. Se utilizar o **Bloqueio por Entidade Contábil** da Solicitação de Compra, será gerado registro na SCR e a Solicitação deverá ser aprovada na rotina de **Liberação de Documentos MATA094.**Os registros gerados na SCR servem como um histórico de aprovação.

**Saiba Mais :**

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Trilha de Videos Restrição de Solicitantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491127349911)

[PCOM09005 - Solicitantes (MATA084)](http://tdn.totvs.com/pages/releaseview.action?pageId=274630904)

[PCOM06003 - Como funciona o bloqueio de solicitação de compras?](https://tdn.totvs.com.br/pages/releaseview.action?pageId=233754768) 

[PCOM06006 - Cadastro de Solicitante e Solicitação de Compra](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=286735615)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alçada de Solicitação de Compras por Entidade Contábil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017527952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Al%C3%A7ada-de-Solicita%C3%A7%C3%A3o-de-Compras-por-Entidade-Cont%C3%A1bil)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como impedir o Solicitante de aprovar a própria Solicitação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018354991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-impedir-o-Solicitante-de-aprovar-a-pr%C3%B3pria-Solicita%C3%A7%C3%A3o-de-Compras-)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
