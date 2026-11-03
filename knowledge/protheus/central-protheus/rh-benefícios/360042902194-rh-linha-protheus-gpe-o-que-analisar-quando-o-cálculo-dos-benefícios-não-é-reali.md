---
article_id: 360042902194
category: RH - Benefícios
content_hash: f48e3370c53080aae1de37c1d03078abf0e1084e80af45ba9ef4f96844a7a1fb
fetched_at: '2026-06-28T22:44:04.922144+00:00'
product: protheus
section_id: 360001597251
source: central-protheus
title: RH - Linha Protheus - GPE - O que analisar quando o Cálculo dos Benefícios
  não é realizado
type: support-article
updated_at: '2025-09-12T17:12:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042902194-RH-Linha-Protheus-GPE-O-que-analisar-quando-o-C%C3%A1lculo-dos-Benef%C3%ADcios-n%C3%A3o-%C3%A9-realizado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24594146204439) Tempo aproximado para leitura: 00:02:00 min  
  
Dúvida**O que analisar quando o Cálculo dos Benefícios não é realizado?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Solução**Para solucionar esse incidente, realize os seguintes passos:   
 **1.** Acesse o Configurador > **Ambiente > Cadastros > Parâmetros** e localize o parâmetro **MV\_CALCBEN**. Verifique se o conteúdo do parâmetro está preenchido com **.T.** , caso não esteja, será necessário realizar a alteração;  
  
**2.** Acesse o Configurador > **Base de Dados > Dicionário > Base de Dados** e verifique o compartilhamento das Tabelas SR0, SM7, RG2 e SRA. Nenhuma destas tabelas pode estar Compartilhada, todas devem estar Exclusivas, conforme o exemplo abaixo:   
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360057793774)

Caso esteja diferente, realize a alteração do Compartilhamento das Tabelas pelo Configurador.

**3.** Na rotina de cálculo, a pergunta 'Complemento por HE?' deve ser preenchida como **NÃO** para o cálculo mensal dos benefícios, e deve ser utilizada de forma diferente somente quando necessário, conforme [esta documentação.](https://tdn.totvs.com/pages/viewpage.action?pageId=776129138)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/24593569879447)

**Saiba Mais**  
[Documento Técnico - Cálculo de Benefícios](https://tdn.totvs.com/pages/releaseview.action?pageId=244927626)   
[Artigos sobre Cálculo de Benefícios](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597251-RH-Benef%C3%ADcios)  
[Pacote de Expedição Contínua - Acumulado de RH](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO)
