---
content_hash: 043a15d1b3c6e4cee013ac3d0d8b97fb5316f4da1569ea8fb18f585f1ab8c7ff
fetched_at: '2026-06-29T00:10:07.742383+00:00'
page_id: '452719426'
product: rm
source: tdn-rm
title: Requisição de Transferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719426
version: 4
---

**Requisição de Transferência**

---

Este tipo de requisição tem por objetivo realizar alteração na lotação do funcionário

**Passos para criar uma Requisição de Transferência:**

**1º Passo:** Criar uma Requisição pelo módulo Valorização | Requisições | Transferência.

**2º Passo:** Preencher os campos disponíveis. Para saber as particularidades dos campos, clique aqui. (link do help Pasta Identificação – Requisição de Transferência)

**3º Passo:** Aprovar/Reprovar a Requisição. Se a Requisição for aprovada e o flag "Gerar Substituição" estiver marcado, será gerada uma Requisição de Substituição, com os dados do funcionário que será transferido.

**4º Passo:** Transferir o funcionário, concluindo a Requisição. Este procedimento pode ser realizado de duas formas: No Totvs Gestão de Pessoas, pelo menu Valorização | Efetivações | Efetivar Transferência. No Totvs Folha de Pagamento, caso exista licença deste produto, pelo menu Rotinas | Alterações Globais de Funcionários | Efetivar Transferência.

**Importante:**

Se o flag "Transferir Vaga" estiver marcado e estiver parametrizado o controle de lotação, no momento em que for executado o processo de Efetivar Transferência, a vaga da seção atual do funcionário será transferida juntamente com o funcionário para a seção destino.

Não se aplica a ex-funcionários. Somente as requisições aprovadas são relacionadas para serem efetivadas. Após executar o processo de Efetivar Transferência, o sistema atualiza automaticamente os dados do funcionário e seus respectivos históricos. As Requisições de Transferência que dependam de alteração de CNPJ somente podem ser efetivadas pelo processo de rescisão do funcionário.

A requisição de transferência pode ser cadastrada tanto na MDI quanto nos Portais. No entanto, quando realizada entre coligadas, a transferência só poderá ser inserida via Portal, visto que via MDI não é possível selecionar uma coligada diferente da coligada contexto que esta sendo acessada no momento do cadastro.  
  
Lembrando que, neste caso, é imprescindível que o usuário responsável pelo cadastro da requisição através do Portal, seja chefe tanto na coligada origem quanto na coligada destino. Caso contrário, não será possível visualizar as seções da coligada destino.

**Campos Complementares na Requisição de Transferência**

* Esta funcionalidade permite a inclusão de **Campos Complementares** nas **Requisição de Transferência**
* Os Campos Complementares criados para a Requisição de Transferência possuem **abrangência global**. Eles serão exibidos em **todas as coligadas** do sistema, independentemente da coligada em que foram criados ou da tabela dinâmica vinculada.
* Para visualizar e gerenciar a existência desses campos, siga o caminho no menu: **Valorização | Requisições | Campos Complementares | Requisição de Transferência**

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Identificação Parecer de Transferência  
Rateio de Centros de Custos

|  |  |
| --- | --- |
|  | Como Fazer |

---

Cancelar Requisição Suspender Requisição Revogar Suspensão Inserir no Fluxo Passar para atendente anterior  
Incluir Parecer em lote  
Alterar Fluxo da Requisição  
Alterar Aprovador Atual da Requisição  
Alterar Dados da Requisição
