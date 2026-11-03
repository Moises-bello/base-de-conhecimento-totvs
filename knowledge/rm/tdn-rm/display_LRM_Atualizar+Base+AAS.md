---
content_hash: 98d962a02e81dd50ffcf3ca773ba2dc1da11979135fbab87b4b7b73c58af25ae
fetched_at: '2026-06-29T00:10:10.395552+00:00'
page_id: '452719823'
product: rm
source: tdn-rm
title: Atualizar Base AAS
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualizar+Base+AAS
version: 3
---

falseATENÇÃO:

A partir da release **12.1.2606**, esta rotina foi descontinuada, pois sua funcionalidade passou a ser atendida pelo **eSocial**.

**Atualizar Base AAS**   
Para a execução do processo o usuário terá como parâmetro a competência inicial e final na qual se deseja efetuar a atualização, juntamente com um filtro de Seleção de Funcionários, caso seja necessário efetuar a atualização apenas de alguns funcionários.

* Acessar Folha de Pagamento, aba Folha Mensal, grupo Relatórios da Folha - Atualizar Base AAS.
* Realizar na parametrização o intervalo da competência que deseja atualizar e caso necessário o filtro de funcionários e executar o processo.  
  A rotina realizará a atualização da Base AAS conforme os lançamentos da ficha financeira do período parametrizado .  
  Através da rotina a composição da tabela PFAAS será ajustada corretamente possibilitando a geração dos relatórios corretamente.  
  A rotina de Liberação de Competência deverá ser validada novamente, pois a rotina efetua a atualização da Base AAS (a mesma encontrava-se com problemas devido a situação foi necessária a criação da rotina para atualizar as competências já fechadas)  
  Ambos os processos devem efetuar a inserção de valores na tabela PFAAS conforme os grupos no cadastro de eventos.  
     
  **Observação**  
  Caso as atualizações da base AAS não forem geradas na liberação de competência através do parâmetro ''Processar Grupo AAS da Ficha Financeira'', deverão ser geradas pelo processo de atualização de base AAS em Folha mensal | Relatórios da Folha | Atualizar Base AAS.

falseImportante!

O Atestado de Afastamento e Salários foi substituído pelo CNIS - Cadastro Nacional de informações Sociais, com isso esse menu está sendo descontinuado e não terá mais manutenção ou evolução.  
Veja mais detalhes em:<https://tdn.totvs.com/pages/releaseview.action?pageId=741313313>
