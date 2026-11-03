---
article_id: 360018286672
category: eSocial - Gerar XML/ Integração Evento
content_hash: c37f04a92681dc07bf427efa4a518fd5a7b7daac153f357c0cd6a065166b3ba5
fetched_at: '2026-06-28T22:47:12.969859+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: 'RH - RM - FOP - eSocial - Erro na integração do S-1200: A operação solicitada
  no XML está em desacordo com o cenário do registro na base do TAF'
type: support-article
updated_at: '2024-06-19T14:50:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018286672-RH-RM-FOP-eSocial-Erro-na-integra%C3%A7%C3%A3o-do-S-1200-A-opera%C3%A7%C3%A3o-solicitada-no-XML-est%C3%A1-em-desacordo-com-o-cen%C3%A1rio-do-registro-na-base-do-TAF
---

**Ocorrência**Ao tentar realizar a integração do S-1200 o TAF rejeita com a mensagem **A operação solicitada no XML está em desacordo com o cenário do registro na base do TAF**.**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
TAF - TOTVS Automação Fiscal - A partir da versão 12.1.17  
  
**Solução**Geralmente esta mensagem é apresentada por dois motivos:

**• Registro já existente**Quando já existe no TAF um evento S-1200 para a mesma pessoa (CPF) e mesmo período de apuração do registro que está sendo integrado. A existência deste registro poderá ser validada com as orientações abaixo: 

1. Verifique no XML do RM o período de apuração e o CPF do funcionário cujo S-1200 está sendo rejeitado;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044394714/mceclip0.png)

2. No TAF, acesse **Atualizações | Eventos eSocial | Trabalhador | Cadastro Trabalhador** e identifique o ID deste trabalhador (Dica: Filtrar pelo CPF);

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045683373/mceclip0.png)

3. Ainda no TAF, acesse **Atualizações | Eventos eSocial | Periódicos | Folha de Pagamento** e filtre os registros através do ID do trabalhador coletado na ação anterior. Verifique se será localizado um registro para o ID e Período de Apuração em questão;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360013909291/mceclip2.png)

4. Caso o registro seja localizado, significa que em algum momento o evento foi integrado ou inserido diretamente no TOTVS Automação Fiscal, ocasionando o erro de inconsistência em desacordo com o cenário.

**• Funcionário com múltiplos vínculos e S-1200 de um vínculo já enviado**

Conforme manual do eSocial, para cada trabalhador deve ser enviado um único evento S-1200 no período de apuração (competência), contemplando todas as rubricas a que o trabalhador fizer jus no período, ainda que provenientes de vínculos distintos.

Quando um funcionário possui múltiplos vínculos sendo um deste vínculos um autônomo do Fluxus/Externo, o sistema irá gerar um S-1200 para cada vínculo. Após integração com o TAF, será gerado um novo XML unificando os dados para transmissão ao RET.  
  
Se o usuário gerar o S-1200 de um vínculo, integrar com o TAF e transmitir ao RET, ao tentar integrar o S-1200 do segundo vínculo será exibida a mensagem de cenário em desacordo.  
  
Assim, sempre realize a geração do XML e integração com o TAF dos S-1200 de todos os vínculos da pessoa antes de transmiti-los para o governo.  
  
Para ajuste da situação, deve-se excluir o S-1200 do ambiente do governo (através do S-3000), gerar o XML e integrar todos os S-1200 relacionados ao CPF da pessoa e, posteriormente, transmitir para o RET.
