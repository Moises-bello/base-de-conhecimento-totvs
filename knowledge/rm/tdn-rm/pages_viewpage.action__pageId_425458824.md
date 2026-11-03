---
content_hash: 348cb0c3b4ba10a1880da372d0c6835996a9e55265a711b6a3a743be2f16fa1a
fetched_at: '2026-06-29T00:09:32.323088+00:00'
page_id: '425458824'
product: rm
source: tdn-rm
title: Atendimentos - Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458824
version: 4
---

**Gerais**

---

**Relatório a ser utilizado para Imprimir Atendimentos**  
   
A partir da visão e/ou edição de atendimentos existe um processo disponível para impressão de ocorrências. Neste aparecem duas opções: "Relatório Padrão de Atendimentos" e "Relatório de Tipo de Atendimento". Após escolher a opção, no disparo do relatório o sistema busca o relatório selecionado e o gera (dando a opção de impressão posteriormente).  
   
O parâmetro "Relatório Padrão de Atendimentos" deve ser criado no recurso de gerador de relatórios e deverá conter informações que deverão ser obtidas a partir do(s) atendimento(s) selecionado para a execução do processo pois o sistema irá enviar a chave primária deste(s) atendimento(s) para a engine que gera o relatório.

**Visão de atendimentos**

---

**Consulta SQL a ser utilizada para recuperar os registros para a visão de atendimentos**  
   
O sistema permite o uso de uma SQL personalizada de acordo com a necessidade de cada organização. Internamente existe uma consulta que traz alguns campos a serem exibidos na visão de atendimentos mas, pode ocorrer de tais campos não atenderem a real necessidade, então este parâmetro pode cadastrado com uma nova consulta SQL. A partir de então ao se acionar a visão de atendimentos o sistema irá utilizar esta consulta. Vale ressaltar que  a consulta personalizada por tipo de atendente possui prioridade sobre a consulta personalizada geral. Ordem de Prioridade: Consulta Personalizada por Tipo de Atendente, Consulta Personalizada Geral, Consulta fixa interna do Sistema.  
   
Algumas observações devem ser seguidas para a elaboração de tal consulta:

* a consulta NÃO pode possuir a clausula WHERE;
* obrigatoriamente a clausula FROM deve fazer referência a tabela HATENDIMENTOBASE;
* os seguintes campos são obrigatórios na cláusula SELECT:  
     
  CODCOLIGADA, CODLOCAL, CODATENDIMENTO, CODSTATUS, CODTAREFA, CODCOLIGPRD, CODPRODUTO, CODATENDENTERESP, CODCOLIGADARESP, CODCOLIGADAALARME, CODATENDALARME, PRAZOLIMITE, CODCOLIGADARPR, CODRPR, ASSUNTOOC, CODITEMPRD, PRIORIDADE, FECHAMENTO.  
     
  **Não permite cadastrar atendimento para fornecedor**  
     
  Um atendimento é aberto quando uma solicitação é realizada. O solicitante do atendimento pode ser um registro da tabela de cliente/fornecedor, prospect, aluno, pessoa ou professor. A tabela que mantém os clientes é a mesma tabela que mantém os fornecedores onde pelo valor de um determinado campo é feito a diferenciação de cliente e fornecedor. Este parâmetro tem o objetivo de impedir (ou não) que os atendimentos possam ser abertos por clientes que estão cadastrados com a especificação de fornecedor.   
     
  **Restringir visualização de atendimentos por hierarquia de localidade**  
     
  O cadastro de localidades pode ser realizado utilizando uma hierarquia. Os atendentes devem ser alocados em localidades.  Por exemplo: Uma árvore de hierarquia montada pelas localidades :  
     
     
                                                               Localidade01  
     
                           Localidade02                                               Localidade03  
     
  Localidade04     Localidade05     Localidade06               Localidade07     Localidade 08  
     
     
  Caso este parâmetro esteja marcado, os atendentes alocados em uma localidade somente acessarão os atendimentos de atendentes de sua localidade ou atendimentos que já tenham passado por ele, isto é, o atendente da localidade 4 não acessará (enxergará) os atendimentos dos atendentes das localidades 1, 2, 5, 6, 3, 7, 8 mesmo que o nível hierárquico seja o mesmo (no caso da localidade 4, as localidades de mesmo nível 5, 6, 7, 8). Os atendentes de um nível hierárquico superior enxergam as atendimentos dos atendentes subordinados (pela hierarquia de localidade) mas respeitam a regra acima. No exemplo acima, atendentes da localidade 2 acessam (enxergam) atendimento de 4, 5, 6 mas não enxergam as atendimentos de 3, 7, 8.  
     
  Os atendentes da localidade de nível hierárquico máximo (pela hierarquia de localidade) enxergam todos os atendimentos de atendentes de localidades subordinadas (no exemplo acima os atendentes da localidade 1). Este parâmetro se aplica tanto a visão de atendimentos quanto atendimentos retornados pela pesquisa de atendimentos.   
     
  **Exceções para a restrição de nível de acesso**

* **Permitir visualizar atendimentos abertos pelo atendente**
* **Permitir visualizar atendimentos que passaram pelo atendente**

**Edição de atendimentos**

---

**Obrigar preenchimento do ampo 'Solicitação' ao inserir atendimentos**   
   
Este parâmetro informa ao sistema que o campo 'Solicitação' deve ser obrigatoriamente preenchido (ou não) ao se criar atendimento via a tela de edição de atendimentos. Esta verificação é realizada no momento de tentar salvar o registro de atendimento.    
   
   
**Apresentar campo 'Número de Série' no formulário de edição**   
   
O atendimento possui um campo que pode ser valorado com um número de série referente a um produto ou referente ao cliente (que pode servir inclusive para identificar o produto e cliente). Este parâmetro define se tal campo estará disponível e visível na tela deedição do atendimento para que possa ser preenchido.  
   
   
**Obriga Selecionar tipo ou modelo de atendimento na abertura de atendimentos**  
   
O sistema obriga a seleção de um tipo (respeitando a configuração da primeira etapa e a liberação de acesso no perfil) ou modelo de atendimento (carrega todos os registros da coligada atual e preenche os campos conforme o modelo) para abertura de novos atendimentos.    
   
**Bloquear abertura de atendimentos para os tipos de clientes**  
   
  É possível configurar para que apenas alguns tipos de clientes possam ser utilizados para abertura de atendimentos. Para definir qual tipo de cliente (Aluno, Cliente, Pessoa, Professor, Prospect) não poderá abrir atendimentos, existe um parâmetro para bloquear os tipos de clientes que forem selecionados. Ao selecionar o tipo de cliente, não será possível realizar abertura de atendimentos com ele.

**Parâmetros do App "Minhas Aprovações"**

---

**URL de configuração do App "Minhas Aprovações":**

**Número de dias para manter notificações**

O número de dias para manter notificações determina a quantidade de dias que os registros serão mantidos no banco de dados. Assim quando for incluido um novo atendimento, serão mantidas apenas as notificações de atendimentos incluídos dentro deste intevalo de dias.
