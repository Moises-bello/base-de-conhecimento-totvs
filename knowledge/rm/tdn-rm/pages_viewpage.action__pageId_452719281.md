---
content_hash: 32d8525a76958ebfa31f6192b6dc3dd3aa24264a6dd780738d0b675d39ee6105
fetched_at: '2026-06-29T00:10:05.290052+00:00'
page_id: '452719281'
product: rm
source: tdn-rm
title: Novidades da Versão 11.40 FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719281
version: 3
---

Implementado no sistema a forma de atender à [LEI Nº 12.546, DE 14 DE DEZEMBRO DE 2011](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/lei%2012.546-2011?OpenDocument), referente ao recolhimento de INSS (parte empresa) para determinados segmentos.  
 Para atender a esta lei será utilizado o parâmetro "Faturamento Bruto" da pasta "Dados p/ INSS" do cadastro de seção.  
 Caso este campo esteja preenchido com valor da receita bruta e a competência do sistema seja a partir de 12/2011, o valor do campo Empresa será zerado na guia de INSS, pois o valor deste campo será recolhido via DARF.  
 Esta regra valerá para quaisquer segmentos que estejam com este valor preenchido no cadastro de seções a partir de 12/2011, exceto produtor rural. Portanto, este campo deverá ser preenchido somente se a empresa se encaixar nos parâmetros desta Lei.  
 Veja também [{+}](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm)<http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm+>   
 **Observação:** Consulte o Novo Ato Declaratório 93 GFIP Lei 12.546\_2011 sobre a aplicação da lei 12.546, com relação a GFIP.  
 **11.40.60- Lançamento financeiro.Net**   
 Inclusão da situação  Z - Admitido Próximo Mês no lançamento financeiro.  
    
 **11.40.60- Sefip.Net**  
 Otimizado a geração do Lançamento financeiro quando o parâmetro "Usar parâmetro especifico" estiver desmarcado.  
    
 **11.40.60- Cadastro de eventos**  
  Atualizado no cadastro de eventos, prioridade do campo ORDEMCALCULO.  
    
 **11.40.60- Termo de Rescisão de Contrato de Trabalho**  
 Otimizado relatório para atender a nova Portaria MTE Nº 1.057/2012.  
    
 **11.40.60- Sefip.Net**  
 Atualizada a geração relatório quando funcionário for demitido por transferência entre coligadas.   
 **11.40.55- Geração do Relatório Seguro desemprego-WEB**   
    
 Implementado o módulo Relatórios | Seguro desemprego atendendo a Resolução CODEFAT Nº 620, DE 5 DE NOVEMBRO DE 2009 e alterações introduzidas na Lei nº 7.998/90 e na legislação trabalhista.  
 Confira o help deste módulo e veja as orientações para gerar o relatório através desta nova funcionalidade.  
    
 **11.40.55- Entrada de dados**   
 Atualizado o processo entrada de dados ,quando for confirmado o parâmetro "Completar número da chapa com zeros a esquerda".  
    
 **11.40.55  -  Contabilização**  
 Atualizado o processo de contabilização quando o parâmetro "Aplicar arredondamento sobre o valor total do encargo" estiver confirmado em Cadastro|Contabilização|Encargos contábeis.  
    
 **11.40.55 – Sefip.Net**  
 Atualizada a geração do Sefip quando funcionario possuir menos de 15 dias trabalhados no ano passando a não gerar centavos no valor da base 13º salario.  
    
 **11.40.55 – Termo de rescisão de contrato**  
 Otimizado o relatório TRCT .  
    
 **11.40.55 – Histórico de Provisões**   
 Implementado o parâmetro  "Abate o valor  da diferença de férias do mês" em Rotinas| Geração Histórico de Provisões.   
    
 **11.40.55 – Cadastro de Fórmulas**  
 Implementada a variável T2,  esta variável retorna o valor da tabela, considerando o valor acima do teto.  
 Retorna valor de tabela T2 ('COD. TABELA', VALOR)  
 EX: T2 ('INSS', RC) - O sistema irá procurar a faixa do salário do funcionário na tabela de código INSS  
 **11.40.50 - Cadastro de Funcionários**  
 Otimizada a abertura da tela do cadastro de funcionários.  
    
 Ajuste na edição do Campo 'Jornada'.  
    
 Atualizado o Cadastro de Funcionários. Net.  
    
 **11.40.50 - Envelope**  
    
 Otimizado o recálculo ao forçar valores do envelope de pagamento.  
    
 **11.40.50 - Escala de Férias**  
    
 Ajustada a consulta SQL para retornar os dados da escala de férias, incluindo a tabela PSECAO para permitir a utilização no filtro de subordinados**.**  
    
 **11.40.50 - Férias**  
    
 Otimizado o cadastro de férias.  
    
 Ajustada a apresentação da tela de marcação de férias.  
    
 **11.40.50 - Lançamento de Eventos**  
    
 Otimizado o tratamento para efetuar corretamente o lançamento dos eventos relacionados do salário composto.  
    
 **11.40.50 - Lançamento Financeiro**  
    
 Ajuste no módulo de lançamento financeiro para preencher o código do departamento.  
    
 **11.40.50 - Linha de Transporte**  
    
 Ajustada a rotina de troca de código da linha de transporte.  
    
 **11.40.50 - MANAD**  
    
 Ajuste nas mensagens que informam as inconsistências no histórico de seção do funcionário ao gerar o arquivo.  
    
 Atualizada mensagem na geração do MANAD, quando o funcionário possuir histórico de seção diferente do cadastro.  
    
 **11.40.50 - Reprogramação Salarial**  
    
 Ajustada a reprogramação salarial para que eventos relacionados com valor zerado não sejam considerados.  
    
 **11.40.50 - RM PORTAL**  
    
 Otimizada a apresentação do histórico de férias ao clicar em 'Consulta de Férias'.  
    
 Otimizada a aprovação de férias pelo RM Portal.  
    
 Ajuste na apresentação dos dados de escala de férias no portal  
    
 **11.40.50 - SEFIP .NET**  
    
 Ajustado o processamento do sefip .Net para converter o campo Hora.  
    
 Ajustado o processamento do sefip .Net para retirar os espaços em branco do código da seção.  
    
 **11.40.50 - TRCT 1621/2010**  
    
 Ajustado para respeitar o parâmetro "IMPRIMIR VERBAS RESCISÓRIAS PRÉ-DEFINIDAS QUANDO VALOR IGUAL A ZERO".  
    
 Otimizado o preenchimento do campo 50 (dias e faltas).  
    
 **11.40.50 - Seções**  
    
 Ajustado o processo de troca de código de seção.  
    
 **11.40.45 - Cadastro de Funcionários**  
    
 Otimizada a edição do campo 'Jornada'.  
    
 Otimizada a apresentação da tela de marcação de férias.  
    
 **11.40.40 - Contabilização**  
    
 Ajustado o processo de contabilização para verificar o período no parâmetro local do sistema.  
    
 **11.40.40 - TRCT 1621/2010**  
    
 Ajuste no relatório TRCT para correto preenchimento do campo 9.  
    
 **11.40.40 - Rescisão Complementar**  
    
 Otimizado o cálculo da rescisão complementar para considerar eventos de outras rescisões complementares para o cálculo de médias.  
    
 **11.40.40 - Rateio de Tomadores**  
    
 Ajuste na tela de rateio de tomadores  
    
 **11.40.40 - Cadastro de Funcionários**  
    
 Ajuste no cadastro de funcionário para não exigir carteira de trabalho para estagiários.  
    
 Ajuste no cadastro de funcionário para funcionário com mais de 80 anos.  
    
 **11.40.40 - Geração do MANAD**  
    
 Otimizada a geração do arquivo MANAD com o registro K200.  
    
 Otimizada a geração do arquivo MANAD para não identificar autonomos através do CPF.  
    
 **11.40.40 - Histórico de Provisões**  
    
 Melhoria na segurança da tela de Histórico de Provisões .Net.  
    
 **11.40.35 - Guia de INSS**  
 Implementado no sistema a forma de atender as normas complementares referente à contribuição previdenciária sobre a receita bruta que prevê a desoneração da folha de pagamento das empresas enquadradas na Lei 12.546/2011  
    
 Foi criado a tela de cadastro 'Parâmetros da Guia de INSS Desoneração' disponível no menu 'Relatórios*|*Guia de INSS', que deve ser abastecida antes da geração da guia de INSS para empresas que possuem o percentual redutor para aplicar no campo parte empresa da guia.  
    
 Esta regra valerá para quaisquer segmentos que estejam com este valor preenchido no cadastro de 'Parâmetros da Guia de INSS Desoneração' disponível no menu 'Relatórios*|*Guia de INSS'. Portanto, este campo deverá ser preenchido somente se a empresa se encaixar nos parâmetros desta Lei.  
    
 Veja também [{+}](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm)<http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm+>   
 **11.40.35 - RM Portal**  
 Otimizada a disposição dos campos na tela do RM Portal.  
 Otimizado o processo de 'Aprovação de batidas em grupo'.  
 O sistema passou a validar o número de dias de direito de férias do colaborador em 'Solicitação de Férias'.  
 Otimizada a geração do Informe de Rendimentos através do RM Portal.  
 Ajustada a numeração das informações que são impressas no relatório Informe de Rendimentos, tópico 7 - Informações Complementares e alterada a mensagem do rodapé para 'DISPENSA ASSINATURA CONFORME IN RFB N 1.215 DE 15/12/2011'.  
 **11.40.35 - Rescisão Complementar**  
 Otimizado o cálculo da rescisão complementar no mesmo mês da rescisão complementar.  
 **11.40.35 - Funcionário .Net**  
 Otimizado o preenchimento do campo CEP ao cadastrar um novo funcionário.  
 Otimizado o preenchimento do campo exame médico.  
 Otimizada a inclusão de um novo funcionário estando o parâmetro 'Somente inclui funcionários em processo de Admissão no RM Vitae' marcado.  
 **11.40.35 - Diferença Salarial**  
 Otimizado o cálculo da diferença salarial.  
 **11.40.35 - Processo de admissão RM Labore X RM Vitae**  
 Otimizado o processo de admissão integrado RM Labore X RM Vitae.  
 **11.40.35 - Guia de INSS**  
 Otimizada a geração da Guia de INSS (GPS) ao utilizar a integração com RM Fluxus e RM Nucleus.  
 **11.40.35 - Cadastro de Eventos**  
 Otimizada o complemento de histórico da contabilização na geração dos lançamentos contábeis.  
 **11.40.35 - TRCT Portaria 1621/2010**  
 O sistema passou a buscar os dados das seções centralizadores na geração do relatório.  
 Otimizada a geração do relatório para levar para o campo 21 'Tipo de Contrato' o código informado no campo 'vínculo' da pasta RAIS, para o campo 27 'Cód. afastamento' os códigos de afastamento informados pelo Caixa Econômica Federal e para o campo 23 'Remuneração Mês Anterior Afast' passou a somar somente os proventos relacionados ao salário.  
 **11.40.35 - DIRF\Informe de rendimentos**  
 Otimizada a geração da DIRF/Informe de Rendimentos.  
 **11.40.35 - Diferença de 13º Salário**  
 Otimizado o cálculo da diferença de 13º Salário.  
 **11.40.35 - Grupo de Eventos .Net**  
 Otimizada a visualização dos registros dos eventos de integração.  
 **11.40.35 - Comparativo SEFIP x Folha Analítica**  
 Otimizada a geração do arquivo de comparação das bases de SEFIP e Folha Analítica.  
 **11.40.35 - MANAD**  
 Otimizada a geração do arquivo para considerar os estagiários, quando informado a categoria '00'.  
 **11.40.35 - Permissões de Acesso**  
 Otimizada as permissões de acesso a menus através da nova MDI.  
 **11.40.35 - Importação de Movimento .Net**  
 Otimizada a importação de movimento ao selecionar o flag 'Altera data de pagamento'.  
 **11.40.30 - Guia de INSS**  
    
 **11.40.30- Parâmetros RM Labore** Implementado o parâmetro "Gera contabilização no Labore antes de enviar para o Saldus" em opções|Parametros| RM Labore|Outros Parâmetros|Parâmetros II . Confirmando este parâmetro ao gerar o lote contábil os lançamentos serão visualizados no menu Cadatros|Contabilização|Lançamentos contábeis (RM Labore), caso contrário ,serão visualizados em Cadatros|Contabilização|Lançamentos contábeis (RM Saldus).  
    
 **11.40.30 – Sefip.Net**

