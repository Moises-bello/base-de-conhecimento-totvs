---
content_hash: 6f3afe934453bb78722beff9e10c79e26b3ee1738e0519786dd4cacb75f22559
fetched_at: '2026-06-29T00:09:29.274265+00:00'
page_id: '423938861'
product: rm
source: tdn-rm
title: Novidades da Versão 11.20.0  - Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938861
version: 4
---

**11.20.20 - Outras atualizações:** Evoluído o processo de Exclusão de Lançamentos, não permitindo a exclusão de lançamentos com data menor ou igual à data de fechamento.

**11.20.15 - Amarração de lançamentos** Alterada a mensagem apresenta ao incluir um lançamento que contraria alguma regra ativa do cadastro de amarração de lançamentos, sendo acrescentada a expressão 'Amarração de Lançamentos', facilitando assim a identificação do erro.

**11.20.15 - Associação de Filtros no cadastro de Usuários** No cadastro de usuários, em associação de filtro, foi disponibilizada a tabela de centro de custo 'GCCUSTO', permitindo que sejam criados filtros associados aos usuários. Este filtro será aplicado na tela de visão do cadastro de centro de custo, e nos seus Lookups (componente de seleção de centro de custo).

**11.20.15 - Outras Atualizações:** Otimizada a utilização de históricos padrões nos lançamentos contábeis.

**11.20.10 - Conversão do Plano de Contas ANS** Foi disponibilizada no processo de conversão do plano de contas da ANS uma opção que permitirá informar a quantidade de dígitos que a nova conta deverá ter.

**11.20.5 - Outras Atualizações:**

* Atualização na importação de movimentos com contabilização do RM Nucleus.
* Otimização no processo de Consistência de Lançamentos

**11.20.1 - Consistência de Lançamentos** Atualização do processo de consistência de lançamentos ao marcar a opção "Ajustar Capa do Lote Automaticamente".

**11.20.1 - Centros de Custos** Acrescentadas as opções 'Ativo' e 'Permite Lançamentos' para a criação de filtros na tela do cadastro de Centro de Custos.

**11.20.1 - Conversão do Plano de Contas ANS** Se houver alguma conta repetida no arquivo XML, o sistema estará informando esta situação, não permitindo que a conversão seja executada.

**11.20.1 - Outras Atualizações:**

* Atualização nos parâmetros que influenciam na forma de visualizar o lançamento contábil após alguma alteração.
* Atualização no Processo de Cópia de Centros de Custos entre Coligadas

**11.20.0 - SPED Contábil:**

* Implementado o campo 'Data de Inclusão' no cadastro de Conta Contábil, Conta Gerencial e Centro de Custo. Este campo é de preenchimento obrigatório. Ao incluir uma conta ou um centro de custo será obrigatório informar a data de inclusão. A data do dia será sugerida como data de inclusão, podendo neste momento ser alterada. Para as contas e centros de custos já incluídos na base, a data poderá ser informada editando-se os cadastros e informando-a ou através do novo Processo implementado 'Atualização da Data de Inclusão'. Este processo permitirá ao usuário atualizar a data de inclusão de várias contas ou centros de custos ao mesmo tempo, basta marcarem os registros desejados, executar o processo e informar a data. Somente será permita a execução do processo para registros com a data de inclusão ainda em branco. Uma vez preenchida a data de inclusão das contas e centros de custos, ela não poderá mais ser alterada.
* O campo 'Natureza da conta para emissão do SPED' dentro do cadastro da conta contábil passou a ser de preenchimento obrigatório.
* O sistema passou a gravar o Histórico de alteração de conta contábil, que poderá ser visualizado através do Anexo disponibilizado no cadastro de contas contábeis. Qualquer alteração efetuada em um dos três campos 'Descrição', 'Natureza da conta para emissão do SPED' e 'Analítica/Sintética' será gravado um Histórico de alteração. Este histórico será enviado para o arquivo digital do SPED Contábil (registro I050).
* **Observações:**
  + A informação da Data de Inclusão da conta contábil não irá gerar um Histórico de alteração.
  + Os Históricos de alteração somente começarão a ser gravados a partir do momento em que as contas já tiverem o campo Data de Inclusão  preenchida .
  + A primeira alteração efetuada em um dos três campos citados anteriormente irá gerar dois Históricos de uma só vez, sendo que o primeiro histórico terá a data de inclusão da conta contábil e os dados antigos (informações antes da alteração) e o segundo histórico terá a data do dia da alteração e os dados correntes (os que foram alterados). A segunda alteração em diante irá gerar somente um Histórico de alteração.
  + Somente será gerado um Histórico de alteração por dia. Se uma conta for alterada mais de uma vez no mesmo dia, sempre será gravado o Histórico da última alteração.
  + Se o campo 'Natureza da conta para emissão do SPED' de uma conta contábil for alterado para 'Não informada', todos os Históricos de alteração existentes para esta conta serão excluídos da base, uma vez que os Históricos só serão utilizados para emissão do SPED Contábil.

* O sistema passou a gravar o Histórico de alteração de Contas Gerenciais/ Centros de Custos, que poderá ser visualizado através do Anexo disponibilizado nos respectivos cadastros.

**11.20.0 - Geração do SPED Contábil:**

