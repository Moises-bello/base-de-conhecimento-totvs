---
content_hash: 5fc31c98091e6dc72432638d63a157250f42f8f16b7662f965992624a29232f5
fetched_at: '2026-06-29T00:05:59.392923+00:00'
page_id: '190513450'
product: rm
source: tdn-rm
title: Release Versão 12.1.5
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=190513450
version: 66
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

## 

5CRM1

* TOTVS Gestão de Relacionamento com Cliente

---

# **RH**

# **RH**

1trueRH1Automação de Ponto

 [Help](http://wikihelp.totvs.com.br/WikiHelp/PTO/PTO.Chronus.aspx) e  do TOTVS Automação de Ponto.

 Adicionada tag segurança para as batidas de refeição no cadastro de visitantes.

* Aprimorada a aprovação de abonos pelo portal.
* Otimizada a integração de inclusão de funcionários com o Protheus.
* Otimizado:

  + recálculo, pelo espelho de ponto, para não carregar a etapa de agendamento de job ao utilizar 3 camadas.
  + processo de recálculo, com fracionamento de Jobs, enviando corretamente o código da coligada ao servidor.
  + visualização de horários, no portal, através da tela de alteração de horário do funcionário.
  + relatório do espelho de ponto, para impressão da descrição de abono nos dias corretos.
  + tag de segurança dos cadastros de Histórico de Horários e Histórico de Horários da Jornada
  + espelho de ponto para que o refresh seja executado automaticamente após o recálculo.
  + processo de definição do período ativo.
  + cálculo das horas extras, dentro do limite de refeição, quando a ausência planejada executada é menor que a planejada.
  + cálculo de ocorrências, dos funcionários admitidos no mês, com horário noturno, para não calcular horas de falta no dia da admissão referente a jornada do dia anterior.
  + lançamento de abonos, através do portal, para funcionários com jornada noturna.
  + lançamento de abonos, de forma global, quando o campo responsável não é preenchido.
  + lançamento global de abonos para não gerar 1 minuto de atraso indevido no cálculo
  + espelho de ponto, para não validar a existência da memória de cálculo sem executar o recálculo.
RH2Folha de Pagamento

 [Help](http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.Labore.aspx) e  do TOTVS Folha de Pagamento.

* Ajuste:
  + ao consistir saldo no cadastro de férias quando é utilizada férias somente com dias úteis.
  + nos campos DDD e Telefone do arquivo Seguro Desemprego. Caso a máscara do DDD seja ### (3 dígitos) o sistema passa a desconsiderar o primeiro dígito antes do DDD visto que não se conhece DDD com primeiro dígito diferente de zero. Ex: 018-3333-4444 sairá no arquivo 1833334444, 10 dígitos como contemplado no layout.
  + função NJTRAB, para retornar o valor correto.
  + importação de histórico de assistência saúde, quando o arquivo possui mais de uma linha, o mesmo apresentava erros na importação a partir do segundo registro.
  + módulo de Geração de Encargos para considerar o somatório de todos os eventos de CC 9 existentes no envelope, para efetuar o abatimento da 1a.parcela no FGTS 13o.
  + entrada de movimento via portal.
  + Cálculo de Dias Abono corridos na sugestão de férias via portal, quando os parâmetros do funcionário e do gestor divergem.

* Disponibilizada a implementação (Processo de Alteração Período Aquisitivo) na tela de Período Aquisitivo.
* Foi habilitada a possibilidade de alteração da tabela salarial no cadastro de salários compostos.
* Incluir no log de cálculo do evento de CC 9 a informação de que o valor dos eventos adicionais de 13o. serão acumulados no valor da 1a.parcela.
* Liberação:

  + Folha Analítica .Net (beta) para o cliente Queiroz Galvão.
  + Folha Analítica .Net para cliente piloto.
* Na DIRF para conferência foi otimizado a rotina de obtenção do valor fixo a deduzir para IRRF, obtendo o valor de acordo com a interseção do primeiro e último dia do mês em cada vigência. Havendo mais de uma vigência que o primeiro ou último dia do mês interceda ao início e fim da vigência será considerado o valor da vigência com data de início maior.
* Não exibir a situação Z (Admitido no próximo mês) na grade de seleção da geração do histórico de provisões.
* Na edição do funcionário o sistema irá atualizar os filtros de Função, Tabela Salarial, Faixa Salarial e Nível Salarial de acordo com os dados do funcionário corrente.
* Otimizada:

  + permissão do campo CIDADE do Endereço do funcionário, quando a permissão não foi dada para alterar o cadastro do funcionário.
  + permissão do campo Número da Ficha de Registro do funcionário, quando a permissão não foi dada para alterar o campo dentro do cadastro do funcionário.
  + validação de usuário existente para a mesma pessoa dentro do cadastro de funcionário.
* Otimizado:

  + processo de geração do relatório de salário contribuição em bases Oracle.
* Otimizado processo de Aprovação de Férias no Portal.
* Restrição de acesso à Folha Analítica .Net
RH3Gestão de Pessoas

 [Help](http://wikihelp.totvs.com.br/WikiHelp/RHU/RHU.Vitae.aspx) e  do TOTVS Gestão de Pessoas.

* Melhorias:

  + Acesso a Requisições através do Totvs Portal.
  + Filtro de perfil para o lookup de anotações pessoais.
  + Envio de e-mail da Avaliação de Desempenho por Competências.
  + Layout da Avaliação de Desempenho através do Totvs Portal.
* Otimizado:

  + Cadastro de Pessoas: o processo "Incluir pessoa como Candidato" finaliza corretamente e inclui a pessoa como "Candidato". Além disso, caso a Pessoa seja um Candidato, o menu "Papéis no Corpore" exibe o link "Candidatos".
  + Cadastro de novos Professores: quando for utilizado o recurso "Localizar pessoa", a unicidade do CPF não será validada quando não houver alteração no mesmo.
  + Cálculo da nota da Avaliação de Desempenho.
  + Filtro por nome do reclamante no cadastro de Processos Jurídicos.
  + Exclusão de Turmas.
* Reestruturação do cadastro de Pessoas quanto ao preenchimento do campo “CodUsuario”.
* Possibilidade de incluir E-mail Customizado para as etapas de Criação, Aprovação, Reprovação, Cancelamento e Conclusão em cada tipo de requisição. Esta definição possibilita a personalização dos e-mails enviados aos seus atuais responsáveis.
* Implementada a possibilidade de realizar a transferência de vários funcionários numa única requisição, através da Requisição de Transferência em Lote.
RH4Segurança e Medicina do Trabalho

 [Help](http://wikihelp.totvs.com.br/WikiHelp/SMT/SMT.VitaeSegurancaTrabalho.aspx) e  do TOTVS Segurança e Medicina do Trabalho.

* Otimizado o anexo EPI do catálogo de forma a contemplar locais de estoque com mesmo código em coligadas diferentes

 

# **BACKOFFICE**

## **BackOffice**

false2trueBO1Estoque, Compras e Faturamento

[Help](http://wikihelp.totvs.com.br/WikiHelp/EST/sEST.Nucleus.aspx) e  do TOTVS Gestão de Estoque, Compras e Faturamento.

* Nos processos onde existe a opção de importação/exportação para Excel não é mais obrigatório que se possua o Excel instalado na máquina. A importação/exportação ocorrerá sem a necessidade do Excel. Caso exista o Excel instalado, o mesmo continua sendo acionado no processo normalmente.
* Disponibilizado o processo de Integração com o Portal de Compras Paradigma.
* Agora os e-mails de repasse do Agilis, quando esse é integrado com outros sistemas, são executados fora da transação. Isso faz com que os relatórios que usem dados criados na transação sejam mostrados integralmente.
* Ajustes:

  + Reenchimento de dados de UF e Município da aba Coleta/Entrega (CTRC) para determinar o INÍCIO e FIM da prestação do serviço e a seleção do código CFOP correspondente.
  + Relatório .NET DACTE para que sejam impressos os veículos associados, bem como a visualização do campo da UF pertinente ao veículo transportador.
* Melhorias:

  + Processo de Inclusão de uma cotação, quando há integração com o Solum, para que o usuário possa informar parâmetros de filtro por rateio de Centro de Custo, Projeto, Tarefa e Grupo Orçamentário.
  + Processo de cotação permitindo que seja alterada a unidade do item cotado.
  + Impressão da descrição do Tipo de Veículo (Tração ou Reboque, equivalentes aos valores “0” ou “1”, respectivamente).
  + Processo de Exclusão de Movimentos.
  + Processo de criar novos produtos de grade numerada.
  + Processo de Regeração de Saldos e Custos.
  + Contrato.
  + Processo de Visualizar município do Tomador no relatório .NET.
* Atendimento à NT-001/2015 (CT-e).
BO2Gestão Financeira

[Help](http://wikihelp.totvs.com.br/WikiHelp/FIN/FIN.Fluxus.aspx) e  do TOTVS Gestão Financeira.

* Ajuste no serviço para que caso o campo "Inscrição Cedente (seg. opcional)" não tenha as suas posições configuradas do layout bancário não acuse erro e sim não preencha, pois o mesmo não é de preenchimento obrigatório.
* Melhorias:
  + Importação de baixa para que os erros de baixa de um lançamento não interfiram na baixa dos outros lançamentos.
  + Serviço de cálculo do valor líquido para criar o contexto de lançamentos criados a partir do RM Classis Ensino Básico.
  + Apresentação de código de lookup de tabelas opcionais.
  + Fórmula de DADOSPAGAMENTOBRADESCO.
  + Processo de importação de baixa em relação aos valores opcionais
  + Geração e cancelamento de acordo: Incluído campo Tipo Contábil, onde o usuário poderá informar um dos seguintes valores: Baixa Contábil ou Contábil, também permitindo que o campo fique em branco. Incluído os campos Valor Juros Acordo, Valor Desconto Acordo e Valor Acréscimo Acordo na visão de Lançamentos. No processo de cancelamento do acordo criado o campo “'Motivo do Cancelamento'. Criação de novas abas no Template de acordo e redistribuição dos campos.
  + Interface do sistema: A interface do sistema foi modificada, inserido ícones para os menus [Tabelas opcionais](http://fwrm-wiki:9999/WikiHelp/FIN/FIN.tabelaOpcional4.aspx), [Campos Complementares](http://wikihelp.totvs.com.br:1210/WikiHelp/GLB/GLB.CamposComplementares.aspx), [Centro de custo](http://wikihelp.totvs.com.br:1210/WikiHelp/CTB/CTB.cadastroCentroCustos.aspx), [Classificação de Centros de Custos](http://wikihelp.totvs.com.br:1210/WikiHelp/CTB/CTB.classificacaoCentroCustos.aspx), [Visualizar Tarefas Contábeis](http://fwrm-wiki:9999/WikiHelp/CTB/CTB.TarefasGerenciador.aspx), [Códigos de Receita](http://fwrm-wiki:9999/WikiHelp/FIN/FIN.codigoReceita.aspx), [tabela Cálculo INSS/IRRF](http://wikihelp.totvs.com.br:1210/WikiHelp/FOP/FOP.TabelasCalculos.aspx) e [Valores Fixos](http://wikihelp.totvs.com.br:1210/WikiHelp/FOP/FOP.ValoresFixos.aspx).
* Otimizado:
  + Processo de Baixa com Perda Financeira para ajuste do código que trata Coligada de Natureza Financeira para aceitar nulo caso este esteja nulo no banco de dados.
  + Processo de Exibir Repasse.  Sistema carrega todos os dados do Centro de Custo corretamente e exibe os nomes coerentes com os ícones de incluir, editar e excluir na tabela de destino do repasse.
  + Integração com o office.
  + Rotina de envio de e-mail através da visão de boletos e visão de lançamentos para conseguir marcar/desmarcar todos os contatos de uma única vez.
* Para o tipo de pagamento cartão, ao realizar a baixa de apenas um item de lançamento dentre vários itens utilizando um mesmo extrato de caixa, deve-se cancelar todo os itens da baixa.
* Processo de devolução de cheque não está finalizando o cheque de lançamentos que foram convertidos da baixa antiga para a nova.
* Criado campo “Contra Apresentação”, no processo de inclusão de [Boletos](http://fwrm-wiki:9999/WikiHelp/FIN/FIN.Boleto.aspx). Ao marcar a opção “Contra Apresentação” na inclusão de boleto será gerado código de barras com zeros (0000) na posição referente a data de vencimento. Se a conta/caixa utilizada no lançamento for HSBC, o cálculo do “Nosso Número” será realizado considerando zeros (0000) na variável data de vencimento utilizada.
* Separação de parâmetros do Contas a Pagar / Receber: 1) "Permite baixar Lançamentos com Borderô ou enviados ao Banco": Foi desmembrado, sendo que para o Contas a Pagar será: "Permite baixar Lançamentos a Pagar com [Borderô](http://fwrm-wiki:9999/WikiHelp/FIN/FIN.Bordero.aspx) gerado ou enviados para o Banco". Para o Contas a Receber será: "Permite baixar Lançamentos a Receber enviados para o Banco.
* Criação do Parâmetro "Permite Data do [Cheque](http://wikihelp.totvs.com.br:1210/WikiHelp/FIN/FIN.emissaorecebcheques.aspx) anterior à Data de Emissão do Lançamento". Através desse parâmetro, é possível permitir a Emissão ou Recebimento via cheque quando a data informada para o cheque for anterior à Data de Emissão do Lançamento.
BO3Gestão Fiscal

[Help](http://wikihelp.totvs.com.br/WikiHelp/FIS/FIS.Liber.aspx) e  do TOTVS Gestão Fiscal.

* Ajustes:
  + Geração dos campos de CNPJ e CPF no registro C600 da SEF II.
  + Validação referente a conversão do RMBonum
  + Processo de cópia de movimento.
  + Cálculo do Diferimento para emissão de NF-e: O percentual de diferimento no tributo do item só deverá ser preenchido quando a natureza for do tipo CST 51 e, caso o tipo de tributação for igual a "Diferido" o percentual será 100%, senão será retornado o valor do percentual de diferimento cadastrado no produto.
  + Para que as TAGs referentes a compras e transportadora não saiam em branco ou nulas no xml da NF-e.
  + Máscara da TAG << QEXPORT>> para que seja enviado como separador de casas decimais o ponto ao invés da virgula.
  + Envio da NFS-e de São Gonçalo - RJ, no preenchimento da TAG <<CNPJAUT>> do arquivo \_nfse001\_cfgambnfse001\_in.
* Efetuada melhoria para não permitir a inclusão de lançamentos fiscais de CT-e cancelados no registro 1400 do SPED Fiscal.
* Evoluído período de apuração do tributo RET quando possui evento tributário para identificar corretamente filiais SCP para tributos que não possuem seu cadastro de evento tributário migrado.
* Foi modificado o processo de geração da NF-e através do Totvs Colaboração 2.0 para considerar o Fator de conversão no cálculo da TAG << Qtrib>> mas não considerá-lo na TAG <<vUntrib>>
* Implementado:
  + Geração do registro C113 do SPED Fiscal para notas complementares.
  + Melhoria na importação IBPTax referente a duplicação de chaves primárias.
  + Ajuste na geração do registro E200 para que sua geração respeite a mesma regra utilizada no período de apuração do ICMS ST ao encerrá-lo.
  + Ajuste na geração do SPED fiscal quando o lançamento fiscal possui as seguintes opções no campo Transporte\Transportadora\Via de Transporte: Marítima,
  + Ajuste para permitir correto funcionamento do processo de importação do layout EFD\_CONTRIBUICOES\_B
  + NFS-e para o município de Esteio/RJ
  + NFS-e para o município de Porto Alegre/RS
  + NFS-e para o município de Novo Hamburgo/RS
  + NFS-e para o município de Ananindeua/PA
  + NFS-e para o município de Lauro de Freitas/BA
  + NFS-e modelo ABRASF para o município de Vila Velha/ES
  + Rotina Municipal - Declaração de Serviços Recebidos (DSR-e) – Recife
  + Rotina Federal - [Auto Declaração de Vendas](http://fwrm-wiki:20658/WikiHelp/FIS/FIS.INOVAR.aspx)- INOVAR Auto
  + Parte B do LALUR
  + Rotina Estadual de SP - [Portaria CAT 79/2003](http://wikihelp.totvs.com.br:1210/WikiHelp/FIS/FIS.CAT.aspx)
  + Para que o valor do Drawback possa ser enviado em uma nota de exportação, sem que mesma necessite de ver movimentos referenciados.
* Melhorada listagem de registros resultantes do processo "Cálculo Ficha de Conteúdo Importação" no anexo "FCI's do Produto".
* Otimização na validação do campo RECOPI no processo de envio da NF-e.
* Melhorias internas no Relatório da DANFE
* NF-e:
  + Envio do grupo de TAG << nProc>> referente ao cadastro de processo judicial
  + Criação dos tipos de transporte internacional 11=Courier; 12=Handcarry.
  + Modificado o processo de emissão da NF-e 3.10 quando o destinatário/remetente for do exterior para que o campo IDESTRANGEIRO seja gerado como nulo não obrigando o preenchimento da informação.
  + Modificado o processo de emissão da NF-e para gerar notas com desoneração de ICMS.
  + Modificado o processo de envio de e-mail automático para informar ao usuário quando o e-mail ou a mensagem não estiverem parametrizados.
  + Ajustado o processo de geração da NFS-e para não gerar a alíquota como decimal.
* Foi implementado o ajuste na tela de regra de ICMS para permitir que o campo "Dados ICMS\Alíquota" fique habilitado quando o tipo de tributação for Diferido.
* Foi modificado o processo de emissão de NF-e para que seja possível enviar IPI com CST 51. E passou a ser considerado o percentual de diferimento preenchido na linha do ICMS e não mais no cadastro do produto
* Foi modificado o processo de geração da NF-e para considerar nota de devolução todas as notas cujo o CFOP esteja configurado como devolução.
* Migração dos Eventos Tributários IRPJ e CSLL
* Foi modificado o processo de emissão da NF-e para permitir que a nota com CST 51 seja transmitida a SEFAZ sem levar as informações dos valores do ICMS
* Foi modificado o processo de geração da NF-e para que o log de erro completo seja apresentado nos casos em que o envio for realizado pela visão do movimento
BO4Gestão Patrimonial

[Help](http://wikihelp.totvs.com.br/WikiHelp/PAT/PAT.Bonum.aspx) e  do TOTVS Gestão Patrimonial.

* Otimização de inclusão de patrimônios, validando o maior código de patrimônio já incluído na base.
BO5Gestão Contábil

[Help](http://wikihelp.totvs.com.br/WikiHelp/CTB/CTB.Saldus.aspx) e  do TOTVS Gestão Contábil.

* Otimizado:
  + Relatório Balancete para que a data se apresente normalmente mesmo em computadores que estejam com formato de data diferente do brasileiro.
  + Relatórios para atender o filtro por Centro de Custo.
  + Parametrização da DLPA e DMPL e sua utilização no SPED contábil, objetivando simplificar o entendimento.
  + Mapa de Rateio, permitindo que vários lançamentos contábeis sejam analisados e suas respectivas distribuições sejam alteradas conforme parametrização no processo.
  + Agrupamento de Lançamentos, permitindo que lançamentos contábeis originados no TOTVS Gestão Fiscal, possam ser agrupados seguindo a regra do processo.
  + Geração da Demonstração Contábil, permitindo a execução em ambiente 3 camadas.
  + Transferência de Grupos Contábeis, permitindo o encerramento da conta de Destino quando o tipo for Origem\Destino\Receptoras.
  + Relatório Balancete, que passa a validar o código de Histórico padrão repetido na aba Filtros.
  + Relatório Balancete, onde os sinais serão impressos de acordo com tipo da conta.
  + Geração do SPED FCONT gerando o arquivo de acordo com as informações parametrizadas.
  + Geração do SPED Contábil caso não seja feito o envio do registro I350/I355 o cálculo do registro J150 ficará incoerente.
  + Relatório de Lançamentos Duplicados para filtrar pelo lote zero.
* Inclusão:
  + Relatório Razão de Cliente/Fornecedor Contábil.
  + Relatório Balanço Patrimonial.
  + Processo de Apuração Virtual.
* Desenvolvimento de layout 3.0 para geração de SPED Contábil referente ao ano base de 2014, para atendimento ao SCP mantida pelo Sócio Ostensivo.

EDUCACIONAL

## **Educacional**

3trueEDU1Educacional

[Help](http://wikihelp.totvs.com.br/WikiHelp/EDU/EDU.totvsEducacional.aspx) e  do TOTVS Educacional.

* Otimizado:
  + Matrícula on-line para que os documentos do tipo Ingresso que estejam pendentes, sejam reavaliados em novas matrículas.
  + Cadastro de professores e alunos ao utilizar pessoas existentes.
  + Processo de alteração da situação de matrícula na disciplina.
  + Processo de geração de usuário do Aluno para que a senha
  + Inclusão de bolsa retroativa para regerar lançamento somente do aluno selecionado na tela de parâmetros, quando existir o mesmo código de contrato para Registros Acadêmicos diferentes.
  + Processo de geração de lançamento, menu Financeiro/contábil | Financeiro.
  + Processo de Inclusão/Exclusão de Bolsa Retroativa, quando o lançamento estiver baixado com cheque, o sistema deverá copiar os dados do cheque para o novo item de baixa gerado após a inclusão da bolsa retroativa. No extrato de caixa, o cheque será estornado (Saque Canc.Receb. Cheque) e gerado novamente extrato do tipo “Recebimento via Cheque” para a nova baixa.
  + Processo de “Geração de Movimentos” para permitir gerar movimento quando o Tipo de Movimento não estiver integrado à NF-e, ou seja, quando contemplar as situações em que a Legislação não obriga gerar NF-e. Nesta alteração, passará a ser listados os Tipo de Movimento, cujo item de movimento esteja configurado como “Não Integrado” para todas as opções “NFS-e Municipal (Modelo Nacional)”, “NF-e Estadual” E “NF-e Municipal”. O usuário deverá ter permissão por tipo de movimento habilitado nas respectivas filiais.
  + Fórmulas do Educacional que utilizam dados do lançamento.
  + Seleção de turmas/disciplinas do Portal do coordenador.
  + Sistema para permitir o correto funcionamento de solicitações geradas com boleto.
* Melhorias:   
  + Mensagem de baixa de lançamentos a receber para tratamento na conversão de valores para adequação ao uso de '.' como padrão de separação de casas decimais.
  + Tela de frequência diária, devido a limitações de segurança o filtro não retornará mais de 1800 registros de frequência se o usuário possuir permissão para justificar as frequências e 3000 registros se o usuário não possuir permissão.
  + Cálculo do percentual de faltas, disponível no Quadro de Avisos no portal do aluno. Quando o aluno tiver faltas informadas na etapa final, esta será levada em consideração no cálculo do percentual, mesmo que a quantidade informada seja 0.
  + Filtro da tela de aprovação de ocorrência do portal do professor, evitando que alunos de outras turmas disciplinas apareçam.
  + Item Status do filtro da tela diário de classe do portal na aba notas etapa e notas avaliação, adicionando o item TODOS.
  + Para que a senha dos responsáveis seja a mesma senha do informada para o aluno.
  + Rotina do Censo Superior para considerar alunos formados que estejam com situação de matrícula que indica conclusão do curso e com a data de conclusão do curso menor ou igual a data de referência do censo.
  + Usabilidade do assistente de preparação de dados para o Censo do Ensino Superior:
  + Educacenso conforme layout de 2015.
  + Tratamentos das informações geradas para a integração por mensageria única dos sistemas Educacionais.
  + Sistema de forma que permita a listagem de alunos na tela de Enturmação em Turma Mista independente de sua situação de matricula.

* \* Inclusão de um botão para localizar os cursos/habilitações.  
   \* Possibilidade de mudar a data e localizar novamente os cursos/habilitações para a data nova.
* Alteração nos campos de mobilidade acadêmica para se adequarem às seguintes regras do INEP:

\* Tipo de mobilidade acadêmica: Campo de preenchimento obrigatório quando informada a opção “1 - Sim” no campo Mobilidade acadêmica e a IES é Federal ou Universidade Estadual.  
 \* IES destino: Campo de preenchimento obrigatório quando informada a opção “1 - Nacional” no campo Tipo de mobilidade acadêmica.  
 \* Tipo de mobilidade acadêmica internacional: Campo de preenchimento obrigatório em duas situações:  
 1) IES Federal ou Universidade estadual: se informada a opção “2 - Internacional” no campo Tipo de mobilidade acadêmica. 2) Demais IES: se informada a opção “1 – SIM” no campo Mobilidade Acadêmica.  
 \* País destino: Campo de preenchimento obrigatório quando informada qualquer opção no campo Tipo de mobilidade acadêmica internacional.

* Ao lançar bolsa retroativa, a data de contabilização de baixa será gravada de acordo com o Parâmetro Financeiro: Contas a Receber/ CONTAB. Baixa a Receber / “Data default da baixa a receber”.   
   O usuário poderá escolher as opções: Sistema, Baixa, Vencimento, Emissão, Previsão de Baixa, Cheque, Inclusão, Digitação, Comp.Cheque.
* Coluna R.A. disponibilizada para utilização em filtros na visão de Cursos/Habilitações.
* Ajuste no calendário online do aluno para exibir todas as suas avaliações, inclusive de turmas mistas.
* Processo de matricula de disciplina em lote permite remover as disciplinas optativas / eletivas da turma.
* Removida a obrigatoriedade do campo Descrição do Complemento da Disciplina.
* Implementado:
  + Mala direta que permite o usuário gerar arquivos de mala direta para registros de uma determinada consulta SQL, com base em um template pré-definido, existindo também a possibilidade do conteúdo do arquivo ser enviado no corpo do e-mail.
  + Assistente “Atualizar etapas da Turma/Disciplina” do Período Letivo e da Parametrização por Curso, a opção de excluir as etapas que não necessitam serem atualizadas.
* Alteração no processo de Cópia de Matriz Curricular: Para tornar o processo de cópia de matriz curricular mais flexível, foi implementado a opção de incluir ou excluir as disciplinas, além de definir o status da nova matriz curricular, antes de realizar o processo de cópia.
* Visualizar os dados das Avaliações no Portal: Permitir o professor/coordenador tenha acesso as demais informações pertinentes à avaliação no ato de sua escolha na digitação de notas.
* Parametrização de casas decimais para carga horária, créditos acadêmicos e créditos financeiros: Criado parâmetro que permite ao usuário configurar o sistema para exibir as informações de carga horária, créditos acadêmicos e créditos financeiros com o número de casas decimais que lhe for mais conveniente.
* Troca de turno na matrícula do período letivo: Implementado no processo de Mudar turma a opção de trocar o turno da matrícula no período letivo dos alunos que ainda não foram enturmados, e permitir ao usuário aproveitar o contrato para os alunos do Ensino Básico.
Edu2Gestão Bibliotecária

[Help](http://wikihelp.totvs.com.br/WikiHelp/BIB/BIB.Biblios.aspx) e do TOTVS Gestão Bibliotecária.

* Otimizado:
  + Processo de configuração de permissões para o TOTVS Gestão Bibliotecária.
  + Processo de consulta de publicações.
  + Processo de movimentação de acervo quando o usuário é aluno e funcionário.
EDU3Processo Seletivo

[Help](http://wikihelp.totvs.com.br/WikiHelp/EDUPS/EDUPS.processoSeletivo.aspx) e  do TOTVS Processo Seletivo.

* Melhoria no processo de confirmação de inscrição e alteração da forma de inscrição para tratarem situações geradas pela integração por mensageria única, no envio de uma mensagem lançamento financeiro e cancelamento de baixa financeira.
* Otimizado processo de registro de presença de candidatos em processos seletivos.
EDU4Avaliação e Pesquisa

[Help](http://wikihelp.totvs.com.br/WikiHelp/TST/TST.testis.aspx) e  do TOTVS Avaliação e Pesquisa.

* Ajuste na execução da Avaliação Institucional para que a data e hora de execução, visualizada no ranking a prova, seja a data e hora de gravação do registro.

PROJETOS

## **Projetos**

4trueCP1Construção e Projetos

[Help](http://wikihelp.totvs.com.br/WikiHelp/PRJ/PRJ.Solum.aspx) e  do TOTVS Obras e Projetos.

* Funcionalidade de encerramento de contratos permite definir o encerramento das atividades concluindo ou cancelando o contrato. Um checklist pode ser parametrizado e executado antes da finalização do contrato.
* Com o intuito de permitir que o TOP trabalhe de forma autônoma da solução da Microsoft, os processos via MS Excel e MS Project poderão ser executados independente do MS Office estar instalado na máquina onde o TOP está sendo executado.
* É possível importar arquivos EMOP com extensão \*.DBF sem utilização de licenças do MS Office.
* Possibilidade de utilizar a funcionalidade de rastreabilidade integrada com BackOffice Protheus.
* Funcionalidade de Concorrência Eletrônica foi migrada para tecnologia .NET e pode ser utilizada sem mudanças no comportamento.
* Possibilidade de controlar e formalizar o conteúdo de pedidos de alteração de escopo, assim como sua aceitação (aplicação ) ou negativa.
* Ajustes:
  + Cálculo de composições por produção que contêm recurso do tipo composição auxiliar de "Mão de Obra ou Equipamento".
  + Cálculo de composição.
  + Exclusão de associação de itens ao contrato.
  + Exportação para o Project, data início e fim não são enviadas com o parâmetro "enviar somente etapas".
  + Geração de cotação de planilha de serviços.
  + Anexo de impacto de tarefas para Insumos Globais.
  + Processo "Cancelar Liberação de Adiantamento" em ambiente integrado com BackOffice Protheus.
  + Execução da geração de Pedido de Material.
  + Execução do processo de rateio de produto em pedidos de materiais utilizando tarefas associadas a insumos globais.
  + Integração com PINI, onde unidades menores ou iguais a 5 caracteres que não existem na base não exibem a opção de selecionar um De/Para ou criar uma nova unidade.
  + Solicitação de envio de e-mail, quando os movimentos gerados pelos processos de integração gerarem um atendimento no CRM.
* Atualização do processo de geração do relatório de composição.
* Melhoria:
  + Performance ao inserir recurso em composições pela tela de edição.
  + Processo de Fluxo de Caixa integrado com Protheus.
* Realizado ajuste no carregamento de rateios de medição com a existência de medição zerada ou negativa.
CP2Incorporação

[Help](http://wikihelp.totvs.com.br/WikiHelp/IMB/IMB.SGI.aspx) e  do TOTVS Incorporação.

* A partir da versão 12.1.5 do TOTVS Incorporação, será permitido efetuar o reajuste de Contratos de Venda e também de Tabelas de Preços, acessando diversas coligadas simultaneamente através da utilização de Filtros. O processo foi evoluído para exibir ao usuário  os Contratos de Venda de todas as coligadas quais ele possua permissão para executar o reajuste.
* Inicialmente, ao abrir a tela do processo de reajuste do contrato de venda, o sistema exibirá  todas as coligadas , sendo que a Coligada corrente e todos os seus Empreendimentos selecionados.
* Os campos de data permitem informar um período  dentro de um mês, trazendo assim todos os reajustes pendentes de acordo com as seleções utilizadas  como filtro.
* Para a execução de reajuste de Tabelas de preço foi criada uma nova tela e um novo processo, permitindo ao usuário a visualização das tabelas de todas as coligadas quais possua permissão para a execução de reajustes. A visualização das Coligadas, Empreendimentos e tabelas de preços ocorre através de uma árvore de registros, que pode ser expandida ou recolhida, além de efetuar seleção e remoção de seleção de todos os registros exibidos na árvore. O sistema trará os itens da coligada corrente já selecionados e também permitirá que a filtragem dos registros seja complementada, utilizando o tipo de tabela de preços (Padrão, Secundária e Ambos) e período de vigência (Inicio de vigência e Fim de Vigência, sendo a data final um campo sem preenchimento obrigatório nos cadastros de Tabelas de Preços).
* Ajuste na importação de campos complementares de venda via *webservice*.
* Aprimorado
  + Forma de pesquisa e busca no Estande de Imóveis.
  + Processo que calcula a fórmula para gerar o valor de rescisão na operação de Distrato.
  + Processo de Aditivos, para o caso de vários aditivos utilizarem um mesmo comprador.
* Melhoria:
  + Campos de Contabilidade da tela de Modalidade.
  + Processo de Comissão, com intuito de armazenar informações de Coligadas nos Produtos e Serviços vinculados a Comissão.
  + Processo de Distrato dos contratos.
  + Mensagens do sistema. São exibidas nos processos de exclusão de lançamentos financeiros.
  + Função de fórmula que é usada para buscar o Valor do Saldo Devedor da Parcela Atualizado, o que possibilita uma melhor performance na execução e fórmulas que utilizam esta função.
  + Tela de Modelos de Contrato.
  + Tela de Proposta de Venda, no campo usado para selecionar a Modalidade.
  + Processo de contabilização de Apuração de Resultados (POC). Com isso, mesmo a subunidade que não esteja vinculada a uma venda, ao realizar a contabilização da Apuração, terá o complemento preenchido no lançamento contábil.
  + Padrões de segurança para os processos de Aditivos.
* No processo de Apuração de Resultados (POC), foram aprimorados os procedimentos de pesquisa e busca de vendas para o período solicitado no momento da apuração.
CP3ETO - Engenharia sob encomenda

[Help](http://wikihelp.totvs.com.br/WikiHelp/ETO/ETO.EngenhariaSobEncomenda.aspx) e do TOTVS Planejamento e Controle da Produção.

* Nos processos onde existe a opção de importação/exportação para Excel não é mais obrigatório que se possua o Excel instalado na máquina. A importação/exportação ocorrerá sem a necessidade do Excel. Caso exista o Excel instalado, o mesmo continua sendo acionado no processo normalmente.

CRM

## **CRM**

5trueCRM1Gestão do Relacionamento com o Cliente

[Help](http://wikihelp.totvs.com.br/WikiHelp/CRM/CRM.Agilis.aspx) e  do TOTVS Gestão do Relacionamento com o Cliente.

* Agora é possível gerar atendimento para clientes da coligada 0 (Global) pela activity de fórmula visual.
* Melhoria
  + Selecionar um parâmetro baseado em sentença SQL que utilize fórmula ou campos do atendimento no Portal.
  + Busca de atendimentos na fila quando o parâmetro "Restringir visualização de atendimentos por hierarquia de localidade" estiver marcado.
  + Execução de conceitos.
* Criação de um novo parâmetro que permite ao usuário selecionar um tipo de cliente default para que seja usado em uma nova solicitação do cliente online quando houver ambiguidade.
