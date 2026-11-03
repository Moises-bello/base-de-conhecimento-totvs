---
article_id: 360025732794
category: Call Center - Telemarketing
content_hash: 18dd8be4223158daf312e9325f00b56310a70b1ef1f6903da52e59db6668dab0
fetched_at: '2026-06-28T22:41:29.466902+00:00'
product: protheus
section_id: 1500001548162
source: central-protheus
title: 'Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- Help: TMKSEMTEL
  ao tentar finalizar um Telecobrança.'
type: support-article
updated_at: '2022-06-22T18:09:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025732794-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Help-TMKSEMTEL-ao-tentar-finalizar-um-Telecobran%C3%A7a
---

**Ocorrência**  
No módulo **Call Center**, ao tentar**finalizar** um atendimento de **Telecobrança ( TMKA271** ) o sistema apresenta o **Help**:

**Help: TMKSEMTEL**

**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)- SIGATMK- A partir da versão 11.80

**Causa**   
Essa mensagem é apresentada, pois o Help indica a **validação** de **existência** de **telefone válido** para o **contato** na geração de ligação pendente, o sistema verifica os **campos** da **SU5** se não estão **vazios**:  
  
SU5->**U5\_FONE**  
SU5->**U5\_CELULAR**  
SU5->**U5\_FAX**  
SU5->**U5\_FCOM1**  
SU5->**U5\_FCOM2**  
  
Se estiver **Vazios**, o Help é **acionado**, pois precisa ter um contato **válido com telefone** para poder **salvar** o atendimento de **telecobrança** e deixar pendente para retorno.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o cadastro de **Contatos ( TMKA070 )**, selecione o **contato** que precisa ter o **telefone válido** e clique em **alterar**;

2. Ao **entrar** no cadastro do contato em questão, na parte **inferior** da tela, existe a aba **telefone**, clique na aba e vá para **linha**;

3. Na linha da **aba telefone**, existe o campo **Tipo**, nesse campo o usuário irá definir o tipo de **telefone** será cadastrado, o campo **Padrão,**  nesse campo o usuário deverá definir se o **tel**. é **padrão** ou não, ao salvar o **tipo, Padrão e o telefone**, o mesmo irá aparecer automaticamente no **cabeçalho** do cadastro de **contato** no campo **determinado** de acordo com o **tipo**.

4. Após fazer os **procedimentos acima**, vá até a rotina de **Telecobrança** e finalize a **operação**!
