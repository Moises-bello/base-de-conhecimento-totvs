---
content_hash: 1c8b1b3c754064029ce53e9c05e91abdb13a345124b8c3808e9a8474aacdcadb
fetched_at: '2026-06-29T00:05:59.636534+00:00'
page_id: '191467484'
product: rm
source: tdn-rm
title: Release Versão 11.82.39
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=191467484
version: 14
---

Topo

## 

1RH1

* TOTVS Automação de Ponto
1RH2

* TOTVS Folha de Pagamento
1RH3

* TOTVS Gestão de Pessoas
1RH4

* TOTVS Segurança e Medicina do Trabalho

## 

2BO1

* TOTVS Estoque, Compras e Faturamento
2BO2

* TOTVS Gestão Financeira
2BO3

* TOTVS Gestão Fiscal
2BO4

* TOTVS Gestão Patrimonial
2BO5

* TOTVS Gestão Contábil

## 

3EDU1

* TOTVS Educacional
3EDU2

* TOTVS Gestão Bibliotecária
3EDU4

* TOTVS Processo Seletivo
3EDU4

* TOTVS Avaliação e Pesquisa

## 

4CP1

* TOTVS Construção e Projetos
4CP2

* TOTVS Incorporação
4CP3

* ETO - Engenharia sob encomenda
4CP4

* TOTVS Manutenção

## 

5CRM1

* TOTVS Gestão de Relacionamento com Cliente

---

# **RH**

# **RH**

1trueRH1Automação de Ponto

### [Help](http://wikihelp.totvs.com.br/WikiHelp/PTO/PTO.Chronus.aspx) do TOTVS Automação de Ponto.

* Otimizado:
  + Impressão de adicional noturno nos campos Totais gerados no período e Eventos do Movimento do Período no relatório do espelho do cartão.
  + Recálculo do espelho de ponto quando existe dia ponte cadastrado no período.
  + Importação de batidas utilizando a Integração com o TSA.
  + Abertura de espelho de ponto.
  + Alteração da jornada.
  + Filtro por perfil na visão do cartão de ponto.
  + Cálculo de adicional noturno para considerar o intervalo de refeição.
  + Processo de Alteração por escala - Horário e Descanso.
  + Processo global de batidas.
  + Recálculo do espelho de ponto.
  + Recálculo do espelho de ponto considerando as horas extras não autorizadas no cálculo do adicional noturno.
  + Impressão da justificativa de autorização de extra no relatório de espelho.
  + Processo de limites de abono para não apresentar mensagem de validação nos abonos com limite 0 ou abonos lançados fora do período de validade.
  + Cálculo de faltas para feriado parcial.
  + Processo de aprovação de abono deixando de exibir a mensagem: “O registro solicitado não foi encontrado na base de dados”.
  + Recalculo do espelho ponto para não exibir a mensagem de referência de objeto.
  + Relatório de espelho de cartão de ponto para ser exibido corretamente a descrição de afastamento, quando existir dois afastamentos no período.
  + Lançamento de batidas Ausência Planejada.
  + Processo lançamento de autorização para validar os campos Limite de horas, Número de horas ou intervalo.
  + Espelho do cartão para exibir os horários do funcionário do período selecionado.
  + Impressão da descrição de abonos do relatório do espelho do cartão.
  + Processo de tradução da coluna tempo de refeição no espelho de ponto.
  + Processo de tradução dos tipos de ocorrências.
  + Processo de geração do relatório de espelho considerando os parâmetros "Apenas hora a pagar/descontar" e "Horas compensando dia a dia".
  + Definição de atitude da ocorrência do banco de horas diário quando as horas são calculadas através de fórmula.
  + Processo de importação de batidas para não ser exibido mensagem de violação de chave.
  + Cálculo das horas extras dentro do limite de refeição quando a ausência executada for menor que a planejada.
  + Atualização do espelho de cartão após o processo de cálculo.
  + Processo de liberação de ponto sem a necessidade de selecionar um período atual e ativo.
  + Processo de troca de chapa.
  + Lançamento de eventos calculados por fórmula no movimento do funcionário.
  + Cálculo da função EXTRAAUTO.
  + Alteração de atitude das ocorrências calculadas, quando forem criticada.
  + Cálculo de horas para funcionários que não possuem jornada planejada.
  + Importação de batidas de visitante priorizando crachá.
  + Cálculo da função “HORAS FALTAS” considerando os parâmetros “Considerar a data atual” ou e “Considerar a data atual - 1”.
  + Recálculo para funcionários que possuem o parâmetro "Considera feriado pelo dia de saída" marcado.
* Criado script para correção na trigger TR\_DEL\_ABATFUNLOG.
* Melhoria para disponibilizar um serviço consumido pelo Labore que retorne as informações do horário planejado no intervalo de datas desejado.
RH2Folha de Pagamento

### [Help](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Labore.aspx) do TOTVS Folha de Pagamento.

* Adicionada opção para utilização de Relatórios .Net no envelope de pagamento via portal.
* Ajuste:
  + Geração do Informe de Rendimentos via portal para funcionários com Rendimentos Recebidos Acumuladamente
  + Arquivo do Seguro desemprego para adequação ao Validador que entende como CEI correto o número completado com zeros à direita. Criado parâmetro de tela para utilizar zeros à direita.
  + Campo hora do evento no código fixo para manter o valor informado.
  + Campo hora na aba Jornada/Salário para ser habilitado ao informar Código de Recebimento H, T ou P.
  + Campo número meses trabalhados no arquivo de seguro desemprego para trazer valor zerado (00) conforme layout.
  + Rotina de importação de códigos fixos para considerar o valor hora.
  + Diferença de Férias para lançar o evento de CC 132, quando o cálculo é feito na mesma competência do primeiro mês das férias partidas.
  + Função de fórmula MV, quando utilizada na Diferença Salarial com as funções MES e ANO.
  + Função NDTRAB para chamar o serviço da Automação de Ponto somente quando o cliente utiliza esse sistema.
  + Geração do SEFIP 650 para abater no valor do CC 69, todos os eventos de CC 99, para emitir o valor do campo Remuneração de FGTS sem 13º.
  + Proporcionalização da perda de dias de direito devido a faltas no CC 329, quando existem avos do período vencido e avos do período proporcional.
  + Rotina de importação de dados RMLabore - códigos fixos para gravar valor correto no campo hora.
  + Rotina de seguro desemprego para gravar campos Penúltimo e Antepenúltimo no perfil e aplicar fórmulas para estes campos.
  + Validação do perfil de seguro desemprego quando não há perfil gravado.
  + Cálculo da diferença de férias para considerar o parâmetro global de férias "Paga adic.constitucional sobre dias de direito de férias".
  + Cálculo de pensão alimentícia para estornar da base de IRRF somente os descontos que estiverem marcados para estornar IRRF.
  + Cálculo do CC 24 na rescisão, que estava abatendo em duplicidade os dias de férias já gozados, quando a projeção do aviso prévio indenizado completa o segundo período vencido de férias.
  + Cálculo do rateio por centro de custo, para ignorar espaços em branco no final do código do centro de custo.
  + Lançamento de empréstimos do Gerenciador de Movimento para o envelope, para não zerar o desconto caso seja efetuado o mesmo lançamento mais de uma vez.
  + Processo de Contabilização para não retornar diferença de 1 centavo no arredondamento do encargo.
  + Processo de Diferença Salarial para permitir o cálculo da diferença do CC 10.
  + Alterar a situação do funcionário para "C - Contrato de Trabalho Suspenso". O Labore irá incluir essa informação automaticamente tanto no histórico de situação quanto no histórico de afastamento, assim como é feito no retorno deste afastamento.
