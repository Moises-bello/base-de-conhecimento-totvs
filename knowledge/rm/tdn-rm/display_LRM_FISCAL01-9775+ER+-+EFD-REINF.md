---
content_hash: b5f0f9bef41c673058e2e17038f186365458e6edbf0b5e61562a00011856acde
fetched_at: '2026-06-29T00:10:25.000522+00:00'
page_id: '501121103'
product: rm
source: tdn-rm
title: FISCAL01-9775 ER - EFD-REINF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-9775+ER+-+EFD-REINF
version: 142
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

# Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | RM | **Módulo** | TOTVS Gestão Fiscal |
| **Segmento Executor** | Backoffice | | |
| **Requisito/Story/Issue** | FISCAL01-9775 | **Subtarefa** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

# Objetivo

Detalhar as alterações necessárias no módulo TOTVS Gestão Fiscal para a implementação da EFD-REINF.

# Introdução

De acordo com o manual da Escrituração Fiscal Digital de Retenções e Outras Informações Fiscais (EFD-REINF) versão 1.04.00 de dezembro de 2018, a EFD-REINF é uma obrigação acessória que visa basicamente reunir informações de retenção e algumas informações fiscais conforme interesse da Receita Federal do Brasil (RFB).

## Exigência

Estão obrigados a EFD-REINF as pessoas jurídicas que prestaram ou contrataram serviços, que retiveram PIS/Pasep, Cofins, CSLL, CPRB, IRRF entre outros, conforme consta no manual versão 1.04.00 seção 2.4 “Pessoas Obrigadas as Declarar”.  
A REINF deverá ser gerada e entregue mensalmente até o dia 15 do mês subsequente ao fato gerador, salvo especificidades previstas na legislação.  
De acordo com a IN RFB 1.842/2018, de 29 de outubro de 2018 serão obrigadas a EFD-REINF a partir de 10 de julho de 2019 todas as empresas que são do Regime Especial Unificado de Arrecadação de Tributos e Contribuições devidos pelas Microempresas e Empresas de Pequeno Porte (Simples Nacional), sendo que as demais já estão obrigadas exceto órgãos públicos.

## EFD-REINF

A EFD-REINF é constituída por vários arquivos magnéticos que representam eventos e devem obedecer ao layout próprio conforme o manual técnico em vigência. Cada evento deve ser assinado digitalmente conforme regras publicadas no manual técnico.  
A entrega dos eventos deverá ocorrer por lotes que podem ser constituídos de 1 (um) à 100 (cem) eventos sendo estes transmitidos para a RFB através do Webservices (WS) pela internet conforme definições do manual técnico.  
Os eventos devem obedecer a sequência lógica conforme abaixo.

* R-1000 e R-1070: Estes eventos são únicos e não precisam ser reenviados a RFB periodicamente, apenas quando for necessário atualizar os dados.
* R-2010, R-2020, R2030, R-2040, R-2050, R-2060 e R-2070: Estes eventos devem ser enviados até o dia 15 do mês seguinte à emissão da nota fiscal ou fatura ou antes do envio do evento R-2099 - Fechamento dos Eventos Periódicos, o que ocorrer primeiro.
* R-2099: Este evento é utilizado para informar o encerramento do período de apuração dos eventos periódicos. Deve ser transmitido até o dia 15 do mês subsequente ao do mês de referência informado no evento.
* R-2098: Este evento poderá ser utilizado após o evento R-2099 com o intuito de reabrir o período de apuração e possibilitar ajustes. Após os ajustes o encerramento do período precisa ser realizado novamente através do R-2099.
* R-3010: Este possuí um período é especifico conforme regras do manual da EFD-REINF e não é afetado pelos eventos R-2099 e R-2098.
* R-5001: Este evento será retornado como resposta de qualquer evento periódico enviado. No caso de um lote com vários eventos será retornando um R-5001 para cada evento enviado.
* R-5011: Este evento é o totalizador do período e deverá ser consultado após o encerramento do mesmo.
* R-9000: Este evento é utilizado para anular qualquer evento periódico (R-2010 à R-2070) ou não periódico (R-3010). Contudo, para os eventos periódicos o período não poderá estar encerrado.

# Obrigações Acessórias

Deverá ser criado um menu EFD-REINF no Módulo Fiscal Pasta Obrigações acessórias e só poderá ser acessado pela filial matriz ou SCP. Este menu terá os seguintes submenus “Eventos Cadastrais” e “Eventos Periódicos”.

