---
content_hash: 81c154732e872623cda67ad986cd76b8ffbb6f7419df474affc2849ca0081164
fetched_at: '2026-06-29T00:09:23.951972+00:00'
page_id: '422546169'
product: rm
source: tdn-rm
title: Parametrização do TOTVS Gestão de Estoque, Compras e Faturamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422546169
version: 8
---

1 - **Cadastros**

**Classificação de Municípios**

A NF-e utiliza a classificação de Municípios do IBGE. Para realizar essa inclusão/alteração acesse: **Cadastros | Tabelas Auxiliares | Município**, em **Anexos,** clique em **Codificação de Município.** Selecione a classificação IBGE e informe o código do município.

**Classificação de Países**

A NF-e utiliza a classificação de Países definida pelo BACEN. Para realizar a inclusão/alteração da codificação acesse: **Cadastro | Países**, em **Anexos**, clique em **Codificação de País**. Selecione a classificação BACEN e informe o código do País.

**Cadastro de Filiais**

Para incluir/alterar uma filial acesse: **Cadastro | Filiais**. Neste cadastro são informados todos os dados do emitente da NF-e.Todos os campos devem ser preenchidos com conteúdo válido. A inscrição SUFRAMA só deverá ser fornecida se o contribuinte possuir uma inscrição no estado de Manaus. Nos campos onde é informado o nome e endereço não deve conter caracteres especiais, como por exemplo (), "!@#$"&\*

**Cadastro de Produtos**  
No cadastro de produtos os campos a serem preenchidos devem seguir as mesma orientações do informada nas documentações do TOTVS Gestão de Estoque, Compras e Faturamento. Mas deve-se atentar aos seguintes campos estão preenchidos:  
Nomenclatura Comum do Mercosul; Procedência; Unidades; Números de série;   
Os **anexos | Dados Fiscais por UF**, deve ser incluídos de acordo com as filiais emissoras de NF-e. Por exemplo: Se tiver uma filial no Rio de Janeiro e outra em Belo Horizonte que emitem NF-e você deverá criar um registro para RJ e outro para MG. É necessário informar a modalidade da determinação da base de cálculo do ICMS e do ICMS-ST, essas informações são utilizadas para identificar como sua base de cálculo foi montada.  
Os valores aceitos nestes campos são:

* ICMS

0 – Margem Valor Agregado (%)  
1 – Pauta (Valor)  
2 – Preço tabela Máximo (Valor)  
3 – Valor da Operação

* ICMS ST

0 – Preço tabelado ou máximo sugerido  
1 – Lista Negativa (valor)  
2 – Lista Positiva (Valor)  
3 – Lista Neutra (Valor)  
4 – Margem Valor Agregado  
5 – Pauta (Valor)

Outra informação importante é o **Preço sugerido ao consumidor.** Esta informação deverá ser preenchida quando se tratar de medicamentos. A informação do lote poderá ser gravada também no lote do produto. Bastando para isso acessar o anexo Lote do produto no cadastro de produtos. Ao gerar a NF-e a informação é procurada primeiro nos dados fiscais por UF do produto. Se ela não estiver lá será gravada a do lote.  
Em **Anexo | Dados Fiscais do Produto**, os campos Situação Tributária PIS e COFINS devem ser informados, mesmo que a empresa seja isenta. Valores aceitos:

