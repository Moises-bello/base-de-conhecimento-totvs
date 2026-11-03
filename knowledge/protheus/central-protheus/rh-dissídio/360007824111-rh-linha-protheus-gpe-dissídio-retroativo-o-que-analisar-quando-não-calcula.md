---
article_id: 360007824111
category: RH - Dissídio
content_hash: 0c4100201f0319bd2c47829eef11ef7d852176c16a99c676856f3489f9a6610c
fetched_at: '2026-06-28T22:43:43.335428+00:00'
product: protheus
section_id: 360003109132
source: central-protheus
title: RH - Linha Protheus - GPE - Dissídio retroativo, o que analisar quando não
  calcula
type: support-article
updated_at: '2025-08-08T14:52:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360007824111-RH-Linha-Protheus-GPE-Diss%C3%ADdio-retroativo-o-que-analisar-quando-n%C3%A3o-calcula
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17493524421655)*Tempo aproximado para leitura: **00:01:30 min****Dúvida**O que verificar quando no dissídio retroativo o sistema não gera cálculo ou calcula apenas a verba de salário base?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
 **Solução**Primeiramente verifique se toda parametrização necessária foi realizada, segue **manual do dissidio retroativo**: <http://tdn.totvs.com/pages/releaseview.action?pageId=220889925>   
A rotina de dissidio passou por uma série de atualizações para corrigir os últimos problemas de conhecimento de Suporte Técnico.   
Por este motivo, **sempre mantenha o ambiente atualizado.**

Verifique também os itens abaixo:

1) Tabela S001 / S002 / S003 / S004 / S037 /S038 devidamente preenchida com os anos de cálculo;  
2)Informar o sindicato correto nos parâmetros (ou deixar em branco);  
3)Cadastro de períodos com inconsistência (roteiro sem data de fechamento, roteiros de FOL e ADI com data de integração, roteiros sem data de integração). Veja Mais no link abaixo:  
[RH - Linha Protheus - GPE - LOG no cálculo de dissídio: Existem roteiros que não foram integrados com a folha](https://centraldeatendimento.totvs.com/hc/pt-br/articles/14044738009367)  
4)Verificar se os IDS: 0988 / 1310 / 1295 / 1445 / 0984 /1294 estão cadastrados (caso não estejam, será necessário realizar os cadastros)  
5)Retirar a opção de demitidos na situação dos parâmetros;  
6)Quando não gerar verba de salario, verificar sequencia da SR3 e SR7;  
7)Verificar sequencia das alterações na tabela SR9;  
Na validação de informações de adicionais , por exemplo percentual de insalubridade ou se a insalubridade é sobre salário mínimo ou percentual de salário , o sistema não valida as informações do cadastro (SRA) e sim o histórico contido na tabela SR9.   
8) Verificar se o campo **RA\_ANTEAUM** no cadastro de Funcionários, está preenchido corretamente. A rotina de dissídio utilizará este campo para validar qual a base para aplicação do percentual. Se o campo estiver em branco , a rotina não atribui valor no cálculo.   
![](https://centraldeatendimento.totvs.com/hc/article_attachments/17493536956183)

**Saiba Mais:**  
[Página Centralizadora do dissídio](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003109132-RH-Diss%C3%ADdio)