Sugiro alterar o menu SPED colocando com submenus do mesmo a opção EFD-ICM IPI e EFD-REINF

# Parâmetros

Deverá ser criado um parâmetro por Filial para armazenar a versão e ambiente da EFD-REINF. Devido a integração com o TOTVS Service Soa (TSS) eu sugiro que seja criado um parâmetro no Totvs Gestão Fiscal para exibir as configurações de conexão com o TSS (TPARFILIAL) e que neste mesmo parâmetro sejam exibidos os campos abaixo.

* **Ambiente:** deverá apresentar as opções:  
  1 - Produção;  
  2 - Produção restrita.
* **Versão:** deverá apresentar um combobox com a versão 1.4.01

# Estrutura de tabelas para os Eventos

Apesar das pequenas diferenças todos os eventos têm a mesma estrutura então será detalhado abaixo a estrutura que será criada para cada Evento seja ele um Evento Cadastral ou Evento Periódico.

truetruefalseEstrutura EFD-REINFfalse4024

## Tabela Evento

Sugestão de nome: DEVENTOREINF

* **Identificador:** Identificador do cadastro do evento;
* **Cód. Coligada:** código da coligada na qual o cadastro foi realizado;
* **Id. Evento Pai:** deve ser preenchido com o evento pai, porém pela sequencia lógica da EFD-REINF o Evento R-1000 terá este campo em branco;
* **Id. Evento REINF:** ID de 36 posições definido pela EFD-REINF. Este campo será preenchido após a primeira integração com o TSS.
  + A identificação única do evento (Id) é composta por 36 caracteres, conforme o que segue:  
    IDTNNNNNNNNNNNNNNAAAAMMDDHHMMSSQQQQQ  
    ID - Texto Fixo "ID";  
    T - Tipo de Inscrição do Empregador (1 - CNPJ; 2 - CPF);  
    NNNNNNNNNNNNNN - Número do CNPJ ou CPF do empregador - Completar com zeros à direita. No caso de pessoas jurídicas, o CNPJ informado deve conter 8 ou 14 posições de acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento R-1000, completando-se com zeros à direita, se necessário.  
    AAAAMMDD - Ano, mês e dia da geração do evento;  
    HHMMSS - Hora, minuto e segundo da geração do evento;  
    QQQQQ - Número sequencial da chave. Incrementar somente quando ocorrer geração de eventos na mesma data/hora, completando com zeros à esquerda.  
    OBS.: No caso de pessoas jurídicas, o CNPJ informado deverá conter 8 ou 14 posições de acordo com o enquadramento do contribuinte para preenchimento do campo {ideEmpregador/nrInsc} do evento S-1000, completando-se com zeros à direita, se necessário.
* **Tipo:** deve ser preenchido com o código do evento da EFD-REINF, exemplo: R-1000, R-1070, R-2010 etc.;
* **Ambiente:** deve ser preenchido com o parâmetro cadastrado para a Filial;
* **Início do Período:** data de início da vigência da EFD-REINF ou do Evento em questão;
* **Fim do Período:** data final do Evento em questão
* **Status:** poderá assumir um dos seguintes valores:
  + Não Transmitido: o Evento foi cadastrado, mas ainda não foi integrado com o TSS para ser transmitido a RBF;
  + Pendente: o Evento foi cadastrado e já integrado com o TSS, e será necessário realizar o processo de consulta para verificar o resultado do processamento do Evento junto a RBF;
  + Inconsistente: os cadastros que dão origem ao Evento estão preenchidos incorretamente e por este motivo não foi possível montar o Evento. O motivo da inconsistência poderá ser verificado no campo observação do histórico;
  + Rejeitado: a RFB não autorizou o Evento por qualquer motivo e o mesmo foi rejeitado. O motivo da rejeição poderá ser verificado no campo observação do histórico;
  + Autorizado: a RFB validou e autorizou o Evento;
  + Alterado: Após autorização os dados de origem do Evento foram alterados e o Evento precisa ser retransmitido a RFB;
  + Pendente Exclusão: foi transmitido o Evento de Exclusão R-9000 e integrado com o TSS com sucesso. Ainda será necessário realizar o processo de consulta para verificar o resultado do processamento do Evento junto a RFB;
  + Excluído: o Evento foi excluído com sucesso do ambiente da RFB.