* Atualizada a geração do lançamento financeiro na geração do Sefip para considerar fórmula informada no complemento de histórico.
* Atualizada a geração do sefip retroativo para funcionarios afastados tipo T-Acidente de trabalho.
* Atualizada a geração do sefip quando confirmado o parâmetro "Importar valores de retenção RM Nucleus".
* Atualizada a geração do Sefip para considerar os afastamentos já pagos em meses anteriores.
* Alterada a localização do parâmetro "Considerar valor de aviso prévio no SEFIP" ,a partir desta versão, será encontrado em OPÇÕES | PARÂMETROS | RMLABORE | PARÂMETROS DE RESCISÃO." 11.40.30 – Homolognet
* Atualizada a geração do Homolognet para levar a causa de afastamento correta para rescisões do tipo T - Término de Contrato e não gerar o arquivo xml para funcionários com menos de um ano de casa.

**11.40.30 -Consulta Movimentação da Integração**  
 Atualizada a visualização da tela Consulta Movimentação da Integração.  
    
 **11.40.30 -Lançamento financeiro.Net**  
 Atualizada a rotina de lançamento financeiro permitindo a geração do liquido de rescisão utilizando fórmula.  
 **11.40.30 - Portal**  
 Atualizada a inclusão,alteração e exclusão no processo de "Entrada de movimento" através do portal.   
    
 **11.40.30 -Funcionarios.Net**  
 Atualizado o processo de inclusão de funcionários.Net quando for integrado com RMVitae e possuir requisição de Admissão**.**  
    
 **11.40.10- Fórmulas**   
 Atualizada a função de fórmula A (acumulador) para aceitar até 100 acumuladores.  
    
 **11.40.10- Manad**  
 Atualizada a geração do manad,quando existir evento de 13 salário código de cálculo 9.  
    
 **11.40.10- Sefip.Net**   
 Atualizada a exclusão do lançamento financeiro do sefip através do aplicativo RMFLUXUS.  
    
 **11.40.10 -Homolognet**   
 Atualizada a importação do arquivo XML no programa Homolognet.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.40.10 -Fórmulas.Net**

