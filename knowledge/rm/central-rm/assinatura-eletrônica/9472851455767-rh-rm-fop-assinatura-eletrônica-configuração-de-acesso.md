---
article_id: 9472851455767
category: Assinatura Eletrônica
content_hash: 2fc6723cf8abcfef9265221240dece607d40293edb6ee4e7c17deb8eb3b48cb6
fetched_at: '2026-06-28T22:46:44.032306+00:00'
product: rm
section_id: 4403549405207
source: central-rm
title: 'RH - RM - FOP - Assinatura Eletrônica: Configuração de Acesso'
type: support-article
updated_at: '2024-06-18T13:28:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9472851455767-RH-RM-FOP-Assinatura-Eletr%C3%B4nica-Configura%C3%A7%C3%A3o-de-Acesso
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17177868399511) Tempo aproximado para leitura: **00:02:20 min****Dúvida**Como configurar os parâmetros para realizar a integração de documentos com o TOTVS Assinatura Eletrônica?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

Acesse: **Ambiente | Parâmetros Globais | aba Integração com Totvs Assinatura Eletrônica,** e preencha com os endereços descritos neste documento para a integração entre o RM e o TOTVS Assinatura Eletrônica.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9472556868119)

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9472519138583)

**URL de autenticação:**

<https://totvssign.totvs.app/identityintegration>

**URL da API de integração:**

<https://totvssign.totvs.app>

**Atualizar situação das assinaturas do documentos ao carregar a visão:** Marque está opção quando quiser que os status dos documentos **Pendente, Finalizado, Rejeitado, Excluído** no RM sejam atualizados online com o TOTVS Assinatura Eletrônica.

Caso a opção estiver desmarcada, poderá solicitar atualização dos status dos documentos em **Monitor de relatórios | Processos | Atualização de status de documentos integrados**.

A vantagem em manter a opção desmarcada é que, na atualização online, dependendo da quantidade de documentos, **pode exigir maior tempo de processamento durante a abertura do Monitor de Relatórios.**

**URL de login via formulário****web:**

<https://totvssign.totvs.app/webapptotvssign/#/auth/login?external=true>

**Saiba mais**

**[RH - RM - FOP - Assinatura Eletrônica: Permissão de Acesso](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500012213541)**

**[Definições e Parametrizações](https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590749)**

**[Processo de Integração de Relatórios](https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590852)**

**[Monitor de Relatórios](https://tdn.totvs.com.br/pages/releaseview.action?pageId=607590599)**
