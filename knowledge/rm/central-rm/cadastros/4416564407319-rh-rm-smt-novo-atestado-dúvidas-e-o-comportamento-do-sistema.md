---
article_id: 4416564407319
category: Cadastros
content_hash: 69c5e09c8dfa9477399f95db1d89a5fd8a160e0e71fbf0a7f20e0a0d6254bc33
fetched_at: '2026-06-28T22:47:36.401872+00:00'
product: rm
section_id: 1500000834961
source: central-rm
title: 'RH - RM - SMT - Novo Atestado: Dúvidas e o Comportamento do sistema'
type: support-article
updated_at: '2025-12-15T21:28:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4416564407319-RH-RM-SMT-Novo-Atestado-D%C3%BAvidas-e-o-Comportamento-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035638401687) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como configurar o Novo Atestado e quais serão os comportamentos adotados pelo sistema em relação a situação do funcionário?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional – A partir da versão 12.1.24   
  
**Solução**

O novo atestado foi criado para atender as solicitações do mercado. Ao utiliza-lo é possível:

* Criar uma desvinculação do período de atestado e o período de afastamento, com a criação de um novo campo (Data Término Afastamento) que possibilita ao usuário definir quando será efetivamente encerrado o afastamento.
* Análise de continuidade dentro do período de carência de forma automática, usuário lance um atestado com quantidade de dias inferior a 16 dias, mas que somando-se a atestados anteriores totalize mais de 15 dias no período de carência, o sistema irá considerar a continuidade e habilitará o campo de termino de afastamento.
* Funcionário com múltiplos vínculos, o atestado passa a ser vinculado à pessoa e consequentemente o atestado será vinculado automaticamente à todas as chapas associadas à pessoa na coligada contexto.
* O atestado cadastrado fica visível somente na coligada que originou o registro, assim como o afastamento.

Para acessar o “Novo Atestado”, o usuário deverá acessar o Parametrizador do módulo TOTVS Segurança e Saúde Ocupacional o menu **Opções** | **Parametrizador** e selecione **Validações,** avance a tela e  habilite o parâmetro '**Encerra Histórico de Afastamento (TOTVS Folha de Pagamento)** **conforme Data Término Afastamento do Atestado (TOTVS Segurança e Saúde Ocupacional)'**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26925664748055)

Após habilitar o 'Novo Atestado', essa passar a ser a nova tela para utilização do atestado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26925664751767)

**Importante**

Valide o comportamento ao utilizar o 'Novo Atestado'.

**Na competência**  
**Menos de 15 dias ou igual a 15 dias:**

- Quando o atestado for lançado na competência atual e tiver duração menor ou igual que 15 dias, o sistema não retornará na tela, as informações referentes às pericias e previsões assim como não habilitará a data de termino de afastamento.

- Preencherá os históricos de afastamento e situação com as datas de início e término de afastamento.

**Mais que 15 dias:**

- Atestado irá habilitar o campo “Data Término de Afastamento”. É o preenchimento da data término que garante que o afastamento está concluído ou não.

Não informando a data término.  
- O Atestado médico é lançado para todas as chapas do funcionário;

- A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado;

- Históricos de situação e afastamento são preenchidos sem a data de retorno, em todas as chapas do funcionário.

Informando a data termino em um atestado já cadastrado.  
- O sistema emitirá uma mensagem informando que irá alterar a situação do funcionário para ativo (se o afastamento terminar na competência atual), atualizar o histórico de afastamento com a data término de afastamento, inserir um novo registro no histórico de situação, referente ao retorno à atividade (se o atestado terminar na competência).

Já preenchendo a data de término.  
- Quando a data de término é na mesma competência, o sistema apenas atualiza os históricos de situação e afastamento com as datas de início e termino do afastamento, cria os atestados e históricos em todas as chapas do funcionário;

- Mantem a situação do funcionário, conforme a situação anterior ao atestado.

**Menos de 15 dias ou igual a 15 dias, com continuidade totalizando mais de 15 dias.**

Informando a data termino.  
- Atualiza o histórico de afastamento com as datas de início e término do afastamento;

- Atualiza o histórico de situação apenas com o início do afastamento.

- A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado;

Não informando a data término.  
- O Atestado médico é lançado para todas as chapas do funcionário;

- A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado.

- Históricos de situação e afastamento são preenchidos sem a data de retorno, em todas as chapas do funcionário.

Informando a data termino em atestado em aberto.  
- Atualiza os históricos de situação e afastamento com a data término do atestado;

- Insere um novo registro no histórico de situação, referente ao retorno à atividade.

**Atestado terminando na próxima competência**  
**Mais de 15 dias.**

- Atestado irá habilitar o campo “Data Término de Afastamento”.

Não informando a data termino.  
- O Atestado médico é lançado para todas as chapas do funcionário;

- A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado.

- Históricos de situação e afastamento são preenchidos sem a data de retorno, em todas as chapas do funcionário.

Informando a data término.  
- Atualiza o histórico de afastamento com as datas de início e término do afastamento;

- Atualiza o histórico de situação apenas com o início do afastamento.

- A situação do funcionário e de suas chapas relacionadas é alterada para a situação de afastamento do tipo de atestado;

- Na execução da rotina de liberação de competência (no Totvs Folha de Pagamento) para a competência de término do afastamento, o sistema então atualizará a o histórico de afastamento com a data término e retornará a situação funcionário para a situação anterior ao afastamento.

**Menos de 15 dias ou igual a 15 dias.**

Quando o atestado tiver quantidade de dias inferior ou igual a 15 e ultrapassar de um mês para o outro, a situação será alterada para o afastamento vinculado ao atestado, devido ao fato de que o mesmo estará de atestado no último dia do mês de competência. Na liberação de competência a situação do funcionário irá retornar pra Ativo.

***Observação: Nos casos onde a situação do funcionário seja "V - Aviso prévio" a situação não será alterada.***

**Saiba Mais**

Para maiores informações, acesse:

- [Novo Atestado](https://tdn.totvs.com.br/display/public/LRM/Novo+atestado)
