---
content_hash: 41c250129db92e612865c24ccf715ca2451f67f03dfad15e604acbbc9d47d4b8
fetched_at: '2026-06-29T00:05:56.965847+00:00'
page_id: '160105553'
product: rm
source: tdn-rm
title: Criando uma nova atividade de Fórmula visual
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160105553
version: 26
---

# **Objetivo**

---

        Demonstrar o que é necessário para realizar a criação de uma nova atividade de fórmula visual.

**Como Funciona**

---

Para criação de uma nova atividade de Fórmula Visual são necessários os seguintes passos:

1. Referenciar as DLLs "**RM.Lib.dll**,**RM.Lib.WinForms.dll**e**RM.Lib.Workflow.Activities.dll**" ao projeto.

   |  |
   | --- |
2. A classe implementada deve herdar da classe **RMSActivity,**ou outra herança desta, como RMSDynamicActivity.

   |  |
   | --- |
3. Implementar sua regra de negócio internamente ao método "Execute", a ser sobrescrito (override).

          No Exemplo abaixo demonstra uma classe que executa um **processo**

           Exemplo:  

         Exemplo de como utilizar um **DataServer** através da atividade

         No Exemplo abaixo é executado um **ReadView** do DataServer Informado.

            Exemplo:  

        4. Manipulando um dataServer de metadados via atividade customizada:

O código exemplo abaixo utiliza as funcionalidades do dataServer para manipular uma tabela de Metadados.  
Foram utilizados os recursos de **ReadView** (para leitura da lista de registros da tabela de metadados),  
**ReadRecord** (para leitura de um registro do metadados) e **SaveRecord** para enviar os dados para o dataServer do metadados.

Foram simuladas as operações de inclusão de um novo registro, alteração do registro existente e exclusão registro em questão.

Esse exemplo foi criado utilizando um dataServer simples criado através do recurso de Metadados do RM.   
Lembrando que ao utilizar esse mesmo exemplo com algum outro dataServer do RM, poderão existir particularidades que impeça correto funcionamento do exemplo.  
Logo, não garantimos que o exemplo se aplicará em qualquer dataServer do RM.   
Lembrando também que a construção de uma atividade customizada é de total responsabilidade do cliente.

Atenção

Ao executar o SaveRecord os registros serão, Inseridos, Atualizados ou Removidos de acordo com o rowState do DataSet informado no SaveRecord.

Para a compilação e execução deste projeto pode ser necessário seguir os passos:

1. Atualizar as referências das DLLs do RM Utilizadas "**RM.Lib.dll**, **RM.Lib.WinForms.dll** , **RM.Lib.Workflow.Activities.dll, RM.Mov.Processos.Intf"** com o caminho das mesmas direcionando para o local da Biblioteca RM.
2. Efetuar "Clean Solution"
3. Efetuar o "Build Solution" em modo **Release**.
4. Copiar a DLL "Gerada" para a pasta da Biblioteca RM.
5. Efetuar o cadastro da Atividade de Fórmula Visual acesse o menu ,,, clique no botão Incluir, será exibida a seguinte tela.

   | Preencha os campos    Nome da Classe:  RM.Spx.Exemplo.Activities.CancelarMovimentoActivity  Nome do Assembly: RM.Spx.Exemplo.Activities | Após salvar a atividade estará disponível para utilização. |
   | --- | --- |

Observação

**Ao retirar a dll referente à atividade criada, da pasta, onde os binários estão localizados, [RM.Net], por exemplo,** **da próxima vez que a fórmula visual for executada, apenas as atividades válidas, ou seja, apenas as atividades vinculadas** **às dll's existentes na pasta [RM.Net] serão efetivamente executadas. Ao abrir uma fórmula visual será observado, que apenas as** **atividades válidas estarão presentes no design da mesma.**

**Desta forma não temos como garantir o correto funcionamento da fórmula visual, caso a dll de alguma atividade seja retirada** **da pasta [RM.Net].**

Para maiores informações:

****[@FRAMEWORK](http://fluig.totvs.com/portal/p/10097/subject/rframework)****

**Canais de Atendimento**

**Chamado:** Através do Portal TOTVS - [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2-2-3-9-5 (Framework) ou 2-2-3-9-4 (BI)

|  |  |
| --- | --- |
| **Produto** | Framework |
| **Versão** | 11.82.XX e 12.01.XX |
| **Processo** | Fórmula Visual |
| **Subprocesso** | Criando uma nova atividade |

|  |  |
| --- | --- |
| Status do Documento: | Produção |
| Data: | 04/09/2014 |
| Versão: | 11.82.XX e 12.01.XX |
| Versão Anterior: | 11.82.XX e 12.01.XX |
| Autores: |  |
