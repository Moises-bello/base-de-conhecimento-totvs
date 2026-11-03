---
article_id: 360018988791
category: Configurações
content_hash: 27e75897e031e5661fde849c95c5f531d3dd5ab0b5ee3132e6eaa1d97defb9ba
fetched_at: '2026-06-28T22:46:29.930168+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Acesso bloqueado para incluir, alterar e excluir batida, abono,
  justificativa de exceções e autorização de extras no RM Portal
type: support-article
updated_at: '2025-01-27T15:53:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018988791-RH-RM-PTO-Acesso-bloqueado-para-incluir-alterar-e-excluir-batida-abono-justificativa-de-exce%C3%A7%C3%B5es-e-autoriza%C3%A7%C3%A3o-de-extras-no-RM-Portal
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16782291248023) Tempo aproximado para leitura: 00:01:00 min  
  
Ocorrência**No RM Portal é apresentado o erro 'Acesso bloqueado para incluir, alterar e excluir batida, abono, justificativa de exceções e autorização de extras' ao realizar alterações para funcionários.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) RM – Automação de Ponto – A partir da versão 11.80  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está incorreta para a edição do espelho de ponto.  
  
**Solução**Para solucionar o erro abaixo, siga os passos apresentados abaixo.  
  
![image001.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360014599832)

1. Acesse o módulo de **Automação de Ponto**, selecione a guia **Configurações**e o menu **Parametrizador e clique avançar:**  
     
   ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29529786609175)
2. Na janela do parametrizador, selecione **RM Portal e** avance**:**  
   ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29529822993047)
3. Na listagem dos grupos de acesso, selecione o desejado e clique no botão **Parametrizar**.  
     
   ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29529786621719)
4. Selecione a etapa **Permissões** e **desmarque** a opção **Bloqueia acesso aos cadastros do RM Portal**. E avance as demais etapas até concluir.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/29529786623895)  
     
   **Saiba Mais:**  
   [Permissões](https://tdn.totvs.com/pages/viewpage.action?pageId=452720001)
