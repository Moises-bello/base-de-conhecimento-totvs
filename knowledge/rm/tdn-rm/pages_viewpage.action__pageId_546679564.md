---
content_hash: 7b4b00263820a2d27b471d855296b5bf96d4b4b53259df0571887694c45b6ac8
fetched_at: '2026-06-29T00:10:41.916463+00:00'
page_id: '546679564'
product: rm
source: tdn-rm
title: Reajuste Revitalizado / Conversor
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546679564
version: 15
---

Para utilizar o Reajuste Revitalizado é necessário executar um conversor para que a base de dados seja parametrizada.

**Após executar o conversor de reajuste, o usuário deverá:**

* **Reiniciar o serviço do host;**
* **Executar o [Comparador de Reajustes](https://tdn.totvs.com/display/LRM/Comparador+de+Reajustes) para validar a base de dados em um ambiente de homologação, exceto para clientes que utilizam fórmulas.**

Para executar o conversor acesse o executar na lateral direita do sistema e pesquise por "**Conversor Reajuste**".

#### **Configurar o ambiente com:**

* 18 execuções de jobs simultâneos, [configurado no Alias do RM.exe](https://tdn.totvs.com/pages/viewpage.action?pageId=271400764#SQL-214524341);
* 8 reajustes paralelos, [configurado no parametrizador do TCGI](https://tdn.totvs.com/pages/viewpage.action?pageId=435105185).

## **Etapas do Conversor:**

1. O conversor irá habilitar o novo reajuste somente para cliente piloto e qualquer base dentro da rede da TOTVS;
2. As fórmulas do produto TIN serão recompiladas para evitar o erro com o novo provider de fórmula;

---

**Após a conversão como o sistema irá se comportar com as vendas já cadastradas?**

As vendas já cadastradas irão continuar sendo reajustadas utilizando o reajuste antigo, sem a opção de utilizar as novas funções de fórmulas liberadas.

Na tabela **XVENDA** foi criada uma nova coluna de nome **HABILITANOVAENGINEVENDA** na qual será utilizada para identificar se a venda foi ou não criada após a conversão para o reajuste revitalizado.

* Somente para as novas vendas que os  e o processo de  estarão disponíveis.

**Exceções e restrições:**

* Para clientes que possuem a maquina de cálculo de reajuste denominada "Nova Engine", as vendas criadas antes da conversão do reajuste também receberão a atualização do campo HABILITANOVAENGINEVENDA = 1 e poderão contar com as funcionalidades de calculo utilizando as novas funções de fórmulas e o processo de alteração global das regras.
* O conversor do reajuste não será executado caso existam contratos com parcelas de resíduo em aberto.

Informação Importante:

A base de dados não pode ser convertida para o novo reajuste com parcelas em aberto de resíduos.  
Na coligada [X], a venda [XXX] possui resíduo em aberto que impede a conversão.

Compilar Fórmulas de Reajuste

Após a execução do conversor será disparado um outro processo para compilar as fórmulas do TCGI para o novo provider.

Este processo será executado em jobs simultâneos para melhor performance

Poderá ser chamado também no menu lateral direito, executar e digitar "Compilar Fórmula TCGI"

Confira as novidades do .
