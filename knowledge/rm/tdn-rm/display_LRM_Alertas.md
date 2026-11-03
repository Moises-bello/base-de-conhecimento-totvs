---
content_hash: 7916f8533a9e3e4cd49b3d24858fd1c9b24ee698312f5351928281e5e729f456
fetched_at: '2026-06-29T00:11:44.736318+00:00'
page_id: '815571322'
product: rm
source: tdn-rm
title: Alertas
type: documentation
url: https://tdn.totvs.com/display/LRM/Alertas
version: 9
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Ativação de recursos em tempo real**
3. **Alertas referente aos Scores**
4. **Alertas referente a Protocolos Clínico**

Documentação1. Visão geral

## **01. Visão Geral**

O módulo de **alertas** foi desenvolvido para notificar a equipe multiprofissional sobre situações de risco identificadas a partir de **protocolos (v.2506) e scores (v.2502).**

Existem dois tipos de alerta disponíveis no sistema:

* **Alerta Padrão** → O usuário final possui autonomia para parametrizar os scores e protocolos clínicos que gostaria de receber o alerta de acordo com a unidade de atendimento.
* **Alerta Crítico** → Alerta definido pela gestão do hospital, com a notificação obrigatória para os usuários parametrizados.

Os alertas aparece em **tempo real e em todas as telas do prontuário**, e compõem o painel de gerenciamento de risco.  São disparados automaticamente a partir das condições:

* Preenchimento do Score dos valores de normalidade configurados.
* Gatilho de abertura do protocolo assistencial.

Lembrando que o alerta padrão exige a configuração no PEP pelo usuário final e o alerta crítico a parametrização no RM.

Ativação de recursos em tempo real

## **02. Ativação de recursos tem tempo real**

A configuração para ativação de recursos em tempo real possibilita um nível maior de interação entre os usuários acessando a aplicação, habilitando o envio de informações do servidor de aplicação para os usuários.

## **2.1 Funcionalidade**

1. Para habilitar esse recurso, é necessário adicionar uma chave no arquivo de configuração em que está instalado o servidor de aplicação (**RM.Host**ou **RM.Host.Service**).
2. Localize o arquivo de configurações referente a instalação do **RM.Host**ou **RM.Host.Service**, e dentro da sessão **configuration /****appSettings**inclua a chave **EnableRealtime**com o valor **"true"**.
3. Com a chave habilitada, o sistema permitirá o envio de informações no sentido servidor de aplicação -> usuários, possibilitando que uma rotina processada no servidor envie notificações para os usuários acessando o sistema.
Alerta referente aos Scores

## **03. Alerta referente aos Scores**

**A configuração do alerta por unidade de atendimento e alerta crítico foi implementado a partir da v.2506**

Para que o profissional receba o alerta é necessário que ele tenha a permissão para visualização da unidade de atendimento que o paciente encontra-se. 

RM → Serviços Globais → Segurança → Perfil → Anexos → Parâmetros RM Saúde: DBA → Acesso a Unid. Atendimento

No cadastro de scores temos a parametrização relacionada ao alerta, o usuário deve definir para cada score qual o alerta será padronizado.

RM → Cadastro → Cuidados com paciente → Outros cadastros → Gerenciamento de risco → Cadastro de Score

 

## **2.1 Cadastro do alerta padrão**

O alerta padrão possibilita que o usuário configure o score e a unidade de atendimento que será utilizado o alerta. A configuração está inserida no painel de gerenciamento de risco: 

## **2.2 Cadastro do alerta crítico**

O cadastro de alerta crítico é realizado no RM, não possibilitando que o usuário final faça alteração no recebimento do alerta. 

RM → Cadastro → Cuidados com paciente → Outros cadastros → Gerenciamento de risco → Cadastro de Alertas Críticos

Os scores que são apresentados para parametrização obrigatoriamente precisam estar parametrizados com o tipo de alerta crítico.

## **2.3 Utilização no PEP**

Após parametrizações realizadas, quando outro profissional fizer o preenchimento de um score e/ou escala para o paciente, e o resultado estiver fora da faixa de normalidade, terá a ocorrência registrada no **Painel de Gerenciamento de Risco,**e caso o sistema esteja habilitado com o recurso em tempo real, também será exibido uma notificação.

Exemplo de um profissional com as configurações para geração de notificações de alertas para o score e/ou escala recebendo a notificação:

**IMPORTANTE:**

A notificação apresenta o recurso de "**Ir para Scores e Escalas".** Esse recurso direciona o profissional, através de uma nova aba do navegador, para a funcionalidade de **Scores e Escalas**do atendimento do paciente que apresentou o resultado alterado, e automaticamente marca a ocorrência como "**Visualizado".**

Exemplo de ocorrência registrada no **Painel de Gerenciamento de Risco**do profissional com a configuração para recebimento de alertas:

Alerta referente a Protocolos Clínicos

## **03. Alerta referente aos Protocolos Assistenciais (Clínicos)**

**A configuração do alerta por unidade de atendimento e alerta crítico foi implementado a partir da v.2506**

Para que o profissional receba o alerta é necessário que ele tenha a permissão para visualização da unidade de atendimento que o paciente encontra-se. 

RM → Serviços Globais → Segurança → Perfil → Anexos → Parâmetros RM Saúde: DBA → Acesso a Unid. Atendimento

No cadastro de protocolos temos a parametrização relacionada ao alerta, o usuário deve definir para cada protocolo qual o alerta será padronizado.

RM → Cadastro → Cuidados com paciente → Outros cadastros → Gerenciamento de risco → Cadastro de Protocolos assistenciais 

 

## **2.1 Cadastro do alerta padrão**

O alerta padrão possibilita que o usuário configure o protocolo e a unidade de atendimento que será utilizado o alerta. A configuração está inserida no painel de gerenciamento de risco: 

## **2.2 Cadastro do alerta crítico**

O cadastro de alerta crítico é realizado no RM, não possibilitando que o usuário final faça alteração no recebimento do alerta. 

RM → Cadastro → Cuidados com paciente → Outros cadastros → Gerenciamento de risco → Cadastro de Alertas Críticos

Os protocolos que são apresentados para parametrização obrigatoriamente precisam estar parametrizados com o tipo de alerta crítico.

## **2.3 Utilização no PEP**

Após parametrizações realizadas, quando outro profissional fizer o preenchimento de um protocolo para o paciente, terá a ocorrência registrada no **Painel de Gerenciamento de Risco,**e caso o sistema esteja habilitado com o recurso em tempo real, também será exibido uma notificação.

Exemplo de um profissional com as configurações para geração de notificações de alertas para o score e/ou escala recebendo a notificação:

**IMPORTANTE:**

A notificação apresenta o recurso de "**Ir para Protocolo".** Esse recurso direciona o profissional, através de uma nova aba do navegador, para a funcionalidade de **Protocolos** do atendimento do paciente que apresentou o resultado alterado, e automaticamente marca a ocorrência como "**Visualizado".**

Exemplo de ocorrência registrada no **Painel de Gerenciamento de Risco**do profissional com a configuração para recebimento de alertas:
