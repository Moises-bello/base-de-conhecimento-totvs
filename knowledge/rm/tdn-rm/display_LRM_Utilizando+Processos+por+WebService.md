---
content_hash: 7a78bd4cb0ef3b79d9ae40797ae51ab54e53d29584009bba5265f4a2aefca6b0
fetched_at: '2026-06-29T00:10:52.207079+00:00'
page_id: '571002138'
product: rm
source: tdn-rm
title: Utilizando Processos por WebService
type: documentation
url: https://tdn.totvs.com/display/LRM/Utilizando+Processos+por+WebService
version: 1
---

É possível pegar o XML dos processos do sistema para que sejam consumidos por WebService. Para isso é necessário primeiramente que o processo seja executado no sistema, em seguida, através dos Jobs que são criados será possível obter o XML, é de suma importância pegar o XML de um processo que foi executado sem erros.

1. Executar o processo que deseja obter o XML informando todos os parâmetros necessários.
2. Obter o XML do processo: [Como obter o XML de Parâmetros de Jobs](https://tdn.totvs.com/pages/viewpage.action?pageId=420544638).
3. Montar a estrutura de XML:

   Exemplo de Estrutura

   <soapenv:Envelope xmlns:soapenv="<http://schemas.xmlsoap.org/soap/envelope/>" xmlns:tot="<http://www.totvs.com/>">  
   <soapenv:Header/>  
   <soapenv:Body>  
   <tot:ExecuteWithXmlParams>  
   <!--Optional:-->  
   <tot:ProcessServerName>WebService(Nome classe Processo)</tot:ProcessServerName>  
   <!--Optional:-->  
   <tot:strXmlParams><![CDATA[Insira aqui o XML]]>  
   </tot:strXmlParams>  
   </tot:ExecuteWithXmlParams>  
   </soapenv:Body>  
   </soapenv:Envelope>
4. Após criar a estrutura é importante adequar os parâmetros para a execução principalmente os campos que são Auto incrementos, por exemplo, ao pegar o XML de um processo de Reajuste de venda existe o campo **CodReajuste** que é um identificador único criado pelo sistema de forma incremental, para que o sistema continue criando corretamente o valor da TAG deve ser -1. Além disso os demais campos precisam ser atualizados de acordo com o proposito da execução, seguindo o exemplo do Reajuste seria preciso também ir atualizando a data de Reajuste para o mês desejado . A seguir uma imagem ilustrando a alteração de 2 TAGS do XML o **CodReajuste** e **DataReajuste**:
5. Em seguida deve ser utilizado o SoapUI.
6. Ao criar um novo Projeto o WSDL que deve ser utilizado é o : **Process(wsProcess)**Este serviço disponibiliza métodos de manipulação de processos RM.
7. Após criar o processo o serviço a ser utilizado é ExecuteWithXmlParams.
8. Ao abrir a Resquest, caso seja utilizado o Exemplo do inicio do documento, todo o conteúdo da Request pode ser substituído, se optar reaproveitar os dados da Request a estrutura deve ficar no mesmo padrão do exemplo.
9. Apos preencher as informações da Request(XML, Autenticação) execute o serviço.
