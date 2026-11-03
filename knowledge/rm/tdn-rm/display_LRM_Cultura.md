---
content_hash: 96dd881cf91db918f59237169ef528bbc2cad05963a09acc47c4abc6a843f171
fetched_at: '2026-06-29T00:09:12.723228+00:00'
page_id: '417700471'
product: rm
source: tdn-rm
title: Cultura
type: documentation
url: https://tdn.totvs.com/display/LRM/Cultura
version: 1
---

**Cultura**   
Importador de Cultura   
Para importação de cultura devem-se seguir as consistências:  
   
Para as consistências:

* Unidade clinica deve corresponder ao código de uma unidade clínica válida na base.
* Especialidade deve corresponder ao código de uma especialidade válida na base.
* Antibiótico deve corresponder ao código de um antibiótico válido na base.
* O campo Sensibilidade deve corresponder a um tipo de sensibilidade válido: R, S ou I
* Os campos material e grupo de material deve corresponder ao código de um material e/ou grupo de material valida na base.  
  Se as consistências acima não forem respeitadas no momento da importação será gerado log com mensagem de AVISO e o campo onde estiver nulo (desde que não seja obrigatório) ou que não tenham valores validos para a base Janus, após importação o campo ficara em branco. O restante do registro será importado normalmente.  
  Observação  
  Ao dar o aviso de antibiótico não encontrado, o antibiograma do pedido de cultura não é importado.  
     
  Será gerado log com mensagem de erro para as consistências:
* O prontuário do paciente deve corresponder a um prontuário válido na base.  
  Caso não encontre o prontuário, será gerada mensagem de ERRO e o registro não será importado
* O Nome do paciente deve corresponder ao nome do paciente associado ao prontuário na base  
  Caso os nomes não sejam iguais, será gerada mensagem de ERRO e o registro não será importado
* Deve haver uma internação com data de admissão anterior ou igual à data do pedido de cultura e data de alta maior que o mesmo ou em aberto, associada ao paciente na base  
  Caso a internação não seja encontrada, será gerada mensagem de ERRO e o registro não será importado.
* O Germe deve corresponder ao código de um germe válido na base.  
  O Crescimento bacteriano será preenchido como sim, caso existam germes associados ao pedido e com não, caso contrário.  
  Quando um germe não é encontrado, não é importado nem o germe nem os antibiogramas daquele germe.  
  A validação de Importação de cultura, será o momento em que o usuário informará dados iniciais ao pedido de cultura e validará a cultura importada.   
  Clique em Menu Utilitários - Validação de Importação de Cultura.
