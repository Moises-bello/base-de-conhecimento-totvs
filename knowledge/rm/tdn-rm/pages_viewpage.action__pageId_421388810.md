---
content_hash: 666ded5fabde64a286aff849bc434bf1f6b6e38c69e7166ac9313bfa13b7d4c4
fetched_at: '2026-06-29T00:09:19.181463+00:00'
page_id: '421388810'
product: rm
source: tdn-rm
title: Dados Adicionais - Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388810
version: 5
---

Nesta pasta são apresentadas informações adicionais ao registro de extrato de caixa.

Centro de Custo

A obrigatoriedade desta informação é validada pela funcionalidade do parâmetro "Centro de Custo obrigatório" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos | etapa Extrato de Caixa).

Departamento  
Escolha o departamento da filial escolhida para o extrato de caixa, o campo não é obrigatório..  
   
Natureza Orçamentária Financeira   
Escolha a natureza orçamentária para o extrato de caixa, o campo não é obrigatório.

Meio de Pagamento

Campo Informativo. O sistema apresenta a forma de pagamento utilizada na baixa de lançamento através do módulo de "Sessão de Caixa".

Tabelas Opcionais

São apresentadas as tabelas opcionais cadastradas. O cadastro das tabelas e obrigatoriedade são de acordo com os parâmetros "Usar Tabelas Opcionais" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos  | etapa Tabelas Opcionais).

Tipo Contábil

Na inclusão de um novo registro a opção para este campo é apresentada por default de acordo com o parâmetro "Default Contábil no Extrato" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos | etapa Contabilização do Extrato de Caixa), que pode ser alterado conforme necessidade.

Contabilização

Ao clicar neste botão é apresentada a janela de contabilização do registro, nesta janela são apresentadas informações sobre a contabilização do registro.  
*Evento Contábil*: esta informação pode ser apresentada por default se você utilizar "Tabela Opcional" no parâmetro "Tabela Default para Evento" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos | etapa Contabilização Financeiro) e incluir um "Evento Contábil" no campo "Evento Contábil para Extrato" da pasta "Evento Contábeis".  
Para definir o preenchimento do Default para Evento contábil, bastar salvar um evento contábil que fica na Contabilização no extrato de caixa e em seguida clicar com o botão direito no campo Evento Contábil escolher a opção "Valor Default" e selecionar a opção "Usar como Default".

Observação: quando são realizadas alterações por parte do usuário nas partidas geradas pelo evento contábil, o mesmo é mantido na contabilização mas permite limpar seu valor e salvar.

**Observações**

Caso a contabilidade estiver integrada ao lote oficial (Lote zero), o tipo contábil do extrato só poderá ser alterado se a operação contábil for excluída.

Para este processo, acessar a visão de extratos e ir em Processos | Regerar Contabilização e após a conclusão executar a exclusão da operação contábil em Processos | Solicitar Exclusão Operação contábil. Ao fim do processo de exclusão, acessar o Gestão Contábil no menu Utilitários | Tarefas | Gerenciador, selecionar a Tarefa desejada e ir em Processos | Executar Tarefa.

Após executar este procedimento o extrato poderá ter seu Tipo contábil alterado.

Data de Contabilização

Esta data já é apresentada por default de acordo com o parâmetro "Data Default do Extrato – Contabilização" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos | etapa Contabilização do Extrato de Caixa).

Valor Contábil

O valor contábil poderá ser diferente do valor do extrato quando for utilizada uma Conta/Caixa que possua moeda que não seja a corrente.

**Exemplo**

Ao incluir um extrato utilizando uma Conta/Caixa que possua a moeda Dólar, o valor do extrato será em Dólar e a contabilização será em Reais. Desta forma, o sistema permitirá a inclusão do extrato com valor diferente.

**Observação:**

Para incluir informações contábeis nos registros que possuem a Operação "Saque CPMF", inclua um Evento Contábil no parâmetro "CPMF – Evento Contábil" (Parâmetros | Assistente de Implantação de Processos | Controle Bancário | Manutenção de extratos | etapa Contabilização do Extrato de Caixa).  
   
**Dicas**

Para que as informações contábeis sejam incluídas corretamente, com segurança e com mais agilidade, utilize as diversas funcionalidades oferecidas pelos "Eventos Contábeis" (menu Cadastros). Através dos eventos contábeis você realiza de forma automática a inclusão das informações contábeis, podendo criar várias combinações, buscar defaults de vários cadastros e muito mais. Leia as informações sobre o "Cadastro de Evento Contábil" e aprenda como utilizar essa excelente funcionalidade.

Controle Orçamentário

Efeito sobre o orçamento Há três opções disponíveis: nenhum efeito orçamento, aumenta valor realizado ou diminui valor realizado.

Grupo Orçamentário Selecione o grupo orçamentário para o extrato de caixa.

**Livro de Caixa Digital do produtor rural**

Tipo de Lançamento no LCDPR

Disponibilizadas opções de  despesa ou receita para preenchimento do campo:

1. Receita da Atividade Rural
2. Despesas de custeio e investimentos
3. Receita de produtos entregues no ano referente a adiantamento de recursos financeiros

Classificação do Lançamento no LCDPR

Disponibilizadas opções de formas de classificação para o extrato:

1. Nota Fiscal
2. Fatura
3. Recibo
4. Contrato
5. Folha de Pagamento
6. Outros

CPF/CNPJ do Participante

Disponibilizado campo para informar CNPJ/CPF quando houver participante.
