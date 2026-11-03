---
content_hash: 977a7abd93a84485d9471ab8ba2d9309fda0da2b9655684a21258bc4d2241643
fetched_at: '2026-06-29T00:09:28.622627+00:00'
page_id: '423938725'
product: rm
source: tdn-rm
title: Passo a Passo para a geração do SPED Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938725
version: 7
---

O Sistema Público de Escrituração Digital (**SPED**) consiste em promover a integração dos fiscos federal, estadual e municipal, mediante a padronização, racionalização e compartilhamento das informações contábeis e fiscais digitais, assim como, integrarem todo o processo relativo às notas fiscais.

O SPED é composto por três projetos:

* **ECD**: Escrituração Contábil Digital
* **EFD**: Escrituração Fiscal Digital
* **NF-e**: Nota Fiscal Eletrônica (Nacional)

O Sistema Público de Escrituração Contábil Digital (**SPED Contábil)** foi  regulamentado através da Instrução Normativa RFB nº. 787, de 19 de novembro de 2007, e visa colocar a escrituração contábil na era digital. Através desse Sistema, o livro Diário e o livro Razão em papel serão substituídos pelos assinados digitalmente. 

**Observação** Antes da geração do SPED Contábil, sugerimos que seja executado o Pré – Validador do SPED Contábil para que assim os dados contábeis sejam pré-avaliados e as inconsistências que por ventura forem encontradas possam ser corrigidas antes da geração propriamente dita do arquivo digital, otimizando assim o envio dos dados.

**Geração do SPED Contábil:**  
**1º Passo**   
Para geração do SPED Contábil é necessário verificar e/ou cadastrar no sistema, informações exigidas pelo Fisco:

**Instituições Responsáveis pela Administração do Cadastro**  
Disponível em Rotinas Legais | SPED Contábil | Instituições Responsáveis Pela Administração do Cadastro. É utilizado para identificar os órgãos e instituições governamentais que compartilham das informações relativas à ECD. O cadastro virá preenchido com os dados divulgados pela legislação, podendo ser alterado por você em casos de alterações legais.

**Outras Inscrições Cadastrais**  
Disponível em Rotinas Legais | SPED Contábil | Outras Instituições Cadastrais. Nele devem ser incluídas as inscrições cadastrais do empresário ou sociedade empresária que legalmente tenham direito de acesso ao livro contábil digital, exceto Secretaria de Receita Federal e Secretaria de Estado da Fazenda que jurisdicionam o estabelecimento do empresário/sociedade empresária.

**Tipos de Relacionamentos de Participantes**  
Disponível em Rotinas Legais | SPED Contábil | Tipos de Relacionamentos de Participantes. É uma tabela que contém informações dos Tipos de Relacionamentos de Participantes com a Empresa no caso do mesmo se enquadrar nos relacionamentos definidos pelo Ato Declaratório Cofis nº 36 de 18/12/2007, Anexo II. Em caso de alterações legais a tabela pode ser alterada por você.

**Participantes**  
Disponível em Rotinas Legais | SPED Contábil | Participantes. Os participantes são empresários ou empresas que possuem vínculo definido por lei ou por regulamentação específica com outra empresa. Nesse cadastro deve ser informado os participantes, ou seja, clientes, fornecedores, transportadores, contabilistas, empresários, entre outros, que fazem ou fizeram relacionamentos com a empresa.

**Qualificação do Assinante**  
Disponível em Rotinas Legais | SPED Contábil | Qualificação de Assinantes.  
Para ECD é necessário informar o signatário (profissional responsável pelas informações contidas na ECD perante o fisco) com sua qualificação de assinante.  
Esse cadastro está preenchido com dados fornecidos pelo Departamento Nacional de Registro do comércio (DNRC) se for necessário você pode cadastrar novas qualificações para adaptar à legislação. As informações aqui definidas serão utilizadas no cadastro da escrituração contábil.

