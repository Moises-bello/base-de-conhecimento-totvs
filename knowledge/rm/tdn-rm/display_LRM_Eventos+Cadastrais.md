---
content_hash: 2b0111eeb4b259dc51b7ceb1a4a0a1ffb2f7711db369cc4c8cd53587714640ca
fetched_at: '2026-06-29T00:10:29.601417+00:00'
page_id: '517138584'
product: rm
source: tdn-rm
title: Eventos Cadastrais
type: documentation
url: https://tdn.totvs.com/display/LRM/Eventos+Cadastrais
version: 52
---

![](https://tdn.totvs.com/download/thumbnails/715830650/Retornar.png)
]]>#f5f5f5#363636noneR-1000 | R-1050 | R-1070

## **Conteúdo**

**2Conteúdo**

## **01. Inclusão**

Ao ser incluído, o Evento assume o Status de "Não transmitido".

O evento R-1000 também pode ser incluído [importando um arquivo XML](https://tdn.totvs.com/x/Y8H5Kg).

## **02. Edição**

Quando o Evento estiver com Status de "Não Transmitido", o status não é alterável. Quando o Evento estiver com o Status "Inconsistente" ou "Rejeitado", o Status é alterado para "Não Transmitido". Para qualquer outro status, o Evento assume o Status de "Alterado".

## **03. Exclusão**

O cadastro do Evento pode ser excluído somente quando status for "Não Transmitido", "Inconsistente" ou "Rejeitado". 

ATENÇÃO

Não confundir a Exclusão de cadastro com o Evento de Exclusão R-9000 da RFB.

## **04. Regras**

* Quando o Evento estiver com status de "Pendente" ou "Pendente Exclusão", todos os campos permanecem bloqueados para Edição, inclusive os campos nos cadastros de origem do Evento;
* Quando o Evento estiver com status de "Excluído", o mesmo é bloqueado para Edição, mas os campos de origem não são bloqueados;
* Nenhum histórico pode ser alterado, excluído ou incluído;
* Os campos **Identificador,** **Status,** **Tipo,** **Ambiente,** **Data da Última Transmissão, Número do Protocolo, XML de envio, XML de retorno** não são editáveis;
* O **Evento Pai** só poderá ser alterado quando o Status for "Não Transmitido", "Inconsistente" ou "Rejeitado".

EventosleftR-1000R-1000

### R-1000

Ao acessar o menu EFD-REINF → “Eventos Cadastrais”, devem ser listados todos os Eventos do tipo R-1000. O cadastro é acionado somente pela Filial Matriz ou Filial SCP. Os campos seguem o padrão de estrutura definidos para os Eventos da EFD-REINF.

A inclusão do registro R-1000 é realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo:

* **Tipo:** é preenchido com o código do evento R-1000 e não será editável;
* **Início do Período:**é informado a data de início da vigência da EFD-REINF ou deste Evento. Quando o evento estiver com status de Não Transmitido, Autorizado, Rejeitado, Alterado ou Inconsistente é possível alterar a data final do R-1000;
* **Código da Filial:** não é editável.
R-1050R-1050

### R-1050

O Evento R-1050 é um anexo ao Evento R-1000. A inclusão do registro R-1050 é realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo:

* **Tipo:** é preenchido com o código do evento R-1050 e não é editável.

#### Validações

* **Código da Filial:** não é editável;
* **Código da Filial SCP**: é informado de acordo com a Filial SCP necessária. Não é possível cadastrar dois eventos R-1050 que possuam a mesma Filial SCP para a mesma Filial e Evento R-1000;
* Os campos **Início do Período** e **Fim do Período** são compreendidos no inicio e fim do período do R-1000 associado.

Observação

O Evento R-1050 pode ser criado em qualquer versão, porém, **apenas será transmitido a partir da versão 2.1.01**.

R-1070R-1070R-1070

### R-1070

O Evento R-1070 é um anexo ao Evento R-1000. A inclusão do registro R-1070 é realizada conforme a estrutura padrão dos eventos da EFD-REINF, porém com os detalhes abaixo:

* **Tipo:** é preenchido com o código do evento R-1070 e não é editável;

#### Validações

* Cada Evento tem somente um processo associado;
* O Processo Judicial só é editado quando o Evento estiver com o Status "Não Transmitido", "Inconsistente" ou "Rejeitado";
* Os campos **Início do Período** e **Fim do Período** são compreendidos no inicio e fim do período do R-1000 associado.

## **05. Transmitir**

Este processo irá transmitir o Evento do ERP para a RFB através do TSS.

Será montado um xml para cada Evento conforme o layout e origem de dados. No caso de erros ao montar o xml dos Eventos, eles serão gravados com Status de "Inconsistente", registrado no histórico com os detalhes e apresentado no log.

Transmissão e consultaleftR-1000R-1000R-1000

### Transmissão e Consulta R-1000

Acessar a tela de Eventos Cadastrais em "Obrigações Acessórias > SPED > EFD Reinf > Eventos Cadastrais".  
Selecione o evento R-1000 e execute o processo de Transmissão, ao assumir o Status de pendente o mesmo pode ser consultado.   
  
Para executar a transmissão do evento R-1000 devem ser seguidos os passos abaixo:

* Efetuar parametrização do TSS e Certificado.
* Acessar tela de eventos cadastrais.
* Selecionar Evento R-1000 que deseja transmitir.
* Executar processo de transmissão.

**Regras**

* Executar Processo "Atualizar Responsável Técnico".
* A transmissão será executada para os seguintes Status: alterado, inconsistente, não transmitido e rejeitado.
* Para os Status inconsistente, não transmitido e rejeitado será gerado o grupo <Inclusão>.
* Para os Status Alterado, será gerado o grupo <Alteração>.
R-1050R-1050R-1050

### Transmissão e Consulta R-1050

Acessar a tela de Eventos Cadastrais em "Obrigações Acessórias > SPED > EFD Reinf > Eventos Cadastrais" - "Menu anexos > R-1050".  
No anexo R-1050 estão disponíveis os processos de Transmissão e Consulta.  
Selecione os eventos desejados e execute o processo de Transmissão, ao assumir o Status de pendente os mesmos podem ser consultados.

Para executar a transmissão do evento R-1050 devem ser seguidos os passos abaixo:

* TSS e Certificado parametrizados (mesma parametrização do R-1000).
* Acessar tela de eventos cadastrais > Anexos > R-1050.
* Selecionar Evento R-1050 que deseja transmitir, caso não seja selecionado o processo será executado para todos.
* Executar processo de transmissão.

**Regras**

* O evento deve ser cadastrado e transmitido quando houver informações de "**Filial SCP"** nos Eventos R-4010 e R-4020.
* Ao cadastrar o evento R-1050 é obrigatório informar “Filial do Tipo SCP".
* Para transmitir o evento R-1050 o evento R-1000 pai deverá estar autorizado.
* O evento será transmitido para os seguintes status: alterado, inconsistente, não transmitido e rejeitado.
* Para os Status inconsistente, não transmitido e rejeitado será gerado o grupo <Inclusão>.
* Para os Status Alterado, será gerado o grupo <Alteração>.
R-1070R-1070R-1070

### Transmissão e Consulta R-1070

Acessar a tela de Eventos Cadastrais em "Obrigações Acessórias > SPED > EFD Reinf > Eventos Cadastrais" - "Menu anexos > R-1070".  
No anexo R-1070 estão disponíveis os processos de Transmissão e Consulta.  
Selecione os eventos desejados e execute o processo de Transmissão, ao assumir o Status de pendente os mesmos podem ser consultados.

Para executar a transmissão do evento R-1070 devem ser seguidos os passos abaixo:

* TSS e Certificado parametrizados (mesma parametrização do R-1000).
* Acessar tela de eventos cadastrais > Anexos > R-1070.
* Selecionar Evento R-1070 que deseja transmitir, caso não seja selecionado o processo será executado para todos.
* Executar processo de transmissão.

**Regras**

* Para cadastrar o evento R-1070 é obrigatório informar o "Processo Judicial".
* Para transmitir o evento R-1070 o evento R-1000 pai deverá estar autorizado.
* O evento será transmitido para os seguintes status: alterado, inconsistente, não transmitido e rejeitado.
* Para os Status inconsistente, não transmitido e rejeitado será gerado o grupo <Inclusão>.
* Para os Status Alterado, será gerado o grupo <Alteração>.
ATENÇÃO

Caso o campo Ambiente do evento seja diferente do ambiente parametrizado em Integrações | TSS, não será possível Transmitir e Consultar eventos Cadastrais, nem Transmitir, Consultar e Gerar eventos periódicos.

## **06. Vídeo How To - Evento R-1000**

648432

## **07. Mapeamento de Campos**

0

## **08. Outras Documentações**



* [Permissão de Perfil do Usuário - Regras de validação do Evento da EFD-Reinf](https://tdn.totvs.com/pages/viewpage.action?pageId=668649871)
