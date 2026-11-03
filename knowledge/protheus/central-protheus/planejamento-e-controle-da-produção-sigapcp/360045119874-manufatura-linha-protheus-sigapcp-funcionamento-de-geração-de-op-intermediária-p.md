---
article_id: 360045119874
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 30a463bb1e1f5271c2fa8966c45fabeb164f0bf63193b310a065d873af972c0a
fetched_at: '2026-06-28T22:42:43.320920+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Funcionamento de geração de OP intermediária
  para produtos com apropriação indireta
type: support-article
updated_at: '2022-04-01T13:08:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045119874-Manufatura-Linha-Protheus-SIGAPCP-Funcionamento-de-gera%C3%A7%C3%A3o-de-OP-intermedi%C3%A1ria-para-produtos-com-apropria%C3%A7%C3%A3o-indireta
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:03:00 min**  
**Dúvida**Quais as regras e parâmetros o Sistema considera na geração de **OP intermediária** para produtos com **apropriação indireta**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**  
Quando o parâmetro **MV\_OPIPROC** possui o conteúdo **.T.** e o parâmetro **Consulta Só Armazém Padrão?** possui o conteúdo **Sim**, o Sistema gera a **OP** **intermediária** e empenho no armazém de **apropriação indireta** e não faz a leitura de nenhum desses dados, empenho e previsão de entrada, ao analisar a disponibilidade de estoque para a segunda **OP**, gerando assim novamente a **OP intermediária**.  
  
Quando o parâmetro **MV\_OPIPROC** possui o conteúdo **.T.** e o parâmetro **Consulta Só Armazém Padrão?** possui o conteúdo **Não**, a **OP** intermediária é gerada para o armazém de **apropriação indireta** e o empenho é registrado para o mesmo armazém, ao avaliar a disponibilidade de estoque essas duas informações são consideradas se o armazém de **apropriação indireta** estiver no range de armazéns definidos nos parâmetros **Armazém De?** e **Armazém Até?**, gerando portanto a **OP intermediária**.  
  
Também quando **MV\_OPIPROC** possui o conteúdo **.F.** e o parâmetro **Consulta Só Armazém Padrão?** possui o conteúdo **Não**, para a segunda **OP** o Sistema identifica a entrada e saída prevista, desde que o armazém de **apropriação indireta** esteja no range dos parâmetros **Armazém De?** e **Armazém Até?**Já quando o parâmetro **MV\_OPIPROC** possui o conteúdo **.F.** e o parâmetro **Consulta Só Armazém Padrão?** possui o conteúdo **Sim**, para a segunda a **OP** o Sistema identifica a entrada em estoque, pois a **OP intermediária** foi gerada para o armazém padrão, mas não identifica a saída, que está registrada no armazém de apropriação indireta, sendo assim a segunda **OP** **intermediária** não é gerada.  
  
Por fim, para que o Sistema gere corretamente a **OP** intermediária considerando a quantidade empenhada no armazém de **apropriação indireta**, uma das três combinações abaixo deve ser adotada:

* **MV\_OPIPROC** com conteúdo igual a **.T.** e **Consulta Só Armazém Padrão?** com conteúdo **Não**;
* **MV\_OPIPROC** com conteúdo igual a **.T.** e **Consulta Só Armazém Padrão?** com conteúdo **Não**, porém o armazém de **apropriação** indireta deve estar no range de parâmetros **Armazém De?** e **Armazém Até?**;
* **MV\_OPIPROC** com conteúdo igual a **.F.** e **Consulta Só Armazém Padrão?** com conteúdo **Não**.

**Importante**  
Os parâmetros **Consulta Só Armazém Padrão?**, **Armazém De?** e **Armazém Até?** são acessados através do **F12** do **MATA650**.  
  
**Glossário**  
**PI** - Produto Intermediário  
**OP** - Ordem de Produção  
**MATA650** - Ordens de Produção  
**MV\_OPIPROC** - Indica se o saldo de **OP's Intermediárias** de semi-acabados geradas automaticamente pelo Sistema deve ser destinado ao local de processo
