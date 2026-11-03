---
article_id: 360050375913
category: Contabilidade Gerencial - Escrituração-Contábil-ECD
content_hash: e238a0b46f9758d91c295c810a77e4a1bc11a119674cd889927e65db940623e2
fetched_at: '2026-06-28T22:40:44.667874+00:00'
product: protheus
section_id: 1500001548702
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB - ECD - Geração do Bloco
  K
type: support-article
updated_at: '2026-04-29T18:08:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050375913-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-ECD-Gera%C3%A7%C3%A3o-do-Bloco-K
---

A geração dos saldos contábeis consolidados do Bloco K para conglomerados econômicos no TOTVS Protheus envolve três etapas: cadastro do Bloco K (CTBS420) para informações do grupo, cadastro do Plano de Contas Consolidado (CTBS430) e cadastro dos saldos das contas consolidadas (CTBS440). A carga dos saldos pode ser feita por importação ou manualmente, considerando a consolidação do grupo ou individualmente. Registros K310 e K315 são preenchidos manualmente.

**Dúvida**  
Como realizar a geração de saldos contábeis consolidados dos Conglomerados Econômicos (Bloco K) da empresa controladora a ser escriturada e das demais empresas que compõem o grupo?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial (SIGACTB) - A partir da versão 12

**Solução**  
A configuração engloba três etapas principais de cadastros e a posterior geração da escrituração. Siga os procedimentos abaixo:

1. **Cadastro do Bloco K - Conglomerados Econômicos (Rotina CTBS420)**  
   Esta rotina é responsável pela criação dos cadastros abrangidos pelos blocos K030, K100 e K110.

   * Acesse o módulo de Contabilidade Gerencial (SIGACTB) no menu Atualizações > Escrituração Cont. > Cadastros > Cad. Bloco K - Conglomerados Econômicos (CTBS420).
   * Preencha a Descrição e o Período da Escrituração Contábil Consolidada. Este cadastro irá compor o bloco K030 com o período de início e fim da escrituração.
   * Preencha o Percentual de Participação, Percentual de Consolidação, Data de Início e Data Final da Empresa, e informe caso tenha ocorrido evento. Este passo compõe o bloco K100.
   * Preencha o Código do Evento e a Data do Evento. Isto compõe o bloco K110.
2. **Cadastro Bloco K200 - Plano de Contas Consolidado (Rotina CTBS430)**   
   Esta rotina é responsável pelos cadastros dos blocos K200 e K210.

   * Acesse o menu Atualizações > Escrituração Cont. > Cadastros > Cad. Bloco K200 - Plano de Contas Consolidado (CTBS430).
   * Clique no botão Outras Ações > Importar Plano de Contas.
   * Na tela de parâmetros, selecione o Registro K030 incluído anteriormente, o range de contas a serem importadas, informe se deseja sobrescrever os registros e se deseja amarrar as contas por Grupo de Empresas.  
       
     Na pergunta "Amarra Contas Grp. Empresas ?". Caso a resposta seja “Sim”, o sistema realizará a gravação do bloco K210 para todas as contas analíticas presentes no K200.

     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106505519767)

     OBS.: A rotina CTBS430 permite importar apenas contas já cadastradas no plano (CTBA020). Para inclusão em lote de contas não cadastradas no plano de contas (CTBA020), utilize o Execauto, conforme documentação disponível.  
       
     <https://tdn.totvs.com/pages/releaseview.action?pageId=362453480>
   * É possível realizar a inclusão dos registros K200 e K210 manualmente, ao clicar em "Incluir" na rotina.  
       
     Para alimentar o bloco K210, preencha os campos da seguinte maneira:  
       
     **Cod. Empresa**: preencher conforme informações constantes no cadastro do bloco K100;  
     **Cod. Cta. Emp.**: Replicar o código da conta preenchido no bloco K200.

     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106505522199)

     Ao preencher os campos **Id. Bloco K** ou **Cod. Conta**, o sistema executará um gatilho.  
       
     O comportamento desse gatilho varia conforme o contexto em que for acionado. Em regra, ele realizará o preenchimento do bloco K210 apenas quando os campos **Id. Bloco K** ou **Cod. Conta** estiverem devidamente informados.  
       
     Se o bloco K210 já estiver preenchido e o campo **Cod. Conta** for alterado, o sistema exibirá uma mensagem de confirmação, questionando se o usuário deseja executar o gatilho e sobrescrever os dados existentes na coluna **Cod. Cta. Emp.** do bloco K210.

     + Ao selecionar **“Sim”**, a coluna **Cod. Cta. Emp.** será atualizada com a conta informada no campo **Cod. Conta**, exceto nas linhas alteradas manualmente, que serão preservadas.
     + Ao selecionar **“Não”**, nenhuma alteração será realizada no bloco K210.

     Caso o bloco K210 já esteja preenchido e o campo **Id. Bloco K** seja alterado:

     + Se não houver alterações manuais no bloco K210, o grid será recarregado com os códigos das empresas correspondentes ao novo **Id. Bloco K**.
     + Se houver alterações manuais no bloco K210, o campo **Cod. Conta** e o grid serão limpos.
3. **Cadastro Bloco K300: Saldos das Contas Consolidadas (Rotina CTBS440)**   
   Esta rotina contempla os cadastros dos blocos K300, K310 e K315.

   * Acesse o menu Atualizações > Escrituração Cont. > Cadastros > Cad. Bloco K300: Saldos das Contas Consolidadas (CTBS440).
   * A carga de saldo das movimentações contábeis (alimentando o campo **Valor Aglutinado**) será realizada em dois momentos:

     1. Por meio da funcionalidade **"Importar Saldos Contábeis"**(Outras Ações do Browse):

        ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106505526039)

        O parâmetro **"Posicao Ant. L/P"** permite ao usuário informar se deseja considerar saldo após ou antes da apuração.

        ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106505527575)

        Sim: considera saldo anterior à apuração.  
        Não: considera saldo após a apuração (contas de resultado zeradas).
     2. Por meio da funcionalidade "**Carrega Saldo"**(Outras Ações no formulário de Cadastro):  
          
        ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106483134615)

     Em ambas as opções, existe a pergunta "Imp. Saldos Grp. Empresa ?" para identificar se o saldo carregado será composto por todo o grupo de empresas.

     ![](https://centraldeatendimento.totvs.com/hc/article_attachments/40106483136151)

     Caso a resposta às perguntas acima seja **“Sim”**, o sistema preencherá o registro K300 com o saldo consolidado, considerando todas as contas e empresas cadastradas nos registros K200/K210.  
       
     Se a resposta for **“Não”**, a rotina seguirá o comportamento atual, apresentando apenas o saldo da empresa logada.
   * Ao alimentar os campos de acordo com o resultado obtido no passo anterior, será feita a gravação do bloco K300

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075817053)

**OBS.:** os registros K310 e K315 serão preenchidos manualmente pelo usuário.

***Tabelas utilizadas:***  
*CQQ - Bloco K030*  
*CQR - Bloco K100*  
*CQS - Bloco K110*  
*CQT – Bloco K115*  
*CQU - Bloco K200*  
*CQV - Bloco K210*  
*CQX - Bloco K300*  
  
  
**Saiba mais**  
[Geração do Bloco K - ECD](https://tdn.totvs.com/pages/releaseview.action?pageId=467764151)  
[Tabela e rotina Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013554251-MP-SIGACTB-ECD-SPED-CONTABIL-TABELA-E-ROTINA-Bloco-K?source=search)
