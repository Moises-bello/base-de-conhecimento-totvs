---
article_id: 360049541474
category: RH - Contabilização
content_hash: 2ee9dd349f6cb611db6c8818ccc76f58a11e2dce8e976e67c73b5071f37db51d
fetched_at: '2026-06-28T22:43:46.140594+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: 'RH - Linha Protheus - GPE - HELP NO CONTAC: Verificar se as contas foram digitadas
  corretamente de acordo com o tipo de lançamento se existem no plano de contas'
type: support-article
updated_at: '2021-06-07T13:26:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049541474-RH-Linha-Protheus-GPE-HELP-NO-CONTAC-Verificar-se-as-contas-foram-digitadas-corretamente-de-acordo-com-o-tipo-de-lan%C3%A7amento-se-existem-no-plano-de-contas
---

**Ocorrência**HELP: NO CONTAC  
Solução: Verificar se as contas foram digitadas corretamente de acordo com o tipo de lançamento se existem no plano de contas  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Causa**Esse incidente ocorre, existe conta contábil (débito ou crédito) bloqueada, cadastrada como sintética ou uma conta digitada nos lançamentos contábeis que não existe no plano de contas.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Após o processamento da contabilização (GPEM110), é apresentada a seguinte mensagem:  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074436754/mceclip0.png)  
  
  
2. Caso os lançamentos contábeis não estejam bloqueados através do parâmetro MV\_ALTLCTO, é possível efetuar a consulta da conta contábil na tela de lançamentos , verificando se a conta está  digitada corretamente ou se é sintética ou bloqueada.   
Selecione uma linha de lançamento contábil , aperte F3 na coluna de conta débito ou crédito e verifique a conta cadastrada:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074436774/mceclip1.png)

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360074436974/mceclip2.png)  
  
3. Se  a conta foi digitada incorretamente , é possível alterar a conta , inserindo a conta correta e salvando em seguida o arquivo. Caso o erro seja no cadastro da conta, será necessário acessar dentro do módulo Contábil (atualizações -> Entidades -> Plano de Contas) e alterar o cadastro da conta.  
  
Obs: essa alteração do cadastro deve ser realizado pelo responsável pela Contabilização da empresa, de modo que ele visualize a necessidade da alteração no cadastro e o impacto em possíveis ajustes.
