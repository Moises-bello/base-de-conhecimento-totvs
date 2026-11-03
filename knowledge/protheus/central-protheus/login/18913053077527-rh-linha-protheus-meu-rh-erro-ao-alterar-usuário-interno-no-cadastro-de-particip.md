---
article_id: 18913053077527
category: LOGIN
content_hash: 5fc4984f412869ab5f532fe88a65d32db0e2f4281c493e9fe1722f958236d6ab
fetched_at: '2026-06-28T22:44:40.465827+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: 'RH - Linha Protheus - MEU RH - Erro ao alterar usuário Interno no Cadastro
  de Participante: Não existe registro relacionado a chave informada no alias AI3,
  ordenação 1'
type: support-article
updated_at: '2025-07-18T13:22:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18913053077527-RH-Linha-Protheus-MEU-RH-Erro-ao-alterar-usu%C3%A1rio-Interno-no-Cadastro-de-Participante-N%C3%A3o-existe-registro-relacionado-a-chave-informada-no-alias-AI3-ordena%C3%A7%C3%A3o-1
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18913069486615) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Ao tentar alterar o usuário interno dentro do **Cadastro de Participante** é apresentada a mensagem "**Problema**: Não existe registro relacionado a chave informada no alias AI3, ordenação 1"  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22235259482903)  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**Este ***HELP*** geralmente aparece por não existir o cadastro do usuário interno na filial em que está *logado* ao realizar a alteração.   
  
Deste modo é preciso entrar no sistema *logado* na filial qual é pertencente ao colaborador e que **exista um usuário Genérico do Portal**.  
  
Este *log*, tem relação também com o compartilhamento das tabelas AI3, AI4, AI5 e RJD, todas precisarão ter o mesmo cenário, ou totalmente exclusiva ou totalmente compartilhada.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22234707383831)  
  
Para ajustar ou manter todas as tabelas mencionadas, devidamente com o mesmo compartilhamento, acesse as seguintes rotinas para recriar os registros padrões:  
  
- AI3, AI4 e AI5 - Usuário Genérico, Fornecedores e Direitos: Acessar o **Módulo 18, rotina presente em Atualizações > Configurações > Usuários > Genérico;**  
- RJD - Permissões Meu RH: Acessar o **Módulo 18, rotina presente em Atualizações > Configurações > Usuários > Permissões Meu RH.**O compartilhamento das tabelas mencionadas, possuem uma relação bastante importante entre si, sendo que, alguns campos da **tabela RD0 (cadastro de Participante/Pessoa)** possuem **alguns gatilhos ("*Valids*"),** que acabam, por vezes, esbarrando em alguma regra que não está sendo atendida quanto a estes compartilhamentos.   
  
Existe inclusive, validações pós gravação, **quando uma execução à essa validação é apresentada**, mas na outra, devido ao campo não ter sido alterado ou carregado, **a execução não bate na regra e apresenta essa mensagem.**  
  
**Saiba Mais:  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referência do MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