* Consistência para não permitir que as funções VALORCODCALCULO e CODCALCULOCORRENTE sejam utilizadas juntas na fórmula de pensão alimentícia no cadastro do dependente.
* Correção:
  + Validação de envio de aviso automático por fórmula.
  + Carregamento de eventos para cálculo de médias.
  + Envio de e-mail para cadastro de sugestão de férias via portal para pegar o chefe imediato correto.
* Criação de parâmetro para definir o final do período em que o auxílio doença de responsabilidade da Empresa teve duração de 30 dias (MP 664).
* De acordo com o entendimento sobre Instrução Normativa SRT nº 15/2010. A nomenclatura para data do aviso na rescisão individual e coletiva foi modificada conforme descrito: - de "Data do Aviso Prévio" para "Data de Início do Aviso Prévio";- De “Data do Aviso Trabalhado” para “Data de Início do Aviso Trabalhado”; - De “Data do Aviso” para “Data de Início do Aviso” .
* Foi incluído no cadastro de seção, na aba Endereço, o botão “Buscar município”, facilitando assim o preenchimento dos campos "cidade" e "código de município".
* Fracionamento de jobs para a crítica de folha.
* Importação de Dados RM Labore, Dados Cadastrais (Funcionários) deixa de ser obrigatório o campo Número Ficha de Registro para casos de parâmetro 'Número de Ficha de Registro gerado pelo sistema' estiver marcado. Nestes casos, o arquivo com os dados de importação poderá ter este campo em branco, gerando número sequencial pelo sistema. Caso o Parâmetro esteja marcado e o número da ficha de registro for informado no arquivo, também será gerado o número sequencial pelo sistema, ignorando o número no arquivo e informando a situação no log.
* Incluída validação para que a funcionalidade "Incluir dígito no código da seção" só esteja disponível;Caso o parâmetro "Utiliza inclusão de dígito na seção" esteja marcado.Este parâmetro ficará na seção "Máscaras e quebras" no parametrizador.
* Melhoria do processo de Troca Chapa.
* Na GRRF, ao calcular a Base FGTS por dissídio, feito ajuste para não considerar o valor da diferença de aviso prévio indenizado, CC 99.
* No cadastro de sugestão de férias via Portal, agora é possível informar a data inicial e final das férias e o sistema deverá calcular o número de dias das férias.
* No relatório Passivo Trabalhista o campo Dias de Aviso na seção "PARAMETRIZAÇÃO SOLICITADA PARA EMISSÃO DO PASSIVO TRABALHISTA" passa a apresentar duas informações:
  + "Valor dos dias do aviso informado na parametrização" se o parâmetro "Executa fórmula de aviso prévio" estiver desmarcado;
  + "Por fórmula", se o parâmetro "Executa fórmula de aviso prévio" estiver marcado.

* Otimização para melhoria na performance do processo de Cálculo de Férias.
* Otimizado:
  + Consideração da marcação do fato gerador no momento de geração dos Lançamentos Financeiros.
  + Exibição da data de estabilidade dentro do item Pendências Demissionais do cadastro do Funcionário.
  + Exibição do endereço do Tomador de Serviço/CEI no relatório do SEFIP.
  + Geração de lançamentos financeiros no processo da guia de INSS.
  + Visualização do botão Executar Novamente no processo da RAIS.
  + Geração do homolognet pelo CNPJ da coligada pelo parâmetro "Utiliza cnpj coligada", mesmo utilizando CEI na base.
  + Geração do SEFIP e GUIA de INSS, para que os eventos de dedução de 13 de licença maternidade sejam levados em consideração no cálculo das deduções.
  + Rotina de inclusão de dígito no código da seção.
  + Verificação de segurança para funcionalidade de calcular e finalizar férias.
  + Cadastro de seção, validação do CEI informado.
  + Complemento de histórico de lançamentos financeiros na geração da guia de INSS.
  + Cadastro de eventos no Salário Composto.
  + Cálculo do salário hora do funcionário com salário composto.
  + Envio de aviso automático para ser processado conforme foi parametrizado, para tela ou e-mail.
  + Funcionamento dos Parâmetros Locais no Folha de Pagamento.
  + Processo de geração do relatório de salário contribuição em bases Oracle.
  + Tratamento do telefone do funcionário no relatório de Seguro Desemprego em casos de telefones com nove dígitos.
  + Tratamento dos campos de aviso misto na rescisão coletiva para persistir os dados tanto em rescisão no mês como próximo mês.
  + Processo de alteração global de tomadores.
  + Regra para redução de aviso prévio, possibilitando ao usuário desmarcar a opção quando o aviso prévio é o indenizado.
* Permitir que seja gerado o histórico de provisão de funcionário transferido pelo tipo 5 (SEM ônus p/ Cedente) no último dia do mês.
* Quando funcionário não possui férias a serem lançadas, permitir que sejam calculados os eventos cadastrados no grupo de eventos lançados.
* Incluído parâmetro em tela para considerar demitidos tipo T(Término de Contrato) em arquivo Seguro do Desemprego.
* Tratamento para que parâmetros do Processo de Geração de Lançamentos Financeiros possam ser lidos através de Fórmula Visual.
RH3Gestão de Pessoas

### [Help](http://wikihelp.totvs.com.br/WikiHelp/RHU/RHU.Vitae.aspx) do TOTVS Gestão de Pessoas.

