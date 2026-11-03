---
content_hash: 04fa214d791ad956b3462c95f294ab78599d8243cbf6b3f950d1404fc5ea69a2
fetched_at: '2026-06-29T00:10:26.269081+00:00'
page_id: '514431682'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Atendimento > Atendimento de Internação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=514431682
version: 31
---

## **ÍNDICE**

1. **Visão Geral**
2. **Importante / Parâmetros**
3. **Tela Inicial**
   1. **Outras Ações / Ações relacionadas**
4. **Tela do atendimento de internação**
5. **Atendimento de pré-registro interno**



sumarioVisão Geral

## **01. VISÃO GERAL**

LGPD - Lei Geral de Proteção de Dados

Informamos que os dados pessoais contidos nesta entidade foram colhidos para emissão de documentos fiscais e geração de rotinas legais e são retidos por determinação legal de normas fiscais e de transparência. Os mesmos não poderão ser eliminados em virtude de obrigação legal de retenção. O comprimento de obrigação legal é hipótese legítima do tratamento dos seus dados conforme a Lei Geral de Proteção de Dados Pessoais (Lei n° 13.709/2018).

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS consulte nossa página neste link ([https://tdn.totvs.com/pages/releaseview.action?pageId=514427789](https://tdn.totvs.com/pages/releaseview.action?pageId=514427789 "Follow link")).

A Internação é o processo de registro do paciente no Hospital/Clínica, para a realização de procedimentos em caráter interno, de urgência ou eletivo.

A visão é acessada no menu Atendimento / Recepção / Registro de Atendimento. Serão exibidos todos os atendimentos de acordo com o filtro desejado. O usuário pode criar filtros que desejar na visão para facilitar o atendimento, tais como: filtro por nome, por data de atendimento, por código da carteira do convênio, por tipo de atendimento, etc.

Importante / Parâmetros

## **02. IMPORTANTE**

Trata-se de um cadastro essencial para as demais funcionalidades dentro do processo de atendimento ao paciente internado e é realizado o registro da entrada do paciente na instituição de saúde.

Para definir obrigatoriedade de algum campo ou valor default, deve-se abrir a tela em modo de visualização, clicar com o botão direito sobre o campo desejado e definir se o mesmo é obrigatório e se o valor já preenchido será o valor default.

Para verificar quais são as configurações definidas para todos os campos, selecione a opção “Todas as preferências...”

## **PARÂMETROS**

Nos parâmetros Gestão Hospitalar > Registro e Controle é possível parametrizar o registro de atendimento e suas funcionalidades.

Para definir **valores default de convênio e plano** acesse:  
Gestão Hospitalar > Registro e Controle > Registro e Controle 3

Informe o convênio default e plano, estes serão preenchidos automaticamente caso o valor de convênio esteja vazio. O parâmetro **Carregar dados do ultimo atendimento** preencherá as informações de convênio primeiro, caso esteja marcado.  
Se o registro estiver sendo criado a partir de um agendamento estes valores default não são considerados, apenas os definidos para agendamento.

Tela Inicial

## **03. TELA INICIAL**

**Outras Ações / Ações relacionadas**

| Ação | Descrição |
| --- | --- |
| Clique em 'Novo', o sistema abrirá a visão pedindo informações do atendimento. | Deve-se preencher todos os campos obrigatórios e necessários com as informações do atendimento. |

Tela do atendimento de internação 

## **04. TELA DO ATENDIMENTO DE INTERNAÇÃO**

```

```

* Ao selecionar  a opção novo, abrirá uma tela solicitando informações do paciente, informe ou clique em [ok].

* Irá abrir a visão para inclusão de um novo atendimento. Confira os dados do paciente e logo após clique em 'Atendimento' no canto esquerdo da tela.

* Ao clicar em 'Atendimento', o sistema exibe os campos para preenchimento das informações necessárias, selecione a opção interno;
* Unidade de Atendimento: este campo é obrigatório e as unidades que são listadas, dependem de parametrizações gerais para terem comportamentos distintos.  
  “Escolhe unid. atend. No registro de internação” e “Escolhe unid. atend. No registro externo”, serve para definir se o campo fica habilitado para escolher a unidade.

  Caso esteja marcado, o sistema listará somente as unidade de acordo com o tipo de paciente escolhido previamente. Com os parâmetros desmarcados, é necessário configurar cada estação de trabalho, para utilizar a “Unidade de atendimento” default.
* “Filtra unidade de atendimento (Registro/Agenda)”: serve para filtrar as unidades de acordo com as unidades configuradas no perfil (anexo de Perfil denominado  “Parâmetros RM Saúde”), na aba “Acesso a Unid. Atendimento”. Este parâmetro é utilizado quando existem muitas unidades de atendimento com endereços distintos, por exemplo, em unidades de hospitais diferentes. Neste cenário, é necessário que os usuários acessem somente as unidades de onde trabalham.
* Deve-se incluir todas as informações necessárias do paciente e convênio.

```

```

* Após selecionar o campo "Tipo do Paciente", clique no botão para selecionar o Leito. Uma nova tela vai abrir chamada "Painel de Leitos"

* Nesta tela somente os leitos livres serão apresentados.
* Também os leitos conforme o sexo do paciente

* Confirme o Leito selecionado.
* Validações serão feitas antes de ocupar o leito, por como exemplo: Centro de Custos, Código de Diária;
* Em situações em que o parâmetro AlteraRespDifDiaria  estiver marcado e os campos "Ocupa Leito", "Número do Leito" e o "Código da Diferença de Diária" estiverem preenchidos, ao editar o atendimento será possível realizar a alteração do responsável pela diária. Lembrando que todas essas alterações são registradas como uma mudança de leito alterando somente o responsável pela diária.
* Caso na mudança de leito seja selecionado um leito que não é coberto pelo plano e não seja informado uma diária base, ao editar o atendimento, o último botão da Imagem 10 será exibido. Ele será exibido somente nessa situação. Ao clicar, será exibida a mensagem "O plano xyz não tem cobertura para o tipo de acomodação selecionada. Deseja escolher outra condição contratual para a(s) diária(s)?" Ao responder sim, será exibida uma tela com as diárias disponíveis. Basta dar um duplo clique sobre a diária desejada que o sistema fará a seleção e depois clicar no botão Salvar, para salvar a diária informada. Após isso, o botão não será mais exibido.

```
Imagem 10
```

* A partir desta seleção, o Leito já encontra-se como "Ocupado". É uma "reserva" até o cadastro final do atendimento interno. Caso abandone a operação e clicar na opção de "Ocupa Leito" igual a "Não" este leito será liberado.
* Após Selecionar "Tipo Paciente" como "Interno" (vide imagem 6) será habilitado dentro de "Dados específicos do Atendimento Interno" (vide imagem 10), um box chamado "Paciente Gestante" e dentro do mesmo um campo chamado "Primeiro Parto" conforme imagem 11 abaixo.
* Validações necessárias para que o campo "Primeiro Parto" esteja visível: Paciente do Sexo Feminino.

```
Imagem 11
```

* É possível incluir um atendimento de internação com o campo Data de Entrada Retroativa realizando um Encaixe. Para a inclusão desse tipo de atendimento o Paciente não pode ter atendimento sem Alta e a Data de Entrada tem que ser menor do que a data Atual.  O Atendimento de encaixe não pode utilizar leitos e ele irá definir a Data Saída e Hora Saída igual a Data de Entrada e Hora de Entrada, finalizando o Atendimento de forma automática.

A imagem acima exibe uma mensagem de confirmação informando que o atendimento é encaixe, caso de confirmação a tela abaixo demonstra o comportamento do tópico anterior.

Atendimento de pré-registro interno

## **05. ATENDIMENTO DE PRÉ-REGISTRO INTERNO**

Quando o tipo de atendimento selecionado é **Pré-Registro Interno**, o sistema ajusta a interface de usuário para permitir a configuração de reservas de leito. Essa funcionalidade é crucial para garantir que pacientes internos tenham suas acomodações preparadas com antecedência.

No contexto de Pré-Registro Interno, o sistema exibe campos específicos para gerenciar a reserva de leitos. Os campos são:

1. **Reservar leito (Sim/Não):**

   * Este campo permite ao usuário indicar se há necessidade de reservar um leito para o paciente.
   * **Opções:** Sim, Não
2. **Tipo de leito (UI/UTI):**

   * Este campo permite ao usuário especificar o tipo de leito necessário, caso a reserva seja necessária.
   * **Opções:** UI (Unidade de Internação), UTI (Unidade de Terapia Intensiva)

### Procedimento

1. **Acesso ao Pré-Registro Interno:**

   * Navegue até a área de registro de atendimentos e selecione a opção de Pré-Registro Interno.
2. **Preenchimento dos Campos de Reserva de Leito:**

   * **Reservar leito:**
     + Selecione "Sim" se for necessário reservar um leito para o paciente.
     + Selecione "Não" se não houver necessidade de reserva de leito.
   * **Tipo de leito:**
     + Se a reserva de leito foi marcada como "Sim", escolha entre "UI" (Unidade de Internação) ou "UTI" (Unidade de Terapia Intensiva) para especificar o tipo de leito necessário.

```

```
