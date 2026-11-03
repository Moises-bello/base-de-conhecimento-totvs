---
content_hash: 3e6e33870ef132cc8426b4ddb7b30579465dedd31916bc64a681c5d4b6dc0666
fetched_at: '2026-06-29T00:11:56.746280+00:00'
page_id: '870398587'
product: rm
source: tdn-rm
title: Parâmetros ECD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870398587
version: 21
---

# **01.  Visão Geral**

Este cadastro é necessário para a geração da ECD MultiColigada.  Esta funcionalidade foi desenvolvida para simplificar o processo de geração do arquivo, grande parte dessas informações era solicitada no momento de gerar a ECD e agora ficarão armazenadas em um cadastro.  
O processo irá consultar todas essas informações que foram cadastradas em cada Escrituração Contábil para gerar o arquivo da ECD.

# **02.  Abas, Campos e Funcionalidades** A tela está dividida em abas para facilitar a inserção e controle dos dados:

**2.1. Identificação**

Clique aqui para visualizar

**Versão do Layout:**Os layouts disponibilizados são a partir do 9.0 que possui início de vigência no ano de 2020 (válido por 5 anos). Esse campo é preenchido automaticamente de acordo com a data final da Escrituração Contábil.

**Plano Referencial:**Conforme as regras de validação (anexo ao Ato Declaratório Cofis nº 36/07), o registro I051 não é obrigatório, as financeiras que utilizam o Cosif e as seguradoras não precisam informar o registro I051.  
O plano referencial é um plano de contas, elaborado com base na DIPJ. As empresas em geral devem usar o plano publicado pela Receita Federal pelo Ato Declaratório Cofis nº 36/07.   
A finalidade é estabelecer uma relação (um DE-PARA) entre as contas analíticas do plano de contas da empresa e um padrão, possibilitando a eliminação de fichas da DIPJ.   
O e-Lalur (Livro Eletrônico de Apuração do Lucro Real, um dos projetos do Sped) importará dados da escrituração contábil digital e montará um "rascunho" correspondente as várias das fichas hoje existentes na DIPJ. Assim, quanto mais precisa for sua indicação dos códigos das contas referenciais no registro I051, menor o trabalho no preenchimento do e-Lalur.   
Quaisquer equívocos na indicação do plano de contas referencial poderão ser corrigidos no e-Lalur.

**Indicador do tipo de ECD:**

Serão apresentadas as 3 opções abaixo.

* ECD da empresa não participante de SCP como sócio ostensivo.
* ECD de empresa participante de SCP como sócio ostensivo: Quando este for o tipo selecionado, no campo "Filial Matriz" serão apresentadas para seleção, somente as Filiais parametrizadas como Sócio Ostensivo.
* ECD da SCP: Quando este for o tipo selecionado, no campo "Filial SPC" serão apresentadas para seleção, somente as Filiais que são SCP.

**Filial Matriz:**Este campo é filtrado conforme regra supracitada. Informe a filial Matriz responsável pela Escrituração Contábil. **Plano Consolidado - Bloco K:**Este campo só será habilitado caso o tipo de Escrituração seja "Centralizada".

**Tipo de Escrituração:**Deverá ser "Centralizada" quando a Matriz for responsável pelas informações das Filiais vinculadas à sua inscrição, e "Descentralizada" quando cada filial for responsável por sua contabilização.

**Situação Especial:**De acordo com a situação, deve ser selecionada uma das opções: Cisão, Fusão, Extinção, Incorporação ou Nenhum.

**Tipo Descentralização:**Esse campo só será habilitado quando o tipo de escrituração for "Descentralizada".

**Filial Escriturada:**Esse campo só será habilitado quando o tipo de "Descentralização" for por Filial. Selecione a filial que será escriturada.

