---
content_hash: a708f5d3d64b79cc04498c87af08f0ba146c1dff772f28f890bd6e9dd34a012e
fetched_at: '2026-06-29T00:09:34.064276+00:00'
page_id: '425459128'
product: rm
source: tdn-rm
title: Fluxo de Atendimentos (Global)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459128
version: 13
---

**Fluxo de Atendimentos (Global)**

---

Este recurso foi criado através do TOTVS Aprovações e Atendimento mas é disponibilizado para todos os módulos da Linha RM. Trata-se de um fluxo de trabalho que permite maior interação com todas as telas de qualquer sistema da linha RM, sendo possível bloquear processos e edições de registro.

Esta funcionalidade garante segurança para o processo, auxiliando no conjunto de regras de negócio da organização além de contribuir para automatização das ações.

**Observação.:** Para que o recurso funcione corretamente, deve ser configurado nos parâmetros Globais (Aba Fluxo de Atendimentos) a flag "Usar o Fluxo de Atendimento do TOTVS Aprovações e Atendimento".  
**Gerenciamento do Fluxo de Atendimento (Global)**

Este recurso permite também a utilização de um parâmetro que permite que os atendimentos sejam gerados em uma coligada como centralizadora.

Caso se deseje utiliza esta forma é necessário habilitar o parâmetro que define qual será a coligada centralizadora.

Caso utilize a coligada centralizadora essa coligada definida neste parâmetro será a coligada considerada no contexto

Acesse : Menu principal RM | TOTVS Aprovações e Atendimento | Ambiente | Parâmetros | Parâmetros Globais | Fluxo de Atendimentos

Habilitando este parâmetro quando o atendimento for gerado o sistema respeitará a coligada definida , a visualização do atendimento poderá ser realizada no anexo  **Atendimentos relacionados ao registro.**

Este anexo permite  vincular atendimento a um atendente pelo processo" **Criar fluxo associado ao registro** " e exibe quais atendimentos estão relacionados ao registro de forma idêntica a visão de atendimentos.

O processo de Fluxo de Atendimentos será visível em qualquer cadastro mas para sua execução é necessário parametrizar o fluxo e gerar o atendimento relativo ao registro.

Veja o exemplo abaixo, em um processo no qual podemos usar o Fluxo de Atendimento:

   
**Gerenciar**  
   
Conforme na opção Fluxo de Trabalho demonstrada acima, temos a opção "Gerenciar", onde criamos o Fluxo de Trabalho determinado para aquela tela e/ou processo que queremos impor os bloqueios.   
  
Para criar e configurar um fluxo, devemos clicar em "Novo". Selecionar o tipo de fluxo: RM CRM e informar o grupo, e então os tipos e modelo pertencentes a ele serão carregados.

   
O próximo passo é parametrizar as etapas do tipo de atendimento, informando a(s) condição(ões) para bloquear os processos (os processos devem ser selecionados) e a(s) condição(ões) para bloquear a edição do registro. Este procedimento deve ser realizado para todas as etapas do fluxo de acordo com as reais necessidades. Vale ressaltar que o sistema verifica a configuração etapa por etapa, se caso somente a primeira etapa do fluxo for parametrizada, quando o atendimento seguir para a próxima etapa, os bloqueios não mais serão realizados.

Temos também opção de configurar uma condição necessária para que o atendimento seja gerado através da caixa "Condição de Bloqueio", vale ressaltar que todas as opções devem ser inseridas dentro desse filtro caso contrário ao tentar selecionar uma nova condição a anterior será apagada.   
   
Nessa condição é informado o item, o operador ( que pode ser: =, <>, >, >=, <, <=, IS NULL, IS NOT NULL, LIKE, NOT LIKE, BETWEEN, IN (Valores) e NOT IN (Valores)) e o valor. Além do modelo de atendimento, o assunto e a solicitação que serão usados como sugestão para o atendimento. Para os campos: assunto e solicitação, o recurso de incluir tag´s está disponível.  
   
Com o botão direito, o recurso de "Inserir campo do registro" será apresentado, basta selecionar o campo desejado e o mesmo será acrescentado entre chaves {} e com a nomenclatura do banco. Somente com a condição totalmente satisfeita o atendimento será gerado.  
   
**Esclarecimentos sobre as definições:**  
   
Condição para criação de atendimento – Nesse componente qualquer campo do cadastro seguido de um operador e um valor podem criar uma ou várias condições. Sempre que o processo "Gerar atendimento para o registro" for executado, essas condições serão testadas e o atendimento somente será gerado caso todas as condições forem verdadeiras.  
   
Assunto do Atendimento – Esse campo será usado no campo assunto do atendimento que será gerado pelo processo "Gerar atendimento para o registro". Ao clicar com o botão direito o recurso de inserir tag´s (Inserir campo do registro) é disponibilizado.  
   
Solicitação do Atendimento – Esse campo será usado no campo solicitação do atendimento que será gerado pelo processo "Gerar atendimento para o registro". Ao clicar com o botão direito o recurso de inserir tag´s (Inserir campo do registro) é disponibilizado.  
   
**Processo "Gerar atendimento para o registro"**  
   
 Este processo gera automaticamente um atendimento para o registro selecionado desde que o mesmo satisfaça as condições configuradas. O atendimento é criado com o modelo, assunto e solicitação informados na parametrização. Quando o atendimento entrar na etapa que possui os bloqueios, os mesmos serão visualizados mas não poderão ser executados.  
   
**Anexos – Atendimentos relacionados ao registro**  
Este anexo permite  vincular atendimento a um atendente e exibe quais atendimentos estão relacionados ao registro de forma idêntica a visão de atendimentos.
