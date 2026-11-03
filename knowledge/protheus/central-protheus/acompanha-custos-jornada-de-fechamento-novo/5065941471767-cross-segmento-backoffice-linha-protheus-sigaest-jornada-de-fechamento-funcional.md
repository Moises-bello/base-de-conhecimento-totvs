---
article_id: 5065941471767
category: ACOMPANHA CUSTOS - JORNADA DE FECHAMENTO (NOVO)
content_hash: 1e9dde8460be88a8377c06e962de348ade518bf4b8566380f1bbd6f66f09c09c
fetched_at: '2026-06-28T22:38:48.139256+00:00'
product: protheus
section_id: 5367899706647
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Jornada de Fechamento
  - Funcionalidade do botão  "Configuração de Parâmetros" '
type: support-article
updated_at: '2025-03-12T12:23:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065941471767-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Jornada-de-Fechamento-Funcionalidade-do-bot%C3%A3o-Configura%C3%A7%C3%A3o-de-Par%C3%A2metros
---

**Dúvida**Como configurar os parâmetros inicias, da rotina Acompanha Custos?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Protheus Release 12.1.33.

**Solução**

#### **Configuração de Parâmetros - Jornada de Fechamento**

**Introdução:**

A funcionalidade Configurar Parâmetros foi disponibilizada para definir as configurações prévias de recálculo de custo médio e fechamento para virada de saldo, essa configuração é considera para cada filial, dessa forma, caso seja realizado o processamento em mais de uma  filial será possível tratar as particularidades de processamento.

* No primeiro acesso o sistema vai capturar as últimas configurações da tabela Cadastro de pergunte Protheus (SX1) retornando em tela somente para validação, **com uma ressalva** dos parâmetros do tipo string (caractere) pois esses devem ser informado na primeira utilização ou serão considerados com o seu conteúdo em branco.

