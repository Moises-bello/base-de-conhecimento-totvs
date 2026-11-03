---
content_hash: b7d217a9cbae7b04ee848b3ab6f9651d7f0f0017458d59c6967092d651c236c6
fetched_at: '2026-06-29T00:10:04.924189+00:00'
page_id: '452719266'
product: rm
source: tdn-rm
title: Novidades da Versão Anterior 11.20 - FOP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719266
version: 3
---

**11.20.45 - Termo de Rescisão de contrato de trabalho**

* Atualizada a geração do termo de rescisão quando for utilizado filtro na geração do relatório.
* Atualizada as informações a serem impressas no campo 03-(Endereço) no relatório termo de rescisão conforme o código de quebra informado.Ao informar o código de  quebra de  CNPJ ,  o sistema irá buscar o Endereço da seção Centralizadora,caso contrário, irá buscar o endereço da seção do funcionário.

Exemplo:  
 01-Seção centralizadora    - Quebra ??            Endereço Av.Raja Gabaglia,2664-Santa Lucia-Bh-MG.  
 01.01-Seção Funcionário    Quebra ?????     Endereço- Av.Raja Gabaglia,2222-Santa Lucia-Bh-MG.  
 Se for informado ?? será visualizado no campo  03 o endereço(Av.Raja Gabaglia,2664-Santa Lucia-Bh-MG), caso contrário, buscará o endereço da seção do funcionário.  
 11.20.45 - Critica da Folha.Net  
 Atualizada a geração do relatório critica da folha.Net.  
    
 11.20.45 - RM Portal  
 Atualizado o processo de sugestão de férias do colaborador validando o número de dias de direito.  
    
 NOVIDADES DA MÁQUINA DE CÁLCULO  
    
 11.20.45 -  Funções de Fórmula

|  |
| --- |
| Atualizada a variável de fórmula MH. |

