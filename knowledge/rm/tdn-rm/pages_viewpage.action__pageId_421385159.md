---
content_hash: c86860db6562d6068f558da2acc47b6613948a8dcc9c1e4d43c7d38dde3845cb
fetched_at: '2026-06-29T00:09:14.228230+00:00'
page_id: '421385159'
product: rm
source: tdn-rm
title: Liberação de Período no FLUIG
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385159
version: 3
---

---

É a liberação do período de contrato que pode ser para pagamento, suprimento ou somente sinalizar o fim do período.

O acesso à Liberação de Períodos se dá através das páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" e está disponível em cada período do contrato nas seguintes opções:

* Liberar para Suprimento/Faturamento
* Liberar para o TOTVS Obras e Projetos;
* Liberar para o Financeiro.

A página de Liberação de Período de Contrato contém três abas:

**Aba de Liberação para o TOTVS Obras e Projetos:**

Nessa aba, temos os seguintes campos e suas funções:

* **Valor da Medição:**
* **% reajuste:** Percentual que pode ser informado para reajustar a medição do período na liberação;
* **Com reajuste:**Valor da liberação aplicado o percentual de reajuste;
* **Sem reajuste:**Valor se o reajuste aplicado;
* **Valor Retido/Deduzido/Adiantado no Período:**Valor total da retenções, deduções e adiantamentos no período. Este campo estará habilitado somente se não existirem deduções, retenções, e no caso de existir os valores e percentuais devem estar zerados;
* **Valor Retido no Item:** Valor da retenção informada na medição do período;
* **Valor Retido Total:** Valor da soma da retenção informada na medição do período e da retenção informada na liberação do período;
* **Total da Liberação:** Valor total da medição adicionando o reajuste e subtraindo a retenção.
* **Reajustes:** Uma tabela com um cadastro de reajuste informado no cadastro do contrato;
* **Deduções:** Utilizado para informar os tipos e valores de deduções do período. Existe, também, a opção para informar os produtos faturados à dedução onde a dedução deverá ser associada.
* **Retenções:** Utilizado para informar os tipos e valores de retenções do período;
* **Adiantamentos:** Utilizado para informar os tipos e valores de adiantamentos do período;
* **Campos Complementares:**Possui os campos complementares cadastrados no Menu Cad. Gerais | Campos Complementares | Detalhamento Medição. (Não disponível nesta versão);
* **Observação:**Observação da liberação.

**Aba de Integração Financeiro**:

Esta aba somente estará disponível se o projeto estiver integrado com o Financeiro RM e não integrado com o Financeiro Protheus**Identificação**;

* + **Código Cliente/Fornecedor:** Permite informar o Cliente ou Fornecedor em questão, o cliente/fornecedor do contrato é automaticamente exibido.
  + **Tipo Contábil:** Permite informar qual o tipo contábil do Lançamento que será gerado no Financeiro.
  + **Tipo Documento:** Permite informar qual o tipo de documento do Lançamento que será gerado no Financeiro.
  + **Conta Caixa:** Permite informar qual a conta caixa do Lançamento que será gerado no Financeiro.
  + **Tipo de Lançamento:** Permite informar o tipo do Lançamento que será gerado no Financeiro (Rateio de Centro de Custo e Rateio de Departamento).
  + **Gerar Lançamento no Financeiro com Rateio de Centro de Custo;**
  + **Gerar Lançamento no Financeiro com Rateio de Departamento;**
  + **Campos Opcionais de Valores:**Permite informar os valores dos Campos Opcionais de Valores parametrizados no Financeiro;
  + **Datas Opcionais:** Permite informar as datas parametrizadas no Financeiro;
  + **Tabelas Opcionais:** Permite informar as tabelas opcionais parametrizadas no Financeiro;
  + **Campos Opcionais Alfa:** Permite informar os campos opcionais Alfas parametrizados no Financeiro.
  + Suprimento/Faturamento: esta funcionalidade está detalhada em um outro documento.

Além das abas citadas, a página de liberação contém a Data de Liberação que será a data considerada na liberação do período, a opção de apenas Salvar as informações sem liberar o período, nesse caso apenas as informações da aba "TOTVS Obras e Projetos" serão salvas e a opção de liberar o período com todas as opções selecionadas. Se o período já estiver liberado a mensagem "O período selecionado já se encontra liberado." será exibida na parte superior da página e apenas a opção de Voltar estará disponível.

