---
content_hash: a564dee4e34f662020924b80e367691d9e6bd9d63269eb60d067a542bb4d688f
fetched_at: '2026-06-29T00:10:45.722670+00:00'
page_id: '553339200'
product: rm
source: tdn-rm
title: RascunhosInstrução de Trabalho | Processo Piloto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=553339200
version: 1
---

5%90%ATENDIMENTO10%90%

**Demandas de Piloto avaliadas pela área de Atendimento**

1. **Identificação do Piloto no *Ticket***
   1. Na **Análise do *Ticket*** a área de Atendimento **deve preencher o campo Origem** com a informação **Cliente beta ou piloto**. Esta informação poderá ser consultada pela área de Desenvolvimento na *Issue* por meio da aba Zendesk.
2. **Demanda de Piloto**
   1. Caso a área de Atendimento não tenha recebido repasse da área de Desenvolvimento, deve transferir a demanda para área de Desenvolvimento.
   2. Caso a área de Atendimento já tenha recebido repasse da área de Desenvolvimento, poderá:
      1. Resolver a demanda do Cliente.
      2. Acionar a área de Desenvolvimento para apoiá-los em caso de dúvidas.
      3. Priorizar os *tickets* de piloto conforme alinhamento realizado com a área de Desenvolvimento.
      4. Encaminhar a demanda para a área de Desenvolvimento quando tratar-se de uma manutenção ou melhoria.

**Transferir demanda para área de Desenvolvimento**

1. **Criar *Issue* no JIRA**
   1. A área de Atendimento deve **criar uma *Issue* no Projeto da *SQUAD***.
2. ***Issue Types* utilizadas**  
   1. Analisar a demanda aberta pelo Cliente e informar a *issue type* relacionada ao assunto.   
      1. **Apoio - Cliente:** deve ser utilizada para explicar o processo piloto ao Cliente ou esclarecer alguma dúvida.
      2. **Manutenção:** sugere-se que seja utilizada para correção de erros identificados no Cliente.
      3. **Story:** sugere-se que seja utilizada em melhorias identificadas no Cliente.
DESENVOLVIMENTO10%90%

1. **Cadastrar EPIC para Piloto**  
   1. Sugere-se que seja **criado um novo EPIC** para vincular as *Issues* registradas durante o Piloto. Facilita a gestão e o controle deste processo.
   2. Porém, pode ser utilizado o **EPIC do desenvolvimento** que já estava sendo utilizado pela equipe para vincular essas novas demandas. Fica a critério de cada Equipe.
2. ***Issue Types* utilizadas (Checar / Informar)**
   1. **Apoio - Cliente:** deve ser utilizada para explicar o processo piloto ao Cliente ou esclarecer alguma dúvida.
   2. **Manutenção:** sugere-se que seja utilizada para correção de erros identificados no Cliente.
   3. **Story:** sugere-se que seja utilizada em melhorias identificadas no Cliente.
   4. Pode ser utilizada a *issue type* **defeito** para realizar a correção dos erros identificados no Cliente. Porém, desta forma não é possível diferenciar os erros encontrados pelo Cliente (externo) dos erros encontrados pela Equipe (interno).
   5. Caso sejam abertos defeitos, pode ser utilizada a *issue type Story* para vincular essas *issues*. Lembrando que a *issue type Story*, não encerra o *ticket* (caso possua algum vinculado).
   6. Para casos em que o cliente registrou uma demanda que já está prevista, sugere-se utilizar a **associação** nas **issue types** de ****Manutenção e *Story.*****
3. **Identificação do Piloto na *Issue***
   1. Ao avaliar a Demanda transferida pela área de Atendimento ou criar uma *Issue*, a área de desenvolvimento poderá preencher o **campo Piloto = Sim / Não** para facilitar na identificação das *Issues* de Piloto.
   2. Na aba Zendesk poderá ser consultado o **campo Origem = Cliente beta ou piloto.** Esta informação deve ser preenchida pela área de Atendimento.
4. ****Documentação do Produto****   
   Durante o Processo Piloto continua sendo obrigatório gerar a Documentação do Produto para o Cliente. Atentar-se as orientações:
   1. ****Novo produto / módulo:**** Documento de Referência.
   2. **Nova funcionalidade em módulo existente:** Documento de Referência + o Documento Técnico.
   3. ***Issues* de piloto abertas para correção de erros:** as documentações devem ser atualizadas se necessário.
   4. Quando criada a documentação no TDN restringir a visualização, gerar um PDF e enviar para o Cliente validar junto com a funcionalidade.
   5. Caso o contrato com o Cliente defina uma forma diferente de entrega deve ser realizado um alinhamento com a Engenharia Corporativa.
