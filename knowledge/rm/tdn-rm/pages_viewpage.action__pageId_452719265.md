---
content_hash: 9c6560f66bee80bffb1b1d18b2778db978e08d9518157b123e1eb0f478bc8827
fetched_at: '2026-06-29T00:10:04.903802+00:00'
page_id: '452719265'
product: rm
source: tdn-rm
title: Novidades da Versão Anterior FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719265
version: 80
---

**12.1.19 – Mandato Sindical Ônus Empregador**  
 Criado o novo tipo "N" de afastamento. É utilizado quando um funcionário foi afastado por mandato sindical, porém o empregador continua arcando com os custos do funcionário.  
    
 **12.1.19 – Novos Códigos de Cálculos**  
 Devido a necessidade de adaptação de algumas verbas rescisórias às novas regras do eSocial, será necessária a criação de novos eventos com códigos de cálculo abaixo:  
      - 365: FÉRIAS EM DOBRO RESCISÃO  
      - 366: ADICIONAL 1/3 FÉRIAS EM DOBRO RESCISÃO  
      - 367: ADICIONAL 1/3 FÉRIAS VENCIDAS RESCISÃO  
      - 368: DIFERENÇA 1/3 FÉRIAS VENCIDAS RESCISÃO  
      - 369: ADICIONAL 1/3 FÉRIAS PROPORCIONAIS RESCISÃO  
      - 370: DIFERENÇA 1/3 FÉRIAS PROPORCIONAIS RESCISÃO  
      - 371: SEGUNDA PARCELA 13° LICENÇA MATERNIDADE PROVENTO  
      - 372: DIFERENÇA 13° SALÁRIO LICENÇA MATERNIDADE PROVENTO  
      - 373: 13° RESCISÃO LICENÇA MATERNIDADE PROVENTO  
      - 374: DIFERENÇA 13° RESCISÃO LIC. MATERNIDADE PROVENTO  
    
 **12.1.19 – Férias | Marcação**  
 Foi implementado uma nova visão que mostra o início e fim do período aquisitivo, o saldo de férias e a data limite de gozo de cada funcionário.  
    
 **12.1.19 – Férias | Coletivas Globais | Parâmetro "Limita aos dias de direito"**  
 Criado o parâmetro "Limita aos dias de direito" no processo de Férias Coletivas/Globais. Este parâmetro tem como objetivo limitar os dias de gozo do funcionário, caso ele tenha um saldo de dias inferior ao que apresenta no campo "Dias de férias".  
    
 **11.83.52 - eSocial**   
 Nesta versão, foram adaptados e implementados cadastrados para contemplar o eSocial. Nomeamos estas adaptações e implementações como 1º pacote do eSocial. Os cadastros e processos listados abaixo contém novidades para o eSocial e estas novidades estão descritos no "Boletim Técnico – Manual de implementações do eSocial" disponível em:   
 [{+}](http://tdn.totvs.com/display/rm/FOP_BT_eSocial_BR_RFOP002)<http://tdn.totvs.com/display/rm/FOP_BT_eSocial_BR_RFOP002+>  
    
 ·         Cadastros existentes:  
 ü  [Funcionários e/ou Pessoas](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Eventos](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Seções](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Ocorrência de Acidente de Trabalho (CAT)](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Processos Jurídicos](http://wikihelp.totvs.com.br:11800Forms);  
    
 ·         Novos cadastros:  
 ü  [Empregador](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Software House](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Profissional da Saúde](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [Cadastro Órgão de Classe](http://wikihelp.totvs.com.br:11800Forms);   
    
 ·         Novos parâmetros:  
 ü  [eSocial (Folha de Pagamento)](http://wikihelp.totvs.com.br:11800Forms);  
 ü  [ASO (SMT)](http://wikihelp.totvs.com.br:11800Forms);  
    
 ·         Novo processo;  
   ü  [Gerar Carga Inicial](http://wikihelp.totvs.com.br:11800Forms).  
    
 **11.82.29-Grupo de eventos (Assistente)**  
 Alterada a nomenclatura do Menu "GRUPO DE EVENTOS (ASSISTENTE) para "LANÇAMENTOS MULTI-COLIGADAS"  
    
 **11.82.29- Recesso de Estagiário**   
 Implementado o tratamento para Recesso de Estagiário.  
 A Lei nº 11.788, de 25 de setembro de 2008 instituiu o novo regramento para a elaboração dos estágios profissionais entre estudantes, as empresas e as instituições de ensino, estabelecendo regras mais rígidas para a elaboração dos contratos e assegurando novos direitos aos estagiários. Dentre os direitos assegurados está o recesso remunerado.  
 [{+}](http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm)<http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm+><http://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11788.htm>  
    
 ***Art. 13****. É assegurado ao estagiário, sempre que o estágio tenha duração igual ou superior a 1 (um) ano, período de recesso de 30 (trinta) dias, a ser gozado preferencialmente durante suas férias escolares.* ***§ 1o****O recesso de que trata este artigo deverá ser remunerado quando o estagiário receber bolsa ou outra forma de contraprestação.* ***§ 2o****Os dias de recesso previstos neste artigo serão concedidos de maneira proporcional, nos casos de o estágio ter duração inferior a 1 (um) ano.*  
    
 **11.82.27- Importação de movimento**   
 Evolução no processo de importação do movimento quando selecionado Importação por centro de custo.  
    
 **11.82.27- Funcionários.Net**  
 ·          Evolução no cadastro funcionários.Incluído o  campo 'Fumante' para filtro.      
 ·          Evolução na inclusão de um  novo funcionário quando o banco e Agência a serem utilizados forem default.  
    
 **11.82.26-Tabelas de cálculo**  
 Evolução no processo de inclusão de valores na tabela de calculo.   
    
 **11.82.25-Funcionários.Net** (TGBVMK)  
 A partir desta versão os campos Número de dependentes Salário Família e Número  dependentes de   
 IRRF serão visualizados apenas para consulta, ficando desabilitados.  
    
 **11.82.25- Caged.Net**  
 Evolução no relatório Caged quando for utilizado filtro.  
    
 **11.82.20 – Integração TOTVS x SAP**   
 Implementado módulo por meio da qual será possível realizar a integração com o sistema SAP, sendo controlada a integração contábil da folha de pagamento e possíveis estornos de documentos já integrados.   
    
 **11.81.15 – Envelope**   
 Implementado o campo Editado no Envelope de Pagamento por Centro de Custo.   
    
 **11.80.0 - Módulos Migrados para a plataforma .NET**   
    
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades.  
 Os módulos migrados ou novos nesta versão são:

* GRRF - Geração de Recolhimento Rescisório do FGTS
* Geração de Encargos
* Importação de Dados Folha de Pagamento
* RAIS - Relação Anual de Informações Sociais

**11.80.0 – Funcionários**   
 Atualizado o registro no cadastro de funcionários quando utilizado o cálculo da rescisão na edição do funcionário.  
    
 **11.80.0 – Rescisão**

* Atualizado o cálculo da referência do 13º salário na rescisão.
* Otimizado a visualização dos itens disponíveis para o Nível Salarial e Faixa Salarial. Para apresentar  somente os níveis e faixas salariais cadastrados na coligada de destino da transferência do funcionário.
* Implementado mensagens caso o usuário preencha um dos dois campos, Nível Salarial ou Faixa Salarial, o sistema irá barrar o processamento informando que se um dos campos foi preenchido o outro obrigatoriamente deverá ser preenchido.

**11.80.0 – Bloqueia Recálculo**  
 Atualizado o Bloqueio do Recálculo quando utilizada a forma de bloqueio parcial.  
    
 **11.80.0 - Contabilização**  
 Implementado parâmetro "Incluir Histórico Padrão no complemento" para no momento da gravação do Complemento do Histórico seja considerado também o Histórico Padrão antes do complemento.  
    
 **11.80.0 - RM Portal** Incluído o campo "6 - RENDIMENTOS RECEBIDOS ACUMULADAMENTE-ART 12-A DA LEI N 7.713, de 1988 (SUJEITOS A TRIBUTACAO EXCLUSIVA)".  
    
 **11.80.0 - Consulta Movimento Integração** Otimizada a visão para consulta dos eventos de integração.  
    
 **11.80.0 - Relatórios**

* Otimizado o valor de preenchimento do campo 23 da TRCT Portaria 1621/2010 que passou a trazer somente os proventos relacionados a salário.
* O sistema passou a levar para o campo 22 'Tipo de Demissão' o código 'SJ1' para demissões do tipo '4 - Iniciativa do empregado sem justa causa'.

**11.80.0 - Folha Mensal**   
 Otimizado  o  acesso ao Menu "Folha Mensal|Consulta Movimentação da Integração" o registro não é editado ao dar um duplo clique sobre o mesmo.  
    
 **11.80.0 - Lançamento Financeiro.net**   
 Otimizado a geração do Lançamento Financeiro .net para considerar fórmula informada no complemento de histórico.  
 **11.52.57- Rescisão**  
 ·          Atualizado o status da requisição de desligamento quando a rescisão for cancelada .  
 ·          Evolução  no cálculo do CC 329 para considerar o período aquisitivo proporcional no cálculo da média de comissão.  
    
 **11.52.57-Fórmula.Net**  
 Atualizado as funções de fórmulas NDFERMES, NDFERPROX e NDFERIAS.  
    
 **11.52.57-Sefip.Net**  
 Atualizado o relatório sefip quando for gerado competência anterior a atual (Sefip retroativo).  
    
 **11.52.57- Termo de Rescisão de contrato de trabalho**  
 ·          Atualizado campos no TRCT   
 ·          Evolução no TRCT com inclusão de parâmetro para (não somar as médias na diferença de férias vencidas (Campo 66).  
    
 **11.52.55-Tabelas de Cálculos**   
 Implementada a finalidade 4-IRRFPL, em Cadastros| Tabelas de cálculos, visando atender a medida provisória nº597, de 26 de dezembro de 2012 .Foi criado o parâmetro "Deduz valor por dependentes na base de IRRF PL " em opções |Parâmetros|Rmlabore|Parâmetros de cálculo|Parâmetros II, caso queira considerar o valor por dependentes.   
    
 **11.52.55-13º Salário**  
 Otimizado o  cálculo da pensão sobre 13o, para abater valor já descontado na 1ª Parcela ao salvar movimento de pensão.  
    
 **11.52.55-Ferias**  
 Otimizado a apuração da base de INSS férias, no cálculo da diferença por dissídio.  
    
 **11.52.55-Afastamento**   
 Otimizado o parâmetro "Usa mês comercial para afastamentos no final do Mês" para considerar a data posterior ao término do período de atestado médico, ao invés da data de início do afastamento.  
    
 **11.52.55-Período Aquisitivo**  
 Otimizado o módulo "Acerto Período Aquisitivo" para não finalizar período perdido que já tenha período de gozo de férias em andamento.  
    
 **11.52.55-Férias Coletivas**  
 Otimizado o parâmetro "Verifica faltas funcionário > 1 ano" do Cadastro de Férias Coletivas.  
    
 **11.52.55-Geração do Histórico de Provisões**  
 A partir desta versão, será possível realizar o fracionamento do processo, bastando confirmar o parâmetro "Habilitar Fracionamento de Jobs " em opções|Parâmetros|RmLabore|Outros Parâmetros|Parâmetros III .  
 **11.52.55-Caged**  
 Otimizado o relatório do  Caged quando for utilizado filtro.  
    
 **11.52.55-Manad**  
 Otimizada a geração do relatório Manad.  
    
 **11.52.55-Portal**  
 Otimizado portal ao incluir movimento através entrada de dados.  
 Otimizado portal ao consultar um subordinado.                                   
    
 **11.52.55-Funcionários.Net**  
 Otimizado a alteração da faixa salarial no cadastro do funcionário.   
 A partir desta versão, será possível alterar as datas do período aquisitivo.Para ter acesso essa nova funcionalidade deverá ir na aba  processos do cadastro de periodo aquisitivo.Apenas  os usuarios que tem permissão para editar esse cadastro tem acesso ao novo módulo.  
    
 **11.51.45 - Ferias**   
 Implementado em Movimento/Ferias/Lançamento o campo "Lança Movimento Proximo Mês".  
 Confirmando este campo o sistema habilita o campo "Periodo" permitindo a seleção do periodo  que as ferias serão lançadas.   
    
 **11.51.35-  Manad**   
 Otimizada  a geração do Manad, a partir desta versão o arquivo do Manad será gerado compactado,será  utilizando a extensão ZIP.  
    
 **11.51.35- TRCT**  
 Otimizado o relatório TRCT quando existir eventos tipo referência.  
    
 **11.50.30-Funcionários.Net**  
 Implementado a coluna "Quantidade de dias" no histórico de afastamento.  
    
 **11.50.30- Cadastro |Chefe supervisor**  
 Atualizado o processo de expansão no cadastro de chefes e supervisores.  
    
 **11.50.30- Portal**  
 Atualizado o processo de alteração de endereço no portal.  
    
 **11.50.25- Restauração Ficha Financeira complementar**  
 Otimizado o processo de restauração da ficha financeira complementar.  
    
 **11.50.25- Cadastro de Funcionarios.Net**  
 Otimizado o cadastro de funcionários.net.  
    
 **11.50.25- Termo de Rescisão de contrato de trabalho**  
 Otimizado o campo 50  do relatório TRCT, quando na movimentação existir número de faltas igual ao dias trabalhados.  
    
 **11.50.25 - MANAD**  
 Atualizada a geração do arquivo MANAD para desconsiderar a data de pagamento dos eventos e considerar a data de competência na geração dos registros do arquivo a partir do registro tipo K300.  
    
 **11.50.25-Linhas de Transporte**   
 Otimizado o processo de trocar código da linha de transporte  .  
    
 **11.50.25- Alterações globais de funcionários**  
 Otimizado o processo de atualização do saldo de FGTS , quando não existir movimentação saldo do funcionário mês anterior.                                                              
    
 **11.50.25- Sefip.Net**   
 Otimizada a geração sefip.net , quando for confirmada a opção "Gerar lançamento financeiro".   
    
 **11.50.25- Recálculo-Bloqueia.Net**  
 Otimizada a Rotina de bloqueio parcial.  
    
 **11.50.25-Contabilização.Net**  
 Otimizado o Log de execução ao efetuar  a rotina de contabilização.   
    
 **11.50.25- Formula.Net**  
 Atualizada a variável CritAdm validando ajuste vazamento memória .  
    
 ***11.50.25- Envelope de pagamento***  
 Otimizado o processo via entrada de dados do envelope de pagamento.   
    
 **11.50.10-Termo de rescisão de contrato de trabalho**  
 Atualizada as informações a serem impressas no campo 03-(Endereço) no relatório termo de rescisão conforme o código de quebra informado.Ao informar o código de quebra de CNPJ , o sistema irá buscar o Endereço da seção Centralizadora,caso contrário, irá buscar o endereço da seção do funcionário.  
 Exemplo:  
 01-Seção centralizadora CNPJ  
 Quebra ?? -Endereço Av.Raja Gabaglia,2664-Santa Lucia-Bh-MG.  
 01.01-Seção Funcionário  
 Quebra- ????? - Endereço- Av.Raja Gabaglia,2222-Santa Lucia-Bh-MG.  
 Se for informado ?? será visualizado no campo 03 o endereço(Av.Raja Gabaglia,2664-Santa Lucia-Bh-MG), caso contrário, buscará o endereço da seção do funcionário.  
 O sistema passou a considerar as informações do vinculo da Rais na emissão do campo 21 -Tipo de Contrato.  
    
 **11.50.10-Funções de Fórmulas**  
 Otimizada a variável NJTRAB .  
    
 **11.50.10-Cadastro de Funcionarios.Net**

* Atualizado o campo CEP ao incluir um funcionário.Net.
* Atualizada a inclusão de exames no cadastro do funcionário.

**11.50.10-RM Portal**

* Atualizada a inserção de eventos na movimentação através da Entrada de dados.
* Incluído no informe de rendimentos o campo 6 - RENDIMENTOS RECEBIDOS ACUMULADAMENTE-ART 12-A DA LEI N 7.713, DE 1988 (SUJEITOS A TRIBUTACAO EXCLUSIVA) EM REAIS

**11.50.5 - Guia de INSS**  
 Implementado no sistema a forma de atender à [LEI Nº 12.546, DE 14 DE DEZEMBRO DE 2011](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/lei%2012.546-2011?OpenDocument), referente ao recolhimento de INSS (parte empresa) para determinados segmentos.  
 Para atender a esta lei será utilizado o parâmetro "Faturamento Bruto" da pasta "Dados p/ INSS" do cadastro de seção.  
    
 Caso este campo esteja preenchido com valor da receita bruta e a competência do sistema seja a partir de 12/2011, o valor do campo Empresa será zerado na guia de INSS, pois o valor deste campo será recolhido via DARF.  
    
 Esta regra valerá para quaisquer segmentos que estejam com este valor preenchido no cadastro de seções a partir de 12/2011, exceto produtor rural. Portanto, este campo deverá ser preenchido somente se a empresa se encaixar nos parâmetros desta Lei.  
    
 Veja também [{+}](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm)<http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm+>   
    
 **Observação:** Consulte o Novo Ato Declaratório 93 GFIP Lei 12.546\_2011 sobre a aplicação da lei 12.546, com relação a GFIP.  
    
 **11.50.5- Cadastro de seções**  
 Atualizada a inclusão de seções quando a mascara de cep estiver em branco.  
    
 **11.50.5 - Portal**  
 Atualizada a inclusão,alteração e exclusão no processo de "Entrada de movimento" através do portal.   
    
 **11.50.5 – Reprogramação Salarial**  
 Atualizada a reprogramação salarial quando o parâmetro do RM Labore "Reprogramação detalhada por centro de custo" estiver Desmarcado.  
    
 **11.50.5 – Sefip.net**  
 Atualizada a geração do sefip quando estiver marcado o parâmetro "Gerar lançamentos financeiros" e na parametrização   
 utilizar fórmula para complemento de histórico.  
    
 **11.50.5-Lançamento financeiro.Net**  
 Atualizada a rotina de lançamento financeiro permitindo a geração do liquido de rescisão utilizando fórmula.  
    
 **11.50.5 – Parâmetros RMLabore**  
 Implementado o parâmetro "Gera contabilização no Labore antes de enviar para o Saldus" em opções|Parametros| RM Labore|Outros Parâmetros|Parâmetros II . Confirmando este parâmetro ao gerar o lote contábil os lançamentos serão visualizados no menu Cadatros|Contabilização|Lançamentos contábeis (RM Labore), caso contrário ,serão visualizados em Cadatros|Contabilização|Lançamentos contábeis (RM Saldus).  
    
 **11.50.1 - Substituição de chefes e supervisores**  
 Implementado o módulo Rotinas| Substituição de Chefes e supervisores.  
 Este processo permite definir um substituto para um atual chefe|Supervisor informando sua data final de chefia juntamente com data inicio e fim da chefia do substituto.  
    
 **11.50.0 - Módulos Migrados para a plataforma .NET**   
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados ou novos nesta versão são:

* Agrupamento de Contas Contábeis (RM Labore)
* Agrupamento de Contas Gerenciais (RM Labore)
* Cadastro de Chefes e Supervisores
* Centros de Custos (RM Labore)
* Encargos Contábeis
* Tipos de Documento

**11.50.0 - Geração do Termo de Rescisão Portaria 1.621/2010**  
 Implementado o módulo Relatório | TRCT Portaria 1621/2010.  
 Confira o help deste módulo e veja as orientações para gerar o TRCT através desta nova funcionalidade.  
    
 **11.50.0 - Parâmetros do Sistema | Gestão Educacional**  
 A partir desta versão, o sistema passa a contar com dois novos parâmetros da Gestão Educacional, que podem ser considerados na Reprogramação Salarial ou no Cálculo do Movimento de Ensino: "Fator para cálculo da Atividade Extra" e "Fator para cálculo da Atividade Complementar".  
 Estes novos parâmetros visam permitir maior flexibilidade no cálculo das atividades Extras e Complementares, uma vez que o fator semanal poderá ser definido pelo tipo da atividade.  
    
 **11.50.0- Sefip.NET**

* Atualizada a geração do SEFIP.NET quando for confirmada a opção "Importar Autônomos do Rm Fluxus / Rm Nucleus".
* Atualizado Sefip.Net quando funcionário não possuir informações de Categoria ou ocorrência.
* Criado o parametro "Gerar arquivo consolidado para Dissídio Coletivo\Reclamatória Trabalhista".Maiores informações consulte o Help.
* Atualizada a geração do sefip.O sistema passou a não permitir o preenchimento dos dados da aba Lançamentos Financeiros, quando o flag Usar Parâmetros Específicos da Coligada está desmarcado. Ao marcá-lo é possível preencher tanto os dados do lançamento financeiro como os demais específicos.
* Alterada a localização do parâmetro "Considerar valor de aviso prévio no SEFIP" ,a partir desta versão, será encontrado em OPÇÕES | PARÂMETROS | RMLABORE | PARÂMETROS DE RESCISÃO."

**11.50.0- Cadastro de Perfis** Atualizado o filtro de perfil ao utilizar a tabela PGRPLANC  
    
 **11.50.0- Importação movimento.NET** Atualizado a importação do movimento.NET quando for confirmado o parâmetro "Data de pagamento".  
 **11.50.0- Tabelas de cálculo** Incluida a coluna "Final Vigência" na visualização da tabela de cálculo.  
 **11.50.0- Manad** Criado o parâmetro para separar tipo de base quando existir diferença por dissidio " Considerar os CC37,66,96 e 97.Marcando o parâmetro as informações geradas no registro K300 quando for diferença por dissídio serão considerados como indicador 1-Base de calculo do salário de contribuição mensal,caso contrário, serão considerado como indicador 8-Não é base de cálculo.  
    
 **11.50.0-Reprogramação Salarial**

* Atualizado o processo de reprogramação salarial quando for realizada a distribuição por centro de custo.
* A partir desta versão, será possível visualizar o Log do movimento de ensino .

**11.50.0- Guia de INSS** Atualizada a geração da guia de INSS quando for confirmado o parâmetro "Armazena geração da guia de inss por chapa" nos parâmetros RMLabore aba parametros III.  
    
 **11.50.0- Entrada de dados por centro de custo** Atualizada a Entrada de dados por centro de custo quando confirmado o campo "Codigo do Centro de Custo a fixar" de forma a visualizar apenas os códigos da coligada atual.  
    
 **11.50.0 - Cadastro de Funcionários**  
 Criação do Histórico de transferência que ficará disponível no cadastro de funcionários onde será possível visualizar todo o histórico de transferência da chapa. O mesmo ficará disponível nos anexos do funcionario .Net e na aba Histórico de situação no funcionário delphi.  
    
 **NOVIDADES DO CÁLCULO.NET (MÁQUINA DE CÁLCULO)**  
    
 **11.50.0 - Módulos Migrados para a plataforma .NET**  
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados ou novos nesta versão são:

* Bloqueio de recálculo
* CAGED
* Sindicatos

**11.50.0 - Eventos**  
 Implementado os códigos de cálculos:  
 319 – PENSÃO ALIMENTÍCIA FÉRIAS NA RESCISÃO  
 320 – PENSÃO ALIMENTÍCIA FÉRIAS INFORMADA  
 321 – PENSÃO ALIMENTÍCIA PL INFORMADA  
 322 – SEGUNDA PARCELA 13º SALÁRIO LICENÇA MATERNIDADE  
 323 – DIFERENÇA DE 13º SALÁRIO LICENÇA MATERNIDADE  
 324 – 13º SALÁRIO RESCISÃO LICENÇA MATERNIDADE  
 325 – DIFERENÇA 13º SALÁRIO RESCISÃO LICENÇA MATERNIDADE  
 326 – DIFERENÇA DE PENSÃO ALIMENTÍCIA FÉRIAS NA RESCISÃO   
 327 – ESTORNO DE PENSÃO DE FÉRIAS NA RESCISÃO  
    
 **11.50.0 - Funcionários .Net**

* Implementado no anexo Dependentes | Movimentação da Pensão de Dependentes o campo "Data Pagto. Férias".
* Implementado os campos "Nro. Dependentes IRRF", "Nro. Dependentes Salário Família" e "Líquido" na aba "Bases" da Ficha Financeira e Ficha Financeira Complementar. Estes campos são apenas informativos, para facilitar a emissão de relatórios, consultas SQL e a visualização da quantidade de dependentes utilizada nos cálculos.

**11.50.0 - Sindicato .Net**  
 Implementada a aba "Comissão", passando a ser possível utilizar parâmetros específicos para o cálculo da média de comissão.  
 Esta aba somente é visível quando o parâmetro "Utiliza parâmetros específicos para média de comissão" está marcado.  
    
 **11.50.0 - Cancelamento de Movimento**  
 Implementado o parâmetro "Cancela movimento de demitidos no mês".  
    
 **11.50.0 - Grupos de Eventos**  
 Disponibilizado o recurso para controle de verbas com insuficiência de saldo.  
    
 **11.50.0 - Assistente de Grupos de Eventos**  
 Implementado o recurso para "Lançar Férias", "Finalizar Férias", "Lançar Líquido de Rescisão" e "Lançar Líquido de Rescisão Complementar".  
    
 **11.50.0 - 13º Salário**  
 Atualizado o recálculo da 2ª parcela do 13º salário quando existe evento de média.  
    
 **11.50.0 - Contribuição Sindical**  
 Implementado o cálculo da Contribuição Sindical para Trabalhador Rural, a base do cálculo será o Mínimo Garantido pelo Sindicato, ao invés do Salário Base.  
    
 **11.50.0 - Rescisão**  
 Atualizado o cálculo da rescisão próximo mês quando existem férias iniciando no mês e com término no próximo mês.  
    
 **11.50.0 - Lançamento do Líquido Rescisão**  
 Retirado os campos para preenchimento dos eventos de líquido de rescisão, passando a serem preenchidos nos parâmetros do RM Labore | Parâm. Rescisão.  
    
 **11.50.0 - Finaliza Férias**  
 Implementada a possibilidade de finalizar férias próximo mês.   
 Implementada a situação de férias "X-Finalizadas para o próximo mês'. Esta situação será preenchida automaticamente pelo sistema na finalização das férias para o próximo mês e na liberação de competência será atualizada para "F-Finalizadas".  
    
 **11.50.0 - Parametros | RM Labore**  
 Implementado o parâmetro "Considera faltas para cálculo de 13º." nos parâmetros da rescisão.  
 Implementado nos parâmetros da rescisão, campos para preenchimento dos eventos de líquido de rescisão e rescisão complementar.
