---
content_hash: e1d74ec3e97a4a3746fec66e4e7f56a81f9064ea361843c569eace85a8c55739
fetched_at: '2026-06-29T00:09:14.878094+00:00'
page_id: '421385291'
product: rm
source: tdn-rm
title: Encerramento de Contrato
type: documentation
url: https://tdn.totvs.com/display/LRM/Encerramento+de+Contrato
version: 13
---

---

O encerramento de um contrato, fornece ao usuário a opção de definir o encerramento das "atividades" do mesmo, por "Conclusão" ou "Cancelamento". Neste encerramento, se o usuário acessar:  Projeto |Construção e Projetos | Projetos |Construção e Projetos |Projetos F6 | Contratos | Checklist, poderá ser realizado uma parametrização de uma "checklist" para ser executada antes de finalizar um contrato.  
    
 O Checklist de encerramento de contrato foi desenvolvido para flexibilizar o encerramento dos contratos (à Pagar e à Receber) deixando a cargo do usuário decidir quais comportamentos serão executados e validados no momento que o contrato está sendo encerrado, ou seja, está sendo concluído ou cancelado.  
 Para possibilitar a existência desse comportamento foi necessário inserir novos parâmetros para definir as ações do sistema diante de alguma condição inválida. Os parâmetros são responsáveis por liberar ou bloquear o encerramento do contrato. Os novos parâmetros serão do tipo lista de seleção com as opções "Não confere", "Avisa" ou "Barra", permitindo ao usuário customizar as ações de validação do sistema no ato de encerrar (concluir/cancelar) o contrato.  
 Serão validados ao encerrar o contrato as seguintes situações:

* Contrato com Retenção;
* Saldo do Contrato;
* Período Medido e Não liberado;
* Pedidos de Compra em Aberto;
* Adiantamento.

**Regras de validação para a parametrização:**

**Contrato com Retenção**  
 No momento de encerramento de um contrato, seja por conclusão ou cancelamento, caso exista alguma retenção contratual ainda não liberada, será consistido o parâmetro e o comportamento da execução levará em consideração a opção selecionada no parâmetro.

* "Não conferir": Nada será validado independentemente da existência ou não de retenções o processo será executado normalmente;
* "Avisar": O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de retenções não liberadas para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, parar o processo ou continuar sua execução.
* "Barrar": O processo será barrado caso o sistema encontre alguma retenção sem liberação, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

**Saldo do Contrato**  
 Ao encerrar um contrato e o mesmo ainda possuir saldo de utilização, o parâmetro o usuário poderá customizar o comportamento do sistema conforme abaixo:

* "Não conferir": Nada será validado e independentemente da existência ou não de saldo no contrato o processo de encerramento será executado normalmente;
* "Avisar": O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de saldo naquele contrato, e solicitará ao mesmo uma ação a ser tomada, encerrar o processo ou continuar sua execução.
* "Barrar": O processo será barrado caso o sistema encontre saldo no contrato, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

**Período Medido e Não liberado**  
 Quando o contrato for encerrado, se existir algum período no mesmo que esteja medido, mas, não esteja liberado o usuário poderá customizar o comportamento, conforme os demais parâmetros.

* "Não conferir": Nada será validado e independentemente da existência ou não períodos medidos e não liberados o processo será executado normalmente;
* "Avisar": O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de períodos medidos e não liberados para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, parar o processo ou continuar sua execução.
* "Barrar": O processo será barrado caso o sistema encontra alguns períodos medidos e não liberados, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

**Contrato de fornecimento de material com movimentos em aberto**

Quando o usuário tentar encerrar o contrato e no mesmo houver algum contrato de fornecimento de material com movimento em aberto (apropriado), o sistema irá consistir o parâmetro, tomando como ação a opção selecionada pelo usuário, conforme listado abaixo:

* "Não conferir": Nada será validado e independentemente da existência ou não de contrato de fornecimento de material com movimentos em aberto o procedimento será executado normalmente;
* "Avisar": O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de contrato de fornecimento de material com movimentos em aberto para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, abortar o procedimento ou continuar sua execução.
* "Barrar": O procedimento será barrado caso o sistema encontra alguns contratos de fornecimento de material com movimentos em aberto, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

**Adiantamento**  
 Se o usuário executar o encerramento de contrato (conclusão/cancelamento) o sistema irá consistir se existe algum adiantamento em aberto, caso ele encontre algum irá consistir o parâmetro, e executando a ação selecionada pelo usuário dentre as listadas abaixo:

* "Não conferir": Nada será validado e independentemente da existência ou não de adiantamento em aberto o processo será executado normalmente;
* "Avisar": O sistema irá exibir uma mensagem de alerta comunicando ao usuário a existência de adiantamento em aberto para aquele contrato, e solicitará ao mesmo uma ação a ser tomada, abortar o processo ou continuar sua execução.
* "Barrar": O processo será barrado caso o sistema encontra algum adiantamento em aberto, e o usuário não conseguirá executar o encerramento enquanto não resolver essa pendência.

**Atenção:**

**Avaliação da existência de workflow**

* Será necessário ao procedimento validar a se os workflows presentes no TOP [TODO: listar quais] irão influenciar o comportamento do encerramento do contrato. Para casos positivos deverão ser adotadas como “barra” as consistências influenciadas por eles.
* Neste caso os dois workflows presentes irão alterar o comportamento dos parâmetros [TODO: parâmetros afetados], que por padrão serão marcados como “barra”, e a menos que os parâmetros referentes aos workflows sejam desmarcados esses parâmetros permanecerão como “barra”.
* Essa validação foi necessária para que o comportamento dos workflows não fosse alterado, de tal modo que a decisão tomada a partir deles não tivesse nenhum peso, sendo assim em caso de existência dos mesmos o comportamento será padrão.

**Atenção (Para clientes/usuários que atualizaram seu sistema RM):**

Para que o sistema fique compatível com o cenário atual dos clientes/usuários, e não haja nenhuma “adesão” inesperada ou mudança de comportamento sem prévio aviso, as novas consistências serão incorporadas de forma a manter compatibilidade com as já existentes no sistema.

Ao atualizar a versão do sistema, a parametrização de contratos será preenchida automaticamente conforme descrito abaixo (mas o usuário poderá alterar, desde que tenha permissão):

* **Contrato com Retenção**  
  Os usuários que utilizam o parâmetro "Permitir encerramento de contrato com retenções" marcado, a compatibilidade com o parâmetro será o mesmo selecionado como "Avisa", para os demais a compatibilidade com o novo parâmetro será o mesmo selecionado como "Barra".
* **Saldo do Contrato**  
  O sistema irá usar como comportamento padrão para o parâmetro "Saldo do Contrato", a compatibilidade com o parâmetro selecionado como "Não consistir".
* **Período Medido e Não liberado**  
  O sistema irá usar como comportamento padrão para o parâmetro "Período Medido e Não liberado", a compatibilidade com o parâmetro selecionado como "Barra".
* **Contrato de fornecimento de material com movimentos em aberto**  
  O sistema irá usar como comportamento padrão para o parâmetro "Pedidos de Compra em Aberto", a compatibilidade com o parâmetro selecionado como "Não consistir".
* **Adiantamento**  
  O sistema irá usar como comportamento padrão para o parâmetro "Adiantamento", a compatibilidade com o parâmetro selecionado como "Não consistir".
