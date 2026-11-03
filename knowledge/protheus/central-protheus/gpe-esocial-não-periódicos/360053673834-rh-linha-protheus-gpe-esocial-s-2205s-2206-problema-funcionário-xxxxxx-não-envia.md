---
article_id: 360053673834
category: GPE - eSocial - Não Periódicos
content_hash: 506aa4915b2b2eae7eaef3377b523cbeb33620d206adc44962fe14342dfb4f2b
fetched_at: '2026-06-28T22:45:04.665573+00:00'
product: protheus
section_id: 360005445813
source: central-protheus
title: 'RH - Linha Protheus - GPE - eSocial - S-2205/S-2206 - Problema: Funcionário
  XXXXXX não enviado(a) ao TAF. Erro: 000012'
type: support-article
updated_at: '2026-06-16T10:55:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053673834-RH-Linha-Protheus-GPE-eSocial-S-2205-S-2206-Problema-Funcion%C3%A1rio-XXXXXX-n%C3%A3o-enviado-a-ao-TAF-Erro-000012
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41258650711063) Tempo aproximado para leitura:**00:01:00 min**  
  
**Ocorrência**  
No módulo Gestão de Pessoal, ao tentar realizar alteração alteração no cadastral do trabalhador apresenta a inconsistência: **Problema:** Funcionário XXXXXX não enviado(a) ao TAF. Erro: 000012  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – Todas as versões  
  
**Causa**  
Normalmente esse erro ocorre quando esta sendo realizado o envio de um evento de alteração do trabalhador, integrando o evento S-2205 (Alteração de Dados Cadastrais do Trabalhador) ou S-2206 (Alteração de Contrato de Trabalho), porém possui um evento pai S-2200 (Admissão de Trabalhador) com inconsistência ou não validado pelo RET no módulo TAF.  
  
**Solução**  
1. Acessar o módulo TAF pelo menu **->Atualizações ->Eventos Esocial ->Trabalhador ->Cadastro do trabalhador**, localizar o funcionário que apresenta o erro no GPE e verificar se existe numero de recibo do governo no evento S-2200.  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360091959253)  
2. Caso não existe numero de recibo, verificar no site do governo se existe o evento S-2200 para o trabalhador, caso não exista realizar o envio do evento para o eSocial  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:   
[Artigos S-2205](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055236434)  
[Artigos S-2206](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055237854)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)   
[MOS - Manual de Orientação eSocial](https://portal.esocial.gov.br/institucional/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://portal.esocial.gov.br/institucional/ambiente-de-producao-empresas/perguntas-frequentes-producao-empresas)
