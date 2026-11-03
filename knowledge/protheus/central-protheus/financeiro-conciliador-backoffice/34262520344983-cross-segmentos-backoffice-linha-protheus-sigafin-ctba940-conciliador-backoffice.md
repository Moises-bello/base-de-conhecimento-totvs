---
article_id: 34262520344983
category: Financeiro - Conciliador Backoffice
content_hash: 4b40615f0065ffa75f20be0cd297f1e2774f7a387a70808c0f017953de0210ed
fetched_at: '2026-06-28T22:37:47.193465+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Conciliador
  Backoffice Financeiro - Ao "Aplicar Conciliação" registros na aba "Dados da Conciliação"
  não marcando os campos E5_RECONC=X , FK5_DTDISP=AAAMMDD ou registros não indo para
  aba "
type: support-article
updated_at: '2025-08-20T11:53:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34262520344983-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Conciliador-Backoffice-Financeiro-Ao-Aplicar-Concilia%C3%A7%C3%A3o-registros-na-aba-Dados-da-Concilia%C3%A7%C3%A3o-n%C3%A3o-marcando-os-campos-E5-RECONC-X-FK5-DTDISP-AAAMMDD-ou-registros-n%C3%A3o-indo-para-aba
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34262523528471) Tempo aproximado para leitura: **00:15:00 min**  
  
**Dúvida**  
CTBA940 - Conciliador Backoffice Financeiro - Ao "Aplicar Conciliação" registros na aba "Dados da Conciliação" não marcando os campos E5\_RECONC=X , FK5\_DTDISP=AAAMMDD ou registros não indo para aba "Dados da Conciliação" após conciliar na aba "Dados não encontrados"  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release  12.1.2310

Qual motivo do problema:  
Caso o ambiente tenha algum tipo de problema de base de dados, poderá acontecer essa ação de não gravação dos campos E5\_RECONC=X , FK5\_DTDISP=AAAMMDD ao "Aplicar Conciliação" registros na aba "Dados da Conciliação

**1 Ponto de análise**

Verificar se os tamanhos de campos estão iguais. Verificar tanto no dicionário (SX3) como no banco de dados

IG\_VLREXT == FK5\_VALOR  
IG\_VLRMOV == FK5\_VALOR  
IG\_DTMOVI == FK5\_DTDISP  
IG\_AGEMOV == FK5\_AGENCI  
IG\_CONMOV == FK5\_CONTA  
IG\_HISMOV == FK5\_HISTOR  
IG\_NATMOV == FK5\_NATURE

Observação: Segue uma imagem do tamanho de campo no banco de dados.

Abrir a tabela que irá verificar em top connect

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34262520305687)

Depois acessar a opção "Arquivo > Estrutura"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34262520307735)

E neste exemplo podemos observar que o tamanho do meu campo **IG\_HISMOV** no banco de dados tem o tamanho **40 caracteres**.

Caso o tamanho do campo **FK5\_HISTOR** esteja diferente, irá apresentar problemas.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34262523533975)

**2  Ponto de análise**

Caso os campos **IG\_MSUIDT, FK5\_MSUIDT, E5\_MSUIDT** referente aos títulos a serem conciliados estejam **sem conteúdo,** poderá apresentar problemas ao conciliar.

**Possível problema:** As tabelas SIG, FK5 e SE5 foram criadas com problemas de estrutura, possivelmente devido a falhas no processo de migração ou troca de modelo de banco de dados (por exemplo, de SQL Server para Oracle), sem que os procedimentos corretos tenham sido seguidos.

**3 Ponto de análise para banco ORACLE:**

Na query abaixo, podemos alterar a consulta das **tabelas** a serem verificadas através da coluna **TABLE\_NAME** alterando para **SIG, FK5 e SE5**

E podemos alterar a consulta dos **campos** a serem verificadas através da coluna **COLUMN\_NAME** alterando para **IG\_MSUIDT, FK5\_MSUIDT, E5\_MSUIDT**

