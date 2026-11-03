---
article_id: 360015448732
category: Rescisão
content_hash: fbed2dd6839fcf74a5f3c2bd607ef3476166fcc31e65bda883413aa1b195d592
fetched_at: '2026-06-28T22:46:55.408115+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - GRRF: Tomador não encontrado'
type: support-article
updated_at: '2024-09-16T19:40:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015448732-RH-RM-FOP-GRRF-Tomador-n%C3%A3o-encontrado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura:**00:01:30 min**

**Ocorrência**No módulo **Totvs Folha de Pagamento**, ao gerar a rotina **GRRF**é apresentada a seguinte mensagem:   
**Erro ao gerar a GRRF:****System.Exception: Tomador não encontrado.****Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões

**Causa**Este erro ocorre, pois o sistema está parametrizado para utilizar Tomador de Serviço em **Configurações | Parametrizador | Folha de Pagamento | Folha Normal | Tomador de Serviço** e antes de Gerar a GRRF não foi executado o processo Distribuir SEFIP.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
1**.** Acesse **Encargos | SEFIP | Distribuir SEFIP** e execute a distribuição.   
2**.** Após finalizar com sucesso, acesse **Encargos | SEFIP | Editar distribuição SEFIP**.Na tela de edição de distribuição da SEFIP serão listados todos os funcionários que tiveram algum valor distribuído;  
3. Para identificar melhor os funcionários e seus movimentos, filtre pelo mês ou pelo ano do movimento clicando no ícone **Procurar.** Escolha como deseja procurar, informe a data e clique no binóculo à direita. Caso queira visualizar somente sua pesquisa, clique no botão **Ocultar Registros**conforme imagem abaixo:  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360010637711/mceclip0.png)   
  
4**.** Após seguir os passos acima gere novamente a GRRF.
