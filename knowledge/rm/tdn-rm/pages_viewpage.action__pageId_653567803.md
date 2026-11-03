---
content_hash: b2146f3da7c421d802cded3d833882f6e53f1b97134f737e3d8bb0f3eefefc22
fetched_at: '2026-06-29T00:11:12.477282+00:00'
page_id: '653567803'
product: rm
source: tdn-rm
title: Trocar Data de Admissão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=653567803
version: 14
---

## **CONTEÚDO**

1. **Versões**
2. **Visão Geral**
3. **Exemplo de utilização**
4. **Tabelas utilizadas**

## **01. Versões**

false

**A partir dos patches:**

* 12.1.33.197
* 12.1.34.113
* ou superiores.

## **02. VISÃO GERAL**

Este processo tem a função de realizar a alteração da data de admissão do funcionário e seus devidos históricos e período aquisitivo.

**Atenção:**

* Alterações poderá ser realizado somente em funcionários admitidos no mês ou próximo mês.
* Será gerado gatilho de gatilho de inclusão ou retificação dos eventos S-2200 ou S-2300.
* Caso tenha alguma produção lançada anterior a nova data de admissão não será realizado a alteração para funcionários (tipo "Rural").

## **03. EXEMPLO DE UTILIZAÇÃO**

11ParametrizaçãoParametrização

 Acesse o menu Serviços Globais| Segurança | Perfis

Selecione o sistema Folha de pagamento, edite o perfil desejado, vá em acesso aos menus e permita o acesso 01.01.01.257 Histórico Afastamento: Trocar Data de Admissão.

2Data de admissão mês atualData de admissão mês atual

 Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários, selecione o funcionário desejado e acesse Processos | Trocar Data de Admissão

**Observação**: Ao executar esse processo será gerado gatilhos correspondentes para o eSocial dos eventos.

* Caso do evento S-2240 caso a data de admissão atual seja menor que a nova data de admissão será gerado gatilhos de exclusão para todos os eventos da fila.
* Caso do evento S-2240 caso a data de admissão atual seja maior que a nova data de admissão será gerado gatilhos de exclusão somente para a data de admissão atual.

3Data de admissão próximo mêsData de admissão próximo mês

  Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários,  vá em  Processos | Trocar Data de Admissão

**Observação**: Ao executar esse processo será gerado gatilhos correspondentes para o eSocial dos eventos.

* Caso do evento S-2240 caso a data de admissão atual seja menor que a nova data de admissão será gerado gatilhos de exclusão para todos os eventos da fila.
* Caso do evento S-2240 caso a data de admissão atual seja maior que a nova data de admissão será gerado gatilhos de exclusão somente para a data de admissão atual.

4Data de admissão próximo mês alteração para competencia atualData de admissão próximo mês alteração para competencia atual

  Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários,  vá em  Processos | Trocar Data de Admissão

5Funcionário com produção agráriaFuncionário com produção agrária

Funcionário possui produção a partir do dia 10/05/2021

  Acesse o menu RH | Folha de Pagamento | Administração de Pessoal | Funcionários,  vá em  Processos | Trocar Data de Admissão

**Ao tentar executar para uma data posterior a data da produção agrária sistema apresenta erro.**

**Alterado para data anterior a produção agrária, sistema altera com sucesso.**

**Observação**: Ao executar esse processo será gerado gatilhos correspondentes para o eSocial dos eventos.

* Caso do evento S-2240 caso a data de admissão atual seja menor que a nova data de admissão será gerado gatilhos de exclusão para todos os eventos da fila.
* Caso do evento S-2240 caso a data de admissão atual seja maior que a nova data de admissão será gerado gatilhos de exclusão somente para a data de admissão atual.

## **04. TABELAS UTILIZADAS**

* PFHSTCATEGORIAESOCIAL, PFHSTCPGTO, PFHSTEND, PFHSTFCO, PFHSTHOR, PHSTOCORRENCIA, PFHSTSAL, PFHSTSEC, PFHSTSIT, PFHSTCODTIPOFUNCIONARIO, PFHSTCODRECEBIMENTO, PFHSTTIPOREGIMEJORNADA, PFUFERIAS, AHSTUTILIZAPONTO, PFHSTESTATUTARIO,PFUNC.