* Foram disponibilizadas duas opções em que o usuário poderá optar por não enviar os Históricos de alteração de contas contábeis para os registros I050 e de contas gerenciais/centros de custos para os registros I100. Se estas opções forem marcadas serão enviadas somente a situação atual dos registros com suas respectivas datas de inclusão. Se esta opção não for marcada, serão enviados para o SPED Contábil todos os Históricos de alterações dos registros existentes na base de dados.
* **Observações:**
  + Não será possível prosseguir na geração do SPED Contábil caso haja no cadastro de Contas Contábeis ou Contas Gerenciais/ Centros de Custos, algum registro em que a Data de Inclusão não esteja preenchida.  Nestes casos serão apresentadas mensagens para o usuário, informando sobre a necessidade destas datas.
  + As contas contábeis que tiverem datas de inclusão maiores que a data final da escrituração gerada não serão enviadas para o registro I050 do arquivo digital, porém,  se para estas mesmas contas existirem movimentação no período da escrituração, estas contas serão enviadas normalmente para o registro I050 com suas respectivas datas de inclusão assim como suas movimentações e, neste caso, como as datas de inclusão das contas são maiores que a data final da escrituração, serão apresentadas Advertências ao validar o arquivo digital no PVA (Programa Validador do SPED Contábil).
  + Caso exista algum Histórico de alteração de conta contábil com data maior que a data final da escrituração gerada, será apresentada Advertência ao validar o arquivo digital no PVA. Neste caso,  se desejado, o usuário pode marcar a opção para não enviar os Históricos de alteração  das contas contábeis ao gerar o arquivo digital. Lembrando que a responsabilidade do envio das informações para o SPED Contábil é do contribuinte.
  + Nunca se pode alterar ou excluir os Históricos de alteração de contas e centros de custos existentes na base, principalmente o último Histórico registrado, pois caso exista algum Histórico, o último sempre é considerado como a situação atual da conta. Se isto acontecer o arquivo digital não será validado.

* Quando a instituição responsável pelo plano referencial for o Banco Central do Brasil (Plano COSIF), ao gerar o arquivo digital as contas do plano referencial (registro I051) não serão enviadas com máscara. Esta é uma exigência do validador do SPED Contábil, pois internamente o validador possui o plano de contas COSIF sem máscara.
* O campo Código do Município dos registros 0000 e 0020 do SPED Contábil estão sendo preenchidos com 7 dígitos. Caso o Código do Município segundo o IBGE esteja cadastrado na base somente com 5 dígitos o sistema irá concatená-lo com o código da UF, carregando assim os 7 dígitos.
* Os lançamentos com efeito Fiscal incluídos na base para geração do SPED FCONT serão totalmente desconsiderados na geração do SPED Contábil. Estes lançamentos serão considerados somente na geração do SPED FCONT, respeitando a data informada para o período de geração.

**11.20.0 - Plano de Contas Paralelo:**

* Implementado o recurso de recolher/expandir todos os itens das listas de contas/centros de custos. Ao clicar com o botão direito do mouse sobre a lista de Contas Contábeis disponíveis, Centros de Custos disponíveis ou Centros de Custos associados serão apresentadas opções que permitirão ao usuário recolher todos os itens da lista ou expandir todos os itens da lista.
* Implementada na aba Associação com Centro de Custo a opção 'Listar Centros de Custos Inativos' que quando marcada disponibiliza na lista os centros de custos inativos, permitindo assim associá-los às contas paralelas.

**11.20.0 - SPED FCONT:**

* Registro I155 - Saldos Periódicos  O registro teve seu conceito alterado, passando a ter o mesmo significado da Escrituração Contábil Digital - ECD. No arquivo do SPED FCONT no registro I155 serão informados os saldos considerando todos os lançamentos contábeis, inclusive os de encerramento, porém serão informadas somente as contas patrimoniais (Ativo, Passivo e Patrimônio Líquido), ou seja, somente as contas que possuem o campo 'Natureza para emissão do SPED' no cadastro de contas contábeis informado como Ativo, Passivo e Patrimônio Líquido é que serão levadas para o registro I155.
* Registro I350 e I355 - Saldo das contas de resultado antes do encerramento.  Este registro será gerado no arquivo do SPED FCONT com o mesmo conceito da ECD. Serão informados no registro I355 os saldos das contas de resultado na data da apuração. Se trimestral, os registros serão informados por trimestre.

**11.20.0 – Consistência de Lançamentos**

O processo de Consistência de Lançamentos foi aperfeiçoado, contemplando mais verificações na base de dados.

**Novo Modelo BackOffice - 11.20.0**

---

  A TOTVS, acompanhando as últimas evoluções tecnológicas, continua a migração do Sistema de Gestão da linha RM para a plataforma .Net da Microsoft. Com novas ferramentas para projeto, análise, desenvolvimento e testes de software, a linha RM ganhará gradualmente um novo padrão visual, mais intuitivo, mais agilidade e novas funcionalidades. Os módulos migrados nesta versão 11.20.0 são:

* - Transferência de Grupos Contábeis
* - Renumeração de documentos
* - Recálculo de Diferença entre Débitos e Créditos

**- Participante**

Ajustado o serviço de contabilização utilizado por outros módulos para que o Participante seja identificado e os lançamentos sejam gerados com o campo 'participante' preenchido automaticamente. Processos ajustados:

* Movimento
* Baixa do lançamento financeiro
* Aplicação Financeira (somente Participante do tipo Filial)

**- Consistência de Lançamentos**

O processo de Consistência de Lançamentos foi aperfeiçoado, contemplando mais verificações na base de dados.
