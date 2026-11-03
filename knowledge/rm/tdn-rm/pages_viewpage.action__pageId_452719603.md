---
content_hash: 5aa3f3d2670259b527a919d23dc556934d866386e114d5363d3096d67348a15b
fetched_at: '2026-06-29T00:10:08.904565+00:00'
page_id: '452719603'
product: rm
source: tdn-rm
title: Requisição de Desligamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719603
version: 8
---

**Requisição de Desligamento**

---

Este tipo de requisição tem por objetivo autorizar a demissão individual de funcionários ou regularizar a situação de ex-funcionário (com demissão na competência atual/posterior e antes da obrigatoriedade do uso desta requisição). Poderá ou não ser gerada uma requisição de substituição para a vaga em questão

**Passos para criar uma Requisição de Desligamento:**

**1º Passo:** Criar uma Requisição pelo módulo Gestão Organizacional | Requisição de Desligamento.

**2º Passo:** Preencher os campos disponíveis. Para saber as particularidades dos campos, clique aqui. (link do help Pasta Identificação – Requisição de Desligamento)

**3º Passo:** Aprovar/Reprovar a Requisição. Se a Requisição for aprovada e o flag "Gerar Substituição" estiver marcado, será gerada uma Requisição de Substituição, com os dados do funcionário que será demitido.

**4º Passo:** Demitir o funcionário, concluindo a Requisição. Este procedimento pode ser realizado de duas formas: No Totvs Gestão de Pessoas, através do menu Recrutamento | Demissão. No Totvs Folha de Pagamento, caso exista licença deste produto, pelo menu Cadastros | Funcionários, após selecionar o funcionário e clicar no ícone "Rescisão".

**Observação:**

- Pelo processo de "Cancelamento da rescisão", existente no Totvs Folha de Pagamento, a requisição de desligamento irá adquirir o status "Cancelado" ou "Retornado ao status anterior".

* Nos processos de rescisão coletiva, no Totvs Folha de Pagamento, se o parâmetro de requisição de desligamento obrigatória estiver marcado e existir requisições criadas/aprovadas para os funcionários, as requisições serão concluídas. Caso contrário, a rescisão coletiva não poderá ser efetuada até que se crie/aprove as requisições ou desmarque o parâmetro de requisição de desligamento obrigatória.
* Pode ser realizada uma Requisição de Desligamento para um ex-funcionário. Ao selecionar um ex-funcionário, os campos "Previsão", "Dias de Aviso", "Tipo de demissão" e "Motivo da demissão" serão preenchidos com os respectivos dados da rescisão do funcionário, não podendo ser alterados. Essa requisição será gerada com o status "Concluída".

* O sistema notificará quando for criada uma Requisição de Desligamento para um funcionário que possui estabilidade da CIPA e/ou for Portador de Necessidades Especiais. Como forma de acompanhamento dos processos relacionados à requisição serão enviados e-mail´s com mensagens padronizadas, podendo ainda optar-se pela notificação ao gestor de RH e ao gestor do departamento pessoal. Todo o processo de notificação poderá ser parametrizado no aplicativo, para isto verifique em Configurações | Parametrizador | Requisições | Configuração de E-mails.

Caso a parametrização do sistema esteja por Gestão de Hierarquia por Posição ao concluir a rescisão de um funcionário que ocupe posição de liderança, a vigência do líder será encerrada e a data final da vigência será atualizada de acordo com a data da rescisão.

**Campos Complementares na Requisição de Desligamento**

* Esta funcionalidade permite a inclusão de **Campos Complementares** nas **Requisições de Desligamento**.
* Os Campos Complementares criados para a Requisição de Desligamento possuem **abrangência global**. Eles serão exibidos em **todas as coligadas** do sistema, independentemente da coligada em que foram criados ou da tabela dinâmica vinculada.
* Para visualizar e gerenciar a existência desses campos, siga o caminho no menu: **Gestão Organizacional | Requisições | Campos Complementares | Requisição de Desligamento**

**Importante**

Foi verificado que quando o SaveParecer está como obrigatório no Agilis, são gerados dois Pareceres: Em andamento e Aprovado. Esse comportamento é previsto em Oracle e SQL.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Identificação Parecer de Desligamento

|  |  |
| --- | --- |
|  | Como Fazer |

---

[Aprovar requisição após conclusão do atendimento](https://tdn.totvs.com/pages/viewpage.action?pageId=874209250)

Cancelar Requisição

Suspender Requisição

Revogar Suspensão

Inserir no Fluxo

Passar para atendente anterior

Incluir Parecer em lote

Alterar Fluxo da Requisição

Alterar Aprovador Atual da Requisição
