---
content_hash: b949358d7e58bbf6bacb324b04f9c15abdfcffab9ad48fcac5cbadfd61938c1a
fetched_at: '2026-06-29T00:11:32.363933+00:00'
page_id: '746516153'
product: rm
source: tdn-rm
title: 8.1 - Edição/Criação de Agendamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=746516153
version: 39
---

## O que são?

A ferramenta de **Agendamento** automatiza a execução de tarefas em horários e datas específicas, permitindo organizar e controlar ações de forma eficiente. Com ela, é possível otimizar processos e garantir que tarefas importantes sejam realizadas sem necessidade de intervenção manual.

## Para que servem?

O Agendamento serve para:

* Automatizar tarefas rotineiras.
* Garantir a execução de atividades em horários e datas previamente definidos.
* Otimizar o uso de recursos computacionais, distribuindo tarefas em diferentes horários e ambientes de execução.
* Minimizar erros humanos em processos que exigem execução regular.

## Exemplo de Uso

Como cadastrarComo Cadastrar 1. Navegação para o cadastro

 1. Navegue no menu do TOTVS Automação de Testes e clique em **Agendamentos → Cadastros.**

 2. Na tabela que será mostrada, clique no botão verde em destaque.

2. Preenchimento dos CamposIdentificação Nome

## Nome

Informe um nome pelo qual seja fácil identificar seu agendamento.

Versão

## Versão

A versão do Agendamento especifica a versão das Atividades que serão executadas.

*Exemplo utilizando a versão do RM*

*Exemplo utilizando a versão padrão*

Descrição

## Descrição

 Descreva seu Agendamento de uma maneira clara e mais detalhada para que qualquer usuário possa identificar o seu propósito.

Habilitado

## Habilitado?

Define se o agendamento está ativo e deve ser executado ou se está desativado e não será executado. Se marcado como "Sim", o agendamento será executado conforme programado. Se marcado como "Não", o agendamento estará desativado e não será executado até ser reativado.

Permissões

