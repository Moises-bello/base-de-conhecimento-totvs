---
content_hash: 189987064d34dd427eebf09ac6d4948f872fdaee02c2304154baa4faa36c7e14
fetched_at: '2026-06-29T00:09:30.786153+00:00'
page_id: '425458523'
product: rm
source: tdn-rm
title: Cadastro do 'Valor de Integração' e parametrização para o Repasse de Bolsa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458523
version: 2
---

---

Valores de Integrações são campos *especiais*, criados para auxiliar uma ação ou determinado processo que envolve *valores* entre este sistema e o sistema financeiro.  Estes campos são totalmente parametrizáveis pelo usuário que definirá o comportamento do mesmo em relação ao lançamento.

O Educacional utilizará este recurso para registrar a diferença a **menor** entre o valor cadastrado para o repasse de bolsa e o valor do lançamento referente à bolsa de crédito que estará sendo baixado.

**Importante**

* A utilização do 'Valor de Integração' para controlar a diferença a *menor* encontrada no Repasse de bolsa, somente estará disponível se, no módulo TOTVS Gestão Financeira, a base estiver parametrizada para realizar os cálculos da baixa por **prioridade** (*Ambiente | Parâmetros | TOTVS Gestão Financeira | Contas a Receber | Baixas | Manutenção de Baixas | Baixas 3/5 | Modo de Cálculo dos Valores da Baixa Parcial =* Baixa calculada por prioridade).

Para realizar o cadastro do 'Valor de integração', primeiramente é necessário que o usuário tenha permissão para manutenção neste cadastro. Confira as permissões no cadastro do perfil do usuário (Perfil Educacional-Tags: *Financeiro/Contábil | Geração | Financeiro | Valores de Integração Financeira |Incluir|Excluir|Editar* devem estar habilitadas).

O cadastro e associação do campo 'Valor de integração' poderá ser feito diretamente nos parâmetros deste sistema, para isto acesse *Ambiente | Parâmetros | Educacional | Financeiro | Educacional | Fin - Vlrs. Opcionais/Integração 3/3*. No local da pesquisa do campo, acione o botão *'Novo'* e inclua o campo que receberá a diferença a *menor* encontrada no Repasse de bolsa ou associe o campo previamente cadastrado (), respeitando sempre as regras à seguir.

**Regras:**

* O campo 'Valor de Integração' para ser utilizado no Repasse de bolsa, deve possuir obrigatoriamente Ação = **'Desconta'**, as outras opções disponíveis dentro deste cadastro **não** podem ser preenchidas, pois o sistema fará esta validação no momento da sua utilização (As opções 'Até vencimento' e 'Fórmula' devem obrigatoriamente ficar em branco).
* Após a primeira utilização deste campo, esta parametrização não poderá mais ser alterada, permanecendo desabilitada.
* Sempre que o valor cadastrado para o repasse de bolsa for **menor** que o valor do lançamento referente à bolsa de crédito, será *obrigatória a identificação*, nos parâmetros deste sistema, do campo 'Valor de Integração' que será responsável por realizar o controle deste valor.