**Filtro de Filial:**   
Esse campo só será habilitado quando o tipo de escrituração for "Centralizada". Se desejar, selecione a Filial ou Filiais para as quais o arquivo digital para o SPED Contábil será gerado. Vale lembrar que a utilização de Filtro de Filial é de sua inteira responsabilidade, pois somente os dados filtrados serão levados para o arquivo digital.

**Não enviar histórico de alteração de Contas Contábeis para o registro I050 | Não enviar histórico de alteração de Centros de Custos para o registro I100:**Algumas alterações efetuadas nos cadastros das contas e centros de custos geram um histórico de alteração.   
Se estas opções forem marcadas serão enviadas somente a situação atual dos registros com suas respectivas datas de inclusão.   
Se estas opções não forem marcadas, serão enviados para o SPED Contábil todos os Históricos de alterações destes registros.

**2.2. Demonstração**

Clique aqui para visualizar

**Demonstração:**Parametrização da Aba de Demonstração, que será utilizada para compor o Bloco J.

Informe aqui o código da estrutura de 'Transferência de Grupos Contábeis' utilizada para a apuração de resultado do período, assim o sistema fará a leitura e indicará automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s) na estrutura indicada. Se preferir indicar manualmente o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, basta clicar no link correspondente, lembrando que o histórico aqui informado deverá ser o mesmo utilizado no fechamento do período, para zerar as contas de Receitas e Despesas através da Transferência de Grupos Contábeis. Informe também a data do fechamento em que foi utilizado. Cada fechamento deve utilizar histórico distinto. Se, por exemplo, o fechamento for trimestral, pelo menos quatro históricos devem ser informados, um para cada trimestre.

**Transferência de Grupos Contábeis:**Esta seção exibe as Transferências de Grupos Contábeis relacionadas à Apuração de Resultado, que possuem moldes dentro do período de escrituração. As transferências devem ser analisadas cuidadosamente, garantindo que estejam dentro do intervalo de datas estabelecido.

**Históricos Padrões:**  
Os Históricos Padrões apresentados nesta seção são exclusivamente aqueles de Fechamento. Para cada histórico, é obrigatório informar uma Data que não pode ser nula. Essa data deve estar dentro do período de escrituração e corresponder ao último dia de um mês.

**Identificação da Demonstração:**

Nesta seção, você encontrará as seguintes opções para identificação da demonstração:

* 1 - Demonstr. cont. do empresário ou sociedade empresária a que se refere a escrituração.
* 2 - Demonstrações consolidadas ou de outros empresários ou sociedades empresárias.

Obs:

1. Ao selecionar a segunda opção, é obrigatório o preenchimento do **Cabeçalho**.
2. Para escriturações onde a Forma de Escrituração é **Razão Auxiliar** ou **Diário Auxiliar**, o campo não será editável.

**2.3. Informações Complementares**

Clique aqui para visualizar

**Indicador do Início do Período:**Especifica a natureza do início do período contábil da empresa, indicando se trata-se de um novo exercício, resultado de uma operação de fusão, cisão ou incorporação, ou se houve alteração na obrigatoriedade de entrega da ECD durante o ano calendário. As opções mais comuns incluem:

* **Abertura:** Primeira escrituração contábil da empresa.
* **Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação:** Empresa resultante de uma operação de fusão, cisão ou incorporação.
* **Normal:** Continuação da escrituração contábil de exercícios anteriores.
* **Início de obrigatoriedade de entrega da ECD no curso do ano calendário:** Empresa que se tornou obrigada a entregar a ECD durante o ano calendário.

**Indicador de Finalidade da Escrituração:**Informa se a escrituração é **original** (primeira entrega) ou **substituta** (retificação de uma escrituração anterior). 

**Hash da Escrituração Substituída:**É um código de verificação que identifica a escrituração anterior que está sendo substituída pela atual. Esse campo é utilizado em casos de retificações ou ajustes na escrituração contábil.

**Indicador de Empresa de Grande Porte:**Indica se a empresa é considerada de grande porte, de acordo com os critérios estabelecidos pela legislação. Essa informação influencia a obrigatoriedade de determinadas informações e procedimentos contábeis.