* Ao transferir um funcionário, o histórico de benefícios dos dependentes são copiados corretamente para a nova chapa.
* Evolução no processo de controle de vaga por seção, para que ao alterar informações do cadastro do funcionário não seja apresentado validação de vaga.
* Otimizada:
  + Chamada da validação de unicidade de Pessoas.
  + Validações das requisições quando for solicitada que a mesma seja inserida no Fluxo.
* Realizada melhoria no processo de geração de tabela salarial de forma a informar ao usuário o motivo de erro, caso exista, pois a mensagem não detalhava o problema.
* Realizado ajuste no processo "Carga Inicial de Estabilidade" de forma a não inserir estabilidade para representantes do empregador na CIPA, pois esses não possuem estabilidade.
* Reestruturação em requisição de alteração de dados funcionais.
RH4Segurança e Medicina do Trabalho

### [Help](http://wikihelp.totvs.com.br/WikiHelp/SMT/SMT.VitaeSegurancaTrabalho.aspx) do TOTVS Segurança e Medicina do Trabalho.

* Ajuste na seleção de exames no Assistente de Agendamento Automático. Quando é feito um filtro utilizando "OR", serão trazidos apenas os exames da coligada corrente, respeitando o filtro.
* Disponibilizado novo relatório ASO que será executado através do processo "Atestado de Saúde Ocupacional", no cadastro de Consultas Realizadas (Anexo do Funcionário).
* Otimizado no processo de geração do relatório ASO a busca dos dados de endereço e contato do médico.
* Realizado ajuste no processo "Carga Inicial de Estabilidade" de forma a não inserir estabilidade "Eleito Titular CIPA" para representantes eleitos como suplente.

 

# **BACKOFFICE**

## **BackOffice**

false2trueBO1Estoque, Compras e Faturamento

### [Help](http://wikihelp.totvs.com.br/WikiHelp/EST/sEST.Nucleus.aspx) e do TOTVS Gestão de Estoque, Compras e Faturamento.

* Ajustes:
  + Campo que referencia Chave de Acesso no processo de impressão e imagem da logomarca da Filial.
  + Envio de CT-e de Substituição para o documento vinculado de CT-e de Anulação.
  + Relatório .NET DACT-e para que sejam impressos os veículos associados, bem como visualização do campo da UF pertinente ao veículo transportador.
* Alteração no relatório DACTE aumentando campos de Endereço e Bairro para comportar informações longas e inclusão da informação de Unidade de Medida para o campo de Quantidade.
* Atendimento à NT-001/2015 (CT-e)
* Consistência no preenchimento da UF e Cidade aba Coleta/Entrega, caso tenha algum dado informado.
* Inclusão de anexo do RM Saúde nos movimentos do RM Nucleus.
* Melhorias:
  + Para impressão da descrição do Tipo de Veículo.
  + Inclusão e edição de um Movimento com tributação.
  + Ao aplicar reajuste de contrato no faturamento.
  + Geração do Segundo código de barras para MDF-e com CT-es em contingência vinculados.
  + Faturamento de medições por Lote para levar em consideração Data da Medição na geração de movimentos.
  + Processo de anulação de CT-e.
  + Processo de estorno de item não recebido.
  + Processo de exclusão de movimentos associados a um CT-e.
  + Processo de Inclusão de Movimento via RM Educacional.
  + Processo de Inclusão de Movimentos para o Campo Código do Serviço.
  + Inclusão e faturamento movimentos que aceitam inclusão via XML (TOTVS Colaboração).
  + Geração de relatório de ficha física financeira.
  + Regerar saldos e custos.
  + Tela responsável pelo relacionamento de movimentos de exportação.
  + Funções de fórmula do movimento.
  + Regras de obrigatoriedade de campos do movimento.
  + Regras de visibilidade do campo "Chave de acesso" no movimento.
  + Cálculo de tributos do movimento.
  + Cálculo do quadro comparativo.
  + Processo de faturamento utilizando TOTVS Colaboração.
  + Processo responsável por alterar contabilidade.
* Recálculo de custo realizado através do sistema de produção desbloqueado por validação de lote quando estiver atualizando custos.
BO2Gestão Financeira

### [Help](http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.Fluxus.aspx) e do TOTVS Gestão Financeira.

* Melhorias:
  + Disponibilização do campo Tipo de Extrato para ser utilizado via WebService no processo de baixa
  + Visão de Emissão de Cheques para que a visualização das casas decimais seja a mesma que foi configurada nos parâmetros do sistema.
  + Processo de Cancelamento de Baixa com cheque para cálculo do valor líquido.
  + Processo “Baixar Créditos/Devoluções Vinculados”, para que o valor das retenções seja proporcional ao valor vinculado.
  + Processo de Alteração Global para que não seja possível alterar o Valor Original de lançamentos do SGI.
  + Processo de Retorno de Cobrança para que seja possível utilizar a data da baixa apenas do cabeçalho na configuração do layout bancário.
  + Processo de Vínculo quando o mesmo é acionado pela tela de baixa de lançamentos.
  + Validação do botão de contabilização do item de baixa, para desabilitá-lo quando se tratar de um item de baixa com cheque emitido.
  + Processo de Cancelamento de baixa para cancelar todos os itens de baixa, quando baixa agrupada e a forma de pagamento for "Cartão de Débito".
  + Processo de Limite de Crédito do cliente. O sistema não permite que um lançamento de documento do tipo “Credito de Adiantamento” interfira no Limite de Crédito do cliente.
  + Utilização do parâmetro "Bloquear o lançamento para alterações automaticamente ao baixar" quando marcado será possível gerar borderô e remessa, mesmo com o lançamento bloqueado para alteração.
  + Execução do processo de Regerar Contabilização “Data da Contabilização” do item de baixa, de acordo com default definido nos parâmetros do sistema “Financeiro | Integração Contábil | Contab. Baixa Pagar | Data Default de Baixa a Pagar”
  + Processo de Inclusão de Fatura para lançamentos com tipo de documento de Crédito de Adiantamento, o sistema não permitirá a seleção desses lançamentos
  + Geração de relatório Totalizador por Níveis que faz com que o sistema traga todos os relatórios independentemente do tipo do relatório selecionado (Analítico ou Sintético) e que ao selecionar um relatório diferente do tipo do relatório selecionado o sistema exibe uma mensagem informando: "Atenção! Esse relatório não é do tipo Relatório (Analítico ou Sintético) selecionado na tela anterior!".
  + Na busca dos lançamentos através da Sessão de Caixa. O sistema busca os lançamentos do aluno informado e não do representante financeiro.
  + Processo de impressão de cheque. O sistema exibe a impressora antes da visualização do relatório.
