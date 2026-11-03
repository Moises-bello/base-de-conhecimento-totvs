---
content_hash: d9ce9710ef31ec51bd9cdabf36e5b2bbd8ec8708c2c104ed80f69dd9d43edbc4
fetched_at: '2026-06-29T00:10:06.604437+00:00'
page_id: '452719320'
product: rm
source: tdn-rm
title: Cadastro NIS
type: documentation
url: https://tdn.totvs.com/display/LRM/Cadastro+NIS
version: 2
---

Modulo que permite gerar o relatório no padrão definido pela Caixa Econômica Federal (CEF) para o cadastramento do trabalhador em lote.   
 Para maior detalhamento do conteúdo do arquivo, acessar: [{+}](http://www.caixa.gov.br/pj/pj_comercial/mp/pis/cadastro_nis_lote.asp)<http://www.caixa.gov.br/pj/pj_comercial/mp/pis/cadastro_nis_lote.asp#+>  
    
    
 **Executando o processo de Geração de relatório de NIS/PIS em lote**  
   
 Para realizar o processo de Geração de relatório de NIS/PIS em lote, o usuário deve acessar: Folha Mensal | Relatórios | Relatórios da Folha | Cadastro NIS, selecionar o Layout do Gerador de Saídas – NIS em arquivo, selecionar o conceito de classificação para o tipo de logradouro (De/Para), selecionar um caminho onde o arquivo será salvo, informar o CPF do responsável pelo cadastramento, e selecionar o Formato do nome do arquivo, avançar a etapa.  
 Nesta etapa, selecionar o(s) funcionário(s), marcar o tipo de arquivo e o tipo da remessa que deseja gerar, informar a versão do arquivo, avançar a etapa.  
 Nesta etapa, deverá selecionar a(s) coligada(s), avançar etapa.  
 Nesta etapa, executar o processo.  
    
    
 **Campos**  
    
   
 **Layout Gerador de Saídas – NIS em arquivo**  
    
 Campo obrigatório, onde o usuário informa o layout para geração de relatório de NIS/PIS em arquivo.  
 A importação do layout, disponibilizado pela Totvs, deverá ser feita pelo módulo Integração, na aba integração, opção Gerador de Saídas. Para mais informações de como executar o processo de importação de layouts, acesse o Link Abaixo Gerador de Saídas.  
    
    
 **Conceito de Classificação para Tipo de Logradouro**  
    
 Campo obrigatório, onde o usuário deve informar o conceito de logradouro que contém o conjunto de tipos de logradouros permitidos pela CEF.   
 A CEF disponibiliza uma tabela de classificação para tipo logradouro que deve ser informada no relatório. O sistema disponibiliza a funcionalidade para atender o cadastrado da classificação de Logradouros, no cadastro de endereços, na aba do eSocial.  
 Para realizar o cadastro de classificação tipo de Logradouro, para que seja retornado no relatório de geração do NIS/PIS em lote de acordo com a tabela de tipos de logradouros permitidos pela CEF, o usuário deve executar os passos abaixo:  
    
 ·          **Classificação de Tipo Rua**  
    
 Acessar: eSocial (beta) | Cadastros | Endereços | Classificação de Logradouros, clicar em novo. O sistema irá abrir uma interface para inserir um novo registro. O usuário deve informar um identificador e uma descrição, clicar em salvar.   
    
 ·          **Codificação de tipo de Rua**  
    
 Acessar: eSocial (beta) | Cadastros | Endereços | Logradouros | Anexos | Codificação de Tipo de Rua. No anexo que abrir, clicar em novo. O sistema irá abrir uma interface para inserir um novo registro. O usuário deve informar o código da classificação, cadastrado na aba classificação de tipo Rua e informar o código do tipo logradouro de acordo com tabela disponibilizada pela CEF, clicar em salvar.  
    
 **Observação**  
    
 ·          O identificador que for cadastrado na classificação de tipo rua que será informado no processo de geração de relatório de NIS/PIS em lote, no campo 'Conceito de classificação para Tipo de Logradouro'.  
 ·          O processo irá atribuir o código do tipo de logradouro de acordo com o tipo rua do cadastro de endereço do funcionário.   
 ·          É de responsabilidade do usuário cadastrar a classificação e codificação dos tipos de logradouros no sistema.   
 ·          O processo de cadastro de codificação dos tipos de logradouros e de Geração de relatório de NIS/PIS em Lote não faz consistência do tipo cadastrado pelo usuário pelos tipos permitidos pela CEF, retornando no arquivo sempre o código cadastrado pelo usuário.    
 ·          Caso algum tipo de rua não tenha o cadastro da codificação de tipo de rua, o sistema retorna uma mensagem de erro no processo de geração de relatório de NIS/PIS em lote.  
    
               
 **Localização dos arquivos**   
    
 Campo obrigatório, onde o usuário irá informar o destino do relatório gerado. Neste destino, será criado uma pasta com nome 'Coligada X', onde o X é o número da coligada.  
    
    
 **CPF do responsável pelo Cadastramento**  
    
 Campo obrigatório, onde será informado o CPF do responsável pelo cadastramento. Este campo, quando informado é inserido no registro referente ao campo no relatório.  
    
    
 **Formato Nome do Arquivo**  
    
 Campo obrigatório, onde o processo retorna opções de nomes de relatórios no formato aceitos pela CEF.   
    
    
 **Seleção de Funcionário**  
    
 Campo destinado para que o usuário possa selecionar um ou mais funcionários que terão registros informados no relatório de NIS/PIS em lote.  
    
 **Observação**  
    
 Nesta seleção não é possível selecionar um funcionário por Chapa, Filtro ou Fórmula de Seleção. Para usar estes filtros, deverá ser feito dentro dos parâmetros da coligada.  
    
    
 **Tipo de arquivo**  
    
 Campo obrigatório, onde o usuário informa o tipo de relatório que será gerado pelo processo de acordo com os layouts definidos pela CEF:   
    
 ·          **Simplificado**   
    
 Usado para os casos de envio de relatório diretamente pela empresa, com o conjunto de registros lógicos com a seguinte estrutura:  
    
 Header Geral  
 n Registros de detalhe, que varia de 0 a 99999999999  
 Trailer Geral  
    
 ·          **Completo**  
    
 Usado para os casos de envio de arquivo por Empresas com os dados segregados por filial ou Escritório de Contabilidade com dados de várias empresas distintas, contento um conjunto de registros lógicos com a seguinte estrutura:  
    
 Header Geral  
 Header Parcial  
 n Registros de detalhe, que varia de 0 a 99999999999  
 Trailer Parcial  
 Trailer Geral  
    
 Neste caso, a sequência 'header Parcial, n Registro de detalhe e Trailer Parcial', doravante denominada lote, poderá ocorrer várias vezes no arquivo e corresponderá aos dados de uma empresa.  
    
 **Observação**  
    
 Quando selecionar o tipo de arquivo 'Completo', o processo exibe a opção 'Tipo de Geração de Arquivo Completo', onde o usuário pode escolher se quer gerar o arquivo unificado ou por coligada.   
 Marcando a opção 'Unificado', o sistema gera em um único arquivo os registros dos funcionários de todas as coligadas selecionadas.   
 Marcando a opção 'Arquivo por Coligada', o sistema gera um relatório de NIS/PIS em lote por coligada.   
    
 **Tipo de remessa**  
    
 Campo obrigatório, onde o usuário informa o tipo de remessa que será gerada, de acordo com especificado pela CEF. Para este campo, são disponibilizadas as opções 'Original' e 'Retificação.  
 Esta informação é inserida no registro referente ao campo no relatório.  
    
    
 **Versão do arquivo**  
    
 Campo obrigatório, onde é informada a versão do arquivo gerado.  
 De acordo com CEF, uma nova versão de arquivo significa informação de novos dados. Poderá ser informada a mesma versão de arquivo anteriormente postados nos casos de retificação. Este campo começa com 0 e tem limite de 99 versões.  
    
    
 **Coligada**  
    
 Campo obrigatório, onde o usuário deve selecionar pelo menos uma coligada.   
    
 **Observação**  
    
 Nesta interface é possível selecionar funcionário por Chapa, Filtro ou Fórmula de seleção, quando o usuário edita os parâmetros da coligada e marca a opção 'Usar Parâmetros Específicos'.   
 Quando o usuário não marca o parâmetro 'Usar Parâmetros Específicos' nesta interface, o processo irá considerar o filtro global de Seleção de Funcionários para gerar o relatório de NIS/PIS em lote.  
    
    
 **Coligada Geral Arquivo Completo**  
    
 Campo obrigatório, onde o usuário informa o código da coligada que será usado para criação do diretório de armazenamento do relatório gerado, quando a geração do relatório de NIS/PIS em lote for completo e o Tipo de Geração de Arquivo Completo for o unificado.  
 Quando o Tipo de Geração de Arquivo Completo for por coligada, os arquivos serão gerados nos diretórios de cada coligada.
