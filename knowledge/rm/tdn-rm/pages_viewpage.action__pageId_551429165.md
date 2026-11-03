---
content_hash: bceb96f2858564f00a092609939807272019925c3f7b651718a39ea293e77d30
fetched_at: '2026-06-29T00:10:43.916447+00:00'
page_id: '551429165'
product: rm
source: tdn-rm
title: 1.2.2 Convênio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=551429165
version: 16
---

O cadastro de Convênios unifica toda a regra dos processos da Integração Bancária, assim como Carteira, Tipo de Cobrança, Registro Online, PIX, entre outros. É muito importante que esses dados sejam validados antes de iniciar o processo e que estejam em conformidade com o manual fornecido pelo Banco, pois assim que houver boleto gerado para lançamentos associados ao Convênio, por segurança e integridade dos dados, nenhuma alteração será permitida no cadastro.

Para gerar Boletos é necessário que exista o Convênio cadastrado.

Após cadastrar a Conta Caixa, importante cadastrar os dados do Convênio. Para isso, acesse: *Anexos | Convênios.*

O cadastro também poderá ser feito pelo menu: Movimentações *Bancárias | Controle Bancário | Convênio*

Incluir um novo Convênio. Clique em "Incluir" acessando o cadastro de convênio, ou acessando pela visão anexos conta/caixa.

ConvêniosIdentificação

**Identificação**

Preencher os dados do convênio, conforme cada contrato com o Banco.

**Convênio:** Informar o número do convênio firmado com o banco;  
**DV:** (Digito do Convênio) Informar digito caso exista;  
**Nome:** Informar o nome do convênio (inserir conforme desejado);  
**Conta/Caixa:** Informação default;  
**Marcar:**

* Ativo
* Convênio default para a Conta Caixa

**Informações bancárias:** Os campos Banco, Agência e Conta, serão carregados automaticamente ao informar uma conta/caixa que possui esses dados associados

Dados Adicionais

**Dados Adicionais**

Esses dados deverão estar preenchidos corretamente de acordo com o processo, pois são importantes na composição do arquivo de remessa, conforme especificado em cada manual fornecido pelo Banco.

Os campos ***Carteira, Tipo Careira, Tipo de Conta, Código cedente, DV, CNPJ/CPF*e*Cedente*** deverão estar preenchidos conforme os dados encaminhados pelo Banco.

**Marcar:**

* **Tipo Nosso Número:** Referência do Boleto
* **Valor código de Barras:** Liquido (Parcial, se o Regional utilizar Registro Online)

**Valor Líquido:** O sistema irá utilizar o valor líquido do lançamento calculado na data de vencimento do título;  
**Valor Original:** O sistema irá utilizar o valor original do lançamento;  
**Valor Parcial:** O sistema irá utilizar o valor parcial do lançamento, que é o mesmo cálculo do valor líquido acima mencionado, porém com uma diferença ele considera todos os valores do lançamento exceto Multa e Juros, os Valores Opcionais que Acrescentam após X dias de atraso são ignorados e os Valores Opcionais que Descontam até o vencimento também são ignorados;  
**Valor Zero:** O sistema irá gerar o boleto com o valor zero.

Estas opções podem mudar de acordo com cada DR.

Remessa Bancária

**Remessa Bancária:**

É possível definir padrões defaults para gerar o arquivo de remessa, permitindo definir o caminho onde o arquivo será salvo, o nome e sua extensão.

* **Código Layout**: É necessário indicar o layout para cada processo. Os layouts deverão ser criados ou importados através do Menu Gestão / Gerador de Saída ou pelo Módulo de Integração.
* **Diretório de Destino**: Local default que será salvo o arquivo, ao ser informado o diretório de destino não será permitido alteração ao gerar a remessa.
* **Nome do Arquivo**: Nome default do arquivo, ao ser informado o nome do arquivo não será permitido alteração ao gerar a remessa. Poderá ser composto por uma parte fixa e por uma parte variável definida pelas seguintes tags: DDMMYYYY | DDMM | MMYYYY - Informação da data de geração do arquivo. (Parte fixa) # caractere para definir o número sequencial do arquivo. (Parte variável).
* **Extensão:** Deverá ser informado a extensão do arquivo de remessa, com opções de .txt ou .rem.
Cobrança Bancária

**Cobrança Bancária**

Informações nesta etapa preenchidos conforme necessidade.

* **Valores Default CNAB:** Preencher os campos com os dados fornecidos pelo banco, sendo que serão utilizados como default para processos futuros com esse convênio.
* **Valores Default:** Preencher conforme a necessidade para que tais campos sejam carregados conforme o conteúdo dos respectivos campos.
* **Relatório default para impressão de boleto:** Informa automaticamente o relatório a ser utilizado na impressão de boletos. Caso seja selecionado mais de um boleto de convênios distintos que estejam parametrizados com relatórios diferentes, na impressão de boletos não será selecionado o relatório automaticamente.
Registro Online

**Registro Online**

A opção "Permite registro de boleto online" só será habilitado para convênios registrados. Marcando a opção, é necessário informar URL do serviço de registro de boleto e URL de retorno do serviço de registro de boleto.  Serão preenchidos conforme necessidade e de acordo com cada Banco e sua particularidade

* Para cada banco serão exibidos campos específicos (de acordo com o manual bancário);
* O código FEBRABAN no cadastro do Banco deve ser informado corretamente, para que os campos do sistema de cobrança possam ser exibidos no convênio de acordo com o banco relacionado.

Exemplo: Caixa Econômica Federal:

* URL do serviço de registro de cobrança

Exemplo: Banco do Brasil:

Campos do sistema de cobrança Banco do Brasil:

* URL do serviço de registro de cobrança
* URL de homologação do serviço de registro de cobrança
* URL do sistema autorizador
* URL de homologação do sistema autorizador
* Client ID
* Client Secret
Anexos

* [Associação do Layout do Registro Online](https://tdn.totvs.com/pages/viewpage.action?pageId=421388759)
Veja Também

* [FIN - Convênio](https://tdn.totvs.com/pages/viewpage.action?pageId=421388845)
* [Cross Segmentos - Backoffice Linha RM - FIN - Como cadastrar Convênio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042156493-Cross-Segmentos-Backoffice-Linha-RM-FIN-Como-cadastrar-Conv%C3%AAnio)