* Atualização:
  + Apresentação da coluna de Valor Original na View de baixas de lançamento. O sistema exibe o valor com as casas decimais como foi configurado nos parâmetros.
  + Validação ao clicar no 'X' quando o sistema se encontra minimizado. O sistema realiza valida antes se o usuário deseja mesmo desativar a sessão de caixa. Se o usuário confirmar o sistema realizará o mesmo processo de desativação da sessão de caixa.
  + Visualização (controle) dos campos de período (campos de início e fim) no relatório Totalizador por Níveis. O sistema bloqueia o campo caso o checkbox não esteja marcado.
  + Processo de importação de lançamento. O sistema salva o código de origem do lançamento.
  + Campo Autenticação do lançamento para CNAB240
  + Status dos lançamentos e dos itens de baixa, ao realizar cancelamento de baixa com um único cheque emitido para mais de um lançamento.
* Disponibilização dos valores opcionais para serem utilizados no processo de baixa via WebService
* Validação no processo de vínculo de forma que o processo de valida se a soma dos valores a vincular é maior que o valor disponível para vínculo do lançamento selecionado.
* Ajuste no tamanho dos campos LIMITESUPERIOR, LIMITEINFERIOR e SEQNOSSONUMERO da tabela FCONVENIO para conter 17 dígitos antes da virgula com uma casa decimal.

Atenção

Melhorias e alterações exclusivas para **Delphi**:

* Atualização no cálculo do valor líquido para converter o valor retornado quando a lançamento está em outra moeda.
* Atualização na disponibilidade do botão do wizard de processo de geração do arquivo remessa. Somente após o usuário informar o caminho para salvar o arquivo remessa.
* Implementado processo de Ajustes de Itens de Baixa Gerados na Conversão para o novo modelo de baixa.
* Lançamentos de Crédito de Adiantamento, estando vinculados, não devem gerar contabilização.
* Melhorias:
  + Processo de faturamento com lançamentos do RM Nucleus.
  + Processo de parcelamento com lançamentos do RMNucleus. Será necessário solicitar script para execução desse processo.
  + Emissão de cheque para que a sequência de geração dos extratos seja a mesma da ordenação feita na visão de lançamentos.
  + Planilha RM e Excel incluindo a opção na janela de filtros chamada "Não Considerar Natureza com Valor Zerado" para que a planilha não mostre naturezas que não possuem valor na coluna Previsto/Realizado para o filtro que for informado.
  + Processo baixa parcial para os casos em que não é utilizado a cumulatividade (O parâmetro Usar retenções de cumulatividade (Lei 10.925) desmarcado) para que seja aplicado o percentual corretamente.
  + Processo de envio de e-mail de boleto para permitir a utilização via fórmula visual.
  + Processo de importação de baixa em relação aos valores opcionais
  + Processo de rastreabilidade. A melhoria foi feita para evitar pontos de vazamentos de memória identificados no mesmo.
  + Serviço de "Desvincular Borderô de Pagamentos" para que seja possível desvincular mais de um lançamento simultaneamente quando os mesmos compõem a base de cálculo de retenções.
  + Tamanho do campo CI\_Orgao. O tamanho do campo na base de dados e um parâmetro que habilita que o sistema utilize o tamanho de 15 caracteres, será disponibilizado via script.
  + Processo de retorno de cobrança CNAB 240 para que as informações dos campos complementares sejam carregadas
  + Baixa de lançamento gerador de IRRF. Ao realizar a baixa, o sistema calcula a data de vencimento do lançamento de IRRF gerada com base na data da baixa do lançamento gerador.
  + Processo de alteração de lançamentos. O sistema valida somente a data informada dos registros antigos e não a data e a hora. Assim, o sistema entende que não há alteração na data. Obs: Antigamente o sistema salvava os registros com a data e a hora. Com uma mudança realizada, o sistema salva somente a data. Por este motivo foi feito a modificação.
  + Processo de cálculo do valor Líquido. O sistema se comporta da mesma maneira da 1150 Delphi. O parâmetro "Calcular valor líquido automaticamente na visão" foi reincorporado no sistema, sendo que ao carregar a tela de lançamentos é calculado o valor líquido dos lançamentos: Opções | Parâmetros | RMFluxus | Contas A Pagar | Avançar | Etapa Inclusão >> habilitar o parâmetro Calcula Valor Líquido automaticamente na visão.
  + Processo de execução de relatório Delphi, quando chamado pelo RM nova MDI.
  + Realizar retorno de pagamento com cumulatividade. O sistema deixa habilitado a opção "Gerar um extrato para todos os lançamentos".
  + Processo do thread apenas no executável (Delphi) para calcular valor líquido.
  + Processo de cancelamento de baixa pela sessão de caixa, para permitir o usuário selecionar qual item de baixa ele deseja estornar.
  + Processo de baixa de lançamentos vinculados a devolução, mesmo com o valor da baixa sendo igual a zero.
  + Baixa de lançamentos que geram tributos para que caso o parâmetro "Buscar dados no lançamento se cli/for vazio" estiver marcado, os lançamentos gerados de tributo assumam a conta caixa do lançamento origem.
  + Importação de arquivo texto de extrato para considerar as contas contábeis informadas no arquivo.
  + Processo de baixa simplificada ao utilizar o parâmetro "Utilizar data default da baixa".
  + Processo de baixa com cheque para preencher o campo complemento de histórico ao utilizar a variável [EMI] na aba de contabilização.
  + Processo de importação de lançamentos em arquivo texto para buscar as informações das tabelas opcionais nos defaults do cliente fornecedor.
  + Processo de retorno de pagamento do BANESTES que contenha informações referentes a TED para que a data da baixa seja lida da posição 367 a 374 conforme layout.
  + Processo de Retorno de pagamento banco ITAÚ que passa a gravar CNABAUTENTICACAO.

