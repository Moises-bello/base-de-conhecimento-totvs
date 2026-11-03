---
article_id: 14690636893207
category: Rescisão
content_hash: 10b80f81663589b793521e97c94019f44b8327822941901d5f0970fd190cd89a
fetched_at: '2026-06-28T22:46:54.226508+00:00'
product: rm
section_id: 1500000834561
source: central-rm
title: 'RH - RM - FOP - Rescisão: Não existe tabela IRRF com vigência apropriada ao
  período'
type: support-article
updated_at: '2025-02-12T18:25:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14690636893207-RH-RM-FOP-Rescis%C3%A3o-N%C3%A3o-existe-tabela-IRRF-com-vig%C3%AAncia-apropriada-ao-per%C3%ADodo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:01:49 min**

**Ocorrência**Ao tentar cadastrar uma rescisão, mesmo a tabela IRRF estando com as informações corretas, o sistema emite a seguinte mensagem: **Não existe 'Tabela de IRRF' com vigência apropriada ao período. Deseja estender a vigência do último valor cadastrado?** ![](https://centraldeatendimento.totvs.com/hc/article_attachments/14691552113943)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Causa**  
O sistema emite o aviso, pois a tabela de IRRF antiga foi copiada. Ou seja, o usuário realizou a cópia da tabela anterior e apenas editou/preencheu com as novas informações. Dessa forma, o sistema "entende" que a tabela anterior ainda está sendo utilizada para a realização do cálculo de rescisão.  
  
**Solução**  
Para que o sistema não emita o aviso e permita que o usuário cadastre a rescisão, é necessário efetuar o seguinte processo: 

1. Primeiramente, acesse **Administração de Pessoal | Cálculos | Tabelas de Cálculo**, procure pela tabela IRRF que está com as novas informações preenchidas e realize a exclusão:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/14691371391255)

2. Após exclusão, faça o cadastro da tabela nova ao invés de copiar a tabela anterior. Para isso, clique em Incluir e preencha as informações conforme o exemplo abaixo: 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/14691459340695)

3. Dessa forma, ao cadastrar a nova tabela realizando o processo desde o início, o sistema permite que o cadastro da rescisão seja executado.  
  
**Saiba Mais**  
[RH - RM - FOP - Tabelas de Cálculo: Vigência](RH%20-%20RM%20-%20FOP%20-%20Tabelas%20de%20C%C3%A1lculo:%20Vig%C3%AAncia)
