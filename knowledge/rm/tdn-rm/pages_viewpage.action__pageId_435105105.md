---
content_hash: 08ded4b6fbc7a01f2f596e0ba8f0477ed93d6c030363d4e31d5d21962a398b2f
fetched_at: '2026-06-29T00:09:47.931840+00:00'
page_id: '435105105'
product: rm
source: tdn-rm
title: Novidades 12.1.20 - TOTVS Construção Gestão de Imóveis
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105105
version: 6
---

**Novidades 12.1.20**

---

**Vendas**  
**Contratos de Vendas**

* A partir desta versão é possível realizar a geração de Brindes através do PVI e integrado com o PROTHEUS.
* Para atender o mercado internacional, foi criado o processo do FIDEICOMISO para gerar o repasse financeiro das vendas imobiliárias, utilizando a geração de movimento de venda.

Para mais informações, consulte:   
Dados de Repasse do Empreendimento Processo- Gerar Movimento de Brinde Processo- Gerar Movimento de Venda  
**Contabilidade** Na contabilização de Venda Imobiliária, foram incluídos novos valores para incidência da contabilização. Estes valores são:

* Valor de Juros Vincendos Antes da Entrega - Valor de Juros Vencidos Antes da Entrega - Valor de Juros Vincendos e Vencidos Antes da Entrega - Valor de Juros Vincendos Após a Entrega - Valor de Juros Vencidos Após a Entrega - Valor de Juros Vincendos e Vencidos Após a Entrega - Valor Monetário Vincendos Antes da Entrega - Valor Monetário Vencidos Antes da Entrega - Valor Monetário Vincendos e Vencidos Antes da Entrega - Valor Monetário Vincendos Após a Entrega - Valor Monetário Vencidos Após a Entrega - Valor Monetário Vincendos e Vencidos Após a Entrega  
  Mais informações sobre o processo de contabilização acesse:  
  Eventos Contábeis  
     
  **Objetos Gerenciais**  
  **TINREL0062 - Ficha Financeira Analítica - Data Base e TINREL0063 - Ficha Financeira Sintética - Data Base**

* Foram implementados nos relatórios de ficha financeira o cálculo do deságio de acordo com a data base do relatório, assim é possível trazer as parcelas para o valor presente.
* Na tela de execução do relatório agora existe um parâmetro para calcular Juros e multa das parcelas.

Para mais informações, leia abaixo:  
FF002 Ficha Financeira Sintética FF001 Ficha Financeira Analítica  
   
   
**Aluguel**   
**Objetos Gerenciais**  
**TINREL0068 - Relatório de Áreas Ocupadas com Vínculo em Contratos de Locação**  
Foi implementado o Relatório de Áreas Ocupadas com Vínculo em Contratos de Locação, que irá auxiliar os usuários a encontrar as Áreas Disponíveis, focando na metragem desejada, isso facilita o gerenciamento das informações de forma rápida e segura.  
**TINREL0069 - Relatório de Verificação de Áreas Disponíveis**  
Foi implementado o Relatório de Verificação de Áreas Disponíveis, sendo que com este relatório o usuário poderá localizar em qual Contrato de Locação está amarrada determinada Área, o que facilita o gerenciamento dessas informações.  
**Contrato de Locação por Prazo Indeterminado**  
Foi implementado o parâmetro "Permite o Contrato de Locação ter prazo indeterminado", que quando marcado retira a obrigatoriedade do preenchimento do campo "Final vigência" do Contrato de Locação. Assim ao salvar o Contrato de Locação sem preencher esse campo, o mesmo terá o comportamento de Prazo Indeterminado.   
Para maiores informações acesse:  Parâmetros do Aluguel ou Contrato de Locação.   
**Permitir mesmo número de aditivo**  
Foi implementado o campo "Número do Aditivo no Cliente" em todos os cadastros de Aditivos do Contrato de Locação. Esse campo representa o número do aditivo físico do Contrato de Locação, dessa forma os aditivos do sistema podem ser agrupados a um número do Aditivo.   
Para a visualização de todos os aditivos do Contrato de locação foi criado o anexo "Visualização de Todos Aditivos", onde é possível realizar agrupamentos dos campos do aditivo, tais como "Número do Aditivo no Cliente".   
Para maiores informações acesse: Visualização de todos Aditivos ou Aditivos do Contrato de Locação.   
**Aditivo de Exclusão de Imóvel**  
Foi implementado um novo aditivo do Contrato de Locação, onde é possível excluir um ou mais imóveis do Contrato de Locação com a possibilidade de geração de multa rescisória.   
Para maiores informações clique aqui.  
**Campos de Juros e Multa nos Parâmetros de Integração**  
Foi implementado os campos de configuração de Juros e Multa de atraso no cadastro do Parâmetros de Integração.   
Para maiores informações clique aqui.  
**Escalonamento por M²**  
Foi implementado a possibilidade do Escalonamento alterar o valor médio do M² no Contrato de Locação. Dessa forma o valores dos lançamentos serão de acordo com o cálculo Valor M² Final \* Área ocupada (por período).   
Para maiores informações clique aqui.   
**Desconto por m²**  
Foi criado um novo Tipo de Desconto, onde será possível que o desconto seja aplicado no "Valor médio do m²" do Contrato de Locação. Além do Contrato de Locação, esse Tipo de Desconto foi inserido nas rotinas de Reajuste e Aditivo de Alteração dos Imóveis do Contrato.   
Para maiores informações sobre o Contrato de Locação clique aqui. Para maiores informações sobre o Aditivo de Alteração dos Imóveis do Contrato clique aqui.  
**Condomínio**   
**Cadastro de Cobrança por Orçamento**  
Este cadastro permite mapear as cobranças do condomínio baseadas no orçamento elaborado para a empresa; As informações desse cadastro serão utilizadas na apuração dos valores do condomínio durante o fechamento.   
Para maiores informações clique aqui  
**Processo de Calcular Fechamento**
