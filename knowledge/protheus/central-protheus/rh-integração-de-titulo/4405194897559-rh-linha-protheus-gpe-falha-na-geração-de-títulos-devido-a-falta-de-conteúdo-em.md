---
article_id: 4405194897559
category: RH - Integração de Titulo
content_hash: 438775b61e40fc05cf1ddeb189294496e26ec3724dad4133d2183a711f5bf288
fetched_at: '2026-06-28T22:43:36.336254+00:00'
product: protheus
section_id: 360004833693
source: central-protheus
title: RH - Linha Protheus - GPE - Falha na geração de títulos devido a falta de conteúdo
  em campos do cadastro de Fornecedor
type: support-article
updated_at: '2025-07-21T20:21:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405194897559-RH-Linha-Protheus-GPE-Falha-na-gera%C3%A7%C3%A3o-de-t%C3%ADtulos-devido-a-falta-de-conte%C3%BAdo-em-campos-do-cadastro-de-Fornecedor
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33616839679511)** Tempo aproximado para leitura: **00:02:00 min**

**Ocorrência**Falha na geração de títulos devido a falta de conteúdo em campos do cadastro de Fornecedor.  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.  
  
**Causa**O log de ocorrência é apresentado devido a ausência de conteúdo em um dos campos da tabela SA2 - Fornecedores que no Padrão do Protheus não é obrigatório.  
A rotina **GPEM650 - Geração** de títulos no processo esta criando o cadastro de Fornecedor para o funcionário apontado nos parâmetros de geração, uma vez que o mesmo ainda não possui este cadastro, o campo em questão por não ser um dos campos obrigatórios no Padrão esta sendo gravado sem conteúdo, por estar definido como obrigatório a rotina **MATA020 - Fornecedores** não permite que o mesmo seja finalizado, segue a relação de campos obrigatórios no Padrão:  
Código - A2\_COD  
Loja - A2\_LOJA  
Razão Social - A2\_NOME  
N Fantasia - A2\_NREDUZ  
Endereço - A2\_END  
Estado - A2\_EST  
Município - A2\_MUN  
Tipo -  A2\_TIPO  
  
**Solução**

Erro apresentado:  **![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405194384023)**  
Para solucionar essa ocorrência:  primeiramente deve ser verificado o campo informado no log, no exemplo acima esta sendo apontado o **A2\_COD\_MUN - Cod. Municip**1- Desabilitar a obrigatoriedade do campos, através do módulo **Configurador - SIGACFG**.  
Obs.: Esse procedimento deverá ser alinhado com o setor responsável devido à posterior utilização em relatórios e consultas.

Acessar: **Configurador ->Base de Dados ->Dicionário ->Arquivos ->Tabela SA2** ->Campo A2\_COD\_MUN / Aba **Uso** e desmarcar o campo **Obrigatório**:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4405188339223)  
  
Já existe uma solicitação de melhoria com data de 2018, para permitir a criação do cadastro apenas com as informações do Padrão, desconsiderando os campos definidos como obrigatórios pelo cliente, mas até o presente momento a mesma não foi aprovada, sendo assim a solução consiste na execução deste procedimento.  
  
**Saiba Mais**  
[Artigos sobre Integração de Título](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360004833693-RH-Integra%C3%A7%C3%A3o-de-Titulo)
