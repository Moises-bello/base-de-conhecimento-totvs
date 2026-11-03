---
article_id: 360024751151
category: Call Center - Dúvidas Gerais
content_hash: 80413c2980df3d72e8d53f502bf03c229674f25bc81cd26bfc9d39bb477116c0
fetched_at: '2026-06-28T22:41:26.678204+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - SIGATMK - Help: ACESS_ROT no Call
  Center'
type: support-article
updated_at: '2026-04-13T13:15:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024751151-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Help-ACESS-ROT-no-Call-Center
---

**Dúvida**

Como proceder quando ocorre o Help ACESS\_ROT em alguma ação no Call Center?

Problema: O usuário que esta utilizando o sistema não tem acesso a esta rotina.

Solução: Somente os administradores do sistema tem acesso a rotina.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360023071271)  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGATMK - Todas as versões  
  
**Solução**

1 - Valide no usuário de configurador deste operador está habilitado para a opção de acesso **"Rotina de atendimento (25)"**, se estiver desmarcada o usuário não terá acesso a rotina, gerando a mensagem em questão.

Desta forma, será necessário selecionar a opção nos acessos de usuário de configurador, salvar o cadastro de usuário, e reiniciar o Smartclient para que o sistema reconheça a configuração.

2 - Veja também as configurações do cadastro de operador, quanto ao acesso das opções de Atendimento (Telemarketing (TMKA272), Televendas (TMKA273), Telecobrança (TMKA280-TMKA350), agenda (TMKA380), Teleatendimento (TMKA503A) e o grupo de atendimento ao qual o mesmo está associado.

3 - Verifique se a ação do usuário possui acesso à regras de módulos integrados como de Pedido de vendas, exemplo "**Alterar pedidos de venda (20)"** e "**Excluir pedidos de venda (21)"****,** essas regras podem interferir no processo do Call Center pela ação não ser permitida na rotina integrada de outro módulo.

**Saiba mais:**

[Cross Segmentos - Backoffice Protheus - SIGATMK - Acessos no configurador do Call Center](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28003033414167-Cross-Segmentos-Backoffice-Protheus-SIGATMK-Acessos-no-configurador-do-Call-Center)
