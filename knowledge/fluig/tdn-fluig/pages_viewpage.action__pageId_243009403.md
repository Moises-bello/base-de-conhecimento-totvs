---
content_hash: f68c8b2573000aad4f4b4b4f481fc493a4224d1b390f09849d8cc15073d27d23
fetched_at: '2026-06-28T21:35:22.964366+00:00'
page_id: '243009403'
product: fluig
source: tdn-fluig
title: DES  - Definir uma data mínima de seleção no calendário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243009403
version: 4
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

**Versão:** 1.5.9

# Ocorrência

Pretendemos implementar uma validação de data referente ao nosso processo de aprovação de horas extras, de forma que, as solicitações devem ser iniciadas com pelo menos três dias de antecedência. 

# Solução

O componente de [calendário](https://style.fluig.com/javascript.html#fluig-calendar) presente no [Style Guide](https://style.fluig.com/) possibilita realizar esta validação, pois é possível definir uma data mínima de seleção. Por exemplo, se o usuário tentar iniciar a solicitação hoje, só conseguirá selecionar no calendário uma data daqui a três dias.  
  
Disponibilizei anexo um exemplo de formulário que aplica a regra descrita acima. Para bloquear a data mínima de seleção, foi utilizado método setMinDate() disponível a partir do objeto FLUIGC.calendar():

jsCalendáriotrue

Com a implementação deste código, podemos visualizar que a data mínima de seleção é de 3 dias após a data atual:

# Observações

Esta configuração não está disponível no editor web da plataforma no momento, é possível de ser feita apenas via TDS, alterando o código manualmente.
