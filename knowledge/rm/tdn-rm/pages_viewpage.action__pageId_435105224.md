---
content_hash: fdbe400e9473cac864a3a6e751f042ec6d67d9daad56eeb3a2b488b82c570867
fetched_at: '2026-06-29T00:09:48.728478+00:00'
page_id: '435105224'
product: rm
source: tdn-rm
title: 03 - TCGI - Atendimento - Solicitação de Atendimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105224
version: 15
---

**Solicitação de Atendimento**   
Essa funcionalidade é responsável por gerenciar as inspeções e atendimentos das garantias dos Empreendimentos. Sempre que houver um problema residencial é aberta uma solicitação de atendimento em que um ou mais responsáveis irão fazer a inspeção e resolução desse problema de acordo com as coberturas e garantias relacionadas à aquela sub unidade.

O Cadastro de atendimento associa automaticamente as garantias relacionadas no contrato de venda respectivo. Após a inclusão do atendimento o usuário pode Avançar Etapa, Voltar Etapa, Incluir agendamento para etapa e gerar movimento para etapa.

O Atendimento pode possuir N arquivos anexos que ficam disponíveis para consulta.

Existe também a possibilidade de visualizar todos os agendamentos realizados por etapa para o atendimento de acordo com o responsável pela garantia e o seu quadro de horário de disponibilidade.

Outra possibilidade é visualizar todos os check-list criados por etapa para o atendimento verificando se ele foi executado ou não.

Outra visão disponível é de todos os movimentos gerados por etapa se assim a etapa foi configurada. Todos os movimentos gerados para o atendimento são apresentados neste anexo.

É possível verificar também o histórico de avanço de etapa do atendimento verificando todas as etapas avançadas.

**Pré-Condições**  
   
Para realizar o cadastro da Solicitação de Atendimento é necessário alguns cadastros e e parametrizações prévias.  
   
*Cadastros:*

* Coberturas
* Modelos
* Responsáveis
* Etapa
* Associar o modelo ao empreendimento.
* Gerar uma venda que possui a cobertura.

*Parâmetros:*

* Informe qual é a etapa Inicial de uma solicitação (Primeira etapa).
* Caso desejar crie um texto default com Mnemônicos para gerar os agendamentos.

**Aba Identificação**

 

**Número do Atendimento:**  
Código da Solicitação de Atendimento. campo auto incremental.  
   
**Código da Etapa:**  
Este campo informa em qual etapa se situa a solicitação. Ao criar uma nova solicitação esse campo é preenchido através do campo informado nos parâmetros de garantia do Incorporação. Com o processo de Avançar ou Voltar etapa, esse campo é alterado automaticamente.  
   
**Status do Atendimento:**  
Esse campo é alterado de acordo com a etapa em que se encontra a solicitação, indica em qual situação está o atendimento, por exemplo: Em inspeção, em atendimento, cancelado, concluído.  
   
**Descrição:**  
Informe detalhadamente o problema que está ocorrendo.

**Preferência de período para visitas**

Poderá informar ou visualizar os dias da semana ao qual terá a disponibilidade para receber visitas da garantia do imóvel.

**Venda/Aluguel:**  
Informe o número da venda/aluguel que possui as coberturas e garantias para a resolução da solicitação. Pode ser feito um filtro pelo nome do comprador, número do contrato, pelo Empreendimento, pela sub unidade, endereço e outros. Apenas vendas com situação Efetivada ou Quitada são permitidas.  
   
**Cobertura da Venda:**  
É mostrada todas as coberturas que o contrato possui e se estão vigentes ou não. São visualizados o status, o tipo de cobertura, o período de vigência e o tipo de início de vigência das coberturas associadas ao contrato.  
   
 

|  |  |
| --- | --- |
|  | Informações Complementares |

---

|  |  |
| --- | --- |
|  | Como Fazer |

---

---

#### Configuração para solicitação de atendimento pelo PDC (Portal do Cliente)

Cadastro de etapa no TIN com inclusão de demais etapas para execução. Vinculação da primeira etapa nos parâmetros do TIN. Inclusão de solicitação de atendimento pelo PDC. Avanço do atendimento pelo TIN para as etapas pré-definidas.

Cadastro da 1ª etapa com definição do status do atendimento. Cadastro das demais etapas para execução do atendimento pelo processo de avanço de etapa do atendimento. O PDC espera a seguinte ordem de avanço de etapa: Em Aberto, Inspeção, Agendamento, Concluído, Cancelado

Vinculação da primeira etapa ao parâmetro de etapa inicial do TIN. Para que um atendimento do PDC seja gerado é necessário definir a etapa inicial do atendimento pelo parâmetro do TIN

##### Abertura de atendimento pelo PDC:

Na tela de abertura o usuário seleciona qual o imóvel deseja atendimento. Depois seleciona opcionalmente uma garantia específica do imóvel para atendimento. Depois informa um título para solicitação, uma descrição e arquivos para envio em anexo do atendimento.

##### Visualização da etapa atual no PDC:

Nesta tela o usuário consegue visualizar em qual etapa predefinida pelo sistema o atendimento se encontra. O usuário não pode fazer nenhuma interação no atendimento pelo PDC. O avanço de etapa é realizado completamente no RM.

##### No PDC é possível visualizar a lista de atendimentos abertos para as respectivas subunidades do empreendimento do contexto:
