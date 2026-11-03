---
article_id: 360028009671
category: Materiais - Compras (SIGACOM)
content_hash: 294262fea9c781a0a612fcde69d97c9ff93a788e15c31584cf9d9c98d1c81a69
fetched_at: '2026-06-28T22:41:10.441245+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Rotina Eliminar Resíduos
  não ocorre no Pedido de Compras - Relação com campo C7_QTDACLA
type: support-article
updated_at: '2021-12-16T12:43:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028009671-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Rotina-Eliminar-Res%C3%ADduos-n%C3%A3o-ocorre-no-Pedido-de-Compras-Rela%C3%A7%C3%A3o-com-campo-C7-QTDACLA
---

**Dúvida**Ao efetuar o processo de eliminação resíduo o sistema não elimina o resíduo do pedido. O processo é finalizado porém o pedido ainda se encontra pendente.  
  
**Ambiente**  
Protheus – Compras – A partir da versão 11.80  
  
**Solução**

Ao tentar processar a rotina de eliminar resíduos (MATA235) com determinada quantidade no campo C7\_QTDACLA, não é concretizado o processamento da eliminação do saldo / resíduo do Pedido de Compras.

Ao realizar o vínculo de um pedido de compras em um documento de pré-nota, é populado o campo **C7\_QTDACLA** com a quantidade a ser classificada. Após realização da classificação da NF via documento de entrada, é compensado automaticamente e zerado o campo.

No entanto, quando se tenta eliminar resíduos no qual o respectivo pedido possuí saldo pendente de classificação no campo **C7\_QTDACLA**, a eliminação não ocorre pois a rotina valida que parte deste saldo está em utilização (especificamente neste caso, atrelado ao saldo a classificar).

Para que seja possível a concretização da eliminação do resíduos de um determinado pedido que encontra-se mediante este cenário, se faz necessário a exclusão da pré-nota na qual está "consumindo" o saldo e reservando-o para classificação ou até mesmo a efetuação da classificação da nota via documento de entrada e posteriormente eliminação do resíduo se ainda pertinente (em situações em que ainda há saldo no pedido, e mesmo após esta classificação e consumido o saldo em questão não será utilizado o restante do saldo restante do pedido de compras).

Outra situação é que muitas vezes o processo de eliminação é "finalizado" porém ao verificarmos o Pedido de Compras, o mesmo encontra-se como pendente, como se o processo não tivesse "reconhecido" o pedido que necessitamos eliminar resíduo.

Isso ocorre por haver inconsistências no campo **C7\_QTDACLA** do referido pedido.

Uma dessas inconsistências pode ser a alteração do número de casas decimais relacionados a quantidade do item, porém o **C7\_QTDACLA** não é alterado também, gerando uma incompatibilidade no dicionário do sistema.

Para se eliminar o resíduo deve-se limpar o conteúdo do campo **C7\_QTDACLA** e efetuar o processo de eliminação de resíduo novamente.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