* Atualizações:
  + Processo de Importação de cliente / fornecedor ao utilizar o sistema parametrizado para utilizar código sequencial.
  + Serviço de desbloqueio de lançamento e baixa para manter compatibilidade com a utilização via Webservice.
  + Baixa de lançamentos financeiro quando utilizado pelo processo de integração. (Mensageria única).
  + Processo de importação de baixa de lançamento em arquivo texto para preencher o histórico do extrato com o valor informado no arquivo
  + Processo de rastreabilidade para lançamentos de IRRF
  + Preenchimento do campo data de contabilização no processo de regerar contabilização de baixa
  + Processo de alteração de conta/caixa e convênio para atualizar o campo Banco e Carteira no lançamento
  + Processo de alteração global para não permitir mudanças nos lançamentos de crédito de adiantamento
  + Processo de baixa com cheque para verificar a permissão de editar contabilização no lançamento
  + Processo de busca dos defaults contábeis de inclusão ao realizar uma baixa informando o evento contábil
  + Processo de inclusão do evento contábil do extrato.
  + Processo do tipo contábil de um extrato. Ao selecionar o tipo contábil A contabilizar o sistema limpa o campo FXCX.DATACONTABILIZ e o FXCX.NUMCONTABIL.
  + Processo de importação de lançamentos em arquivo texto para buscar as informações de contabilização definidas nas tabelas opcionais nos defaults do cliente fornecedor
  + Processo de geração de acordo para considerar lançamentos em outra moeda
* Otimizados:
  + Processo de envio de email pela visão de lançamentos e boletos para respeitar a seleção dos contatos do cliente fornecedor
  + Processo de baixa de lançamentos vinculados a devolução, mesmo com o valor da baixa sendo igual a zero.
  + Processo de emissão de cheque. Foi incluído um parâmetro no parametrizador para que ao emitir um cheque, os campos opcionais dos lançamentos sejam copiados para seus itens de baixa.
  + Processo de geração de Log ao estornar um lançamento na sessão de caixa. Agora o sistema não paga o IDBAIXA do LOG de baixa da sessão de caixa ao estornar.
  + Rotina de envio de email através da visão de boletos e visão de lançamentos para conseguir marcar/desmarcar todos os contatos de uma única vez
* O campo Tipo de Documento passa a ser exibido na visão de pesquisa da sessão de caixa.
* Ajustado o serviço de baixa no assinante de vinculo para que a lista de vinculo armazene todos os vinculo, quando existe mais de um contexto sendo executado pelo serviço.
BO3Gestão Fiscal

### [Help](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx) do TOTVS Gestão Fiscal.

* Para os registros do Bloco J, Bloco K, Bloco L, Bloco M310 e M360 que dependem de serviços do contábil para geração, serão gerados mediante Integração entre os módulos Gestão Fiscal x Gestão Contábil do RM.
* Adicionada mensagem informativa sobre a implementação referente a rotina ECF.
* Ajustes:
  + Edição do campo lançamento fiscal - Aba transporte/Modal Aéreo/Modal Aéreo/Tipo de tarifa.
  + Geração do registro E113 para não ser gerado em duplicidade.
  + Campo "Classificação" no cadastro de outros débitos/créditos para filiais do Paraná.
  + Envio da NFS-e de São Gonçalo - RJ.
  + Não permitir o envio de NFS-E e de substituição para o município de Sarzedo-MG.
  + Para que a TAG <<NRE>> seja preenchida com as informações do item e não do item referenciado.
  + Erros Encontrados pela Homologação CAT 79/2003
  + Geração do registro E200 para que sua geração respeite a mesma regra utilizada no período de apuração do ICMSST ao encerrá-lo.
  + Geração do SPED fiscal quando o lançamento fiscal possui as seguintes opções no campo Transporte| Transportadora| Via de Transporte:
* Melhorias:
  + Geração da ECF onde o campo 9 (MES\_BAL\_RED) do registro 0010 será preenchido conforme Layout.
  + Geração do registro G140 do SPED Fiscal para correta geração no arquivo.
  + Campo Lançamento Fiscal/Situação Tributária/Itens/Informações Adicionais/Referências/Campo Quantidade Exportada para aceitar quatro casas decimais.
  + Para não permitir a inclusão de lançamentos fiscais de CT-e cancelados no registro 1400
  + Consulta para carregar a Codificação Fiscal do Produto "TPRDCODFISCAL" no processo de importação da tabela IBPTAX.
  + Geração da rotina ECF - Escrituração contábil fiscal
  + Geração das informações dos Períodos de apuração com suspensão/balanço na rotina ECF - Escrituração Contábil Fiscal
  + Geração do bloco N - rotina ECF - Escrituração Contábil Fiscal
  + Referente a escrituração do valor de ICMS desonerado.
  + Processamento da contabilização pelo evento contábil para que quando o usuário utilizar fórmula e o valor processado der algumas dizimas exemplo, 12.83333, o sistema não aplique o arredondamento de 2 casas decimais para cada item, aplique somente o arredondamento no final do processamento da contabilização.
  + Integração com o TSS para permitir o envio do cancelamento da NFS-e de Itajaí com o motivo do cancelamento preenchido.
  + Geração do registro C197, campo 05 (VL\_BC\_ICMS) para considerar o valor do item - descontos + despesas.
* Modificado:
  + Processo de emissão da NFS-e para não validar SCHEMA para o município de São Gonçalo
  + Processo de emissão de NFS-e para gerar a TAG Natureza de operação baseado no conteúdo do campo complementar do item do movimento TIPOTRIBNFSE.
  + Processo de geração do movimento de NFS-e a partir do XML do RPS, para considerar a data de competência retornada pela prefeitura.
* Evoluída geração do registro C100 para contemplar regras de geração específicas de documentos de modelo 65.
* Geração da TAG <<REFNFe>> para o tipo de motivo de referência 13 - Devolução Simbólica de Mercadoria em Consignação - Estoque Terceiros.
* Grupo <<EXPORTIND>> só deve ser gerado para movimentos de exportação indiretos.
* Implementado:
  + Escrituração do ICMS Desonerado
  + Envio de NFS-e de Porto Velho - RO, validação para que não permita o envio de NFS-e de substituição para este município.
  + Envio de NFS-e para o município de Além Paraíba – MG - Município não permite o envio de NFS-e de substituição.
  + Envio de NFS-e para o município de Limeira - SP.
  + Envio de NFS-e para o município de Natal – RN - Município não possui processo de cancelamento e de substituição de NFS-e pelo Sistema.
  + Para que o valor do Drawback possa ser enviado em uma nota de exportação, sem que mesma necessite de ver movimentos referenciados.
  + Marítima, Fluvial, Lacustre, Postal, Conduto/Rede de Transmissão, Meios Próprios, Entrada/ Saída ficta, Courier e Handcarry.
  + Geração do Arquivo da rotina Estadual de SP CAT 79/2003.
* Otimizado:
  + Processo de processo de importação do layout EFD CONTRIBUIÇÕES.
  + Processo de envio de NFS-e para os municípios de Novo Hamburgo e São Leopoldo, campo código de serviço federal para os municípios de, não pode ter máscara
  + Log do processo de consulta de NFS-e por RPS.
  + Preenchimento da TAG <<cEanTrib>>.
  + Preenchimento do grupo de impostos
  + Processo de envio de XML por e-mail para que o mesmo só filtro os contatos do cliente fornecedor que estiverem ativos no sistema.
