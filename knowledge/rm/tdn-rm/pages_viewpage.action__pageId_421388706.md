---
content_hash: 4cfa9cd85f69b87d3672e1d3f8d11b545b9df66c6535be55b829e9353b4b256f
fetched_at: '2026-06-29T00:09:18.486473+00:00'
page_id: '421388706'
product: rm
source: tdn-rm
title: FIN - Retorno Pagamento Eletrônico 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388706
version: 20
---

A importação de arquivos de retorno é um processo, que consiste em baixar automaticamente ou atualizar os Lançamentos Financeiros por meio de  importação de arquivos disponibilizados pela rede Bancária. Em se tratando de Cobrança Eletrônica, Pagamento Eletrônico e Débito Automático, a baixa será realizada automaticamente desde que o arquivo de retorno contenha dados requeridos, assim como data de crédito, valor do crédito, motivo de ocorrência específica para baixas ou quitações,  entre outras informações afins. Alguns arquivos de retorno apenas reportam atualizações para o lançamento financeiro, provenientes de transações entre a empresa e o Banco. Um exemplo dessa transação é o arquivo de retorno que o Banco disponibiliza à empresa informando do processamento dos títulos. Ao importar esse arquivo a única alteração a ser feita é a atualização do STATUS.CNAB do Lançamento para "Registrado" , "Recusado" ou outros e não produzirá baixas.

**Retorno de Pagamento**

Retorno de Pagamento

Esta opção deverá ser utilizada na importação de retorno de Pagamento de arquivos fornecidos por todos os Bancos que adotarem o padrão CNAB240 com adequações próprias e aos demais arquivos de formatos e tamanhos diversificados.

Retorno de Pagamento *– Padrão Febraban (CNAB240)*

Esta opção deverá ser utilizada para importação de arquivos de retorno "no padrão" CNAB 240 da FEBRABAN, sem nenhuma adequação.  
   
Padrão SIACC CEF – Esta opção estará disponível no retorno de pagamentos (opção CNAB240) quando o código do banco selecionado for o 104.  
   
**Observação:**

Se no arquivo de retorno houver alguma informação em posições diferente do padrão, exemplo, valor na posição 70 a 84, você deverá optar pelo tipo de retorno "Retorno de Pagamento" e não pela opção "Retorno de Pagamento CNAB240", mesmo que o arquivo de retorno tenha 240 colunas.

**Dados da Importação**

É necessário informar o Local onde está o arquivo de retorno, o Código da Filial, a Conta Caixa (o Banco, que deverá ser o Banco que gerou o arquivo, será preenchido automaticamente). Informe também o Evento Contábil para a contabilização da baixa ou poderá utilizar o evento parametrizado para o processo de Baixa. Indique também o Histórico para os registros do extrato, e se não for  indicado será utilizado e "Histórico default da Baixa a Pagar" parametrizado pelo Assistente de Implantação de processos, etapa 02.01 Contas a Pagar / Baixas a Pagar.

**Parâmetros da Importação**

Quando o valor Baixado for diferente do valor líquido, considerar a diferença valores indicados: Esta comparação é feita entre o valor liquido do Lançamento Financeiro com o valor pago informado no arquivo de retorno. É necessário indicar o campo do sistema que receberá tais informações.

Utilizar Conta/Caixa do Lançamento:

A baixa será realizada utilizando a conta caixa do lançamento ao invés de usar a conta caixa informada no momento da importação do retorno.

Gerar um extrato para todos os lançamentos

Com essa opção ativa, será gerado apenas um extrato de caixa pelo valor total dos lançamentos pagos pelo banco. O processo será executado dentro de uma única transação, sendo assim, se ocorrer um erro na baixa de algum dos lançamentos selecionados, o processo será interrompido e nenhum lançamento será baixado.

Com a opção desmarcada, a contabilização da baixa dos lançamentos que possuem  o Tipo Contábil igual a  "Contábil" ou "Baixa Contábil" será realizada simultaneamente, o que poderá tornar o processo mais lento em função do volume de dados e da complexidade dos Eventos contábeis. Com a opção marcada, o processo de baixa é realizado sem a exigência das informações contábeis, que poderão ser incluídas posteriormente.

**Padrão:  Office Bank Bradesco**

O Bradesco dispõe de Software específico para o pagamento de tributos e este Software exporta os dados, que poderão ser importados no Gestão Financeira, já produzindo baixas dos títulos. Os tributos poderão ser digitados neste software ou poderão ser exportados do Gestão Financeira a partir de relatórios de saída nos padrões do Bradesco: com 463 colunas ou o denominado estendido, com 664 posições.

A utilização deste software é opcional e o pagamento de tributos poderá ser realizado também a partir de remessa eletrônica dos lançamentos financeiros do Gestão Financeira para o Banco, no formato Bradesco CNAB240.  
No retorno de pagamento do Office Banking do Bradesco a chave do lançamento deverá ser definida com 20 caracteres, tanto no layout padrão quanto no estendido. As 3 primeiras posições são referentes ao código da coligada e os outros 17 campos são referentes ao ID do Lançamento.

**DICAS**

O arquivo a ser importado deve possuir  características que definem o processo "retorno". É comum obtermos essa informação analisando o motivo ou código de ocorrência (esse termo varia entre Bancos) indicado no mesmo.

Quando o parâmetro "Lançamentos de Tributos serão Faturados pelo RM Liber" estiver marcado, não será possível realizar Retorno de Pagamento utilizando lançamentos financeiros de Tributos a Pagar. Estes lançamentos são identificados pelas Classificações: 6 (IRRF/PJ), 7 (IRRF/PF), 13 (IRRF gerado pelo Gestão Folha de Pagamento), 18 (CSLL/RF), 19 (PIS/RF), 20 (COFINS/RF), 21 (Tributos Agrupados). Se o parâmetro estiver marcado, os lançamentos com essas classificações não poderão ser baixados nem por retorno, nem manualmente. Eles deverão ser faturados pelo Gestão Fiscal( RM Liber - geração de Guias) para depois serem baixados.

