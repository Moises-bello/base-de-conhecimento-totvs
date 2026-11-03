---
content_hash: 10b1de8e10df4db02890f137b0e7f13cc8d3135943879cf6824c5fb7f6dcc4b1
fetched_at: '2026-06-29T00:10:31.136512+00:00'
page_id: '520670320'
product: rm
source: tdn-rm
title: Geração de Fatura SUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520670320
version: 51
---

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Processo Faturamento de AIH, BPA e APAC**
4. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Para gerar uma fatura Sus é necessário acessar a rotina do menu Faturamento/Faturamento SUS/Faturas, e incluir um novo registro. Diferente da versão antiga, é necessário criar o cabeçalho da fatura, para depois executar o processo de Geração do arquivo de faturamento.

O processo de criação da fatura é o mesmo tanto para AIH, BPA e APAC. Após a execução do processo de Geração do arquivo de faturamento, os campos de quantidade de contas e total da remessa serão atualizados, assim como na página "Atendimentos da remessa" serão listados os atendimentos pertencentes à fatura.

## **02. EXEMPLO DE UTILIZAÇÃO**

falseSustrueCriação da fatura

Para se criar o cabeçalho da fatura, selecione a unidade de faturamento e o convênio SUS. Ao salvar o registro, o sistema gera o número da próxima remessa com a data atual.

Após gerar o arquivo de faturamento a página "Atendimentos da Remessa" será preenchida com as contas pertencentes à fatura criada

Processo de Faturamento

Existem três formas de Elaboração de contas para o faturamento do convênio SUS, são elas:

* AIH (Autorização de Internação Hospitalar) – Paciente interno.
* BPA (Boletim de Procedimento Ambulatorial) – Paciente externo.
* APAC (Autorização de Procedimentos de Alta Complexidade) – Paciente interno/externo.

No TOTVS Gestão Hospitalar acesse Faturamento/Faturamento SUS/Processos/Faturamento AIH, BPA e APAC.

Na tela do processo, devem ser preenchidas as seguintes informações:

- Unidade de Faturamento: campo somente leitura, já vem preenchido de acordo com a remessa selecionada.- Opções de faturamento: faturamento, refaturamento, reprocessamento.

- Tipo de faturamento: BPA, AIH, AIH Rejeitada, APAC.

- Filtro por data: campo opcional, caso queira filtrar a seleção de contas as opções são período por data de saída, data final da parcial ou data de liberação.   
Quando utilizar um filtro por data, é obrigatório preencher a data inicial e final. A data inicial não pode ser maior que a final.

- Unidade de Atendimento (opcional).

- Responsável pela Liberação (opcional).

- Informe o Tipo de Faturamento: BPA, AIH, AIH Rejeitada, APAC

- Mês / Ano da apresentação: competência para apresentação do faturamento SUS (obrigatório)

### **Incluir novas Contas**

No segundo passo de refaturamento é possível incluir novas contas como é mostrado abaixo:

Ao clica em incluir novas contas uma tela de pesquisa é aberta:

Dessa forma, o usuário pode incluir contas que foram excluídas de uma outra remessa, por exemplo.

Processo de Refaturamento

Existem três formas de Elaboração de contas para o refaturamento do convênio SUS, são elas:

* AIH (Autorização de Internação Hospitalar) – Paciente interno.
* BPA (Boletim de Procedimento Ambulatorial) – Paciente externo.
* APAC (Autorização de Procedimentos de Alta Complexidade) – Paciente interno/externo.

No TOTVS Gestão Hospitalar acesse Faturamento/Faturamento SUS/Processos/Faturamento AIH, BPA e APAC.

Na tela do processo, devem ser preenchidas as seguintes informações:

- Unidade de Faturamento: campo somente leitura, já vem preenchido de acordo com a remessa selecionada.

- Opções de faturamento: Selecionar a opção refaturamento.

- O Tipo de faturamento (BPA, AIH, AIH Rejeitada, APAC) já é preenchido conforme a fatura selecionada.

- Filtro por data: campo opcional, caso queira filtrar a seleção de contas as opções são período por data de saída, data final da parcial ou data de liberação.   
Quando utilizar um filtro por data, é obrigatório preencher a data inicial e final. A data inicial não pode ser maior que a final.

- Unidade de Atendimento (opcional).

- Responsável pela Liberação (opcional).

AIH

Uma vez selecionada a opção de AIH, o sistema fará a busca das contas de acordo com os filtros informado.

Para a geração da fatura de AIH, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa
* Se o percentual de cesáreas em relação aos partos normais, é menor ou igual ao parâmetro permitido (Parâmetros Sus | AIH | Gerais II | % Cesarianas)

### Faturamento AIH

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento AIH. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta c:/temp chamado SUS.TXT.

### Refaturamento AIH

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento AIH já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo chamado SUS.TXT é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo.

### Reprocessamento AIH

Selecionar a opção reprocessamento AIH

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Observação: Caso a quantidade de cotas não seja maior que 1 a remessa então será cancelada.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Auditoria)
* Retornar Conta para Correção(Faturamento)

As duas opções acima para o SUS tem o mesmo comportamento.

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Auditoria)" ou "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo podemos verificar que as contas foram liberadas, vide imagem abaixo.

BPA

Uma vez selecionada a opção de BPA, o sistema fará a busca das contas de pacientes externos de acordo com os filtros informado.

Para a geração da fatura de BPA, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa

### **Parâmetro "Habilita BPA no Registro de Atendimento externo"**

O parâmetro se encontra em Registro e Controle, como é mostrado na imagem abaixo:

Caso este parâmetro esteja marcado, contas com atendimento, em que o tipo paciente é igual a Interno serão trazidos no grid, como é mostrado abaixo:

