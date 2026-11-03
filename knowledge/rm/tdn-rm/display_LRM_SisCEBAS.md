---
content_hash: 6103a8d7d3726dd6f672a15ac6c7a6ad60565219f14e42223a1e5b2a949e833a
fetched_at: '2026-06-29T00:09:34.139189+00:00'
page_id: '425459153'
product: rm
source: tdn-rm
title: SisCEBAS
type: documentation
url: https://tdn.totvs.com/display/LRM/SisCEBAS
version: 6
---

---

Os requerimentos de certificação originária e de renovação do Certificado de Entidade Beneficente de Assistência Social, regulamentados pela Lei n°12.101, de 27 de novembro de 2009, deverão ser protocolados nos Ministérios da Educação, da Saúde e do Desenvolvimento Social e Combate à Fome, conforme a área de atuação preponderante da entidade.

As entidades mantenedoras educacionais devem realizar o cadastramento exclusivamente em meio eletrônico por meio do Sistema de Certificação de Entidade Beneficente de Assistência Social na Área de Educação – SisCEBAS.

No SisCEBAS as entidades mantenedoras devem indicar, além de outras informações, a relação dos alunos bolsistas. Esta relação pode ser feita de forma manual, cadastrando um a um dos alunos bolsistas com suas respectivas informações, ou de forma automática, anexando um arquivo com a extensão .CSV que contenha estas informações.  
O TOTVS Educacional, disponibiliza a geração deste arquivo através do menu: Gestão | Ferramentas de Análise | Gerador de Saídas. Selecione o layout "Listagem de Bolsistas - SISCEBAS", acesse Processos | Geração de Saídas e preencha os dados dos Filtros para a sua geração.

O arquivo será composto por 8 colunas. Para cada aluno será gerada uma única linha, com os seguintes dados:  
**1-Nº de identificação no CENSO**: Código INEP do aluno (Caso o aluno ainda não possua o número, será gerado em branco)  **2-Nome do Bolsista**: Nome completo do Aluno bolsista **3-Data de nascimento**: Data de nascimento do Aluno bolsista **4-CPF do Bolsista**: O número do CPF do Aluno bolsista **5-Nome do Responsável Financeiro**: Nome do responsável financeiro do aluno bolsista **6-CPF do Responsável Financeiro**: O CPF do responsável financeiro do Aluno bolsista **7-Valor da Mensalidade**: Valor total dos serviços prestados \* **8-Valor da Bolsa no ano**: Valor total da bolsa no ano \*

No final do processo será gerado o arquivo SISCEBAS.CSV com o resultado das informações processadas. O sistema irá fornecer um caminho default para a geração do arquivo. Se necessário indique um novo caminho no servidor.

Estarão presentes no arquivo gerado, todos os alunos que tiverem alguma Bolsa\* (cancelada ou não) associada em seu contrato (cancelado ou não). O valor dos serviços\* (todos os serviços ou somente daqueles indicados no Filtro) presentes neste contrato, calculados através da 'Simulação' de valores, serão apresentados na 7ª coluna do arquivo gerado. A 8ª coluna do arquivo gerado será composta pelo somatório dos valores lançados a **débito** nas contas contábeis utilizadas para contabilizar os valores mensais das Bolsas, obtidos através da realização da contabilização dos contratos pelo regime de competência.

Na geração do arquivo, além do preenchimento das informações nos Filtros obrigatórios (Coligada, Filial, Conta de débito), pode-se utilizar outros Filtros para direcionar ainda mais a seleção dos dados que irão compor o arquivo e, quando não se informar valor para determinado Filtro, todos os registros serão buscados. Por exemplo, para buscar todos os códigos de contrato basta deixar o Filtro 'Código do Contrato' em branco.

O Filtro 'Código da Conta Débito' para indicação da conta contábil de débito é obrigatório. Para isto deve-se cadastrar previamente filtros internos com a indicação das devidas contas contábeis que recebem a contabilização mensal das referidas Bolsas presentes nos contratos dos alunos. Na confecção deste filtro é permitido utilizar o caracter '%' para a seleção das contas contábeis, desde que a expressão seja montada utilizando-se o operador 'LIKE' (Exemplo: Operador **LIKE**com o valor **2.1.2%** = indica que a seleção será para todas as contas contábeis que iniciam com o código 2.1.2). No Filtro 'Código do Período Letivo' pode-se utilizar também o caracter '%' para conseguir filtrar mais de um período letivo. (Exemplo: Períodos letivos 2016/1 e 2016/2. Para a seleção dos dois períodos letivos, pode-se indicar nesta situação = 2016%.   
Lembrando que se o Filtro ficar em branco indica que não haverá restrição na pesquisa.)   
   
**Atenção:** Para a geração deste arquivo o sistema trabalha com certa limitação, pois não há uma rastreabilidade direta entre a conta contábil e os itens contabilizados, como por exemplo, Bolsa, Serviço, Contrato. Portanto, cabe ao usuário informar no Filtro as contas contábeis corretas a serem consideradas, pois caso não sejam especificadas corretamente, o sistema poderá retornar valores que não são correspondentes à contabilização de Bolsa que é o objeto deste arquivo. (Exemplo: Indicação de uma determinada Bolsa e indicação de uma conta contábil que não corresponde à contabilização desta bolsa.)

Importante

* Para os contratos cancelados serão processadas somente informações das parcelas que tenham lançamentos financeiros gerados e que não estejam cancelados.
* Ressaltamos que durante o processo de geração do arquivo SisCebas poderão ser apresentadas mensagens de validação impossibilitando a simulação dos valores das parcelas, quando isso ocorrer nenhuma informação será gerada no arquivo. Neste caso deverá ser analisada a mensagem apresentada, proceder com o ajuste, e executar o processo novamente.

Observação:

O arquivo do layout de exportação do SisCEBAS ("Listagem de Bolsistas - SISCEBAS.TotvsGen") é disponibilizado juntamente com a instalação do RM  dentro da pasta  ObjetosGerenciais\Layout.

[Veja a dica de importação](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007794211-RM-BI-Categoria-em-layout-do-Gerador-de-Sa%C3%ADdas-)  
   
    Veja Também

---

**[CEBAS](http://cebas.mec.gov.br/)****-** Certificação de Entidades Beneficentes de Assistência Social
