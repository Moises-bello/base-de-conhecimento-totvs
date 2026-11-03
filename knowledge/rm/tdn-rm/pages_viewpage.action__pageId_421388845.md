---
content_hash: 811cf173723a7e1fbc96933350958908e26b0d611b4f612a9b700d179c4ab6e7
fetched_at: '2026-06-29T00:09:19.356728+00:00'
page_id: '421388845'
product: rm
source: tdn-rm
title: FIN - Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388845
version: 67
---

LGPD - Lei Geral de Proteção de Dados

Informamos que possui dados pessoais contidos nesta entidade. Foram colhidos para geração de rotinas financeiras.

Para mais informações sobre a LGPD e as soluções oferecidas pela TOTVS, clique [aqui](https://espacolegislacao.totvs.com/lgpd/).

O cadastro de Convênio unifica toda a regra dos processos da integração bancária, assim como Carteira, tipo de Cobrança, etc. É muito importante que esses dados sejam validados antes de iniciar o processo e que estejam em conformidade com o manual fornecido pelo banco, pois assim que houver boleto gerado para lançamentos associados ao Convênio, por segurança e integridade dos dados, nenhuma alteração será permitida no cadastro. Para gerar boletos é necessário que exista o Convênio cadastrado e para realizar este cadastro, acesse o menu "Movimentações Bancárias / Controle Bancário / Convênio".

A visão de Convênio é capaz de exibir os registros de todas as coligadas, porém é muito importante se atentar que para utilizar a coluna "Coligada" na visão ou mesmo em um filtro o sistema precisa estar com o parâmetro Usar contabilização de mútuo marcado.

CardsDados Adicionaistrue2Identificação

Cada Convênio deverá ser associado a uma Conta/Caixa, Banco, Agência e Conta Corrente. A conta/caixa deverá ser preenchida para o convênio cadastrado e esse convênio pode ser definido como default ao marcar a flag "Convênio default para a Conta Caixa". Quando definido como default, todo lançamento inserido no sistema com determinada Conta/caixa carregará automaticamente este convênio.

3Dados Adicionais

Esses dados deverão estar preenchidos corretamente de acordo com o processo, pois são importantes na composição do arquivo de remessa, conforme especificado em cada manual fornecido pelo Banco.  
Tomemos por exemplo o processo Custódia, se no manual do Banco não exigir a Carteira, não será necessário informá-la no Cadastro, no entanto será necessário indicar o Layout do relatório de remessa na Aba "Remessa Bancária". Para todos os processos da Integração Bancária deverão ter o seu respectivo Convênio com as informações pertinentes.

**Observação**:

Na inclusão de um novo convênio na aba Dados Adicionais, o campo "Tipo de Cobrança" será selecionado como default a opção "Registrado".  
Em "Informações do cedente" é permitido informar CPF ou CNPJ.

A opção de "Tipo Nosso Número" como *Gerado pelo Banco* não deve ser utilizada em convênios, que não usam o registro online, para boletos oriundos do Educacional já que o valor proveniente do mesmo é gerado com zero.

Valor Código de Barras: Informe o valor que será utilizado para a geração do Código de Barras.

Valor Líquido

O sistema irá utilizar o valor líquido do lançamento calculado na data de vencimento do título na geração do boleto. Ou seja, os valores de juros, multa, desconto e valores opcionais estarão apenas no lançamento.

Obs: Atentar-se ao parâmetro "Contas a Receber | Integração Bancária | Integração Bancária | No retorno bancário utilizar os valores do arquivo sobrepondo os do lançamento", pois ele considera os valores(juros, multa desconto e valores opcionais) que vêm no arquivo de retorno bancário. Para este caso, sugerimos utilizar "Contas a Receber | Integração Bancária | Cobrança Eletrônica | Valor Default para diferença em retorno bancário".

Valor Original

O sistema irá utilizar o valor original do lançamento.

Valor Parcial

O sistema irá utilizar o valor parcial do lançamento, que é o mesmo cálculo do valor líquido acima mencionado, porém com uma diferença ele considera todos os valores do lançamento exceto Multa e Juros, os Valores Opcionais que Acrescentam após X dias de atraso são ignorados e os Valores Opcionais que Descontam até o vencimento também são ignorados.

Valor Zero: O sistema irá gerar o boleto com o valor zero.

Usa padrão SIACC

Essa opção trata a integração com o padrão de comunicação entre arquivos (remessa e retorno) SIACC adotado pela Caixa Econômica Federal.

Importante: para cada convênio distinto com o banco deve existir um registro no cadastrado diferente, assim, dois convênios com mesmo número de convênio, banco e agência não devem ser cadastrados. O controle se sequencial SIACC é único por convênio.

Atualizar próximo sequencial SIACC

Para utilização do padrão SIACC basta marcar a flag e para executar o processo de atualizar próximo sequencial. Para execução do processo será necessário permitir ao usuário acesso através das permissões de perfil do usuário. Esta opção estará disponível apenas para Convênios que possuem na conta/caixa, integrada ao banco Caixa Econômica Federal, que deve ser cadastrada com o código Febraban 104.

**Borderô de Pagamentos**

Fórmula Dados Bancários

Neste campo o usuário poderá cadastrar uma fórmula contendo regras específicas para a definição dados bancários que atende melhor ao lançamento financeiro a pagar na inclusão ou na vinculação ao Borderô de Pagamento. A fórmula deve retornar a referência de um dos registros do anexo "**Dados Bancários**" do cliente/fornecedor informado no lançamento.

Exemplo de fórmula:

SE (TABLAN('VALORORIGINAL', 'V') < 5000) ENTAO  
2  
SENAO  
3

Nesse exemplo quando o valor original do lançamento for menor que R$5000,00 o dado bancário de referência "2" será carregado para o lançamento, se for maior que R$5000,00 será carregado para o lançamento o dado Bancário "3".

4Remessa Bancária

Remessa de Débito Automático / Cobrança / Pagamento / PIX

É possível definir padrões defaults para gerar o arquivo de remessa, permitindo definir o caminho onde o arquivo será salvo, o nome e sua extensão.  
Código Layout: É necessário indicar o layout para cada processo. Os layouts deverão ser criados ou importados através do Menu Gestão / Gerador de Saída ou pelo Módulo de Integração.  
Diretório de Destino: Local default que será salvo o arquivo, ao ser informado o diretório de destino não será permitido alteração ao gerar a remessa.   
Nome do Arquivo: Nome default do arquivo, ao ser informado o nome do arquivo não será permitido alteração ao gerar a remessa.   
Poderá ser composto por uma parte fixa e por uma parte variável definida pelas seguintes tags:

* DDMMYYYY  | DDMM | MMYYYY - Informação da data de geração do arquivo. (Parte fixa)
* # caractere para definir o número sequencial do arquivo. (Parte variável).

Extensão: Deverá ser informado a extensão do arquivo de remessa, com opções de .txt ou .rem.

Remessa de Custódia de Cheque

Código Layout: É necessário indicar os layouts para cada processo.   
Os layouts deverão ser criados ou importados através do Menu Gestão / Gerador de Saída ou pelo Módulo de Integração.

5Cobrança Bancária

Valores Default CNAB:

Nesse aba é possível definir valores defaults utilizados no processo de inclusão de boleto para os campos:

* Espécie;
* Comando;
* Aceite;
* Instrução Cod1, Quantidade de dias Instrução1, Data Instrução1;
* Instrução Cod2, Quantidade de dias Instrução2, Data Instrução2;
* Instrução Cod3, Quantidade de dias Instrução3, Data Instrução3.

Os Valores Default CNAB sempre serão carregados para os lançamentos, independente da regra selecionada na inclusão.

Valores Default:

* Multa ao Dia
* Carência Juros
* Tipo Juros ao Dia

Os valores default são carregados para os boletos através do processo de inclusão do boleto, exceto quando utilizada a opção de "Um boleto para cada lançamento", onde serão carregados os valores do lançamento para cada boleto criado se não houve divergência nos valores dos lançamentos, ignorando os defaults do convênio. Para as outras opções, serão carregados os valores informados no default.  
  
Relatório default para impressão de boleto

Informa automaticamente o relatório a ser utilizado na impressão de boletos.  
Caso seja selecionado mais de um boleto de convênios diferentes que estejam parametrizados com relatórios diferentes, na impressão de boletos não será selecionado o relatório automaticamente.

Cancelar boleto(s) pendente(s) de remessa ao alterar valor do(s) lançamentos(s)

Este parâmetro deverá ser utilizado nos casos onde o banco não possui comando específico para realizar a atualização do valor de um determinado boleto registrado.  
Desta forma, caso seja necessário alterar o valor do lançamento, este boleto deixará de ser válido.

Com esta solução, os boletos que possuírem status "Pendente Remessa" e que seu(s) lançamento(s) tiver(em) valores modificados pelo usuário, serão cancelados caso possuam convênio com este parâmetro marcado.  
Abaixo segue os campos que se forem alterados, cancelam o boleto com status pendente remessa:  
VALORORIGINAL, VALORDESCONTO, JUROSDIA, MULTADIA, CARENCIAJUROS, VALORCAP, CAPMENSAL, CODINDEXADOR, CODMOEVALORORIGINAL, VALORJUROS, VALORMULTA,  VALOROP1, VALOROP2, VALOROP3, VALOROP4, VALOROP5, VALOROP6, VALOROP7, VALOROP8,  FORMULAJUROS, FORMULAMULTA, FORMULADESCONTO, FORMULAVALOROP1, FORMULAVALOROP2, FORMULAVALOROP3, FORMULAVALOROP4, FORMULAVALOROP5, FORMULAVALOROP6, FORMULAVALOROP7, FORMULAVALOROP8, FORMULACAPITALIZACAO, LISTAVALORESINTEGRACAOLANCAMENTO.

Para utilizar o parâmetro, acesse a aba "Cobrança Bancária", na tela de edição de convênios e marque a opção "Cancelar boleto(s) pendente(s) de remessa ao alterar valor(es) do(s) lançamentos(s).

6Registro online

Na aba 'Registro online' do cadastro do Convênio existem os campos relacionados ao uso do registro online dos boletos. A opção "Permite registro de boleto online" será habilitada somente quando a opção "Registrada" é definida no Tipo de Cobrança (aba 'Dados adicionais' do convênio). Logo, ao habilitar esta opção os campos pertinentes aos dados do registro como as URLs do serviço de registro, certificado digital (para os bancos que utilizam), etc ficarão disponíveis para preenchimento. Esses campos deverão ser preenchidos conforme os dados disponibilizados por cada banco. Para mais destalhes a respeito dos campos exibidos nesta aba, consulte a documentação específica de cada banco na página do processo de [Registro online de Boletos](https://tdn.totvs.com/display/LRM/Registro+Online+de+Boletos).

7Conta Transitória

Na emissão de boletos, o sistema irá buscar os dados para composição do nosso número/código de barras da conta transitória (conta de cobrança), presente no convênio. A baixa ou retorno deste boleto continuará utilizando a conta normal do convênio (conta movimento).

Exemplo:  
Algumas empresas por exemplo do ramo de construção/incorporação, iniciam o empreendimento e conseguem empréstimos/financiamentos junto aos bancos e os recursos destes empréstimos são liberados de acordo com o recebimento da carteira de cobrança deste empreendimento. Com a separação em conta de cobrança, os bancos conseguem separar a movimentação, identificando os valores para que seja realizado o controle dos seus processos internos vinculados ao financiamento.

Utilização:  
Para utilizar a funcionalidade de Conta Transitória, basta acessar a aba "Conta Transitória" no cadastro de convênio.  
Os campos que devem ser preenchidos neste cadastro, são:

* Agência de cobrança;
* Conta corrente para cobrança;
* Dígito da AG/Conta de cobrança.

Além deste cadastro, não é necessário alterar nenhum outro parâmetro no sistema.  
Após salvar este convênio com as informações acima, o sistema já estará pronto para gerar nosso número e código de barras utilizando as informações da conta transitória.

**Observações:**

Para um convênio onde a conta transitória for utilizada, ao gerar o nosso número e o código de barras, os dados utilizados serão sempre os da respectiva conta transitória cadastrada.

Não será possível alterar a conta transitória cadastrada num convênio, sendo necessário cadastrar um novo, caso as informações da conta transitória não sejam mais utilizadas.

Para o banco ITAÚ, nas carteiras 198, 107, 012, 142, 143, 195, 196, 198, 107, 122, 142, 143 e 196, o campo livre será calculado da seguinte maneira: carteira, nosso número, número documento e código cedente.

Para outras carteiras, o cálculo do campo livre utilizará: carteira, nosso número, agência, conta e DV + 3 zeros a direita;

O DV utiliza a agência e conta da conta transitória cadastrada no convênio.

Outros bancos possuem regras diferentes.

 Veja Também

true
