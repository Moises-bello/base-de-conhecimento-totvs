---
article_id: 5527343471127
category: Meu RH - Instalação, configuração, qrcode, permissões e erros
content_hash: 74b04a1a7f4b36c8ee279ad2ba5b1755c62d64ad18554061b7449ab6e86d1b04
fetched_at: '2026-06-28T22:47:29.517149+00:00'
product: rm
section_id: 1500000961062
source: central-rm
title: RH - RM - Meu RH - É possível auditar os acessos realizados e saber quais rotinas
  estão sendo executadas pelos usuários
type: support-article
updated_at: '2026-05-15T15:17:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5527343471127-RH-RM-Meu-RH-%C3%89-poss%C3%ADvel-auditar-os-acessos-realizados-e-saber-quais-rotinas-est%C3%A3o-sendo-executadas-pelos-usu%C3%A1rios
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24076786803607) Tempo aproximado para leitura: **00:02:15 min**  
  
**Dúvida**  
É possível auditar os acessos realizados no Meu RH e saber quais rotinas estão sendo executadas pelos usuários?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Solução**  
Atualmente não existe um processo ou rotina específica do Meu RH que registre os acessos ou as rotinas executadas pelos usuários no Meu RH.  
  
Porém, uma funcionalidade que pode ajudar, é que quando um usuário realiza o Login no Meu RH (app ou web), é gravado na **tabela  GULTIMOCONTEXTOUSUARIO, campo RECMODIFIEDON**, a data e hora do último acesso realizado.  
  
Consulta que poderá ser utilizada: ***SELECT CODUSUARIO, CODSISTEMA, CHAPA, RECMODIFIEDON FROM GULTIMOCONTEXTOUSUARIO WHERE CODUSUARIO = 'Informe o Código do Usuário'***  
  
Print de exemplo:

***![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5527288025111)***  
  
**Importante:**  
Caso entenda ser útil a existência de uma rotina ou processo que armazene dados exclusivos do Meu RH como, quantidade de acessos, quais foram as rotinas executadas pelos usuários no Meu RH, recomendamos que acesse nossa[**Central Colaborativa**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037255934-C%C3%B3digo-de-Conduta-Central-Colaborativa) e realize essa sugestão de melhoria.
