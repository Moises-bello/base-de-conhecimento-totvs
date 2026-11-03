---
article_id: 360059540413
category: MDT - PCMSO
content_hash: 09597fc92216e468a20152167e62cc5543c7fc947dbaf3a014297666c32b1a95
fetched_at: '2026-06-28T22:44:28.330358+00:00'
product: protheus
section_id: 360010945214
source: central-protheus
title: RH - Linha Protheus - MDT - Como cadastrar e definir os exames que serão apresentado
  no PCMSO (Programa de Controle Médico de Saúde Ocupacional)
type: support-article
updated_at: '2025-09-03T13:01:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059540413-RH-Linha-Protheus-MDT-Como-cadastrar-e-definir-os-exames-que-ser%C3%A3o-apresentado-no-PCMSO-Programa-de-Controle-M%C3%A9dico-de-Sa%C3%BAde-Ocupacional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25844058708503)**Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como cadastrar e definir os exames que serão apresentado no PCMSO (Programa de Controle Médico de Saúde Ocupacional)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**O Módulo Medicina, disponibiliza algumas rotinas, para servirem de facilitadores no controle e amarrações  dos exames periódicos.   
  
Importante ressaltar que  a empresa deverá avaliar qual opção melhor atende sua necessidade. Lembrando que não é necessário ter todos esses cadastros e amarrações, apenas realize os cadastros que for eficaz em seu controle.   
  
Os cadastros e definições são divididos nas seguintes rotinas:  
  
[MP - MDT - Exames por Filial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056781474)  
[MP - MDT - Exames por Programa de Saúde](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058678453)  
[MP - MDT - Exames por Agente (MDTA035)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057693074)  
[MP - MDT - Exames por Função (MDTA450)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057694314)  
[MP - MDT - Exames por Risco (MDTA185)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057694574)Na geração do **PCMSO,** o programa considera em primeiro lugar os exames definidos em **função dos programas de saúde.** Em segundo os exames definidos com base nos **riscos ambientais,** e finalmente, os **exames definidos por filial**, ou seja, aqueles exames genéricos que todos devem realizar periodicamente.

É indispensável que no grupo de exames por filial, seja implantado o **exame de avaliação clínica** conforme descrito na função exames por filial. Com base nesta estrutura de necessidade de exames, o programa calcula a idade do funcionário e verifica em que **faixa etária** ele se enquadra, obedecendo a periodicidade definida para cada exame.

No caso dos **exames por risco**, o programa verifica ainda, qual o ambiente de risco que o funcionário se encaixa e quais os exames definidos para cada risco. Cria então, na tabela de Exames do Funcionário, registros que identificam quais exames devem ser realizados e quando. É importante observar que para os exames definidos com base no ambiente de risco, é considerada a estrutura de definição dos riscos, que é formada por centro de custo, função e tarefa. O Sistema verifica o centro de custo e a função no próprio Cadastro do Funcionário e a tarefa, é verificada nas tabelas de Tarefas e de Funcionários que as executam.

Para cada processo de **geração da programação**, é gravado um registro com os parâmetros informados que deram origem à programação dos exames. Na exclusão deste registro de parâmetros, o programa exclui também todos os registros de exames relacionados.

Esta rotina possibilita a alteração do fornecedor (quando existir mais de um disponível) na geração dos exames.

Se a data de referência do exame não for informada, o conteúdo do campo Vencimento Exame Médico é verificado. Se o conteúdo estiver preenchido, a data de referência é gerada a partir desta data, se não estiver preenchido, a data de referência é gerada à partir da Data de Admissão. Isto ocorre quando o funcionário não possuir exames anteriores para referência.  
  
**Dica:** O parâmetro **MV\_NG2D190** permite evitar que o programa gere um exame que o funcionário já fez dentro do período de tempo estipulado no parâmetro, baseado na data do último exame agendado, para os casos onde os exames são efetuados em uma data periódica fixa para todos os funcionários.  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos eSocial SST](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004428991-MDT-eSocial)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
