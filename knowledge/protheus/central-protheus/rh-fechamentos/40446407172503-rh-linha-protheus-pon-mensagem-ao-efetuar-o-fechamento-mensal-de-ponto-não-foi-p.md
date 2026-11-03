---
article_id: 40446407172503
category: RH - Fechamentos
content_hash: 7ab58e338acf7560572551d88f6538eb6ae5741b60e11dc9791495a1d577ab81
fetched_at: '2026-06-28T22:44:48.907798+00:00'
product: protheus
section_id: 32419231682455
source: central-protheus
title: 'RH - Linha Protheus - PON - Mensagem ao efetuar o fechamento mensal de Ponto:
  não foi possível concluir o processo, outro processo está utilizando a seguinte
  tabela: SP8, SPB, SPC ou SP'
type: support-article
updated_at: '2026-05-15T17:36:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40446407172503-RH-Linha-Protheus-PON-Mensagem-ao-efetuar-o-fechamento-mensal-de-Ponto-n%C3%A3o-foi-poss%C3%ADvel-concluir-o-processo-outro-processo-est%C3%A1-utilizando-a-seguinte-tabela-SP8-SPB-SPC-ou-SP
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40446407139095) Tempo aproximado para leitura: **01:00:00 min**  
  
**Dúvida**  
Mensagem ao efetuar o **fechamento mensal** de Ponto: **Não foi possível concluir o processo, outro processo está utilizando a seguinte tabela: SP8, SPB, SPC ou SP5**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/40446968857239)  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Ponto Eletrônico - Todas as versões  
  
**Solução**  
Para o [**Fechamento do Período de Ponto**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004103232-RH-Linha-Protheus-PON-Como-efetuar-o-Fechamento-Mensal-do-Ponto), é necessário que o usuário possua acesso restrito no ambiente, pois o sistema efetua alteração de [tabelas efetuando DE X PARA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013084192-RH-Linha-Protheus-PON-Migra%C3%A7%C3%A3o-de-dados-no-Fechamento-Mensal-do-Ponto) de informações na base de dados.

Para solução do problema, verifique:  
**1.** Verificar se algum usuário não está utilizando algum processo que utiliza alguma tabela informada;  
**2.** Reiniciar os serviços (inclusive DBACCESS para que todas as licenças sejam liberadas);  
  
**Saiba mais:**  
[Pacote de Expedição Contínua - Acumulado de RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854)  
[Manual do Ponto Eletrônico](https://tdn.totvs.com/pages/releaseview.action?pageId=630823373)
