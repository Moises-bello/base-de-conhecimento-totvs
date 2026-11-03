---
content_hash: beb78bcec292f3b76aab4ed2dfa7b4bd6362987d95fe9372bb079d18287ff984
fetched_at: '2026-06-29T00:11:33.345886+00:00'
page_id: '756458907'
product: rm
source: tdn-rm
title: Análise de Antimicrobianos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=756458907
version: 23
---

AnaliseAntimicrobianaVisaoGeralVisão Geral

## **01. VISÃO GERAL**

A tela pode ser acessada através do Menu > Apoio Gerencial> Análise > Análise de Antimicrobianos

Ao acessar a tela de análise de antimicrobianos, será exibida a tela com todas as prescrições liberadas que possuem antibiótico.

Campos da grid:

**Nome** → Nome do paciente da prescrição.

**Sítio de infecção** → Corresponde aos sítios que foram vinculados com o antibiótico.

**ATB prévio? →** Se há situação de antibiótico previamente administrado na mesma internação

**Dt. prescrição** → Data em que foi realizada a prescrição.

**Status** → Corresponde ao status da análise da prescrição, status possíveis:

      

**Intervenção** → Indica se na análise foi indicado que deve ter uma intervenção.

**Avaliado em**→ Ultima data em que a prescrição foi avaliada.

**Próx. avaliação**→ Caso algum item seja necessário uma próxima avaliação, deve exibir a próxima data que foi definida pelo avaliador.

**Prescritor(a)** → Médico que realizou a prescrição.

**Prescrição** → Código da prescrição.

**Prontuário** → Número do prontuário do paciente.

**Dt. internação** → Data em que o paciente foi internado.

**Tempo internação** → Tempo que o paciente está internado.

**Unidade de atendimento** → Unidade de atendimento onde o paciente está internado.

## **CONTROLE DE ACESSO**

**Quando um usuário abrir a análise de uma prescrição, a prescrição fica em status em análise e não pode ser analisada por outro usuário.**

Existe um processo para liberar o acesso da prescrição do estado de em análise.

ConfiguracaoPEPRMConfiguração para utilização da análise antimicrobiana no PEP RM

## **02. Configuração para utilização da análise antimicrobiana no PEP RM**

A configuração para utilização da análise antimicrobiana deverá ser realizada por Unidade de Atendimento.

Para isso, o usuário deve acessar: Menu > Cadastro > Uso Geral > Unidade de atendimento:

Na tela de unidade de atendimento, acessar a aba PEP RM > Prescrição médica

Caso o usuário deixe marcado a opção acima, todas as prescrições que forem criadas pelo médico e possuam antibiótico, nessa unidade de atendimento, serão enviadas para a análise do CIH. 

Para que um antibiótico prescrito no PEP seja enviado para o CIH é importante fazer as seguintes configurações  , marcar o mesmo como antimicrobiano 

e informar o código identificador do produto 

e no cadastro do Antibiótico é necessário informar no campo código externo o valor do identificador 

Pronto agora é so ir ao Prontuário Eletrônico e fazer a prescrição do Antibiótico. 

MotivoAnaliseAnálise de Prescrição de Antimicrobianos

## **03. Análise de Prescrição de Antimicrobianos**

Ao clicar duas vezes ou o botão de editar a seguinte tela é exibida:

TelaDeAnaliseTelaDeAnaliseCabecalhoCabeçalho

## **03.01. Cabeçalho da****Análise de Prescrição de Antimicrobianos**

O cabeçalho da tela apresenta informações sobre a internação que a prescrição foi feita.  
  
  
**Nome** → Nome do paciente da prescrição.  
**Sexo** → Sexo do paciente da prescrição.  
**Idade** → Idade do paciente da prescrição.  
**Prontuário** → Número do prontuário do paciente da prescrição.  
**Leito** → Leito em que o paciente encontra-se internado.  
**Unidade de atendimento** → Unidade de atendimento em que o paciente encontra-se internado.  
**Número da prescrição** → Apresenta o número da prescrição no sistema e o status da mesma.  
**Situação** → A situação em que o paciente se encontra (Internado, Alta ou Óbito)  
**Data Entrada** → Data em que o paciente deu entrada na Internação  
**Data Saída** → Data em que o paciente deu saída da Internação  
**Tempo de Internação** → Tempo em dias em que o paciente se encontra internado.  
**Clínica / Especialidade** → Especialidade do Prescritor  
**Prescritor** → Médico responsável pela prescrição

GridTabela de Antibióticos

## **03.02. Tabela de antibióticos da** **Análise de Prescrição de Antimicrobianos**

Na parte inferior esquerda da tela temos a seguinte tabela, que apresenta os antibióticos e suas informações:

**Colunas da tabela:**

**X →**Coluna de seleção das linhas da tabela **Descrição do item →**O Nome ou descrição do antibiótico a ser prescrito. **Sítios de Infecção →** Corresponde aos sítios que foram vinculados ao antibiótico.  
**Status** **→** Status da análise do antibiótico como nas imagens abaixo:

