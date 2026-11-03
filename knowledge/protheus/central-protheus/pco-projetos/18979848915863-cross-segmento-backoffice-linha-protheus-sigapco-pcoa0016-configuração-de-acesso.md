---
article_id: 18979848915863
category: PCO - Projetos
content_hash: fd4af32a83aae56f4fde78284a97ec2e84bdd21570a7207a66708941d3bd2a79
fetched_at: '2026-06-28T22:37:06.340148+00:00'
product: protheus
section_id: 1500001551042
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAPCO - PCOA0016 - Configuração
  de Acesso para Criação e Manutenção de Projeto Orçamentário  '
type: support-article
updated_at: '2023-11-10T18:42:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18979848915863-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-PCOA0016-Configura%C3%A7%C3%A3o-de-Acesso-para-Cria%C3%A7%C3%A3o-e-Manuten%C3%A7%C3%A3o-de-Projeto-Or%C3%A7ament%C3%A1rio
---

**Dúvida**Como configurar o acesso a criação e manutenção de projetos.

**Ambiente**Cross Segmento - BackOffice Linha Protheus -Planejamento e Controle Orçamentário.

#### **Solução:**

Para liberação a manutenção e criação de Projetos no módulo do PCO, é necessário configurar o parametro MV\_PCOPRO com o código o usuário que terá acesso a manutenção e criação de projetos na rotina PCOA0016:

Segue exemplo de configuração para o usuário admin:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18979910666647)

Caso deseje informar mais de um usuário com diretos ao projeto, devera informar os códigos separados por ";" conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18979897683095)

Após configuração do parametro basta acessar a rotina com o usuário definido no parametro, que a rotina esta liberada para inclusão, alteração e exclusão de projeto orçamentário.

**Saiba mais:**

[Menu Projeto de Planejamento (PCOA011)](https://tdn.totvs.com/pages/releaseview.action?pageId=439693670)

[Projeto Orçamentário (PCOA016 - SIGAPCO)](https://tdn.totvs.com/pages/viewpage.action?pageId=312175579)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Principais parâmetros do módulo PCO - Principais parâmetros do módulo PCO - Planejamento e Controle Orçamentário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017496452-MP-SIGACOM-Principais-par%C3%A2metros-do-m%C3%B3dulo-PCO-?source=search)

[Controladoria - PCO - Protheus 12](https://tdn.totvs.com/display/public/PROT/Controladoria+-+PCO+-+Protheus+12)

[Cross Segmento - Backoffice Linha Protheus - SIGAPCO - CheckList para utilização do modulo Planejamento de Custos Orçamentários](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038998854-MP-SIGAPCO-CheckList-para-utiliza%C3%A7%C3%A3o-do-modulo-Planejamento-de-Custos-Or%C3%A7ament%C3%A1rios)