**11.20.41 - Guia de INSS**  
 Implementado no sistema a forma de atender à [LEI Nº 12.546, DE 14 DE DEZEMBRO DE 2011](http://legislacao.planalto.gov.br/legisla/legislacao.nsf/Viw_Identificacao/lei%2012.546-2011?OpenDocument), referente ao recolhimento de INSS (parte empresa) para determinados segmentos.  
 Para atender a esta lei será utilizado o parâmetro "Faturamento Bruto" da pasta "Dados p/ INSS" do cadastro de seção.  
    
 Caso este campo esteja preenchido com valor da receita bruta e a competência do sistema seja a partir de 12/2011, o valor do campo Empresa será zerado na guia de INSS, pois o valor deste campo será recolhido via DARF.  
    
 Esta regra valerá para quaisquer segmentos que estejam com este valor preenchido no cadastro de seções a partir de 12/2011, exceto produtor rural. Portanto, este campo deverá ser preenchido somente se a empresa se encaixar nos parâmetros desta Lei.  
    
 Veja também [{+}](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm)<http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2011/Lei/L12546.htm+>   
    
 **Observação:** Consulte o Novo Ato Declaratório 93 GFIP Lei 12.546\_2011 sobre a aplicação da lei 12.546, com relação a GFIP.  
    
 **11.20.40- Sefip.NET**

* Atualizada a geração do SEFIP.NET quando for confirmada a opção "Importar Autônomos do Rm Fluxus / Rm Nucleus".
* Atualizado Sefip.Net quando funcionário não possuir informações de Categoria ou ocorrência.
* Criado o parametro "Gerar arquivo consolidado para Dissídio Coletivo\Reclamatória Trabalhista".Maiores informações consulte o Help.
* Atualizada a geração do sefip.O sistema passou a não permitir o preenchimento dos dados da aba Lançamentos Financeiros, quando o flag Usar Parâmetros Específicos da Coligada está desmarcado. Ao marcá-lo é possível preencher tanto os dados do lançamento financeiro como os demais específicos.
* Alterada a localização do parâmetro "Considerar valor de aviso prévio no SEFIP" ,a partir desta versão, será encontrado em OPÇÕES | PARÂMETROS | RMLABORE | PARÂMETROS DE RESCISÃO."

**11.20.30- Sefip.Net**

* Atualização do sefip.Net quando usuário possuir mais de um perfil associado e utilizando filtro de perfis.
* Criado o parametro "Gerar Funcionários Administrativos" ,quando o Tomador de serviço for o mesmo apresentado no cadastro do funcionário e nos parâmetros do sistema. Após confirmado o novo parâmetro deverá ser informado o código GPS 2100.

**11.20.30-Portal** Atualizada a visualização do informe de rendimentos e envelope de pagamento através do portal.  
    
 **11.20.20 - Contabilização.NET**  
 Ajuste na rotina de contabilização, através do módulo Contabilização .Net.  
    
 **11.20.20 - Homolognet**  
 Otimizada a geração do arquivo homolognet para funcionários alocado em uma seção com o campo CEI não preenchido e com o parâmetro 'Utiliza CEI'.  
 **11.20.20 - SEFIP.NET**

* Otimizada a geração do arquivo SEFIP.RE para retificação de valores no sefip.
* Otimizada a geração do arquivo SEFIP.RE para empresa que utilizam centralização do recolhimento.

**11.20.20 – RM PORTAL**  
 Otimizada a geração do Informe de Rendimentos, através do RM PORTAL para anos anteriores a 2010.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.20 - Cadastro de Funcionários.NET**

* Otimizado o processo de envio de E-Mail, através do cadastro de funcionários .Net.
* Otimizado o processo de exclusão de funcionários com admissão para o próximo mês.
* Otimizada a funcionalidade de definir como obrigatórios os campos 'Agência' e 'Conta  Corrente' , através do cadastro de funcionários .Net.

**11.20.15 – SEFIP.NET**

* Acertada a geração do arquivo SEFIP.RE para não levar R$0,01 para o campo "BASE DE CÁLCULO 13º SALÁRIO PREVIDÊNCIA SOCIAL" para funcionários demitidos por transferência.
* Otimizada a geração do arquivo SEFIP.RE para uma coligada identificada por CPF.
* Otimizada a geração do arquivo SEFIP.RE, através do módulo SEFIP .NET para levar o valor do evento de CC55 - SALÁRIO FAMÍLIA RETROATIVO.
* Otimizada a geração do arquivo SEFIP.RE, para desconsiderar as filiais cadastradas com 0.

**11.20.15 - MANAD**  
 Ajustada a geração do arquivo MANAD para considerar eventos de férias partidas.  
    
 **11.20.15 - HOMOLOGNET**  
 Ajustada a geração dos arquivos com valores de rubricas e rubricas externas do homolognet para correta transmissão ao ministério do trabalho.  
    
 **11.20.15 – RM PORTAL**  
 Otimizada a inclusão via portal de um substituto para um funcionário que seja chefe em seções presentes em coligadas diferentes mas que tenham o mesmo código de seção.  
    
 **11.20.15 – Cadastro de Seções**  
 Otimizado o processo de "Trocar Código de Seção" na tela de visão do cadastro de seções.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.15 - Diferença de Pensão Alimentícia**  
 Atualizado o cálculo da Diferença de Pensão Alimentícia, quando o valor da pensão for apurado através da variável de fórmula SM (Salário Mínimo).  
    
 **10.20.15 – Lançamento de eventos**  
 Atualizado o lançamento de eventos (proventos e descontos) para o próximo mês, quando o funcionário esta com situação 'Z-Admissão próx. mês'.  
    
    
 **11.20.10 - Férias**  
 Atualizado o cálculo de férias, quando nos 'Eventos Adicionais de Férias' existe evento que utiliza a variável de fórmula CALMED e o funcionário recebe abono pecuniário.  
    
 **11.20.10 - Rescisão Complementar**  
 Atualizado a rescisão complementar quando calculada em competência posterior a demissão e o período atual é menor do período da rescisão.  
    
 **11.20.10 - HomologNet**

* Ajustada a geração dos arquivos XML com a formatação do CNPJ e CEI com 14 casas decimais e zeros a esquerda.
* Ajustada a geração dos arquivos XML para levar os eventos de pensão alimentícia pagos na rescisão contratual.

**11.20.10 - SEFIP .NET**

* Otimizada a geração do arquivo SEFIP.RE ao selecionar a opção 'Importar autônomos de outro Sistema'.
* Otimizada a geração dos lançamentos financeiros, utilizando a opção de 'Gerar um único arquivo consolidado'.

**11.20.10 - TOTVS PORTAL**  
 Otimizada a geração do Envelope de Pagamentos, utilizando o Gerador de Relatórios.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.10 - Cadastro de Fórmula**  
 Atualizado o Cadastro de Fórmulas do RM Labore para a plataforma .Net.  
    
 **11.20.10 - Funções de Fórmula**

* Atualizada a variável de fórmula CALCMED.
* Atualizada a variável de fórmula CALCMEDDATA.

**11.20.10 – Entrada de Dados**

* Atualizada as telas de Entrada de Dados quanto ao funcionamento do parâmetro "Ler Próximo Registro" e a verificação de alteração manual na movimentação do funcionário.
* Atualizada a Distribuição de Valores quando existe movimento lançado pela Entrada de Dados Tomador.
* Atualizada Entrada de Dados e Entrada de Dados por Tomador passando a considerar "Caminho padrão para gravação \ importação de arquivos.txt" dos parâmetros do sistema.
* Atualizadas as telas de Entrada de Dados nos campos Código de Evento e Código de Centro de Custo.
* Atualizado o cálculo das Férias Proporcionais quando o evento de faltas (Código de Cálculo 8) é calculado através de Fórmula.
* Retirada as opções de Maximizar e Minimizar a tela, disponibilizando apenas o botão Fechar no canto superior direito da tela.

**11.20.10 – Pensão Alimentícia**  
 Atualizado o cálculo da Pensão Alimentícia nas Férias quando os Código de Cálculo "141-INSS Férias no Mês (INFORMADO)" e "142-INSS Férias Próximo Mês (INFORMADO)" constam na movimentação de férias.  
    
 **11.20.10 – Férias**  
 Foi atualizado o cálculo de férias quando há Antecipação das Férias.  
    
 **11.20.10 - Contabilização .Net**  
 Otimizada a geração da contabilização, através do módulo .net .  
    
    
 **11.20.5 – Tabelas de Cálculo**  
 Atualização na tabela de cálculo quando for realizada a "Cópia de múltiplos registros".  
    
 **11.20.5 – 13 º Salário**  
 Atualizado o recálculo da 2ª parcela do 13º salário quando existe evento de média.  
    
 **11.20.5 - Manad**  
 Atualização no relatório do manad no registro k250.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.5 – Cadastro de Eventos**  
 Implementado no Cadastro de Eventos o anexo Lançamentos Vinculados.  
    
 **11.20.5 – Vale transporte**  
 Atualizado o lançamento de Vale Transporte na Rescisão.  
    
 **11.20.5 - Geração do Histórico de Provisões**  
 Atualizada a rotina de geração do Histórico de Provisões.Net.  
    
 **11.20.5 – Rescisão**  
 Otimizado o cálculo da Rescisão caso o Parâmetro de RH "Utiliza CEI" esteja marcado.  
    
 **11.20.5 – Rescisão Complementar**  
 Atualizado o cálculo da Rescisão Complementar.    
 **ATENÇÃO!**  
    
 **11.20.1 -** Esta versão esta preparada para atender o artigo 10 da **Instrução Normativa RFB nº 1.033, de 14 de maio de 2010**, que diz:  
    
 ***"Artigo 10,*** *§ 3º:  No caso dos rendimentos de que trata o inciso II do § 1º, se o empregado for beneficiário de plano privado de assistência à saúde, na modalidade coletivo empresarial, contratado pela fonte pagadora, deverão ser informados os totais anuais descontados em folha de pagamento, correspondente à participação do empregado, discriminando as parcelas correspondentes ao beneficiário titular e as de cada dependente."*  
    
 Para maiores informações, consulte o help dos módulos:  
 Cadastros | Funcionários | Registro | Histórico de Assistência à Saúde  
 Cadastros | Fórmulas | Função de Fórmula - SALVAVALDEP  
 Utilitários | Importação de Dados do RM Labore | Funcionários | Históricos  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.1 - Módulos Migrados para a plataforma .NET**  
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados ou novos nesta versão são:

* Geração de Lançamentos Financeiros (.Net)

**11.20.1 – Funcionário.Net**

* Atualizado a 'Base de FGTS Folha' e 'Base de INSS Folha' na aba incidência do envelope de pagamento, quando no funcionário está marcado 'FGTS - Não optante', ou 'INSS - Não Calcula' ou quando o funcionário está afastado o mês todo por acidente de trabalho.
* Implementado o parâmetro 'Calcula IRRF/INSS de múltiplos vínculos sem chapa centralizadora' em Opções | Parâmetros | RM Labore | Parâm. Cálculo | Parâmetros II, para funcionários que utilizam o cálculo de IRRF e INSS com múltiplos vínculos.
* Implementado o anexo 'Histórico Assistência à Saúde', para atender a Instrução Normativa RFB nº 1.033, de 14 de Maio de 2010 da DIRF.

**11.20.1 – Rescisão**  
 Para os clientes que utilizam 'Importação do movimento de ensino de sistema acadêmico de terceiros' e no evento esta parametrizado para 'Segue Rateio Movimento Ensino Importado', e não existe movimento de ensino com data de vigência no mês da rescisão ou rescisão complementar, o sistema passou a verificar o centro de custo do movimento de ensino com a vigência anterior no rateio dos eventos da rescisão.  
    
 **11.20.1 – Formulas**  
 Implementado nas variáveis HORASTRAB e DIASTRAB um parâmetro onde o usuário definirá se deseja considerar o intervalo de refeição.  
 **11.20.1 – Lançamento da movimentação para o próximo mês**  
 Este processo tem o objetivo de facilitar a usabilidade do sistema para o cliente que utiliza a máquina de cálculo e necessita processar algum movimento para o próximo mês e por algum motivo não pode liberar a competência.  
    
 Para atender esta implementação foi necessário adequar o cálculo e a interface dos módulos:  
 Movimento | Folha de Pagamento | Lançamentos Automáticos | Grupo de Eventos (.Net) Assistente   
 Implementado o parâmetro 'Lança movimento próximo mês'.  
 Movimento | Folha de Pagamento | Cancelamento de Movimento  
 Implementado o parâmetro 'Cancela movimento próximo mês'.  
 Movimento | Folha de Pagamento | Recálculo | Executa  
 Implementado o parâmetro 'Recalcula movimento próximo mês'.  
 Movimento | Folha de Pagamento | Recálculo | Bloqueia  
 O sistema passou a apresentar os períodos que tem movimentação no próximo mês.  
 Movimento | Rescisão | Rescisão Coletiva e Cadastros | Funcionários | Anexo Rescisão  
 O sistema passou a apresentar uma mensagem impossibilitando salvar/calcular uma rescisão, quando houver movimentação em meses posteriores ao mês de demissão.  
    
 **11.20.1 – Férias Coletivas / Globais**  
 Implementado o parâmetro 'Verifica faltas funcionário >1 ano', possibilitando o cadastramento das férias coletivas ou globais considerando as faltas do funcionário.  
    
 **11.20.1 – Parâmetros RM Labore**  
 Implementado o parâmetro 'Consid. avo em mês de 30 dias p/ admitidos dia 17 na prov. férias' em Opções | Parâmetros | RM Labore | Outros Parâmetros | Parâmetros II que será verificado na geração do Histórico de provisão.  
    
 **11.20.0 - Módulos Migrados para a plataforma .NET**  
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados ou novos nesta versão são:

* Atualização de Saldo de FGTS .Net
* Crítica da Folha
* Comparativo SEFIP X Folha Analítica
* Validação de Liberação de Competência

**11.20.0 - Cadastro de Funcionários**

* A partir desta versão, ao incluir um funcionário, será realizada a consistência do número de funcionários de acordo com a definição da licença Light On-Demand.
* O campo "Cartório" do cadastro de dependentes teve a descrição alterada para  "Novo Registro / Cartório".
* Atualizada a visualização do envelope de pagamento quando existem mais de 32 itens cadastrados na tabela dinâmica 'INT34 - Nome de Acumulador', a partir de agora será permitido cadastrar até 40 itens de acumuladores.
* Otimizado o preenchimento dos campos 'Base de FGTS' e 'Base FGTS13' da tabela PFPERFF, quando no cadastro do funcionário no campo 'Situação FGTS' for informado '2 – Não Optante'.
* Atualização do cálculo da pensão Alimentícia, quando o funcionário possuir na movimentação eventos com incidência de pensão folha.
* Otimizada a visão das 'Linhas de Transportes', quando existir mais de uma coligada com o mesmo código de linha de transporte.
* Atualização na inclusão do funcionário, serão listadas apenas as seções ativas.
* A partir desta versão, e-mails iniciados com números passaram a ser permitidos no campo 'e-Mail' da aba Identificação.
* Atualização na exclusão de funcionário que possui integração com RMVitae.
* Otimizado o processo 'Troca a chapa do funcionário', passando a contemplar atualizações das tabelas criadas na versão 11.20.
* Otimização do cálculo do número de Dias Trabalhados para funcionário que retorna do afastamento dentro do mês e, em seguida, é transferido entre seções de CNPJ's diferentes.

**11.20.0 – Cadastro de Eventos**

* Otimizada a visualização dos acumuladores quando existem mais de 32 itens cadastrados na tabela dinâmica 'INT34 - Nome de Acumulador'. O sistema passou a permitir cadastrar até 40 itens de acumuladores.
* Realizados procedimentos de melhoria na tela de inclusão de eventos relacionados.

**11.20.0 – Cadastro de Seções**  
 Implementado o campo 'Código Pagamento GPS Terceiros', onde o usuário poderá informar o código específico de pagamento da GPS caso existam valores apenas de Terceiros.  
    
 **11.20.0 – Cadastro de Sindicato**

* Alterado a nomenclatura do parâmetro sindical 'Considera maiores valores para soma' para 'Considera maiores valores por grupo de média'.
* A partir desta versão, o sistema possibilitará o cálculo das médias considerando o mês de admissão, quando for processado o calculo da média de licença maternidade.

**11.20.0 – Valores Fixos**  
 A partir desta versão, a alíquota do 'FAP - Fator Acidentário de Prevenção' deixará de ser cadastrada nos Parâmetros do RM Labore e passará a ser cadastrada em Valores Fixos, bastando informar a finalidade Alíquota FAP.  
 Com esta melhoria, será possível manter históricos junto a alíquotas FAP, permitindo com isso a  emissão de relatórios.  
    
 **11.20.0 – Tabelas de cálculo**  
 Otimizado o processo de configuração de perfil para utilização do gerenciamento de filtros.  
    
 **11.20.0 – Contabilização**

* Implementado o período '4-Mês Anterior' para cálculo do rateio por centro de custo, possibilitando ao usuário contabilizar encargos utilizando o rateio por centro de custo da competência anterior.
* Otimizado o acesso ao cadastro de grupo de contábil em cadastros de Agrupamento de Contas Contábeis.
* Otimizado o processo de cálculo de encargos contábeis (contabilização e geração de encargos) quando o mesmo utiliza percentagem com número de casas decimais maior que 2.

**11.20.0 – Financeiro**  
 Tratamento no processo de lançamentos financeiros, passando permitir fórmulas para complemento de histórico que contenham a variável PAR na parametrização dos lançamentos financeiros.  
    
 **11.20.0 – Cadastro de Fórmulas**

* Implementada a variável NDIASDESCGRP que verifica o número de dias de descanso em um período determinado, cadastrados no Grupo de Descanso associado ao funcionário no RM Chronus.
* Implementada a variável BASERECFER( ), possibilitando o retorno da base de INSS ou base de IRRF  do último recibo de férias cadastrado para o funcionário.

**11.20.0 – Cadastro de Perfis**

* Implementado o item de segurança 'Histórico de Dados Bancários' do cadastro de Funcionários.
* Implementado o item de segurança para o processo 'Sincronizar Centros de Custos global com Centros de Custos do RM Labore' do cadastro de Centro de Custo (RM Labore)
* Otimizado o item de segurança do Agrupamentos de Contas Contábeis (RM Labore).
* A partir desta versão foi ajustado o item de segurança 'Eventos Programados' do cadastro de Funcionários. Sendo necessário revisar os perfis que possuem acesso a este item.

**11.20.0 – Importação do PIS pela Empresa**  
 Atualização na importação do PIS quando existe funcionário com período bloqueado parcialmente.  
    
 **11.20.0 – Cadastro de Férias**

* O sistema passou a não permitir o cadastramento de Dias de Abono, quando calculado 30 dias de férias para o funcionário.
* Otimizada a visualização do Cadastro de Férias para funcionários que possuem faltas.
* Otimizado o cálculo de salário comissão nas férias, quando no período de apuração da média houve outro período de gozo de férias.

**11.20.0 – Diferença de Férias**

* Otimizado o cálculo da diferença de férias por dissídio quando as férias são partidas.
* Otimizado o cálculo do INSS em meses com férias partidas.

Ajustada a descrição do parâmetro 'Dias de direito para func. > 1 ano' para 'Verifica faltas funcionário >1 ano'**,** possibilitando o cadastramento das férias coletivas ou globais considerando as faltas do funcionário.  
 Veja mais detalhes no Help.  
 **11.20.0 – Rescisão**

* A partir desta versão, não será permitido o cálculo de rescisão quando o funcionário tiver férias cadastradas para o próximo mês.
* Otimizada a inclusão do novo motivo de demissão, quando é utilizado o ícone "Cadastro de motivos de demissão" na rescisão.
* Otimizado o processo de cálculo da rescisão de funcionário admitido em novembro, e demitido logo após o lançamento da 1ª parcela de 13º Salário.
* Otimizado o processo para desativar o usuário no momento da rescisão individual ou coletiva. O sistema passou a desabilita também a permissão de acesso ao RM Portal.
* Otimizado o cálculo do número de dias de Saldo de Salário pagos na demissão, quando a rescisão é calculada com data igual ao último dia do mês, em meses de 31 dias.
* Os novos relatórios do termo de rescisão, conforme portaria 1.621 de 14 de Julho de 2010 já estão disponíveis. Para utilizá-los, favor fazer a importação dos mesmos.
* A partir desta versão, o sistema passará a realizar o lançamento do evento de código de cálculo 150 quando for processado o módulo de Lançamento de liquido. Maiores informações consulte o Help do módulo Lançamento de liquido no menu de Rescisão.
* A rescisão por transferência foi atualizada para garantir a integridade da movimentação de batidas de responsabilidade do TOTVS Automação de Ponto, referente ao novo conceito disciplinar da Portaria 1510/2009.

**11.20.0 – Alteração Global de Salários**  
 Implementado o parâmetro 'Alteração de Salários por Percentual', permitindo o usuário efetuar alterações salariais de acordo com percentual pré-estabelecido.  
    
 **11.20.0 – Geração de Lançamentos Financeiros**

* Otimizada a geração do lançamento financeiro de IRRF, para funcionário que tem a data de pagamento da rescisão anterior a data de pagamento da folha.
* Otimizada a geração do lançamento financeiro, quando na parametrização de lançamentos possuírem fórmulas repetidas.
* Otimizada a geração do lançamento financeiro de Pensão Alimentícia, quando o funcionário possui mais de um dependente de pensão e existem verbas de diferença salarial na movimentação do mês.

**11.20.0 – Geração da Movimentação**  
 Aperfeiçoada a geração da movimentação quando todos os funcionários são selecionados.  
 **11.20.0 – Transferência Manual dos Registros da Ficha Financeira**  
 Implementada a transferência manual dos registros da ficha financeira para que quando a opção na liberação da competência que é "Transferir registros da Ficha Financeira para Ficha Financeira Complementar anterior a ...." não for marcada os dados da ficha financeira sejam transferidos manualmente.  
    
 **11.20.0 – Liberação de Flgs FGTS**  
 Otimizado o filtro de seleção de funcionários.  
    
 **11.20.0 – Cálculo de Benefícios de Funcionário**

* Otimizado o cálculo do benefício quando não é informada fórmula de percentual.
* Otimizado o cálculo do benefício quando é utilizado filtro.
* Otimizada as mensagens na tela de cálculo do benefício.

**11.20.0 - Gestão Educacional**  
 Implementado os campos 'Data Início da Atividade' e 'Data Final da Atividade' nas Informações do Educacional e na edição da Distribuição das Horas do Movimento de Ensino.  
    
 **11.20.0 - Homolognet**  
 Implementado o assistente de geração do arquivo do Homolognet (sistema disponibilizado pelo Ministério do Trabalho e Emprego para a homologação de rescisões por meio eletrônico).  
    
 **11.20.0 - Folha Analítica**  
 Otimizada a demonstração do valor no 'INSS Empresa', passando a considerar também o valor da Base INSS Autônomos.  
    
 **11.20.0 - GRFC**  
 Otimizada a verificação do campo 'Reposição de Vaga' quando o mesmo não é alterado pelo usuário.  
    
 **11.20.0 - SEFIP.Net**

* Atualizado o desempenho e uso de memória do SEFIP, quando existem mais 18.000 registros na base.
* Atualizado o relatório do SEFIP, quando o parâmetro  'Sefip para 13º Salário' estiver marcado e o colaborador possuir na movimentação o evento de restituição de INSS com o código de cálculo 92 e ocorrência 5.
* Otimizada a importação de autônomos na geração do arquivo SEFIP.RE, quando nos parâmetros específicos da coligada, o parâmetro "Importar autônomos de outros sistemas" está marcado.
* Otimizado a geração do arquivo do SEFIP em dezembro, quando há pagamento de diferenças de 13º Salário.
* Otimizado o processo de importação de autônomos do RM Fluxus na geração do aquivo do SEFIP. Tratamento para considerar como zerada a base de INSS Outra Empresa que não foi preenchida na geração do lançamento.
* Tratamento para informar 0,01 centavo no campo 'Base de Cálculo do 13º Salário da Previdência', quando o funcionário não teve base de 13º Salário no cálculo de rescisão.

**11.20.0 - Guia de INSS**  
 Implementada a gravação do código que identifica o Lançamento Financeiro da GPS, considerado na geração do Layout de Pagamento de GPS.  
    
 **11.20.0 - GRCSU**  
 Atualização no relatório da GRCSU, quando existe diferença de contribuição sindical com código de cálculo 198.  
    
 **11.20.0 - RAIS**

* Otimizado o processo de geração da RAIS, que passa a desconsiderar valores de eventos informados na tela de geração nos campos existentes na aba 'Eventos', na composição da remuneração do mês da rescisão.
* Otimizado o processo de geração da RAIS, que passa a observar de forma mais completa, os valores de 13º Salário pagos durante o Ano-Base para funcionário transferido.

**11.20.0 - Parâmetros do Sistema**

* Implementado nos Parâmetros de Rescisão, o parâmetro 'Ignora eventos que incidem em salário no Aviso Prévio Indenizado', possibilitando ao usuário definir se eventos que incidem em salário irão ou não compor a base de Aviso Prévio Indenizado.
* Implementado nos Parâmetros de Rescisão, o parâmetro 'Permite cópia da Ficha Financeira por Centro de Custo entre coligadas'.
* Implementado em Outros Parâmetros, o parâmetro 'Armazena Geração da Guia de INSS por chapa', possibilitando ao usuário armazenar os valores da Guia de INSS (GRPS e GPS) por chapa.
* Implementado em Outros Parâmetros, o parâmetro 'Não cadastrar número de Ficha de Registro para Temporários', permitindo a inclusão de funcionário do tipo P-Temporário sem a informação do número da ficha de registro.

**11.20.0 - Importação de Dados do RM Labore**

* Otimizado o processo de importação de histórico de afastamento, permitindo a importação do código do tomador de serviço e seu respectivo CEI, utilizado no afastamento por Acidente de Trabalho.
* Otimizado o processo de importação de histórico de ocorrências do SEFIP, passando a substituir o registro do cadastro quando no arquivo importado existir registro com a mesma data.
* Otimizada a rotina de importação de eventos, com relação à marcação de "Acumuladores".

**11.20.0 - Avisos Automáticos**  
 Atualização dos avisos automáticos quando existem avisos desativados.  
    
 **NOVIDADES DA MÁQUINA DE CÁLCULO**  
    
 **11.20.0 - Módulos Migrados para a plataforma .NET**  
 A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft.  
 Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados ou novos nesta versão são:

* Geração Histórico de Provisões (.Net)
* Importação de Movimento (.Net)
* Liberação de Competência (.Net)
* Controle de Faltas Bloquear Lançamentos
* Controle de Faltas Consultar Lançamentos Bloqueados
* Controle de Faltas Importação
* Eventos Programados

**11.20.0 - Cadastro de Funcionários**

* Implementado no anexo 'Descontos de Empréstimos' o campo 'Nro. Parcelas Pagas', com a finalidade de armazenar a quantidade de parcelas descontadas na rescisão, de forma que no processo de Cancelamento de Rescisão seja restaurado o Saldo Devedor  e nº de parcelas anteriores ao cálculo da rescisão.
* Implementada a visualização dos Logs de Cálculo e de Média no Histórico de Provisões.
* Implementada a visualização de Relatórios do Gerador no cadastro de Funcionários e de Rescisão.
* Implementado o anexo 'Controle de faltas para cálculo de avos', com o objetivo de considerar o dia efetivo da falta no cálculo de avos de Férias e 13º Salário.
* Implementado o anexo 'Eventos Programados', possibilitando ao usuário determinar o inicio e fim do lançamento de um evento, assim com um centro de custo específico. É possível cadastrar o mesmo evento para o mesmo funcionário mais de uma vez.

**11.20.0 – Cadastro de Eventos**

* Implementado o código de cálculo 315-BASE DE FGTS DE AFASTADOS, com o objetivo de facilitar a composição da Base de FGTS do Funcionário afastado por Acidente de Trabalho(P), Serviço Militar(M) ou Doença Ocupacional(O).
* Implementado o código de cálculo 313 - JORNADA MENSAL CONSIDERANDO HORAS TRABALHADAS para clientes que utilizam o RMChronus. Veja mais detalhes no help Códigos de Cálculos.
* A partir desta versão o cadastro de evento passou a preencher o campo SEGUERATEIOMOVENSINO quando o parâmetro "Segue Rateio Movimento de Ensino Importado" é alterado, em versões anteriores o sistema preenchia o campo SEGUERATEIOSALCMP.

**11.20.0 – Cadastro de Fórmulas**

* Implementada as variáveis de fórmulas EP, EXISTEEP, NEPRG e TABEVTPROG, com a funcionalidade de retornar informações dos eventos programados do funcionário.
* Implementada a variável de fórmula TOTALFALTAS, para facilitar o desconto das faltas do funcionário quando o cliente não tem integração com o RM Chronus e utiliza o Controle de faltas para cálculo de avos.

**11.20.0 - Cadastro de Sindicato**  
 Implementado o parâmetro 'Substitui período de afastamento por meses anteriores' no Cadastro de Médias do Sindicato.  
    
 **11.20.0 – Tabelas** **Dinâmicas**  
 Implementado o código 'TPEVTPROG-Tipo de Eventos Programados', para o usuário definir os grupos para lançamento dos eventos programados.  
    
 **11.20.0 – Cadastro de Perfis**

* A partir desta versão foi criado em todos os históricos do anexo do funcionário o item de segurança 'Visualizar'. Sendo assim será necessário ajustar todos os perfis que possuem acesso a estes históricos.
* Implementado os itens de segurança abaixo no cadastro de Funcionários:
  + Período de Gozo
  + Eventos Programados
  + Histórico de Dados Bancários
  + Definição da(s) chapa(s) e coligadas centralizadora(s) de IRRF/INSS
  + Controle de Faltas
* Implementado no item de segurança 'Consulta Movimento de Ensino Importado' as opções Inserir, Editar e Excluir.

**11.20.0 - Cadastro de Férias**

* O sistema passou a gravar o salário do funcionário na tabela PFUFERIASRECIBO no momento do cálculo do recibo de férias.
* Implementada o recurso para o usuário selecionar o status de férias que desejar cancelar. Foram disponibilizados os status:
  + D-Aguardando aprovação DP
  + G-Aguardando aprovação Gestor
  + M-Marcadas
* Otimizada a rotina de Cálculo de Férias, possibilitando antecipar dias de férias do próximo período aquisitivo quando o funcionário não tem saldo suficiente para total de dias de férias.

**11.20.0 - Rescisão**

* O sistema passou a trazer o parâmetro "Substituir arquivo" marcado no Cancelamento de Rescisão.
* Implementado o parâmetro 'Lança Eventos Programados'.

**11.20.0 - Parâmetros do Sistema**

* Implementado nos Parâmetros de Cálculo, o parâmetro 'Utiliza controle de faltas para cálculo de faltas'.
* O sistema passou a somar os dias de atestados dentro do período de carência com o mesmo motivo. E foi retirado o parâmetro "Soma dias atestados dentro período de carência pelo mesmo motivo" existente em Parâm. Cálculo.
* Implementada nos Parâmetros de Rescisão e Parâmetros de 13º Salário, a aba 'Eventos Programados', para usuário definir quais eventos deverão ser lançados na rescisão e 13º salário.
* Implementada nos Parâmetros de Rescisão, a aba 'Eventos de Integração' que permite ao usuário selecionar qual(is) o(s) tipo(s) evento(s) de integração com outros aplicativos serão lançados no cálculo da rescisão.
* Implemento em Outros Parâmetros, o parâmetro 'Caminho padrão para gravação \ importação de arquivos.txt.' que permite inserir um diretório local ou na rede para a gravação dos arquivos texto.

**11.20.0 – Importação de Dados do RM Labore**  
 Implementado a importação dos Eventos Programados em Funcionário | Funcionário I.  
    
 **11.20.0 - Gestão Educacional - Cálculo do Movimento de Ensino**  
 O log de Aviso que é gerado ao fim do Cálculo do Movimento de Ensino foi otimizado e irá demonstrar apenas os funcionários que tiveram o novo cálculo de movimento.  
    
 **11.20.0 – Grupos de Eventos.Net**  
  Implementado o parâmetro 'Lança Eventos Programados'.  
    
 **11.20.0 – 13º Salário**  
  Implementado o parâmetro 'Lança Eventos Programados'.  
    
 **11.20.0 – Férias Coletivas / Globais**
