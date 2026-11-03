---
content_hash: a68dc5b7229eb6acf8adc9680461553793af178d7972277887a28089ae3f363d
fetched_at: '2026-06-29T00:06:30.242287+00:00'
page_id: '235317278'
product: rm
source: tdn-rm
title: ER_PCREQ-9418_Integracao_de_Calendarios_e_Turnos_com_NG_para_o_Mobilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-9418_Integracao_de_Calendarios_e_Turnos_com_NG_para_o_Mobilidade
version: 116
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Projetos |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | R\_C&P\_TOP010 | **IRM1** | PCREQ-3154 |
| **Requisito1** | PCREQ-9418 | **Subtarefa1** | PDR\_CP\_TOP010-69 |
| **Chamado2** | Não se aplica | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *Pré-Requisitos para melhor entendimento da especificação:*     | Módulo | Link | | --- | --- | | Mobilidade | <http://tdn.totvs.com/display/public/integracoes/TOTVS+TOP+MOBILE> | |  |  | | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

Este documento tem como objetivo demonstrar a melhoria no apontamento de equipamento, fazendo com que a informação do turno do equipamento seja levada para o Manutenção de ativos (Protheus). Os detalhes deste procedimento serão descritos nos próximos tópicos.

## Definição da Regra de Negócio

**Modelo Atual**

No modelo atual para o usuário realizar um apontamento de equipamento é necessário seguir os seguintes passos: 

1º.     Usuário acessa o coletor e informa o código do equipamento o horário de início e de fim do equipamento.

2º.     O apontamento registrado no coletor vai para o TOP (Totvs Obras e Projetos), o sistema valida os dados do apontamento e reenvia o apontamento para o Protheus.

3º.     O apontamento enviado no TOP chega no Protheus. Caso os dados estejam corretos o apontamento e registrado na parte diária, caso o apontamento tenha algum problema (horímetro menor, data registrada conflitante, turno errado, etc.), o apontamento e registrado no acerto de consistência.

No modelo atual, para não haver problemas com turno do equipamento, o usuário cadastra um calendário para o equipamento com turno de 24h, não sendo necessário o acerto de consistência. Este modelo é bem utilizado para equipamentos terceirizados, mas provoca alguns problemas quando é utilizado em equipamentos próprios, pois equipamentos próprios possuem controle de turno e fazem parte de relatórios gerenciais.

**Implementação do turno no apontamento de equipamento**

Nesta proposta de desenvolvimento entendemos que para o processo de envio do turno do equipamento ser automatizado, será necessário que no recebimento do apontamento do equipamento no Totvs Obras e Projetos, o sistema analise o intervalo do horário do apontamento e selecione o turno automaticamente.

                Para a seleção do turno automática pelo intervalo do apontamento, torna-se necessário o envio do calendário de turno cadastrado no Manutenção de ativos para o Totvs Obras e Projetos. Este envio de dados do calendário será feito pelo WebService do Protheus e será informado o caminho nos parâmetros Gerais aba integração dentro do Totvs Obras e Projetos. Com o WebService cadastrado o usuário poderá executar o processo de sincronismo de calendário do equipamento, assim como no envio do apontamento o sistema irá verificar a data de atualização do calendário e de forma automática consultar o webservice e recuperar o turno atual.

                Com o calendário sincronizado entre Manutenção de Ativos e Totvs Obras e Projetos, o sistema irá conseguir identificar através do intervalo do apontamento, qual o turno do equipamento e consequentemente enviar esta informação na mensagem do apontamento para Manutenção de Ativos. Para o melhor entendimento da análise do sistema, segue alguns exemplos da regra que será utilizada pelo Totvs Obras e Projetos:

**Cenário 1:** Apontamentodo coletor no intervalo de 1 turno.

No cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento do equipamento com turno 01

**Cenário 2:**Apontamentodo coletor no intervalo de 2 turnos.

 

No  cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento do equipamento com turno 01. Apesar do intervalo conflitar entre o apontamento, o sistema irá informar o turno que iniciou o apontamento. 

 **Cenário 3:** Apontamento do coletor no intervalo ultrapassado pela hora fim.

 

No cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento do equipamento com turno 01. Apesar do intervalo de hora fim ultrapassar o horário do turno o Totvs Obras e Projetos irá informar o turno que iniciou o apontamento.

 

**Cenário 4:** Apontamentodo coletor inciando fora do intervalo de turnos.

No cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento do equipamento com turno 02. Apesar do intervalo de hora inicio não esta contemplando a hora inicio de nenhum calendário, a hora fim do apontamento esta contido no intervalo do calendário 02.

**Cenário 5:** Apontamentodo coletor sem intervalo de turnos.

No cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento sem turno. Provavelmente este apontamento poderá cair em acerto da parte diária no Manutenção de Ativos ou na Parte Diária caso exista um turno de 24 horas cadastrado de forma padronizada.

**Cenário 6:** Apontamentodo coletor sem calendário de turnos sincronizado.

No cenário informado acima o Totvs Obras e Projetos irá enviar o apontamento sem turno. Provavelmente este apontamento poderá cair em acerto da parte diária no Manutenção de Ativos ou na Parte Diária caso exista um turno de 24 horas cadastrado de forma padronizada.

***Fluxograma do processo de sincronismo***

Para melhor entendimento de como será o procedimento de sincronismo, iremos demonstrar como será o fluxo do processo de sincronismo e cadastro do calendário de turno do equipamento:

O processo de sincronismo poderá ocorrer de duas maneiras a primeira de forma manual e a segunda de forma automática. A forma manual o usuário terá que selecionar o processo de importar calendário de turnos vide protótipo 02, dentro da visão de associação de calendários a Obra, e solicitar a execução, o Totvs obras e projetos irá realizar a chamada do serviço da manutenção de ativos e atualizará os calendários com os turnos. O processo automático será durante o envio do apontamento para a Manutenção de Ativos, onde o sistema no momento do envio irá verificar se a data de atualização do calendário é inferior a 1 dia, em caso positivo o sistema atualizará os calendários e turnos, em caso negativo o sistema utilizará o calendário atual, sendo assim, será realizado apenas uma única chamada diária ao webservice de Manutenção.

É importante lembrar que o calendário de turnos será cadastrado por obra, sendo assim cada obra poderá ter turnos diferentes. O calendário sincronizado não será por equipamento e sim para todos os equipamentos da filial.

Exemplo do XML de envio para NG:

<?xml version="1.0" encoding="UTF-8"?>  
 <Root>  
     < ListaCalendario >  
         <Calendario>

            <Empresa>01</Empresa>  
             <Filial>01</Filial>

            <Codigo>001</Codigo>

        </ Calendario >

        <Calendario>

            <Empresa>01</Empresa>  
             <Filial>01</Filial>

            <Codigo>002</Codigo>

        </ Calendario >

    </ ListaCalendario >  
 </Root>

Exemplo do XML de retorno da NG:

<?xml version="1.0" encoding="UTF-8"?>  
 <Root>  
     <ListaCalendario>  
         <Calendario>

            <Empresa>01</Empresa>  
             <Filial>01</Filial>

            <Codigo> 001</Codigo>

            <ListaPeriodo>

                <Periodo>

                    <DiaSemana> Segunda</DiaSemana>

                    <Inicio>08:00</Inicio>

                    <Fim>12:00</Fim>

                </Periodo>

                <Periodo>

                    <DiaSemana> Segunda</DiaSemana>

                    <Inicio>13:30</Inicio>

                    <Fim>18:00</Fim>

                </Periodo>

                <Periodo>

                    <DiaSemana> Terca</DiaSemana>

                    <Inicio>08:00</Inicio>

                    <Fim>18:00</Fim>

                </Periodo>

            </ListaPeriodo>

        </Calendario>

        <Calendario>

            <Empresa>01</Empresa>  
             <Filial>01</Filial>

            <Codigo> 002</Codigo>

            <ListaPeriodo>

                <Periodo>

                    <DiaSemana> Segunda</DiaSemana>

                    <Inicio>08:00</Inicio>

                    <Fim>18:00</Fim>

                </Periodo>

            </ListaPeriodo>

        </Calendario>

    </ListaCalendario>  
 </Root>

**Observação:** No Protheus é possível cadastrar diversos períodos para um calendário, de forma a desconsiderar, por exemplo, o horário de almoço em um calendário comercial. Assim, quando houverem diferentes intervalos, o WebService, por ser genérico, irá enviar os intervalos.

 Na mensagem de requisição podem ser enviados vários itens para consulta em uma única mensage. Cada item é separado pela tag <Calendario>, sendo as tags <Empresa> e <Filial> obrigatórias. Ao enviar <Empresa> + <Filial> + <Codigo> a pesquisa é feita pontualmente. Caso se informe apenas <Empresa> + <Filial>, a rotina deve retornar todos os calendários da filial.

Na mensagem de retorno, cada calendário é separado pela tag <Calendario> e cada período válido é informado dentro da tag <Periodo> composta pelas tags <DiaSemana> e <Inicio> e <Fim> representando as horas do período. Pode haver mais de um período no dia da semana, e nem todos os dias são obrigatórios – se um dia não tiver períodos válidos, não será enviado.

***Associação do turno a obra***

Para a correta analise e seleção automática do turno para o apontamento de equipamento no Totvs Obras e Projetos, será necessário a associação do turno a obra. Para esta seleção o Totvs Obras e Projetos não permitirá a associação de turnos conflitantes em seus horários, sendo assim, ao se associar um turno a obra não será possível associar um novo turno que o horário gera um conflito com o turno já associado, e para garantir essa integridade será criada uma mensagem de aviso ao usuário da inconsistência ocorrida:

**Não será possível associar este calendário nesta obra, pois existe turnos conflitantes com períodos no mesmo intervalo de tempo.**

Para  a associação do turno a obra, é necessário que o usuário cadastre na obra os turnos que farão parte dos apontamentos dos equipamentos. Esta associação estará disponível no menu Delphi (Cadastro => Mobilidade => Equipamento => Associação do calendário de turno) ou na Nova MDI (aba Controle =>Mobilidade => Equipamento => Associação do calendário de turno). Será possível realizar a associação do turno a obra através do processo de “Incluir turnos a Obra”:

Neste processo será possível selecionar os turnos que foram sincronizados pelo processo de sincronismo e que farão parte da obra.

***Envio de apontamento para o Manutenção de Ativos***

O processo de envio do apontamento do equipamento será alterado para buscar o turno do apontamento automaticamente de acordo com o intervalo do apontamento. Será necessário alterar este processo para realizar o sincronismo com o Manutenção de Ativos caso os calendários estejam desatualizados em 1 dia.

Será necessária alteração na mensagem APPOINTMENT, acrescentando mais um campo onde será informado o turno do apontamento.

A informação do turno não será pré-requisito para o envio do apontamento para o Manutenção de Ativos, sendo assim, o apontamento poderá ser enviado normalmente mesmo com a informação do turno em branco.

## Protótipo de Tela

 

### **Protótipo 01 - Tela de parametrização do WebService**

### **Protótipo 02 - Processo de associação e  importação dos calendáriodo do WebService**

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
