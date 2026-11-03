---
content_hash: 02173614be41c13a024dc551af1d02c5cdf29ec59a4962664f9f1c222469965f
fetched_at: '2026-06-29T00:11:39.090628+00:00'
page_id: '787864521'
product: rm
source: tdn-rm
title: Integração RM x Gerint
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787864521
version: 15
---

PainelVisão Geral / Parâmetros Gerais

## **01. VISÃO GERAL**

Este documento tem por objetivo reunir todas as informações relevantes sobre a Integração do TOTVS Gestão Hospitalar (RM Saúde) x Gerint (Gerenciamento de internações) disponível a partir da 12.1.2310

## **02. PARÂMETROS GERAIS**

**2.1. RMSAUDE**

           Para acessar a tela de parâmetros gerais:

           No RMSAUDE,  Ambiente > Parâmetros > Gestão Hospitalar

         

          **2.2. Parâmetros**

Para utilizar integração com sistema Gerint é necessário preencher os dados e habilitar "Utiliza integração com sistema GERINT":

          Em Integração > GERINT

         

Permissão por perfil

## **03. PERMISSÃO POR PERFIL**

**3.1.** **Solicitações Gerint**

Para acessar a tela de solicitações com a gerint é necessário alterar a permissão por perfil:  
Serviços Globais > Segurança > Perfis  
  

Permitir o acesso em:  
Perfil > Acesso a Menus > Hospitais e Clinicas> Atendimento > Internação > Outros > Solicitações Gerint

Solicitações GERINT

## **03. SOLICITAÇÕES GERINT**

Exibe todas as solicitações de internação com a GERINT para melhor controle e visualização dos status, números Cerih, CNES da unidade enviada e nome da Unidade enviada a fim de obter o melhor controle do que foi solicitado junto a GERINT.

Acesse em:  
Atendimento > Internações > Outros > Solicitações Gerint

Essa tela conta hoje somente com a visualização e opções de atualizar a fim de buscar dados atualizados com a GERINT

Cadastro Leito

## **04. CADASTRO LEITO**

**4.1. Tipo de leito**

**Informar tipo de leito para quando o leito é SUS no cadastro ou edição:**

Cadastro > Leitos

       

        Identificação - Informações SUS - Código Tipo Leito

       

      Selecionar o tipo de leito

                

Solicitação Serviço de Internação 

## **05. SOLICITAÇÃO SERVIÇO DE INTERNAÇÃO**

**Para realizar uma solicitação de internação é necessário realizar algumas configurações previas.**

**5.1. Informar o tipo de leito de internação**

**Cadastro > Leitos > Selecione o leito**Preencha a informação "Código tipo leito internação"

**5.2 Cadastro de procedência conforme Gerint  
Cadastros > Registro e Controle > Outros Cadastros > Procedências**Esse cadastro somente será usado caso a internação seja URGENCIA

Deve ser cadastrado os dados de procedência conforme valores da GERINT 

**Tabela de referências conforme orientações GERINT**

|  |  |  |
| --- | --- | --- |
| Código | Valor | Descrição |
|  |  |  |
| 999 | ambulatorioProprio | Ambulatório da própria instituição |
| 1000 | outraInstituicao | Encaminhado de outra instituição |
| 1001 | espontaneo | Espontâneo |
| 1002 | internacaoposproced | Internação pós-procedimento regulado |
| 1003 | samuEstado | SAMU Estadual |
| 1004 | samuPoa | SAMU Porto Alegre |

**Coluna Código segue referente ao cadastro do RM**  
**Coluna Valor segue referente ao cadastro do GERINT**  
**Coluna Descrição opcional de acordo com usuário**

**Ao clicar em "+" para adicionar uma nova procedência, será exibido a tela de cadastro e deve ser cadastrado obrigatoriamente o CÓDIGO conforme descrito na tabela acima para chave e localização do valor junto a integração GERINT  
Obs. Campo descrição não precisa ser correspondente a coluna DESCRIÇÃO, esse valor será a critério do usuário.**

**5.3. Obrigatório informar o CPF do médico solicitante no cadastro de prestadores**

**5.3 Registrando Atendimento e solicitando o serviço de** **internação**

**Registe o atendimento com as informações abaixo preenchidas**  
**Cartão SUS paciente**Endereço paciente  
Data nascimento  
**Tipo Paciente Interno**  
**Convenio SUS  
Medico solicitante cujo o CPF seja cadastrado em Prestadores  
Leito configurado conforme no item 5.1**

**Depois de clicar em Salvar será habilitado as abas "Elaboração AIH" e "Sinais e Justificativa"**

**Elaboração AIH**  
  
**Obrigatório o preenchimento do Procedimento Principal.**

**Se o atendimento for ELETIVO deve ser preenchido o código GERCON realizado no SISTEMA GERCON.**

**Se o atendimento for URGÊNCIA deve ser preenchido os campos sinais vitais em classificação de risco.**

**Sinais e Sintomas**  
  
**Preenchimento obrigatório tanto para justificativa quanto para sinais e sintomas.**

**A solicitação do serviço de internação será realizado após o correto preenchimento dos dados acima citados e o clique no botão "OK"**

**Caso exista alguma inconformidade nos dados preenchidos, o RM irá exibir uma mensagem informando qual inconformidade e fechará a tela de registro de atendimento.**  
**Caso não exista nenhuma** **inconformidade,** **a tela de registo de atendimento irá fechar automaticamente sem nenhum erro.  
  
Para validar a solicitação pode seguir os passos do item 03 e validar o CERIH retornado com o número do CERIH dentro de Elaborações AIH**

