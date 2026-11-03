---
content_hash: 1e2aaa2ed4e850d86ca59db98f852dd35a7f4eea54001e279e41118aaa759d29
fetched_at: '2026-06-29T00:09:12.790954+00:00'
page_id: '417700517'
product: rm
source: tdn-rm
title: Cirurgia
type: documentation
url: https://tdn.totvs.com/display/LRM/Cirurgia
version: 2
---

**Cirurgia**   
Para as consistências:

* Tipo de cirurgia tem que ser um dos tipos validos. Tipo valido: E, T, U e nulo (tipo cirurgia não é obrigatório).
* Tipo de ferida tem que ser um dos tipos validos. Tipo valido: L, C, P, I e nulo (Tipo de ferida não é obrigatório).
* Anestesia tem que ser um dos tipos validos. Tipo valido: L, G, B e nulo (anestesia não é obrigatório)
* Risco cirúrgico tem que ser um dos tipos validos. Tipo valido: 1, 2, 3, 4, 5, 6 e nulo (Risco cirúrgico não é obrigatório).
* Validação de especialidade - A especialidade deve ser válida.
* Anestesista pode ser nulo ou devera corresponder a um CRM valido no cadastro de médico.
* Cirurgiões. Devera corresponder a um CRM valido no cadastro de medico.  
  A função pode ser P (Principal), A (Auxiliar) ou vazio. A informação da função não é obrigatória ao se importar. Ao validar a importação de cirurgia, poderá informar a função do cirurgião.    
  Se as consistências acima não forem respeitadas no momento da importação será gerado log com mensagem de AVISO e o campo onde estiver nulo (desde que não seja obrigatório) ou que não tenham valores validos para a base Janus, após importação o campo ficara em branco. O restante do registro será importado normalmente  
  Será gerado log com mensagem de erro para as consistências:
* O registro ou prontuário terá que corresponder a um prontuário valido já lançado no sistema.
* O nome do paciente da cirurgia tem que corresponder ao nome do paciente lançado na base Janus.
* A data de cirurgia tem que estar dentro de uma internação valida do paciente.  
  Observação  
  Para que os dados importados sejam validados, é necessário que todos os procedimentos cirúrgicos das tabelas de origem (SUS, AMB) estejam mapeados com um procedimento NHSN.   
  A validação de Importação de cirurgia, será o momento em que o usuário informará dados iniciais a cirurgia e validará a cirurgia importada.   
  Clique em Menu Utilitários - Validação de Importação de Cirurgia.
