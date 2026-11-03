---
article_id: 4409545197847
category: PCMSO / Exames
content_hash: 2679fd831291ba938d60d318e5a9c32b34951a52f06f99bea347c52843f6fa21
fetched_at: '2026-06-28T22:47:42.159119+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Importar o resultado de exames e/ou consultas médicas
type: support-article
updated_at: '2025-11-24T17:59:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409545197847-RH-RM-SMT-Importar-o-resultado-de-exames-e-ou-consultas-m%C3%A9dicas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036950074007) **Tempo aproximado para leitura: 00:01:30 min** **Dúvida**Como importar o resultado de exames e consultas medicas, através do Assistente de Importação de Resultado de exames ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - Todas as versões   
  
**Solução**Para importar os exames sigas os passos abaixo:

* Crie o arquivo XML com os dados da consulta e exames e funcionários.   
    
  Caso seja a primeira vez que importação irá ocorrer, é necessário relacionar os campos do XML com o campos do tabela do banco de dados:
* Acesse o menu PCMSO; Assist. Importação de Resultado de exames.   
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409550980887)
* Antes de importar o XML é necessário relacionar os campos do arquivo criado com os campos da tabela do RM. Para isso acesse o menu PCMSO > Assistente de Importação de Resultado de Exames, escolha a opção: "Relacionar Campos do Arquivo", avance etapa e escolha o arquivo a ser importado, relacione os campos. Por exemplo: "CODPESSOA" receberá o parâmetro "CÓDIGO".  
    
  ![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409544432407)
* Selecione o caminho onde o arquivo está salvo e avance e execute o processo:  
    
  ![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409544865175)
* Faça o relacionamento para a tabela de CONSULTA e EXAMES, e após realizar o relacionamento avance e execute o processo.  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/JQnZn2JE0ak8zmyIgULO1FhDw/?name=inline1777536799.png)  
    
  Para importa os exames e as consultas, acesse o assistente novamente e selecione a Opção Importar resultados dos exames.  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/25ZOstnjQPf0KDKvXQ0qfpzlG/?name=inline1086347718.png)
* Selecione o caminho onde o arquivo está salvo e avance e execute o processo:  
    
  ![](https://totvssuporte.zendesk.com/attachments/token/WeJYV3hvQ6REL5Hd29jBr8iyg/?name=inline1098946227.png)​

**Importante**

- A importação do resultado de exames, possui uma estrutura XML específica, sendo diferente da estrutura XML do evento S-2220. Portanto, é necessário inserir a estrutura XML relacionada ao Resultado de Exame para que não ocorra erros.

- Ao ser importado o arquivo XML, automaticamente será gerado o evento S-2220 e o mesmo irá ficar disponível para gerar o XML do eSocial.

**Saiba mais**Para maiores informações, acesse:

- [Importação de Resultado de Exames - Estrutura Arquivo XML](https://tdn.totvs.com/pages/releaseview.action?pageId=496396606)

- [Assistente de Importação de Resultado de Exames](https://tdn.totvs.com/pages/releaseview.action?pageId=452718895)