**Estrutura da Demonstração:**Define a estrutura da demonstração contábil que será utilizada na escrituração. Essa informação é importante para a padronização da apresentação das informações contábeis.

**Tipo:**Apresenta duas alternativas, sendo elas:

* **DLPA:** Demonstração das Mutações do Patrimônio Líquido. Essa demonstração mostra as alterações ocorridas no patrimônio líquido da empresa em um determinado período, explicando o aumento ou a diminuição do valor do patrimônio líquido.
* **DMPL:** Embora não seja uma sigla tão comum, é provável que se refira a um tipo específico de demonstração contábil ou relatório relacionado ao patrimônio líquido.

**Enviar somente Fatos Contábeis que tenha valor processado:**Indica se somente os fatos contábeis que geraram movimentação financeira devem ser incluídos na escrituração. Essa opção pode ser utilizada para otimizar o processo de geração do arquivo ECD.

**Mostrar código do Fato Contábil juntamente com a descrição (registro J200):**Determina se o código do fato contábil deve ser apresentado juntamente com a sua descrição no registro J200. Essa informação pode ser útil para a auditoria e análise das informações contábeis.

**2.4. Parametrização DRE / Balanço Patrimonial**

Clique aqui para visualizarNesta etapa, define-se como as informações serão enviadas para as origens de registro da Demonstração do Resultado do Exercício (J150) e do Balanço Patrimonial (J100). Abaixo estão detalhadas as opções de parametrização disponíveis:

#### **Origem da DRE (J150) - Opções de Busca**

1. Buscar a partir do Plano de Contas:

É possível configurar o registro para que as informações sejam obtidas diretamente do Plano de Contas. As seguintes parametrizações estão disponíveis:

* **Mostrar o saldo final da "Apuração de Resultado do Exercício", junto a sua Descrição;**
* **Não mostrar contas analíticas na demonstração de resultado do exercício;**
* **Mostrar o código da conta na geração do J150;**

2. Buscar a partir da Ferramenta de Demonstrações Contábeis:

Outra opção é configurar o registro para que as informações sejam extraídas a partir da Ferramenta de Demonstrações Contábeis. As parametrizações disponíveis incluem:

* **Definição de estrutura e colunas para busca dos valores;**
* **Mostrar código do fato contábil na geração do registro J150;**
* **Mostrar fatos contábeis com valor zerado na geração do registro J150;**

**Origem do Balanço (J100)** **- Opções de Busca**

1. Buscar a partir do Plano de Contas:

É possível configurar o registro para que as informações sejam obtidas diretamente do Plano de Contas. As seguintes parametrizações estão disponíveis:

* **Grau de aglutinação (Balanço Patrimonial);**
* **Mostrar o código da conta na geração do J100;**
* **Gerar informações quando o saldo final estiver zerado e existir saldo inicial;**
* **Gerar informações quando o saldo final estiver zerado e existiram movimentações;**

2. Buscar a partir da Ferramenta de Demonstrações Contábeis:

Outra opção é configurar o registro para que as informações sejam extraídas a partir da Ferramenta de Demonstrações Contábeis. As parametrizações disponíveis incluem:

* **Definição de estrutura e colunas para busca dos valores;**
* **Mostrar código do fato contábil na geração do registro J100;**
* **Gerar informações quando o saldo final estiver zerado e existir saldo inicial;**

**Observações:**

