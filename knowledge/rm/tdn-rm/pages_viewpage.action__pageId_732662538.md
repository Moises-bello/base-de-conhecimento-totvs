---
content_hash: ab5cfab560d81b672343852167865b7aa83cc4d7c647aaac933a7ea2ab1ad9d5
fetched_at: '2026-06-29T00:11:28.600783+00:00'
page_id: '732662538'
product: rm
source: tdn-rm
title: Novo Atendimento - Visão de Atendimento - Edição de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=732662538
version: 11
---

Ao clicar duas vezes para acessar a tela de **Edição do Atendimento**, a partir da tela de [Visão de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=732660488), o Atendente poderá acesso às opções abaixo, além dos Anexos e Processos da [Visão de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=732660488), que possibilitam a análise e a interação com o Cliente:

* Aba **Identificação**:

**Dados do Cliente:** Neste agrupador são exibidos o *Nome do Cliente* e as formas de contato com o mesmo, como Número de Telefones *Celular*, *Fixo* e *Comercial* e também o *Email*, Todas essas informações tem uma ação ao se clicar sobre elas,

Por exemplo: ao clicar no Nome do Cliente, é aberto o cadastro do mesmo, facilitando a obtenção de mais informações; ao clicar sobre um número de telefone, o sistema tentará abrir um programa para que o Atendente faça a ligação para este número. e ao clicar sobre o Email o sistema abrirá um programa para que o Atendente possa escrever e enviar um email para este Cliente;

É importante ressaltar que para as ações externas ao ambiente RM, as ações acima utilização os programas configurados como padrão no sistema operação da estação de trabalho do Atendente;

Caso o Atendimento editado seja de um [Tipo de Atendimento](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI) que permita ao Cliente escolher o Período para Visitas, o sistema exibirá o agrupador abaixo nesta tela de edição:

**Preferência de Período para Visitas:** são exibidos os dias da semana que o Cliente escolheu para receber a visita para vistoria da demanda deste Atendimento. Importa

**Turno:** são exibidos os Turnos dos dias acima, que o Cliente escolheu para receber a visita;

