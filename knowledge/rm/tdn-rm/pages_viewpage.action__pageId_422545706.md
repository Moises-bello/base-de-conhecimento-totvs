---
content_hash: 9cd4b0685d3dc2e20803b93494adc2a04b0bab8615f31375b878005e5e93c6f3
fetched_at: '2026-06-29T00:09:20.556065+00:00'
page_id: '422545706'
product: rm
source: tdn-rm
title: FCI - Ficha de Conteúdo de Importação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545706
version: 15
---

## Conteúdo

Conteúdo

## **01. Visão Geral**

Através do [Ajuste SINIEF nº 19/2012](https://www.confaz.fazenda.gov.br/legislacao/ajustes/2012/AJ_019_12), foi instituída a "Ficha de Conteúdo de Importação" (FCI), visando prestar informações sobre o conteúdo de Importação à Administração Tributária sobre a participação da parcela importada no total do bem ou mercadoria, além de identificar o contribuinte e a própria mercadoria.  
Os contribuintes deverão prestar informações sobre o Conteúdo de Importação de seus produtos através de arquivo digital a ser encaminhado à Administração Tributária.

## **02. Requisitos**

requisitosCadastro do Produto

Para a correta geração do arquivo, deverão ser informados nos anexos do *[Produto](http://tdn.totvs.com/pages/viewpage.action?pageId=423938817) > FCI's do Produto* os seguintes os campos:

* Unidade de medida
* Valor da Parcela importada no Exterior
* Valor da saída interestadual
* Conteúdo de Importação

FCI's do ProdutoObservação

Após a segunda fase de Implementação da Rotina, os campos acima serão calculados automaticamente.  
Após a importação da FCI, o campo Número da FCI Gerada será preenchido automaticamente.

Parametrização do Processo

No TOTVS Gestão Fiscal, acesse *Cadastros > Parâmetros de Processos.*Faça o cadastro de um novo processo especificando **FCI - Ficha de Conteúdo de Importação** no campo **Processo.**

Parâmetros de Processo FCI

Neste processo, devem ser informados os produtos submetidos ao processo de industrialização (que serão utilizados nos movimento de Venda).  
Para cadastrar os produtos, acesse o menu *Anexos > Filtro Produto*.

Filtro Produto

Além disso, o usuário poderá informar quais itens são passíveis de recálculo (quando o cálculo for otimizado) e alíquota do ICMS praticada.

Cálculo Conteúdo de Importação

Para realizar o cálculo, acesse o Cadastro do Produto > Processos > Cálculo Ficha de conteúdo importação e informe os seguintes campos:

* **Filial:** código da filial
* **Fórmula VI e VO:** fórmula de VI (Valor da Parcela Importada do Exterior) e VO (Valor Total da Operação de Saída Interestadual)
* **Data último período de apuração**;
* **Meses pesquisa CI:** quantidade de meses que serão pesquisados os movimentos.

Cálculo Ficha de conteúdo importação

## **03. Estrutura do Arquivo**

O arquivo da FCI gerado pelo TOTVS Gestão Fiscal é composto por três blocos, sendo eles:

BlocosBloco 0

**Bloco 0 -**Informações de abertura e Identificação do Contribuinte.

RegistrosBloco0leftRegistro 0000

**Registro 0000**– Abertura do arquivo digital  
São gravadas neste registro informações da filial do estabelecimento e informações digitadas na tela de geração da rotina.

Registro 0001

**Registro 0001**– Abertura do bloco 0  
Este registro informa o texto padrão em caracteres. Tem o objetivo de certificar que os demais dados relacionados nos registros subsequentes poderão ser lidos sem divergências ou erros de acentuação/língua. O padrão UTF-8 é bastante difundido entre os editores de texto ou produtores de conteúdo.

Registro 0010

**Registro 0010**– Informações do Estabelecimento/Contribuinte informante  
São gravadas as informações da Filial como: CNPJ, Razão social, endereço etc.

Registro 0990

**Registro 0990**- Finalização do Bloco 0  
Neste registro são informados a quantidade de linhas do Bloco 0.

Bloco 5

**Bloco 5 -** Informações referentes a dados da Mercadoria, dados de identificação do bem ou mercadoria e do percentual do Conteúdo de Importação.

Bloco 5leftRegistro 5001

**Registro 5001** – Abertura do Bloco  
O início do bloco, utilizado o campo fixo 5001

Registro 5020

**Registro 5020** – Informações de Bens/Mercadorias  
São gravadas as informações dos bens e mercadorias que participaram do processo de Importação. Será um registro para cada Bem/mercadoria.  
Neste registro serão usadas as informações do anexo do Cadastro do Produto - FCI's dos Produtos.

Registro 5990

**Registro 5990** - Finalização do Bloco 5  
São informadas a quantidade de registro do Bloco 5

Bloco 9

**Bloco 9 -** Informaçõesreferentes a totalização dos registros anteriores.

Bloco 9leftRegistro 9001

**Registro 9001**- Abertura do Bloco 9  
Abertura do bloco 9.

Registro 9900

**Registro 9900**- Totalizadores de Registros anteriores  
Esse registro traz a contagem de registros "0000", "0010" e "5020".

Registro 9990

**Registro 9990** - Encerramento do Bloco 9  
Esse registro traz a contagem de registros do bloco 9.

Registro 9999

**Registro 9990**- Encerramento do arquivo  
Nesse registro a contagem considera inclusive o registro 9999 na quantidade de linhas.

## **04. Geração da Rotina**

Para gerar a FCI, acesse o menu Obrigações Acessórias > Federais > FCI. Ao expandir este menu, serão exibidas duas opções: Exportação e Importação.

Menu FCI

### **04.01 Exportação**

A exportação faz a geração do arquivo a ser importado no validador da FCI através do gerador de saídas. O layout da FCI está disponível através do TOTVS Compartilhamento sob o nome "**FISLAY0013 - FCI.TotvsGen**"

Geração Arquivo FCI

Informe o layout da FCI na tela de Exportação e preencha os campos:

* **Coligada:** Informar a coligada para a qual deseja gerar a Rotina
* **Filial:** Informar a Filial
* **Versão:** Versão de leiaute do arquivo, informação disponível no manual do usuário que a SEFAZ disponibiliza.
* **Personalizar Código do Produto:** Selecionar qual o Código do produto será utilizado na geração do arquivo\Opções Código - Identificador(IDPRD) – Código Reduzido – Código Auxiliar todos estes campos estão disponível no Cadastro do Produto.
* **Selecionar Produtos com Conteúdo de Importação Menor ou Igual a 40%:** Com este ícone habilitado ao gerar a Rotina será selecionado o Produto que tem o Conteúdo de Importação <=40%.  
  Após preencher as informações necessárias para gerar a Rotina – Clicar em Avança e Executar. Após gerar aparece a tela abaixo, deve ser verificado se ocorreu erro em algum Registro ou Processo.

### **04.02 Importação**

Nesta opção, é possível importar o arquivo texto de retorno enviado pela SEFAZ com os números das FCIs geradas pela SEFAZ. Assim, os números da FCI dos produtos constantes no arquivo serão gravados no Cadastro do *Produto > Anexo FCIs do Produto > Campo**Número**FCI*.

Importação Arquivo FCI

## **05. Outras Informações**

Para que o número da FCI seja apresentado nas informações adicionais da NF-e, será necessário a criação de uma [Fórmula Visual](http://tdn.totvs.com/pages/viewpage.action?pageId=403746948) que retorne o valor do campo do cadastro do Produto. Desta forma, ao salvar o movimento que contenha os produtos informados na FCI, o campo será preenchido.
