---
article_id: 4411520104727
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 65926521cc7a9128c7a8b6406faa0a72f02d5b8d225a40cb5bfe2457c7328b85
fetched_at: '2026-06-28T22:37:21.504314+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como Finalizar um contrato
  ?
type: support-article
updated_at: '2026-06-24T14:58:26Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411520104727-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-Finalizar-um-contrato
---

Para "Finalizar" um contrato no Gestão de Contratos TOTVS Protheus, deve-se alterar o status do contrato primeiro para "Sol. Finalização" e depois para "Finalizado" via rotina de Manutenção (SIGAGCT). A mudança é irreversível, exclui títulos provisórios, mas não estorna medições ou pedidos. Não há no padrão funcionalidade de finalização automática nem alteração direta para "Finalizado" sem passar por "Sol. Finalização".

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36749913901207) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como realizar a Finalização de um Contrato no Gestão de Contratos ?

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões

**Solução**

Para a mudança de status do Contrato para o status "Finalizado", pode-se utilizar a opção existente na rotina de Manutenção conforme sequência abaixo:

Em SIGAGCT->Atualizações->Contratos->Manutenção:

Posicionado sobre o contrato em questão use a opção "Outras Ações->Situação":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411511537559)

Utilizar a opção 07 - Sol. Finalização

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411519749015)

Ao confirmar a opção o contrato ficará com a legenda "SOl. Finalização"

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411511627927)

Posteriormente, a deve-se realizar o mesmo procedimento escolhendo o Status da opção "08-Finalizado":

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520038295)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520042903)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411520057879)

***Obs.:***

1 - Realizando a alteração do status para "Finalizado" os títulos provisórios (PR) existentes para o contrato provenientes de sua inclusão serão excluídos.

2 - As medições realizadas e os Pedidos/Títulos provenientes dessas medições já realizadas não serão estornados ou excluídos.

3 - No padrão do módulo não existe uma funcionalidade para realização de Finalização ou Encerramento Automática de contratos.

4 - Atualmente o módulo não possui uma possibilidade de se modificar o Status diretamente para "Finalizado", onde sempre deve-se primeiramente passar para "Sol. Finalização" para depois modificar para "Finalizado".

5 - O Gestão de Contratos não possui uma funcionalidade ou parametrização que um contrato quando atinge a "data limite" ou "acabe o saldo", ele ficar como "Vencido", onde é possivel apenas ele ficar "Finalizado" conforme as orientações deste artigo.

***Importante:***

Lembramos que esta mudança de situação para "Sol. Finalizado" e "Finalizado" é irreversível.

***Saiba Mais:***

* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Existe como Desabilitar a tela de Avaliação de Fornecedores ao Finalizar um Contrato do SIGAGCT ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/30591703503895-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Existe-como-Desabilitar-a-tela-de-Avalia%C3%A7%C3%A3o-de-Fornecedores-ao-Finalizar-um-Contrato-do-SIGAGCT)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como realizar o cancelamento de um Contrato no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052136373)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Existe a possibilidade de excluir ou estornar um contrato com status Finalizado ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024697991-MP-SIGAGCT-CNTA300-Manuten%C3%A7%C3%A3o-de-Contratos-retornar-status-finalizado)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível alterar um contrato da situação de Solicitação de Finalização para Vigente ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022098611-MP-Gest%C3%A3o-de-contratos-Como-alterar-a-situa%C3%A7%C3%A3o-de-um-contrato-de-solicita%C3%A7%C3%A3o-de-finaliza%C3%A7%C3%A3o-para-vigente-novamente)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Validação CN100VERNF ao Finalizar um Contrato - Medição em Aberto ou Medição sem NF - MV\_CNVERNF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407274770583-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Valida%C3%A7%C3%A3o-CN100VERNF-ao-Finalizar-um-Contrato-Medi%C3%A7%C3%A3o-em-Aberto-ou-Medi%C3%A7%C3%A3o-sem-NF-MV-CNVERNF?source=search)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as situações disponíveis ou Ciclo de Vida de um Contrato do Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026376592-MP-SIGAGCT-Ciclo-de-vida-do-Contrato?source=search)
* [Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