* Ajuste e melhorias nas variáveis de fórmulas. NET.
* Criada a função de fórmula LIQFERIASDATA(Data1,Data2,tipo)Retorna o valor líquido do recibo com situações marcadas ou pagas, verificando a data de pagamento,o tipo e o intervalo informado.Os tipos são:Tipo 0 Retorna o somatório do Líquido de todos os recibos nas situações Marcadas ou Pagas, com data de pagamento no intervalo informado.Tipo 1 = Retorna o líquido do primeiro recibo nas situações Marcadas ou Pagas, com data de pagamento no intervalo informado.Tipo 2 =Retorna o líquido do último Recibo nas situações Marcadas ou Pagas, com data de pagamento no intervalo informado.

**11.40.10- Código de Calculo 46**   
 Atualizado o calculo da Base FGTS para evento com Código de Cálculo 46.  
    
 **11.40.10- Ferias.Net**  
 Atualizado o lançamento das Ferias.Net no calculo da rescisão.Net  
    
 **11.40.10- Diferença 13 Salario.Net**  
 Atualizado o cálculo da Diferença 13 salário.Net  
    
 **11.40.5 - Contabilização.Net**  
 Atualizada a data da contabilização gravada no perfil na geração do relatório contabilização.net.  
    
 **11.40.5 – Gestão Educacional**  
 Atualizado o lançamento dos eventos da integração do módulo Gestão Educacional através do menu "LANCAMENTOS DE EVENTOS POR CENTRO DE CUSTO .NET" .  
    
 **11.40.5 – Sefip.Net**   
 Atualizada a geração do Sefip.Net quando for confirmada a opção "Usa parametrização" na aba lançamento financeiro.  
    
 **11.40.5 – Sefip.Net – Lançamento Financeiro**  
 Atualizado o Lançamento Financeiro do Sefip.Net passando a ratear por Centro de Custo e Natureza Financeira, parâmetros do do RMFluxus.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.40.5 - Cadastro de Funcionários.Net**  
 Atualizada a inclusão do dependente preenchendo automático o campo "Numero".  
    
 **11.40.5 – Envelope.Net**

