---
content_hash: 5eeb277afaf7003c79a6534be917929baa5eca80ac6580ebcdd1b5f2853df905
fetched_at: '2026-06-29T00:10:31.973068+00:00'
page_id: '525014173'
product: rm
source: tdn-rm
title: Painel de Eletivos PEP
type: documentation
url: https://tdn.totvs.com/display/LRM/Painel+de+Eletivos+PEP
version: 14
---

## 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**
4. **Prefixo unidade**
5. **Tipo de ordenação**

## **01. VISÃO GERAL**

A tela de Painel de Eletivos do PEP RM corresponde à aba "Atendimento Médico" do Painel de Atendimentos Eletivos do RM Saúde, cujo propósito é exibir a fila de pacientes eletivos a serem chamados pelo médico, segundo as configurações do RM Saúde.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de Painel de Eletivos o sistema carregará 5 pacientes ou quantos estiverem agendados para atendimento no dia.

Só serão carregados pacientes das ultimas 24 horas.

Para serem visualizados no Painel de Eletivos, deve ser seguido o processo de inserção de atendimentos pelo [RM](https://tdn.totvs.com/pages/viewpage.action?pageId=513434577).

## **03. TELAS UTILIZADAS**

Para buscar mais pacientes podem ser realizadas as seguintes buscas:

* Seleção da Unidade: No Combo de Seleção da Unidade é possível digitar a unidade desejada para facilitar na busca pela unidade, por padrão, o filtro é pré-selecionado pela última unidade utilizada.

* Busca de Pacientes: Através do campo "Buscar pacientes"  é possível realizar a busca pelo código, nome ou nome social do paciente e a palavra buscada poderá estar no início, meio ou final do nome e leitura da pulseira de identificação do paciente (código de barras).
* Por padrão, sistema traz os pacientes filtrados pelos status *aguardando, em atendimento e observação*. Para alterar os filtros, basta marcar os checkbox;
* Ao filtrar os resultados, os filtros atualmente selecionados são refletidos logo acima da listagem;
* Carregar mais resultados: Em qualquer momento, pode se clicar no botão "Carregar mais resultados", fazendo com que a pagina carregue mais 5 resultados da pesquisa.

A qualquer momento é possível selecionar o paciente desejado clicando na opção "Selecionar" no canto direito das informações do paciente.

**Caso o médico já esteja em atendimento:**

Quando o médico está com um atendimento já iniciado, acima da listagem de pacientes é exibida uma mensagem informando que já existe um paciente em atendimento com um link para o seu prontuário. Neste caso, as opções de **chamar o próximo** e **chamar um paciente específico** ficam desabilitados até que o atendimento seja finalizado.

## **04. PREFIXO UNIDADE**

Existe uma configuração no cadastro de unidade de atendimento que permite que seja configurado um prefixo para todas as senhas obtidas no toten para aquela unidade. O acesso à configuração se dá conforme imagem abaixo:

Quando existir um prefixo configurado, ele aparecerá antes da senha no **painel de eletivos** do **PEP RM** da seguinte forma:

## **05. TIPO DE ORDENAÇÃO**

Cada unidade de atendimento no RM Saúde possui a seguinte configuração:

Esta configuração determina se os pacientes serão ordenados por *Horário de Chegada,*sendo considerado o horário que o paciente entrou na fila do médico, ou por *Horário de Agendamento*, ou seja, o painel de eletivos se torna vinculado à Agenda do médico.

## Prioritário e risco

Ainda que o Painel de Eletivos não se comporte da mesma forma que o Painel de Classificação de Risco quanto a ordenação dos pacientes conforme as cores de algum determinado protocolo de classificação, é possível atribuir risco a um paciente Eletivo ou informar se o mesmo é prioritário (acima de 60 anos ou acima de 80 anos).

Para unidades de atendimento configuradas para ordenarem os pacientes pelo horário de agendamento, a ordem é feita da seguinte forma:

1. Pacientes com 80 anos ou mais
2. Pacientes com 60 anos ou mais
3. Pacientes em alto risco
4. Horário do Agendamento
5. Horário de Chegada

Qualquer dúvida sobre o funcionamento da ordenação, seja no PEP RM, seja no Gestão Hospitalar, entre em contato com nosso suporte.

# **DOCUMENTAÇÕES RELACIONADAS**

Exemplo de UtilizaçãoEnviar para Observação 

1. **Visão Geral**
2. **Telas utilizadas**

## **01. VISÃO GERAL**

Esta funcionalidade está presente no painel de eletivos e tem como objetivo permitir que o profissional envie um determinado paciente para observação.

## **02. TELAS UTILIZADAS**

Ao acessar a tela de Painel de Eletivos o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para enviar o paciente para observação o mesmo deve estar no status '**Em Atendimento**'

Nas ações disponíveis para o paciente na tabela, deve-se clicar no botão **'Enviar para observação'**:

A seguinte mensagem de confirmação será exibida e ao clicar em '**Confirmar**' o paciente será enviado para observação.

Pacientes em observação podem ser visualizados através do filtro '**Em observação**' conforme imagem abaixo:

Iniciar/Finalizar Atendimento

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parametrizações necessárias**
4. **Definição de Sala**

## **01. VISÃO GERAL**

Esta funcionalidade está presente no painel de eletivos e tem como objetivo permitir que o profissional inicie e finalize um atendimento para um determinado paciente ou para o próximo eletivo.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de Painel de Eletivos o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para chamar o próximo paciente eletivo, antes é necessário selecionar uma unidade na caixa de seleção:

Com a unidade selecionada, basta clicar no botão "Chamar próximo":

## **03. PARAMETRIZAÇÕES NECESSÁRIAS**

Para que seja possível chamar um paciente específico no PEP é necessário que o parâmetro '**Chama o paciente nas filas através do duplo clique no registro do grid'** seja habilitado através da antiga MDI do RM (Delphi).

A tela para alteração deste parâmetro pode ser acessada pelo menu '**Parâmetros Gerais**':

Na aba '**Classificação de Risco**' o parâmetro pode ser encontrado no canto inferior esquerdo:

* **Iniciar atendimento a partir do painel de eletivos:**

Ao acessar a tela de Painel de Eletivos o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para os pacientes que estão no status '**Aguardando'**, a última coluna da tabela irá apresentar um menu com a opção de '**Chamar o paciente**' o paciente para atendimento.

Uma modal será exibida para confirmação dos dados do paciente. Caso o campo "Sala" no painel tenha sido preenchido, tanto no cabeçalho do Painel de Eletivos do RM Saúde quando no do PEP RM, a sala selecionada será exibida no título da modal:

Ao clicar em '**Iniciar Atendimento**', caso a operação seja efetuada com sucesso a seguinte mensagem será exibida:

* **Iniciar atendimento a partir do prontuário do paciente:**

Ao acessar a tela de Painel de Eletivos o sistema carregará os pacientes de acordo com o filtro por status do atendimento.

Para os pacientes que estão no status '**Aguardando**', a última coluna da tabela irá apresentar um menu com a opção de "**Abrir Prontuário**".

Na tela do prontuário do paciente será exibido um botão com a opção de chamar o paciente em questão:

Uma modal será exibida para confirmação dos dados do paciente:

Ao clicar em "Iniciar Atendimento", caso a operação seja efetuada com sucesso a seguinte mensagem será exibida:

* **Guia passo a passo (Finalizar atendimento)**

Para finalizar um atendimento, é necessário abrir o prontuário de um paciente com atendimento iniciado.

No canto superior direito estará disponível o botão '**Finalizar atendimento**'

Ao clicar em **Finalizar atendimento**, uma modal será exibida para o preenchimento das informações da finalização do atendimento.

1. Preencha o tipo de saída;
2. Caso o sistema esteja configurado para tal, o CID também deve ser informado obrigatoriamente;
3. O preenchimento do campo observação é opcional.

Ao terminar de preencher as informações, clique em **Finalizar**

Quando o atendimento é finalizado uma mensagem de sucesso é exibida e o botão de finalizar atendimento não é mais exibido.

## **04. DEFINIÇÃO DE SALA**

Para definir a sala no PEP RM, basta preencher o campo ao lado da unidade. Caso ele já tenha sido informado no RM Saúde, a informação de lá será exibida também e o preenchimento deste campo também afeta a sala informada pelo RM Saúde para o mesmo usuário.

      

Adicionar ou Remover Pacientes da Fila 

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Telas utilizadas**

## **01. VISÃO GERAL**

Esta tela tem como objetivo auxiliar o profissional quando for necessário remover ou adicionar pacientes da fila.

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a tela de painel de eletivos o sistema carregará os pacientes de acordo com o filtro selecionado trazendo ações disponíveis na última coluna da tabela. Para filtrar pelos pacientes ausentes, basta selecionar o filtro ausentes, conforme imagem abaixo.

## **03. TELAS UTILIZADAS**

* **FILTRO**

O filtro de ausentes é exclusivo, ou seja, ao selecioná-lo, todos os outros filtros são desmarcados.

* Para os pacientes em status **'Aguardando Atendimento'** será apresentada a opção **'Remover paciente da fila'**.

* Os pacientes removidos da fila (ausentes) irão disponibilizar a opção **adicionar o paciente na fila** caso o mesmo precise voltar para a fila.