* Valores do campo VAFRMM deveriam ser preenchidos no item do movimento ao invés de ser no movimento e replicado para todos os itens.
* O processo de encerramento do período de apuração do tributo ICMS-ST foi alterado para considerar o crédito de ICMS-ST retido na chancela para os períodos posteriores.
BO4Gestão Patrimonial

### [Help](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.Bonum.aspx) do TOTVS Gestão Patrimonial.

* Atualizações:
  + Rotina de Fechamento de Período relativo à atualização de período já fechado.
  + Método de baixa de patrimônio para SGDB Oracle.
  + Método de validação do maior patrimônio da base.
  + Cálculo de Ocorrências de Acréscimo ou Transferência Monetária no primeiro dia do mês.
* Ajustes:
  + Relatórios de Agrupamento por Contas e Ficha de Imobilizado para buscar o valor base de depreciação ao invés do valor de aquisição.
  + Cálculo de depreciação de patrimônios que receberam Transferência Monetária de patrimônios com valor de aquisição igual a zero e totalmente depreciados. Neste caso não poderá ser gerado valor de ajuste.
  + Processo de contabilização da Transferência de Controle para que não seja apresentado comportamento inadequado ao contabilizar duas transferência de controle simultaneamente.
* Implementação o Relatórios de Depreciação dos patrimônios
* Melhoria no processo de Baixa para que seja possível especificar o valor de venda dos patrimônios por cenário de cálculo.
BO5Gestão Contábil

### [Help](http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.Saldus.aspx) do TOTVS Gestão Contábil.

* Melhorias:
  + SPED Contábil para utilização de Contas Gerenciais com mais de 25 caracteres.
  + Demonstrações Contábeis para que a opção “Total de Débito” seja gerada.
  + Evento Contábil para campo de Integração com Protheus.
  + Pré-validador do SPED Contábil para filtrar as filiais SCP normalmente.
  + Método de avaliação de estoque para a geração do registro L200 conforme o manual da ECF.
  + Apuração virtual para apurar resultado considerando o centro custo, isto em função da ECF.
  + Geração do SPED Contábil para desconsiderar o caractere TAB, que causa erro no PVA de conteúdo do campo inválido.
  + Parametrização da DLPA e DMPL e geração no SPED contábil com o objetivo de simplificar o entendimento.
* Ajustes:
  + SPED Contábil, onde o registro I350 aceita Históricos que contenham em sua descrição o carácter #.
  + Ferramenta de Demonstração Contábil para que a demonstração comparativa calcule os totalizadores sintéticos automaticamente.
  + Carregamento dos parâmetros na geração do SPED Contábil.
  + Exclusão das parametrizações das informações da ECF referente ao módulo contábil no cadastro de Filial.
  + Contabilização da baixa do lançamento financeiro quando utilizamos a classificação por centro de custo.
  + SPED Contábil se caso não enviar o registro I350/I355 o cálculo do registro J150 ficará incoerente.
* Implementado:
  + Evento contábil para buscar valor para os campos Item Contábil e Classe de Valor quando há integração com Protheus.
  + Evento contábil para buscar valor para os campos Item Contábil e Classe de Valor quando há integração do Educacional com Protheus.
* Modificações:
  + Cadastro de evento contábil de forma a permitir que seja incluído em base de dados do tipo ORACLE.
  + Cadastro de período de manutenção de usuário para que as datas informadas sejam atualizadas em ambiente 3 camadas.
  + Processo de agrupamento de lançamentos de forma a permitir que lançamentos contábeis originados no RM Liber possam ser agrupados seguindo a regra do processo.
  + Processo de Demonstração Contábil de forma a permitir que as informações sejam exibidas e executadas em ambiente 3 camadas.
  + Processo de desagrupamento de lançamentos para que seja possível desagrupar lançamentos de outros sistemas.
  + Processo de importação via conceito de forma a permitir a importação do plano de contas Contábil.
  + SPED FCONT de forma a permitir que o arquivo seja de acordo com as informações parametrizadas.
  + Ferramenta de Demonstrações Contábeis para considerar o filtro das contas parametrizadas a crédito.

EDUCACIONAL

## **Educacional**

3trueEDU1Educacional

### [Help](http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.totvsEducacional.aspx) do TOTVS Educacional.

* A geração do arquivo SISCEBAS foi alterado para calcular os valores das parcelas de acordo com as informações do financeiro e a de bolsas conforme dados contábeis.
* Ajustes:
  + Ao carregar informações da matrícula do aluno durante a execução do processo de "Matrícula de disciplina por substituição".
  + Exibição da mensagem quando não se preenche o período letivo de planejamento quando se tenta acessar os itens Turmas, Turmas / Disciplina, Plano de pagamento e Parametrização por curso na opção de planejamento dentro de Currículo e Oferta > Oferta > Mais.
  + Realização de uma reserva de recursos pelo portal caso o usuário não seja um professor.
  + Tela de cadastro de alunos para capturar dados de necessidades e recursos especiais necessários para o aluno realizar a prova do ENADE de acordo com o novo layout.
  + Visualização do Extrato Financeiro no portal do aluno, permitindo que sejam visualizados apenas boletos do nível de ensino selecionado.
  + Visualização do histórico no portal aluno, impedindo que seja gerada quebra de linha desnecessária no código da disciplina.
  + Cadastro de Histórico do Ensino Básico, permitindo que letras ou caracteres especiais sejam informados no campo Carga Horária.
  + Cálculo do número de meses restantes a serem contabilizados o qual não estava considerando as parcelas já contabilizadas
  + Cálculo do valor simulado das parcelas, durante a matrícula online, para que os créditos financeiros da turma/disciplina mista também sejam calculados.
  + Processo da Avaliação Institucional, permitindo que as avaliações também sejam cadastradas para professores de turmas sem matriz aplicada.
