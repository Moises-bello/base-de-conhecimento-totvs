---
content_hash: c564a5dc13f81f78d607e640d393b9bb2183ae8e5269cb11223ec5aea524d67a
fetched_at: '2026-06-29T00:11:38.004644+00:00'
page_id: '780787856'
product: rm
source: tdn-rm
title: TCGI - Visão de Atendimentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=780787856
version: 1
---

# **Cobrança| Visão de Atendimentos**

**PROCESSO DE CONFIGURAÇÃO DE ATENDIMENTO.**

Nesta visão o atendente irá visualizar os atendimentos que estão sobre sua responsabilidade. Os atendimentos são tarefas que seguem um determinado fluxo com várias etapas, com instruções sobre cada etapa, até sua conclusão.

As regras para criação/gerenciamento do atendimento seguirão os padrões que devem primeiro ser definidos no TOTVS Aprovações e Atendimento. Consulte a documentação abaixo para maiores detalhes da rotina de acordo:

* [Grupos de Atendimento](https://tdn.totvs.com/display/LRM/Grupos+de+Atendimentos)
* [Tipo de Atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=425459518)
* [Atendentes](https://tdn.totvs.com/display/LRM/Cadastro+de+Atendentes)
* [Grupo de Atendentes](https://tdn.totvs.com/display/LRM/Grupo+de+Atendentes) - É importante que neste cadastro a opção Tipo de Repasse fique como **Por um rodízio entre os atendentes do grupo**, com isso o sistema automaticamente faz a distribuição para todos os atendentes deste grupo.
* [Etapas](https://tdn.totvs.com/display/LRM/Etapas) - Sugerimos que seja utilizados 3 etapas(**Em Atendimento, Atendimento concluído e Atendimento cancelado**), caso exista necessidade podem ser criadas quantas etapas forem necessárias.
* [Fluxo de Etapas](https://tdn.totvs.com/display/LRM/Fluxo+de+Etapas)
* [Parâmetros - Apontamento](https://tdninterno.totvs.com/pages/releaseview.action?pageId=425458983) - TOTVS Aprovações e Atendimento>>Ambiente>>Parâmetros>>TOTVS Aprovações e Atendimento.
* Resultado do Contato -Locao para informar o resultado de cada contado com o cliente dentro de uma lista de resultados pré-definidos.

* [Gerar Ação de Cobrança Manual: É possível realizar o envio de SMS e E-mail para o atendimento.](https://tdn.totvs.com/display/public/LRM/SMS+Corporativo+Via+Mashup#ServidordeJob--429978606)
* [Avançar Etapa](https://tdn.totvs.com/pages/viewpage.action?pageId=425458944)
* [Repassar Atendimento](https://tdn.totvs.com/display/LRM/Repassar+Atendimento)
* [Repassar de Volta](https://tdn.totvs.com/display/LRM/Repassar+de+Volta)
* [Agendar Atendimento](https://tdn.totvs.com/display/LRM/Agendar+Atendimento)
* [Em Andamento](https://tdn.totvs.com/display/LRM/Em+Andamento)
* [Transferência de Atendimentos](https://tdn.totvs.com/pages/viewpage.action?pageId=425458563)
* [Imprimir Ocorrências](https://tdn.totvs.com/pages/viewpage.action?pageId=425918480)
* [TOTVS Aprovações e Atendimento - Link Geral caso deseja visualizar mais algumas configuração](https://tdn.totvs.com/pages/viewpage.action?pageId=198948845).

Ao editar um atendimento será feito a abertura da tela de cobrança, será possível visualizar todos os dados da cobrança que está vinculada ao atendimento e através do menu atendimento será possível atualizar o atendimento.

**Atendimento:**

* **Atendimento**:  
  ♦ **Dados do Cliente**: Será apresentado informações para contato do cliente em forma de hiperlink, que possibilita um rápido acesso ao cadastro do cliente.  
  ♦ **Dados da Cobrança**: Data de abertura da Cobrança e quantidade de dias em atraso do lançamento com maior vencimento.  
  ♦ **Dados do Contrato**: Apresenta informações básicas do contrato(Venda ou Aluguel), e com acesso rápido para o contrato de venda/aluguel ou empreendimento/imóvel através de hiperlink.  
  ♦ **Iniciar Atendimento**: Informações do atendimento.  
  ♦ **Agendar**: Realiza o agendamento do atendimento, para o correto funcionamento é importante verificar o Link a seguir [Despertar Atendimento](https://tdn.totvs.com/display/LRM/Despertar+Atendimento).  
  ♦ **Iniciar/Concluir** **Apontamento**: Irá iniciar e finalizar o apontamento no atendimento. Caso a opção **Gerar apontamento automático para este atendente**esteja habilitado no cadastro do atendente não será possível inserir uma Descrição sem iniciar o apontamento. Com a opção desmarcada o apontamento não é obrigatório para inserir uma descrição.  
  ♦ **Histórico da Descrição**: Apresenta todo o Histórico de descrição do atendimento.  
  **♦ Descrição**: Ao preencher a descrição desejada a opção de 'Salvar' ficara habilitada.
* **Apontamento**: Será apresentado os apontamentos realizados no atendimento.
* **Arquivos anexos ao atendimento**: Exibe os arquivos anexos ao atendimento, na própria visão é possível realizar a inclusão de novos arquivos.
* **Histórico de Status**: Demonstra o histórico dos status que o atendimento foi percorrendo.

Importante:

Caso todos os lançamentos da cobrança sejam quitados ou renegociados o processo de Gerar Cobrança irá finalizar o atendimento.

**Exemplo de uso do tipo de  Atendimento.**

Criada uma Ação de cobrança de : Abertura de Atendimento - neste exemplo será usado para Carteira de Cobrança acima de 60 dias, como no nosso exemplo tempos carteira Junior menor ou igual 60 e Senior acima de 60 dias , tem que se criar para ambas carteiras. **Neste exemplo será criado um para Acima dos 60 dias**.

**Se tiver 5 carteiras, tem que ter 5 tipos de antendimentos.**

**Grupo de atendimento :** Sempre pode ser o mesmo para todos atendimentos , neste exemplo ( Cobrança )

**Tipo de Atendimento :** Utilizado separado , no exemplo um para Acima de 60 dias e outro para menor ou igual 60 dias.

**Parametros do TAA no TCGI**

Apontamento automático , caso queira que o atendente gere apontamento de horas durante o atendimento , ai se define neste parametro a atividade.

# **Cadastros.**

## **GRUPOS ATENDIMENTO**

Cadastro Simples

## 

## **TIPOS ATENDIMENTOS**

Editar o tipo de atendimento desejado.

**Primeiro cadastro**: do Tipo de Atendimento: ETAPA

Criando etapas do tipo de atentimnto - Inciando até finalizar

Neste exemplo , cadastrada primeira etapa - Em cobrança ( Ordem 1 ) e será repassado no caso para um determinado Grupo de atendentes

Segunda Etapa : Neste exemplo , criada uma ( Concluir cobrança ) - Ordem 2 - e Tipo de repasse de etapa , neste caso é : Manter com atendente atual , não alterar o atendente que deu abertura.

E uma ação para este caso é : Concluído confirmado.

Terceira Etapa : Neste exemplo , criando uma nova etapa que é ( Cancelar cobrança ) Ordem 3 - Tipo de Repasse de etapa , Manter o atendente atual e em Ação a ser realizada nesta etapa : Cancelar Atendimento.

**Segundo cadastro**: do Tipo de Atendimento: Fluxo das Etapas

Exemplo , Etapa 1 avançando para Etapa 2.  Etapa 1 para Etapa 3 . ( Tipo que um fluxograma ).

Cadastrando Primeiro Fluxo , Informo a Etapa Origem e Destino.

Sobre o **Motivo de Repasse** :

Tipo de Motivo : Tem sempre que ser (  **FLUXO DE TAREFAS**  )

Segundo Fluxo de Etapa cadastrada , que é da Etapa em Cobrança para Cancelar etapa e lembrando que foi feito o cadastro do Motivo de Repasse Excluir e do Tipo de Motivo ( Fluxo de Tarefas ).

Visualizar os Fluxos de uma outra forma : Anexo : Fluxo Visual

Mostrando que de : Em cobrança pode concluir ou Cancelar.

## 

## **PESSOAS**

Cadastro de Pessoa.

Obrigatório cadastro de usuário para que possa efetuar o login no processo.

Cadastro da Pessoa Chefe que irá receber as notificações.

Cadastros realizados de Pessoas.

## 

## **ATENDENTES**

No cadastro do Atendente é informada a pessoa cadastrada acima.

Buscar pela Pessoa e inciar o cadastro do Atendente.

Exemplo acima , o Atendente : Astoni Teste Cobrança tem Chefe e dentro da Hierarquia é informado o nome do Chefe como mostra o print abaixo.

Neste campo : Código de Atendente chefe é feito o vínculo do Chefe com o atendente.

Outro parâmetro importante no cadastro de Atendente é ( Autoriza repasse para qualquer atendente ) Esse é marcado para Chefe e podendo até mesmo ser marcado para Não chefe em caso de Férias do Chefe , mas isso vai de parametrização e desejo do Cliente , esse Atendente que ficará responsável é informado abaixo do Parâmetro.

Neste exemplo de Repasse: O Chefe Astoni Teste Cobrança em férias colocou o Sub Chefe Teste Cobrança como Responsável em seu lugar.

**Mais sobre Atendentes** : [Clique Aqui.](https://tdn.engpro.totvs.com.br/display/public/LRM/Cadastro+de+Atendentes)

## 

## **GRUPOS ATENDENTES**

Cadastro d Grupo de Atendentes tem que seguir o mesmo fluxo da Carteira - Neste caso é feito um Grupo para lançamentos em Atraço com Mais de 60 Dias e no caso deverá cadastrar um outro Grupo para os abaixo de 60 Dias em atraso.

Ao ter mais de um atendente no Grupo é feito um rodízio entre atendentes , neste exemplo foi selecionada esta opção.

Atendente inserido no novo grupo.. Lembrando que ai informando apenas o Atendente ( Astoni Teste Cobrança ) não os chefes , pois se informar os chefes ai , eles iriam receber atendimento também.

Tipo de Atendimento após cadastro do Grupo Atendente.

Após o cadastro do Grupo de Atendente com seu Atendente , voltar ao cadastro do Tipo de Atendimento , Anexo ( Etapas ) Selecionar a etapa e informar o Grupo cadastrado.

No exemplo das outras etapas , manter etapa com atendente atual ( Apenas exemplo. )

**Mais sobre Grupo Atendentes**: C[lique Aqui.](https://tdn.engpro.totvs.com.br/display/public/LRM/Grupo+de+Atendentes)

## **MOTIVOS ATIVIDADE / INATIVIDADE**

No **Ativo** = Marcar o parâmetro (**Aparece como ativo no posto de Trabalho** )

Caso de **Inativo** = Não marcar esse parâmetro.

**Mais sobre o cadastro de Motivos de Atividade / Inatividade :** [Clique Aqui.](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=425458422)

## **PERÍODO DE TRABALHO  &  POSTO DE TRABALHO**

Sobre Período de Trabalho : [Clique aqui.](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=425458429)

Sobre Postos de trabalho : [Clique aqui.](https://tdn.engpro.totvs.com.br/display/public/LRM/Posto+de+Trabalho)

## **ALTERAR STATUS ATENDENTE**

Em caso de Inativo: Informar o substituto neste local e em caso de Ativo , não é mostrado o campo de Subsitutuo.

Neste exemplo , Astoni Teste Cobrança encontra-se ( Ativo ).

## **RESULTADOS DO CONTATO**

Resultado do contato serve para conferência , são cadastros livres que serão visualizados no atendimento e ao gerar um relatório será mostrado por exemplo , quantas vezes o atendente tentou entrar em contato e o cliente atendeu , ou não atendeu e ai gerar indicadores.

Gerando Cobrança com Opção de Tipo de Atendimento

## **Gerando Cobrança com ação de ( TIPO DE ATENDIMENTO ).**

Carteira de Cobrança : Retirada a Régua ( Ficando a opção de Manual para se gerar a Cobrança )

Neste exemplo a ação será Manual.

Visão de Cobrança | Processos | Gerar Ação Manual de Cobrança

Selecionando a Ação cadastrada para Atendimento acima de 60 dias, Tomar muito cuidado com o Cód Carteira , bom filtrar por carteira para gerar  ação incorreta de uma carteira X para outra Y.

Ao executar o processo , é aberto o Atendimento.

## 

## **Após a geração do Tipo de Atendimento , quem passa a assumir no caso é o Usuario do atendimento , onde isso é feito ?**

Cobrança | Visão de Atendimento

Selecionar o  que foi aberto o atendimento, no Atendimento tem os principais campos, no exemplo acima mostra o código da cobrança e ai vem outros importantes como, Carteira , Dias em Atraso, Nome do Cliente , Status do atendimento , entre outros campos importantes para conferência.

**DICA :**

Importante criar um filtro com status em Andamento para nao ficar muito poluida a tela do usuário com tempo.

Neste momento o atendente pegou trabalho e passa a atuar no processo de Cobrança.

Atendimento passa a aparecer na tela de Visão de Cobrança.

Para o atendente ficar por dentro de tudo que aconteceu com esse processo de cobrança , basta entrar em Histórico de cobrança.

Um exemplo de contato com Cliente:

Atendente entrou em contato com Cliente e ele não atendeu, ai basta clicar em Atendimento e inserir o Resultado de contato e Descrição do ocorrido. ( Salvar em seguida ).

Exemplo , **cliente atendeu a ligação e pediu para retornar ligação dia X e hora Y** .. ai no caso o atendente informa o dia e hora que será despertado o atendimento e retornar a ligação.

Status fica em Agendamento o Atendimento.

Historico mostrando que o Cliente Atendeu a Ligação.

**Mais sobre o processo de DESPERTAR ATENDIMENTO** : [Clique Aqui.](https://tdn.engpro.totvs.com.br/display/public/LRM/Despertar+Atendimento)

Status volta para : **Em Andamento** quando chega a data agendada com Cliente.

Concluindo o Atendimento.

**Concluindo o Atendimento!**

Cliente pagou todas parcelas em atraso e como será realizada a conclusão do Atendimento?

Atendente abre o atendimento , seleciona todas parcelas em Atraso e baixa.

Parcelas não ficam mais no Atendimento.

Entrar em Visão de Cobrança - Selecionar a cobrança que gerou o Atendimento e executar o processo ( Gerar Cobrança ).

Atendimento passando a ficar com status : **Concluído Confirmado.**

Histórico passa a mostrar: ( Solução e motivo dela ).

Na parte superior do Atendimento mostra o dia e inicio do Atendimento , quantos agendamentos foram realizados no atendimento e quando foi finalizado.
