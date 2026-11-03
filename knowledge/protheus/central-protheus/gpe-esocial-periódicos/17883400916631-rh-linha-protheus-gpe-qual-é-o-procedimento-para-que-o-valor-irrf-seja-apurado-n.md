---
article_id: 17883400916631
category: GPE - eSocial - Periódicos
content_hash: 680a09f1a1f0f9faba0aa923d59d3ee3629ce177ed84efb58c4e7944fab3dd94
fetched_at: '2026-06-28T22:45:09.945779+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - Qual é o procedimento para que o valor IRRF seja
  apurado na DCTFWeb
type: support-article
updated_at: '2023-09-28T20:01:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17883400916631-RH-Linha-Protheus-GPE-Qual-%C3%A9-o-procedimento-para-que-o-valor-IRRF-seja-apurado-na-DCTFWeb
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17883430436887)** Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Qual é o procedimento para que o valor de**IRRF - Imposto de Renda Retido na Fonte** seja apurado na **DCTFWeb**?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**  
Para que o**IRRF** seja considerado na **DCTFWeb**, deverá validar as seguintes informações:  
  
- A rubrica de Desconto do IRRF deve estar com um dos códigos da [Tabela 21](https://www.gov.br/esocial/pt-br/documentacao-tecnica/leiautes-esocial-v-s1-1-nt-02-2023/index.html/tabelas.html#21): **31, 32, 33 ou 34**;  
- O demonstrativo que está no**S-1200/S-2299** deve ter a rubrica de Desconto IR;  
- O evento **S-1210** deve referenciar o demonstrativo que tem a Desconto do IR;  
- O evento **S-5002 - Imposto de Renda Retido na Fonte por Trabalhador** deve totalizar o IRRF conforme Período de Apuração da data de pagamento informado no S-1210;  
- O evento **S-5012 - Imposto de Renda Retido na Fonte Consolidado por Contribuinte** deve totalizar todos os **S-5002** e enviar para **DCTFWeb**.  
  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[Automação Fiscal - Relatório - Acessando o Relatório de Conferência de IRRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/17503337989271-Automa%C3%A7%C3%A3o-Fiscal-Relat%C3%B3rio-Acessando-o-Relat%C3%B3rio-de-Confer%C3%AAncia-de-IRRF)  
[RH - Linha Protheus - GPE - eSocial - S-5002 - Como consultar no site do eSocial dados do evento de IRRF S-5002 (Imposto de Renda Retido na Fonte)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042806434?source=search)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