**Tipo de Garantia:** é exibido o [Tipo de Cobertura de Garantia](https://tdn.totvs.com/display/LRM/02+-+TCGI+-+Atendimento+-+Tipos+de+Coberturas) que o Cliente utilizou para abrir este Atendimento. Ao clicar nesta informação o sistema apresentará os dados da Garantia genérica;

**Dados do Contrato:** Neste agrupador o sistema apresenta os dados de acordo com o tipo do Contrato que o Cliente utilizou para abrir este Atendimento. São apresentadas as informações de acordo com os tipo de Contrato abaixo:

**Contrato de Venda:** Número da Venda, Nome de Fantasia do Empreendimento, Unidade e Subunidade deste contrato. Ao clicar sobre alguma dessas informações o sistema abre o seu cadastro para que o Atendente visualize mais detalhes sobre o mesmo; ou

**Contrato de Locação:** Código de Identificação do Contrato de Locação, Descrição do Imóvel, Descrição da Área e Área Ocupada por este Imóvel. Aqui também ao clicar sobre alguma dessas informações o sistema abre o seu cadastro para que o Atendente visualize mais detalhes sobre o mesmo;

**Iniciar Atendimento:** Neste agrupador são exibidas a Data de Abertura deste Atendimento, a Data de Fechamento, a Data do Primeiro Contrato e a Quantidade de Agendamentos para este Atendimento;

**Atendimento do TAA:**, Este campo apresenta um link para se abrir e editar o atendimento diretamente no TAA, caso seja necessário alguma interação diretamente no mesmo;

**Resultado do Contrato:** O Atendente deve utilizar este campo para informar o Resultado do Contato com o Cliente. Este campo é obrigatório e deve ser preenchido ao se salvar cada Descrição no Histórico;

**Agendar Atendimento:** O Atendente pode utilizar este campo para Agendar o Atendimento. Esta informação será utilizada pelo processo de [Agendar Atendimento](https://tdn.totvs.com/display/LRM/Agendar+Atendimento) para [Despertar](https://tdn.totvs.com/display/LRM/Despertar+Atendimento) o Atendimento.

Ao marcar esta opção, o sistema habilita os campos abaixo para preenchimento:

**Data e Horário do Agendamento:** utilize este campo para registrar a data e o horário agendado para este Atendimento

**Previsão Final:** Informe a previsão de conclusão das ações previstas para este agendamento. Esta informação também será usada para calcular o [Prazo Limite](https://tdn.totvs.com/display/LRM/Agendar+Atendimento) este Atendimento.

Ainda neste agrupador, de *Iniciar Atendimento*, são exibidos os dois botões abaixo, para que o Atendente realize o [Apontamento Automático](https://tdn.totvs.com/pages/viewpage.action?pageId=425458983)  do tempo gasto na análise deste Atendimento. A configuração desta funcionalidade deve ser realizada nos [Parâmetros do TOTVS Aprovações e Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=425458983).

Botão **Iniciar Apontamento:** Este botão permite ao Atendente iniciar o Apontamento Automático do tempo gasto na análise deste Atendimento

Botão **Concluir Apontamento:** Este botão encerra o Apontamento Automático do tempo gasto na análise deste Atendimento.

**Histórico da Descrição:** Este quadro apresenta o Histórico de todas as interações registradas para este Atendimento;

**Descrição:** Neste campo deve ser digitado o texto descritivo das atividades e interações realizadas. Este texto pode ser apenas interno ao Atendimento ou também pode ser publicado no Fórum/Meu Imóvel/Portal do Cliente, através da opção "**Publicar a Discussão no Forum?**" localizada ao lado do botão para **Salvar** essa Descrição;

Caso este Atendimento esteja em uma [Etapa](https://tdn.totvs.com/display/LRM/Novo+Atendimento+-+Cadastros+-+Tipo+Atendimento+TCGI+-+Etapas) cuja parametrização exija o preenchimento da Lista de Verificação/[Checklist](https://tdn.totvs.com/display/LRM/Atendimento+TCGI+-+Etapas+-+Checklist) ou permita a geração de um [Movimento](https://tdn.totvs.com/pages/viewpage.action?pageId=435105038) para Serviço, o sistema exibirá os botões abaixo:

Botão **Checklist:** Este botão abre o [Checklist](https://tdn.totvs.com/pages/viewpage.action?pageId=435104889) que está associado à esta Etapa do Atendimento.

Em uma mesma Etapa, *Atendente* pode preencher o Checklist ao poucos, porém ao preenchê-lo e marcar a opção para "Finalizar o Checklist da Etapa?", o mesmo não poderá mais ser editado.

Botão **Gerar Movimento:** Este botão abre a tela para que o Atendente possa gerar o Movimento associado à esta Etapa do Atendimento;

**Etapa Atual:** Este campo exibe a informação sobre a Etapa Atual deste Atendimento. O mesmo não é editável;

A partir do *Patch Específico 12.1.2302.125* o sistema exibe também o **Status Atual** do Atendimento.

Botão **Avançar Etapa:** Este botão é utilizado para avançar a Etapa do Atendimento. Ao acioná-lo, o sistema irá validar as ações realizadas na Etapa Atual do Atendimento e caso não haja nenhuma inconsistência avançará o mesmo para a próxima Etapa definida para este Tipo de Atendimento.

* Aba **Financeiro:**

Esta aba apresenta:

* + Os **Lançamentos/Parcelas Financeiras em Atraso**, permitindo ao Atendente visualizar e calcular os valores devidos pelo Cliente e conforme as *Permissões* aplicadas ao *Perfil* do mesmo, realizar a emissão de boletos, negociação, etc; e
  + Os **Acordos Realizados** para este Cliente.

* Aba **Visão Cliente 360**: Ao acessar esta aba, o sistema apresenta ao Atendente a tela do Novo Cockpit com a [Visão 360](https://tdn.totvs.com/pages/viewpage.action?pageId=709413990) dos dados deste Cliente, expandindo o acesso deste, para informações além das do Atendimento em análise.

Os **Anexos** e **Processos** da tela de ***Edição do Atendimento***, são os mesmos que estão disponíveis para a **[Visão de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=732660488)**,
