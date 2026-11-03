---
article_id: 28213353601559
category: Meu RH - Férias
content_hash: de5ca6053b791a8e7110df72b52282c0386045beabbf23135fc05fc5cdcabea2
fetched_at: '2026-06-28T22:47:31.639360+00:00'
product: rm
section_id: 1500000835241
source: central-rm
title: RH - RM - Meu RH - Como identificar se tem algum Chefe, Supervisor ou Externo
  sem e-mail preenchido
type: support-article
updated_at: '2025-06-16T12:01:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28213353601559-RH-RM-Meu-RH-Como-identificar-se-tem-algum-Chefe-Supervisor-ou-Externo-sem-e-mail-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28213353579927) Tempo aproximado para leitura: **00:05:00min** **Dúvida**Como verificar qual chefe, supervisor ou externo está sem e-mail preenchido via Consulta SQL  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**Para poder identificar qual chefe, supervisor ou externo que está sem o e-mail cadastrado gerando o erro **"Não é possível enviar um e-mail sem que o endereço seja informado"**, pode-se realizar a consulta SQL abaixo e obter o retorno de todos os cadastros do ambiente conforme o exemplo abaixo.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/28213353584279)

Veja a consulta SQL completa:

```
--Validação para chefe --  
SELECT DISTINCT PFUNC.CHAPA, PFUNC.NOME, PPESSOA.EMAIL, PSUBSTCHEFE.CODSECAO, PSUBSTCHEFE.CODCOLIGADA  
FROM PSUBSTCHEFE (NOLOCK)  
JOIN PFUNC (NOLOCK) ON PSUBSTCHEFE.CODCOLSUBST = PFUNC.CODCOLIGADA AND PSUBSTCHEFE.CHAPASUBST = PFUNC.CHAPA  
JOIN PPESSOA (NOLOCK) ON PPESSOA.CODIGO = PFUNC.CODPESSOA  
  
--Validação para supervisor--  
SELECT DISTINCT PFUNC.CHAPA, PFUNC.NOME, PPESSOA.EMAIL, PSUBSTSUP.CODSECAO, PSUBSTSUP.CODCOLIGADA  
FROM PSUBSTSUP (NOLOCK)  
JOIN PFUNC (NOLOCK) ON PSUBSTSUP.CODCOLIGADA = PFUNC.CODCOLIGADA AND PSUBSTSUP.CHAPASUBST = PFUNC.CHAPA  
JOIN PPESSOA (NOLOCK) ON PPESSOA.CODIGO = PFUNC.CODPESSOA  
  
--Validação para chefe externo--  
SELECT   
PE.CODEXTERNO,        -- Código do externo da tabela PEXTERNO  
PC.CODSECAO,          -- Código da seção da tabela PCHEFEEXTERNO  
PC.CODCOLIGADA,          -- Código da seção da tabela PCHEFEEXTERNO  
PP.NOME,              -- Nome da pessoa da tabela PPESSOA  
PP.EMAIL,             -- E-mail da pessoa da tabela PPESSOA  
PP.CODIGO             -- Código da pessoa da tabela PPESSOA  
FROM   
PEXTERNO PE (NOLOCK)   
JOIN   
PCHEFEEXTERNO PC (NOLOCK) ON PE.CODEXTERNO = PC.CODEXTERNO  -- Relaciona os externos com suas seções  
JOIN   
PPESSOA PP (NOLOCK) ON PP.CODIGO = PE.CODPESSOA  -- Relaciona as informações pessoais dos externos  
  
--Validação para supervisor externo--  
SELECT   
PE.CODEXTERNO,        -- Código do externo da tabela PEXTERNO  
PC.CODSECAO,          -- Código da seção da tabela PSUPERVEXTERNO  
PC.CODEQUIPE,          -- Código da equipe da tabela PSUPERVEXTERNO  
PC.CODCOLIGADA,          -- Código da coligada do tabela supervisor externo  
PP.NOME,              -- Nome da pessoa da tabela PPESSOA  
PP.EMAIL,             -- E-mail da pessoa da tabela PPESSOA  
PP.CODIGO             -- Código da pessoa da tabela PPESSOA  
FROM   
PEXTERNO PE (NOLOCK)   
JOIN   
PSUPERVEXTERNO PC (NOLOCK) ON PE.CODEXTERNO = PC.CODEXTERNO  -- Relaciona os externos com suas seções  
JOIN   
PPESSOA PP (NOLOCK) ON PP.CODIGO = PE.CODPESSOA  -- Relaciona as informações pessoais dos externos
```

Após identificar os cadastros sem e-mail, faça o preenchimento do campo através do cadastro do funcionário, e tente solicitar as férias novamente para o e-mail ser enviado com sucesso.

**Importante**

Caso existam chefes ou supervisores com a validade expirada no cadastro, eles deverão ser removidos da estrutura. Isso porque, durante a validação, será gerado o mesmo erro indicando que o destinatário não pôde ser localizado devido à ausência de validade ativa no cadastro.
