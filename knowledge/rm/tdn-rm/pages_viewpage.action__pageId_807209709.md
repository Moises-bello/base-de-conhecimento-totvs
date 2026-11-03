---
content_hash: afcfafcf09528b2aafe828171638347bda70e777b19ec42cea8a9e1afc410ac4
fetched_at: '2026-06-29T00:11:43.458190+00:00'
page_id: '807209709'
product: rm
source: tdn-rm
title: Configuração do Relatório para Declaração Mensal de Serviços Educacionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=807209709
version: 50
---

## Provedor - Dados da declaração mensal de serviços educacionais

Esse provedor de dados tem o objetivo de gerar a declaração mensal de serviços educacionais para a prefeitura de Salvador conforme o [decreto](http://www.nota.salvador.ba.gov.br/arquivos/legislacao/Decreto_37264_2023.pdf)e baseado o layout fornecido pela prefeitura.

ATENÇÃO

Disponível a partir dos patches:

* **12.1.2302.240 ou superior**
* **12.1.2306.187 ou superior**
* **12.1.2310.121 ou superior**

Para a geração correta do relatório da declaração mensal de serviços educacionais, antes devem ser **realizadas algumas configurações no sistema** para a sua geração.

Parametrizações

|  |  |  |  |
| --- | --- | --- | --- |
| 1 - Executar os script's de marcações **CN.2023.11\_05 e CN.2023.12\_02** na base de dados.  Esse execução é **obrigatória**, após execução do script é aconselhável deletar o Host e subir novamente para aparecer no Campo Complementar o cadastro de Serviço.  O script **CN.2023.12\_02 é obrigatório para base de dados Oracle.** | | | |
| 2 - Nas permissões do Perfil liberar acesso no Campo Complementar do cadastro de Serviço. | | | |
| 3 - Criação do campo complementar **CTISS**para o serviço. Esse campo deve ter **obrigatoriamente** o nome de **CTISS** ser do tipo alfanumérico com tamanho 10, e subtipo do campo texto igual a texto. Após a criação do campo, **deverá ir no cadastro de serviços** e editar o serviço desejável, e na **aba campos complementares** o campo deverá ser preenchido conforme as regras presentes na documentação da **declaração mensal de serviços educacionais.** | | 3 - Criação do campo complementar **CODIGOBENEFICIO** para a bolsa. Esse campo deve ter **obrigatoriamente** o nome de **CODIGOBENEFICIO** ser do tipo alfanumérico com tamanho 10, e subtipo do campo texto igual a texto. Após a criação do campo, d**everá ir no cadastro de bolsas** e editar a bolsa desejável, e na **aba campos complementares** o campo deverá ser preenchido conforme as regras presentes na documentação da **declaração mensal de serviços educacionais.** | |
|  | |  | |
| 4 - Após criar os campos complementares dar permissão no Nível de Ensino | | | |

Relatório Declaração Mensal de Serviços 

Os relatórios para a Educação Superior e Básica serão disponibilizados no **TOTVS Compartilhamento** presente no Menu Gestão → **Utilitários** dentro do módulo Educacional.

No campo "**Buscar**" informar o nome do relatório e mandar pesquisar. Após a conclusão da pesquisa clicar na opção "**Baixar Arquivo**"

Serão disponibilizados dois relatórios, um para a educação superior e outro para educação básica

* EDUREL0084 - Declaração Mensal de Serviços Educação Superior.TotvsReport
* EDUREL0085 - Declaração Mensal de Serviços Educação Básica.TotvsReport

ATENÇÃO

Após a importação dos relatórios é importante vincular os relatórios importados com a fonte de dados "Declaração Mensal de Serviço".

personalizadoCriar Relatórios Personalizados

Caso os relatórios presentes no **TOTVS Compartilhamento** não atende as suas necessidades, pode-se criar relatórios personalizados.

A seguir como criar um novo relatório informando a fonte de dados que é o novo provedor criado, a **Declaração Mensal de Serviços.**

Vale lembrar que este provedor somente funciona se vinculado ao cadastro do relatório conforme abaixo e apenas para relatório da declaração mensal de serviços.

**Uma vez vinculado não é possível remover a fonte de dados**, para remover, será necessário criar um novo relatório.

Ao abrir o layout do relatório e ir na lista de campos da tabela **SDECLARACAOMENSALSERVICO**  irá aparecer com os seus respectivos campos.

**SDECLARACAOMENSALSERVICO**

Tabela de dados da declaração mensal de serviço, segue os campos possíveis:

* + - * + - * + - * + - NOMEALUNO: Nome do aluno.
                      - NOMESOCIALALUNO: Nome social do aluno.
                      - NOMECURSO: Nome do curso ou etapa de ensino vinculado ao contrato do aluno.
                      - NUMEROMATRICULA: Número da matrícula. O número da matrícula será o registro acadêmico do aluno.
                      - NOMERESPONSAVEL: Nome do responsável financeiro informado no cadastro do aluno.
                      - NOMEFANTASIARESPONSAVEL: Nome fantasia do responsável financeiro informado no cadastro do aluno.
                      - CPFRESPONSAVEL: CPF do responsável financeiro informado no cadastro do aluno.
                      - VALORCONTRATO: Valor total do contrato do aluno.
                      - MESCOMPETENCIA: Mês de competência da declaração mensal de serviços. Será o mês de competência informado no parâmetro DATACOMPETENCIADMS.
                      - ANOCOMPETENCIA: Ano de competência da declaração mensal de serviços. Será o ano de competência informado no parâmetro DATACOMPETENCIADMS.
                      - VALORMENSALIDADE: Valor da mensalidade do serviço da parcela presente no contrato do aluno.
                      - CODIGOBENEFICIO: Código do benefício informado no campo complementar conforme descrição acima na bolsa presente no contrato do aluno.
                      - VALORBENEFICIO: Valor do benefício que é o valor da bolsa presente no contrato do aluno.
                      - CTISS: Valor do CTISS informado no campo complementar conforme descrição acima no serviço presente na parcela do contrato do valor.
                      - CODCURSO: Código do curso do aluno vinculado ao contrato do aluno.
                      - CODCOLIGADACFO: Código da coligada do responsável financeiro informado no cadastro do aluno.
                      - CODCFO: Código do financeiro informado no cadastro do aluno.
                      - CODCOLIGADA: Código da coligada do contrato do aluno.
                      - RA: Registro acadêmico do aluno.
                      - CODCONTRATO: Código do contrato do aluno.
                      - IDPERLET: Identificador do período letivo vinculado ao contrato do aluno.
                      - IDHABILITACAOFILIAL: Identificador da habilitação filial vinculada ao contrato do aluno.
                      - CODFILIAL: Código da filial do contrato do aluno.
                      - CODTIPOCURSO: Código do nível de ensino do contrato do aluno
                      - CODSERVICO: Código do serviço presente da parcela do contrato do aluno.
                      - CODBOLSA: Código da bolsa presente no contrato do aluno.

A partir daí é montar o layout conforme a solicitação do layout da declaração mensal de serviços solicitada pela prefeitura de Salvador.

ATENÇÃO

O relatório deve gerar um arquivo com **extensão xlsx ou xls.**

O layout apresentado na imagem abaixo está considerado a **educação superior**.

  

Utilização do Relatório

Com o relatório pronto, basta agora executar o mesmo informados os dados dos parâmetros.

Selecionar o relatório na tela do RM Reports e ir no processo de gerar relatório, o sistema irá abrir a tela de geração de relatório.

 Nessa etapa basta clicar no botão avançar                                                                                                

                     

  

Na tela de parâmetros informar os valores para cada parâmetro.

* A Origem só é permitido Valor Fixo.
* A competência deve ser informada no formatado **MM/yyyy**. Ex: 11/2023, 01/2024

Na tela de tipo de geração deve selecionar a opção exportação para arquivo                                  Na tela de tipo de saída selecionar a opção Microsoft Excel (XLSX) ou Microsoft Excel (XLS).

Na tela de caminho selecionar o caminho que o arquivo será gravado, e ajustar o nome do arquivo conforme a documentação do layout fornecido pela prefeitura de Salvador.

 

O relatório irá gerar o arquivo considerando as informações presente na tabela **SDECLARACAOMENSALSERVICO**que o provedor fornece. A regra de preenchimento dos dados na tabela **SDECLARACAOMENSALSERVICO**será:

* Os contratos ativos pertencentes à coligada, filial, nível de ensino e que tenha parcela com data de vencimento na competência informada.
  + As parcelas com lançamentos gerados serão considerado o valor original do lançamento e os valores das bolsas vinculadas aos lançamentos gerados que estão não estão cancelados ou gerados por acordo. Isso por questão de performance para a geração do relatório.
  + As parcelas sem lançamentos gerados os valores serão simulados para obter o valor da parcela e os valores das bolsas. Simulação de valores utilizará as mesmas regras presentes no sistema nos processos de simulação de valores das parcelas
* Será criada uma linha para cada serviço e bolsa presente no contrato do aluno.

Exemplo 1:

No contrato do aluno temos o serviço A e as bolsas X e Y. Então no arquivo terá uma linha para o serviço A para a bolsa X, e uma outra linha com o serviço A para a bolsa Y.

|  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Nome do Aluno** | **Nome do Curso** | **Nº de Matrícula** | **Nome Responsável** | **CPF Responsável** | **Valor Contrato** | **Mês** | **Ano** | **Valor Mensalidade** | **Código Benefício** | **Valor Benefício** | **CTISS** |
| Aluno 1 | Curso 1 | RA-0001 | Responsável financeiro 1 | 111.111.111-11 | 1000,00 | 11 | 2023 | 100,00 | Bolsa X | 10,00 | CTISS Serviço A |
| Aluno 1 | Curso 1 | RA-0001 | Responsável financeiro 1 | 111.111.111-11 | 1000,00 | 11 | 2023 | 100,00 | Bolsa Y | 15,00 | CTISS Serviço A |
