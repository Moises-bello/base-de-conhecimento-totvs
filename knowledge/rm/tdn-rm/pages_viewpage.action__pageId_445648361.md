---
content_hash: 6e749c72eb28e059619eb4f637134ef6c71d11124617660355796e6fc55b77bb
fetched_at: '2026-06-29T00:09:54.828200+00:00'
page_id: '445648361'
product: rm
source: tdn-rm
title: Relatórios - Vencimentos de Contrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445648361
version: 5
---

# Procedimentos para utilização

---

Este relatório é um objeto gerencial criado para exibir os respectivos valores de vencimento dos imóveis associados a um determinado contrato de locação.

Para utilizar este relatório é necessário importar o Objeto Gerencial 'TCGIRELALG0075 - Vencimentos de Contrato.TotvsReport' através de Gestão / RM Reports / Processo de Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação deste relatório, basta então acessar Gestão / RM Reports / TOTVS Incorporação, e  selecionar o relatório TCGIRELALG0075 - Vencimentos de Contrato, ir em processos e clicar em "Gerar Relatório".

Será exibida a tela de parâmetros para o Relatório com os seguintes campos:

**Data Início e Data Fim:** Período de vencimento dos contratos. Serão listados os contratos cujo fim de vigência esteja dentro deste período. É obrigatório informar os valores para estes parâmetros

**Número do Contrato:** Caso deseje filtrar o contrato, informe o seu número ou parte dele neste parâmetro. Não é obrigatório, podendo ser deixado em branco para que todos os contratos que atenderem ao período sejam exibidos

O Relatório será gerado dividido em 3 grupos, sempre agrupados para o contrato em questão, que trarão informações sobre:

* Grupo 1: Dados do contrato de locação;
* Grupo 2: Dados dos locatários;
* Grupo 3: Dados dos vencimentos/imóveis do contrato;
