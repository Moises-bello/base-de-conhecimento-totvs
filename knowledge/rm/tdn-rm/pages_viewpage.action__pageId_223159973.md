---
content_hash: 13acb89e379deb94346aa1c460491458ee7e8b44f41581bdd3c2039cc7efa8f0
fetched_at: '2026-06-29T00:06:21.016952+00:00'
page_id: '223159973'
product: rm
source: tdn-rm
title: SAU0065_Integração_LIS_TOTVS_Gestão_Hospitalar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=223159973
version: 2
---

# Qual o fluxo e o layout da integração entre o sistema LIS RM e o sistema terceiro?

|  |  |
| --- | --- |
| **Produto:** | TOTVS Gestão Hospitalar |
| **Versões:** | A partir 11.8x |
| **Ocorrência:** | Qual o fluxo e o layout da integração entre o sistema LIS RM e o sistema terceiro? |
| **Passo a passo:** | **Pré-requisitos**  Sistema terceiro ter acesso ao WebService LIS RM;  Sistema LIS RM ter acesso ao WebService sistema terceiro;  Tabelas de DE/PARA necessários para integração (convênio, posto/setor e exame);    **Integração proposta**  A integração entre os sistemas será realizada via WebService e ocorrerá em dois momentos:     * Importação de pedidos:   O sistema terceiro irá fazer uma requisição ao WebService do sistema LIS RM com os pedidos de exames a serem integrados. O sistema LIS irá realizar os DE/PARA de códigos necessários (convênio, posto/setor e exame) e cadastrar os pedidos dos exames no LIS, que irá retornar ao sistema terceiro uma resposta à requisição contendo quais pedidos foram importados com sucesso e quais não foram, e para os que não foram, o motivo pela não importação.     * Exportação de resultados:   Após a liberação do laudo pelo responsável, o sistema LIS RM fará a exportação desse resultado ao sistema terceiro. Essa exportação será realizada via WebService.    **Formato padrão para datas**  As datas devem estar no formato ODBC (aaaa-mm-dd) e caso possua horário, este deve estar com horas, minutos e segundos (00:00:00).  Exemplo de data e hora: “2011-09-28 14:30:45”    **Tipo de dados dos elementos**  O tipo de dado que irá compor os elementos XML deverão ser “string”.    **Importação de Pedidos**  **Método de importar pedido do WebService do sistema LIS RM:** ImportarPedido(OrdensServicos).    **XML de entrada:**  **XML Ordens de Serviço**  Estrutura básica:  <OrdensServicos> <OrdemServico>  ...  </OrdemServico>  < OrdemServico>  ...  </OrdemServico > </OrdensServicos>    **Tag principal: OrdensServicos**  Deve ser composta por uma ou mais ordens de serviço. Uma ordem de serviço é onde estão definidos os dados do paciente e dos exames a serem importados.    **Tag OrdemServico**  Elementos:  Endereco  Cidade  Estado  Cep  Sexo  DataNasciment                                ------------------Informações do paciente.  Rg  Email  Bairro  Nome  Cpf  Ddd  Telefone  ObsTelefone  DddCelular  Celular  Altura  Peso  DUM (Data Ultima Mestruação)    ResponsavelNome  ResponsavelEndereco  ResponsavelCidade  ResponsavelEstado  ResponsavelBairro    -----------Informações do responsável pelo paciente.  ResponsavelCep  ResponsavelTelefone  ResponsavelRg  GrauParentesco    Leito  CNS               -----------Informações sobre o posto/setor de atendimento.  PostoOrigem    DataCadastro  CodigoPacienteHIS  Convenio      ------------Informações da ordem de serviço.  NomeConvenio  OrdemServicoHIS    Exames         à   Informações dos exames (código, amostras, médicos...).    **Tag Exames**  Elementos:  Exames (Lista)  Amostras (Lista)  MedicosCRM (Lista)  MedicosUF (Lista)  MedicosNome (Lista)  MedicosConselho (Lista)  MedicosExames (Lista)            --------------Informações do exame.  Perguntas (Lista)  Respostas (Lista)  Coleta (Lista)  Volume (Lista)  Tempo (Lista)  Material (Lista)    **XML de exemplo com dados obrigatórios.**    **XML de retorno:**    **Exportação de Resultado**  **Método para exportação de resultado do sistema terceiro:** EnviarResultados(RetornaResultado).    **XML de Entrada**  **XML RetornaResultado**  Elementos:  DataHora  OrdensServicos    **Tag OrdensServicos**  Elementos:  OrdemServicoResultado    **Tag OrdemServicoResultado**  Elementos:  OrdemServicoHIS  Resultados  LaudoURLOs    **Tag Resultados:**  TblResultado    **Tag TblResultado**  Elementos:  Exame  LaudoURLExame  ResponsavelLiberacao  DataHoraLiberacao    **XML de exemplo com dados para exportar resultados:**      **XML de saída:** |

divs
