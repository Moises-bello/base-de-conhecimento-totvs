---
article_id: 30076556464023
category: Contabilidade Gerencial - Movimentos, Lançamentos contábeis automáticos,
  lançamentos manuais e contabilização
content_hash: a4f135b1c888fc73e35721286fd82b627499da7794229672c4609a4f213733fa
fetched_at: '2026-06-28T22:40:32.537506+00:00'
product: protheus
section_id: 1500001537961
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - SIGAATF - SIGAPCO -
  Procedure Desatualizada ou Incompatível
type: support-article
updated_at: '2025-02-18T22:47:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30076556464023-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-SIGAATF-SIGAPCO-Procedure-Desatualizada-ou-Incompat%C3%ADvel
---

**Dúvida:**

Ao realizar os processamentos das rotinas é exibida a mensagem de Procedure Desatualizada ou Incompatível.

**Ambiente:**Cross Segmento - Backoffice Linha Protheus - Contabilidade Gerencial | Ativo Fixo | PCO  – Todas as versões  
![unnamed (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/30076685332631)

**Solução:**

Para corrigir o help indicado, recomendamos a verificação do **painel do Stored Procedure** através do **Configurador**.

O status das procedures podem ser identificados pela legenda disponível no painel:

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/30076620077463)**

* + **Incompatível (Cinza):** Não é possível processar a rotina.
  + **Desatualizado (Amarelo):** A versão instalada no ambiente não é a mais recente disponibilizada pela TOTVS.

As procedures auxiliam o processamento de rotinas do sistema, por isso recomendamos que todas estejam atualizadas. Para melhor desempenho, as assinaturas devem estar compatíveis entre o processo x rotina.

Realize os passos abaixo para que a mensagem não seja mais apresentada:

* Certifique-se de que o sistema está atualizado com:
* Central de Atualizações/Gestor de procedure:  
  <https://tdn.totvs.com/pages/releaseview.action?pageId=532651679>
* O pacote mais recente do módulo:    
  [Expedição Continua Backoffice Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160)
* Siga a documentação para atualização das **Stored Procedures** através do **Configurador**:  
  [Instalando/Atualizando pacotes de procedures](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-instalando_pacotes)

**Saiba Mais:**

[Stored Procedures - Novo gerenciador de pacotes](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes#StoredProceduresNovogerenciadordepacotes-instalando_pacotes)
