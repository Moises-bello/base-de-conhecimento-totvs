---
content_hash: 05fe3e23479635e6f6dd06c1602fa9d77f290986986794b412d9e36a212fd356
fetched_at: '2026-06-29T00:08:40.127782+00:00'
page_id: '286210544'
product: rm
source: tdn-rm
title: Como_Fazer_Venda_Importação de Tabela de Preço por Planilha Excel ou .Net
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=286210544
version: 3
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | TOTVS Incorporação 12.1.3 e superiores |
| **Processo** | : | Tabela de Preço – Importação de Planilha .Net |
| **Subprocesso** | : | Importar Tabela de Preço por Planilha e Reajuste de Tabela de Preço por Planilha |
| **Data da publicação** | : | 17/12/2014 |

Este recurso permite ao usuário importar, atualizar ou reajustar tabelas de preço através de planilhas excel ou planilha RM.

Foi criado um novo processo de importação de planilha na visão de tabelas de preços, onde é possível selecionar um arquivo de planilha excel ou planilha RM para importar os preços das sub-unidades(apartamentos). Para a execução deste processo é necessário que tabela de preço esteja “em preparação”.

Foi criado também um novo tipo de reajuste de tabela de preço “por planilha”, onde é possível reajustar uma tabela de preço já existente “efetivada” importando os preços de uma planilha excel ou planilha RM. Será criada uma nova tabela de preço em preparação com os preços reajustados e ao efetivá-la, a tabela de preço anterior será revogada.

## Desenvolvimento/Procedimento

Menu de acesso: Cadastros -> Tabela de Preço

## Processo de “Importar uma nova tabela de preço através de planilha”

Menu de acesso: Cadastros -> Tabela de Preço -> **Importar preço por planilha**

Para criar uma nova tabela de preço através de planilha, na visão de tabela de preço, **sem marcar nenhuma tabela de preço**, o usuário deve executar o processo de “**Importar tabela de preço por planilha**”:

   Nesta tela, o usuário deve informar o nome, empreendimento e data inicial de vigência da nova tabela de preço:

### Formato do arquivo de planilha:

O arquivo da planilha deverá conter os 3 campos que compõem a chave da sub-unidade:

- Código do Empreendimento

- Código da Unidade (Torre)

- Código da Sub-Unidade (Apartamento)

- E o campo do preço da sub-unidade.

Observação: o código do empreendimento e o código da unidade(torre) são necessários para que o sistema possa identificar que o usuário selecionou um arquivo errado e interromper o processo.

**Importante: Devido o sistema não possuir um padrão para o código do apartamento no banco de dados, por exemplo, podemos ter na mesma torre(unidade), um apartamento “102”, “000102” ou “0102”, o código da apartamento na planiha deve ser “exatamente” igual ao código da sub-unidade gravado no banco de dados (considerando os zeros a esquerda).**

Exemplo de um arquivo de planilha com a tabela de preço a ser importada:

**Observação: a próxima linha ao último registro de preço deverá estar em branco, para o que o sistema possa identificar o final do arquivo:**

### Mapeamento das células da planilha

Nesta tela, o usuário deverá informar o arquivo da planilha Excel ou .Net a ser importada e quais as células de onde o sistema deverá buscar as informações dos preços para alimentar a tabela de preço, quais as células do preço base e do preço por metro quadrado da tabela de preço e o nome da planilha. Sendo que os campos preço base e preço por metro quadrado da tabela de preço são **opcionais**.

Caso a célula seja “**fixa**”, como o código do Empreendimento e o código da Unidade, o usuário deverá informar a célula **com cifrão**:

Exemplo: **$C$1**

Caso a célula seja “**variáve**l”, como o código da Sub-Unidade e o preço, o usuário deverá informar a célula inicial **sem cifrão**:

Exemplo: **B10**

Com o objetivo de facilitar o processo de importação de planilhas, o CheckBox “**Manter configuração de importação**” indica que as configurações realizadas nesta tela serão mantidas para a próxima importação de planilha, considerando que todas as planilhas de tabela de preço do cliente tenham o mesmo formato.

## Processo de “Atualizar uma tabela de preço através de planilha”

 Menu Acesso: Cadastros -> Tabela de Preço -> **Importar preço por planilha**

Para atualizar uma tabela de preço “**em preparação**”, o usuário deve marcar uma tabela de preço na visão, com a situação “**em preparação**” e executar o processo de “**Importar preço por planilha**”.

Em seguida, será exibida a mesma tela da página 5 de mapeamento das células da planilha.

## Processo de “Reajustar uma tabela de preço através de planilha”

Menu Acesso: Cadastros -> Tabela de Preço -> **Reajustar tabela de preço**

Para reajustar uma tabela de preço através de planilha, o usuário deve marcar uma tabela de preço “**efetivada**” e executar o processo de “**Reajustar tabela de preço**”:

### Selecionando o tipo de reajuste e as sub-unidades a serem reajustadas

Na tela de reajuste, o usuário deve selecionar o tipo de “reajuste por planilha excel”.

E, depois, o usuário deve selecionar quais as sub-unidades(apartamentos) serão importadas do arquivo de planilha na tabela de preço.

**Observação**: será criada uma nova tabela de preço “em preparação” com os preços das sub-unidades marcadas.

Caso seja marcado o CheckBox “Efetivar automático”, a tabela de preço será automaticamente efetivada e a tabela de preço corrente será revogada.

Em seguida, será exibida a mesma tela da página 5 de mapeamento das células da planilha.

## Informações Adicionais

Não se aplica.

#### Informações Técnicas

|  |  |
| --- | --- |
| **Tabelas Utilizadas** | XTABPRECO  XTABPRECOSUBUNIDADE  XTABPRECOREAJUSTE  XTABPRECOHISTORICO |
| **Funções Envolvidas** | Processo de Importação de Tabela de Preço por Planilha  Processo de Reajuste de Tabela de Preço por Planilha |
| **Sistemas Operacionais** | Windows 7 SP1 ou Superiores |
