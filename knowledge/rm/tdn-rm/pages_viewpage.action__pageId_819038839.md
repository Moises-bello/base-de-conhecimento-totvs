---
content_hash: dd6912e2da15674bb49995e64c69ad39e950eacc38f17e8a1190aa2a3ab2aca8
fetched_at: '2026-06-29T00:11:45.007644+00:00'
page_id: '819038839'
product: rm
source: tdn-rm
title: Envio de XML TISS para Operadora de Saúde
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819038839
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações**
3. **Processos**
   1. **Envio de Documentos**
4. **Arquivos XML**
5. **Histórico de Autorização**
6. **Anexos da Guia**
7. **Comunicação Internação/Alta**

itensVisão Geral

## **01. VISÃO GERAL**

Quando um paciente que possui convênio está sendo atendido, o hospital precisa entrar em contato com a operadora de saúde para consultar se o paciente está ativo, informar o procedimento executado, verificar se o mesmo é atendido pela operadora, entre outras situações.

Atualmente o sistema utiliza 5 serviços de comunicação com a operadora, que são:

* + **Solicitação de Elegibilidade**  
    Verifica com a operadora se o paciente está ativo, em dia, etc...
  + **Solicitação de Autorização**Verifica com a operadora se a mesma cobre determinado procedimento.
  + **Solicitação de Cancelamento da Guia**Solicita a operadora que determinada guia de solicitação de autorização seja cancelada.
  + **Solicitação de Status de Autorização**Determinados procedimentos não tem uma resposta imediata (autorizando ou não), ficando com status "Em análise".  
    Com isso é necessário utilizar este serviço para consultar se o item em análise já foi autorizado.
  + **Envio de documentos**Envia documentos complementares referente a guia, para justificar determinado procedimento por exemplo.
  + **Comunicação de Internação/Alta**  
    Envia a comunicação de Internação ou Alta do paciente para a operadora.
Configurações

## **02. CONFIGURAÇÕES**

Para que seja feita a comunicação com as operadoras de saúde, é necessário efetuar algumas configurações.

Acessar Cadastros > Faturamento > Condições Contratuais > editar o contrato do convênio.

Na tela de configurações, configurar a versão da TISS em Eletrônicos III > Geral I > TISS > Versão dos arquivos XML.

Ainda na aba Eletrônicos III, na aba Web Services, configurar as URLs de comunicação com o web service da operadora, e usuário e senha.

Na aba WS Config há algumas configurações adicionais, como o prefixo das tags do XML, e qual informação do prestador será utilizada, como seu código na operadora ou CNPJ.

Processos

## **03. PROCESSOS**

Para a utilização dos processos de comunicação com a operadora, é necessário gerar um atendimento.  
Acessar Atendimento > Recepção > Registro de Atendimento.

Para verificar a elegibilidade, deve-se acessar a aba Atendimento e preencher o código do usuário no convênio e a validae da carteira, e clicar no botão de verificação (ao lado do campo de código do usuário no convênio) ou ao sair do campo código do usuário no convênio ou ao salvar o atendimento.

Os demais processos ficam na aba Guia/Autorização, mas antes pode ser necessário informar os campos da aba Informações ANS - TISS

Em Guia/Autorização deve-se lançar uma guia, e depois disso, selecionar a mesma e clicar em processos.

Os processos somente ficam visíveis se as configurações mencionadas forem efetuadas corretamente, e de acordo com o status da guia.

Por exemplo, se a guia foi criada e ainda não enviada, podemos visualizar o processo de Solicitação Autorização.  
Se a guia já foi autorizada, poderemos visualizar o processo de Envio Documentos.  
Se a guia ficou com status "Em Análise", poderemos visualizar o processo Solicitar Status Autorização.

### Envio de Documentos

O envio de documentos fica localizado em Guia/Autoricação > Processos > Enviar Documentos

Um destaque para o processo de envio de documentos, pois este é o único processo até o momento que possui janela para interação.

Neste processo deve-se informar um ou mais arquivos, e se desejar uma observação para o mesmo.  
Os formatos de arquivos permitidos no momento são JPG, JPEG, PNG, TIFF e PDF.

Caso o processo não esteja visível, pode ser necessário revisar as configurações mencionadas no tópico "**2. Configurações**" e preencher a URL do webservice da operadora para o envio de documentos.

Pode ser necessário também reiniciar o host da aplicação após ajustar a configuração.

Arquivos XML

## **04. ARQUIVOS XML**

Atenção!

A partir da release na 12.1.2402 a configuração onde os arquivos XML são salvos mudou e os parâmetros onde eram informados os caminhos dos arquivos XML da TISS foram descontinuados, para saber mais sobre as mudanças, consultar nossa FAQ

Para cada processo da TISS, teremos uma pasta com os contendo os arquivos XMLs. 

Se dentro daquele processo houver um envio e retorno, novas pastas serão criadas para organizar os arquivos.

Histórico de Autorização

## **05. HISTÓRICO DE AUTORIZAÇÃO**

Os processos executados podem gerar algum log, contendo informações ou justificativas, como o motivo de determinado procedimento não ser autorizado, ou falha na comunicação com a operadora.

O mesmo pode ser visualizado editando algum registro das tela de guias.

Anexos da Guia

## **06. ANEXOS DA GUIA**

Ao utilizar o processo de envio de documentos, os arquivos enviados são salvos no sistema como anexos da guia.

Estes documentos podem ser visualizados acessando o item da guia e clicando no botão "Anexos da Guia".

Nesta tela é possível clicar no botão "Visualizar" (destacado na grid com a cor azul), que abrirá o arquivo no visualizador padrão do windows.

Também é possível clica no botão excluir, para excluir este arquivo **somente no sistema**, **sem efetuar qualquer comunicação com a operadora**.  
Este botão fica destacado em verde ou vermelho de acordo com o status do documento, onde:

* + Se verde é porque o mesmo não foi enviado para a operadora, assim considerando que é um arquivo ainda sem validade com a operadora.
  + Se vermelho, o arquivo já foi enviado para a operadora, e nesse caso não é recomendável excluir o arquivo.

No rodapé da tela há uma legenda explicando esta situação.

Caso o usuário tente excluir um item enviado para a operadora, exibirá uma mensagem de confirmação.

Comunicação Internação/Alta

## **07. COMUNICAÇÃO INTERNAÇAO E ALTA**

Disponível a partir da TISS 4.03

Este processo e suas funcionalidades só estão disponíveis a partir da **versão 4.03.00 da TISS** . Certifique-se de que seu sistema está atualizado.

O WebService de Comunicação de Internação/Alta segue o mesmo padrão de configuração dos demais WebServices já existentes no sistema. Caso necessite de apoio na configuração inicial, consulte o guia de *Configurações*.

## O que é este processo?

O processo de **Comunicação de Internação ou Alta** é responsável por notificar automaticamente (ou de forma manual) a operadora de convênio de saúde sobre a entrada (internação) ou saída (alta) de um paciente na instituição.

O processo é executado de forma **automática** pelo sistema assim que você finaliza o cadastro de um atendimento, desde que o campo de internação esteja devidamente preenchido.  
  
  
Caso precise reenviar ou executar o processo individualmente fora do fluxo padrão, você pode acioná-lo diretamente através do menu de Processos do atendimento.

## Auditoria de Envios

Para garantir que a operadora recebeu as informações corretamente, o sistema disponibiliza uma **Tela de Auditoria de Envio**. Nela, você pode verificar o status da transmissão e o retorno enviado pela operadora.
