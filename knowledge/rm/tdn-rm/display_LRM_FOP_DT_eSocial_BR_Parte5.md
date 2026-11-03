---
content_hash: 001ffaa76dfbb3a03641e5f5962c5ef9f42ad9672b3e91533cdf6520d342a127
fetched_at: '2026-06-29T00:06:18.785071+00:00'
page_id: '219686575'
product: rm
source: tdn-rm
title: FOP_DT_eSocial_BR_Parte5
type: documentation
url: https://tdn.totvs.com/display/LRM/FOP_DT_eSocial_BR_Parte5
version: 18
---

# ESOCIAL - SANEAMENTO DE DADOS LAYOUT 2.1 E CARGA INICIAL XML

## Características do Requisito

  

| **Linha de Produto:** | *RM* |
| --- | --- |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Folha de Pagamento** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *eSocial* | *Carga inicial XML* | |
| **Versões / Release:** | Biblioteca RM 12.1.8 **|** 11.83 **|** 11.82.42(patch 138) |
|  |  |

## Descrição

Este documento trata-se de evoluções cadastrais relacionadas ao “Requisito: Adequação de Campos cadastrais  – Layout 2.1 do eSocial  e geração da Carga Inicial de Dados XML.

Evoluímos o requisito conforme tópicos abaixo :

**Módulo Geração da Carga Inicial de dados**

* **S-1000**–******Informações do Empregador/Contribuinte**
* **S-1005**–******Tabela de Estabelecimentos e Obras de Construção Civil (Cadastro de Seção e Tomador de Serviço)**
* **S-1010**–******Tabela de Rubricas (Cadastro de Eventos)**
* **S-1020**–**Tabela de Lotações Tributárias (Cadastro de Seção)**
* **S-1030**–**Tabela de Cargos (Cadastro de Função)**
* **S-1050**–**Tabela de Horários/Turnos de Trabalho**
* **S-1070**–**Tabela de Processos Administrativos/Judiciais**
* **S-2100**–**Cadastramento Inicial do Vínculo (Cadastro de Funcionário)**

**Atenção :**  O governo ainda não liberou o ambiente de teste, portanto a utilização da carga inicial de dados será somente para conferência de dados cadastrais conforme layout 2.1 do eSocial.

**Programa “Executor de Scripts” - Conversão do Modelo de dados - Utilização somente nas versões 11.82 e 11.83**

11.83.55 (Específica) - 22/12/2015

11.82.42 (Específica)-  30/03/2016   
  
Para utilização da versão eSocial 5º pacote  o usuário Administrador do sistema deverá executar o programa “Executor de Scripts” na base de dados: RM.Script.Executor.exe para base MSSQL ou ORACLE.  
Nesta atualização constam os scripts do 2º , 3º , 4º e 5º pacote. Caso já tenha rodado o 2º ,  3 º e 4º pacote,  ao executar o programa não executará novamente, somente scripts do  5º  pacote.  
O 1º  pacote foi atualizado através de conversor, não sendo considerado neste Executor de Scripts.   
Ao final deste documento, veja em Informações Adicionais como executar o programa de atualização da base de dados. Este executor de scripts não se aplica as versões 12.1 

# **Módulo da Carga Inicial**

O acesso ao módulo está disponível na MDI .Net conforme imagem abaixo: 

Na tela inicial é possível selecionar quais os tipos arquivos deseja gerar. Selecionando o tipo “S-2100” será habilitada a seleção de funcionários para fazer filtros:

Para filtrar os demais eventos e/ou filtrar o “S-2100” para uma chapa específica é necessário acessar os Parâmetros da Coligada:  
Para geração dos XMLs deverá informar o caminho onde será salvo o arquivo.  
  
Nesta primeira versão será liberado somente a geração da tag  ‘Inclusão’.  
As tags “Alteração “ e “Exclusão” serão disponibilizadas após a liberação do ambiente de teste do governo.

Após a geração  serão  gerado logs de Aviso, Erros e de Execução.

**Avisos**Campos obrigatórios não informados serão avisados aos clientes e deverão ser informados, caso contrário,  não serão processados quando ocorrer o envio para o governo.

**Erros**Quando ocorrer erros como o exemplo abaixo, o XML será gerado.Porém, será necessário a correção para não ser barrado na validação do XML pelo governo.  
“O campo 'natRubr' do registro 'dadosRubrica' é obrigatório e não está preenchido”

