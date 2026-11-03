---
article_id: 360012166552
category: PCMSO / Exames
content_hash: 03d6c85d7a0db60451bfc2485449fe1aca0346ae238b9f6592bfde862861741b
fetched_at: '2026-06-28T22:47:42.190336+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT - Situações em que é gerado o exame pendente do tipo Mudança
  de Riscos Ocupacionais
type: support-article
updated_at: '2026-05-29T20:06:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012166552-RH-RM-SMT-Situa%C3%A7%C3%B5es-em-que-%C3%A9-gerado-o-exame-pendente-do-tipo-Mudan%C3%A7a-de-Riscos-Ocupacionais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16036348091543) Tempo aproximado para leitura: **00:01:30 min**

**Dúvida**  
Em quais situações é gerado o exame pendente do tipo mudança de função?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Segurança e Saúde Ocupacional - Todas as versões  
  
**Solução**  
O **Segurança e Saúde Ocupacional**  segue a normativa NR-7 conforme paragrafo a seguir:

*" 7.4.3.4.1. Para fins desta NR, entende-se por mudança de função toda e qualquer alteração de atividade, posto de trabalho ou de setor que implique a **exposição do trabalhador à risco diferente daquele a que estava exposto antes da mudança**."*  
  
Seguindo esta normativa todas as vezes que o funcionário for relacionado a um novo perfil de exames, ou for associado um novo exame ao seu perfil de exame, definido com o tipo mudança de função, o produto compreende que ele estará exposto ao novo risco e será gerado o exame pendente mudança de função.  
  
Neste cenário se o funcionário tiver um troca de seção/função e esta seção/função estiver relacionado o mesmo perfil de exames, da atual, não ocorrerá a geração do exame mudança de função, visto que a mudança esta relacionada ao novo risco que ele é exposto.  
  
Como este é o comportamento padrão do sistema, para que o exame seja gerado como periódico, deve acessar **Perfil de Exames** | **Bateria de Exames**, edite o exame de Mudança de Risco Ocupacional e preencha o campo **Exigido a partir de** com uma **data posterior a data atual.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26792250181015)

Após preencher o campo, salve o cadastro, acesse o cadastro de funcionário e execute o processo de **Gerar Exames Pendentes**. Após isto, vocês podem **limpar o campo de data Exigido a partir de**, pois a partir deste momento, o exame gerado já será o Períodico.

**Saiba Mais:**

Para maiores informações, acesse:

[- Exames Pendentes](https://tdn.totvs.com/display/LRM/Exames+Pendentes).

[- Geração de exames](http://tdn.totvs.com/pages/releaseview.action?pageId=4812916).
