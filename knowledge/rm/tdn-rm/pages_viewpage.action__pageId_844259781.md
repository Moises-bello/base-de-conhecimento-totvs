---
content_hash: d6407b896de4df17b65fa2224ccbd15022617a2cdba726afe6e68fedd993b6a6
fetched_at: '2026-06-29T00:11:50.642035+00:00'
page_id: '844259781'
product: rm
source: tdn-rm
title: Scores.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844259781
version: 13
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
   1. **Tipo de seleção das respostas**
3. **Cadastro RM**
4. **Cadastro RM - A PARTIR V.2506**

Scores (V.2406)Visão Geral

## **01. VISÃO GERAL**

A nova funcionalidade de preenchimento de scores e escalas será integrada na aba "Scores", no menu lateral do PEP. Essa funcionalidade permitirá que os profissionais de saúde registrem, visualizem e analisem os resultados e status dos scores e escalas, garantindo maior precisão e eficiência na avaliação e monitoramento dos pacientes.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Ao acessar a aba de Scores no PEP, será exibido uma timeline contendo os scores e escalas preenchidos, quando houver, composta por:

* Status (alterado ou normal): resultado do **último** score/escala preenchido indicando se o mesmo está de acordo ou fora do valor mínimo e máximo cadastrado no RM.
* Score/Escala: nome do score ou escala utilizada
* Botão "Histórico": exibe o histórico de preenchimento do score/escala selecionado.
* Botão "Adicionar": abre modal para seleção e preenchimento dos scores e escalas.
* Botão "Imprimir"

Ao expandir o accordion, será exibido um histórico de preenchimento do score ou escala em uma tabela, composta por:

* Ícone com responsável pela criação, pelo registro e suspensão do score/escala com data e hora e da liberação
* Status de assinatura
* Data e hora  da aplicação da escala
* Pontuação e Classificação quando aplicável
* Ícone de opções:
  + Visualizar: exibe modal com o score/escala preenchida sem opção para edição, se o registro estiver **finalizado**.
  + Editar: exibirá uma modal com o score/escala preenchido com possibilidade de edição. Essa opção é habilitada quando o score/escala estiver como **rascunho**.
  + Excluir: essa opção é habilitada quando o score/escala estiver como **rascunho.**
  + Suspender: essa opção é habilitada quando o score/escala estiver como **finalizado.**
  + Imprimir: imprime apenas o score/escala selecionado.

Para iniciar o preenchimento de um score ou escala, clique no botão "**+ Adicionar**". Uma modal será exibida para preenchimento, composta por:

* Score ou Escala: a lista exibida será composta por scores e escalas cadastrados, conforme permissão do usuário.
* Data e horário de aplicação.
* Resultado: exibe a pontuação e/ou classificação obtida após o preenchimento e informa se o resultado está com ou sem alterações. Exibe também orientações recomendadas para os profissionais quando aplicável.
* Botão Cancelar: cancela a inclusão e as informações preenchidas são perdidas.

Para finalizar o preenchimento, clique no botão **"Incluir"**. A modal continuará aberta para que o usuário selecione outros scores e escalas para preenchimento, quando necessário.

* Se o preenchimento do score/escala estiver incompleto e o usuário fechar a modal, essa versão ficará salva como rascunho e será recuperada ao reabrir a modal.
* A assinatura digital será solicitada somente ao adicionar o primeiro score e/ou escala preenchida, para os demais, a assinatura não será solicitada para o mesmo usuário.

Para visualizar o histórico de preenchimento de um score ou escala, clique no botão **"Histórico"** e uma modal será exibida, composta por:

* Score ou Escala: campo para selecionar o score ou escala.
* Data inicial e final: filtra os registros no período selecionado.

Após preencher os campos, clique no botão **"Filtrar"** para exibir o histórico.

O histórico será exibido em uma tabela contendo:

* Ícone com nome do profissional responsável pela criação e registro do score/escala.
* Status do resultado.
* Data e hora da liberação.
* Pontuação e Classificação quando aplicável.

Ao expandir o accordion, as respostas selecionas pelo profissional serão exibidas.

O usuário poderá imprimir os scores e escalas preenchidas clicando no botão **"Imprimir"** na tela principal. O usuário poderá selecionar quais scores e escalas serão impressas marcando ou desmarcando o respectivo checkbox e também definir um período para impressão preenchendo os campos de data inicial e data final.

## **02.a TIPO DE SELEÇÃO DAS RESPOSTAS**

O sistema permite que as perguntas dos scores sejam apresentadas com dois tipos de seleção:

* **Seleção única:** o usuário pode escolher apenas uma opção.
* **Seleção múltipla:** o usuário pode selecionar uma ou mais opções simultaneamente. (*A partir da versão **12.1.2602***)

Essa definição impacta diretamente a forma de preenchimento e a visualização das respostas.

#### 🔹 Comportamento na interface

* Perguntas de **seleção única** exibem opções exclusivas.
* Perguntas de **seleção múltipla** permitem marcar mais de uma alternativa. (*A partir da versão **12.1.2602***)
* O usuário pode revisar e alterar as seleções enquanto o registro estiver em rascunho.

#### 🔹 Aplicabilidade

Nesta fase, o comportamento de múltipla seleção e sua respectiva lógica de cálculo aplicam-se exclusivamente ao **score SAPS III**, contemplando os seguintes campos:

* Comorbidades
* Motivo de internação (Infecção)
* Motivo de internação (Cardiológico)
* Motivo de internação (Abdômen)
* Motivo de internação (Neurológico)

O cálculo da probabilidade de óbito no **SAPS III** utiliza a equação calibrada para a América Central/Sul, garantindo maior aderência à realidade regional.

Cadastro RM

## **03. CADASTRO RM**

* Cadastro de valor mínimo e máximo de normalidade dos resultados obtidos nos scores e escalas para :

RM > Cadastros > Cuidados com o Paciente: Outros Cadastros > Gerenciamento de Risco > Cadastro de Scores.

Escolha o score ou escala, utilize o campo de busca se necessário, e clique na seta indicada:

Clique no botão "Editar" e na tela seguinte preencha os campos com o valor mínimo e máximo. Para finalizar a inclusão, clique no botão "Salvar":

RM Cadastro V.2506Cadastro RM

## **04. CADASTRO RM**

A funcionalidade de **parametrização de scores** permite ao usuário configurar:

* Valores de normalidade de cada score.
* Se valores fora da normalidade irão **disparar alertas**.
* O **tipo do alerta**:

  + **Padrão** → alerta com possibilidade de parametrização pelo usuário final e monitorado no *Painel de Gerenciamento de Risco* .
  + **Crítico** → alerta sem possibilidade de parametrização pelo usuário final e monitorado no *Painel de Gerenciamento de Risco* .
* Em quais **unidades de atendimento** o score estará disponível para preenchimento.

Essa configuração garante a padronização do uso dos scores pela instituição e reforça a segurança do paciente.

## **4.1. Fluxo de cadastro referente ao Score**

### 🔹 Valor de normalidade

* Informe o **intervalo de valores considerados normais** para o score.
* Sempre que um valor fora dessa faixa for preenchido, o sistema irá **disparar um alerta** (se configurado).

### 🔹 Unidade de Atendimento

* Selecione em quais **unidades de atendimento** o score estará habilitado para preenchimento.
* Isso garante que apenas as unidades parametrizadas possam lançar valores desse score.

### 🔹 Utilização de Alerta

* Defina se o score terá **alerta habilitado ou não**.
* Caso habilitado, escolha o **tipo**:

  + **Alerta Padrão** →
  + **Alerta Crítico** →

##
