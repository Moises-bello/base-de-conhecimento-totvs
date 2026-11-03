---
content_hash: 999d2ae3ee68e87f1f7b5dbe207ee9f4d6d3b8bd9eb97122189a368da6459d3f
fetched_at: '2026-06-29T00:09:54.826168+00:00'
page_id: '445648354'
product: rm
source: tdn-rm
title: Relatórios - Listagem de Garantias de Contratos Vigentes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=445648354
version: 11
---

# Procedimentos para utilização

---

Este relatório é um objeto gerencial criado para exibir as garantias de um determinado contrato de locação, ou de todos os contratos.

Para utilizar este relatório é necessário importar o Objeto Gerencial ***TCGIRELALG0074 - Listagem de Garantias de Contratos Vigentes.TotvsReport*** através de Gestão / RM Reports / Processo de Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação deste relatório, basta então acessar Gestão / RM Reports / TOTVS Incorporação, e  selecionar o relatório ***TCGIRELALG0074 - Listagem de Garantias de Contratos Vigentes***, ir em processos e clicar em "Gerar Relatório".

Será exibida a tela de parâmetros para o Relatório com os seguintes campos:

**Data Base:** Serão listadas as garantias dos contratos cuja vigência esteja dentro desta data. É obrigatório informar o valor para este parâmetro;

**Número do Contrato:** Caso deseje filtrar o contrato, informe o seu número ou parte dele neste parâmetro. Não é obrigatório, podendo ser deixado em branco para que todos os contratos que atenderem a Data Base sejam exibidos

O Relatório será gerado dividido em 3 grupos, sempre agrupados para o contrato em questão, que trarão informações sobre:

* Grupo 1: Dados do contrato de locação;
* Grupo 2: Dados dos locatários;
* Grupo 3: Dados dos fiadores/garantias;

Para facilitar a execução do relatório em ocasiões futuras, recomendamos anexá-lo na visão de Contratos de Aluguel dentro do TOTVS Incorporação. Para isso, basta seguir os seguintes passos:

# Incluir relatórios do RM Reports à visão

---

* Acesse os Anexos | Relatórios | Inserir Relatório.
* Selecione o relatório ***TCGIRELALG0074 - Listagem de Garantias de Contratos Vigentes.TotvsReport*** e execute o processo;
* Realize o vínculo do campo Coligada com o campo de Coligada do Contrato de Locação e avance;

* Em seguida é só selecionar o relatório que é listado no menu Anexos | Relatórios.
