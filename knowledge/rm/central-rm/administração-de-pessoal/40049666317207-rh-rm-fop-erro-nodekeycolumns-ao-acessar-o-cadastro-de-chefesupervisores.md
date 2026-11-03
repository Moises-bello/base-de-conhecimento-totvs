---
article_id: 40049666317207
category: Administração de Pessoal
content_hash: 2a315e70dd509aeeff0daefa91cbfab8fec5dc909c5fa152b313a1ba15c9515e
fetched_at: '2026-06-28T22:47:01.065809+00:00'
product: rm
section_id: 1500000861042
source: central-rm
title: RH - RM - FOP - Erro 'NodeKeyColumns' ao acessar o cadastro de Chefe/Supervisores
type: support-article
updated_at: '2026-04-28T13:34:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/40049666317207-RH-RM-FOP-Erro-NodeKeyColumns-ao-acessar-o-cadastro-de-Chefe-Supervisores
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40049643569815) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
Como proceder para corrigir o erro relacionado a **NodeKeyColumns** ao tentar acessar o registro de 'Chefe/ supervisores'?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de pagamento - Todas as versões  
  
**Solução**  
Ao acessar a tela de 'Chefe e Supervisores', o sistema apresenta a seguinte mensagem de erro;

**Ocorreu um erro ao tentar ordenar as  as rows.**

**Provavelmente o NodeKeyColumns está incorreto. Foi passado: "\* CODIGO;CHAPAUNICA;DATAINICIO;CODEQUIPE'.**

**Ao se tentar gerar o sort o resultado foi: 'CODIGO, CHAPAUNICA,DATAINICIO,CODEQUIPE.**

![Captura de tela 2026-04-27 143722.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40049643574039)

Este erro pode ser encontrado pelo usuário caso a parametrização do Código de quebra mestre não estiver de acordo com a Máscara código de seção. Para corrigir a situação, o usuário deve seguir os passos: 

1 -Acessar; **configuração | parametrizador | mascaras e quebras.**

**Verifique se o código de quebra mestre está de acordo com a quebra de seção. Se a quebra estiver em branco ou diferente do que está na quebra de seção, o sistema exibirá o erro conforme descrito anteriormente.**

![Captura de tela 2026-04-27 145056.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40049643577623)

2 - A correção será feita com o preenchimento de interrogações correspondente ao número de caracteres na Máscara código de seção, assim como o exemplo abaixo.

![Captura de tela 2026-04-27 145357.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40049666300439)

**Após a correção do parametrizador, avance o processo e conclua ele, sendo possível acessar normalmente 'Chefe/Supervisores'.**

**Saiba mais**  
[RH - RM - FOP - RH Máscaras e Quebras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/8872536849431-RH-RM-FOP-RH-M%C3%A1scaras-e-Quebras)  
[RH - RM - FOP - Chefes e Supervisores: Cadastro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019444691-RH-RM-FOP-Chefes-e-Supervisores-Cadastro)
