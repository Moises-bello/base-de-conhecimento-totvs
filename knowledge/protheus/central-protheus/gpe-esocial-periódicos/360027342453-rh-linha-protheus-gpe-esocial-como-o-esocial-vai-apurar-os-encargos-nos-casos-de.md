---
article_id: 360027342453
category: GPE - eSocial - Periódicos
content_hash: 675e826c30ab51888673f6fb62b4b1f4f68a585b23a1c5f76605bcbec92997d7
fetched_at: '2026-06-28T22:45:07.541363+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como o eSocial vai apurar os encargos
  nos casos de Reajuste/Dissidio Retroativo
type: support-article
updated_at: '2025-07-25T14:35:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342453-RH-Linha-Protheus-GPE-eSocial-Como-o-eSocial-vai-apurar-os-encargos-nos-casos-de-Reajuste-Dissidio-Retroativo
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28160520289687)** Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Como o eSocial vai apurar os encargos nos casos de Reajuste/Dissidio Retroativo?  
Como será apurado encargos dissidio retroativo no esocial?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Os valores apresentados no portal do eSocial são computados de acordo com a incidência das rubricas, mas o cálculo é realizado pelo próprio RET (Governo), ou seja, é uma ferramenta externa ao Protheus, o que podemos fazer é certificar que essas informações estão saindo do Protheus da forma esperada pelo leiaute do eSocial.  
  
A Informação será integrada do GPE com o TAF de acordo com o Parâmetro **MV\_ESOCDIS (**[**BOLETIM TÉCNICO**](http://tdn.totvs.com/x/laWbFg)**)**:  
  
Na situação do **MV\_ESOCDIS**com conteúdo **.T.**:  
  
Conforme descrito no [**BOLETIM TÉCNICO**](http://tdn.totvs.com/x/laWbFg), o seu padrão é **.T.** e **sugerimos que seja mantido dessa forma** para que as informações sejam encaminhadas ao eSocial abaixo da *tag* **<infoPerAnt>** de **Remuneração em Períodos Anteriores**, conforme exigido pelo leiaute vigente do eSocial.  
  
As informações enviadas abaixo da tag **<infoPerAnt>** são as verbas de origem que tem incidência e não as de diferença de dissidio, para saber mais sobre as Verbas/Rubricas acesse : **[MP - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852)**Nessa situação há relatos que o RET (Governo) não recalcula valores, ele simplesmente acata o que você informou no S-1200 abaixo da tag **<infoPerAnt>**, porém isso não fica claro no Totalizador do Portal do eSocial, porém a guia da **DCTFWEB** vem com o valor correto, contudo não há como afirmar devido ao motivo exposto no inicio deste artigo.

Abaixo segue trecho do [Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica) vigente onde informa que quando há informações de períodos anteriores o esocial não efetua o cálculo da contribuição do segurado, o empregador deve calcular o valor de contribuição e informa-lo em rubrica própria com incidência 31 ou 32.  O processo de cálculo do valor segurado já é realizado automaticamente no Protheus através da rotina de dissídio retroativo desde que esteja configurada corretamente conforme Boletim técnico que disponibilizamos no início dessa documentação. Considerando a verba de INSS que será integrada é a verba de origem e que ela se encontra configurada com opção 31 ou 32 no campo contribuição previdenciária na aba esocial do cadastro de verba e também no cadastro de rubrica no governo, O eSocial deverá compor esse valor com a contribuição segurado.  
**[![](https://centraldeatendimento.totvs.com/hc/article_attachments/28160566177559)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852)**  
Na situação do **MV\_ESOCDIS**com conteúdo "**.F.**":  
  
Caso o conteúdo do parâmetro seja alterado para "**.F.**", a informação será encaminha ao eSocial abaixo da tag **<infoPerApur>** de **Remuneração no período de apuração.**As informações enviadas na tag <infoPerApur>, são consideradas no mês atual, essa possibilidade foi criada para quem quer forçar o envio das verbas de dissidio, mas isso é por conta em risco de cada Empresa, os encargos serão apurados no período atual e não no período original da diferença.  A incidência dessas rubricas e apuração dos encargos é de responsabilidade de cada Empresa.

Nessa situação o RET (Governo) vai rejeitar o evento enviado para Trabalhadores Demitidos informando que ele deveria estar ativo nesse período e para o Trabalhadores ativos ele vai considerar as informações de Dissidio/Reajuste no mesmo período da Folha de Pagamento do Mês de envio, assim sendo, ele somará os valores para compor a base de cálculo do INSS de acordo com suas incidências e pode gerar valores divergentes de desconto de INSS do Trabalhador.  
  
**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[MP - GPE - eSocial - S-1200 - Como gerar informações de dissidio e rescisão complementar por dissidio no esocial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013552271)  
[MP - GPE - eSocial - S-1200 - Ao gerar os Eventos Periódicos o sistema apresenta no log a mensagem "Preenchimento incorreto das tabelas S050/S126. As informações de dissídio não foram geradas"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360017971692)  
[MP - GPE - eSocial - S-1200 - Quais verbas serão enviadas para o eSocial nos casos de Dissidio Retroativo?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018355852)  
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[Agenda de Eventos Tira-Dúvidas / Responde [Suporte Padrão]](https://tdn.totvs.com/pages/releaseview.action?pageId=550307175)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
