---
article_id: 4441139391767
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: d59a653442e3d3f7662dace960bd66c2a55ba21831d0af30b031ad0e578487f0
fetched_at: '2026-06-28T22:47:29.417346+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH- Dicas para melhorar a performance do Meu RH
type: support-article
updated_at: '2026-06-09T18:05:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4441139391767-RH-RM-Meu-RH-Dicas-para-melhorar-a-performance-do-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22215978346263) Tempo aproximado para leitura: **00:07:46 min**  
  
**Ocorrência**  
Quando você acessa o Meu RH, pode enfrentar **problemas de lentidão**. Como identificar a **causa da baixa performance** e quais são as melhores práticas para **melhorar a performance** do Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.27  
  
**Causa**  
A lentidão no Meu RH pode ser causada por diversos fatores, incluindo configurações do ambiente, um grande número de acessos simultâneos,  quantidade de licenças utilizadas, e o desempenho da infraestrutura atual.  
  
**Solução**  
Criamos uma **documentação** conforme link abaixo, que detalha todas as **configurações** recomendadas para **melhorar a performance** do Meu RH. Recomendamos que você leia **atentamente** toda a documentação preparada. Se, após seguir essas orientações, o problema persistir, **continue consultando o restante deste KCS** para mais informações e soluções adicionais.  
  
[Clique aqui para acessar o documento das melhores práticas específicas para o Meu RH !!!](https://tdn.totvs.com/pages/viewpage.action?pageId=860246669)  
  
Se, mesmo seguindo **todas orientações acima**, continuar enfrentando problemas de desempenho na usabilidade do Meu RH, **verifique** os itens listados abaixo:  
  
**1. Quantidade de Licenças: Consumo ao Atingir o Limite**  
  
Quando o número de licenças do Meu RH atinge seu limite, os usuários não recebem uma mensagem de erro. Em vez disso, o sistema se torna mais lento, pois as requisições ficam em espera até que novas licenças sejam liberadas no pool. Essa espera causa uma **lentidão geral** no uso do Meu RH.  
  
Para verificar se essa é a causa, acesse o **Monitor de Licenças** e acompanhe o uso durante os **horários de pico da empresa**. As licenças utilizadas pelo Meu RH são: 4177, 4001, 4000, 4099 e 4016.  
  
[Clique aqui para acessar o documento de como monitorar as licenças em tempo real](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9218011037079-Framework-Linha-RM-Frame-Monitorar-uso-de-licen%C3%A7as-em-tempo-real)  
  
[Clique aqui para acessar o documento sobre maiores explicações sobre o funcionamento do consumo das licenças do Meu RH.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/25510214148119-RH-RM-Meu-RH-Como-as-licen%C3%A7as-no-Meu-RH-s%C3%A3o-consumidas)  
  
Caso identifique que estão chegando muito **próximo ao limite**,  entre em contato com o seu **ESN** (Executivo de Soluções de Negócio) para avaliar a necessidade de **adquirir mais licenças.**  
  
**2. Desempenho da Infraestrutura: Processamentos, Memória ou Banco de Dados Atingindo Níveis Críticos**  
  
Assim como no item 1, durante os horários de pico, é  essencial monitorar o **servidor onde o Meu RH está instalado**, também o **servidor de aplicação** que hospeda o Host consumido pelo Meu RH e, finalmente, o **servidor do banco de dados**. Todos esses servidores devem ser acessados e monitorados rigorosamente. Fique atento aos níveis de processamento e memória; se esses níveis se aproximarem de **90%**, a **performance** do Meu RH pode ser **significativamente afetada.**  
  
Caso identifique algum **nível crítico**, considere a possibilidade de **dimensionar o hardware**. Para orientações sobre as recomendações de dimensionamento, [consulte nosso **documento de Portabilidade** clicando aqui.](https://tdn.totvs.com/display/LRM/Portabilidade)

**Recomendações Relacionadas à Infraestrutura:**  
  
**2.1** Importante utilizar servidores de aplicação (serviços de hosts) dedicados para o Meu RH, assim não terá concorrências com acessos e processamento do ERP RM.  
  
**2.2** Avalie a possibilidade de aumentar a quantidade de Hosts utilizados pelo Meu RH.

**3. Inconsistência na Estrutura de Seção do Módulo Folha de Pagamento, Causando Lentidão no Meu RH**  
  
Quando a coluna **CODIGOPAI** e a coluna **CODIGO** na tabela **PSECAO** possuem o mesmo identificador, isso pode causar uma queda repentina do Host ou instabilidade e lentidão no Meu RH. Para ajudar a identificar e solucionar esse problema, criamos um KCS específico que demonstra como resolver esse incidente.  
  
[Clique aqui para acessar o documento para identificar e solucionar a lentidão causada na estrutura de seção que afeta o Meu RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002471482-RH-RM-Meu-RH-Instabilidade-e-lentid%C3%A3o-gerando-erros-no-acesso-ao-Meu-RH)  
  
**4. Se a lentidão estiver de forma generalizada, ou seja, em qualquer processo, qualquer módulo, sugerimos verificar a documentação abaixo:**  
[Framework - Framework RM - BD - Orientações Gerais para Otimização de Performance](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027943052-Framework-Framework-RM-BD-Orienta%C3%A7%C3%B5es-Gerais-para-Otimiza%C3%A7%C3%A3o-de-Performance)

**Importante**  
Se houver necessidade de investigação mais aprofundada em seu ambiente, temos nosso serviço TIS. O Infraestrutura de Sistemas é o serviço especializado de análise, sustentação e evolução da infraestrutura que suporta os sistemas de gestão da TOTVS.  
Para maiores detalhes, segue link [**TIS**](https://produtos.totvs.com/ficha-tecnica/tudo-sobre-o-servico-infraestrutura-de-sistemas/)

**Saiba mais**  
Para avaliar locks no banco, segue documentação para base SQL:  
[Framework - Framework RM - BD - Como verificar Deadlock no SQL Server](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003068212-Framework-Framework-RM-BD-Como-verificar-Deadlock-no-SQL-Server)  
  
Como apoio, para auxiliar no monitoramento do ambiente, segue documentação sobre o Sentinela:  
[Framework - Framework RM - BD - Sentinela RM Ferramenta de Monitoramento de Ambientes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007212312--Framework-Framework-RM-BD-Sentinela-RM-Ferramenta-de-Monitoramento-de-Ambientes)  
  
Confira também, como melhorar o desempenho de outros Produtos do RH:  
[RH - RM - FOP- Dicas para melhorar a performance da Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41083949075863-RH-RM-FOP-Dicas-para-melhorar-a-performance-da-Folha-de-Pagamento)  
[RH - RM - PTO- Dicas para melhorar a performance do Automação de Ponto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/41002575739287-RH-RM-PTO-Dicas-para-melhorar-a-performance-do-Automa%C3%A7%C3%A3o-de-Ponto)
