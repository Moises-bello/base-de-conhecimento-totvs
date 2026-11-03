---
content_hash: 20374d6ca2911a61a2b6ab498b0d6f1a52353fd72929d24d91b70f44133d48e6
fetched_at: '2026-06-29T00:10:51.381940+00:00'
page_id: '567579774'
product: rm
source: tdn-rm
title: TOTVS Gestão Hospitalar > Integrações > Shift
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=567579774
version: 19
---

## **ÍNDICE**

1. **Visão Geral**
2. **Parâmetros**
   1. **Gerais**
   2. **Unidade**
3. **Uso**
   1. **Envio Pedido**
   2. **Recebimento do Resultado**
4. **Itens que são****integrados**
5. **PEP**

SumárioVisão Geral

## **01. VISÃO GERAL**

Esse documento explica como configurar e como funciona a integração do RM com o sistema Shift.

Parâmetros

## **02.** **PARÂMETROS**

## **a.** **Gerais**

Para acessar os parâmetros da integração shift acesse o menu: Ambiente > Parâmetros > Gestão Hospitalar

Continue selecionando Unidade Diagnostico:

E agora temos acesso a parametrização da integração SHIFT:

Os parâmetros a serem informados são:

* **Endereço do WS:** Endereço informado pela shift para a integração com o nosso cliente.
* **Tag de Integração**: Campo referente ao método RecebePedido da integração, campo integracaoField.
* **Usuário**: Usuário informado pela SHIFT.
* **Senha**: Senha informado pela SHIFT.
* **Tipo de Documento para anexar o resultado de exame**: É o tipo de arquivo que está sendo importado como resultado, fica salvo na tabela de anexos do RM.
* **Integração única por pedido**: Essa parametrização tem que estar marcada para que a integração da shift seja ativada no sistema. No caso de não estar marcado o botão de finalizar não é exibido.

## **b.** **Unidade**

Para acessar os parâmetros da unidade acesse o menu: Cadastro > Unidade de Atendimento

Ao selecionar a unidade vá na aba de integrações e na parametrização de laboratório informe a integração Shift

Uso

## **03.** **USO**

## **a.** **Envio De Pedido**

Ao cadastrar um pedido com a unidade parametrizada para integração shift, após cadastrar o exame o botão de finalizar fica disponível para fazer a integração. Ao clicar em finalizar é feito o envio do pedido para a SHIFT. Após o envio e recebimento pela Shift, o status de integração do pedido é alterado para "Processado" e é gerado um registro no log de integrações (Utilitários => Integração Monitor);

**Observações:**

* Ao enviar o pedido de exame para integração shift, tambem é enviado o código da unidade de atendimento do paciente (no xml, a tag "PostoOrigem") seguindo a seguinte regra: Se o paciente estiver em um leito, será enviado o codigo da unidade de atendimento onde o leito se encontra, se não possuir um leito será enviado o codigo da unidade de atendimento do prontuário. 
  + Se no ambiente da shift não estiver "cadastrado" o codigo da unidade de atendimento será apresentado o seguinte erro: "Erro integração Shift: Erro no Web Service Shfit:ERRO #5001: DE/PARA da unidade de coleta cliente XX não cadastrado ou inativo", XX corresponde ao codigo da unidade enviado na tag "PostoOrigem";

## **b.** **Recebimento de Resultado**

O recebimento do resultado é feito pelo con-conector acessando o wsdl como no exemplo: **[http://localhost:8051/wsSau/mex?wsdl](http://bhn050104627:8051/wsSau/mex?wsdl).** A informação do o localhost é o servidor aonde a aplicação do RM está instalado e o 8051 é a porta configurada no httpport da instalação do RM. Com o wsdl pode-se utilizar a ferramenta como o SOAP-ui para ter acesso ao método que recebe o resultado:

 

Segue um exemplo de um xml de teste para ser importado o resultado.

400

## **b.** **Cancelamento**

* O processo de cancelamento da Shift segue o mesmo processo de cancelamento de exame ou pedido de exame, ao solicitar o cancelamento é enviado para Shift o exame para cancelamento, se a integração Shift retornar a confirmação do cancelamento com sucesso é realizado o cancelamento do exame no RM, caso contrário o usuário é notificado.

### Nova forma de manipulação de arquivos

Conforme estipulado na documentação , o pdf de recebimento de resultado integrado a partir do XML acima será alocado na pasta obedecendo o seguinte formato:

*"FileServerPath"\Saude\"Coligada\_X"\Filial\_0\Shift\Processado*

Observações:

* O "FileServerPath" pode ser configurado no host. Mais informações: ;
* A "Coligada\_X" é dinâmica conforme a que o usuário estiver utilizando. Exemplo: Coligada\_X será substituido por Coligada\_1 ou Coligada\_2 de acordo com o codigo da coligada configurada no usuário;
* A gravação do arquivo em pasta só ocorrerá se o sistema estiver configurado para salvar o arquivo em pasta, caso contrário será gravado no banco de dados.
  + Se o arquivo for salvo em banco de dados. Na tabela SZARQUIVO e na coluna NOMEARQUIVO será gravado apenas com o nome do arquivo e o conteudo do arquivo será gravado na coluna ARQUIVO;
  + Se o arquivo for salvo em disco. Na tabela SZARQUIVO e na coluna NOMEARQUIVO será gravado o nome da pasta e nome do arquivo, o arquivo será salvo na pasta "...\Processado" (Esta gravação é necessária para identificar onde o arquivo se encontra) e na coluna ARQUIVO será gravado nulo;
Itens Integrados

## **04.** **ITENS QUE SÃO INTEGRADOS**

Abaixo segue uma tabela com todos os itens do RM que são integrados com a Shift.

| Dado do RM | Envio/Recebimento | Observações |
| --- | --- | --- |
| Unidade de Atendimento | Envio | É enviada a Unidade de atendimento do leito caso o paciente seja atendimento interno. E a unidade do atendimento caso seja atendimento externo. |

PEP

## **05.** **PEP**

O PEP também contempla a integração da SHIFT, em qualquer tela que é possível solicitar pedidos de exame. O cancelamento funciona da mesma forma nas telas que é possível cancelar o pedido de exame.

##
