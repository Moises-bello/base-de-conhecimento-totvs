---
article_id: 360018166992
category: Gestão de Transportes (TMS)
content_hash: 4031b4149b11b8f5feaf7686b2bd37de395e48db4566d00d14d98aea52bcc048
fetched_at: '2026-06-28T22:45:33.493780+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: 'Logística - Linha Protheus - TMS - Viagem rodoviária - Serviços e Tipos '
type: support-article
updated_at: '2022-04-27T11:36:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018166992-Log%C3%ADstica-Linha-Protheus-TMS-Viagem-rodovi%C3%A1ria-Servi%C3%A7os-e-Tipos
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:04:18 min  
  
Dúvida**Quais os tipos de viagens e processos relacionado a elas no **SIGATMS**?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) -  Todas as versões  
  
**Solução**No **TMS** existe três Serviços de viagens com os tipos abaixo  
  
**Coleta -**A coleta é um serviço regular de transporte entre um terminal de frete e as instalações do consignatário, ou seja, é o processo para efetuar a retirada das mercadorias no endereço determinado pelo cliente solicitante.    
Os tipos de viagens são:

* **Normal -**Exige que sejam relacionados os documentos de transporte - **CT-es** ou notas fiscais de serviço. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e **Entrega**.
* **Planejada -**É possível cadastrar uma viagem com data futura e alocar motoristas/veículos que realizarão a viagem. Neste momento, os motoristas/veículos não precisam estar liberados. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e **Entrega**.
* **Socorro** - Assim como na viagem do tipo vazia, não é necessário relacionar documentos. Essa viagem é utilizada para o trânsito de veículos sem carga, porém, deve ser registrada para o cálculo dos custos de transporte e para a liberação do veículo/motorista quando existir controle de portaria - **parâmetro MV\_CONTVEI = T**.  A diferença da viagem socorro entre os outros tipos de viagem é que o Sistema, por meio da opção **Complemento de Viagem**, não valida a inclusão de um veículo do tipo **Cavalo**, permitindo a inclusão sem o tipo **Reboque**. Nos outros tipos de viagem, não é permitida inclusão do tipo **Cavalo sem o** **Reboque**. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e **Entrega**.

**Transporte -**A viagem de transporte rodoviário é utilizada para efetuar a transferência de cargas entre as transportadoras que possuem filiais.   
  
**Entrega -**A entrega é o processo utilizado para efetuar a distribuição das mercadorias na região destino.  
  
Para os serviços de Transporte e Entrega os tipos de viagens são:

* **Normal -**Exige que sejam relacionados os documentos de transporte - **CTRCs** ou notas fiscais de serviço. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e **Entrega**.
* **Vazia -**Não é necessário relacionar documentos. A viagem vazia é utilizada para trânsito de veículos sem carga, porém, deve ser registrada para o cálculo dos custos de transporte e para a liberação do veículo/motorista quando existir controle de portaria - parâmetro **MV\_CONTVEI = T**. Este tipo de viagem pode ser utilizado em processos de **Transporte** e **Entrega**.
* **Planejada -**É possível cadastrar uma viagem com data futura e alocar motoristas/veículos que realizarão a viagem. Neste momento, os motoristas/veículos não precisam estar liberados. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e **Entrega**.
* **Socorro** - Assim como na viagem do tipo vazia, não é necessário relacionar documentos. Essa viagem é utilizada para o trânsito de veículos sem carga, porém, deve ser registrada para o cálculo dos custos de transporte e para a liberação do veículo/motorista quando existir controle de portaria - **parâmetro MV\_CONTVEI = T**. A diferença da viagem socorro entre os outros tipos de viagem é que o Sistema, por meio da opção Complemento de Viagem, não valida a inclusão de um veículo do tipo **Cavalo**, permitindo a inclusão sem o tipo **Reboque**. Nos outros tipos de viagem, não é permitida inclusão do tipo **Cavalo sem o Reboque**. Este tipo de viagem pode ser utilizado em processos de **Coleta**, **Transporte** e Entrega.
* **Redespacho -**Tipo utilizado para criar viagens com documentos indicados para redespacho. Este tipo de viagem pode ser utilizado em processos de **Entrega**.

**Glossário**  
**CT-e** - Conhecimento de transporte eletrônico  
**CTRC** - Conhecimento de transporte  
**SIGATMS** - Gestão de Transportes  
**TMS** - Gestão de transportes
