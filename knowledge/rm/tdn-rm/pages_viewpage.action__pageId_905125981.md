---
content_hash: 32377a478fffc31a82bcbd7c0d6de811438d2a032b2afa6260df9d2cc31a30a7
fetched_at: '2026-06-29T00:12:03.265983+00:00'
page_id: '905125981'
product: rm
source: tdn-rm
title: Suspensão1
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=905125981
version: 18
---

LayoutCampos

Registro deve ser gerado sempre que houver Debito Discutido Judicialmente. Quando no Período de Apuração (Anexo - Darf - Sub Pasta - Outros Dados) estiver informado o processo judicial/administrativo e o campo Valor Suspensão estiver preenchido.

Dentro do cadastro do Processo Judicial e Administrativo, o campo Natureza da Ação Judicial deve ser preenchida com uma natureza adequada para geração do Registro.

Observação: Não estamos considerando os tributos IRPJ e CSLL, serão implementados sob demanda.

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **Campo** | **Nível** | **Tipo** | **Descrição** | **Origem dos Dados** | **Obrigatório** |
| ListaSuspensoes | 1 | Array | Lista das suspensões da apuração. |  | Não, mas pode existir somente se SemMovimento for “false” e se não houver o array ListaEventosEspeciais |
| (sem nome) | 2 | Object | Agrupa os dados da suspensão (pode ocorrer mais de uma vez) |  | Sim, se houver o array ListaSuspensoes. |
| TipoSuspensao | 3 | Number | Tipo da suspensão, sendo: 1: administrativa; 2: judicial. | Gerado conforme o campo Tipo de Processo, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em ListaSuspensoes. |
| MotivoSuspensao | 3 | Number | Motivo da suspensão judicial, sendo: **1**: Liminar em Mandado de Segurança; **2**: Depósito judicial do montante integral; **4**: Antecipação de tutela; **5**: Liminar em Medida Cautelar; **8**: Sentença em Mandado de Segurança favorável ao contribuinte; **9**: Sentença em Ação Ordinária favorável ao contribuinte e confirmada pelo TRF; **10**: Acórdão do TRF favorável ao contribuinte; **11**: Acórdão do STJ em Recurso Especial favorável ao contribuinte; **12**: Acórdão do STF em Recurso Extraordinário favorável ao contribuinte; **13**: Sentença de 1ª Instância não transitada em julgado com efeito suspensivo. | Gerado conforme o campo **Natureza Judicial**, dentro do Processo Judicial e Administrativo, segue "**De Para**":  **Caso** Decisão Judicial Oriunda de Liminar em Mandado Segurança Coletivo ou **Caso** Decisão Judicial Oriunda de Liminar em Mandado Segurança ou **Caso** Decisão Judicial Oriunda de Liminar em Mandado Segurança, exigibilidade suspensa de contribuição **Retorno: 1** Liminar Em Mandado De Segurança;  **Caso** Decisão Judicial Vinculada a Deposito Administrativo ou Judicial em Montante Integral ou **Caso** Decisão Judicial Vinculada a Deposito Administrativo ou Judicial em Montante Integral - Exigibilidade suspensa de contribuição: **Retorno: 2** Deposito Judicial Do Montante Integral;  **Caso** Decisão Judicial Oriunda de Antecipação de Tutela: **Retorno: 4** Antecipação De Tutela;  **Caso** Decisão Judicial Oriunda de Liminar em Medida Cautelar: **Retorno: 5** Liminar Em Medida Cautelar;  **Caso** Sentença Em Mandado De Segurança Favorável Ao Contribuinte: **Retorno: 8** Sentença Em Mandado De Segurança Favorável Ao Contribuinte;  **Caso** Sentença Ação Ordinária Favorável ao Contribuinte e Confirmada pelo TRF: **Retorno: 9** Sentença Em Ação Ordinária Favorável Ao Contribuinte E Confirmada Pelo TRF;  **Caso** Acordão do TRF favorável ao Contribuinte: **Retorno: 10** Acordão Do TRF Favorável Ao Contribuinte;  **Caso** Acordão do STJ em recurso Especial Favorável ao Contribuinte: **Retorno: 11** Acordão Do STJ Em Recurso Especial Favorável Ao Contribuinte;  **Caso** Acordão do STF em recurso Extraordinário Favorável Contribuinte: **Retorno: 12** Acordão Do STF Em Recurso Extraordinário Favorável Ao Contribuinte;  **Caso** Decisão Judicial Não Transitada Em Julgado, a favor da Pessoa Jurídica ou **Caso** Decisão Judicial Não Transitada Em Julgado, a favor da pessoa jurídica, exigibilidade suspensa de contribuição: **Retorno: 13** Sentença De Primeira Instancia Não Transitada Em Julgado com Efeito Suspensivo;  **Caso**Não esteja na lista acima o retorno é zero e será apresentado mensagem de inconsistência de schema, sendo necessário uma análise mais aprofundada da opção selecionada pelo usuário e opções disponíveis na rotina MIT. | Sim, para cada ocorrência de objeto em *ListaSuspensoes* e se *TipoSuspensao* for [2]. |
| ComDeposito | 3 | Boolean | Indicador de suspensão judicial com depósito, sendo: **false**: Não; **true**: Sim. | Valor Fixo preenchido com "**false**" Sem Depósito | Sim, para cada ocorrência de objeto em ListaSuspensoes e se MotivoSuspensao for diferente de [2]. |
| NumeroProcesso | 3 | String (20) | Número do processo judicial (20 dígitos) ou administrativo (17 dígitos). Exemplos: "98765431220251017777" e “12345987654202450”. | Gerado conforme o campo Número, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em *ListaSuspensoes*. |
| ProcessoTerceiro | 3 | Boolean | Indicador de que o processo judicial é de terceiro, sendo: **false**: Não (contribuinte é o autor); **true**: Sim. | Gerado conforme o campo Autor da Ação é Terceiro, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em *ListaSuspensoes* e se *TipoSuspensao* for [2]. |
| DataDecisao | 3 | Number | Data da decisão judicial no formato AAAAMMDD. Exemplo: 20240920. | Gerado conforme o campo Data da Sentença, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em *ListaSuspensoes* e se *TipoSuspensao* for [2]. |
| VaraJudiciaria | 3 | Number | Número da Vara Judiciaria onde tramita o processo. Exemplo: 1. | Gerado conforme o campo Vara, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em *ListaSuspensoes* e se *TipoSuspensao* for [2]. |
| CodigoMunicipioSj | 3 | String (7) | Código IBGE do município sede da subseção judiciária onde tramita o processo, com 7 dígitos. Exemplo: "5002704". | Gerado conforme o campo Cod Município, dentro do Processo Judicial e Administrativo | Sim, para cada ocorrência de objeto em *ListaSuspensoes* e se *TipoSuspensao* for [2]. |
| ListaDebitosSuspensos | 3 | Array | Lista dos débitos objeto da suspensão. | Lista dos débitos (guias) que possui processo judicial ou administrativo vinculado | Sim, para cada ocorrência de objeto em *ListaSuspensoes*. |
| (sem nome) | 4 | Object | Agrupa os dados do débito suspenso (pode ocorrer mais de uma vez). | Agrupador de dados | Sim, para cada ocorrência do array *ListaDebitosSuspensos*. |
| IdDebitoSuspenso | 5 | Number | Número de identificação do débito suspenso. Exemplo: 1. | Identificador incremental automático. | Sim, para cada ocorrência de objeto em *ListaDebitosSuspensos*. |
| ValorSuspenso | 5 | Number | Valor suspenso do débito com 2 casas decimais. Exemplo: 1000.00. | Valor suspenso informado na guia. | Sim, para cada ocorrência de objeto em *ListaDebitosSuspensos*. |

ExemplojsSuspençõestrue
