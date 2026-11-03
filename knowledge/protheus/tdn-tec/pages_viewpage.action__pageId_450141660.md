---
content_hash: ded140fb5495bafd2e573834e3eb8618b59596220f73dfe8a660d972259b1d6e
fetched_at: '2026-07-02T19:24:23.440502+00:00'
page_id: '450141660'
product: protheus
source: tdn-tec
title: Seção [BTMonitorAppD] - Chave LogOutDir
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=450141660
version: 3
---

Define o diretório base onde será criado o diretório específico para os logs do Agent da AppDynamics.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| vazio (Padrão) | Define como vazio o diretório base e causa um erro, encerrando o AppServer. |
| <diretório\_relativo\_válido> | Define como <diretório\_relativo\_válido> o diretório relativo base onde será criado o diretório específico para os logs do Agent da AppDynamics. |
| <diretório\_absoluto\_válido> | Define como <diretório\_absoluto\_válido> o diretório absoluto base onde será criado o diretório específico para os logs do Agent da AppDynamics. |

## Observações

* Caso o diretório base fornecido seja vazio, o AppServer será encerrado com um erro, indicando a ausência da configuração para esta chave;
* Caso o diretório base fornecido seja relativo, este será criado e/ou usado a partir do diretório onde o binário do AppServer é executado e, dentro daquele, será criado o diretório específico;
* Caso o diretório base fornecido seja absoluto, este será criado e/ou usado e, dentro deste, será criado o diretório específico;
* O processo executando o AppServer deverá ter, no diretório base fornecido, as permissão necessárias para criar diretórios, listar arquivos e escrever arquivos;
* Caso o diretório fornecido não seja vazio mas seja inválido, o diretório específico será criado no diretório /tmp/appd no Linux ou C:\tmp\appd no Windows;
* O diretório específico será criado a partir do diretório base, um por nó da aplicação monitorada pelo AppDynamics, no seguinte formato:

  -]]>
* Onde as partes do nome do diretório específico são:

  | Parte do nome do diretório específico | Origem |
  | --- | --- |
  | ``` <nome_da_máquina> ``` | Nome da máquina (computador) |
  | ``` <número_da_porta_com_zeros_à_esquerda> ``` | O primeiro dos seguintes valores de chave:  ou [Seção [TCP] - Chave Port](http://tdninterno.totvs.com/pages/viewpage.action?pageId=135496000), preenchido com zeros à esquerda até 5 posições,  ou [Seção [Webapp] - Chave Port](http://tdninterno.totvs.com/pages/viewpage.action?pageId=307834845), preenchido com zeros à esquerda até 5 posições,  ou `00000`, cinco zeros, indicando ausência de valor de porta adequado. |

## Exemplos

* Caso o **diretório base** fornecido seja **relativo** e igual a **SomeRelativeDir**, o AppServer seja executado a partir de **C:\totvs\appserver**, o nome da máquina seja **SomeServerMachineName** e a **porta TCP** seja **1234**, define o diretório específico como **C:\totvs\appserver\SomeRelativeDir\SomeServerMachineName-01234**:
* Caso o **diretório base** fornecido seja **absoluto** e igual a **C:\SomeAbsoluteDir**, o nome da máquina seja **SomeServerMachineName** e a **porta TCP** seja **1234**, define o diretório específico como **C:\SomeAbsoluteDir****\SomeServerMachineName-01234**:

## Abrangência

Builds [17.3.0.8](http://tdn.totvs.com/display/tec/Application+Server+-+17.3.0.8).

## Veja também