**Escriturações Contábeis**  
Disponível em Rotinas Legais | SPED Contábil | Escriturações Contábeis. Todos os livros da escrituração contábil podem ser incluídos no SPED Contábil, em suas diversas formas. São previstas as seguintes formas de escrituração:

* · Livro Diário (Completo, sem escrituração auxiliar)
* · Livro Diário com Escrituração Resumida (com escrituração auxiliar)
* · Livro Diário Auxiliar ao Diário com Escrituração Resumida
* · Livro Balancetes Diários e Balanços
* · Razão Auxiliar . Escrituração SCP Mantida pelo Sócio Ostensivo

**Plano de contas contábil**  
No plano de contas contábil é necessário informar a Natureza da conta para emissão do SPED. No caso de existir alguma conta que não deve ser enviada, deve ser informada a opção "Não informada". Outra informação necessária neste cadastro é a data de inclusão. O SPED não será gerado caso exista alguma conta sem a data de inclusão informada.

**Contas Correlatas (a partir do Layout 3.0)**  
Nos Anexos do plano de contas contábil poderá ser feita a associação da subconta correlata da conta contábil. -Uma conta contábil pode ter várias subcontas correlatas, porém uma subconta correlata somente pode estar associada a uma única conta contábil. - Uma conta contábil já vinculada como subconta correlata não pode possuir em seus Anexos nenhuma subconta correlata associada a ela. -Tanto a conta contábil como a subconta correlata devem ser Analíticas.

**Plano de contas gerencial**  
Se em Opções | Parâmetros | RM Saldus | Rotinas Legais | SPED Contábil, no parâmetro Considerar para o Centro de Custo, a opção *Conta Gerencial* estiver marcada, permite que a conta gerencial seja enviada para o arquivo referente ao SPED Contábil. Para isso é necessário também marcar a opção "Enviar para o SPED Contábil" no cadastro das contas gerenciais. Outra informação necessária neste cadastro é a data de inclusão. O SPED não será gerado caso exista alguma conta sem a data de inclusão informada.

**Centros de Custos**  
Se em Opções | Parâmetros | RM Saldus | Rotinas Legais | SPED Contábil, no parâmetro Considerar para o Centro de Custo, a opção *Próprio Centro de Custo* estiver marcada, permite que o centro de custo seja enviado para o arquivo referente ao SPED Contábil. Para isso é necessário também marcar a opção "Enviar para o SPED Contábil" no cadastro dos Centros de Custos. Outra informação necessária neste cadastro é a data de inclusão. O SPED não será gerado caso exista algum centro de custo sem a data de inclusão informada.

**Plano de contas paralelo**  
No menu Cadastros | Plano de contas paralelo é possível relacionar as contas do plano de contas contábil do sistema com as contas do plano de contas referencial fornecida pelo governo. Este processo é necessário quando a Sociedade Empresária estiver sujeita à regulamentação, seja do Banco Central ou da SRF. Para isso é necessário identificar a 'Instituição Responsável'. A opção 'Não Aplicável' neste cadastro deverá ser utilizada nos planos de contas paralelo cuja finalidade não seja a geração do SPED Contábil.

**Atualizar o Participante nos Lançamentos**  
Informar os *participantes* nas transações de Clientes/Fornecedores ou Filial dos lançamentos. Para facilitar a identificação dos participantes nos lançamentos existentes na base, pode-se utilizar o processo existente no próprio cadastro do Participante. O SPED não será gerado caso exista algum participante pendente de atualização.

**2º Passo**  
Definir os parâmetros que serão utilizados pelo processo de geração do SPED em Opções | Parâmetros | RM Saldus | Rotinas Legais | SPED Contábil.

**3º Passo**  
Conferir, através dos relatórios, os saldos das contas, onde as contas de resultado devem necessariamente estar zeradas. Lembre-se de verificar também o saldo das contas por centro de custo ou gerencial, conforme opção definida nos parâmetros, pois estes também devem estar zerados.

