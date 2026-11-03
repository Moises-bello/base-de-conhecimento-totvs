---
content_hash: ea39a95a2320f924345678df37096263dcd65aa73a651c1a6817be621686cc00
fetched_at: '2026-06-29T00:09:15.341596+00:00'
page_id: '421385352'
product: rm
source: tdn-rm
title: Contratos Parâmetros do Projeto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385352
version: 2
---

---

**Não Associar Tarefa a Contrato em mais de 100%:** Caso esta opção esteja habilitada, na associação de tarefas ao contrato, não será permitida a associação das tarefas em quantidades superiores a quantidade total, nem em único contrato e nem em contratos diferentes.

**Permite contratação de Serviços com Valor superior ao Orçado:** Se desmarcado será feito o bloqueio na associação de uma tarefa a um contrato com valor superior ao valor na visão de Tarefas. Caso contrário, a associação poderá ser feita em qualquer valor.

**Bloquear a edição de períodos anteriores a períodos medidos e liberados:**

Se ativo não será permitido a edição de nenhum período anterior a um período liberado. Neste caso se o período seguinte estiver simplesmente medido o sistema vai permitir a edição.

**Desagrupar produtos do rateio ao enviar para Suprimentos / Faturamento**

Se na medição do item existir o mesmo produto de rateio default para varias tarefas, com o parâmetro "Desagrupar produtos do rateio ao enviar para Suprimentos / Faturamento" ativo ao liberar a medição para o Suprimentos / Faturamento (Nucleus) será listado o mesmo produto de acordo com o número de tarefas que o tem como produto default.

**Exemplo**

Tarefa A utiliza produto XX como Produto de rateio default.

Tarefa B utiliza produto XX como Produto de rateio default.

Tarefa C utiliza produto XX como Produto de rateio default.

Ao liberar medição para o Suprimentos/Faturamento (Nucleus) este produto será listado 3 (três) vezes na tela de movimentos do Suprimentos/Faturamento (Nucleus).

Porém, se necessário Agrupar os produtos na tela de movimentos do Suprimentos/Faturamento (Nucleus) é necessário marcar nos parâmetros do tipo de movimento no Suprimentos / Faturamento (Nucleus) possível o agrupamento de itens. (Outras movimentações - clique em parametrizar, Clique em item - identificação 2/2 e ative o parâmetro "Agrupar itens repetidos".

**Atenção**

Se o tipo de movimento estiver com o parâmetro ativado "Gera Apropriação" na integração com projetos, o parâmetro "Agrupar itens repetidos" não ficara habilitado.

**Permite medição superior a 100%:**

**Sempre permitir:**

Permite que a medição acumulada até o período seja superior a quantidade total contratada. Somente exibe avisos quando a medição ultrapassar o contratado.

**Solicitar senha:**

Solicita senha quando a medição acumulada até o período for superior a quantidade total contratada. O lançamento da medição é liberado depois que é digitada a senha de um usuário que tem permissão no item de menu 'Autoriza medição superior a 100% mediante senha'. Mesmo que o usuário seja supervisor, se ele não tiver acesso a esse item de menu, ele não consegue autorizar a medição, não sendo necessário que seja supervisor. Se o usuário que está fazendo a medição acima do contratado tem acesso ao perfil 'Autoriza medição superior a 100% mediante senha' não será solicitada a senha, pois este próprio tem o poder de autorizar.

**Nunca permitir:**

Não permite que a medição acumulada até o período seja superior a quantidade total contratada, independente do usuário logado (supervisor ou não).

**Observação**

A permissão de acesso 'Autoriza medição superior a 100% mediante senha' definida no perfil do usuário, permite que o usuário efetue medições superiores a quantidade contratada e através de sua senha pode autorizar esse tipo de medição a outros usuários, durante o lançamento da medição.

**Histórico a ser inserido na criação do projeto**

É possível definir a chapa do responsável e o histórico do projeto para preenchimento automático ao se cadastrar um contrato. Para projetos integrados com o Protheus não ficará disponível a opção da chapa do responsável.

---
