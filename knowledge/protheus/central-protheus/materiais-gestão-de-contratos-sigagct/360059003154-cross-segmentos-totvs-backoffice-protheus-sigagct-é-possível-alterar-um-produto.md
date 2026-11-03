---
article_id: 360059003154
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 4279c3bed83651d819eaf9612f38bf94a827476fab7e78f9d443ea3a9e746fe9
fetched_at: '2026-06-28T22:37:22.649097+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - É possível alterar
  um Produto de um Item de Planilha em um Contrato já Vigente ?
type: support-article
updated_at: '2025-12-01T13:35:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059003154-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-%C3%89-poss%C3%ADvel-alterar-um-Produto-de-um-Item-de-Planilha-em-um-Contrato-j%C3%A1-Vigente
---

**Dúvida**  
É possível alterar um Produto de um Item de Planilha em um Contrato já Vigente ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

No padrão do módulo de Gestão de Contratos não existe uma Funcionalidade ou Tipo de Revisão para realizar a "troca" ou alteração de produtos dos itens de uma planilha do contrato.

A alternativa existente de se usar outro produto no cadastro do contrato do Tipo Fixo é zerando o saldo do item com o produto existente que ja teve medição e incluído um novo item com novo produto e informações desejadas.  
  
A forma de se fazer é através de uma Revisão de Tipo Aditivo (configurada para ser realizada Acréscimo e Decréscimo), Aberta ou Renovação, onde nessa revisão:  
  
**Passo 1)** Para os itens dos códigos produtos existentes que se deseja não mais utilizar:

* Caso já tenha havido medição, pode ser feita a diminuição da quantidade do item para a quantidade igual de medições já realizadas (ficando assim zerado o saldo deste item da planilha) conforme instrução no artigo abaixo:

[MP - SIGAGCT - Como Zerar o Saldo do produto do contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021322032-MP-SIGAGCT-Como-Zerar-o-Saldo-do-produto-do-contrato?source=search)

Caso o item possua informações que não devam mais ser utilizadas no contrato, como entidades contábeis desativadas e etc, essas informações podem também ser retiradas do item.

* Caso o contrato ainda não tenha tido medição, o item pode ser deletado (tecla Del).

**Passo 2)** E nesta mesma revisão de Aditivo (que foi utilizado um Tipo de revisão para se realizar decréscimo e também acréscimo) pode-se incluir os novos itens com os códigos novos produtos respectivos aos zerados e/ou deletados com as quantidades que haviam de saldo restante dos itens anteriores e valores iguais.

***Obs1:***

Quando se trata de um contrato cadastro com uma ***Planilha de Serviço*** conforme o artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais as configurações para utilização de Contrato / Planilha de Serviço no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053570234-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Quais-as-configura%C3%A7%C3%B5es-para-utiliza%C3%A7%C3%A3o-de-Contrato-Planilha-de-Servi%C3%A7o-no-Gest%C3%A3o-de-Contratos-?source=search)

o mesmo não possui uma forma de se alterar a quantidade para se "zerar o saldo" do item, e dessa forma ele não possui uma forma de o item ser inutilizado.

Sendo assim, nesta situação, a possibilidade seria apenas o cadastro de um novo contrato com o item correto que se deseja.

***Obs2:***

No caso de uma ***Planilha Semi-Fixa*** conforme o artigo abaixo:

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Contrato Semi-Fixo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407174331671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Contrato-Semi-Fixo)

neste tipo de planilha é permitido se deletar o item da planilha através da tecla Del nas Revisões dos tipos "Aberta", "Renovação" e "Aditivo".

Dessa forma podem ser seguidos os mesmos passos acima reportados de um contrato Fixo na situação em que a planilha não sofreu nenhuma medição, deletando o item que não se deseja mais utilizar.

***Obs3:***

**Como realizar a troca de um produto já medido em Planilha de Serviços?**

Para que possa trocar um produto em um contrato com planilha de serviço , contrato que já possui medições encerradas, realize os passos abaixo:

Inclua uma ***Revisão do "Tipo Aberta"***

1. Alterar o valor do item para 0. O sistema criará um novo item com valor zerado e quantidade que do item que não teve medição realizada.
2. Deletar o Item que foi criado e ainda não foi medido.
3. Adicionar o novo item
4. Acessar a **Aba parâmetros/Revisão** e ajustar **opções Arrasto e Redis.Valor** para Sim. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/36688562960791)**
5. Acessar **Outras Ações>Atualizar Cronograma financeiro/físico:![](https://centraldeatendimento.totvs.com/hc/article_attachments/36688562962583)**

***Saiba Mais:***

[MP - SIGAGCT - Como Zerar o Saldo do produto do contrato](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021322032-MP-SIGAGCT-Como-Zerar-o-Saldo-do-produto-do-contrato?source=search)

[DT Permitir excluir produto na revisão de uma planilha semi fixa](https://tdn.totvs.com/x/gR9rJw)

[Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Quais os tipos de Revisão disponíveis no Gestão de Contratos ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034587334)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
