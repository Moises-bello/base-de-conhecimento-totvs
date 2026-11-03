---
article_id: 360012517431
category: Cadastros
content_hash: eb1da93d013ac85b59caaa52f598bb5f3c95567383c5556301efd3dd5a1ff0e0
fetched_at: '2026-06-28T22:46:28.545656+00:00'
product: rm
section_id: 1500000861582
source: central-rm
title: RH - RM - PTO - Exclusão de funcionários admitidos no período atual
type: support-article
updated_at: '2025-02-21T16:37:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012517431-RH-RM-PTO-Exclus%C3%A3o-de-funcion%C3%A1rios-admitidos-no-per%C3%ADodo-atual
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16503061929623) Tempo aproximado para leitura: 00:01:12 min  
  
Dúvida**Como realizar a exclusão de funcionários admitidos no período atual?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80  
  
**Solução**Através do Processo de **Exclusão de Funcionários** o usuário poderá excluir um funcionário do cadastro desde que tenha sido admitido no mês atual e não possua movimentação lançada na Ficha Financeira e/ou no espelho de ponto.

Ou seja, o sistema permite a exclusão de funcionário com a situação **A-Ativo** e data de admissão dentro da competência/período atual ou a situação **Z-Admissão próximo mês** e com data de admissão superior ou igual a competência/período atual.

Para realizar a exclusão de funcionário, as vezes é necessário **limpar as tabelas do módulo de Automação de Ponto** caso o funcionário tenha sido incluído para utilizar cartão de ponto, já tenha algum registro de cálculo, ou seja, ja tenha criado algum tipo de relacionamento no ponto**.** Abaixo segue os passos de como realizar a limpeza:

1. Acesse no Automação de Ponto, o menu **Cadastros | Funcionários**, selecione a chapa desejada e acesse o espelho de pono. Ao abrir visão do espelho de ponto, acesse a opção **Processos | Parametrizar sindicato,** ao abrir o assistente, avance até a etapa **Cálculo** e **desmarque** a flag do **Calcula funcionário sem movimento.** Avance as demais etapas até concluir.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30146464349207)
2. Após alterar a parametrização do sindicato do Automação de Ponto, ainda dentro da visão do espelho de ponto do funcionário, **efetue um recálculo** para caso ja tenha sido gerado ocorrências e movimentações seja limpo os registros. O recalculo deve ser o selecionando parâmetros, marcando todas as opções.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30146464354327)
3. Ainda na visão do espelho de ponto acesse o menu **Processos | Cancelar movimento** e confira os seguintes parâmetros: **Seleção de funcionários:** Esteja selecionado a chapa desejada.  
   **Seleção de datas:** Os campos **Início** e **Fim** devem estar preenchido com as datas do período de início e fim do Automação de Ponto, corresponde a data de admissão e este período deve estar com status de atual/ativo.  
   **1-Tipo Pessoa:** Funcionário   
   **2-Status:** Todas as opções marcadas  
   **3-Tipo batida:** Todas as opções marcadas  
   **4-Movimento:** Todas as opções marcadas  
   **5-Após Cancelamento:** Nao marque nada  
   **6-Justificativa**: Informe o motivo do cancelamento do movimento.  
   Após definir a parametrização execute o processo, ao aparecer a mensagem:   
     
   *Todas as batidas selecionadas serão excluídas. Confirma cancelamento?*Clique em **sim**.    
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30146496299159)  
     
   Após executar o processo, a mensagem: **Chapa XXXXX habilitada a exclusão**, será apresentada no log do processo.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30146464357271)
4. Após executar todos os passos, realize a exclusão do funcionário através do botão **Exclusão de funcionário**.  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/30146464359447)

**Importante:**

* Caso exista outra tabela relacionada ao funcionário excluído, o sistema apresentará uma mensagem no log e abortará o processo, para o usuário excluir o relacionamento manualmente.
* Ao processar a exclusão o sistema armazenará alguns dados do funcionário excluído, isso será necessário porque a ficha de registro é sequencial, e para que não fique um intervalo entre o nº das fichas de registro e não gere questionamentos pelo fiscal do trabalho.  
  Os dados serão armazenados na tabela PFUNCEXCLUIDO.
* Ao excluir um funcionário, será gerado o Evento de Exclusão **S-3000** para o e-Social.

**Saiba mais**  
Para maiores informações sobre o processo de exclusão de funcionários, acesse a documentação [Exclusão de Funcionários](https://tdn.totvs.com/pages/releaseview.action?pageId=452719229).
