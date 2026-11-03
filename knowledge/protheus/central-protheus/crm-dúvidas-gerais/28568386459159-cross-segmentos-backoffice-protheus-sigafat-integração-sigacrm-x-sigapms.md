---
article_id: 28568386459159
category: CRM - Dúvidas Gerais
content_hash: 4b489a03c94cbfcd28c0ea7ace7927c4fa5778974470d3c50f9c0834aa44b67b
fetched_at: '2026-06-28T22:40:27.739365+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Integração SIGACRM x SIGAPMS
type: support-article
updated_at: '2025-01-10T19:28:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28568386459159-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Integra%C3%A7%C3%A3o-SIGACRM-x-SIGAPMS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28568348387479) Tempo aproximado para leitura: 00**:04:00 min****Situação:**

Ao gerar uma Proposta de Serviços vinculada à Proposta Comercial é gerado Orçamento de Projeto no módulo Gestão de Projetos. Ao confirmar a gravação desta Proposta Comercial é gerado um segundo Orçamento, sendo que este segundo Orçamento é gerado no módulo do Faturamento como um Orçamento de Venda.  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT – Todas as versões  
  
**Solução**

**Criado um processo para a Proposta Comercial quando ela estiver vinculada a uma Proposta de Serviços.**

Para realizar essa vinculação, o usuário deve executar a opção "Serviços (PMS)", disponível na rotina da Proposta Comercial.

Para acessar a opção "**Serviços (PMS)**", siga os passos abaixo:

1. **Através do módulo Faturamento:**

   * Acesse o menu: Atualizações → CRM - Administração de Vendas → Oportunidades → Selecione a oportunidade desejada → Clique no botão **Alterar** → Outras Ações → Proposta Comercial → Clique no botão **Incluir** (para incluir uma proposta) ou selecione a proposta desejada e clique em **Alterar** → Outras Ações → **Serviços (PMS)**.
2. **Através do módulo CRM:**

   * Acesse o menu: Atualizações → Vendas → Vendas → Oportunidades → Selecione a oportunidade desejada → Clique no botão **Alterar** → Outras Ações → Proposta Comercial → Clique no botão **Incluir** (para incluir uma proposta) ou selecione a proposta desejada e clique em **Alterar** → Outras Ações → **Serviços (PMS)**.

**Parâmetro MV\_ORCSPMS ativado (conteúdo igual a .T.):**

A Proposta Comercial manterá seu comportamento anterior a este novo processo, desde que a opção "Serviços (PMS)" não seja acionada. Caso seja informado um produto qualquer via "Serviços (PMS)", a Proposta Comercial aceitará apenas produtos originários dessa opção. Ou seja, todo produto (campo **ADZ\_PRODUT**) deverá ser informado ou alterado via "Serviços (PMS)", assim como os campos de Quantidade (**ADZ\_QTDVEN**) e Valor (**ADZ\_PRCVEN**), pois ambos serão reflexos das informações contidas no Orçamento de Projeto gerado pela opção "Serviços (PMS)".

Caso a opção "Serviços (PMS)" tenha sido utilizada para a carga dos produtos da Proposta Comercial (**ADZ\_PMS preenchido**), ao confirmar a gravação dessa Proposta Comercial, não será gerado o Orçamento de Vendas no módulo de Faturamento.

**Observações:**  

* As alterações realizadas nos produtos do Orçamento de Projeto criado via "Serviços (PMS)" serão totalmente replicadas na Proposta Comercial, mantendo, na tela, os produtos anteriores como registros deletados até a efetivação da gravação da Proposta Comercial.
* Os Orçamentos de Projeto vinculados a uma Proposta Comercial terão a edição de suas Tarefas bloqueada. A edição deverá ser feita através da opção "Serviços (PMS)" da Proposta Comercial, garantindo a integridade dos dados.

  

**Parâmetro MV\_ORCSPMS desativado (conteúdo igual a .F.):**

A Proposta Comercial aceitará tanto produtos informados diretamente na grid da sua rotina quanto produtos informados via "Serviços (PMS)". Se o usuário utilizar a opção "Serviços (PMS)" para a carga de produtos na Proposta Comercial, o valor mencionado em "Serviços (PMS)" não será considerado na Proposta Comercial. No entanto, as quantidades dos produtos informadas em "Serviços (PMS)" serão totalizadas na Proposta Comercial, gerando uma única linha do produto com a quantidade total.

Os produtos mencionados diretamente na grid da Proposta Comercial não serão levados ao Orçamento de Projetos gerado pela opção "Serviços (PMS)".

Ao confirmar a gravação da Proposta Comercial, serão gerados os Orçamentos de Vendas para os itens da sua grid de produtos, independentemente de sua origem.
