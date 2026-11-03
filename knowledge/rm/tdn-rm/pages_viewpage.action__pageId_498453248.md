---
content_hash: 1b9ca156741b5c0495ad3bdeb8daede8396612f36445e8c8e533407c68c1ab6b
fetched_at: '2026-06-29T00:10:22.658804+00:00'
page_id: '498453248'
product: rm
source: tdn-rm
title: Relatórios - Listagem de Garantias com Validade Final no Período
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=498453248
version: 8
---

# Procedimentos para utilização

---

Este relatório é um objeto gerencial criado para exibir as **Garantias** de, um ou mais ,**Contratos de Locação** cuja Validade Final da garantia esteja dentro de um dado período.

Para utilizar este relatório é necessário importar o Objeto Gerencial **TCGIRELALG0094 - Listagem de garantias com validade final no período.TotvsReport** através de Gestão / RM Reports / Processo de Importar Estrutura de Relatório.

O relatório estará disponível na pasta de Objetos Gerenciais da instalação do RM.

Após a importação deste relatório, basta então acessar Gestão / RM Reports / TOTVS Incorporação, e  selecionar o relatório **TINRELALG0094 - Listagem de garantias com validade final no período**, ir em processos e clicar em "Gerar Relatório".

Será exibida a tela de parâmetros para o Relatório com os seguintes campos:

**Data Início e Data Fim:** Período para filtrar a validade final das garantias. Serão listadas as garantias cuja **Validade Final** esteja dentro deste período. É obrigatório informar os valores para estes parâmetros

**Número do Contrato:** Caso deseje filtrar o contrato, informe o seu número ou parte dele neste parâmetro. Não é obrigatório, podendo ser deixado em branco para que todos os contratos que atenderem a Data Base sejam exibidos

O Relatório será gerado dividido em 3 grupos, sempre agrupados para o contrato em questão, que trarão informações sobre:

* Grupo 1: Dados do contrato de locação;
* Grupo 2: Dados dos locatários;
* Grupo 3: Dados dos fiadores/garantias;

Para facilitar a execução do relatório em ocasiões futuras, recomendamos anexá-lo na visão de Contratos de Aluguel dentro do TOTVS Incorporação. Para isso, basta seguir os seguintes passos:

# Incluir relatórios do RM Reports à visão

---

* Acesse os Anexos | Relatórios | Inserir Relatório.
* Selecione o relatório TCGIRELALG0094 - Listagem de garantias com validade final no período.TotvsReport e execute o processo;
* Realize o vínculo do campo Coligada com o campo de Coligada do Contrato de Locação e avance;

* Em seguida é só selecionar o relatório que é listado no menu Anexos | Relatórios.