Aqui você poderá determinar qual ou quais grupos terão acesso ao seu **Agendamento** e ainda se poderá alterá-lo ou não. (Saiba mais sobre o que são os [Grupos](https://tdn.totvs.com/display/LRM/6+-+Grupos) no **TOTVS Automação de Testes**).

Gatilhos

Utilize para programar a execução do seu Agendamento.

**Uma vez:** Seu agendamento irá executar somente uma vez na data e hora informada.

**Diário:** Seu Agendamento irá executar todos os dias.

* + Intervalo de dias: Se deixar 0 (zero), será executado todos os dias. Se informar algum numero, será executado de tantos em tantos dias de acordo com o informado. Executará saltando a quantidade de dias especificada.
* Vigência: Utilize para determinar um período para a execução de seu Agendamento.  
  Validações:
  + Data inicial maior ou a igual a hoje.
  + Data Final maior ou igual a data inicial
  + Data inicial diferente de nula.
  + Data final pode ser nula.

**Semanal:** Utilize quando precisar escolher dias da semana para a execução do seu Agendamento que não sejam sequenciais. Ex.: Executar toda segunda-feira e toda quarta-feira.

* Vigência: Utilize para determinar um período para a execução de seu Agendamento.  
  Validações:

* + Data inicial maior ou a igual a hoje.
  + Data Final maior ou igual a data inicial
  + Data inicial diferente de nula.
  + Data final pode ser nula.
Ambientes de execução 

Utilize para determinar o modo de execução de seu Agendamento nos servidores.

* **Sequencial em um servidor:** O Agendamento será executado somente em um servidor. Caso exista mais de um servidor informado, será executado no servidor que tiver com maior disponibilidade para a execução de todas as Atividades deste Agendamento.
* **Sequencial em todos os servidores:** O Agendamento será executado em paralelo em todos os Servidores informados.

Adicione o servidor e o ambiente correspondentes à sua atividade.

**Atenção:** Para este tipo de execução, se algum dos servidores não puder ser acessado (se a VM não estiver ativa, se o Agent do TOTVS Automação de Testes não estiver disponível, ou se o ambiente especificado não existir), o status da execução do agendamento será marcado como falha.

**Saiba mais:**[Agent](https://tdn.totvs.com/display/LRM/13+-+Download+-+Agent) e [Servidor](https://tdn.totvs.com/display/LRM/5.+Servidores#Cria%C3%A7%C3%A3odeumgrupo--1297575106)

Notificações 

Utilize os seguintes critérios para determinar quando e-mail de conclusão do Agendamento será enviado:

* Não enviar e-mail
* Enviar sempre
* Quando o agendamento for concluído com sucesso.
* Quando ocorrer um erro durante a execução.

Adicione os destinatários que receberão o e-mail logo após a conclusão da execução do Agendamento.

Atividades 

Insira as Atividades que serão executadas neste Agendamento.  
Pode utilizar o nome da atividade para uma busca aproximada ou especificar o tipo para refinar os resultados. É possível inserir quantas atividades forem necessárias.

Certifique-se de que os ambientes selecionados para o agendamento estejam preparados para executar todas as atividades. Recomenda-se agrupar atividades relacionadas em um único agendamento para evitar a necessidade de alocar múltiplos recursos em um mesmo ambiente.

É permitido incluir a mesma atividade mais de uma vez em um único agendamento.

As atividades podem ser excluídas ou reordenadas conforme a necessidade do utilizador.

Ícones Seção Atividades

### **Arrastar:**

O ícone de Arrastar permite que você reordene as **Atividades**, movendo-os para a posição desejada. Isso facilita a organização e a estruturação das etapas, garantindo que sejam executadas na sequência correta.

### **Remover:**

O botão Remover permite excluir passos previamente adicionados a Atividade dos **Agendamentos** Utilizando este recurso, você pode manter a lista de passos atualizada e livre de informações desnecessárias ou incorretas.

Exemplo prático

Imagine que um técnico de TI precise chegar mais cedo todos os dias para realizar a limpeza das máquinas dos servidores antes da chegada dos funcionários. Com o uso de tarefas agendadas, essa atividade pode ser automatizada e iniciada diariamente no início da manhã, sem necessidade de intervenção manual.

*A seguir, apresentamos um exemplo de um projeto de teste com a atividade de Limpeza do Ambiente:*

*Atividade adicionada ao Agendamento:*

---

# Saiba mais

Certifique-se de que todos os Ambientes cadastrados no Agendamento possuam os recursos necessários para a execução correta das Atividades previstas.

Se o seu agendamento semanal incluir todos os dias, considere criar um agendamento diário para maior eficiência.

O registo dos Agendamentos só poderá ser salvo se todos os campos obrigatórios estiverem preenchidos. Para facilitar a visualização dos campos não preenchidos, será acrescentado um sinal de exclamação na secção que contiver algum campo obrigatório vazio. Ele só desaparecerá após o preenchimento dos campos obrigatórios.

Agendar tarefas, como backups ou sincronizações, durante horários de menor utilização do sistema (como de madrugada) reduz o impacto no desempenho e aumenta a eficiência das operações

# FAQ

**P: É possível visualizar o histórico de execuções anteriores de um agendamento?**  
R: Sim. O TOTVS Automação de Testes mantém um histórico completo de todas as execuções de um agendamento, incluindo a data, hora, resultado (sucesso ou falha) e logs detalhados de cada execução. Esse histórico pode ser acessado para auditoria e análise de desempenho.

**P: É possível automatizar restauração de backups de banco de dados usando agendamentos no TOTVS Automação de Testes?**  
R: Sim. É possível criar agendamentos no TOTVS Automação de Testes para realizar a restauração de backups de bancos de dados por meio das atividades inseridas no Projeto de Teste, definindo os horários e a frequência no Agendamento conforme necessário.

**P:****O TOTVS Automação de Testes suporta a execução paralela de agendamentos?**

R: Sim. O TOTVS Automação de Testes suporta a execução de múltiplos agendamentos em paralelo, o que é útil para processar várias tarefas simultaneamente e otimizar o uso dos recursos do servidor.