**4º Passo**  
O processo de geração do SPED Contábil consiste em criar um arquivo digital em um formato específico.  
É acessado através do Menu | Rotinas Legais | SPED Contábil | Gerar SPED Contábil.  
Para gerar o arquivo, são necessárias as seguintes informações:

* **Plano Referencial:** Conforme as regras de validação (anexo ao Ato Declaratório Cofis nº 36/07), o registro I051 não é obrigatório. O plano referencial é um plano de contas, elaborado com base na DIPJ. As empresas em geral devem usar O plano publicado pela Receita Federal pelo Ato Declaratório Cofis nº 36/07. As financeiras que utilizam o Cosif e as seguradoras não precisam informar o registro I051. Tem por finalidade estabelecer uma relação (um DE-PARA) entre as contas analíticas do plano de contas da empresa e um padrão, possibilitando a eliminação de fichas da DIPJ. O e-Lalur (Livro Eletrônico de Apuração do Lucro Real, um dos projetos do Sped) importará dados da escrituração contábil digital e montará um "rascunho" correspondente as várias das fichas hoje existentes na DIPJ. Assim, quanto mais precisa for sua indicação dos códigos das contas referenciais no registro I051, menor o trabalho no preenchimento do e-Lalur. Quaisquer equívocos na indicação do plano de contas referencial poderão ser corrigidos no e-Lalur.

* **Indicador do tipo de ECD** (disponível à partir do Layout 3.0) terá como opções: -ECD de empresa não participante de SCP como sócio ostensivo. -ECD de empresa participante de SCP como sócio ostensivo.  Quando este for o tipo selecionado, à seguir serão apresentadas para seleção, somente as Filiais parametrizadas como Sócio Ostensivo. -ECD da SCP.  Quando este for o tipo selecionado, à seguir serão apresentadas para seleção, somente as Filiais que são SCP.
* **Filial Matriz:** informe a filial Matriz responsável pela escrituração contábil
* **Tipo de Escrituração:** deverá ser "Centralizada" quando a Matriz for responsável pelas informações das Filiais vinculadas à sua inscrição, e "Descentralizada" quando cada filial for responsável por sua contabilização.
* **Situação Especial:** de acordo com a situação, deve ser selecionada uma das opções: Abertura, Cisão, Fusão, Extinção, Incorporação, Transformação, ou Nenhum. **Observações:**
  + Nos casos de extinção, cisão parcial, cisão total, fusão ou incorporação o SPED Contábil deverá ser entregue até o último dia útil do mês subseqüente ao do evento.
  + A opção de "Transformação" será utilizada quando, por exemplo, a empresa passar de Limitada para Sociedade Anônima.
  + Ainda para o campo Situação Especial, não será possível a utilização da situação de "Abertura" para o Layout 2.0 e posteriores

