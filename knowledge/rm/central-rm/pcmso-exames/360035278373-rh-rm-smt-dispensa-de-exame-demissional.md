---
article_id: 360035278373
category: PCMSO / Exames
content_hash: 330816d70f372da8fc69b15764bb2c8d90606f721d35c40ad914eb047c05567d
fetched_at: '2026-06-28T22:47:42.164375+00:00'
product: rm
section_id: 1500000861462
source: central-rm
title: RH - RM - SMT -  Dispensa de exame demissional
type: support-article
updated_at: '2025-05-06T21:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035278373-RH-RM-SMT-Dispensa-de-exame-demissional
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16035828833559) Tempo aproximado para leitura: 00:01:30 min  
  
Dúvida**Em quais situações o funcionario não deve realizar o exame demissional?

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Segurança e Saúde Ocupacional - A partir da versão 11.80  
 **Solução**Conforme a NR-7 não é necessário realizar exame demissional, caso o exame mais recente tenha sido realizado há menos de 135 (centro e trinta e cinco) dias, para as organizações graus de risco 1 e 2, e há menos de 90 (noventa) dias, para as organizações graus de risco 3 e 4.  
  
Dessa forma, além do cadastro dos tipos de exames demissionais no perfil de exames, deve-se também se atentar ao código **CNAE** vinculado à seção do funcionário. No código CNAE, há o grau de risco vinculado e este pode variar de 1 a 4, e este grau é determinante para a geração ou não do exame pendente demissional, caso tenha controle dos exames a serem realizados. E também com este cadastro, o referido exame será dispensado sempre que houver sido realizado qualquer outro exame médico obrigatório.   
  
Para realizar a validação do CNAE, siga os passos abaixo:   
  
1 - Acesse no modulo de Segurança e Saúde Ocupacional o menu **PPRA/PGR | Grau de Risco/Atividade** **Econômicas****,** e valide os CNAE's cadastrados:    
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26836776879127)

2 - Acesse o modulo de **Segurança e Saúde Ocupacional** o menu **Cadastros | Seções** e edite a seção no qual o funcionario esta lotado. No cadastro de seção, clique na guia **identificação** e valide o campo CNAE 2.0:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26836760130455)

3 - Acesse o módulo de Folha de Pagamento | menu **Administração de Pessoal | Seções** e edite a seção no qual o funcionario esta lotado. Vá até a guia **RAIS/ CAGED/ eSocial,** e valide o campo CNAE:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26836760131479)

**Saiba Mais**

Para maiores informações, acesse:

- [NR 7 - PROGRAMA DE CONTROLE MÉDICO DE SAÚDE OCUPACIONAL - PCMSO](http://www.guiatrabalhista.com.br/legislacao/nr/nr7.htm)
