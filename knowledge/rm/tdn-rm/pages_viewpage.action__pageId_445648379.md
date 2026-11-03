---
content_hash: bfea445b7a0a27aab92ed373149121bf09eafbfecdfe9331873d67b4e2cf94db
fetched_at: '2026-06-29T00:09:54.830430+00:00'
page_id: '445648379'
product: rm
source: tdn-rm
title: Relatórios - Reajuste de Índice
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445648379
version: 9
---

# Procedimentos para utilização

---

Este relatório é um objeto gerencial criado para exibir os respectivos índices de reajuste associados a um determinado contrato de locação.

Para utilizar este relatório é necessário importar o Objeto Gerencial 'TCGIRELALG0076 - Reajuste de Índice.TotvsReport' através de Gestão / RM Reports / Processo de Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação, basta então acessar Gestão / RM Reports / TOTVS Incorporação, e  selecionar o relatório TCGIRELALG0076 - Reajuste de  Índice.TotvsReport, ir em processos e clicar em "GerarRelatório".

Será exibida a tela de parâmetros para o relatório, com os seguintes campos:

* **Número do Contrato:** Caso deseje filtrar o contrato, informe o seu número ou parte dele neste parâmetro. Não é obrigatório, podendo ser deixado em branco para que todos os contratos que atenderem o período sejam exibidos
* **Data Inicial Reajuste e Data Fim Reajuste:** Período de reajuste dos contratos. Serão listados os reajustes e seus respectivos índices, cuja data de reajuste esteja dentro deste período. É obrigatório informar os valores para estes parâmetros

O Relatório será gerado dividido em 2 grupos, sempre agrupados para o contrato em questão, que trarão informações sobre:

* **Grupo 1:** Dados do contrato de locação;
* **Grupo 2:** Dados dos índices de reajuste.

Para facilitar a execução do relatório em ocasiões futuras, recomendamos anexá-lo na visão de Contratos de Aluguel dentro do TOTVS Incorporação. Para isso, basta seguir os seguintes passos:

# Incluir relatórios do RM Reports à visão

---

* Acesse os Anexos | Relatórios | Inserir Relatório.
* Selecione o relatório TCGIRELALG0076 - Reajuste de Índice.TotvsReport e execute o processo;
* Realize o vínculo do campo Coligada com o campo de Coligada do Contrato de Locação e avance;

* Após finalizar o processo, o relatório estará sempre disponível na visão de contratos.