**Execução**Exibe a descrição dos eventos processados  
  
Total de eventos processados: 1.  
Total de eventos processados: 4.  
Total de eventos processados: 547.  
Total de eventos processados: 574.  
Total de eventos processados: 613.  
Total de eventos processados: 729.  
Total de eventos processados: 730.  
 

# **Eventos da Car****ga Inicial**

**S-1000** – **Informações do Empregador/Contribuinte**

O S-1000 é o primeiro evento do eSocial que deve ser transferido pelo Empregador/Contribuinte e não pode ser enviado outro evento antes deste. O Empregador/Contribuinte fornece informações cadastrais, alíquotas e outros dados necessários para o preenchimento e validação dos demais eventos do eSocial, inclusive para apuração das contribuições.  
 Neste evento estão as informações para a apuração correta das contribuições, como a classificação tributária do contribuinte, indicativo de desoneração da folha, FAP, isenções para entidades beneficentes de assistência social, acordos internacionais para isenção de multa, situação da empresa (normal, extinção, fusão, cisão ou incorporação), cooperativas de trabalho, construtoras, opção pelo registro eletrônico de empregados, processos judiciais e administrativos, entre outras.

No sistema, o evento não possui mais o campo “aliqRat”. Esta informação foi removida da tela **Informações do Empregador**  
   
 CAMINHO:  **TOTVS Folha de Pagamento / eSocial (Beta) / Informações do Empregador**.

  Antes

 Depois

Neste evento, será gerado um único XML, que corresponde as informações do empregador para a coligada atual.

**S-1005** – **Tabela de Estabelecimentos e Obras de Construção Civil**

Este evento identifica os estabelecimentos e obras de construção civil da empresa, detalhando as informações de cada estabelecimento (matriz e filiais) do empregador/contribuinte, como por exemplo, informações relativas ao CNAE Preponderante.  
 As informações prestadas no evento são utilizadas na apuração das contribuições incidentes sobre as remunerações dos trabalhadores dos referidos estabelecimentos, obras e CAEPF.

Neste evento, será gerado um XML para cada **Seção**, desde que o tamanho do código da seção seja igual ao tamanho do “Código de quebra do CNPJ” (**Parametrizador / 06.04 RH Máscaras e quebras**), e os **Tomadores de Serviço** do tipo Obra Própria (tipo de lotação “01”) e que estiverem com o novo campo “Tomador Folha” marcado,  veja abaixo:

**Criado novos campos no cadastro de Seção para atender o saneamento de dados 2.1 para o evento de  S-1005 – Estabelecimentos e Obras**

Campos para processo de alteração das alíquotas RAT e FAP. Esses campos devem ser preenchidos caso exista algum processo judicial que altere alguma dessas alíquotas para o estabelecimento.

**Criado novos campos no cadastro de Tomador (cliente/Fornecedor)  para atender o saneamento de dados 2.1 para o evento de  S-1005 – Estabelcimentos e Obras****- “Tomador de serviços folha”:** Indica que o Cliente/Fornecedor será lido na carga inicial pelo E-Social.  
**- “CNO da obra própria”:** CNO da obra, que deverá ser preenchido para alguns tipos de lotação.  
**- “FPAS”****- “CodTerc Alíquota de FPAS de terceiros”****“Indicativo de Substituição da Contribuição Patronal de Obra de Construção Civil”****“Alíquota CNAE Preponderante”****“CNAE Preponderante”**

**S-1010 - Tabela de Rubricas**

Esse evento apresenta o detalhamento das informações das rubricas da folha de pagamento da empresa. É utilizado para inclusão, alteração e exclusão de registros na tabela de rubricas do empregador/contribuinte. As informações consolidadas desta tabela são utilizadas para validação do evento de Remuneração dos trabalhadores.

Para enviar este evento, é necessário o envio prévio do evento de Informações Cadastrais do empregador/contribuinte.

Neste evento, será gerado um XML para cada **Evento** ativo.  
Nesta versão foi criado a natureza de rubrica “2510 -  Direitos autorais e intelectuais”

**S-1020 - Tabela de Lotações Tributárias**