![](https://tdn.totvs.com/download/attachments/572499747/profile.gif?version=1&modificationDate=1643216674380&api=v2)

**Como utilizar Configurar Parâmetros do Acompanha Custos**

**Utilização**

Acessível através da opção de menu Fechamentos botão Configurar Parâmetros. Ao realizar a configuração o sistema vai gravar em seu perfil com a filial que realizou a configuração para processamento.

**Alterar Configurações**

Em caso de necessidade de alteração de alguma configuração de processamento basta acessar a rotina, o sistema vai resgatar as informações do perfil e depois de alterar clicar em Salvar Configurações novamente para que as novas configurações sejam salvas.

**Restaurar configurações**

E possível restaurar as configurações padrões mediante ao Cadastro de pergunte Protheus (SX1), para isso basta acessar a rotina e clicar no botão Restaurar Padrão**.**

**Detalhamento de cada Parâmetro**

**Seção definições gerais**

| **Parâmetro** | Recalcular custos de transportes |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Recalcula os custos dos movimentos internos de transporte. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Calcular custo em partes |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Indica se o cálculo do custo em partes será executado. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Cálculo de mão de obra |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Recalcula a mão de obra no recálculo do custo médio através dos valores contábeis do centro de custo relacionado a MOD. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | % de aumento da MOD |
| --- | --- |

| **Tipo** | Texto |
| **Descrição** | Percentual a ser adicionado ao custo médio da mão de obra. |
| **Valor** | 0 a 100 |

| **Parâmetro** | Sequência de cálculo |
| --- | --- |

| **Tipo** | Seleção |
| **Descrição** | Mostra em tela a sequência em que será feito o recálculo do custo médio antes do processamento. |
| **Valor** |  |

| **Parâmetro** | Sequência processamento FIFO |
| --- | --- |

| **Tipo** | Seleção |
| **Descrição** | Indica se a sequência de processamento do FIFO será a mesma do custo médio ou se respeitará a data e a sequência de digitação. |
| **Valor** |  |

**Seção movimentações internas**

| **Parâmetro** | Gerar estrutura pela movimentação |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Gerar uma estrutura para cada produto baseada nas movimentações?  Habilitado: O sistema irá montar uma estrutura temporária, nos moldes da estrutura de produtos (SG1), só que baseada nas movimentações existentes.  Desabilitado: O sistema irá utilizar a estrutura do produto já existente (SG1).  OBS.:  1. Empresas que NÃO possuam estrutura de produtos cadastrados ou que façam requisições manuais podem marcar '' a este parâmetro.  2. Caso selecione certifique-se que não existam referências circulares nas movimentações (Ex.: Requisitar um produto para a produção dele mesmo). |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Recalcular níveis de estrutura |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Recalcular os níveis das estruturas dos produtos para garantir a correta nivelação dos componentes nas estruturas?   OBS.: Quando habilitada a geração de estrutura pelas movimentações (Gerar estrutura pela movimentação - parâmetro anterior) o recálculo de níveis será processado obrigatoriamente para poder nivelar as estruturas temporárias geradas. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Atualizar arquivos de movimento |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Atualizar o arquivo de movimentações internas (SD3)?   OBS.: Os outros arquivos de movimentos (SD1, SD2, SDB, SD5) são SEMPRE atualizados. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Apagar estornos |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Após o recálculo, excluir da base de dados dos movimentos estornados? |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Movimentos internos valorizados |
| --- | --- |

| **Tipo** | Seleção |
| **Descrição** | Processa os movimentos internos valorizados antes ou depois dos demais movimentos internos. |
| **Valor** |  |

**Seção lançamentos contábeis**

| **Parâmetro** | Mostra lançamentos contábeis |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Mostra em tela a sequência em que será feito o recálculo do custo médio antes do processamento  OBS.: Recurso não disponível. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Aglutina lançamentos contábeis |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Indica se os lançamentos contábeis a serem gerados no recálculo do custo médio serão gerados aglutinados. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Centro de custo |
| --- | --- |

| **Tipo** | Seleção |
| **Descrição** | Tipo de centro de custo: Contábil.  SIGACON: será considerado o saldo do SI1 (descontinuado).  SIGACTB: será considerado o saldo CT7.  OBS.: Somente ativo extracontábil devido ao SIGACON ter sido descontinuado. |
| **Valor** |  |

| **Parâmetro** | Conta contábil inibir de: |
| --- | --- |

| **Tipo** | Texto |
| **Descrição** | Conta contábil inicial a ser inibida na filtragem do recálculo do custo médio. |
| **Valor** |  |

| **Parâmetro** | Conta contábil inibir até: |
| --- | --- |

| **Tipo** | Texto |
| **Descrição** | Conta contábil final a ser inibida na filtragem do recálculo do custo médio |
| **Valor** |  |

| **Parâmetro** | Gerar lançamento contábil |
| --- | --- |

| **Tipo** | Seleção |
| **Descrição** | Gerar  lançamentos contábeis no recálculo dos custo médio?  SIM: gera lançamentos contábeis.  NÃO: apaga lançamentos contábeis.  MANTÉM LCTOS: mantém lançamentos contábeis. |
| **Valor** |  |

**Seção fechamento**

| **Parâmetro** | Gera saldo inicial para mão de obra |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Indica se deve gerar registros de saldo inicial para produtos mão de obra (MOD) no processo de virada de saldos. |
| **Valor** | Habilitado ou desabilitado |

| **Parâmetro** | Atualiza saldo atual não de obra |
| --- | --- |

| **Tipo** | Flag |
| **Descrição** | Indica se atualiza o saldo atual de produtos com características mão de obra. |
| **Valor** | Habilitado ou desabilitado |

**Ações**

| **Rótulo** | Restaurar padrão |
| --- | --- |

| **Tipo** | Botão |
| **Descrição** | Restaura as configurações localizadas no Protheus SX1. |
| **Valor** |  |

| **Rótulo** | Salvar configurações |
| --- | --- |

| **Tipo** | Botão |
| **Descrição** | Salva no profile do usuário as configurações selecionadas. |
| **Valor** |  |

**Informações Técnicas**

Foi desenvolvido uma classe REST de controle para entrada e saída de dados através da linguagem TLPP, sendo responsável por gerações e gravações de registros nas tabelas de perfil de usuário do Framework

Especificações de Serviços, [Clique Aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=572499747#:~:text=Informa%C3%A7%C3%B5es%20T%C3%A9cnicas)

**Saiba mais**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - O que é a rotina Acompanha Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5065773526039)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Validação para inicia a rotina Acompanha Custos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/5240908654999)*
