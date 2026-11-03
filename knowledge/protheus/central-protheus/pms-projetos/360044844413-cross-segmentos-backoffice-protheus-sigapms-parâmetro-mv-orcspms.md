---
article_id: 360044844413
category: PMS - Projetos
content_hash: 715c3d7d0864109a014d25e9dc1cdf4e0e46deb0b7956b9cebcacc421decc27d
fetched_at: '2026-06-28T22:37:14.942780+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Parâmetro MV_ORCSPMS
type: support-article
updated_at: '2024-02-26T18:29:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044844413-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-Par%C3%A2metro-MV-ORCSPMS
---

**Dúvida**

Qual o comportamento parâmetro **MV\_ORCSPMS**?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - A partir da versão 12  
  
**Solução**

Parâmetro **MV\_ORCSPMS** ativado (conteúdo igual a **.T.**):

Ao gerar uma **Proposta de Serviços** vinculada à **Proposta Comercial** é gerado **Orçamento de Projeto** no módulo **Gestão de Projetos**. Ao confirmar a gravação desta **Proposta Comercial** é gerado um segundo **Orçamento**, sendo que este segundo **Orçamento** é gerado no módulo do **Faturamento** como um **Orçamento de Venda**.

A Proposta Comercial manterá o seu comportamento anterior a este novo processo, desde que não seja acionada a opção de Serviços (**PMS**). Caso seja informado um produto qualquer, via Serviços (PMS), a Proposta Comercial passará a aceitar apenas produtos originários desta opção. Ou seja, todo Produto (**ADZ\_PRODUT**) deverá ser informado/alterado, via Serviços (PMS), assim como os campos de Quantidade (**ADZ\_QTDVEN**) e Valor (**ADZ\_PRCVEN**), pois ambos serão reflexos das informações contidas no Orçamento de Projeto que foi gerado pela opção de Serviços (PMS).

Caso a opção de Serviços (PMS) tenha sido utilizada na carga dos produtos da Proposta Comercial (**ADZ\_PMS**preenchido), ao confirmar a gravação desta Proposta Comercial, não será gerado o Orçamento de Vendas no módulo do Faturamento.

* Parâmetro **MV\_ORCSPMS** desativado (conteúdo igual a **.F.**):

A Proposta Comercial aceitará tanto produtos que tenham sido informados diretamente na *grid* da sua rotina, quanto produtos informados via opção de **Serviços (PMS)**. Se o usuário utilizar a opção **Serviços (PMS)** para a carga de produtos na Proposta Comercial, o valor mencionado em **Serviços (PMS)** não será considerado na **Proposta Comercial**. Enquanto que, as **quantidades** dos produtos iguais informadas em **Serviços (PMS)** serão totalizadas na **Proposta Comercial**, gerando uma **única linha do produto** com a sua **quantidade total**.

Os produtos mencionados diretamente na *grid* da **Proposta Comercial** não serão levados ao **Orçamento de Projetos** que foi gerado pela opção de **Serviços (PMS)**.

Ao confirmar a gravação da **Proposta Comercial** serão gerados os **Orçamentos de Venda** para os itens da sua *grid* de produtos, independentemente da sua origem.

**IMPORTANTE :**A criação automática do parâmetro **MV\_ORCSPMS** estará disponível apenas na expedição oficial da Release 12.1.33 do Protheus prevista para Outubro/2020. Não serão expedidos quaisquer pacotes específicos no intuito de criar este parâmetro nas versões anteriores à 12.1.33. Portanto, caso deseje ativar esta funcionalidade nas versões anteriores, além da aplicação do patch deste requisito em ambiente válido e cujo suporte/atendimento esteja liberado, o parâmetro **MV\_ORCSPMS** deverá ser criado manualmente. 

**Documento complementar : <https://tdn.totvs.com/x/kIF-Dw>**
