---
article_id: 8872536849431
category: Configurações
content_hash: bd17db45b83d51c83aa0042618591f898bc714b946187bf02295e40c5a3ef746
fetched_at: '2026-06-28T22:46:49.506405+00:00'
product: rm
section_id: 1500000834621
source: central-rm
title: RH - RM - FOP - RH Máscaras e Quebras
type: support-article
updated_at: '2025-01-16T19:45:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8872536849431-RH-RM-FOP-RH-M%C3%A1scaras-e-Quebras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29265178091799) Tempo aproximado para leitura: **00:01:40 min** **Dúvida**Como parametrizar a Máscaras e Quebras no parametrizador?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - Todas as versões  
  
**Solução**Será definido neste parâmetro , a Máscara que será aplicada ao Código de Seção, o Código de quebra mestre, o Código de quebra para CNPJ ou CEI, a Máscara para CEP, Telefone e Centro de Custo Labore,  que será utilizado na hierarquia do cadastro de seções. 

Acesse: **Configurações | Parametrizador | RH Máscaras e Quebras** e preencha os campos **Máscaras** conforme o print abaixo de acordo com parametrização definida para a empresa.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8872474069783)

**Exemplo de um estrutura com Matriz e Filiais:**0         Matriz - CNPJ DA MATRIZ - Centralizadora da coligada

01        Matriz - CNPJ DA MATRIZ

01.01

01.02

02        Filial 02 - CNPJ DA FILIAL 02

02.01

02.02

...

09        Filial 09 – CNPJ DA FILIAL 09

09.01   
  
**No parametrizador, as Máscaras e Códigos de Quebra do exemplo acima são:****Máscara código de seção:**##.##  
**Código de Quebra Mestre:**?????  
**Código de Quebra para CNPJ:**??  
  
**Saiba mais**

[Seção Centralizadora da Coligada](https://tdn.totvs.com/pages/releaseview.action?pageId=223904906)

[Máscara](https://tdn.totvs.com/pages/viewpage.action?pageId=622217661)