* Atualizado o lançamento do código de calculo 20 e 21 somente quando o período estiver criado.
* Atualizado o Rateio de eventos por Centro de Custo.
* Atualizada a proporcionalização de Salário Composto quando o evento é do tipo Dia.

**11.40.5 – Log de Cálculo**  
 Atualizado a apresentação do Log de Cálculo quando o processo é gerado para mais de um funcionário. O sistema deixou de demonstrar o debug de cálculo e média, devendo o usuário visualizar o log no funcionário.  
    
 **11.40.5 – Fórmulas**

* Atualizada a variável RANT passando a não considerar eventos que incidem em salário.
* Atualizada o calculo da variável C passando a verificar o parametro local.

**11.40.5 – Férias.Net**

* Atualizado no processo Finaliza Ferias o lançamento do evento 131-INSS FÉRIAS MÊS ANTERIOR.
* Atualizado o cálculo de férias em dobro, quando ocorre perda de período aquisitivo devido a afastamento em períodos posteriores ao período dobrado.
* Atualizada o calculo das Férias Vencidas e das Ferias Proporcionais quando a data de vencimento é no mês da rescisão.

**11.40.5 – Rescisão.Net**

* Atualizada o cálculo das médias de férias quando existir período de médias diferenciado.
* Atualizado o calculo de Ferias indenizadas quando o parâmetro 'Soma avos ref. aviso após calculo' estiver marcado e a data de demissão estiver no mês de vencimento do período aquisitivo.
* Ajustado o lançamento do liquido de rescisão próximo mês quando o período atual esta bloqueado.

**11.40.5 – Geração Histórico de Provisões.Net**

* Atualizada o calculo da Provisão.Net quando no envelope do funcionário estiver valores forçados.
* Atualizada a contagem de avos na provisão de férias quando usuário adianta dois períodos de gozo.

**11.40.5 – Contabilização.Net**  
 Atualizado a geração retroativa da Contabilização.Net.  
    
 **11.40.5 – Liberação de Competência**  
 Atualizado a liberação de competência quando o funcionário tem retorno de afastamento no mês.  
    
 **11.40.5 – Parâmetros do Sistema**  
 Ajustado o parâmetro 'Separar Média de Férias Vencidas e Proporcionais na Rescisão' possibilitando informar a data em que as médias passaram a ser separadas.  
    
 **11.40.0 - Cadastro de Funcionários**

* Otimizado o cadastro de funcionários a partir de uma PESSOA já existente.
* Aumentado o tamanho da coluna 'Desc. Motivo' para visualizar as descrições do histórico de situação com mais de 50 caracteres.

**11.40.0 - Rescisão**  
 Otimizada a rotina de transferência de funcionário para atualizar a jornada de trabalho no cadastro do funcionário ao marcar o parâmetro 'Altera chapa do funcionário demitido'.  
    
 **11.40.0 - Cadastro de Eventos**

* Otimizada a visualização das incidências de desconto 'Dedutível IRRF' e 'Estorna IRRF', 'Dedutível IRRF Férias' e 'Dedutível IRRF 13º'.
* Ao incluir um novo evento com o tipo 'Provento' e marcar a incidência 'FGTS', o sistema passou a desabilitar a incidência 'Incide FGTS 13º Salário'.
* Acertado o posicionamento dos campos 'Fórmula de Valor' e 'Opções de fórmulas'.
* Foi ajustado o campo 'Procurar por:' para trazer os campos 'Evento Obrigatório', 'Compõe Salário' e 'Evento de Insuficiência de Saldos', ao ser selecionado.

