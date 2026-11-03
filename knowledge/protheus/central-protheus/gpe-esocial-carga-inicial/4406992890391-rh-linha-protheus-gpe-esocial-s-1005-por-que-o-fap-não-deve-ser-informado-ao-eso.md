---
article_id: 4406992890391
category: GPE - eSocial - Carga Inicial
content_hash: 5cee9c24c5ffb10bc08dab9e3c690d915b40b6d2fe7b75eccb3b2d9cc1534c64
fetched_at: '2026-06-28T22:45:03.045189+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1005 - Por que o Fap não deve ser informado
  ao eSocial
type: support-article
updated_at: '2024-08-23T11:43:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4406992890391-RH-Linha-Protheus-GPE-eSocial-S-1005-Por-que-o-Fap-n%C3%A3o-deve-ser-informado-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25842488562839) Tempo aproximado para leitura: 00:01:00 min **Dúvida**Por que o Fap não deve ser informado ao eSocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
Com o objetivo de suprir eventual falha de integração do eSocial com a base do FAP e, neste caso, permitir que o contribuinte possa informar o FAP correto, foi alterada com a simplificação, a regra de validação do campo {fap} no evento S-1005 (Tabela de Estabelecimentos, Obras ou Unidades de Órgãos Públicos).  
O procedimento padrão recepcionado pelo eSocial é sem a informação do **FAP, exceto se houver** **processo que autorize** o uso de coeficiente diferente do publicado.  
O evento **S-1005** está condicionado à **validação do Fator Acidentário de Prevenção na Tabela FAP**, e essa validação ocorre de forma distinta, de acordo com a versão do leiaute do eSocial utilizado na transmissão do evento.  
Ressaltamos que **o FAP só deverá ser informado caso a empresa possua algum processo judicial** que altere o valor padrão, ou quando for retornada a mensagem de erro 1801 pelo fato de não ter sido encontrado na Tabela FAP.  
Os valores de FAP podem ser consultados pelas empresas pelo [FAPWeb](https://fap.dataprev.gov.br/) sendo que para acessar, é necessário cadastro prévio de uma senha na Receita Federal do Brasil.   
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)