**Indicação de tratamento →** Seprofilático ou terapêutico **Parâmetros →** Indica o status da análise prévia realizada pelo módulo. **Administrado →** Indica se o antibiótico já foi administrado.  
**Data Início →**Data de início do tratamento do antibiótico.  
**Data Fim →**Data do final do tratamento do antibiótico.  
**Indicação do item **→**** Número de dias indicado para a utilização do antibiótico no tratamento.  
**Frequência de uso do item** **→** Indica a frequência de uso do antibiótico.  
  
Na parte inferior da tabela há a contagem do total de itens da prescrição, junto com um botão de desfazer.  
**O botão de desfazer** pode ser utilizado para desfazer alterações em linhas marcadas na coluna **X** ou para todas as linhas, enquanto não for marcada nenhuma linha.  
**O PROCESSO DE DESFAZER SÓ PODE SER EXECUTADO ANTES DA FINALIZAÇÃO DA ANÁLISE, APÓS FINALIZAÇÃO DA ANÁLISE TODAS AS ALTERAÇÕES IRÃO SER EFETIVADAS!** 

DetalhesDetalhes do antibiótico

## **03.03. Detalhes de antibióticos da** **Análise de Prescrição de Antimicrobianos**

Na parte inferior direita da tela, temos as informações ou detalhes dos antibióticos da prescrição:

Aqui é onde as operações de análise são realizadas.  
Primeiramente temos o nome do antibiótico, onde caso seja selecionado mais de um a aparecerá o número de antibióticos selecionados como na segunda imagem.  
  
**Dose →** Quantidade da dose prescrita do antibiótico  
**U.M. →** Unidade de medida da prescrição do antibiótico  
**Via →**Via de administração do antibiótico  
**ACM →** Indica se o antibiótico é A critério Médico  
**S/N →** Indica se o antibiótico é indicado Se Necessário  
**Horários →** Horários indicados para o tratamento com o antibiótico

## **Ações**

Asações são operações que devem ser utilizadas na avaliação da prescrição:

OperacoesAnaliseDetalhesReavaliarReavaliar

## **03.03.01 Ação de Reavaliar**

A ação de reavaliar deve ser usada em casos onde o antibiótico deve ser reavaliado posteriormente.

Ao clicar em reavaliar os campos abaixo dos botões serão liberados conforme a imagem:

Nessa ação será liberada todos os campos obrigatórios abaixo para preenchimento: **Análise CIH →** Motivo padronizado da análise do antibiótico **Observações ou Justificativa →**Campo onde pode ser informado informações adicionais e/ou Justificativa da análise. **Data reavaliação →** Campo onde deve ser informado a data para reavaliação do antibiótico.

DetalhesIntervencaoIntervenção

## **03.03.02 Ação de Intervenção**

A ação de intervenção deve ser usada em casos para interromper o uso do antibiótico.

Ao clicar em Intervenção os campos abaixo dos botões serão liberados conforme a imagem:

Há dois campos obrigatórios o preenchimento nessa ação: **Análise CIH →** Motivo padronizado da análise do antibiótico **Observações ou Justificativa →**Campo onde pode ser informado informações adicionais e/ou Justificativa da análise.

DetalhesLiberarLiberar

## **03.03.03 Ação de Liberar**

A ação de liberar deve ser usada em casos de liberação do antibiótico para uso.

Ao clicar em Liberar apenas o campo de Observações ou Justificativa será habilitado conforme a imagem:

Há apenas um campo obrigatórios para preenchimento nessa ação:  
**Observações ou Justificativa →**Campo onde pode ser inserido informações adicionais e/ou Justificativa da análise.

DetalhesFinalizarAnaliseFinalizar Análise

## **03.03.04** **Botão Finalizar análise**

**O botão de finalizar análise contido no final dos detalhes, efetiva todas as ações dos antibióticos, esse processo consiste as ações sem possibilidade de mudança.**

No final de cada ação há dois botões:  
**Limpar →** Retorna o(s) antibiótico(s) selecionado(s) ao estado de pendente caso a ação não esteja confirmada.  
**Confirmar →**Confirma a ação do(s) antibiótico(s) selecionado(s).  
  
E contem 2 informações, caso uma ação já tenha sido feita na prescrição do antibiótico selecionado:  
**Responsável análise →** Responsável pela análise realizada.  
**Data/horário análise** **→** Data e horário da análise realizada.

ProntuarioPEPRMAcesso ao prontuário PEP RM

## **03.04****Prontuário Eletrônico PEP RM**

Caso a unidade de atendimento utilize o PEPRM, ela terá acesso ao prontuário eletrônico através da tela de Análise de Antimicrobianos.

Caso não tenha acesso ao PEP RM, ao abrir a  tela de Análise de Antimicrobianos, no canto inferior esquerdo da tela não ira aparecer o botão de acesso ao prontuário

