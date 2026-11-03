---
article_id: 9778762633367
category: eSocial - Parametrizador
content_hash: 84fe245bf32b6c87df683af1821e33fe5065fec36ba57d4773356e29d9a7dbb9
fetched_at: '2026-06-28T22:47:06.297068+00:00'
product: rm
section_id: 1500000834501
source: central-rm
title: RH - RM - FOP - eSocial - Ao realizar a inclusão do evento S-1200 manualmente
  o sistema não encontra o código do funcionário
type: support-article
updated_at: '2024-12-30T13:51:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9778762633367-RH-RM-FOP-eSocial-Ao-realizar-a-inclus%C3%A3o-do-evento-S-1200-manualmente-o-sistema-n%C3%A3o-encontra-o-c%C3%B3digo-do-funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Ocorrência**Ao realizar a inclusão do evento S-1200 manualmente na Fila de Eventos o sistema não localiza o código de pessoa do funcionário, impossibilitando registrar o evento.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778498569751)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O funcionário não é localizado devido ao **Tipo de Regime Previdenciário** no cadastro do funcionário não está preenchido.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778549851671)

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse **Administração de Pessoal | Funcionários** e localize o funcionário;2. No cadastro do funcionário que apresentou a inconsistência, acesse aba **Situação** e preencha o **Tipo de Regime Previdenciário** de acordo com o regime do funcionário.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/9778654254103)

3. Após realizar o ajuste, salve o cadastro do funcionário e inclua novamente o XML do evento S-1200.