5. **Repasse**
   1. A área de Desenvolvimento pode optar por realizar o repasse para a área de Atendimento antes de iniciar o Piloto.
      1. Esta prática ocorre nos casos em que a funcionalidade já foi liberada ao mercado ou somente para alguns Clientes.
      2. A área de Desenvolvimento pode aproveitar o piloto para capacitar a área de Atendimento e trabalhar em parceria no Atendimento dos *tickets*.
   2. É responsabilidade da área de Desenvolvimento alinhar com a área de Atendimento a priorização dos *tickets* de Piloto.
   3. A área de Atendimento pode solicitar apoio da área de Desenvolvimento para solucionar um *ticket* de Piloto.
6. **Comunicação com o Cliente**
   1. Pode ser realizada por meio do botão **Comunicação com Cliente** na *Issue* do JIRA. Esta opção está disponível somente em *Issues* que possuem *Ticket* vinculado.
      1. **[Instrução de Trabalho - Como Fazer Comunicação com o Cliente, TOTVER ou Analista do Suporte no JIRA?](http://tdn.totvs.com/x/YLO1HQ)**
   2. Acionamento direto ao Analista do Desenvolvimento.
   3. Report: o Cliente pode solicitar um report do projeto ou da funcionalidade que está pilotando. Este item é opcional e deve ser realizado conforme acordo com o Cliente.
   4. E-mail.
   5. Skype.
7. **Liberação do Pacote para o Cliente**
   1. Na *issue type* Manutenção está disponível o botão para realizar **Liberação Emergencial**.
   2. Na *issue type Story* está sendo avaliada a opção de **Liberação Emergencial.** *Este item será tratado com o GCAD de todos os sites.*
8. **Solicitar Aceite do Cliente (Opcional)**

   1. Sugere-se que a área de Desenvolvimento solicite aceite do Cliente referente a conclusão do Processo Piloto.
   2. É importante que este alinhamento ocorra por parte do Cliente e da TOTVS.
   3. Não existe um artefato padrão para ser utilizado na formalização deste aceite, pode ser registrado por e-mail ou utilizado outro documento do segmento.
   4. Caso ocorra esta formalização, sugere-se que a evidência do aceite seja anexada ao *EPIC* no JIRA.
9. **Implantação da Funcionalidade no Cliente (*em desenvolvimento*)**  
   1. A área de desenvolvimento pode subcontratar a área de Serviços para implantar uma funcionalidade mais complexa no Cliente.
   2. Neste caso, a área de serviços seguirá a MIT - Metodologia de Implantação TOTVS.
   3. Para os casos onde implantação da funcionalidade é realizada pela área de desenvolvimento, iremos em breve definir com o segmento os artefatos necessários e incluir orientações no Processo Padrão.
CLIENTE10%90%

1. **Comunicação com a TOTVS**
   1. Abertura ou Retorno de Informações por meio do *ticket* no Portal do Cliente.
   2. Acionamento direto ao Analista do Desenvolvimento.
   3. Acompanhamento por meio de Report.
   4. e-mail.
   5. Skype.
2. **Aceite do Cliente (Opcional)**
   1. Sugere-se que o Cliente formalize seu Aceite referente a conclusão do Processo Piloto com a TOTVS.
   2. Para este aceite não existe um artefato padrão, pode ser registrado por e-mail ou utilizado outro documento do segmento.
5%
div.theme-default .ia-splitter #main {
margin-left: 0px;
}
.ia-fixed-sidebar, .ia-splitter-left {
display: none;
}
#main {
padding-left: 10px;
padding-right: 10px;
overflow-x: hidden;
}
.expand-control-text {
color: #000000;
font-size: 13px !important;
font-weight:bold !important;
}
.expand-icon, .aui-icon, .aui-icon-small, .aui-iconfont-chevron-right {
color: #FF8000;
}
.aui-header-primary .aui-nav, .aui-page-panel {
margin-left: 0px !important;
}
.aui-header-primary .aui-nav {
margin-left: 0px !important;
}
]]>