01 – Operação Tributável (base de cálculo = valor da operação alíquota normal  (cumulativo/não cumulativo));  
02 - Operação Tributável (base de cálculo = valor da operação (alíquota diferenciada);  
03 - Operação Tributável (base de cálculo = quantidade vendida x alíquota por unidade de produto);  
04 - Operação Tributável (tributação monofásica (alíquota zero));  
05 - Operação Tributável (substituição tributária);  
06 - Operação Tributável (alíquota zero);  
07 - Operação Isenta da Contribuição;  
08 - Operação Sem Incidência da Contribuição;  
09 - Operação com Suspensão da Contribuição;  
99 - Outras Operações;

De acordo com o ramo de atividade da empresa os seguintes campos deve ser preenchidos:  
**Classe Enquadramento IPI e Código Selo de Controle IPI:** Devem ser informados no caso de bebidas e cigarros. Deve ser utilizada a codificação prevista nos atos normativos editados pela Receita Federa.  
**Código ANP:** Deve ser informado quando se tratar de produtos regulados pela Agência Nacional do Petróleo.  
**Código CODIF:** Deve ser informado no caso de derivados de petróleo. Informar apenas quando a UF utilizar CODIF (Sistema de Controle do Diferimento do Imposto nas Operações  com AEAC – Álcool Etílico Anidro.

**Tipo de Documento**

É importante que o usuário não altere os tipos de documento já existente e sim inclua um novo para a NF-e. O campo Código do Modelo do Documento deverá ser preenchido com o valor 55 que é o código utilizado para a NF-e.

**Veículos**

Registro na ANTT - Este campo deverá receber o número do Registro Nacional de Transportador de Carga (ANTT) dos veículos que efetuam o transporte de mercadoria.   
Atenção: Cadastre a placa do veículo com letras maiúsculas e sem o separador hífen  entre as letras e o número. Exemplo: HMN2200.

**Veículos Novos**

Através desta opção o sistema irá gerar a Tag de Veículos Novos no XML da NFE   
Somente serão selecionados movimentos que atenderem às seguintes restrições:

1) O produto deverá ser controlado por número de série e ter NCM iniciado com 8703 .  
2) O número de série deve ser informado no movimento e o mesmo deve ter os campos complementares devidamente preenchidos.

Para a montagem da TAG (J) no XML o sistema irá tratar os campos complementares do produto, número de série e tipo de movimento, cujo nome deve ser cadastrado igual ao conteúdo da coluna CAMPO da TAG (J) Detalhamento Específico de Veículos Novos(vide detalhes no Manual de Integração Contribuinte a ser acessado no Portal Nacional da NF-e):

**Criação dos campos complementares**

Todos os campos complementares criados deverão ser do tipo alfanumérico e o tamanho deverá obedecer ao previsto no Manual de Integração Contribuinte a ser acessado no Portal Nacional da NF-e.

|  |  |  |
| --- | --- | --- |
| **Nome da Coluna Vinculada** | **Descrição** | **Tabela de Campo Complementar** |
| TPOP | Tipo da Operação | Movimento |
| Chassi | Chassi do Veículo | Número de Série |
| XCOR | Descrição da Cor | Produto |
| POT | Potência | Produto |
| CM3 | CM3 (Potência) | Produto |
| TPCOMB | Tipo de Combustível | Produto |
| NMOTOR | Número de Motor | Número de série |
| CMKG | CMKG | Número de série |
| DIST | Distância entre eixos | Produto |
| RENAVAM | RENAVAM | Número de série |
| ANOMOD | Ano Modelo Fabricação | Número de série |
| ANOFAB | Ano de Fabricação | Número de série |
| TPPINT | Tipo de Pintura | Produto |
| TPVEIC | Tipo de Veículo | Produto |
| ESPVEIC | Espécie de Veículo | Produto |
| VIN | Condição do Vin | Número de série |
| CONDVEIC | Condição do Veículo | Produto |
| CMOD | Código Marca Modelo | Produto |
| \*CILIN | Cilindradas | Produto |
| \*CMT | Capacidade Máxima de Tração | Número de série |
| \*CORDENATRAN | Código da Cor | Produto |
| \*LOTA | Capacidade máxima de lotação | Produto |
| \*TPREST | Restrição | Número de série |
| \*MOTDESICMS | Motivo da desoneração do ICMS | Movimento |

**Layout NFe 2.0**

Para os campos cCor, pesoL e pesoB deverão ser usados, respectivamente, os seguintes campos já existentes no cadastro de produto: Cor, Peso Líquido e Peso Bruto na aba Característica do cadastro de produto. O campo nSerie será preenchido com o número de série selecionado para o item de movimento.

***Atenção!***Poderá ser informado no XML da NFE no máximo um registro de veículo novo. Desta forma somente um único número de série pode estar selecionado no item de movimento.

**NF-e Referenciada**

Quando for realizado a transmissão de uma NF-e de devolução de produtos deve-se ser gerado um movimento de cópia por referência.   
Para produtores rurais o movimento de entrada deve ter o CODMODOC igual a 01 ou 04 e o ramo de atividade no cadastro de cliente/fornecedor marcado como produto rural.  
Para cupom fiscal deve gerar um cópia por referência do movimento do cupom fiscal em um tipo de movimento parametrizado para NF-e.

**Envio de Email**  
A configuração do envio de email é necessária de acordo com a empresa, pois o sistema disponibiliza o recurso de enviar o arquivo XML da NF-e por email para os respectivos clientes.  
Estes parâmetros deverão ser preenchidos de acordo com as necessidades do servidor de email da empresa. Parâmetros Globais, pasta Envio de Emails.