**No exemplo** abaixo vamos executar a query no banco **Oracle** para a tabela **SIG**, para verificar a estrutura do campo **IG\_MSUIDT**

    SELECT  
   COLUMN\_NAME,              -- Nome da coluna  
   DATA\_TYPE,                -- Tipo de dado  
   DATA\_LENGTH,              -- Tamanho do campo  
   COLUMN\_ID,                -- Posição da coluna na tabela  
   NULLABLE,                 -- Indica se a coluna aceita nulos ('Y' ou 'N')  
   DATA\_DEFAULT              -- Valor padrão ou função associada  
FROM  
   ALL\_TAB\_COLUMNS  
WHERE  
   TABLE\_NAME = '**SIG010**' -- Nome da tabela (em letras maiúsculas)  
   AND COLUMN\_NAME = '**IG\_MSUIDT**'; -- Nome da coluna que você está buscando

Segue um exemplo de como a estrutura deve ser criada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34305772961943)

A função **SYS\_GUID()** é responsável por criar o conteúdo ID no campo **IG\_MSUIDT** para **banco Oracle**

**Possível problema:** Caso a estrutura do tamanho do campo esteja diferente de 32 de tamanho, o sistema não irá conseguir encontrar o registro gerando uma busca indevida conforme um exemplo abaixo, fazendo o registro não conciliar.

IG\_MSUIDT  = HEXTORAW('BB0FCC9C7D4341F098680050562C9A52    ')  <--- modo inválido caso o campo COLUMN\_ID esteja mais que o tamanho de 32 de caractere

IG\_MSUIDT  = HEXTORAW('BB0FCC9C7D4341F098680050562C9A52') <---- modo correto quando o campo COLUMN\_ID  possui o tamanho de 32 de caractere

Os campos das tabelas foram criadas com problemas de estrutura, possivelmente devido a falhas no processo de migração ou troca de modelo de banco de dados (por exemplo, de SQL Server para Oracle), sem que os procedimentos corretos tenham sido seguidos.

**4 Ponto de análise para banco SQL SERVER:**

Na query abaixo, podemos alterar a consulta das **tabelas** a serem verificadas através da coluna **TABLE\_NAME** alterando para **SIG, FK5 e SE5**

E podemos alterar a consulta dos **campos** a serem verificadas através da coluna **COLUMN\_NAME** alterando para **IG\_MSUIDT, FK5\_MSUIDT, E5\_MSUIDT**

**No exemplo abaixo** vamos executar a query no banco **SQL SERVER** para a tabela SIG, para verificar a estrutura do campo **IG\_MSUIDT**

SELECT  
   COLUMN\_NAME,             -- Nome da coluna  
   DATA\_TYPE,               -- Tipo de dado  
   CHARACTER\_MAXIMUM\_LENGTH AS DATA\_LENGTH,  -- Tamanho máximo do campo (para tipos de dados de caracteres)  
   ORDINAL\_POSITION AS COLUMN\_ID, -- Posição da coluna na tabela  
   IS\_NULLABLE,             -- Indica se a coluna aceita nulos ('YES' ou 'NO')  
   COLUMN\_DEFAULT          -- Valor padrão ou função associada à coluna  
FROM  
   INFORMATION\_SCHEMA.COLUMNS  
WHERE  
   TABLE\_NAME = '**SIG010**'   -- Nome da tabela  
   AND COLUMN\_NAME = '**IG\_MSUIDT**';  -- Nome da coluna

Segue um exemplo de como a estrutura deve ser criada

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34305772964631)

A função **(newid())** é responsável por criar o conteúdo ID no campo **IG\_MSUIDT** para **SQL Server**

**Observações**: Sempre permita que o sistema Protheus crie automaticamente todas as estruturas e campos necessários. O ideal é evitar a inclusão ou alteração de informações diretamente no banco de dados, ou por meio do APSDU, para garantir a integridade e o funcionamento correto do sistema.

**Saiba mais**

[Suporte Financeiro- CTBA940 Conciliador Financeiro](https://tdn.totvs.com/display/public/PROT/Suporte+Financeiro-+CTBA940+Conciliador+Financeiro)
