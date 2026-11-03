---
content_hash: ffbbbcdf31e0038b93819a095f48896a5d66d48574c8d0246cb9935e18fd9a7c
fetched_at: '2026-06-29T00:10:03.964642+00:00'
page_id: '452719180'
product: rm
source: tdn-rm
title: Homolognet - FOP
type: documentation
url: https://tdn.totvs.com/display/LRM/Homolognet+-+FOP
version: 2
---

**Geração do Arquivo do Homolognet**  
    
 Aqui o usuário encontrará as informações necessárias para a correta geração do arquivo XML que será enviado para o Ministério do Trabalho, através do novo sistema de homologação de rescisões – Homolognet.  
    
 Antes de iniciar qualquer procedimento aqui descrito, aconselhamos a leitura completa dos manuais e outras publicações feitas pelo Ministério do Trabalho sobre o tema.   
    
 Outros documentos que devem ser lidos e entendidos são os tópicos de ajuda de outros módulos do sistema que sofreram alterações para se adequarem e consolidarem informações solicitadas no layout. São eles:  
    
 Cadastro de Eventos  
 Cadastro de Sindicatos  
 Rescisão  
    
 Somente após o total entendimento das informações recomendamos a geração do primeiro arquivo. Esse processo é feito a partir do Assistente de Geração do Arquivo Homolognet.  
    
 **Assistente de Geração do Arquivo do Homolognet**  
    
 Aqui se encontram as etapas que o usuário irá passar para a geração do arquivo XML do Homolognet. Esse assistente é composto pelos 4 passos abaixo:  
    
 Perfil de Parâmetros e Descrição do Processo  
 Seleção de Funcionários e Período  
 Eventos  
 Concluindo o Assistente  
    
    
 **Perfil de Parâmetros e Descrição do Processo**  
    
 É a tela inicial do assistente de geração do arquivo XML do Homolognet. Aqui, é dado início à geração do arquivo de acordo com layout definido pelo MTE (Ministério do Trabalho e Emprego). Essa tela é composta dos parâmetros abaixo:  
    
             **Caixa "Perfil de Parâmetros"**  
    
 Essa caixa é composta de três itens:  
    
 Combobox - Esse é o local onde são criados novos perfis ou selecionados perfis criados anteriormente. Na primeira execução do assistente é **obrigatória** a criação de um perfil.  
    
 Excluir - Esse botão tem a finalidade de excluir um perfil que não é mais utilizado.  
    
 Salvar Perfil ao Incluir - Esse Check Box tem a finalidade de indicar que o perfil que está sendo utilizado será modificado durante a execução do assistente e que tais modificações deverão ser gravadas. Ao utilizar um perfil sem a marcação desse parâmetro, caso o mesmo seja modificado durante o processo, essas alterações não serão gravadas. Na criação de um novo perfil esse parâmetro deverá estar marcado.  
    
 **Seleção de Funcionários e Período**  
    
 Aqui são informados os dados básicos para a geração do arquivo como: o período das rescisões, seleção dos funcionários e local onde o arquivo será gravado.  
    
 **Seleção de Funcionários**  
 Ao clicar no botão de Seleção de funcionários o sistema abrirá uma janela com os campos onde você poderá selecionar um funcionário digitando sua chapa ou localizando seu nome. Também será possível fazer a seleção de funcionários pela situação, tipo de funcionário e recebimento ou ainda criar Filtros ou Fórmulas de Seleção.  
    
 **Utiliza CNPJ Coligada**

