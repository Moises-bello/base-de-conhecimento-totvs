---
content_hash: 25106a20de42e2fa97ad1c4b615fa92e5ce707f4f8bd277cc2f94f6215ddac32
fetched_at: '2026-06-29T00:08:15.675339+00:00'
page_id: '244920334'
product: rm
source: tdn-rm
title: RMPAT00002_Liberação de Competência.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244920334
version: 8
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.16 ou superior |
| **Ocorrência:** | Liberação de Competência |
| **Ambiente:** |  |
| **Passo a passo:** | Tem como objetivo alterar o período de cálculo da base de dados bem como realizar o cálculo dos valores do patrimônio de forma a mantê-los atualizados de acordo com o período. Ou seja, a Liberação de Competência realiza a transposição de um mês de cálculo para o próximo mês, garantindo através de validações, que todas as informações referentes ao cálculo e sua contabilização, foram executados e validados com sucesso.  **Exemplo:** Patrimônios não baixados e estão sem cálculos, valores calculados e não contabilizados, aquisições não contabilizadas, etc.  A liberação de competência mensal do sistema aumenta o comprometimento dos usuário com os cálculos naquele determinado mês, promovendo ações de correção, ainda no próprio mês, e não mais no final do período como no modelo anterior 11.40.  A Liberação de Competência faz parte do desmembramento do antigo processo de Liberação de Período que conta também com o processo de [Fechamento de Período](https://tdn.totvs.com/pages/viewpage.action?pageId=423938274).    **Regras para Liberação de Competência:** - Todas as ocorrências do período realizadas e seus valores conferidos.  - Todas as integrações do período (Notas, Transferências, Aquisições...) do período realizadas.  - Todos os relatórios do período gerados e conferidos.  - Backup da base de dados realizado.  - Contabilização de aquisição, ocorrência com (status “a contabilizar”) pendente.    O sistema permite que o período de cálculo tenha um limite de 24 meses, ficando a critério do usuário definir qual será o período e ao final do mesmo realizar o seu fechamento.  **É extremamente importante que se faça um BACKUP da base de dados antes da execução do processo de Liberação de Competência.** ****Se por algum motivo a Liberação de Competência não se completar deve-se verificar o log gerado ao final do processo, e se necessário restaurar imediatamente o BACKUP e iniciá-lo novamente.****    Disponível através do ****Menu | Utilitários | Liberações | Liberação de Competência****.      O serviço de Liberação de Competência possui uma parametrização de recálculo para patrimônios, onde os cálculos dos patrimônios são feitos para o novo mês de cálculo, para isso as opções "Executar recálculo" e "Executar Ocorrência Pendentes" devem estar marcadas.        **Exemplo:** Ao executar o processo de liberação de Janeiro para Fevereiro os valores de Fevereiro serão calculados e exibidos na aba Cálculo Razão do cadastro de patrimônios.  Caso esta opção não esteja marcada, o processo de cálculo de depreciação deverá ser executado manualmente. Através do **Menu | Cadastros | Cenários | Selecionar o respectivo cenário | Processos | Calcular cenário**.  Se existir patrimônios sem cálculo de depreciação/correção para o período de cálculo atual o sistema irá apresentar uma mensagem, solicitando o cálculo, a contabilização e a integração dos mesmos. Desta forma o usuário será responsável por interromper a Liberação de Competência para realização destes procedimentos ou continuar. |
| **Observações:** |  |
