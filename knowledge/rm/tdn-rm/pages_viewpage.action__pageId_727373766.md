---
content_hash: f276be419ac99b924a8fbed032325e90867d6e81213f5ebc2c050d3af478943e
fetched_at: '2026-06-29T00:11:27.570889+00:00'
page_id: '727373766'
product: rm
source: tdn-rm
title: Validação de Débitos Financeiros do Responsável Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=727373766
version: 17
---

## **01. VISÃO GERAL**

Recurso disponível a partir da versão 12.1.2302

Venda Online

As regras e comportamentos relatados a seguir também são válidos para processos seletivos do tipo "**Venda online**".

Quando o candidato se inscreve em um processo seletivo do tipo "**Venda Online**" o sistema realiza inscrição e matricula de forma simultânea, e neste caso as validações relacionadas ao débito financeiro do responsável financeiro serão aplicadas **somente** se as parametrizações de débito financeiro forem definidas no cadastro do processo seletivo.

Caso o responsável financeiro da inscrição possua débitos financeiros, será possível emitir um alerta ao candidato ou impedir a conclusão da inscrição, além disso é possível personalizar uma mensagem que será apresentada ao candidato.

**Tela de parâmetros do TOTVS Processo Seletivo**

**Portal de inscrições**

A validação dos **débitos financeiro** será aplicada durante o preenchimento das informações dos responsáveis no momento em que o responsavel financeiro informar o CPF, ou ao avançar para a próxima etapa caso o responsável financeiro esteja definido com um candidato, pai ou mãe.

Entende-se como débitos financeiros, parcelas com lançamentos financeiros vencidos (em aberto) para alunos do TOTVS Educacional em que o responsavel financeiro tenha o mesmo CPF informado no responsável financeiro  da inscrição.

**Exemplo:**

**Opção "Alertar" marcada**

**Opção "Bloquear inscrição" marcada**

Nos exemplos acima é apresentado a mensagem padronizada, no entanto será possível personalizar a mensagem que vai ser apresentada.

Algumas parametrizações relacionadas a inadimplência financeira definidas no do **TOVTVS Educacional** serão consideradas na validação dos débitos financeiros durante a inscrição.

Caminho dos parâmetros: Ambiente > Parâmetros > TOTVS Educacional >Tesouraria

* **Verificar débitos do aluno em outras coligadas** :determina se a validação de inadimplência será apenas no âmbito da coligada corrente ou levará em consideração todas as coligadas do sistema.
* **Número de dias de carência para inadimplência:** determina a partir de quantos dias de atraso no pagamento o sistema passa a considerar como inadimplência.
* **Valor máximo de tolerância  para inadimplência:** determina um valor teto para que o aluno ainda não seja considerado inadimplente.

**Inscrição via RM.exe**

Inscrição via RM.exe

Ao adicionar uma inscrição diretamente no RM.exe, caso o candidato possua débitos financeiros e o processo seletivo esteja habilitado para bloquear não será permitido prosseguir com a inscrição, caso o processo seletivo esteja habilitado apenas para alertar, será apresentada uma mensagem informativa conforme a mensagem parametrizada, permitindo ao usuário decidir se que ou não seguir com a inscrição.

A mesma regra será aplicada ao clicar na opção "Matricular"