**Cancelar Liberação do Período**

A funcionalidade de Cancelar Liberação do Período também está disponível nas páginas de "Medição de Item de Contrato" e "Consumir Objetos do Contrato" juntamente com as opções de liberação. Ao selecionar essa opção uma pergunta será exibida, questionando se realmente o cancelamento é necessário, onde ao confirmar, a liberação do período será cancelada.

Todas as ações de liberação e cancelamento da liberação, serão refletidas na MDI e dessa forma, todas as validações de segurança também serão respeitadas no FLUIG.

**Workflow de Liberação de Período de Contrato**

**Parâmetros Gerais**

No Menu | Projeto | Agrupador Parâmetros | Construção e Projetos | Gerais, escolha a aba chamada "Fluig" nos parâmetros gerais do TOTVS Obras e Projetos. Escolha a aba inferior Liberação de Período para configurar o workflow. Esta aba contém três parâmetros, sendo: um para definir o processo relativo ao workflow de Liberação de Período de Contrato, mais um para definir quais os estados do workflow que determinam que o mesmo esteja aprovado e um terceiro para definir quais os estados do workflow que determinam que o mesmo esteja reprovado.

**Parâmetros de Projeto**

Na aba "Integração FLUIG" em "Projeto | Agrupador Parâmetros | Construção e Projetos | Projeto", pasta "Integração | Integração Fluig" foram adicionados os seguintes parâmetros: "Integração Fluig" que deve é inicializado desmarcado para um novo Projeto. "Contrato a Pagar - Liberar Período" e "Contrato a Receber - Liberar Período" que são inicializados desmarcados e habilitados somente se o parâmetro "Integração Fluig" estiver marcado. Marque os parâmetros acima caso deseje trabalhar com aprovação via Workflow Fluig para os contratos do tipo à pagar e/ou à receber, respectivamente.

**Processo de Liberar Período**

Ao clicar em "Executar", o sistema inicia o workflow para aprovação no Fluig. Devem ser considerados os parâmetros de projeto para o tipo de contrato (pagar ou receber). O workflow referente a este processo, é definido na aba "Fluig" dos parâmetros gerais do projeto em "Workflow Fluig". O identificador do workflow é armazenado para permitir a consulta no Fluig e para realizar a liberação de processos. Esta informação pode ser visualizada no anexo "Fluxo de Aprovação Fluig" na visão de Contratos do TOTVS Obras e Projetos.

Quando este processos for executado, será disparado o gatilho que gera o formulário com as informações do período, gerando workFlow de liberação do período de contrato..

Enquanto o workflow não receber o status de Aprovado ou Reprovado,não será possível realizar mais nenhuma alteração no período. A menos que o workflow seja cancelado no Fluig, ou em processos  internos, listado no anexo de ‘Aprovar Liberação de Período no Fluig’ .

A medição e os processos serão bloqueados enquanto o workflow estiver pendente e será impresso uma mensagem amigável informando ao usuário o motivo do bloqueio.  Também sendo possível identificar através de imagens ou colunas, que o período está aguardando o resultado do workflow.

 Se o status do Workflow esteja diferente de APROVADO, o sistema irá desabilitar os campos de "Liberar TOTVS Obras e Projetos" e "Enviar para financeiro". Caso esteja com status APROVADO, o sistema habilitará os campos antes citado e o usuário poderá liberar o período obedecendo também as regras atuais para a liberação. Caso o usuário modifique o valor a ser liberado o Workflow atual será cancelado e será gerado um novo Workflow para o período.

**Cancelamento de Liberação**

Com o projeto marcado para utilizar integração Fluig, quando realizar um cancelamento de liberação do período de contrato, o processo deverá cancelar o workflow caso exista e esteja pendente de aprovação.

**Gerar integração com Suprimentos / Faturamento**

Com o projeto marcado para utilizar integração Fluig ao executar este processo, o sistema valida a existência e situação do workflow de aprovação. O sistema emite uma mensagem informando ao usuário que o processo não poderá ser executado, caso não exista um workflow APROVADO.

**Anexo Fluxo de Aprovação Fluig - Liberar Período**

Anexo "Fluxo de Aprovação Fluig - Liberar Período" na visão de Contratos. Com o projeto marcado para utiliza integração Fluig este anexo exibe os workflows criados para cada período do contrato, além de verificar o status atual do workflow no servidor do Fluig.  
   
   
   Veja Também

---