Caso contrário, não ser trago os pacientes Internos:

### Faturamento BPA

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento BPA. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo. Um exemplo abaixo é mostrado:

### Refaturamento BPA

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento BPA já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo é gerado na pasta definida no parâmetro SUS: Diretório de Armazenamento do Arquivo.

### Reprocessamento BPA

Para selecionar a opção de reprocessamento com BPA, devemos acessar os seguintes passos:

Acessar Faturamento -> Fatura SUS

Selecionar uma conta e acessar o menu: Processos → Faturamento AIH, BPA, APAC.

Escolher a opção “Reprocessamento” e “BPA”

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Nesse processo será recalculado o valor total da fatura e a quantidade de contas que a mesma possui,

Observação: Caso a quantidade de contas não seja maior que 1 a remessa então será cancelada.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Auditoria)
* Retornar Conta para Correção(Faturamento)

As duas opções acima para o SUS (BPA) tem o mesmo comportamento.

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Auditoria)" ou "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo as contas foram liberadas.

APAC

Uma vez selecionada a opção de APAC, o sistema fará a busca das contas de pacientes externos de acordo com os filtros informado.

Para a geração da fatura de APAC, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa

### Faturamento APAC

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento APAC. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada.

Um arquivo é gerado na pasta definida no parâmetero Diretório de Armazenamento do Arquivo.

### Refaturamento APAC

Para realizar o processo de refaturamento de uma remessa é necessário que a mesma esteja **Faturada**, vide a imagem abaixo.

A opção tipo de faturamento APAC já deverá estar selecionada. Selecionar a opção **Refaturamento**.

Nessa etapa serão exibidas todas as contas que fazem parte da fatura, não é possível realizar alterações.

Após executar o processo podemos notar que a remessa foi refaturada.

Um arquivo é gerado na pasta definida no parâmetero Diretório de Armazenamento do Arquivo.

### Reprocessamento APAC

Para selecionar a opção de reprocessamento com APAC, devemos acessar os seguintes passos:

Acessar Faturamento -> Fatura SUS

Selecionar uma conta e acessar o menu: Processos → Faturamento AIH, BPA, APAC.

Escolher a opção “Reprocessamento” e “APAC”

* Excluir Conta da Fatura

Para excluir uma conta da fatura deve-se selecionar a opção para reprocessamento e selecionar as contas que deseja excluir.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Nesse processo será recalculado o valor total da fatura e a quantidade de contas que a mesma possui.

**Observação:** Caso a remessa só possua uma conta ao remover essa conta da fatura, a mesma deve ser cancelada caso exista uma outra remessa em aberta. Caso não tenha nenhuma remessa em aberta, a remessa que teve a conta removida deve ter seu status modificado para em aberto e a quantidade de contas e valor total de ser zerado.

* Cancelar Fatura

Para realizar esse processo é necessário selecionar a opção "Cancelar Fatura", não deve ser necessário selecionar contas.

Quando selecionada a opção cancelar fatura automaticamente todas as contas devem ser removidas da fatura, para que a mesma seja cancelada.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Para este processo todas as contas que estão na fatura devem ser removidas da fatura.

* Retornar Conta para Correção(Faturamento)

Para realizar esse processo é necessário selecionar a opção "Retornar Conta(s) para Correção (Faturamento)". Neste processo as contas que foram selecionadas serão marcadas como liberadas, para que o usuário possa fazer os ajustes necessários na conta.

Em seguida, no terceiro passo, é mostrado a tela para colocar o motivo do reprocessamento, como é mostrado abaixo:

Após executar o processo as contas foram liberadas, neste processo não deve remover as contas da remessa e o valor da remessa deve manter o mesmo.

AIH Rejeitada

Uma vez selecionada a opção de AIH Rejeitada, o sistema fará a busca das contas de pacientes de acordo com os filtros informado.

Para a geração do faturamento para AIH Rejeitada, o sistema verifica as seguintes condições:

* Se existem contas selecionadas
* Se as contas selecionadas não ultrapassa 999 nessa remessa
* Se o percentual de cesáreas em relação aos partos normais, é menor ou igual ao parâmetro permitido (Parâmetros Sus | AIH | Gerais II | % Cesarianas)

### Faturamento AIH Rejeitada

Para realizar o processo de faturamento de uma remessa é necessário que a mesma esteja em aberto, vide a imagem abaixo.

Devemos selecionar o tipo de faturamento AIH Rejeitada. É obrigatório o preenchimento do mês/ano de apresentação.

Nessa etapa devemos selecionar todas as contas que devem ser incluídas na remessa e serão faturadas.

Após executar o processo podemos notar que a remessa foi faturada, vale ressaltar que a fatura criada será do tipo AIH.

Um arquivo é gerado na pasta definida no parâmetro Diretório de Armazenamento do Arquivo.

**03.** **TABELAS UTILIZADAS**

* SZFATURACONVENIO
* SZATENDIMENTO
* SZPARCIALATEND

Para AIH:

* SZSUSAIHPROD
* SZSUSRECEMNATO
* SZSUSAIHCID
* SZSUSPROCREALIZADOS

Para BPA:

* SZSUSBPALANC
* SZSUSBPAPROD
* SZSUSBPAPRODHIST

Para APAC

* SZSUSAPAC
* SZAPACPROC
* SZAPACMED
* SZAPACNEFRO
* SZAPACNEFROFISTULA
* SZAPACNEFROACOMPDRC
* SZAPACRADIO
* SZAPACQUIMIO
* SZAPACQUIMIO
* SZAPACPOSBARI
* SZAPACPREBARI
* SZAPACBARI
* SZAPACLAUDO
