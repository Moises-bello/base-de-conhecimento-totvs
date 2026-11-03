---
article_id: 360056069833
category: eSocial - Middleware
content_hash: d8e26e8d4452cdc9a2d98ff8cbb1db7bc22e225543a695075ed79ed632fd11fc
fetched_at: '2026-06-28T22:47:05.632450+00:00'
product: rm
section_id: 1500000834541
source: central-rm
title: RH - RM - FOP - eSocial  - Passos para ativação do Middleware e configuração
  dos relatórios de conferência
type: support-article
updated_at: '2025-03-05T20:36:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056069833-RH-RM-FOP-eSocial-Passos-para-ativa%C3%A7%C3%A3o-do-Middleware-e-configura%C3%A7%C3%A3o-dos-relat%C3%B3rios-de-confer%C3%AAncia
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19110707099159)**Tempo aproximado para leitura: **00:03:30 min**

**Dúvida**  
Como realizar a ativação do Middleware e como configurar o sistema para utilização do Relatórios de Conferência?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões de mercado  
  
**Solução**  
O Middleware é um serviço do TAF cujo objetivo é prover um serviço de entrega direta dos xml’s da Folha de Pagamento para o governo sem a necessidade de gravação dos xml’s no ambiente do TAF, facilitar a gestão de configuração e agregar relatórios gerenciais para auxiliar os usuários nas validações das entregas do eSocial.  
  
A ativação do Middleware é **irreversível**. Sendo assim, avalie se sua empresa se enquadra no cenário de uso e, em caso de dúvidas, entre em contato com o suporte do eSocial.  
  
Abaixo segue documentação com orientações de ativação e validação do Middleware e, também, configuração para utilização dos relatórios de conferência.

* Clientes que utilizam produto hospedado em Cloud  
       [Cloud - Passos para ativação do Middleware e configuração do Relatório de Conferência](https://tdn.totvs.com/pages/viewpage.action?pageId=557319572)
* Clientes que utilizam produto em servidor próprio  
      [Passos para ativação do Middleware e configuração do Relatório de Conferência](https://tdn.totvs.com/pages/viewpage.action?pageId=563428854)

**Importante**Para realizar a ativação deve-se, primeiramente, atender às premissas abaixo:

* **Não utilizar o TAF para consolidação de eventos**: todas as informações necessárias para geração dos eventos eSocial devem estar no produtos da linha RM. Caso utilize softwares terceiros ou outras linhas de produto TOTVS (ex.: Datasul, Protheus, etc) que gerem dados ao eSocial, será necessário o uso do TAF Full para consolidação, não podendo utilizar o Middleware no momento;
* **Possuir o ambiente RM e TAF atualizados**: TAF atualizado com o último pacote acumulado e RM atualizado com o Patch mais atual da sua respectiva release;
* **Não possuir eventos pendentes de atualização**: não pode existir eventos na fila do RM com o status **3 - Enviado TAF** e/ou **4 - Aceito TAF**.Necessário atualizar os status antes da ativação;
* **Recibo de entrega dos eventos atualizados**: atualizar os recibos do eSocial no RM antes de realizar a ativação.

**Saiba mais**  
Para mais informações sobre o Middleware, acesse:  
    - [Ativar Integração com o Middleware (eSocial do Futuro)](https://tdn.totvs.com/pages/releaseview.action?pageId=519722143)
