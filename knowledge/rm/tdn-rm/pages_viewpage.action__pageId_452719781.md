---
content_hash: 3692230850b1ad5e029301514d9aae5f46fb211ff2a7a201facc374bc255cd1d
fetched_at: '2026-06-29T00:10:10.006866+00:00'
page_id: '452719781'
product: rm
source: tdn-rm
title: Alteração Global de Rateio Fixo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719781
version: 2
---

Neste módulo será possível alterar e/ou estabelecer uma configuração de rateio fixo de centro de custo para um ou mais funcionários simultaneamente.  
 **Observação**  
 Este módulo estará disponível apenas se o parâmetro: "Utiliza Cálculo por Centro de Custo" do menu Opções | Parâmetros | RM Labore | Pasta Parâm. Cálculo estiver marcado.   
 **Incluindo rateio fixo para os funcionários**  
 Para incluir rateio fixo para funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Alteração Global de Rateio Fixo (.Net), selecionar o funcionário desejado, definir o(s) centro(s) de custo a ser incluído, definir o percentual e clicar no botão: "Executar".  
 **Alterando rateio fixo para os funcionários**  
 Para alterar rateio fixo de funcionários, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Alteração Global de Rateio Fixo (.Net), selecionar o funcionário desejado, definir o(s) centro(s) de custo a ser alterado, definir o percentual e clicar no botão: "Executar".  
 **Importante**  
 Para os dois casos acima, é possível definir a distribuição do rateio fixo dos Centros de Custo por valor, para isso o parâmetro "Rateio Fixo por Valor" do menu Opções | Parâmetros | RM Labore | Pasta Parâm. Cálculo deverá estar marcado.   
 **Calculando rateios conforme valores dos Salários Compostos**  
 Para incluir rateio fixo para funcionários a partir das informações do salário composto, o usuário deverá acessar: Rotinas | Alterações Globais de Funcionários | Alteração Global de Rateio Fixo (.Net), selecionar o funcionário desejado e marcar o parâmetro "Calcula Rateios Conforme Valores do Salário Composto" e clicar no botão: "Executar".

**Observação:**  
 Este parâmetro somente será exibido para clientes que têm integração com o Totvs Educacional e estando marcado o parâmetro "Reprogramação salarial detalhada por Centro de Custo" em Opções | Parâmetros | RM Labore | Gestão Educacional. A alteração será feita considerando os registros selecionados em Cadastros | Funcionários | Pasta Salário Composto "Eventos por centro de custo" e lançará em Cadastros | Funcionários | Rateio fixo.
