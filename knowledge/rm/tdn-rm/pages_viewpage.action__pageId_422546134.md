---
content_hash: f804d267c9258c1ebcfe728dd121256c3f8fd9ab4292eb44f85c9446b42c2750
fetched_at: '2026-06-29T00:09:23.810885+00:00'
page_id: '422546134'
product: rm
source: tdn-rm
title: Integração TOTVS Gestão Fiscal X TAF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546134
version: 13
---

A integração com o TAF será feita através de web service [criado em sua instalação](http://tdn.totvs.com.br/pages/releaseview.action?pageId=331868191) . Para que esta integração ocorra os parâmetros específicos da integração deverão ser preenchidos. Eles estão localizados em  Parâmetros | TOTVS Gestão Fiscal | Processo 03.05 - Integração | 03.05.05 - TAF.  
**Servidor:**Onde o TAF está instalado (de onde o webservice da REINF é distribuído)

**Porta:** Porta na qual o webservice da REINF escuta

**Usuário:** O mesmo utilizado para login no TAF

**Senha:**A mesma utilizada para login no TAF

**Observações:**

A porta não é obrigatória pois a quando o TAF é utilizado como SmartClient esta informação pode estar implícita no endereço, portanto os parâmetros poderão ser informados nos formatos abaixo:

**Servidor**: http://SERVIDOR/rest  
**Porta**: XXXX

**Servidor**: SERVIDOR/rest (**Neste caso, o processo de envio acrescenta o http:// na frente do endereço. Quando se tratar de https este deve ser informado obrigatoriamente**.).  
**Porta**: XXXX

**Servidor**: https://SERVIDORSMARTCLIENT/rest/wstafst2   
**Porta**: SEM INFORMAÇÃO

Para que a integração dos dados sejam feitas com sucesso o campo Código da Filial em Sistemas Externos da aba Dados Adicionais do cadastro de Filiais deverá ser preenchido com o código atribuído ao [Complemento de Empresa do TAF](http://tdn.totvs.com.br/display/public/TAF/Complemento+de+Empresa+-+TAFA050+-+TAF+-+P12).  
Todas as informações integradas ao TAF serão armazenadas em tabela criada para este fim. Para que o usuário possa visualizá-las foi criada uma visão em Obrigações Acessórias | TAF | Integração RM X TAF.  
  
**Inclusão:** Por se tratar de uma visão não é possível a inclusão manual ou edição, os registros só serão abertos para visualização. A inclusão de registros nesta visão será feita através da execução de um layout específico que deverá ser previamente importado no  Gerador de Saídas. Quando executado o layout irá incluir as informações de integração para a coligada corrente e filial selecionada no processo.  
  
**Exclusão:** A exclusão está disponível a partir da versão 12.1.25.144, pode ser realizada independente do status do registro e não tem nenhum vínculo com os dados já integrados com o TAF. (Os dados são excluídos apenas no RM - Gestão Fiscal).   
  
Os registros gravados nesta visão poderão assumir alguns status de acordo com os processo executados neles.

1. Incluído: Status inicial do registro quando ele é gravado no banco de dados e ainda não foi integrado ao TAF.
2. Alterado: Registro pré-existente que foi gravado novamente após o registro do RM que o originou ter sofrido alguma alteração. O registro com este status ainda não foi integrado novamente.
3. Registro não integrado. Com erro.
4. Registro integrado com sucesso ao TAF.
5. Registro integrado via banco de dados.

Para cada operação executada com o registro será criado um registro de log que poderá ser visualizado acessando o anexo da visão.

**Processos relacionados à integração RM X TAF**

* Processo de Geração TAF Fiscal: Através deste processo o layout TAF será executado para a gravação dos dados que serão integrados .
* Integrar Registro ao TAF: Este processo irá enviar o/os registros selecionados para o [TAF através de web service.](http://tdn.totvs.com.br/pages/releaseview.action?pageId=331868191)  Após o envio o status do registro será alterado e será criado um registro em seu log.
* Buscar Status da Integração com o TAF: Após os [processos internos do TAF](http://tdn.totvs.com.br/display/public/TAF/Processamentos+-+TAFAINTEG+-+TAF+-+P12) de integração do TAF serem executados este processo irá buscar o resultado do processamento dos registros integrados.
* Contingência ao web service TAF: No caso de impossibilidade de uso do web service do TAF para a integração dos registros o usuário poderá fazer a integração banco a banco. Este processo consiste em gravar os registros previamente criados na visão de integração como TAF para uma tabela (TAFST2) que o TAF cria na base do RM quando o mesmo é configurado para integrar via banco com o RM. Após isto, acessando o TAF, os [processos de integração](http://tdn.totvs.com.br/pages/releaseview.action?pageId=270919411) devem ser executados normalmente como se os registros tivessem sido integrados via web service. Posteriormente o status destes registros poderá ser buscado do TAF normalmente.

***Observação:*** Alterações nos cadastros de log do cadastro de Filial, Dados Fiscais da Filial, Processo Judicial e Tributos Discutidos: Sempre que houver alteração nos cadastros que gerar registro de log, é necessário reintegrar esses dados com o TAF. Os dados só vão ser reintegrados quando houver LOG de alteração.  
Para que seja facilitada a integração dos dados foi criado um parâmetros na tela de geração da integração para que sejam carregados somente os lançamentos que possuem informação que será utilizada na geração da REINF. Marcando este checkbox serão selecionados somente lançamentos (para a geração do registro T013 e filhos) que possuam em algum de seus itens os tributos INSS, FUNRURAL ou Contribuição Previdenciária. Os registros relacionados ao T013 como os de Participantes e Produtos, por exemplo também serão gerados.

**Filtro de Lançamentos**

No processo de geração de registros, na tela de integração RM x TAF, foi incluído um filtro de lançamento fiscal:   
Nele é possível filtrar os registros para que gerem somente os referentes aos lançamentos filtrados, desde que o filtro não contenham parâmetros que tenham que ser informados posteriormente.  
Ao clicar no botão de filtro uma tela será exibida com os filtros já configurados na tela de lançamentos fiscais.  
***Importante:***O filtro de lançamentos funcionará em conjunto com a data inicial e final selecionada, assim como a filial. Ao executar o processo com filtro de lançamento, somente o lançamento filtrado e seus registros correspondentes (filhos) serão gerados.  
Para geração dos demais registros, é necessária a execução sem o filtro de lançamento.

Maiores Informações

* [EFD - REINF](http://tdn.totvs.com/display/public/LRM/EFD-REINF)
* [TAF - Pré-requisitos e download](http://tdn.totvs.com.br/pages/releaseview.action?pageId=274305742)
* [Instalação TAF](http://tdn.totvs.com.br/pages/releaseview.action?pageId=331868191)
* [Processos Internos de Integração do TAF](http://tdn.totvs.com.br/display/public/TAF/Processamentos+-+TAFAINTEG+-+TAF+-+P12)
* [Cadastro do TAF](http://tdn.totvs.com.br/pages/releaseview.action?pageId=240290238)
