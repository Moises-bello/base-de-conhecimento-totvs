---
content_hash: e09f1d9b894769003f3f37c37fc6ae86398ffc5adcf767633917498a2d9aa002
fetched_at: '2026-06-29T00:09:35.542087+00:00'
page_id: '425459388'
product: rm
source: tdn-rm
title: Dimensões Controladoria
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459388
version: 2
---

**Dimensões Controladoria**

---

A Área Controladoria é dividida em subgrupos e cada subgrupo possui suas tabelas Fatos, conforme descrito abaixo:

* **Gestão Contábil e Orçamentária**: Contempla informações da Contabilidade Realizada e Orçamento Contábil, em valores e percentuais.

**1**. Contabilidade – (Tabela Fato HL9): Apresenta informações das contas contáveis relacionadas à contabilidade realizada.  
    
 **2**. Orçamento – (Tabela Fato HLC): Apresenta informações relativas aos lançamentos nas contas contábeis relacionada a contabilidade orçada.

* **Indicadores Econômicos Financeiros**: Contempla informações de Indicadores Econômico-Financeiros, em valores, índices e percentuais.

**1**. Indicadores Gerenciais – (Tabela Fato HLA): Apresenta informações de diversos indicadores econômicos e financeiros relacionados à gestão da empresa.  
 Os Conceitos que serão utilizados para carga das tabelas fatos são:

* Fato – Controladoria - Contabilidade.icp
* Fato – Controladoria - Orçamento.icp
* Fato – Controladoria - Indicadores Gerenciais.icp

Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
