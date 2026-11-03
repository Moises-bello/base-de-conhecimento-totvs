---
content_hash: 68d58a8801ee564aa2544c43aea3f26359071f5eb4dc1afd0993115bc3424f7b
fetched_at: '2026-06-29T00:11:11.484978+00:00'
page_id: '646680797'
product: rm
source: tdn-rm
title: Adesão ao Pagamento Recorrente no Portal do Processo Seletivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=646680797
version: 28
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Para os clientes que possuem o **eduCONNECT Pay**o pagamento com cartão no portal do processo seletivo permite habilitar o pagamento recorrente.

Para conhecer um pouco mais sobre cobrança recorrente [clique aqui](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=542149951)

Para que opção "**Pagamento recorrente**" fique disponível no portal é necessário que o cadastro da área de interesse ofertada esteja com a opção “**Permitir recorrência**” marcada.

Para processo seletivo do tipo "Venda online"

Para outros processos seletivos utilizando o novo portal

**A partir da versão 12.1.2402.1**, o sistema seguirá as seguintes regras para exibir a opção "**Pagamento Recorrente**":

**Para boletos não agrupados:**

* Exibe a opção apenas se todos os serviços associados ao contrato permitirem recorrência.
* Exibe a opção apenas se os seguintes parâmetros estiverem habilitados:  
  + “**Permitir recorrência**” no cadastro da área de interesse ofertada.
  + **“Permitir habilitar pagamento automático**" nos parâmetros de tesouraria.

**Para boletos agrupados:**

* Exibe a opção apenas se pelo menos um dos serviços associados ao boleto permitir recorrência.
* Exibe a opção apenas se os seguintes parâmetros estiverem habilitados:
  + “**Permitir recorrência**” no cadastro da área de interesse ofertada.
  + **“Permitir habilitar pagamento automático**" nos parâmetros de tesouraria.
  + “**Permitir pagamento recorrente em boletos agrupados**” nos parâmetros de integração financeira.

Obrigatoriedade do usuário

Para que a opção de pagamento recorrente fique disponível no portal, os candidatos ou responsáveis que forem realizar o pagamento, deve obrigatoriamente possuir um usuário de acesso ao portal do aluno.

Portanto, a parametrização de Geração de Usuário automática, deve estar habilitada, para que o pagamento seja realizado com sucesso.

Para mais informações sobre a geração de usuários [clique aqui](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360001043088-RM-EDU-Parametriza%C3%A7%C3%A3o-para-gerar-usu%C3%A1rio-automaticamente-):

Lembrando que este pagamento pode estar sendo realizado pelos seguintes papeis: aluno, responsável acadêmico, responsável financeiro, pai, mãe, portanto é importante realizar as devidas parametrizações.

## **02. EXEMPLO DE UTILIZAÇÃO**

Tela checkout TOTVS Pagamento Cartão a partir da versão 12.1.2410

* Validar configurações do Rewrite e ARR .

#### **Pagamento com novo cartão**

Ao realizar o pagamento com um novo cartão no processo seletivo será possível habilitar a recorrência, ao confirmar pelo pop-up que será exibido.

Para marcar a opção "Pagamento recorrente" é necessário que a opção "Salvar cartão para pagamentos futuros" esteja marcado, pois a recorrência será cadastrada para o cartão que esta sendo utilizado no pagamento.

#### **Pagamento com cartão já cadastrado na carteira digital**

Ao realizar o pagamento com um cartão já cadastrado na carteira digital também será possível habilitar a recorrência.

Será apresentado para o usuário a mensagem de confirmação, e após isso a seleção do(s) serviço(s) para a recorrência:

Após a confirmação do pagamento a recorrência será habilitada para o contrato vinculado a matricula do aluno.

**A partir da versão 12.1.2402.1**, se o aluno/responsável habilitar a opção "**Pagamento Recorrente**" para algum pagamento, a recorrência será habilitada para os serviços associados ao contrato, seguindo as seguintes regras:

**Para boletos não agrupados:**

* A recorrência será ativada para todos os serviços vinculados ao contrato.

**Para boletos agrupados:**

* A recorrência será ativada para todos os serviços e contratos associados ao boleto.

Posteriormente é possível no portal do aluno o usuário que habilitou a recorrência realizar a gestão (consultar, desativar....).

Para maiores informações
