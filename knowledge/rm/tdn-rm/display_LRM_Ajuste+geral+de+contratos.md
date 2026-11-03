---
content_hash: b0143ef067909e73db801d86351694881d2ad5ab7523066959bb5221e1b916ce
fetched_at: '2026-06-29T00:09:54.951276+00:00'
page_id: '445668284'
product: rm
source: tdn-rm
title: Ajuste geral de contratos
type: documentation
url: https://tdn.totvs.com/display/LRM/Ajuste+geral+de+contratos
version: 5
---

permite ajustar inconsistências no contrato, podendo selecionar entre as opções:

Este processo **Ajuste de Inconsistências de Contratos**  é utilizado para iniciar o processo de correção ou ajuste de informações relacionadas a contratos já cadastrados.

Na tela que se abre funciona como a **primeira etapa do processo**, onde o usuário informa:

* **Qual tipo de ajuste deseja realizar**
* **Como os contratos serão localizados e agrupados** para aplicação do ajuste

Essa tela não realiza alterações diretamente. Ela apenas **define o contexto** para que o sistema apresente, nas próximas etapas, os contratos elegíveis para o ajuste escolhido.

## Quando utilizar esta tela

O usuário deve utilizar esta funcionalidade sempre que:

* O sistema identificar inconsistências em contratos
* Houver necessidade de corrigir valores, vínculos ou periodicidade
* For necessário ajustar informações financeiras já registradas
* O contrato não estiver se comportando conforme o esperado em medições, faturamentos ou integrações

### Filtro Tipo de ajuste

Este filtro define **o que será corrigido ou ajustado** nos contratos.

É um campo obrigatório e possui as seguintes opções:

* **Ajustar Inconsistências:** Opção utilizada para correções gerais. Normalmente aplicada quando o sistema aponta erros ou divergências nos dados do contrato, como vínculos incorretos, validações pendentes ou informações inconsistentes.
* **Ajustar Valores Medidos:** Utilizada quando há divergência nos valores de medições já lançadas, permitindo a correção desses valores.
* **Ajustar Saldo de Adiantamento:** Indicada quando o saldo de adiantamento do contrato está incorreto e precisa ser recalculado ou ajustado.  [Saiba mais](https://tdn.totvs.com/display/LRM/Atualizar+Saldo+de+Adiantamento)
* **Ajustar Valores de Aditivos:** Utilizada para corrigir valores provenientes de aditivos contratuais que impactam o valor total do contrato.
* **Ajustar Deduções e Retenções:** Permite corrigir valores de impostos, retenções ou deduções aplicadas ao contrato.
* **Ajustar Vínculo de Contratos gerados por Movimento:** Usada quando contratos gerados a partir de movimentos estão com dados incorretos, como por exemplo o estorno de pedidos
* **Ajustar Periodicidade:** Utilizada para corrigir datas de períodos que não estão de acordo com a periodicidade do contrato

> ⚠️ Importante: a opção selecionada acima influencia diretamente as próximas telas e os tipos de dados que poderão ser alterados.

### Opção Por Coligada ou Por Projeto

Estas opções define **como o sistema irá localizar os contratos** que poderão ser ajustados.

O usuário deve escolher uma das opções abaixo:

* **Por Coligada**  
  Ao selecionar esta opção, o sistema apresentará os contratos vinculados a uma coligada específica.
* **Por Projeto (Contexto)**  
  Ao selecionar esta opção, o sistema considerará os contratos vinculados ao projeto que está ativo no contexto atual do usuário.