* **Data da Última Transmissão:** data da última transmissão autorizada ou excluída;
* **Número do Protocolo:** número do último protocolo retornado pela RFB para este Evento;
* **Cód. da Filial:** código da filial no qual este registro pertence;
* **XML de envio:** xml do último Evento enviado a RFB, contudo dependendo do status este campo poderá estar em branco;
* **XML de retorno:** xml do último Evento retornado pela RFB, contudo dependendo do status este campo poderá estar em branco.

**Primary key:** Identificador  
**Foreign key:** Cód. Coligada - FK com a tabela de coligada, Id. Evento Pai - FK com a própria tabela de Evento (auto relacionamento), Cód Filial - FK com a tabela de Filiais.  
**Unique key:** Identificador, Cód. Coligada  
**Campos Nullable**: Id. Processo,Id. Evento Pai, Id. Evento REINF, Fim do Período, Data da Última Transmissão, Número do Protocolo, XML de envio e XML de retorno.

SUGESTÃO

Utilizar o mesmo ID que será enviado ao TSS com 100 posições. Exemplo: Coligada + Tipo do Evento + o Identificador do cadastro do Evento

## Tabela de Histórico

Sugestão de nome: DEVENTOREINFHIST

* **Identificador:** será o Id do evento no qual este histórico pertence;
* **Id Evento REINF:** será preenchido com o ID de 36 posições definido pela EFD-REINF;
* **Status:** poderá assumir um dos seguintes valores:
  + Não Transmitido;
  + Pendente;
  + Inconsistente;
  + Rejeitado;
  + Autorizado;
  + Alterado;
  + Pendente Exclusão;
  + Excluído.
* **Data do status**: será gravada a data na qual aquele status foi gerado;
* **Tipo:** deve ser preenchido com o código do evento da EFD-REINF, exemplo: R-1000, R-1070, R-2010 etc.;
* **XML de envio:** será preenchido com o xml do evento enviado a RFB, contudo dependendo do status este campo poderá estar em branco;
* **XML de retorno:** será preenchido com o xml retornado pela RFB, contudo dependendo do status este campo poderá estar em
* **Número do Protocolo:** será preenchido com o número do protocolo retornado pela RFB para este status;
* **Observação:** quando necessário será preenchido com os detalhes do status.

**Foreign key:** Identificador - FK com a tabela Evento.  
**Campos Nullable**: XML de Envio, XML de retorno e Observação.

# Cadastro

Os Eventos devem seguir o padrão de cadastros do ERP, contudo podem existir particularidades entre os Eventos e neste caso deve ser verificada a regra na documentação especifica do Evento.

## Inclusão

Ao ser incluído o Evento assumira o Status de "Não transmitido".

## Edição

Quando o Evento estiver com Status de "Não Transmitido" o status não será alterado, quando o Evento estiver com o Status "Inconsistente" ou "Rejeitado" o Status será alterado para "Não Transmitido". Qualquer outro status o Evento assumirá o Status de "Alterado".

## Exclusão

O cadastro do Evento poderá ser excluído somente quando status for Não Transmitido, Inconsistente ou Rejeitado. 

ATENÇÃO

Não confundir Exclusão de cadastro com o Evento de Exclusão R-9000 da RFB.

## Regras

* Quando o Evento estiver com status de "Pendente" ou "Pendente Exclusão" todos os campos precisão permanecer boqueados para Edição inclusive os campos nos cadastros de origem do Evento;
* Quando o Evento estiver com status de Excluído o mesmo deverá ser bloqueado para Edição, mas os campos de origem não serão bloqueados;
* Os campos **Cód. Coligada** e **Cód. da Filial**não devem ficar visíveis para o usuário;
* Nenhum histórico pode ser alterado, excluído ou incluído;
* Os campos **Identificador,** **Status,** **Tipo,** **Ambiente,** **Data da Última Transmissão, Número do Protocolo, XML de envio, XML de retorno** não devem ser editáveis;
* O campo **Id. Evento Pai** só poderá ser alterado quando o Status for "Não Transmitido", "Inconsistente" ou "Rejeitado".

# Layout das estruturas comuns à todos os Eventos

Serão demonstrados os layouts referentes à estrutura comuns entre os Evento, contudo algum Evento pode ter um comportamento diferente do descrito abaixo e neste caso deverá ser verificado a documentação do mesmo.

falseOrigensleft0idePeriodo

## idePeriodo

xmlidePeriodo
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| iniValid | Campo "Início do Período" do Cadastro do Evento |
| fimValid | Campo "Fim do Período"  do Cadastro do Evento |

1ideEvento

## ideEvento

xmlideEvento
123
123
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpAmb | Será gerado conforme o campo **Ambiente**  do Cadastro do Evento |
| procEmi | Valor fixo 1 - Aplicativo do contribuinte |
| verProc | Será gerado conforme o campo **Versão**do parâmetro da EFD-REINF |

2ideContri

## ideContri

xmlideContri
5
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| tpInsc | Gerar conforme o cadastro da Filial 1- CNPJ 2- CPF |
| nrInsc | CNPJ/CPF da Filial |

3novaValidade

## novaValidade

xmlnovaValidade
str1234
str1234
]]>

### Origem de dados

| Elemento do XML | Origem |
| --- | --- |
| iniValid | Campo "Início do Período" do Cadastro do Evento |
| fimValid | Campo "Fim do Período" do Cadastro do Evento |

# Processos

A integração com a RFB será realizada através dos WS do TSS no qual o TOTVS Gestão fiscal irá enviar os Eventos e o TSS se encarregará da assinatura dos XML, montagem dos lotes e comunicação com a RFB. Basicamente toda a integração com o TSS ocorrerá através dos processos "Transmitir" e "Consultar". Ambos os processos devem ser disponibilizados na lista de processos de cada Evento e, também, na lista de processos da visão dos menus "Eventos Cadastrais" e "Eventos Periódicos" podendo ser executados para um ou vários Eventos simultaneamente.

Serviços do TSS

Os detalhes dos serviços do TSS devem ser consultados na especificação de integração com o TSS.

## Transmitir

Este processo irá transmitir o Evento do ERP para a RFB através do TSS. O processo deverá permitir a execução por agendamento de Job de forma que seja capaz de identificar Eventos com status "Não transmitido" e "Alterado" enviando-os ao TSS de forma autônoma.

### Montar xml

Deverá ser montado um xml para cada Evento conforme o layout e origem de dados do mesmo. No caso de erros ao montar o xml dos Eventos os mesmos devem ser gravados com Status de "Inconsistente", registrado histórico com os detalhes e apresentado no log para o usuário.

DICA

Para fins de geração do XML observar o comportamento do process "Gerar Eventos Periódicos" no documento de especificação de Eventos Periódicos e se possível implementar da mesma forma.

### Configurar TSS

A configuração será realizada somente se existirem xmls gerados para enviar ao TSS. O TSS deverá ser configurado conforme consta na especificação de integração com o TSS.

### Validar o xml

Com o xml gerado deverá ser realizada uma validação de schema através do serviço VALIDARSCHEMA do TSS.

Os Eventos que apresentarem erros devem ser gravados com Status de "Inconsistente", registrado histórico com os detalhes e apresentado no log para o usuário.

### Enviar ao TSS

Somente os Eventos que forem validados com sucesso podem ser enviados ao TSS através do serviço ENVIAREVENTOS.

Os Eventos que apresentarem erros devem ser gravados com Status de "Inconsistente" e os Eventos enviados com sucesso devem ser gravados com Status "Pendente". Ambos devem registrar histórico com os detalhes e apresentar no log para o usuário.

## Consultar

Este processo irá consultar no TSS o resultado da transmissão realizada para a RFB. O processo deverá permitir a execução por agendamento de Job de forma que seja capaz de identificar Eventos com status "Pendente" consultando-os no TSS de forma autônoma.

### Configurar TSS

O TSS deverá ser configurado conforme consta na especificação de integração com o TSS.

### Consultar no TSS

Consultar os Eventos no TSS através do serviço CONSULTAREVENTOS. Se for identificado que os Eventos ainda não possuem uma resposta da RFB o usuário deve ser informado e um registro no histórico deve ser gravado, mas os Status dos  Eventos não devem sofrer alterações. No caso da consulta ser realizada com sucesso o Status do Evento será alterado conforme o resultado obtido podendo ser "Autorizado" ou "Rejeitado", em ambos os casos um histórico deve ser gravado e no caso da rejeição ainda será necessário informar ao usuário o motivo da rejeição através de log.

# Anexos

## Histórico

Todos os Eventos devem armazenar um histórico com todas as mudanças que provocarem alteração de Status ou Erro nos processos, registrando as informações mais importantes do Evento somente para consulta. O histórico deve ser disponibilizado em forma de anexo no Cadastro do Evento.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