Esse parâmetro ficará habilitado independentemente da coligada utilizar ou não CEI. Se esse parâmetro for marcado e a empresa utilizar CEI, retornará para os dados do empregador o CNPJ da Coligada. Se a empresa utilizar CEI e o parâmetro não for marcado, o sistema levará para o arquivo o CEI registrado na seção do funcionário. Se a empresa não utilizar CEI e não marcar o parâmetro, será retornado o CNPJ da Seção do funcionário. Caso marcar o parâmetro, será retornado o CNPJ da Coligada.  
    
 **Período**  
 **Data Inicial:** É a data inicial de apuração das rescisões que serão consideradas na geração do(s) arquivos(s) XLM do Homolognet;  
    
 **Data Final:** É a data inicial de apuração das rescisões que serão consideradas na geração do(s) arquivos(s) XLM do Homolognet;  
    
 **Competência Atual:** Marcando esse CheckBox o sistema irá considerar somente as rescisões da competência atual. Os campos data inicial e final serão preenchidos, respectivamente, com o primeiro e o último dia da competência atual.  
    
    
 **Fórmula Para Funcionários Cujo Salário Já Foi Pago**  
 Anteriormente o sistema não oferecia um modo seguro de garantir que o salário do mês anterior foi pago, a solução foi criar um lookup para utilização de fórmula. A fórmula deverá retornar TRUE se o salário do mês anterior a rescisão de um funcionário foi pago, ou FALSE caso contrário.   
 Comportamento esperado : A TAG VLSalaioLiquidoMesAnteriorARescisao NÃO  deve aparecer no homologNet caso esteja TRUE na formula. Pois indica que o salário  foi pago anteriormente no envelope do funcionário e  não deve ser pago na rescisão.  
 Comportamento esperado : A TAG VLSalaioLiquidoMesAnteriorARescisao  deve aparecer no homologNet caso esteja FALSE na fórmula. Pois indica que o salário não foi pago anteriormente no envelope do funcionário e deve ser pago na rescisão.  
    
 **Desconsiderar incidência em salário para base de periculosidade:** Marcando este parâmetro, o processo não irá considerar os eventos com código de rubrica 014 que incidem em salário para o valor de base de cálculo para a rubrica. Quando não marcado, irá considerar os eventos com código de rubrica 014 que incidem em salário no valor de base de cálculo para rubrica.  
    
    
 **Considerar Evento Base Gratificação Com o Código da Rubrica 017**  
  Se o parâmetro estiver marcado, o sistema verifica a existência de um evento do tipo BASE, que tenha a rubrica 017 vinculada, caso o parâmetro esteja desmarcado e a rubrica estiver no evento de BASE ele não leva valor nenhum. Caso a rubrica 017 esteja em um PROVENTO e o parâmetro Marcado/Desmarcado, sistema leva o valor que estiver no Provento.   
    
 **Localização do(s) Arquivo(s) XLM**  
 Selecionar a pasta para informar o local de geração do(s) arquivo(s)  
    
    
 **Eventos**  
 Aqui são informados alguns eventos de desconto que possuem tratamento especial no Homolognet e que não possuem código de cálculo específico.  
    
 **Evento Valor Vale Alimentação**  
 Informe o código do evento de Vale Alimentação.  
    
 **Evento Reembolso Vale Alimentação**  
 Informe o código do evento do Reembolso do Vale Alimentação.  
 **Indenização Art. 480 CLT**  
 Informe o código do evento da Indenização Art. 480.  
 **Contribuição Previdência Privada**  
 Informe o código do evento de Previdência Privada.  
 **Contribuição FAPI**  
 Informe o código do evento da Contribuição FAPI.  
    
 **Outras Deduções IRRF**  
 Informe o código do evento de outras deduções de imposto de renda.  
    
 **Aviso Prévio Misto**  
    
 O layout do arquivo de importação definido pelo Ministério do Trabalho e Emprego (MTE) na versão 2.10 permite apenas informações sobre aviso prévio trabalhado ou aviso prévio indenizado, não tratando o aviso prévio misto.  
 Conforme informações abaixo:  
 "Duração do Aviso Prévio: Informar o número de dias de aviso prévio estabelecido no instrumento coletivo de trabalho da categoria profissional"  
 "Data do Aviso Prévio: Data em que o empregado ou empregador foi pré-avisado do término do contrato de trabalho."  
    
 Para atender demanda de clientes, o sistema permite a escolha das informações a serem levadas para estes campos de acordo com o entendimento da empresa.  
 O usuário poderá escolher entre as seguintes opções:  
    
 Quantidade de dias:  
    
 *Informar quantidade de dias de aviso prévio indenizado:* Marcando essa opção o sistema levará para o campo "Duração do aviso prévio" no homolognet, apenas a quantidade de dias que foram indenizados ao funcionário.  
 *Informar quantidade de dias de aviso prévio trabalhado:* Marcando essa opção o sistema levará para o campo "Duração do aviso prévio" no homolognet, apenas a quantidade de dias que o funcionário trabalhou no aviso prévio.  
 *Informar quantidade de ambos (indenizado + trabalhado):* Marcando essa opção o sistema levará para o campo "Duração do aviso prévio" no homolognet, o somatório dos dias que foram indenizados e trabalhados pelo funcionário.  
    
 Data de início:  
    
 *Informar data de início de aviso prévio indenizado:* Marcando essa opção o sistema levará para o campo de Data do aviso prévio, a data do aviso indenizado no cadastro da rescisão.  
 *Informar data de início de aviso prévio trabalhado:* Marcando essa opção o sistema levará para o campo de Data do aviso prévio, a data do aviso trabalhado no cadastro da rescisão.  
    
 **Concluindo o Assistente**  
    
 Esse é o processo final. Ao ser executado, criará o arquivo XLM e, no seu fechamento, irá demonstrar o um log demonstrando todos os arquivos que foram gerados com sucesso ou demonstrando todos os erros e avisos encontrados.  
    
 Dependendo do número de rescisões no mês, o sistema poderá gerar vários arquivos. Essa separação em vários arquivos é justificada pela existência de várias variáveis. Essas variáveis são visíveis no próprio nome do arquivo e, a partir do entendimento da composição do nome entenderemos melhor a divisão. Abaixo segue o nome do arquivo XML gerado pelo RM Labore, e o significado que cada número em seu formato:  
    
 **HomologNet\_Id(11111030)\_Col(1)\_Secao(01)\_Sindic(0001)\_Funcs(000015).xml**  
    
**1**  
 Indica se os funcionários cumpriram integralmente ou não a jornada de trabalho**.**  
 **1**  
 Indica se os funcionários compensam ou não o sábado durante a semana.  
 **1**  
 Indica a forma de calcular as médias das verbas salariais variáveis 13º salário.  
 **1**  
 Indica a forma de calcular as médias das verbas salariais variáveis Férias.  
 **1**  
 Indica a forma de calcular as médias das verbas salariais variáveis Aviso Prévio.  
 **030**  
 Indica a duração para o aviso prévio.  
 **Col(1)**  
 Código da Coligada.  
 **Sindic(0001)**  
 Código do Sindicato.  
 **Secao(01)**  
 Código da Seção  
 **Funcs(000015)**  
 Quantidade de funcionários gerados no arquivo.  
    
 **Observação:** Os cinco primeiros campos são indicadores que são informados de acordo com as especificações do arquivo de leiaute disponibilizado pelo MTE. Caso queira entender melhor como esses campos podem ser preenchidos, recomendamos a leitura deste arquivo.
