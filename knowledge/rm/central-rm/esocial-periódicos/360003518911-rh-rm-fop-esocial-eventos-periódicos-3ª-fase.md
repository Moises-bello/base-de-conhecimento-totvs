---
article_id: 360003518911
category: esocial - Periódicos
content_hash: 09a2eed609049c6d547d38e378f5e39771f99099a3e3730fe71c383a81f8602d
fetched_at: '2026-06-28T22:47:09.371928+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: 'RH - RM - FOP - eSocial - Eventos Periódicos: 3ª Fase'
type: support-article
updated_at: '2024-06-27T19:37:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003518911-RH-RM-FOP-eSocial-Eventos-Peri%C3%B3dicos-3%C2%AA-Fase
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484912237207) Tempo aproximado para leitura: 00:02:00 min**

**Dúvida**Como devo parametrizar o sistema para que sejam gerados corretamente os evento periódicos (3ª fase)?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as Versões  
  
**Solução**  
Abaixo indicação de onde o sistema busca os eventos periódicos (3ª fase).

**• S-1200** - Remuneração de trabalhador vinculado ao Regime Geral de Previdência SocialApresenta todos os eventos de envelope de pagamento, incluindo INSS (tabela PFFINANC). Caso utilize tomadores de serviço, o valor levado para o XML será o presente em **Encargos | SEFIP | Editar distribuição Sefip**.

• **S-1210** - Pagamentos de Rendimentos do TrabalhoApresenta o desconto do IRRF e pensão, indicação do valor liquido recebido pelo funcionário, eventos referente a PLR (tabela **PFFINANC**).

**• S-1280** - Informações Complementares aos Eventos PeriódicosInformações referente a empresas optantes pelo simples ou com tributação previdenciária substituída e não substituída. Para correta geração desse evento, em **eSocial | Informações do Empregador**, o campo **Classificação Tributária** deve ser preenchido com **03**. As informações da substituição patronal deve ser preenchida em **eSocial | Período de Apuração**.

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24484756106519)

**• S-1298** - Reabertura dos Eventos PeriódicosEste evento é utilizado para reabrir movimento de um período já encerrado, possibilitando o envio de retificações ou novos eventos periódicos.  
  
**• S-1299** - Fechamento dos Eventos PeriódicosDestina-se a informar ao ambiente do eSocial o encerramento da transmissão dos eventos periódicos, no período de apuração. Neste momento são consolidadas todas as informações prestadas nos eventos S-1200 a S-1210.

**Saiba mais**Para mais informações, acesse:  
      • [Geração dos eventos periódicos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360003044711)   
      • [Eventos Periódicos](http://tdn.totvs.com/pages/releaseview.action?pageId=351376216)
