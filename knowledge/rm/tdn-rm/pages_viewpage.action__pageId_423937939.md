---
content_hash: a13669d666fa1c958d212f69453edb4de474bcb8b59aba6301c56a6508d9af4b
fetched_at: '2026-06-29T00:09:24.506398+00:00'
page_id: '423937939'
product: rm
source: tdn-rm
title: Parametrização do Envio de MDF-e via Client Neogrid
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423937939
version: 5
---

Para parametrizar um movimento de MDF-e, deve-se levar em consideração os dados da Filial, configurando também a "Etapa 5 - TOTVS Colaboração" como "Versão TOTVS Colaboração" a opção 2.0 e também deverá ser definido o diretório da instalação do Client Neogrid para haja integração entre o Client e o sistema. A filial a ser configurada nos parâmetros por filial deverá conter:

* Um usuário e senha TOTVS Colaboração;
* O "Tipo Documento Integração TOTVS Colaboração" deverá estar marcado para "Envio MDF-e" e "Recebimento MDF-e";
* Ambiente "Produção" para o envio oficial ou ambiente "Homologação" para testes;
* A versão do MDF-e (layout e envio) deve ser 3.00.

Essa parametrização deverá ser acessada através do seguinte caminho: Ambiente | Parâmetros |Gestão de estoque, compras e faturamento | Integração | Fiscal | Dados Fiscais.  
Para parametrizar o movimento do tipo 2, dever ser acessado o seguinte caminho: Ambiente | Parâmetros |Gestão de estoque, compras e faturamento | Vendas | Faturamento.

* O movimento deverá ser do tipo 2.2.xx;
* O movimento deve ser parametrizado para acessar "Coleta de Entrega", "CTRC Saída", "CT-e";
* A etapa "Fis - Conhecimento de Transporte" deverá estar configurada, onde o campo Tipo de Operação esteja definido como "Emitir MDF-e";
* Definido para Editar os dados da placa do veículo;
* Os "Campos Complementares" deve estar habilitado para receber a informação do percurso (caso o percurso seja interestadual não contendo uma divisa de estados).

Na inclusão do movimento na aba CT-e além motorista é exibido o seguro de carga. Na aba CTRC Saída será exibida a aba Carga Perigosa sempre que o tipo de documento associado for de NF-e ou CT-e e será possível incluir um registro para cada documento associado.   
O carga perigosa conterá todos os campos do CT-e, exceto o campo Ponto de Fulgor. Também no CTRC Saída a aba CIOT será exibida.   
Quando o tipo de documento associado for um CT-e e se o mesmo tiver CIOT preenchido, os campos serão exibidos automaticamente preenchidos.   
Se não, é possível preencher seus campos (Chave de acesso, CPF/CPNJ do Contratante, CIOT do CT-e) manualmente, sendo que o CIOT não é obrigatório.   
Quando o tipo de documento associado for uma NF-e também será exibida a aba CIOT e poderá ser preenchido o CPF/CPNJ do Contratante caso necessário.  
Ainda na inclusão do movimento na aba Transporte, Identificação há o campo Tipo de Transportador e seu preenchimento ou não ocorre quando:

* Se tipo emitente informado for igual a Prestador de Serviço de Transporte, CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador deverá ser diferente de TAC;
* Se tipo emitente informado for igual a Transportador de Carga Própria e CNPJ do proprietário do veículo não for informado ou for igual ao CNPJ do Emitente do MDF-e: A informação do tipo de transportador não deverá ser preenchida;
* Se tipo emitente informado for igual a Transportador de Carga Própria e CNPJ do proprietário do veículo for informado diferente do CNPJ do Emitente do MDF-e: A informação do tipo de transportador deverá ser preenchida com TAC.

Em Cadastros | Tabelas Auxiliares | Seguradora é realizado o cadastro da seguradora pra informar no MDF-e. Esse cadastro deve conter o CNPJ e Nome da Seguradora. O mesmo será utilizado na aba CT-e do movimento de MDF-e, onde permite a busca das seguradoras cadastradas.

Informações Adicionais

* [Parametrização do Envio de MDF-e via TSS](http://Parametrização do Envio de MDF-e via TSS)
* [MDF-e 3.00](http://tdn.totvs.com/display/LRM/MDF-e+Layout+3.0)
