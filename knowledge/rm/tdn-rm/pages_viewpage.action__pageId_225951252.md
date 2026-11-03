---
content_hash: 4d6d1fdc7fa367380c453a713e1c4522d7a933e44f6797dcb7d4b013a8e76908
fetched_at: '2026-06-29T00:06:26.550985+00:00'
page_id: '225951252'
product: rm
source: tdn-rm
title: Informações importantes sobre o processo de migração
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225951252
version: 2
---

**FAQ - Como fazer o Upgrade para o TOTVS Educacional?**

**• O que é mais importante no processo de Upgrade?**

O mais importante neste processo é entender que o TOTVS Educacional é uma nova versão com evoluções tecnológicas, porém com uma estrutura de dados diferente. São novas tabelas e novos conceitos. Praticamente é uma nova implantação.

**• Como é feita a migração de dados?**  
Existe um importador de dados, com layout de arquivos TXT. Porém a TOTVS não oferece nenhuma ferramenta de extração de dados das versões RM Classis Ensino Básico e RM Classis Ensino Superior. Além disso, existe um Migrador de dados, que é um produto que migra os dados das tabelas do RM Classis EB e ES para o TOTVS Educacional.

**• Quais os principais pontos de atenção quanto ao uso deste Migrador de dados?**

Um Migrador de dados como este, é um produto extremamente complexo, que precisa lidar com um conjunto muito grande de variações de dados existentes nas bases dos nossos clientes. Por isso, cada migração é uma nova realidade de execução do migrador.Isso quer dizer que em cada projeto podem surgir situações ainda não previstas e conseqüentemente não tratadas pelo Migrador. **Portanto a instituição deve validar todos os registros migrados, antes de entrar em produção. Identificando alguma inconsistência ou dúvida registrar um chamado com o suporte para que o caso seja especificado.**

**• Como podem ter situações não tratadas, qual a menor forma de conduzir um processo de venda e execução do Upgrade?**

O ideal é termos um planejamento prévio e que considere que a validação da migração é um processo cíclico, e que o número de repetições desse processo varia de acordo com a complexidade e tamanho da base de dados do cliente. Uma métrica para servir como base é um ciclo de 3 validações, cada validação com 1 semana de trabalhos (conversão + ajustes + validação dos dados). Neste cenário, uma migração prévia é um bom ponto de partida para mensurar os prazos de uma o período de validação. O CDBH pode dar apoio nessa migração prévia, E já sinalizando quais são os pontos de atenção ou já identificando situações não tratadas anteriormente. Caso esse apoio seja necessário, é interessante avisar com antecedência, para que haja um planejamento.

**• Qual o apoio que a TOTVS oferece neste processo?**

No processo de importação, oferecemos o apoio da nossa equipe de suporte para tirar dúvidas. No processo de migração, oferecemos o apoio da equipe de desenvolvimento para analisar os erros encontrados e fazer algumas conversões de teste, desde que planejado com antecedência. **Lembrando novamente que é de responsabilidade do cliente a verificação dos dados entre origem x destino, antes da entrada em produção. O log gerado pelo aplicativo apenas apresenta algumas falhas já tratadas e erros de banco de dados. O conteúdo inserido em cada tabela deve ser verificado pela instituição, antes da entrada em produção e em caso de dúvidas/inconsistências o suporte Educacional deve ser acionado (através da comunidade R@ Educacional no Fluig, Portal da TOTVS, ou telefone 4003-0015).**

**• Tudo é migrado automaticamente?**

**Não**. É importante ressaltar que no processo de importação ou migração, somente dados são contemplados. Relatórios, Fórmulas, Consultas SQL, Gráficos, Cenários, etc. não são migrados e precisam ser refeitos.

**• Como funciona o treinamento na nova ferramenta?**

Funciona como os outros produtos da Linha RM. O treinamento pode ser contratado presencialmente ou via EAD.  
  
**• Quanto tempo leva um processo completo de Upgrade?**

É muito difícil prever esse tempo. Na verdade, é um novo projeto de implantação, com uma facilidade que é o migrador de dados. O processo como um todo precisa levar em consideração os tempos de validação, treinamento, migração de dados, confecção dos novos relatórios, fórmulas, etc.

**Como é a performance do Migrador?**

O tempo de migração de dados varia muito de acordo com o volume de dados do cliente e a infra-estrutura disponível. Seguem alguns números de referência:

Base de 7 GB com 200 mil matriculas e 500 mil lançamentos:  
12 hs migração - 3 maquinas paralelas

Base de 200 GB com 1 milhão matriculas e 8 milhões lançamentos:  
18 hs migração - 11 maquinas paralelas

**• O migrador faz a unificação de bases? Ou seja, se eu tenho duas bases de dados ele consegue migrar e unificar as bases?**

Não. O migrador só migra para uma mesma base de dados e mesma coligada.

**• Caso existam inconsistências na base de dados atual, o conversor corrige?**

Não. Caso o conversor encontre alguma inconsistência ele gera um Log e o cliente precisa fazer os ajustes na base atual para continuar a migração.

**• Como conseguir o migrador?**

Atualmente o migrador pode ser conseguido através do Suporte Educacional.

**• Todas as funcionalidades do RM Classis EB e ES estão no TOTVS Educacional?**

A TOTVS definiu que alguns poucos recursos não seriam implementados no TOTVS Educacional, devido à especificidade deles ou pouca utilização pelo mercado nacional e internacional. Alguns exemplos: Controle de acesso direto com integração com catraca eletrônica, Organograma, Controle de entrega de material didático, Integração com MS Excel e Diário ótico (os dois últimos estão sendo preteridos pelo mercado frente a utilização do Portal).  
  
**• As customizações feitas para o RM Classis EB e RM Classis ES funcionam para o TOTVS Educacional?**

Não. As customizações não são migradas pelo Migrador e não funcionam para a nova versão. Algumas customizações feitas por limitações do RM Classis EB e RM Classis ES já são supridas pelo TOTVS Educacional. Porém é preciso fazer uma análise criteriosa do recurso no novo produto. Caso o recurso não seja atendido nativamente, a customização precisa ser migrada. Neste caso, a equipe responsável pela customização precisa ser acionada desde o início do projeto de Migração, para que todas as ações sejam tomadas com antecedência.
