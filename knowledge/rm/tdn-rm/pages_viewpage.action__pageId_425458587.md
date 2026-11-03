---
content_hash: bf255dcd0bdf2868258e248e787cbc2c9ced9ce1ecc72fd88236927c67ff1397
fetched_at: '2026-06-29T00:09:31.268563+00:00'
page_id: '425458587'
product: rm
source: tdn-rm
title: Controle de alteração de registros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458587
version: 6
---

O controle de alteração de registros, têm como objetivo auxiliar Instituições que desejam manter um maior controle sobre os dados que gerem impacto na geração de folha de pagamento do professor. Com a utilização deste controle, quando o registro é cadastrado ou  alterado, será necessário executar o processo de aprovação, e somente após esta aprovação os dados serão enviados para o sistema TOTVS Folha de Pagamento.   
O controle é realizado de acordo com a necessidade de cada Instituição, habilitando somente os controles que lhe são úteis.   
Os itens que podem ser controlados perante parametrização são: Turma/Disciplina, Atividade Extra e Atividade Complementar.   
Com a utilização deste recurso, os registros controlados terão o conceito de "Status".

**Status disponíveis:**

* **Pentente** O registro terá seu status como Pendente sempre que for inserido ou sofrer uma alteração.
* **Reprovado** O registro terá seu status como Reprovado sempre que tiver sua alteração ou cadastro negado pelo usuário.
* **Aprovado** O registro terá seu status como Aprovado sempre que tiver sua alteração aprovada pelo usuário.

Somente registros com os Status "Aprovado" serão enviados para o TOTVS Folha de Pagamento e consequentemente serão utilizados para calculo da folha de pagamento do Professor.  
**Notificações**  
Ao executar o processo de Aprovação/Reprovação, caso parametrizado, o sistema enviará uma notificação por e-mail para os destinatários cadastrados. O cadastro de endereções de e-mail e realizado nos parâmetros do sistema, junto a habilitação do controle.

**Registros pendentes de aprovação:**   
Nesta visão serão retornados todos os registros que estejam "Pendentes" de aprovação. O objetivo é facilitar a visualização dos registros que sofreram alteração e estão com o status "Pendente". Também é possível visualizar o histórico de alterações, aprovações e reprovações do registro. Caso seja necessário realizar alguma alteração no registro esta também pode ser executada a partir dessa visão.  
   
**Observações:**

* Nas visões de cadastro dos registros, também será disponibilizado o processo de Aprovação/Reprovação. Para visualização do processo o usuário deve ter habilitada a permissão no seu perfil.Processo "Controle de alteração de registro" no cadastro de turma do professor
* A cada aprovação/reprovação do registro, será gerado um novo registro na visão de logs do registro.
* O controle de aprovação não trata registros que forem excluídos.
* O controle de aprovação não realizará a atualização das alterações na folha de pagamento e este controle deverá ser feito manualmente.
* Ao reprovar uma alteração o registro não terá seus dados atualizados para os dados anteriores.
* Um registro com status aprovado não pode ter o status alterado para reprovado, mas qualquer alteração neste registro fará com que o seu status volte para pendente.

## Links relacionados
