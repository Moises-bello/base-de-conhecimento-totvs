---
content_hash: d6b8f25ff80cfac938a0f24576a49647f122d8a737f9ff521e5ad328d5439bba
fetched_at: '2026-06-29T00:09:16.878165+00:00'
page_id: '421385601'
product: rm
source: tdn-rm
title: Validar Apontamentos
type: documentation
url: https://tdn.totvs.com/display/LRM/Validar+Apontamentos
version: 4
---

---

Os registros de apontamentos conciliados podem ter como status Pendente, Validado ou Apropriado. O apontamento recebe o status Pendente quando o registro foi conciliado por outros dois do anexo de Apontamentos dos Coletores e este novo registro ainda não foi verificado. O status Validado não possui uma forma automática de alteração nos registros, pois é uma situação onde o apontamento deve passar por uma verificação manual, uma análise, pelo usuário a fim de garantir que suas informações estão consistentes. Após esta verificação é possível alterar o status para "Validado". O usuário pode efetivar esta "validação" dos apontamentos para vários registros simultaneamente através deste processo. No menu Cadastros | Mobilidade | Ciclos de transporte | Anexos | Apontamentos Conciliados, o usuário seleciona o conjunto de registros que deseja efetuar a Validação múltipla e seleciona Processos | Validar apontamentos. O sistema valida se algum dos registros está com o status diferente de "Pendente" e, em caso afirmativo, emite mensagem explicativa e aborta o processo. Se só foram selecionados apontamentos com status "Pendente", o sistema altera o status dos registros selecionados para "Validado".

**Observação:**

* Este processo irá ser disparado nem a necessidade de uma interface específica em que o usuário precise informar algum dado em particular;
* A seleção de apontamentos com status diferentes de "Pendente" não irá invalidar a execução do processo, porém estes apontamentos não serão processados e será incluída uma mensagem no final do log do processo informando que estes apontamentos não foram validados.
