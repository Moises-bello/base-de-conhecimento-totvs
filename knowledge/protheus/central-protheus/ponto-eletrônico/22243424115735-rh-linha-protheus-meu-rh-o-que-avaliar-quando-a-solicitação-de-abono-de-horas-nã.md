---
article_id: 22243424115735
category: PONTO ELETRÔNICO
content_hash: 0e993640f9be26ca674a668c386bf420de3e2dcb1c99f4383d68bb2b5efea2a1
fetched_at: '2026-06-28T22:44:36.509014+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - O que avaliar quando a solicitação de abono
  de horas, não grava ao realizar a inclusão
type: support-article
updated_at: '2026-06-26T20:41:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22243424115735-RH-Linha-Protheus-Meu-RH-O-que-avaliar-quando-a-solicita%C3%A7%C3%A3o-de-abono-de-horas-n%C3%A3o-grava-ao-realizar-a-inclus%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22243409125911) Tempo aproximado para leitura: **00:05:00 min**  
  
**Dúvida**  
O que avaliar quando a solicitação de abono de horas, não grava ao realizar a inclusão  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões  
  
**Solução**  
É necessário inicialmente, verificar se o **período de apontamento está aberto corretamente** no módulo do Ponto Eletrônico. Para isso, acesse o **módulo 16 - SIGAPON, na rotina Atualizações > Cadastro de Ponto > Período de apontamento.**  
  
**Outras Ações > Modificar Período** e verifique qual o período aberto:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22243424083223)  
Se estiver correto, prossiga:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22243409130647)  
  
Necessário também, verificar na rotina Permissões Meu RH, se vinculado ao **usuário genérico do portal,** deste funcionário, **as liberações de abono estão corretamente habilitadas**.  
  
Acesse o módulo **18 - SIGATCF e na rotina Atualizações > Configurações > Usuários > Permissões Meu RH**, selecione o Usuário Genérico correspondente e Alterar:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22243409132951)  
  
As permissões que precisarão ser habilitadas são:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22243424088215)  
  
Se estiverem todas corretamente habilitadas, acesse no próprio módulo **18 - SIGATCF, a rotina Atualizações > Configurações > Usuários > Genéricos**, selecione o Usuário Genérico correspondente e Alterar, verificando se o campo usuário interno está preenchido:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/22243424089239)  
  
Este usuário interno **é de suma importância nas configurações**, pois é um cadastro feito no módulo **SIGACFG - Configurador**, que precisará ser um usuário que não esteja vinculado a **nenhum Grupo de Administrador**, e que tenha **todas as permissões de acesso, rotinas, Empresas e módulo do Protheus**. Para saber mais sobre este usuário interno, [**clique aqui**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729194)**.**  
  
Por fim, verificar se após a inclusão do abono pelo Meu RH, foi **criado um registro de requisição na tabela RH3**, responsável por todas as solicitações oriundas do *App* Meu RH.   
  
No artigo a seguir, segue um passo a passo para extração de um **relatório genérico da tabela RH3**, para conferência dessa inclusão:  
[**Como emitir um Relatório para acompanhamento das solicitações feitas no App Meu RH**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19222743777943)

Outro ponto importante é validar se o controle de numeração está correto pois a perda da sequencia de gravação faz o Meu RH não gravar a solicitação para não gerar duplicidade.  
Para correção é necessário acessar o **SIGACFG e entrar no seguinte caminho Ambiente - Cadastro - APCFG110(controle de numeração)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22381133961239)

Após isso você irá procurar por **RH3** e e alterar o valor do campo numero para um numero acima do ultimo registro da **tabela RH3:**

Controle de numeração com o valor de 172![](https://centraldeatendimento.totvs.com/hc/article_attachments/22381125990807)

Ultimo código da **tabela RH3** com o valor de 171![](https://centraldeatendimento.totvs.com/hc/article_attachments/22381133998999)

Após todas as conferência, se o cenário não for corrigido, **abra um** ***ticket*** **ao Suporte**, com as evidências tendo em comparação, **todas as informações acima citadas nesse artigo**, juntamente com *prints* ou vídeo de **todo o processo de login no** ***App*** **Meu RH, até a inserção do abono** demonstrando a inconsistência na gravação do registro.  
  
A orientação é verificar se no momento da inserção não houve por ventura algum *errorlog*.  
Por fim, numa **aba de Visitante do Navegador, sem a influência de memória cache**, insira novamente o abono ao funcionário.  
  
Verifique as inclusões, nas tabelas envolvidas:  
**ACB e AC9 = referente ao anexo inserido se houver**  
**RH3, RH4 e RGK = solicitação realizada.**  
  
**Saiba Mais:**  
[**CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH**](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI para acessar a documentação de referência do MEU RH**](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
