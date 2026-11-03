---
article_id: 360018845931
category: CRM - Dúvidas Gerais
content_hash: 46a6ffc1869f11a0263afe236225112961a6d0019a5ee7b8a73b1dd8fef6ff2b
fetched_at: '2026-06-28T22:40:27.540717+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: MP-CRM-Ajuste na configuração do campo descrição do produto -U2_DPRO- no Cadastro
  dos Concorrentes do Telemarketing
type: support-article
updated_at: '2021-04-28T14:50:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018845931-MP-CRM-Ajuste-na-configura%C3%A7%C3%A3o-do-campo-descri%C3%A7%C3%A3o-do-produto-U2-DPRO-no-Cadastro-dos-Concorrentes-do-Telemarketing
---

**Dúvida**O campo descrição do produto no Cadastro dos Concorrentes do Telemarketing é exibido já com conteúdo, sem ao menos ter sido preenchido o seu código correspondente.  
   
 **Ambiente**Microsiga Protheus - a partir da versão 12.  
   
**Solução**

1. Acessar o módulo SIGACFG;
2. Através do caminho do menu desse módulo: Base de dados → Dicionários → Base de dados, acesse as configurações da tabela SU2 - Concorrentes;
3. Acione o botão "Alterar";
4. Localize o campo "U2\_DPRO" na estrutura da tabela SU2;
5. Acione o botão "Alterar";
6. Na aba "Opções" altere o conteúdo do campo "Inic. Padrão" digitando a seguinte informação: IIf( ! Empty(M->U2\_COD), Posicione("SB1",1,xFilial("SB1")+M->U2\_COD,"B1\_DESC"), "")
7. Confirme a manutenção, acionando o botão "Salvar";
8. Por fim, realize a atualização do dicionário de dados, efetivando a gravação dessa alteração de configuração.
