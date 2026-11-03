---
content_hash: 292b32a081cc8fd75c0b57e28f50d3b7f549ea6d1221a1f6c175d7ea43ebb73e
fetched_at: '2026-06-29T00:08:49.478732+00:00'
page_id: '330835395'
product: rm
source: tdn-rm
title: 05- Carol Connect (2C)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=330835395
version: 31
---

Carol Connect: É a ferramenta responsável por obter dados do Banco de dados. Saiba mais em <https://docs.carol.ai/docs/carol-connect-2c>.

O conector que deve ser utilizado na configuração de conexão ao banco de dados do TOTVS Educacional é: totvsrm

Abaixo a lista de tabelas do banco de dados do sistema de gestão TOTVS Educacional utilizadas pela solução:

1. FACORDO  
2. FACORDOREL  
3. FLAN  
4. GCOLIGADA  
5. GFILIAL  
6. GIMAGEM  
7. HATENDIMENTOBASE  
8. PPESSOA  
9. SALUNO  
10. SATENDIMENTO  
11. SBOLSA  
12. SBOLSAALUNO  
13. SCAMPUS  
14. SCONCEITO

15. SCONTRATO  
16. SCURSO  
17. SDISCGRADE  
18. SDISCIPLINA  
19. SETAPAS  
20. SFREQUENCIA  
21. SHABILITACAOALUNO  
22. SHABILITACAOFILIAL  
23. SJUSTIFICATIVAFALTA  
24. SLAN  
25. SLOGPLETIVO  
26. SMATRICPL  
27. SMATRICULA  
28. SNOTAETAPA

29. SNOTAS  
30. SOCORRENCIAALUNO  
31. SOCORRENCIATIPO  
32. SPARCELA  
33. SPESSOA  
34. SPLANOAULA  
35. SPLETIVO  
36. SPROVAS  
37. SSTATUS  
38. STIPOCURSO  
39. STURMADISC  
40. STURNO

```

```

**FAQ - Perguntas frequentes sobre o Carol Conect (2C)**

* O que devo fazer quando não conseguir efetuar login no Carol Conect (2C)?  
    
  1. Certifique-se que a Tenant/Domínio, o usuário e a senha estejam corretos;
  2. Quando a rede utilizar firewall ou proxy, certifique-se de que a URL da Carol (\*.carol.ai) esteja adicionada como exceção**;**
* Existe alguma forma de enviar os dados sem a utilização de triggers?  
    
  Sim. Basta setar o parâmetro **ignoreTriggers** para **true,** no arquivo de configuração **3c-integrations.yaml**, e preencher o campo **Sync using timestamp field** informando quais campos serão utilizados. No caso do RM, deverão ser utilizados os campos **RECCREATEDON** e **RECMODIFIEDON**. É importante observar que os campos utilizados devem ser do tipo **DateTime**.
* Como saber se a carga inicial dos dados já foi finalizada?

Basta verificar, na visão **Database Manager,** a quantidade de registros pendentes. Para atualizar esta tabela, basta clicar no botão **Refresh pending queue**.

* O que posso fazer para otimizar o envio de dados pelo 2C utilizando uma máquina com recursos limitados?

O valor dos parâmetros **syncThreads** (número de threads) e **poolSize** (número de conexões com o banco de dados) podem ser aumentados para otimizar os recursos disponíveis.

Além disso, não se recomenda habilitar todas as tabelas de uma única vez.

* Como melhorar a performance do 2C quando percebo que o envio dos dados está lento?

Uma das formas de melhorar a performance do envio pelo 2C é aumentar o número de threads utilizadas. Isso pode ser feito através do parâmetro **syncThreads**, no arquivo **app.config.yml**. Para bases com um volume grande de alterações diárias recomendamos que o valor deste parâmetro seja igual a 20. Outro recurso que temos é melhorar o servidor onde o 2C está sendo executado, aumentando memória RAM e capacidade de processamento.
