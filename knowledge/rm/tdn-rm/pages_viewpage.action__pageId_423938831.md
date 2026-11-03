---
content_hash: 8bf21cfdb11e0365c3f9db90dc9559302c5539ba2b089ab8d8f300d2fb5b401f
fetched_at: '2026-06-29T00:09:29.191651+00:00'
page_id: '423938831'
product: rm
source: tdn-rm
title: Parametrização do Envio de MDF-e via TSS 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938831
version: 3
---

Para parametrizar um movimento de MDF-e, deve-se levar em consideração a "Etapa 5 - TOTVS Colaboração" como "Versão Totvs Colaboração" a opção 1.0 e os dados da Filial, onde se parametriza o Certificado Digital para a integração do TSS e a versão do layout e evento que é 3.00. A parametrização da filial deverá ser acessada através do seguinte caminho: Ambiente | Parâmetros |Gestão de estoque, compras e faturamento | Integração | Fiscal | Dados Fiscais.  
Para parametrizar o movimento do tipo 2, dever ser acessado o seguinte caminho: Ambiente | Parâmetros |Gestão de estoque, compras e faturamento | Vendas | Faturamento.

* O movimento deverá ser do tipo 2.2.xx;
* O movimento deve ser parametrizado para acessar "Coleta de Entrega", "CTRC Saída", "CT-e";
* A etapa "Fis - Conhecimento de Transporte" deverá estar configurada, onde o campo Tipo de Operação esteja definido como "Emitir MDF-e";
* Definido para Editar os dados da placa do veículo;
* Os "Campos Complementares" deve estar habilitado para receber a informação do percurso (caso o percurso seja interestadual não contendo uma divisa de estados);

Na inclusão do movimento na aba CT-e além motorista é exibido o seguro de carga.   
Na aba CTRC Saída será exibida a aba Carga Perigosa sempre que o tipo de documento associado for de NF-e ou CT-e e será possível incluir n registros para cada documento associado.   
O carga perigosa conterá todos os campos do CT-e, exceto o campo Ponto de Fulgor.  
Também no CTRC Saída a aba CIOT será exibida.   
Quando o tipo de documento associado for um CT-e e se o mesmo tiver CIOT preenchido, os campos serão exibidos automaticamente preenchidos.   
Se não, é possível preencher seus campos (Chave de acesso, CPF/CPNJ do Contratante, CIOT do CT-e) manualmente, sendo que o CIOT não é obrigatório.   
Quando o tipo de documento associado for uma NF-e também será exibida a aba CIOT e poderá ser preenchido o CPF/CPNJ do Contratante caso necessário.  
Ainda na inclusão do movimento na aba Transporte | Identificação, o campo Tipo de Transportador possui três opções de preenchimento:

* Prestador de Serviço de Transporte;
* Transportador de Carga Própria ou;
* Transportador que emitirá CT-e globalizado.
* Devem ser observadas as seguintes situações:

* + Se tipo emitente informado for igual a Prestador de Serviço de Transporte, o CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador deverá ser diferente de TAC;
  + Se tipo emitente informado for igual a Transportador de Carga Própria e CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador não deverá ser preenchida;
  + Se tipo emitente informado for igual a Transportador de Carga Própria e CNPJ do proprietário do veículo for informado diferente do CNPJ do Emitente do MDF-e: A informação do tipo de transportador deverá ser preenchida com TAC.
  + Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte ou Transportador que emitirá CT-e Globalizado: Todos os campos do grupo de informações do seguro da carga deve ser obrigatoriamente informados.
  + Se o tipo de emitente informando for igual a Transportador que emitirá CT-e Globalizado: O tipo de documento preenchido na aba CTRC Saída não pode ser CT-e.
  + Se modal Rodoviário e Tipo Emitente for igual a Prestador de Serviço de Transporte ou Transportador que emitirá CT-e Globalizado devem ser preenchidos os campos: Responsável pela Geração do CIOT ou Responsável pelo pagamento do Vale Pedágio, na aba CTRC Saída.

Em Cadastros | Tabelas Auxiliares | Seguradora é realizado o cadastro da seguradora pra informar no MDF-e. Esse cadastro deve conter o CNPJ e Nome da Seguradora. O mesmo será utilizado na aba CT-e do movimento de MDF-e, onde permite a busca das seguradoras cadastradas.

Maiores Informações

* # [MDF-e Layout 3.0](http://tdn.totvs.com/display/LRM/MDF-e+Layout+3.0)
* [Parametrizar tipo de movimento para emissão de MDF-e](http://tdn.totvs.com.br/display/public/LRM/MDFE0003_Parametrizar_tipo_de_movimento_para_emissao_de_MDF-e)
