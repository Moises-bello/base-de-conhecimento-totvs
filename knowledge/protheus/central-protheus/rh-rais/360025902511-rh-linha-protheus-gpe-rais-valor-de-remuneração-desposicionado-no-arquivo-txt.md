---
article_id: 360025902511
category: RH - RAIS
content_hash: acb55d95657226af50cee84955e7968d5387d6b7455eea46f2c8c80600f694e7
fetched_at: '2026-06-28T22:44:05.789873+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - RAIS - Valor de remuneração desposicionado no arquivo
  TXT
type: support-article
updated_at: '2025-08-06T14:57:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025902511-RH-Linha-Protheus-GPE-RAIS-Valor-de-remunera%C3%A7%C3%A3o-desposicionado-no-arquivo-TXT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33987582776471) Tempo aproximado para leitura:**00:01:00 min**

**Ocorrência**Valor de remuneração (Posição 163 até 270) desposicionado no arquivo TXT , fazendo com que um salário de 5 mil seja demonstrado como 50 mil no programa GDRAIS  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –  Todas as versões  
  
**Causa**O erro ocorre quando o tamanho do campo R2\_CBO está diferente de 6.  
  
**Solução**Para realizar a correção deste erro, é necessário a correção do tamanho deste campo e para isso, realize o seguinte procedimento:  
  
1. Acesse o sistema via SIGACFG;  
2. Acesse o caminho Base de Dados/Dicionário/Base de Dados;  
3. Ache a tabela SR2 e o campo R2\_CBO e altere o tamanho do campo para 6;  
4. Salve a alteração;  
5. Realize novamente a geração do arquivo .txt e verifique se o erro ainda é apresentado.  
  
**Saiba mais**  
Para verificar as dúvidas mais frequentes sobre a RAIS 2019, acesse o *link*abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS>