**Filial**

Verifique se estão preenchidas corretamente as informações de CNPJ, Inscrição Estadual, Código do Município, NIRE, data no registro de empresas e endereço (Rua, Número, CEP, Bairro, Cidade e UF). Em caso de enviar um desses campos com informações incoerentes, a NF-e poderá ser rejeitada pela SEFAZ.  
Para realizar emissão de NF-e na versão 2.0 deve-se informar no parâmetro versão do layout da NF-e utilizado o valor 2.00. Essa parametrização é informada na integração fiscal no módulo Gestão de Compras e Estoque em parâmetros por filial.

**Cliente / Fornecedor**

Verifique se todos os clientes/fornecedores válidos possuem preenchidos corretamente os campos: CNPJ/CPF, Inscrição Estadual, Código do Município e endereço (Rua, Número, CEP, bairro, cidade e UF). Em caso de enviar um desses campos com informações incoerentes, a NF-e poderá ser recusada pela SEFAZ   
Para o envio do e-mail do XML para o cliente, será necessário preencher o e-mail e o contato principal do cadastro.

2 - **Movimento**

**Movimento**

Para o correto envio da NF-e deve preencher os seguintes campos no Movimento:

**Identificação do Movimento**

* Cliente/Fornecedor – o cadastro deve estar completo
* Série – deve ser numérica
* Natureza – deverá ser previamente parametrizada com a correta situação tributária do ICMS  e do IPI de acordo com a operação realizada.

***Atenção!*** Se o campo Tipo de ICMS SEM Valor no cadastro da natureza estiver desmarcado ou nulo o Gestão Fiscal define que o valor do item (tag vProd) está compondo o valor da NF-e (tag indTot igual a 1), caso contrário o valor do item não compõem o valor da NF-e (tag indTot igual a 0).  
Para realizar esse tipo de validação deve-se criar uma formula (criar link para help de formulas) para o Tipo de Movimento consistir essa regra.

**Item do Movimento**

Produto – previamente parametrizado   
Unidade – a unidade de controle deve possuir um valor valido de acordo com o manual do contribuinte e não deve possuir assentos ou qualquer sinal gráfico em sua descrição e código. Exemplo: Para Peça, grave PC e não PÇ.  
Quantidade e Preço – devem estar preenchidos  
Natureza – deve ser preenchida

**Tributos do Item**

Para os tributos ICMS, IPI e ICMSST (quando existir) devem ter os campos Base de Calculo, Alíquota e Valor preenchidos de acordo com a CST da Natureza de Operação (Para maiores informações consultar o manual do contribuinte)

* Situação Tributária – Este valor será preenchido automaticamente se for gravado no default do tipo de movimento. Somente para o PIS e COFINS. A situação tributária do IPI é gerada internamente de acordo com o tipo de IPI definido no cadastro da natureza.
* Modalidade Base de Calculo – Carregado do anexo Dados Fiscais por UF no cadastro do produto. Somente para o ICMS e ICMSST.

Seleção de Tributos Retidos

Para selecionar os tributos retidos, o sistema irá verificar primeira se os mesmos foram informados nos tributos do ITEM. Na ausência dos tributos no item, o sistema irá verificar os tributos retidos do MOVIMENTO.

É obrigatório que na tributação do Item seja incluído o tributo ICMS e o ICMS-ST onde deve ser informando somente a base de calculo do ICMS com sua alíquota e valor com **valores igual a 0**, conforme legislação vigente da NF-e.  
Ao realizar esse processo, será incluído na tag de Informações Complementares de interesse do Contribuinte (infCpl) as informações referentes ao ICMS 60. Conforme exemplo abaixo:  
<infCpl>  
Informacoes da saida ST 60 (Produto - Base ICMS ST - Valor ICMS ST) : 02.04- 520 - 62,40|02.05- 3900 -  468|02.06- 260 - 31,20|  
</infCpl>  
***Observação:***Não existe vinculo entre os Movimentos e não é realizado o controle de estoque por Substituição Tributária.

Código município / país

* [C](https://www.bcb.gov.br/pt-br/#!/home)[odificação de País](https://www.bcb.gov.br/pt-br/#!/home)
* [Codificação de Município](https://www.ibge.gov.br/geociencias-novoportal/organizacao-do-territorio/estrutura-territorial/15761-areas-dos-municipios.html?=&t=sobre)