* Alteração:
  + Educacenso conforme leiaute de 2015.
  + Cadastro de Contrato do aluno, na aba Responsável Financeiro, o campo Percentual deverá permitir preencher somente com caracteres numéricos.
  + Menu “Assistentes | Criar parcelas”, para obedecer o parâmetro financeiro “Número de casas decimais” no campo Valor do Serviço.
  + Processo de inclusão de bolsa retroativa para permitir lançar Bolsa Exclusiva quando a parcela do aluno já existe uma bolsa lançada, porém o status da mesma encontra-se Inativo.
  + Processo de Inclusão/Exclusão de Bolsa Retroativa, quando o lançamento estiver baixado com cheque, o sistema deverá copiar os dados do cheque para o novo item de baixa gerado após a inclusão da bolsa retroativa. No extrato de caixa, o cheque será estornado (Saque Canc.Receb. Cheque) e gerado novamente extrato do tipo “Recebimento via Cheque” para a nova baixa.
  + Processo de Mudança de Turma para atribuir a data de matrícula da disciplina de origem para a nova matrícula na turma de destino.
  + Processo de Gerar Contabilização, para contabilizar a bolsa do contrato quando a conta contábil está marcada para gerar rateio gerencial.
  + Processo de inclusão/exclusão de bolsa retroativa para permitir a regeração de lançamento com movimento de NF-e já gerado, somente se o parâmetro da Bolsa Filial “Não considerar desconto” estiver marcado.
* Corrigida a consulta para que mostre os itens que estão marcados no campo "Recebe Bolsa de Apoio Social" da tela de Dados do curso para o Censo Escolar
* Criada a funcionalidade campos complementares de ocorrências do aluno.
* Otimizado:
  + Novo modelo de contabilização por competência de forma a evitar que o cálculo e parcelas a contabilizar seja feito de forma incorreta, o que acarretaria valores inválidos de contabilização. Foi feita otimização também para que diferenças residuais não sejam tratadas como aumento ou redução no valor acumulado por serviço.
  + Processo de bolsa retroativa de modo a suportar a inclusão de uma bolsa de crédito para quando a parcela já contém uma bolsa de crédito.
  + Processo de bolsa retroativa para que seja mantido o tipo contábil do lançamento financeiro após a execução do processo.
  + Processo de cancelamento de acordo, de forma que ao cancelar um acordo que tenha gerado um contrato financeiro, o sistema consiga excluir o contrato e suas dependências.
  + Processo de contabilização por competência para que o sistema não tente realizar a contabilização de um evento que não tenha tido as partidas contábeis carregadas durante o processamento do evento contábil.
  + Processo de geração de lançamentos de forma a não validar a conta caixa do responsável financeiro da parcela ao regerar lançamentos de bolsa de crédito.
  + Processo de pagamento de boletos por cartão de crédito, de forma que o pagamento seja permitido para os casos onde existam vínculo com cheque em baixas canceladas.
  + Processo de regeração de lançamentos cancelados, de forma que o cálculo residual da última parcela somente considere um único lançamento e calcule assim, o valor da parcela de forma correta.
  + Processo de remoção de bolsa retroativa de forma a ajustar o valor de bolsa existente no lançamento financeiro, para quando a mesma bolsa está aplicada mais de uma vez no contrato, porém para parcelas diferentes.
  + Lançamento quando parcela utiliza faixa de crédito e houve cancelamento de disciplinas parcial e total no mesmo período.
  + Performance da digitação de notas de avaliações do Portal.
  + Validação de choque de horários do professor na turma/disciplina para considerar data de participação do professor na turma.
  + Central do aluno para seu devido funcionamento após várias chamadas consecutivas desta funcionalidade.
  + Consulta do histórico financeiro do aluno no Portal.
  + Processo de contabilização através do menu “Financeiro/Contábil | Contabilidade”.
* Modificação no sistema:
  + Para permitir recuperar a informação dos parâmetros Matricula.Geral.MotivoAltStatusDisc Matricula.Geral.MotivoAltStatusPLetivo e salva-los ao executar as respectivas fórmulas.
  + Para exibir corretamente o nome da Disciplina no quadro de horários do aluno.
  + Para que seja possível utilizar o TBC com o DataSet EduAluno.
  + Para ajustar a conversão das datas no processo de personalização de plano de pagamento.
* Implementada validação da permissão do usuário ao emitir um relatório via portal. Na visão de emissão de relatórios no portal, só serão retornados os relatórios parametrizados no sistema e que o usuário tenha permissão para executá-lo.
* Inclusão da opção Tabela Default nos eventos contábeis com processos (Contrato Educacional e Parcela Contábil Educacional) para buscar a conta gerencial vinculada ao centro de custo.
* Melhoria:
  + Processo de atualizar endereço de pais e responsáveis, possibilitando que o usuário selecione qual dos telefones do aluno deve ser atualizados nos pais e responsáveis.
  + Processo de Matricula - Sistema passou a validar o parâmetro "Considerar documentos faltantes do tipo de ingresso, mesmo que não seja a primeira matrícula" para os documentos de Tipo = "Ingresso" no Ensino Básico.
  + Serviço para pagamento via cartão de crédito para que sejam exibidos os serviços do boleto selecionado no extrato financeiro do Portal, e não um texto fixo.
* Não permitir a alteração da validade da bolsa no contrato do aluno se a nova validade não englobar os atuais lançamentos gerados
* Padronização da mensagem de validação do Tipo de Usuário durante a matrícula online. Mensagem será visualizada na própria página e permitirá que o usuário altere o tipo de usuário para continuar com a matrícula.
Edu2Gestão Bibliotecária

### [Help](http://wikihelp.totvs.com.br/WikiHelp/BIB/BIB.Biblios.aspx) e do TOTVS Gestão Bibliotecária.

* Alterado estrutura de permissões de movimentações, para que a "Visão de Empréstimos" não seja dependente da permissão de "Movimentações", assim foi retirado o ícone do botão de "Movimentações" e adicionado ao lado com a mesma função.
* Otimizado:
  + Processo de geração de lançamentos de multas por devolução em atraso.
  + Processo de importação de usuários.
EDU3Processo Seletivo

### [Help](http://wikihelp.totvs.com.br/WikiHelp/EDUPS/EDUPS.processoSeletivo.aspx) e do TOTVS Processo Seletivo.

* Incluído:
  + Novo layout do arquivo de retorno com resultados da edição 2014 do ENEM fornecido pelo INEP.
  + Campos Tipo Rua e Tipo Bairro nos cadastros de candidatos e responsável no Processo Seletivo
* Otimizado:
  + Processo de cadastro de responsáveis no processo seletivo.
  + Processo de geração de segunda via de comprovante de inscrição.
  + Processo de parametrização do processo seletivo.
EDU4Avaliação e Pesquisa

### [Help](http://wikihelp.totvs.com.br/WikiHelp/TST/TST.testis.aspx) e do TOTVS Avaliação e Pesquisa.

* Ajuste na visualização das questões abertas no ranking de candidatos.
* Otimizado o processo de prova via Webservice no Totvs.

