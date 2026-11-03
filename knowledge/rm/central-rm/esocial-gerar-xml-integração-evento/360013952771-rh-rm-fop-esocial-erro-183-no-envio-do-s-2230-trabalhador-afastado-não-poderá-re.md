---
article_id: 360013952771
category: eSocial - Gerar XML/ Integração Evento
content_hash: 2169d8ebefe7be2642a20b894322908fb533204bd375fc5bcb255fed06dbaa5d
fetched_at: '2026-06-28T22:47:12.099013+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro 183 no envio do S-2230: Trabalhador afastado
  não poderá receber este tipo de evento'
type: support-article
updated_at: '2026-01-26T15:59:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013952771-RH-RM-FOP-eSocial-Erro-183-no-envio-do-S-2230-Trabalhador-afastado-n%C3%A3o-poder%C3%A1-receber-este-tipo-de-evento
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24038131652887) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**  
Ao transmitir o evento S-2230 de início de afastamento, o governo retorna uma mensagem de erro **Código do erro: 183 Descrição: Trabalhador afastado não poderá receber este tipo de evento.**

![erro_183.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360009445972)

**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial  - Todas as versões  
  
**Causa**  
Essa inconsistência ocorre pois o funcionário já consta no ambiente do governo (RET) como afastado em decorrência de outro afastamento.  
  
**Solução**  
Para resolver esta inconsistência, siga os passos abaixo:  
1. Realize a consulta através do eSocial Web e verifique a situação do funcionário para o qual deseja transmitir o evento S-2230;  
2. Caso o funcionário esteja afastado, verifique se existe o registro de início enviado através do ERP para envio do término, ou verifique a necessidade de exclusão deste registro no RET;  
3. Caso o funcionário já esteja ativo, abra uma demanda para o próprio governo avaliar a ocorrência.   
  
**Saiba Mais**  
Para mais informações acesse:

* [S-2230 -  Afastamento temporário](https://tdn.totvs.com/pages/viewpage.action?pageId=364908488)
* [S-2230 - Como retificar um afastamento temporário?](https://tdn.totvs.com/pages/viewpage.action?pageId=403735186)
* [Contato com o Governo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004050432)
