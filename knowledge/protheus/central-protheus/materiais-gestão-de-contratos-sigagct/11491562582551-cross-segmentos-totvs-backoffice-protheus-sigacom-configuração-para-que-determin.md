---
article_id: 11491562582551
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 4eb5f54a07f2b684f7779906d4ad5448329c2ec3d741d3c3d9f711498aba83e3
fetched_at: '2026-06-28T22:37:20.241135+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Configuração para que
  determinados usuários possam visualizar ou não um campo.
type: support-article
updated_at: '2023-01-06T19:56:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11491562582551-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Configura%C3%A7%C3%A3o-para-que-determinados-usu%C3%A1rios-possam-visualizar-ou-n%C3%A3o-um-campo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:06:00 min** **Dúvida**Configuração para que determinados usuários possam visualizar ou não um campo.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões  
  
**Solução**

Os níveis de usuário servem para você controlar a visualização de campos que os usuários podem ter. Os níveis vão de 1 a 9. Por exemplo, se um usuário tem Nível 5, no módulo SIGACOM, ele poderá visualizar campos que tenham nível 5 ou menos. Caso um campo tenha nível 6 ou mais, esse campo não aparecerá para o usuário.

**IMPORTANTE: isso não vale para campos obrigatórios. Campos obrigatórios irão sempre aparecer.**

Para configurar os níveis de usuário e dos campos, siga o procedimento abaixo.

**Atenção**:No exemplo, iremos configurar determinado campo para que ele não apareça na rotina para este usuário, pois o campo terá um nível maior do que o nível que está configurado para o usuário.

**Para alterar o Nível do Usuário/Grupo**  
- Acesse Configurador >**Usuário**>**Senhas**>**Usuários**ou**Configurador**>**Usuário**>**Senhas**>**Grupos**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931065340951)  
  
- Selecione o usuário/grupo e clique em**Alterar**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483386279831)

- Acesse a aba **Restrições de Acesso > Ambientes,**selecione no Módulo e na coluna **Nível** clique duas vezes no campo para alterar o Nível do usuário (Ex: Nível = 5).

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483449431447)

- Após alteração clique em **Confirmar.**

**Para alterar o Nível do Campo**  
- Acesse**Configurador**>**Base de Dados**>**Dicionário**>**Bases de Dados**

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9931187285015)  
  
- Clique em**Dicionário de Dados**, e selecione a tabela que contém os campos que deseja configurar (EX: SC1).

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483519613079)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483548716183)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483567570711)

- Clique sobre a tabela e clique em**Editar.  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483608424983)**

-Clique em +Solicitação de Compras e clique em Campos.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484125649559)

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11490557566231)

- Na **aba Validações**, altere o nível do campo para um número superior ao nível do usuário (Ex.: Nível=6)

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11490570952599)

Clique em **Salvar**, depois em **Confirmar.**  
- Para que, esta alteração no campo tenha efeito, é necessário atualizar a base de dados. Em **modo exclusivo**(nenhum usuário pode estar acessando as tabelas envolvidas na alteração), clique no ícone**Atualizar Base de Dados.**

**![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484407894167)**

- Clique em **Avançar** até **Finalizar,** confirmando a atualização dos campos alterados.  
  
- Conforme exemplo acima, o usuário/grupo em questão não irá visualizar o campo **Centro de Custo** na rotina MATA110, ao Incluir ou Alterar cadastro de Solicitação de Compras.

Usuário Comprador 1 que alterei nível do campo para 6, não está visualizando o campo.

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11491409831703)

Usuário Adminstrador tem o Campo.

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11491483692951)

**Observações**

- Essa regra é valida apenas para campos que não sejam campos que não sejam de cabeçalho(váriaveis) e obrigatórios, e ou seja, campos obrigatórios não respeitam os níveis de acesso, serão sempre exibidos.

***Saiba Mais :***

* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