1. Nesta etapa deve ser definido também o Grau de Aglutinação. Para maiores informações sobre as Contas de Aglutinação [clique aqui](https://tdn.totvs.com/x/hMpEGQ).
2. O registro J150 será gerado seguindo a ordem que foi definida nos fatos contábeis na [Estrutura](https://tdn.totvs.com/pages/viewpage.action?pageId=423938729)da Demonstração. Caso necessário, essa ordem poderá ser alterada. A ordem do registro apenas será afetada caso nesse passo da geração do SPED seja informada uma estrutura de demonstração.
3. Quando escolhido pelo usuário gerar a DRE através da ferramenta de demonstrações contábeis, utilize o 'Mostra fato Contábil com Valor zerado na geração do registro J150' parar possibilitar que o usuário gere fatos com saldos igual a zero na ECD.

**2.5. Registros Facultativos**

Clique aqui para visualizar

Os registros facultativos são aqueles que não são obrigatórios para todas as empresas. A inclusão desses registros depende de características específicas da empresa, como seu porte, natureza das operações e legislação aplicável.

**Registros Facultativos por Forma de Escrituração:**

Alguns registros são dependentes entre si, não sendo possível seleciona-los individualmente, esses estão destacados em negrito.

1. **Diário Geral:**

* 0020 - Escrituração Contábil Descentralizada
* 0150/0180 - Cadastro e Identificação de relacionamento do Participante
* **I052 - Indicação dos Códigos de Aglutinação**
* I053 - Subcontas
* I075 - Tabela de Histórico Padronizado
* I157 - Transferência de Saldos de Plano de Contas Anterior
* I350/I355 - Saldos das Contas de Resultado Antes do Encerramento - Identificação da Data e Detalhes dos Saldos
* **J005 - Demonstrações Contábeis**
* **J100 - Balanço Patrimonial**
* **J150 - Demonstração do Resultado do Exercício**

2. **Diário Resumido:**

* 0020 - Escrituração Contábil Descentralizada
* 0150/0180 - Cadastro e Identificação de relacionamento do Participante
* **I052 - Indicação dos Códigos de Aglutinação**
* I053 - Subcontas
* I075 - Tabela de Histórico Padronizado
* I157 - Transferência de Saldos de Plano de Contas Anterior
* I350/I355 - Saldos das Contas de Resultado Antes do Encerramento - Identificação da Data e Detalhes dos Saldos
* **J005 - Demonstrações Contábeis**
* **J100 - Balanço Patrimonial**
* **J150 - Demonstração do Resultado do Exercício**

3**. Diário Auxiliar:**

* 0020 - Escrituração Contábil Descentralizada
* 0150/0180 - Cadastro e Identificação de relacionamento do Participante
* I075 - Tabela de Histórico Padronizado
* I150/I155 - Saldos Periódicos - Identificação do Período e Detalhes dos Saldos

4. **Balancete:**

* 0020 - Escrituração Contábil Descentralizada
* **I052 - Indicação dos Códigos de Aglutinação**
* I053 - Subcontas
* I157 - Transferência de Saldos de Plano de Contas Anterior
* I350/I355 - Saldos das Contas de Resultado Antes do Encerramento - Identificação da Data e Detalhes dos Saldos
* **J005 - Demonstrações Contábeis**
* **J100 - Balanço Patrimonial**
* **J150 - Demonstração do Resultado do Exercício**

5. **Razão Auxiliar:**

* 0020 - Escrituração Contábil Descentralizada
* 0150/0180 - Cadastro e Identificação de relacionamento do Participante
* **I050 - Plano de Contas**
* I075 - Tabela de Histórico Padronizado
* **I150/I155 - Saldos Periódicos - Identificação do Período e Detalhes dos Saldos**

6. **SCP Mantida por Sócio Ostensivo:**

* 0020 - Escrituração Contábil Descentralizada
* 0150/0180 - Cadastro e Identificação de relacionamento do Participante
* **I052 - Indicação dos Códigos de Aglutinação**
* I053 - Subcontas
* I075 - Tabela de Histórico Padronizado
* I157 - Transferência de Saldos de Plano de Contas Anterior
* I350/I355 - Saldos das Contas de Resultado Antes do Encerramento - Identificação da Data e Detalhes dos Saldos
* **J005 - Demonstrações Contábeis**
* **J100 - Balanço Patrimonial**
* **J150 - Demonstração do Resultado do Exercício**
