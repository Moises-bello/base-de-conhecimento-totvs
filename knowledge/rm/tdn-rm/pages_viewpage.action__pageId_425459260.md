---
content_hash: 34ecfcb801b066a07632f026232eaa29ee9efc5a3e753809bbf42efd1a631fed
fetched_at: '2026-06-29T00:09:34.839771+00:00'
page_id: '425459260'
product: rm
source: tdn-rm
title: Dimensões RH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459260
version: 4
---

**Fatos RH**

---

A Área de Recursos Humanos é dividida em subgrupos e cada subgrupo possui suas tabelas Fatos, conforme descrito abaixo:

* **Analise dos Treinamentos:** Contempla informações dos Treinamentos Realizados e em Andamento, e das Bolsas de Estudos, em quantidades e valores dos Colaboradores.

**1**. Treinamentos Colaboradores (Tabela Fato HLM): Apresenta informações de quantidade de colaboradores, horas e valores relacionados aos treinamentos realizados.

**2**. Analise Treinamento por Tipo de Custo (Tabela HQV): Apresenta os dados dos treinamentos que foram realizados pelos colaboradores da organização, categorizando por tipo de custo.

* **Gestão de Gastos com Pessoal:** Contempla informações de Folha de Pagamento e Banco de Horas, em valores, quantidades e percentuais.

**1**. Banco de Horas (Tabela Fato HLO): Apresenta informações de quantidade e valores do banco de horas dos colaboradores. Para extração da quantidade de Horas do funcionario, somente sera enviado ao Cognos as horas de periodos consolidados no RH, com isto o saldo de periodos em aberto não sera considerado.  
    
 **2**. Folha de Pagamento (Tabela Fato HLP): Apresenta informações relacionadas aos cálculos da folha de pagamento dos colaboradores.

* **Gestão da Vida Profissional:** Contempla informações da Vida Profissional (Indicadores Demográficos, Movimentações Funcionais e Rotatividade), em valores, quantidades e percentuais.

1. Vida Profissional (Tabela Fato HLQ): Apresenta informações relacionadas à vida profissional dos colaboradores.

2. Reclamações de Colaboradores (Tabela Fato HLF).

3. Recrutamento de Colaboradores (Tabela Fato HLG).

**Observações.:**  
    
 Na execução dos relatórios é considerado:

* O funcionário de maior DATAADMISSAO evitando duplicidade de registro;
* A última mudança de cargo do funcionário;
* Atualmente, não existe integração da requisição de treinamento com a turma. Não é enviado para o Cognos IBM a informação de qual requisição solicitou o treinamento devido processo de análise que está sendo executado.  
      
   Os Conceitos que serão utilizados para carga das tabelas fatos são:

* Fato - RH - Analise Treinamento por Tipo de Custo
* Fato - RH - Análise Treinamentos
* Fato - RH - Banco  de Horas
* Fato - RH - Folha de Pagamento
* Fato - RH - Reclamações de Colaboradores
* Fato - RH - Recrutamento de Colaboradores
* Fato - RH - Vida Profissional

Os registros nestas tabelas serão incluídos na Stage Area através da execução dos Conceitos importados. Pra isto acontecer conforme demanda do cliente deve-se agendar os Conceitos para serem executados via Jobs. Este procedimento deverá ser configurado para todos os Conceitos.  
    
 Lembrando que a partir da versão 11.40.15 é possível realizar o agendamento nos Conceitos de maneira simultânea, ou seja, está disponível a opção de selecionar todos os Conceitos referentes aos Cadastros Comuns e definir Data, Hora e sua repetição de maneira simultânea. É indicado definir um horário que não tenha usuários utilizando os sistemas da Linha RM e também que não aja conflito com o horário de outras áreas do BI.  
    
 Para isto acontecer é necessário alterar os arquivos de configuração para utilizar o ambiente 3 Camadas. Deve-se adicionar nos arquivos a Tag abaixo:  
 <add key="JobServer3Camadas" value="True" />