No retorno bancário de pagamento, quando ocorrer devolução de um título que já se encontra baixado, o sistema irá cancelar a baixa do Lançamento e alterar o STATUS CNAB do mesmo para "Não remetido".  Estas atualizações serão realizadas se no arquivo de retorno, o "Status do Pagamento"  for igual a R (Citibank)  ou o motivo da ocorrência for igual a DV para os demais Bancos.

A importação do arquivo de retorno para o pagamento eletrônico está disponível para os seguintes Bancos:

* BANESPA
* BANESTADO
* BANESTES\*
* BankBoston
* BCN
* BNB
* BRADESCO
* Citibank
* HSBC / Bamerindus
* ITAU
* OBB Bradesco (Office Banking Bradesco)\*
* Real
* Rural
* Safra
* Unibanco
* Crefisa

E para os Bancos que utilizam o Padrão FEBRABAN CNAB240, sem nenhuma adaptação.

* **Observações**  
  Diferentemente dos demais processos da Integração Bancária, a importação do arquivo de retorno de pagamento eletrônico tem o processamento interno gerenciado pelo Sistema e não disponibiliza nos Anexos do cadastro de Bancos/Layout Bancário, o recurso para se indicar as posições que cada informação ocupa no arquivo de retorno. Por padrão, a chave de identificação do lançamento financeiro para o processamento do registro/liquidação (baixa) é composta pelo seguinte formato: CCCLLLLLLLLLLLLLLLLL, sendo 'C' o código da coligada (3 posições) + 'L', sendo a referência do lançamento.

**Importante**: No caso de coligada com mais de 3 dígitos ('1000', por exemplo), à partir dos patchs 12.1.2506.203 e 12.1.2510.134, liberamos uma melhoria no retorno de pagamento que funciona da seguinte forma nas posições destinadas ao número do documento atribuído pela empresa:

| Identificador da Chave | Tamanho | Descrição |
| --- | --- | --- |
| X | 1 | Valor fixo. Indica que o lançamento utiliza o novo modelo de chave. Serve como critério para diferenciação do formato antigo (3 posições para a coligada). |
| CCCCC | 5 | Código da coligada com preenchimento à esquerda com zeros, suportando até 99.999 coligadas. |
| LLLLLLLLLLLLLL | Variável | Identificador do lançamento (IDLAN) com quantidade de dígitos variável conforme descrito pelo manual bancário. |

**\*Banestes**

* A data de baixa dos lançamentos de acordo com o manual do banco Banestes se refere a "data de agendamento" informado no arquivo de retorno nas posições 371 a 378 para a operação 17 - Transação diversas.

**\*OBB ( Office Banking Bradesco)**

Para facilitação da correta identificação do tipo de tributo no retorno de pagamentos eletrônicos de tributos de lançamentos a pagar do Office Banking Bradesco, passamos a definir uma chave de identificação do tipo de tributo a partir das versões 12.1.29, 12.1.31. Esta chave deve ser enviada no arquivo de remessa de pagamento no campo "Uso da Empresa", e será devolvida no mesmo campo no arquivo de retorno de pagamento.

O padrão adotado para este código é iniciado SEMPRE por um asterisco <\*>, seguido por uma série de atributos, delimitados por asteriscos <\*>:

* Coligada do Lançamento
* Identificador do Lançamento
* Tipo do Tributo (conforme cada layout OBB)
* Complementado com zeros à direita

Como exemplo, um lançamento da coligada 1, com identificador 1234, de tipo DARF (tipo de tributo 1), o campo "Uso da Empresa" poderá ser formatado da seguinte forma:

\*001\*001234\*1\*000000000000000000000000...

Como o formato é delimitado, há bastante liberdade para determinar o tamanho de cada campo, desde que respeitados a ordem dos campos e os delimitadores.

ATENÇÃO

Os layouts de remessa já existentes poderão ser alterados para considerar a chave de identificação do tipo de tributo/segmento do pagamento (A, J, O, etc). Caso não sejam alterados no arquivo de retorno de pagamento no campo "Uso da Empresa" constatará somente a informação da chave do lançamento. E o processo de retorno de pagamento utilizará as regras atuais para identificar o tipo de tributo/segmento do pagamento quando o arquivo não tiver tal chave de identificação.

Exemplos:

* Arquivo de retorno de pagamento AAAA.RET não tem a chave de identificação do tipo de tributo:
  + Nesse caso o sistema irá utilizar a informação do campo "Tipo de Tributo" ou  campo "Identificador do tributo", depende do layout do tributo, para identificar o tributo.
* Arquivo de retorno de pagamento BBBB.RET tem a chave de identificação do tipo de tributo:
  + Nesse caso o sistema irá utilizar a informação da "Chave de Identificação do Tipo de Tributo" para identificar o tributo.
* Arquivo de retorno de pagamento em coligada com mais de 3 dígitos ('1000', por exemplo) tem a seguinte chave de identificação: **X**CCCCCLLLLLLLLLLLLLL (vide explicação na tabela acima). Exemplo de configuração do layout de pagamento (gerador de saídas) com este exemplo de chave de identificação:

Informações Complementares

* [Procedimento para importar arquivos de retorno de Pagamento Eletrônico](http://tdn.totvs.com/pages/viewpage.action?pageId=46079924)
* [DT Retorno de Pagamento do Banco Crefisa](http://tdn.totvs.com/display/LRM/DT+Retorno+de+pagamento+do+banco+Crefisa)
