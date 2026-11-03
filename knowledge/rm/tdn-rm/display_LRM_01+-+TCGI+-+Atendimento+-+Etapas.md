---
content_hash: 090af1e26dc61dc2ba503a8a19d6e5bff397300b8cfbb9c289bb25a4e086665e
fetched_at: '2026-06-29T00:09:48.547820+00:00'
page_id: '435105186'
product: rm
source: tdn-rm
title: 01 - TCGI - Atendimento - Etapas
type: documentation
url: https://tdn.totvs.com/display/LRM/01+-+TCGI+-+Atendimento+-+Etapas
version: 8
---

**Etapas**

---

O TOTVS Incorporação permite que seja cadastrado o fluxo de etapas da solicitação de atendimento de garantia. Essas etapas definem o caminho que o atendimento deve seguir até seu encerramento. Cada uma dessas etapas tem suas especificidades e permissões, além de indicar qual é a etapa antecessora.

O cadastro de etapa é premissa para que seja possível realizar a inclusão de atendimentos de garantia e entrega de chaves. A etapa é composta por lista de perfis de permissão para avanço de etapa, etapa correspondente do RM Agilis quando utilizada a respectiva integração, lista de check-list por etapa e lista de tipos de movimento que podem ser gerados por etapa.

**Aba Identificação**  
   
**Código da Etapa:**  
Código Identificador da etapa, esse campo é auto incremental.  
   
**Nome:**  
Informe o Nome da Etapa que será cadastrada. Exemplo: Em aberto, Em Inspeção, Em Atendimento, Solicitação Concluída...  
   
**Status do Atendimento:**  
São os estados do atendimento, indicam em que ponto está o atendimento.

Ao avançar ou voltar etapa o atendimento receberá o status definido na etapa.  
É possível escolher entre os seguintes status.

* Em aberto
* Inspeção
* Agendamento
* Concluído
* Cancelado

**Código da Etapa Anterior:**  
Ao cadastrar a primeira etapa este campo deve ser deixado em branco, as demais etapas cadastradas devem informar a anterior para definir o fluxo, dessa forma é possível avançar ou voltar etapas no processo.  
Toda solicitação deve ser associada a uma etapa definida como inicial (que possui o campo em branco).  
   
*Observação:* Para definir qual é a primeira etapa da solicitação acesse os parâmetros do Incorporação.  
   
**Descrição:**  
Informe o objetivo e detalhes da etapa a ser cadastrada.  
   
   
   
**Aba Permissão**  
   
**Perfil:**   
Insere qual o perfil de usuário tem permissão para utilizar a etapa cadastrada.

A associação de um perfil ao acesso a etapa é obrigatório para permitir o avanço de etapa do atendimento.

Apenas os usuários do RM que tiverem permissão nos perfis associados poderão avançar aquela determinada etapa.

|  |  |
| --- | --- |
|  | Informações Complementares |

Nos parâmetros do sistema é definido a etapa inicial do fluxo de atendimento de garantia e entrega de chaves, conforme imagens a seguir:

Tipo de atendimento Garantia e Entrega de Chaves: O fluxo de atendimento de garantia e entrega de chaves é definido justamente pela etapa inicial parametrizada no TIN, que indica qual será o fluxo de execução de cada tipo de atendimento

**Etapa inicial do atendimento de garantia**

**Etapa inicial do atendimento de entrega de chaves**

Logo que o sistema está parametrizado os atendimentos podem ser cadastrados a partir do:

Cadastro de solicitação de atendimento de entrega de chaves

Cadastro de solicitação de atendimento de garantia

E pelo PDC (Portal do Cliente) pode ser cadastrado uma solicitação de atendimento de garantia.

---

|  |  |
| --- | --- |
|  | Veja Também |

---

Para saber mais sobre os perfis do sistema, acesse o link abaixo:  
  
   
Para Informações sobre os Parâmetros de garantia:
