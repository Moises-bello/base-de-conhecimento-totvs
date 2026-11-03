---
article_id: 360024915131
category: Materiais - Compras (SIGACOM)
content_hash: 08001d77b51a087380c6bad4ffe74da929f31349d9dc0289eade269dfa722478
fetched_at: '2026-06-28T22:41:10.155204+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Parâmetros e Tabelas
  envolvidas no Controle de Alçadas
type: support-article
updated_at: '2025-03-14T18:21:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024915131-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Par%C3%A2metros-e-Tabelas-envolvidas-no-Controle-de-Al%C3%A7adas
---

**Dúvida**Quais são as tabelas envolvidas no processo de controle de Alçadas?

**Ambiente**Protheus – Compras – A partir da versão 12   
  
  
**Solução**

### **Parâmetros**

* **MV\_RESTSOL:** Indica se utiliza o controle de restrição aos solicitantes de produtos com restrição. Conteúdo do parâmetro igual Sim.
* **MV\_RESTCOM:** Indica se o acesso às solicitações de compras é restrito aos usuários cadastrados no grupo de compras da solicitação. Conteúdo do parâmetro igual Sim.
* **MV\_RESTINC:** Indica se restringe a inclusão de pedido de compras sem solicitação de compras para usuários não cadastrados como compradores. Conteúdo do parâmetro igual Sim.
* **MV\_RESTPED:** Indica se a manutenção do pedido de compras é restrita ao seu grupo de compras/compradores. Conteúdo do parâmetro igual Sim.
* **MV\_RESTNFE:** Indica se restringe o uso de pedidos bloqueados no recebimento de materiais. Conteúdo do parâmetro igual Sim.
* **MV\_PCAPROV:** Indica o grupo de aprovação padrão utilizado na aprovação do pedido de compras.
* **MV\_CPAPROV:** Indica o grupo de aprovação padrão utilizado na aprovação dos contratos de parceria.
* **MV\_ALTPDOC:** Indica se a pasta Documentos no Grupo de Aprovação é exibida. Apresenta as opções T e F.
* **MV\_APGRDFL:** Define o grupo de aprovação padrão a ser utilizado na aprovação por entidades contábeis. Deve ser preenchido com o código do grupo; item de entidade contábil do grupo. Exemplo : 000001;01
* **MV\_APROVSA:** Ativa o controle de bloqueio das Solicitações ao Armazém.
* **MV\_APROVSC:** Indica se há bloqueio automático das solicitações de compras com base nas regras do Cadastro de Solicitantes.
* **MV\_APRPCEC:** Habilita o controle de alçadas por item do pedido de compras direcionado por entidades contábeis. T=Sim e F=Não.
* **MV\_APRSCEC:** Habilita o controle de alçadas por item da solicitação de compras direcionada por entidades contábeis. T=Sim e F=Não.
* **MV\_APRSAEC:** Habilita o controle de alçadas por item da solicitação ao armazém direcionado por entidades contábeis. T=Sim e F=Não.
* **MV\_IPAPREC:** Define se a liberação de Alçada para o Tipo de Documento Itens de Pedido deve ocorrer por Grupo de aprovação, permitindo assim o recebimento de Documentos de Entrada para os Itens Liberados, mesmo quando houver itens do pedido pendentes de aprovação. T= Libera por Grupo de aprovação e F= Libera por Documento.
* **MV\_PERFALC:** Define critério utilizado para avaliação do Perfil do grupo de Aprovação para aprovações com Entidade Contábil 1- Total da Aglutinação, 2- Total do Item.
* **MV\_APRIPPC:** Define se a aprovação de Item de Pedido ocorrerá em 2 etapas: aprovação IP + PC (1-Sim / 2-Não).
* **MV\_EXAPROV:** Permite visualizar o histórico de aprovação após o pedido ser eliminado via resíduo. .T.=Sim e .F.=Não.
* **MV\_DOCAPRV:** Define quais tipos de documentos não passarão pela validação da data base do ambiente no momento da aprovação. Exemplo de preenchimento (**IM,PC,IP**)

**Tabelas**

• Solicitantes (SAI - DBK)

• Grupos de Produtos (SBM)

• Produtos (SB1)

• Compradores (SY1)

• Grupos de Compradores (SAJ)

• Grupos de Aprovação (SAL - DBL - DHM)

• Grupos de Compras (SAJ)

• Aprovadores (SAK)

• Perfis de Aprovação (DHL)

• Documentos com Alçada (SCR)

• Itens de Documento com Alçada (DBM)

• Pedido de compras (SC7​)

• Solicitações de Compras (SC1)

• Saldo dos Aprovadores (SCS)

**Obs:**

Caso tenha dúvidas no compartilhamento de tabelas no processo de alçada consulte o artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Compartilhamento das tabelas de alçada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30647938159639-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Compartilhamento-das-tabelas-de-al%C3%A7ada)

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Compartilhamento das tabelas de alçada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30647938159639-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Compartilhamento-das-tabelas-de-al%C3%A7ada)

[Controle de Alçadas - FAQs](https://tdn.totvs.com/pages/viewpage.action?pageId=270095502)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