Caso ele tenha acesso ao prontuário eletrônico, ao abrir a tela o botão aparecera no canto esquerdo inferior da tela  

## 

 Tendo acesso ao mesmo já logado.

BotaoMaisInformacoesBotão mais informações

## **03.05****Botão Mais Informações**

Para acessar mais detalhes relacionados a prescrição do item, o usuário deverá clicar em "+ informações". 

O botão permite a seleção de apenas um item por vez. Caso sejam marcados no grid mais de um item o botão ficará desabilitado.

Serão exibidas as informações relativas à prescrição do item, como:

Via, apresentação, quantidade, frequência, data de início e duração do tratamento, justificativa da prescrição e se o item foi prescrito na condição de SN ou ACM.

Dentro do botão mais informações, tenho acesso detalhado dos parâmetros para cada antibiótico

Hoje temos 2 parâmetros o ok e o exclamação

Regras para o ok

* Se não houver cadastro de linhas de tratamento - **ok**
* Se antibiótico prescrito for 1ª linha de tratamento - **ok**

* Se antibiótico prescrito for 2ª linha de tratamento com 1ª linha de tratamento cadastrado - **Atenção (exclamação)**
* Se antibiótico prescrito não corresponder nem a 1ª nem a 2ª linha de tratamento cadastradas - **Atenção (exclamação)**
* Se antibiótico importado não for encontrado em nossa base de dados - **Atenção (exclamação)**

Dentro do RM eu consigo conferir o Antibióticos dentro da Aba Cadastros

Nesse exemplo a Ampicilina esta cadastrada como 1º

Para que um antibiótico, apareça para ser cadastrado como 1º ou 2º linha de tratamento

Deve ser marcar o campo Antibiograma, onde esta marcado com a seta.

## 

Já o campo Código Externo é importante na hora da importação do Antibiótico, se não for localizado na hora da importação  vamos mostrar a seguinte mensagem "Item não encontrado na importação. favor validar"

* Se antibiótico prescrito não corresponder nem a 1ª nem a 2ª linha de tratamento cadastradas - **Atenção (exclamação)**

Medicamento não pertence a 1º e nem a 2º linha de tratamento

É importante se atentar para a faixa etária

       De  0 a 28 Dias Neonato  
       de 29 dias a 24 meses Lactente  
       2 a 7 anos Criança  
       maior que 7 a 18 anos Adolescente  
       entre 18 a 65 anos adulto e maior que 65 Idoso.

MotivoAnaliseMotivo de Análise CIH

## **04. Motivos para Análise de Prescrição de Antimicrobianos**

Os motivos de Análise de prescrição pode ser aberto no caminho:

**Ao abrir a tela será exibida a tabela de Motivos cadastrados:**

As informações contidas na tabela são:  
**Código →** Código único do motivo de Análise CIH  
**Descrição →** Descrição do motivo de Análise CIH  
**Tipo →** Tipo de ação em que o motivo pode ser utilizado, sendo Reavaliar, Intervenção ou Ambos (Todos).

CadastroNovoMotivoCadastro de novo Motivo

## **04.01 Cadastro de motivos para Análise de Prescrição de Antimicrobianos**

Ao clicar Incluir apresentará a seguinte tela de cadastro:

As informações a serem preenchidas são:  
**Descrição →** Descrição do motivo de Análise CIH  
**Tipo →** Tipo de ação em que o motivo pode ser utilizado, sendo Reavaliar, Intervenção ou Ambos (Todos).

**Ativo →**Informa se o motivo está ativo ou não

FatoresAssociadosFatores associados a infecção

## **05. Fatores associados a infecção**

Para apoiar o médico infectologista na análise, o RM disponibiliza acesso as infecções associadas à internação do paciente, mesmas informações do cadastro do prontuário do paciente no Controle de IRAS, é um acesso rápido que pode ser acessado através do formulário de análise na aba + Fator associado a infecção. O usuário deve ter permissão ao processo.

AtualizacaoAutomaticaAtualização automática por tempo definidoDeve-se à atualização automática da tela por tempo determinado pelo usuário em minutos.

## **06. Atualização de prescrições automaticamente por tempo definido pelo usuário**

A tela de prescrições antimicrobianas possui uma atualização automática que pode ser habilitada**.**

Para habilitar essa atualização automática o usuário deve configurar o tempo de atualização (em minutos) no caminho abaixo:

Ambiente → Parâmetros → Controle de Infecção Hospitalar

Avançar até chegar nos processos onde será exibido os processos e selecionar Parâmetros por estação de trabalho.

Nessa tela você poderá configurar por nome da estação de trabalho ou usuário:

Ao criar ou modificar algum registro de estação de trabalho poderá ser observado que há uma aba de Configurações no final onde consta o campo para definição do tempo da atualização automática:

**Onde 0 é desativada, e qualquer valor maior que 0 ativa a atualização automática.**