Serviço de Internação / Cadastro de integração relacionamento de espercialidade RM X ESPECIALIDADE GERINT

## **06. SERVIÇO DE INTERNAÇÃO**

**6.1 Para integrar o serviço de internação Gerint**

Será feito a integração de internação ao concluir o item 05 Solicitação de internação seguindo todos seus requisitos,

após clicar no botão ok conforme item 5.3 e desde que o tipo do leito selecionando seja SUS.

## **07. CADASTRO DE INTEGRAÇÃO RELACIONAMENTO DE ESPECIALIDADE RM X ESPECIALIDADE GERINT**

**7.1 Para realizar os cadastros de integração relacionamento.**

Entrar em Utilitários → Integração Relacionamento.

Abrira o grid dos relacionamentos cadastrados, então clicar no símbolo + para um novo cadastro.

Preencher todos os campos do relacionamento conforme imagem abaixo, identificador RM e identificador sistema Gerint conforme planilha de especialidades.

Obs: Obrigatório realizar o relacionamento de todas as especialidades que já são utilizadas no RM, caso o selecione alguma

especialidade que não tenha feito o relacionamento, a integração de solicitação de internação não será realizada.

Evolução do Paciente

## **08. EVOLUÇÃO DO PACIENTE**

**Configurações para execução do processo.**

**8.1. Dependência de menus PEP RM**     Acesso: Serviços Globais > Segurança > Perfis > Anexo > Parâmetros RM Saúde > Dependência de menus PEP RM

Cadastre bloqueio diário para Evolução com dependência de Anamnese.

Ao confirmar a configuração acima e ao acessar a aba evoluções em prontuários do PEP RM será exibido a mensagem abaixo.

**8.2. Cadastro Itens de Lançamento**  
**Cadastro obrigatório para paciente internados em leitos registrados como Enfermaria ou UTI**

Cadastre um novo item conforme a imagem abaixo, com a descrição livre porém o **tipo item** como "Ventilações"

Configurar integração relacionamento em Utilitários > Integração Relacionamento  
Conforme as orientações abaixo.  
  
Identificador RM : **Código da ventilação cadastrada acima**  
Identificador Sistema: **Código referente a GERINT da coluna Valor (vide quadro abaixo)**  
Descrição: Opcional  
Tipo de Integração: **Ventilação**Sistema Integrador: **Gerint**

**Quadro de referência**

| Valor | Descrição |
| --- | --- |
| AR\_AMBIENTE | Ar Ambiente |
| OCULOS\_OU\_CATETER\_NASAL | Óculos ou cateter nasal |
| CAMPANULA | Campânula |
| MASCARA\_VENTURINI\_OU\_HUDSON | Máscara Venturini ou Hudson |
| VENTILACAO\_MECANICA | Ventilação Mecânica |
| CPAP | CPAP |

**8.3. Cadastro parâmetros ventilatórios**  
**Obrigatório para cadastro de ventilação como VENTILACAO\_MECANICA conforme item 8.2**

**Realizar o cadastro conforme as informações abaixo**

**Descrição:**

**FIO2  
  SATO2  
  PEEP  
  
Realizar três cadastros conforme imagem abaixo**

**8.4. Envio evolução paciente a Gerint pelo PEP RM**

Preencher dados da anamnese conforme imagem abaixo

**Realiza a liberação da prescrição médica para pacientes internados em leito de Enfermaria ou UTI**  
Realizar configuração conforme imagem abaixo, seguindo os tipos de ventilações cadastradas no item 8.2

**Informar os valores dos parâmetros ventilatórios para ventilação cadastrada como VENTILACAO\_MECANICA no item 8.2**Realizar os cadastros conforme a imagem abaixo

Após a configuração dos itens anteriores seguir para Evolução em PEP RM, preencher as informações pertinentes e

clicar em finalizar para enviar a evolução do paciente a GERINT

Transferência do Leito de internação

## **09. TRANSFERÊNCIA DO LEITO DE INTERNAÇÃO**

Para a transferência de leito no RM e Gerint é necessário acessar o seguinte menu Atendimento → Outros → Mudança de Leito.

é necessário informar o motivo da transferência e o novo leito,  o novo leito deve estar desocupado no RM e no Gerint

Após informar os dados necessários, clique em avançar que a mudança de leito será efetivada.

Veja que os leitos foram alterados no Gerint

e no RM

Reversão de Internação

## **10. REVERSÃO DE INTERNAÇÃO**

Para realizar a reversão da internação é necessário ter o número CERIH válido e a internação não pode ter ocorrido a mais de 24 horas

Caso a internação tenha ocorrido a mais de 24 horas o campo Ocupa Leito ficara desabilitado para alteração.

No exemplo abaixo a internação ocorreu na data 12/10/2023 as 09:58 e no dia 13/10/2023  as 14:16 não consigo editar, pois já se passaram 24 horas da internação

Agora vamos ver um exemplo onde ocorreu a reversão da internação

O Quarto 82B esta ocupado aqui no RM Saúde e no Gerint, mais vai ocorrer uma reversão de internação

Assim que desmarcar o Ocupa Leito, sim, para não, o RM me pede para confirmar" Confirma a liberação do leito 82B e a Reversão da Internação? "

Caso confirme, será pedido para inserir uma justificativa que depois será apresentada, na Aba Dados Sus → Sintomas e Justificativas

Após inserir a justificativa a reversão e liberação do leito será efetiva e essa opção não tem como ser revertida

 o valor será apresentado no campo Justificativa da Reversão de Internação e não poderá ser alterada

Caso não tenha ocorrido a reversão esse campo não aparecera na tela
