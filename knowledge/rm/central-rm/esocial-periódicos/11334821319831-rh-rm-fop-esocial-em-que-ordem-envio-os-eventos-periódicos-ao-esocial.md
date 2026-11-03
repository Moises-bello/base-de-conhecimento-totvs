---
article_id: 11334821319831
category: esocial - Periódicos
content_hash: db4ed953942139c1c1037c0c63401b6aa7556d78afc907ec8f3d3a3c2f9051d8
fetched_at: '2026-06-28T22:47:09.248627+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Em que ordem envio os eventos periódicos ao eSocial '
type: support-article
updated_at: '2024-06-10T19:04:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11334821319831-RH-RM-FOP-eSocial-Em-que-ordem-envio-os-eventos-peri%C3%B3dicos-ao-eSocial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Em que ordem envio os eventos periódicos ao eSocial ?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**Abaixo indicação de onde o sistema busca os eventos periódicos (3ª fase):

**• S-1200**- Remuneração de trabalhador vinculado ao Regime Geral de Previdência SocialApresenta todos os eventos de envelope de pagamento, incluindo INSS (tabela PFFINANC). Caso utilize tomadores de serviço, o valor levado para o XML será o presente em **Encargos | SEFIP | Editar distribuição Sefip**.

• **S-1210**- Pagamentos de Rendimentos do TrabalhoApresenta o desconto do IRRF e pensão, indicação do valor liquido recebido pelo funcionário, eventos referente a PLR (tabela **PFFINANC**).

**• S-1280**- Informações Complementares aos Eventos PeriódicosInformações referente a empresas optantes pelo simples ou com tributação previdenciária substituída e não substituída. Para correta geração desse evento, em **eSocial | Informações do Empregador**, o campo **Classificação Tributária** deve ser preenchido com **03**. As informações da substituição patronal deve ser preenchida em **eSocial | Período de Apuração**.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360028872832/mceclip11.png)

**• S-1298**- Reabertura dos Eventos PeriódicosEste evento é utilizado para reabrir movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos.  
  
**• S-1299**- Fechamento dos Eventos PeriódicosDestina-se a informar ao ambiente do eSocial o encerramento da transmissão dos eventos periódicos, no período de apuração. Neste momento são consolidadas todas as informações prestadas nos eventos S-1200 a S-1210.

**Saiba mais**Para mais informações, acesse:  
      •[Geração dos eventos periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711)  
      •[Eventos Periódicos](http://tdn.totvs.com/pages/releaseview.action?pageId=351376216)