PROJETOS

## **Projetos**

4trueCP1Construção e Projetos

### [Help](http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Solum.aspx) e do TOTVS Obras e Projetos.

* Melhorias:
  + Cálculo da curva S para que o total da Curva S se encontre em um percentual aceitável em relação ao total do cronograma, diminuindo a perda de casas decimais para tarefas de valor cotado
  + Cálculo do Histograma.
  + Cópia de subprojetos, onde será verificado a hierarquia das tarefas durante e após a execução do processo.
  + Exportação de Planilhas de Atividade para o MS-Project
  + Tela de 'Consumir Objetos do Contrato' para salvar Layout definido pelo usuário na área 'Objetos a Consumir'.
  + Pedido Extra para impedir que o registro fique travado com o status "Em Faturamento"
  + Processo 'Importar Tarefas via MS Project'
  + Processo de liberação para Suprimento/Faturamento no Pedido de Material Extra
  + Campo "equipe" do Recurso da Composição para que seja exibido como decimal
  + Para que o cronograma base não seja recalculado e seus valores corretos sejam exibidos
  + Reajuste Default na liberação do Período, é aplicado quando o mesmo não for calculado manualmente ou automaticamente pelos processos que podem liberar o período do contrato.
  + processo de arredondamento de itens fracionados por rateio de produto.
  + para limitar o tamanho do campo de acordo com a capacidade de armazenamento da entidade de dados.
  + processo de cópia de itens, cópia todos os subprojetos do projeto e coligada origem.
  + Índice durante a impressão na tela do anexo Grid Fixo quando o projeto utilizar uma máscara grau 2 ou maior (###.##) definido na obra.
CP2Incorporação

### [Help](http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.SGI.aspx) do TOTVS Incorporação.

* Melhoria:

  + Simulador de reajuste
  + Ao excluir valores de origem da composição do POC
  + Geração da parcela de resíduo após quitar a última parcela
  + Processo de reajuste quando a periodicidade é maior que um
  + Ao verificar se a venda pode ser quitada. O processo passa a desconsiderar valores de resíduo inferiores ou igual a zero.
  + Exibição do cliente/fornecedor da subunidade quando a venda possui distrato.
  + Modalidade: modalidades globais não aplicarão eventos contábeis locais.
  + Aditivo de Alteração de Valor de Parcela para componentes do tipo Seguro Por Empreendimento.
  + Cálculo do seguro prestamista quando a venda possui parcelas canceladas.
  + Distrato de venda quando o sistema não permite data de vencimento anterior à data de emissão.
  + Processo de apuração POC.
  + Processo de atualização do plano de financiamento para MCMV.
  + Processo de reajuste das parcelas da venda.
  + Processo de reajuste, o mesmo passa desconsiderar todas as parcelas enviadas a banco.
  + Calcular o Valor Base para o reajuste quando o componente de CM for configurado para corrigir somente sobre o Saldo Devedor Principal será considerado somente o valor do componente do tipo Principal.
  + Reajuste de parcelas enviadas a banco quando o plano possui componente de resíduo.
  + Processo de DIMOB, desconsiderando Empreendimentos reservados
  + Aditivo de Renegociação de Contrato atualizando os valores no RM Fluxus.
  + Processo de Reajuste
  + Processo de reajuste de resíduo
* Alteração para voltar a gravar o histórico de reajuste da venda, tabelas XReajuste, XReajusteVenda e XReajusteComponenteParcela
* Alterada:

  + Criação da conexão do reajuste paralelo para manter o mesmo usuário conectado
  + Rotina de conversão para ignorar histórico de baixa de valor de integração para lançamentos cancelados
  + Rotina EFD bloco F200 para que o campo 22 passe a enviar os CPFs de todos os compradores ativos
  + Validação no momento de se efetivar o aditivo para ignorar a inexistência de lançamentos financeiros em parcelas canceladas
  + Validação no momento de se salvar o valor de integração do componente
  + Processo de reajuste para considerar corretamente a configuração de reajustar até o dia da data de vencimento para periodicidade maior que 1 e com o dia da data de vencimento sendo menor que o dia da data base para o reajuste
  + Chamada da alteração de lançamentos financeiros para incluir o usuário executante
* Alterado o processo de reajuste para que quando a venda tiver resíduo e o reajuste for no período do resíduo junto com a correção monetária e/ou do juros, o sistema gerar corretamente o histórico de reajuste dos componentes para que não seja gerado em duplicidade
* Alterados os valores disponíveis para seleção do tipo de Data Base no cadastro de componentes da modalidade nos componentes de juros e correção de modo que eles sejam os mesmos tratados no cadastro de componentes das regras do plano de financiamento
* Criado parâmetro para configurar o processo de reajuste para considerar a variação por periodicidade ao detectar deflação para poder ignorá-la
* Incluído atributo de visibilidade nos parâmetros necessários ao processo de recontabilização do distrato dentro da fórmula visual.
CP3ETO - Engenharia sob encomenda

### [Help](http://wikihelp.totvs.com.br/WikiHelp/ETO/ETO.EngenhariaSobEncomenda.aspx) e do TOTVS Planejamento e Controle da Produção.

* Melhorias:
  + Cálculo do MRPII, método CalculaDataFinalPrev, alterando a declaração da variável "resultado", recebendo datafimprev ao invés de min.value.
  + Recalculo .NET relacionando a valoração de custo indireto da estrutura.
  + Relacionada a apuração de custo de subproduto gerado no recalculo .NET.
  + Relacionando ao desempenho de materiais controlado por lote.
  + Relacionadas ao recálculo de custo .NET.
* Migração de recursos relacionando ao recalculo de custos .NET.
CP4Manutenção

### [Help](http://wikihelp.totvs.com.br/WikiHelp/MNT/MNT.Oficina.aspx) do TOTVS Manutenção.

* Melhorias:
  + Processo de apontamento de serviços da OS.
  + Processo de inclusão e faturamento da OS.

CRM

## **CRM**

5trueCRM1Gestão do Relacionamento com o Cliente

### [Help](http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.Agilis.aspx) do TOTVS Gestão do Relacionamento com o Cliente.

* Liberação:
  + Funcionalidade de Fórmulas Visuais no avanço de etapas no Portal.
  + Utilização de informações do TOTVS Educacional em parâmetros baseados em sentenças SQL no TGRC.
* Correção de inconsistência ao executar o serviço de "Inserir discussão/anexos a partir de e-mails"
* Adição de mensagem explicativa na inclusão de arquivos anexos ao atendimento sem atendente definido
* Otimização na execução de conceitos