* **Descentralização:** esse campo só será exibido quando o tipo de escrituração for "Descentralizada".
* **Filial Escriturada:** esse campo só será exibido quando o tipo de "Descentralização" for por Filial. Selecione a filial que será escriturada.
* **Filtro de Filial:** esse campo só será exibido quando o tipo de escrituração for "Centralizada". Se desejar, selecione a Filial ou Filiais para as quais o arquivo digital para o SPED Contábil será gerado. Vale lembrar que a utilização de Filtro de Filial é de sua inteira responsabilidade, pois somente os dados filtrados serão levados para o arquivo digital.
* **Não enviar histórico de alteração de Contas Contábeis para o registro I050 e Não enviar histórico de alteração de Centros de Custos para o registro I100**: Algumas alterações efetuadas nos cadastros das contas e centros de custos geram um histórico de alteração. Se estas opções forem marcadas serão enviadas somente a situação atual dos registros com suas respectivas datas de inclusão. Se estas opções não forem marcadas, serão enviados para o SPED Contábil todos os Históricos de alterações destes registros.-
* **Formas de Escrituração:** informe a  Natureza do  Livro,  para o qual você deseja gerar o SPED, conforme o Cadastro de Escriturações.
* **Demonstrações Contábeis:** Informe aqui o  código  da estrutura de 'Transferência de Grupos Contábeis' utilizada para a apuração de resultado do período, assim o sistema faz a leitura e indica automaticamente o(s) Histórico(s) de Fechamento(s) utilizado(s). Se preferir indicar *manualmente* o(s) código(s) do(s) Histórico(s) de Fechamento(s) utilizado(s) e suas respectivas datas, basta clicar no *link* correspondente, lembrando que o histórico aqui informado deverá ser o mesmo utilizado  no fechamento do período, para zerar as contas de Receitas e Despesas através da Transferência de Grupos Contábeis. Informe também a data do fechamento em que foi utilizado. Cada fechamento deve utilizar histórico distinto. Se, por exemplo, o fechamento for trimestral, pelo menos quatro históricos devem ser informados, um para cada trimestre. **Observação** Dependendo da forma de escrituração utilizada e da identificação da demonstração, é possível que se defina neste momento um novo Cabeçalho para a Demonstração.
* **Indicador do início do período** (disponível a partir do Layout 2.0) terá como opções:
  + 0 - Normal (início no primeiro dia do ano)
  + 1 - Abertura
  + 2 - Resultante de cisão/fusão ou remanescente de cisão, ou realizou incorporação
  + 3 - Início de obrigatoriedade da entrega da ECD no curso do ano calendário

* **Indicador de Finalidade da Escrituração** (disponível a partir do Layout 2.0) terá como opções:

  + 0 - Original
  + 1 - Substituta da escrituração com NIRE
  + 2 - Substituta da escrituração sem NIRE
  + 3 - Substituta da escrituração com troca de NIRE  
          **Observações** - Quando a opção "3 - Substituta da escrituração com troca de NIRE" for selecionada, será apresentado um novo campo NIRE da escrituração que Está sendo Substituída, para que seja informado o novo NIRE. - Quando as opções 1, 2 ou 3 forem selecionadas será apresentado um novo campo Hash da escrituração substituída para que seja localizado e selecionado o arquivo de Hash.
* **Indicador de empresa de grande porte** (disponível no Layout 2.0) terá como opções:

  + 0 - Empresa não é de Grande Porte
  + 1 - Empresa de grande porte - Ativo Total superior a R$ 240.000.000,00 ou  Receita Bruta  Anual superior R$300.000.000,00. **Ou**
* **Indicador de entidade sujeita a auditoria independente** (disponível a partir do Layout 3.0) terá como opções:

  + 0 - Empresa não é entidade sujeita a auditoria independente
  + 1 - Empresa é entidade sujeita a auditoria independente - Ativo Total superior a R$ 240.000.000,00 ou Receita Bruta Anual superior R$300.000.000,00.  
    -
