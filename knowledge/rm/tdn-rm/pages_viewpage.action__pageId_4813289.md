---
content_hash: c73c32305cae9fbf1ece96dd5b921357532dbea1949a7ab0f12818e83ad5d187
fetched_at: '2026-06-29T00:10:19.314013+00:00'
page_id: '4813289'
product: rm
source: tdn-rm
title: Nota Fiscal Eletrônica Municipal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813289
version: 5
---

BLOCK

Nota Fiscal Eletrônica Municipal

FAQ: **Nota Fiscal Eletrônica Municipal**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 10.80 |

Avaliação

* **Como Fazer**

Como parametrizar o sistema para utilizar Nota Fiscal Eletrônica Municipal?

* ***Definição do Processo***

Tem por finalidade parametrizar a base de dados para geração de NFe Municipal para os municípios de São Paulo, Recife, Manaus, Macaé, Resende, assim como as validações feitas no movimento e restrições para escrituração dos mesmos.

Solução

* ***Parametrizações Necessárias***

Acessar **| Cadastro | Fórmula | Incluir |** e cadastrar formula que será utilizada para calcular a base de cálculo de ISS.

Exemplo:

SE

TABPRD ('TIPO' , 'S') = 'S'

ENTAO

KQT \* KPU

SENAO 0

FIMSE

Acessar **| Cadastro | Tabelas de Tributação | TRIBUTOS |** e cadastrar tributo **| ISS |**, onde deve informar:

Sigla: ISS

Tipo tributo fiscal: ISS

Tipo: Variável

Incidência: Serviço

Buscar Alíquota: Tipo de Movimento

Acessar **| Relatório | Gerador |** **Novo |** e incluir relatório para ser utilizado na exportação dos dados para Prefeitura. O layout em questão pode ser obtido junto ao suporte, e corresponde ao layout 30.01.

Conteúdo do Layout:

[![clip_image002](http://lh5.ggpht.com/_G7KXZLoZDsY/TN1167a4YbI/AAAAAAAADnw/ee8R5R9mHaE/clip_image002_thumb.jpg?imgmax=800 "clip_image002")](http://lh6.ggpht.com/_G7KXZLoZDsY/TN115-QVXfI/AAAAAAAADns/x7DxzA5ZOIY/s1600-h/clip_image002%5B3%5D.jpg)

Acessar **| Cadastro | Segurança | Usuário |** editar os usuários que poderão enviar NFe e editar a aba | **Configuração de Segurança |** para averiguar o perfil vinculado aos mesmos.

De posse desta informação deve acessar **| Cadastro | Segurança | Perfil | Acesso a Menus |** e habilitar acesso á opção **| Customização | NFe Municipal |**

Acessar | **Opções | Parâmetros | Tipos de Movimentos | RMNucleus | 04.09 | Avançar |** editar movimento a ser parametrizado para este fim e informar:

**Etapa Fis Tributação – Item**

**Tributo**: ISS

**Cód.Retenção**: informar o código da receita que deverá ser apresentado na guia a ser gerada(opcional)

**Fórmula da base de cálculo do tributo**: informar código da fórmula que retorna o conteúdo desejado para composição da base de cálculo do tributo

**Procurar alíquota em**: Município

T**ributo Base**: ISS

**Etapa Fis – Dados**

Informar | Buscar Endereço em |: qual endereço referenciado em **| Cadastro | Cliente \ Fornecedor | Endereço |** será considerado na inclusão da movimentação

**Etapa Fis – Nfe**

Informar em NFe Municipal:

**- NFe**: definir como será gerada numeração do documento de NFE tendo as opções:

Não Integrado: Não emite nota fiscal eletrônica

Numerado por auto-incremento: O tipo de movimento passa a emitir Nota Fiscal eletrônica e a numeração e série são geradas por auto-incremento.

Numerado pelo movimento : O tipo de movimento passa a emitir Nota Fiscal eletrônica e a série e número do movimento passam a ser utilizados pelo RPS.

**- Fórmula Valor do Serviço**: informar código da fórmula a ser utilizada para calcular “valor do serviço”. A mesma só pode utilizar variáveis de itens e vai incidir apenas sobre os itens que possuírem base de cálculo preenchida, motivo pelo qual deve ser feita restrição dos tipos dos itens na mesma.

Exemplo: (KQT \* KPU)

Funcionamento deste parâmetro

Fórmula do Valor do Serviço NFe preenchida

O sistema vai comparar o conteúdo da fórmula com a informação preenchida na “Base de Cálculo do Tributo ISS” do item. Caso os dados sejam distintos, a diferença entre eles será preenchida na aba **| NF-e Serviço | Dados do Recibo | Dedução do Serviço |** na exportação do movimento.

Exemplo:

Valor total do Item: 1.250,00

Valor da base de calculo do tributo: 610,00

Fórmula | KQT \* KPU |: 1.250,00

Vr de Dedução do Serviço: 640,00

Fórmula do Valor do Serviço NFe vazio

O sistema vai copiar a informação preenchida na aba **| Integrações | Integração RMLIBER | Dedução de ISS |** para aba | **NF-e Serviço | Dados do Recibo | Dedução do Serviço |**

* ***Descrição do Processo***

**Valor do Serviço NF-e:**

Será apresentado este campo, somente se nos parâmetros do tipo de movimento sub pasta Dados Fiscais, seja informado uma fórmula para o valor do serviço NF-e.

Observação:

O campo Valor Serviço NF-e é diretamente dependente que o campo tipo do cadastro do produto seja um serviço. Caso não seja, a fórmula não é executada e o campo é preenchido com 0 (zero). Este campo é preenchido automaticamente em tempo de cálculo do item de movimento.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link:<http://totvsconnect.blogspot.com/2010/11/como-fazer-nota-fiscal-eletronica.html>