Este evento identifica a classificação de atividades para fins de atribuições do código FAPS, a obra de construção civil, o contratante de serviço, ou uma condição diferenciada de tributação. É utilizado para inclusão, alteração e exclusão de registros na tabela de LOTAÇÕES do empregador. As informações consolidadas desta tabela são utilizadas para validação de outros eventos do eSocial (ex: admissão, alteração contratual, remuneração, etc.).

Neste evento, foi gerado um XML para cada **Seção** folha (seções de último nível) e todos os **Tomadores de serviço** que estiverem com o novo campo “Tomador Folha” marcado.

**S-1030** – **Tabela de Cargos** **(cadastro de Função no RM)**

Este evento contém as informações de identificação do cargo,  apresenta o código e período de validade. É utilizado para inclusão, alteração e exclusão de registros na Tabela de Cargos do empregador/contribuinte. As informações consolidadas nesta tabela são utilizadas para validação de diversos eventos do eSocial, entre os quais os eventos de cadastramento inicial, admissão, alteração de dados contratuais, etc.

Os cargos podem ser encontrados através do caminho, **Totvs Folha de Pagamento / Administração de Pessoal / Função**

Neste evento, será gerado um XML para cada **Função** ativa (PFUNCAO).

**S-1050** – **Tabela de Horários/Turnos de Trabalho**

Este evento contém, as informações de identificadores do horário contratual, apresentando o código e período de validade do registro. Detalha os horários de início e término do intervalo para a jornada de trabalho. É utilizado para inclusão, alteração e exclusão de registros na tabela de horários/turnos de trabalho.

As informações sobre turno de trabalho são calculadas de acordo com as configurações do Totvs Automação de Ponto.

Neste evento, será  gerado um XML para cada **Intervalo de Horários** por intervalo e por jornada, para cada índice.

**S-1070** – **Tabela de Processos Administrativos/Judiciais**

Este evento é utilizado para inclusão, alteração e exclusão de registros na Tabela de Processos Administrativos/Judiciais do empregador/contribuinte, de entidade patronal com representação coletiva, de trabalhador contra um dos órgãos governamentais envolvidos no projeto e que tenha influência no cálculo das contribuições, dos impostos do FGTS, e de outras empresas, quando influenciem do comprimento das suas obrigações principais e acessórias. As informações consolidadas desta tabela são utilizadas para validação de outros eventos do eSocial.

Neste evento, será gerado um XML para cada **Processo** cadastro no Vitae, que estiver com o campo “Processo da empresa contra órgão governamental envolvido no eSocial” marcado conforme imagem abaixo:

**S-2100** – **Cadastramento Inicial do Vínculo**

Este evento se refere ao arquivo que será enviado pela empresa no início da implantação do eSocial, com todos os vínculos ativos, com seus dados cadastrais atualizados, servindo de base para a construção do ‘’ Registro de Eventos Trabalhistas’’.  
Neste evento, será  gerado um XML para cada **Funcionário** com situação **diferente** de “D – Demitido”, ou se demitido,  que tenha alguma movimentação na competência atual.  Não serão considerados funcionários dos tipos “A – Autônomo”, “D – Diretor” e “T - Estagiários”. Estes funcionários serão enviados no evento “S-2300” que está em desenvolvimento.

# **Informações Adicionais**

**Atenção** : Para execução do programa Executor de Scripts,  deverá desabilitar o ‘Log de auditoria’,  caso o cliente utilize.  
No Portal do Cliente, disponibilizamos o **PacoteeSocial5Entrega.zip**, que contém compactado os programas de atualização de campos da base: **RM.Script.Executor.exe** para execução da atualização da base MSSQL e ORACLE.

**Descompacte os arquivos.**   
Para os usuários do sistema utilizar os novos campos implementados de acordo com o eSocial, será necessário executar o programa compatível com a sua base, seguindo o passo a passo abaixo:

1) Pedimos a atenção do usuário Administrador do Sistema para **fazer o backup da base de dados de produção, antes de realizar os passos seguintes.**Para a execução do programa, siga os passos conforme link a seguir Veja orientações no link a seguir  <http://tdn.totvs.com/display/public/rm/Executor+de+Scripts+RM>2) Ao fim do processo, será exibido o resultado da execução. Caso tenha executado com sucesso será exibido uma mensagem informando o número de linhas afetadas (isto quer dizer que foi executado com sucesso).  
3) Caso seja registrado número de erros maior que 0 (zero), poderá indicar necessidade de restaurar o backup de segurança da sua base. Entre em contato com nosso suporte.
