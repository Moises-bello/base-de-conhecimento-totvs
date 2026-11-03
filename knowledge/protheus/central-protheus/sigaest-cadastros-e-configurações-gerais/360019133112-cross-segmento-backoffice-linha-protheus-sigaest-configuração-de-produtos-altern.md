---
article_id: 360019133112
category: SIGAEST - CADASTROS E CONFIGURAÇÕES GERAIS
content_hash: c11948d9a6254f3d8a660fbe1ccc9d1ee4228deab8f015128840215f1451d356
fetched_at: '2026-06-28T22:39:07.873286+00:00'
product: protheus
section_id: 1500001550022
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Configuração de Produtos
  Alternativos na Ordem de Produção
type: support-article
updated_at: '2021-12-31T11:44:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019133112-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Configura%C3%A7%C3%A3o-de-Produtos-Alternativos-na-Ordem-de-Produ%C3%A7%C3%A3o
---

**Dúvida**O que é e como configurar Produto Alternativo no *Protheus*?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**

É necessário primeiramente cadastrar todos os produtos no programa **MATA010 - Cadastro de Produto**.

Por exemplo no print abaixo com uma estrutura de 1 PA para 1 MP, deve cosntar mais um produto que será o alternativo quando faltar saldo da Matéria prima principal.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417594253591/mceclip0.png)

![](https://totvssuporte.zendesk.com/attachments/token/l3CsWjLCoSCvuPVOBHmqfBLpe/?name=inline1112739524.png)​

Essa relação será considerada sempre que o saldo disponível em estoque do produto origem não suprir totalmente a necessidade para produção. A diferença não atendida pelo produto origem poderá ser  atendida pelo produto alternativo relacionado ao produto origem, de acordo com o cadastro de tipo e fator de conversão. Se ainda assim a necessidade não for totalmente atendida, o  produto original será utilizado, uma vez que é o preferencial.

**Cadastrando o Produto Alternativo**

Após o cadastro selecione o produto que pode ser substituído e clique em **Outras Ações** **>  Alternativos**, neste cadastro preencha a ordem, o produto alternativo, o tipo de conversão, fator de conversão e se entra ou não no **MRP - Material Requirement Planning**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417588186519/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417588289559/mceclip2.png)

**Importante**  
A opção de **Alternativos** no **MATA010** será exibida apenas nos módulos **SIGAPCP - Planejamento e Controle da Produção**, **SIGAEST - Estoque/Custos** ou **SIGATEC - Gestão de Serviços**.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Cadastros e Configurações Gerais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550022-SIGAEST-CADASTROS-E-CONFIGURA%C3%87%C3%95ES-GERAIS)*
