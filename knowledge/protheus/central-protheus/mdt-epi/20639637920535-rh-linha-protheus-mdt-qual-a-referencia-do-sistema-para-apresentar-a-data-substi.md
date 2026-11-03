---
article_id: 20639637920535
category: MDT - EPI
content_hash: 10baffd0230a47b129f304ebee95cff1d9f26ec7fa47c56bbe0af117e7225f11
fetched_at: '2026-06-28T22:44:25.527808+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Qual a referencia do sistema para apresentar a
  Data Substituição do EPI no Relatório de Substituição de EPI (MDTR815)
type: support-article
updated_at: '2024-01-17T13:37:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20639637920535-RH-Linha-Protheus-MDT-Qual-a-referencia-do-sistema-para-apresentar-a-Data-Substitui%C3%A7%C3%A3o-do-EPI-no-Relat%C3%B3rio-de-Substitui%C3%A7%C3%A3o-de-EPI-MDTR815
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20639637907735) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual a referencia do sistema para apresentar a Data Substituição do EPI no Relatório de Substituição de EPI (MDTR815)?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**No cadastro do EPI x Fornecedor o campo **Dias Utiliz (TN3\_DURABI)** Durabilidade do EPI, indica a quantidade de dias que o EPI pode ser utilizado pelo funcionário. Esta informação será utilizada para calcular a data de substituição do EPI.  
  
Não temos uma tolerância para substituição deve ser cumprido os valores estabelecidos.  
  
O sistema consulta o cadastro do *fornecedor x EPI* para o campo durabilidade que pode ser **Geral** ou **USO**.   
O sistema considera essa Durabilidade para projetar a substituição deste epi, contando a partir da entrega do mesmo e conforme a seleção se é uso geral ou USO.   
**Geral** conta os dias corridos.  
**USO** vai considerar somente os dias usados, descontando os dias afastados, férias, dias não trabalhados. (COMPENSADO, DSR são dias que o funcionário não trabalhou).  
  
Necessário ter o cadastro do Epi > Epi x Fornecedor, relacionar o epi ao fornecedor e informar uma durabilidade para o epi.  
Selecionar o funcionário e realizar a entrega do epi, sempre que o tempo de durabilidade do epi esteja ultrapassado ao emitir o Relatórios > Epi > Substituição Epi. Será listado a informação.  
  
A rotina *MDTR81*5, com a opção "**Substituir**" exibe os EPI's á substituir e não os EPI's que estão com a vida útil ultrapassada.  
Para que seja exibido os EPI's que estão com a vida útil ultrapassada ou qual é a data que deve ser devolvido o EPI, deve ser adicionado no parâmetro "**Devolver**". Consulte para maiores informações:  
[RH - Linha Protheus - MDT - Como emitir o Relatório de Substituição de EPI (MDTR815)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060011513-RH-Linha-Protheus-MDT-Como-emitir-o-Relat%C3%B3rio-de-Substitui%C3%A7%C3%A3o-de-EPI-MDTR815-?source=search)  
  
**Saiba Mais**  
[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Artigos EPI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945554-MDT-EPI)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
