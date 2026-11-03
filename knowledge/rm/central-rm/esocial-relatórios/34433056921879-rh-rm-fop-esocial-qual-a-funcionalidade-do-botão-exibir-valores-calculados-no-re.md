---
article_id: 34433056921879
category: eSocial - Relatórios
content_hash: 26641f5dd424de0505ac0763625a00b368354dcb35f9d28a802a9aaa6c168591
fetched_at: '2026-06-28T22:47:04.893541+00:00'
product: rm
section_id: 1500000861002
source: central-rm
title: RH - RM - FOP - eSocial - Qual a funcionalidade do botão 'Exibir Valores Calculados'
  no Relatório de INSS Patronal
type: support-article
updated_at: '2026-06-05T17:18:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34433056921879-RH-RM-FOP-eSocial-Qual-a-funcionalidade-do-bot%C3%A3o-Exibir-Valores-Calculados-no-Relat%C3%B3rio-de-INSS-Patronal
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34433041991575) Tempo aproximado para leitura: **00:02:00min**  
  
**Dúvida**  
Qual a funcionalidade do botão 'Exibir Valores já Calculados' no relatório de INSS?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Versões de Mercado.  
  
**Solução**  
Sempre que este parâmetro estiver desmarcado o sistema irá buscar os valores de INSS com base no envelope de pagamento com o valores retornados do RET (S-5011), caso contrário será utilizados os valores retornados na ultima geração do relatório.  
Ou seja, o parâmetro somente deve ser marcado em casos de re-geração do relatório onde não houve alteração de dados.  
É importante ressaltar, que caso o usuário tenha realizado alguma modificação em dados que impactam os cálculos, é imprescindível que o parâmetro esteja desmarcado, para o sistema trazer a informação atualizada.

**Exemplo quando utilizar o parâmetro marcado:**

O usuário gerou o relatório com o parâmetro desmarcado, não fez nenhuma alteração em dados que impactam os cálculos e deseja apenas gerar novamente o relatório.

**Saiba Mais:**

[Relatório de Conferência INSS Patronal](https://tdn.totvs.com/pages/releaseview.action?pageId=714242305)
