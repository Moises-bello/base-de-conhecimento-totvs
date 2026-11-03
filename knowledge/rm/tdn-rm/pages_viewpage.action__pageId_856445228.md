---
content_hash: 798998503f45d26da47e6a9617c492a198a41cf1ba777c35353e0361e3720957
fetched_at: '2026-06-29T00:11:54.621634+00:00'
page_id: '856445228'
product: rm
source: tdn-rm
title: Integração RM x Cross
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=856445228
version: 20
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Parâmetros e permissões**
3. **Relacionamento**
4. **Monitor de Integração**4.1. **Detalhar informações**
5. **Registrar Internação**5.1**. Cancelamento Internação**
6. **Informar Alta Paciente**6.1. **Cancelamento de Alta**

Integração RM CrossVisão Geral

## **01. VISÃO GERAL**

Integração com sistema Cross (Central de regulação de ofertas de serviços de saúde)Parâmetros Gerais

## **02. PARÂMETROS GERAIS**

Parametrização necessária para Integração com o sistema CROSS

Acesse Ambiente > Configuração > Parâmetros > Gestão Hospitalar

Após a aberturado processo, clique em avançar, selecione:

Preencha os Campos e clique em avançar:

A seguinte mensagem será exibida:

Clique em Sim e em Concluir.

Relacionamento

## **relacionamento03. RELACIONAMENTO**

Relacionamento necessário para realização da integração RM x Cross.  
Para fazer isto acesse Utilitários e depois Integração relacionamento. Como é mostrado abaixo

Para cadastrar um novo clique em incluir e preencha da seguinte forma:

* **Identificador RM**: Identificador do medicamento que consta no sistema RM
* **Identificador Sistema:** Identificador do medicamento que consta no sistema Cross
* **Descrição**: Pode-se entrar qualquer coisa
* **Tipo de Integração:** Para sistema Cross usamos ou Especialidade, Estado Civil, Raça Paciente, Tipo Documento, Leito do Paciente
* **Sistema Integrador:** No caso, sempre será escolhido sistema Cross

Após clicar em salvar, o registro será salvo. Dessa forma, ao fazer uma integração que envolva internação essas informações serão consultadas para fazer a integração corretamente.

Monitor Integração

## **monitorCross04. MONITOR DE INTEGRAÇÃO CROSS**

Monitor de integração para visualizar todas as integrações realizadas e status das integrações realizadas com sistema Cross.

Necessario: Permissão de acesso no perfil

Acesse Utilitários > Integrações > Monitor Integração Cross

Será exibido todas as integrações realizadas

#### **4.1. Detalhar informações**

Detalhar informações das integrações realizadas

Registrar Internação

## **05. REGISTRAR INTERNAÇÃO**

Registrar internação e integrar com sistema CROSS (Central de regulação de ofertas de serviços de saúde).

Necessario que as configurações de parametros gerais e correlação de integração - itens 02 e 03 deste documento - estejam feitas corretamente.

Seguir o caminho: Aba 'Atendimento' > Seção 'Recepção'> Item: 'Registro Atendimento'

Realizar o registo de internação informando obrigatoriamente o convênio como **SUS**Marcar o ocupa leito como **SIM**Informar um leito que esteja devidamente relacionado no itemInformar a especialidade cujo esteja devidamente relacionado no item

Obs.  
Dados do paciente que são obrigatórios para integração:

* Nome Paciente
* Nome Mãe
* Data Nascimento
* Sexo (devidamente relacionado no item )
* Raça (devidamente relacionado no item )
* Estado Civil (devidamente relacionado no item )
* Munícipio
* IBGE Munícipio
* UF
* DDD + Telefone

Ao clicar em salvar a integração será realizada.

A validação da integração poderá ser verificada no item  deste documento.

Cancelamento Internação

###### **5.1. CANCELAMENTO INTERNAÇÃO**

Informar o cancelamento da internação e integrar com sistema CROSS (Central de regulação de ofertas de serviços de saúde).

Necessario que as configurações de parametros gerais e correlação de integração - itens 02 e 03 deste documento - estejam feitas corretamente.

Seguir o caminho: Aba 'Atendimento' > Seção 'Recepção'> Item: 'Registro Atendimento' > Selecionar a internação > Processo: Cancelamento Internação  
  
ou

Seguir o caminho: Aba 'Atendimento' > Seção 'Recepção'> Item: 'Cancelamento'

Após selecionar a internação desejada e iniciar o processo será exibido a tela abaixo.

Ao clicar em '*Avançar*' e posteriormente em '*Executar*', o RM realizará o cancelamento da internação do paciente no RM, e no sistema Cross  
A validação da integração poderá ser verificada no item  deste documento.

Informar Alta

## **06. INFORMAR ALTA PACIENTE**

Informar alta do paciente e integrar com sistema CROSS (Central de regulação de ofertas de serviços de saúde).

Necessario que as configurações de parametros gerais e correlação de integração - itens 02 e 03 deste documento - estejam feitas corretamente.

Seguir o caminho: Aba 'Atendimento' > Seção 'Alta'> Item: 'Alta'

Informar motivo da alta que esteja devidamente relacionado no itemInformar obrigatoriamente o CID da alta

Obs.  
Dados do paciente que são obrigatórios para integração:

* Nome Paciente
* Nome Mãe
* Data Nascimento
* Sexo (devidamente relacionado no item )
* Raça (devidamente relacionado no item )
* Estado Civil (devidamente relacionado no item )
* Munícipio
* IBGE Munícipio
* UF
* DDD + Telefone

Ao clicar em '*Avançar*' e posteriormente em '*Executar*', o RM realizará a alta do paciente no RM e no sistema Cross  
A validação da integração poderá ser verificada no item  deste documento.

**6.1. Cancelamento de Alta**

Informar o cancelamento da Alta e integrar com sistema CROSS (Central de regulação de ofertas de serviços de saúde).

Necessario que as configurações de parametros gerais e correlação de integração - itens 02 e 03 deste documento - estejam feitas corretamente.

Seguir o caminho: Aba 'Atendimento' > Seção 'Alta'> Item: 'Alta' 

Informar o paciente que recebeu alta e marcar o 'Cancelamento de Alta'

Após clicar em 'Avançar', será exibido a tela para conferencia dos dados para cancelamento da alta conforme tela abaixo

Após clicar em 'Avançar' e logo em seguida 'Executar' o processo de reversão de alta será iniciado e a alta será retornada  no RM e no sistema Cross  
A validação da integração poderá ser verificada no item  deste documento.

---