**11.40.0 - Tarifas de transporte**  
 Aumentado o campo 'Código' para aceitar até quatro caracteres no cadastro da tarifa de transporte.  
    
 **11.40.0 - Linhas de Transporte**  
 Criado o campo 'Ativo', deverá ser utilizado quando o usuário desejar desativar/ativar uma linha de transporte.  
    
 **11.40.0 - Chefes e Supervisores**  
 O sistema passou a preencher automaticamente a data de término do cadastro de chefe/supervisor ao realizar a transferência do funcionário quando a seção do funcionário for alterada no cadastro de funcionários.  
    
 **11.40.0 - Moedas e Índices**  
 Otimizado a liberação de licença para os cadastros de moedas e cotações através do RM Labore.  
    
 **11.40.0 - Cadastro de Perfis**  
 Otimizado o filtro de Perfil para trazer somente os dados do filtro cadastrado e selecionado.  
    
 **11.40.0 - Cálculo da Diferença Salarial**  
 Ajustado o cálculo da diferença salarial retroativo para funcionários com valores de pensão alimentícia para um ou mais dependentes.  
    
 **11.40.0 - Contabilização**  
 Ajustada a geração da contabilização de meses retroativos, para o sistema considerar a filial contábil do histórico da seção.  
    
 **11.40.0 - Sefip .Net**  
 Otimizada a geração do arquivo SEFIP.RE no mês de janeiro.  
    
 **11.40.0 - Passivo Trabalhista**  
 Criado o botão 'Executa Fórm. Dias aviso do Sind.' na tela de geração do Passivo Trabalhista, quando for informado o campo 'Chapa' na grade de seleção de funcionários.  
    
 **11.40.0 - Avisos Automáticos**  
 Criado o tipo de aviso automático '11 - Admissão de candidatos'. Este tipo de aviso automático será disparado ao efetuar uma admissão de candidato. Este tipo de aviso somente estará disponível quando estiver integrado com o RM Vitae.  
    
 **11.40.0 - RM Portal**  
 Otimizado o processo de enviar e-mail para a chapa informada no parâmetro 'Enviar aviso no RM LABORE para o funcionário' ao iniciar o processo de admissão de um funcionário.   
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
 **11.40.0 - Cadastro de Funcionários.Net**

* Atualizada visualização do campo Salário Hora, considerando a funcionalidade do parâmetro do sistema "Permite salário hora com mais de duas casas decimais".
* Atualizado a visualização do Histórico Salarial no Cadastro de Funcionários.Net em relação ao parâmetro do sistema disponível em "Opções|Parâmetros|Outros Parâmetros <Edita Data de Processamento>".
* Atualizado o campo VINCULO RAIS que deixa de ser obrigatório para funcionários do tipo Estagiários, Diretores, Autônomos e Conselheiros.
* ```
  Implementado no Cadastro de Funcionário.Net o item \[Históricos\], onde é apresentada uma aba para cada histórico, melhorando a usabilidade.
  ```
* Implementado no Cadastro de Funcionário.Net ícones de atalhos para alguns Anexos e Processos.
* Atualizado na Ficha Financeira.Net a apresentação dos campos da aba 'Verbas geradas por diferença' e a criação do campo 'Período'.

**11.40.0 - Cadastro de Eventos**  
 Atualizada a rotina de "Copiar eventos entre coligadas" e "Copiar grupo de evento entre coligadas" quando utiliza Lançamentos Vinculados.  
    
 **11.40.0 - Diferença de Pensão**  
 Atualizado cálculo de Diferença Salarial quando existe movimento de pensão calculado sobre Salário Mínimo.  
    
 **11.40.0 - Férias**  
 Atualizada rotina de antecipação de férias, permitindo que sejam calculadas/lançadas férias antecipadas, mesmo que já tenham sido antecipados dias de férias anteriormente.  
    
 **11.40.0 - Férias Coletivas**  
 Atualizado o funcionamento do parâmetro sindical 'Maiores 50 anos podem ter férias partidas' no cálculo de Férias Coletivas.  
    
 **11.40.0 - Parâmetro de RH**  
 Atualizada a tela de OPÇÕES/PARÂMETROS/RH, passando a limitar a quantidade de dígitos do campo CÓDIGO DE QUEBRA PARA CNPJ de forma que seja menor ou igual a MÁSCARA DE SEÇÃO.
