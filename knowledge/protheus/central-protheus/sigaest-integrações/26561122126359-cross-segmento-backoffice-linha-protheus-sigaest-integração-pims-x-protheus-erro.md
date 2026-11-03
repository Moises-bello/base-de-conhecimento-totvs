---
article_id: 26561122126359
category: SIGAEST - INTEGRAÇÕES
content_hash: 4c1326a1d8947ba0a644cbeddb804b33631462a410b6aa7add8b01cfc479b436
fetched_at: '2026-06-28T22:38:46.217430+00:00'
product: protheus
section_id: 21226442947351
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Integração PIMS x
  Protheus erro "array out of bounds [3] of [0] on PSWCHAVE(SIGAPSW.PRG)"
type: support-article
updated_at: '2024-09-23T16:49:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26561122126359-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Integra%C3%A7%C3%A3o-PIMS-x-Protheus-erro-array-out-of-bounds-3-of-0-on-PSWCHAVE-SIGAPSW-PRG
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26561122113431) Tempo aproximado para leitura: **00:02:21min****Dúvida**Ao realizar a integração do sistema PIMS para o Protheus ocorre mensagem de erro :

INTEGDEF RETURN ERROR --> [array out of bounds [3] of [0] ]   
|array out of bounds [3] of [0] on PSWCHAVE(SIGAPSW.PRG) 13/08/2024 15:56:59 line : 1700  
|Called from USRRETNAME(MATXALC.PRX) 13/06/2024 17:21:57 line : 495  
|Called from MATI105(MATI105.PRX) 11/05/2022 16:42:23 line : 358

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**Normalmente esse erro está relacionado com o Cadastro de Usuário que está gerando a movimentação, geralmente em caso de acionamento do fonte MATI105 que gera a solicitação ao armazém.  
  
**Solução**

Ao coletar a ultima chamada do fonte MATI105 linha 358 |Called from MATI105(MATI105.PRX) 11/05/2022 16:42:23 line : 358 . Verificamos que é realizada uma validação relacionada ao usuário:

![](https://totvssuporte.zendesk.com/attachments/token/5r7Y8TNYJG2GOJScftaa5h8Q6/?name=image.png)  
   
Essa função UsrRetName retorna o usuário do sistema para maiores detalhes [clique aqui.](https://tdn.totvs.com/x/jfxn)  
 

Após essa chamada é realizada uma validação no fonte MATXALC linha 495 |Called from USRRETNAME(MATXALC.PRX) 13/06/2024 17:21:57 line : 495 .Verificamos que nessa validação continua sendo validado questões de usuário:

   
![](https://totvssuporte.zendesk.com/attachments/token/OtIpbFqwbhhtd2LLWAK1NqEzA/?name=image.png)  
   
Essa condição que verifica se um usuário específico existe em um banco de dados de usuários, e caso ele exista, atribui uma chave de acesso, para maiores detalhes sobre a função PsqSeek [clique aqui](https://tdn.totvs.com/x/h-xn)  
 

E por fim o erro estoura na função PSWCHAVE : array out of bounds [3] of [0] on PSWCHAVE(SIGAPSW.PRG) 13/08/2024 15:56:59 line : 1700

Porém essa validação não temos acesso por ser um fonte de LIB, mas pesquisando sobre SIGAPSW verificamos que tem relação com os arquivos de senhas sigapss.spf   
   
Sabendo dessas validações acima, entendemos que o problema está relacionado a usuário no momento de realizar a movimentação da integração, sendo necessário entender se está implantando o sistema e é necessário algum cadastro especifico na parte do PIMS, ou se foi realizada alguma mudança relacionada ao usuário.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Integrações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/21226442947351-SIGAEST-INTEGRA%C3%87%C3%95ES)*
