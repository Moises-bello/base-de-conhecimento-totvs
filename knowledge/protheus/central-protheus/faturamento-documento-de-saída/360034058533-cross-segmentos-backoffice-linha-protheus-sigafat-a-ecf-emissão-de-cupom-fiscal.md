---
article_id: 360034058533
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: f6b06c0c94bb0d6d1a070e387021ffa2bb6945bdc1052bf9817be4cf63711bdf
fetched_at: '2026-06-28T22:38:43.979356+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice (Linha Protheus) - SIGAFAT -A ECF (Emissão de
  Cupom Fiscal) está disponível no módulo Faturamento
type: support-article
updated_at: '2023-07-12T21:13:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034058533-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFAT-A-ECF-Emiss%C3%A3o-de-Cupom-Fiscal-est%C3%A1-dispon%C3%ADvel-no-m%C3%B3dulo-Faturamento
---

**Dúvida**

A ECF (Emissão de Cupom Fiscal) está disponível no módulo Faturamento?

**Ambiente**

Cross Segmentos - Backoffice (Linha Protheus) – Faturamento (SIGAFAT) – Todas as versões

**Solução**

Com o objetivo de atender a legislação do Programa Aplicativo Fiscal – Emissor de Cupom Fiscal (PAF – ECF) Ato COTEPE 06/08, desenvolvido pelo CONFAZ – Conselho Nacional de Política Fazendária, informamos que o módulo Front-loja/SigaLoja (rotina Venda Assistida) é a única interface Protheus que permitir a emissão de cupom fiscal.

A partir de 01/01/2013, as rotinas envolvidas com emissão de cupom fiscal, Leitura X e Redução Z, serão retiradas do módulo Faturamento nas versões 10 e 11 (todos os releases), o qual suportará apenas a emissão de notas fiscais.

Esta definição está fundamentada a partir do Ato e Convênios dos links abaixo:

<http://www.fazenda.gov.br/confaz/confaz/atos/atos_cotepe/2008/ac006_08.htm;>   
<http://www.fazenda.gov.br/confaz/confaz/Convenios/ICMS/2008/CV015_08.htm;>   
<http://www.fazenda.gov.br/confaz/confaz/Convenios/ICMS/2009/cv009_09.htm>.

Caso o cliente se enquadre na situação de emissão de cupom fiscal pelo módulo Faturamento atualmente, deve-se avaliar os seguintes cenários:

Caso tenha a obrigatoriedade de uso do ECF (Emissor de Cupom Fiscal), deve adotar o PAF-ECF como solução de interface de venda.

Para obter mais informações sobre o PAF-ECF acessar o TDN (http://tdn.totvs.com) com a palavra-chave “PAF” ou entre em contato com o nosso Help Desk. Para a questão de licenciamento, deve entrar em contato com o seu Executivo de Contas;

Caso o cliente não tenha a obrigatoriedade de uso do ECF, deve adotar a emissão de notas fiscais.  
Para os clientes que utilizam ECF, porem não há obrigatoriedade do PAF-ECF em seu estado, sugerimos a migração para o módulo Front-Loja/SigaLoja, que são aptos a emissão dos cupons de acordo com as Legislações locais.

**OBS: A definição de obrigatoriedade ou não do uso do ECF é uma avaliação do próprio cliente uma vez que depende da sua atividade econômica, faturamento anual, estado de atuação (UF) dentre outras variáveis. A TOTVS não tem nenhuma responsabilidade sobre esta definição.”**

**Saiba Mais: [MP - FAT - Como emitir NFCe para o módulo Faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115011591027-MP-FAT-Como-emitir-NFCe-para-o-m%C3%B3dulo-Faturamento)**