* **DMPL / DLPA** (disponível a partir do Layout 2.0) **[**Estrutura da Demonstração**](http://tdn.totvs.com/x/qcpEGQ)**: Neste campo o usuário deverá selecionar uma estrutura de DMLP ou DLPA já criada anteriormente através do menu de Demonstração Contábil. Esta informação irá compor os registros J200, J210 e J215 do SPED.

  Conforme a necessidade de envio, podem ser selecionadas as opções de Enviar somente Fatos Contábeis que tenha valor processado bem como Mostrar código do Fato Contábil juntamente com a descrição (registro J200).
* **Parametrização da DRE / Balanço Patrimonial:** pode-se  informar  uma  DRE  e/ou  Balanço Patrimonial criados a partir do sistema (menu Demonstração de Resultados) para serem utilizados na validação do arquivo. Para isto deve-se marcar a opção Utilizar modelo criado no RM Saldus. Caso não deseje utilizar os relatórios criados no RM Saldus, deve-se deixar desmarcadas estas opções. Desta forma a DRE e o Balanço Patrimonial serão criados a partir dos registros correspondentes. Nesta etapa deve ser definido também o Grau de Aglutinação. Para maiores informações sobre as Contas de Aglutinação **clique aqui**.

* **Seleção dos registros facultativos:** a partir da forma de escrituração contábil informada anteriormente, serão apresentados os registros (opcionais) que serão enviados para o arquivo referente ao SPED Contábil. Selecione os registros que devem ser enviados para o SPED Contábil, conforme a seguir:
  + **Escrituração Contábil: Livro Diário (Completo, sem escrituração auxiliar)**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); 0150 (Tabela de Cadastro de Participante); 0180 (Identificação do Relacionamento com o Participante); I052 (Indicação dos Códigos de Aglutinação); I075 (Tabela de Histórico Padronizado); I350 (Saldos da Contas de Resultado antes do Encerramento – Identificação da Data); I355 (Detalhes dos saldos das contas de resultado antes do encerramento); J005 (Demonstrações Contábeis); J100 (Balanço Patrimonial); J150 (Demonstração do Resultado do Exercício).
  + **Escrituração Contábil: Livro Diário com Escrituração Resumida (com escrituração auxiliar)**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); 0150 (Tabela de Cadastro de Participante); 0180 (Identificação do Relacionamento com o Participante); I052 (Indicação dos Códigos de Aglutinação); I075 (Tabela de Histórico Padronizado); I350 (Saldos da Contas de Resultado antes do Encerramento – Identificação da Data); I355 (Detalhes dos saldos das contas de resultado antes do encerramento); J005 (Demonstrações Contábeis); J100 (Balanço Patrimonial); J150 (Demonstração do Resultado do Exercício).
  + **Escrituração Contábil: Livro Diário Auxiliar ao Diário com Escrituração Resumida**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); 0150 (Tabela de Cadastro de Participante); 0180 (Identificação do Relacionamento com o Participante); I075 (Tabela de Histórico Padronizado); I150 (Saldos Periódicos – Identificação do Período); I155 (Detalhes dos Saldos Periódicos).
  + **Escrituração Contábil: Livro Balancetes Diários e Balanços**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); I052 (Indicação dos Códigos de Aglutinação); J005 (Demonstrações Contábeis); J100 (Balanço Patrimonial); J150 (Demonstração do Resultado do Exercício); I350 (Saldos das Contas de Resultado Antes do Encerramento – Identificação da Data); I355 (Detalhes dos saldos das contas de resultado antes do encerramento).
  + **Escrituração Contábil: Razão Auxiliar**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); 0150 (Tabela de Cadastro de Participante); 0180 (Identificação do Relacionamento com o Participante); I050 (Plano de Contas); I075 (Tabela de Histórico Padronizado); I150 (Saldos Periódicos – Identificação do Período); I155 (Detalhes dos Saldos Periódicos); I555 (Detalhes do Livro Razão Auxiliar com Layout Parametrizável).
  + **Escrituração Contábil: Escrituração SCP Mantida pelo Sócio Ostensivo**  
    Registros facultativos: 0020 (Escrituração Contábil Descentralizada); 0150 (Tabela de Cadastro de Participante); 0180 (Identificação do Relacionamento com o Participante); I020 (Campos Opcionais); I051 (Plano de contas Referencial); I052 (Indicação dos Códigos de Aglutinação); I053 (Subcontas Correlatas); I075 (Tabela de Histórico Padronizado); I100 (Centro de Custo); I157 (Transferência de Saldos do Plano de Contas Anterior); I350 (Saldos da Contas de Resultado antes do Encerramento – Identificação da Data); I355 (Detalhes dos saldos das contas de resultado antes do encerramento); J005 (Demonstrações Contábeis); J100 (Balanço Patrimonial); J150 (Demonstração do Resultado do Exercício); J200 (Tabela de Histórico de Fatos Contábeis que Modifica a Conta Lucros Acumulados ou a Conta Prejuízos Acumulados ou Todo o Patrimônio Líquido); J210 (Demonstração de Lucros ou Prejuízos Acumulados (DLPA)/Demonstração de Mutações do Patrimônio Líquido (DMPL); J215 (Fato Contábil que Altera a Conta Lucros Acumulados ou a Conta Prejuízos Acumulados ou o Patrimônio Líquido); J935 (Identificação dos Auditores Independentes)
* **Registros Dependentes**  
  Existem alguns registros que respeitam a regra de dependência de registros, ou seja, caso um registro dependente seja enviado para o arquivo do SPED Contábil, os outros registros dependentes a ele deverão também ser enviados. Caso um registro dependente não seja enviado, os registros dependentes a ele não poderão ser enviados para o arquivo referente ao SPED Contábil.  
  Exemplo: Escolhendo a forma de escrituração contábil Razão Auxiliar durante a parametrização do processo e avançar até a tela referente aos registros facultativos, ao desmarcar o registro I050 para não ser enviado para o arquivo os registros I150 e I155 serão desmarcados automaticamente e assim também não serão enviados para o arquivo do SPED Contábil.  
  Para as escriturações contábeis Livro Diário (Completo, sem escrituração auxiliar), Livro Diário com Escrituração Resumida (com escrituração auxiliar), Livro Diário Auxiliar ao Diário com Escrituração Resumida e Livro Balancetes Diários e Balanços os registros que possuem dependência são J005, J100, J150, I052.  
  Para a escrituração contábil Razão Auxiliar os registros que possuem dependência são I050, I150, I155.  
     
  -**J800 - Outras Informações:** Se desejar, selecione arquivos que contenham informações adicionais que julgue necessárias constar nos livros a serem entregues, tais como Pareceres, Outras Demonstrações, Relatórios, etc.  Estes arquivos devem ter a extensão .RTF

**5º Passo**   
Após a execução do processo, o arquivo digital será salvo na máquina em um caminho fixo. Caso queira o arquivo poderá ser salvo em um caminho específico, indicado por você. Para isto clique no botão "Baixar Arquivo" e informe os dados.

Para otimizar a utilização da memória evitando travamento na execução do processo de geração do SPED, o sistema utiliza o recurso de **Upload** dos arquivos manipulados, tais como arquivo com modelo próprio para o Razão Auxiliar e Arquivos Adicionais-J800, levando-os parcialmente para o servidor de aplicação liberando a memória. Ao mandar Copiar o arquivo gerado o sistema utiliza o recurso de **Download** para baixar o arquivo do servidor para o local indicado.

Ao final do processo serão gerados LOG´s com informações relevantes sobre os dados levados para os registros do arquivo digital assim como LOG's de execução, indicando todas as ações realizadas para a geração do SPED e o tempo gasto em cada uma. Favor avaliar o conteúdo da pasta **Logs**.  
   
**6º Passo**   
Após a geração do arquivo digital pelo TOTVS Gestão Contábil, você deverá importar e validar este arquivo no Programa Validador e Assinador (PVA) fornecido pela Receita Federal, que você já deve ter previamente baixado.

Após a validação do arquivo do SPED Contábil pelo PVA da ECD, é importante que antes de realizar a Transmissão da Escrituração Contábil, os relatórios (DRE, Balanço Patrimonial, DMPL/DLPA e outros) apresentados no validador sejam conferidos com os relatórios gerados pelo TOTVS Gestão Contábil.

Após a conferência, o arquivo deverá ser assinado digitalmente pelo empresário ou representante legal da sociedade empresária e pelo contabilista responsável pela escrituração.

Depois de transmitida, a escrituração contábil é armazenada em um banco de dados que irá permitir que os órgãos parceiros do SPED obtenham cópias integrais do arquivo. O titular da escrituração poderá, pela Internet, ter conhecimento de qual órgão teve acesso a sua escrituração.

Uma vez transmitida, qualquer pessoa que tiver o arquivo, poderá verificar a autenticidade da escrituração contábil da empresa, visualizar e imprimir a escrituração.

Veja Também

* Contas de Aglutinação
