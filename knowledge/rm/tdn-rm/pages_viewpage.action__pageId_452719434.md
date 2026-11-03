---
content_hash: de5ccb9b220c4682ab1226dd5a345a3f73c75148267e850e7d6268eb416c19f5
fetched_at: '2026-06-29T00:10:07.773158+00:00'
page_id: '452719434'
product: rm
source: tdn-rm
title: Integração Folha de Pagamento X Gestão de Pessoas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719434
version: 3
---

**Devolução de EPI:**  
Quando o funcionário possuir EPI emprestado será emitida uma mensagem de advertência para, no momento da demissão deste funcionário, alertar caso a data de devolução estiver em branco, mas não impedirá a demissão do funcionário, devendo, caso necessário, ser providenciado a atualização no Gestão de Pessoas.  
   
**Requisição:**  
Se o Gestão de Pessoas estiver parametrizado para utilização obrigatória da requisição de desligamento e existindo uma requisição de desligamento aprovada para o funcionário selecionado, os dados desta tela serão preenchidos com os mesmos dados da requisição, caso o parâmetro "Permitir alterar dados da requisição vinculada" esteja selecionado, no Gestão de Pessoas, os dados da requisição vinculada poderão ser alterados. Se  for confirmada a alteração dos dados o sistema obrigatoriamente gerará um novo parecer para a requisição, no qual constará o registro do usuário logado, a justificativa fornecida e as alterações realizadas. Além disso, será enviado e-mail para o requisitante, o Gestor do RH e todos os participantes do fluxo comunicando a situação da requisição.  
Para requisições aprovadas, porém suspensas, será permitido, no momento da demissão, revogar a suspensão da requisição para que ela possa ser utilizada neste processo; caso a suspensão não seja revogada o processo de demissão será interrompido.  
Caso seja obrigatório a utilização da requisição de desligamento e não existindo uma requisição aprovada para o funcionário em questão será exibida uma mensagem de alerta notificando esta situação e o processo será interrompido. A demissão só poderá ser efetivada após a existência de uma requisição aprovada.   
Ao finalizar o processo de demissão o status da requisição será automaticamente alterado para "Concluído" e neste momento será verificada a existência da requisição de substituição criada a partir da requisição de desligamento. Existindo esta requisição o número de vagas do quadro de lotação do funcionário demitido será mantido, caso contrário haverá redução de uma vaga disponível neste quadro. Este procedimento será válido se o Gestão de Pessoas estiver parametrizado para utilizar o controle de lotação. Todos os procedimentos relacionados à conclusão da requisição serão notificados, através do envio de e-mail para o Gestor do Depto. de Pessoal e para os demais participantes do fluxo da requisição, conforme configurações no Gestão de Pessoas.  
   
**Atenção:**  
Se o funcionário selecionado para a demissão estiver vinculado à outro tipo de requisição que não seja a de desligamento, o processo de demissão não será efetivado até que a requisição em questão seja cancelada.  
   
**Observação:**  
Para verificar os processos relacionados à requisição de desligamento acesse, no Gestão de Pessoas, em Gerência de RH em Requisições em Processos de Desligamento.  
   
**Gerar exames pendentes:**  
O sistema passa a gerar exames pendentes do tipo "Demissional" automaticamente ao cadastrar uma rescisão. Essa geração será possível se: - no sistema Segurança e Medicina do Trabalho for feito o processo de "Associação de Perfil", associando um perfil de exames que tenha pelo menos um Exame Demissional a uma função e/ou seção e/ou lotação; - no sistema Folha de Pagamento realizar a rescisão de um funcionário que tenha função/seção/lotação com o perfil citado acima associado.  
Nessas condições, ao realizar o cadastro da rescisão, o sistema emitirá uma mensagem informando que o funcionário possui exame médico demissional pendente, e  incluirá esses exames no cadastro de exames pendentes do funcionário.

**Observação:** O prazo determinado para a realização de exames é definido pelo Grau de Risco associado à seção do funcionário. Esse risco está associado à Atividade Econômica cadastrada na seção. De acordo com a NR-7, Seções cujo Grau de Risco seja 1 ou 2, possuem um prazo de 135 dias; seções cujo Grau de Risco seja 3 ou 4, possuem um prazo de 90 dias. Quando não houver uma Atividade Econômica(CNAE) válida cadastrada na seção, nenhum Exame Pendente Demissional é gerado.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Funcionários

Rescisão
