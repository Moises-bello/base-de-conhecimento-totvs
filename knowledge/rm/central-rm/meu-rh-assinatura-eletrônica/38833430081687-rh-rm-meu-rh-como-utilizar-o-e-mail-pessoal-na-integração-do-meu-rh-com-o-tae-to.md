---
article_id: 38833430081687
category: Meu RH - Assinatura Eletrônica
content_hash: c47e503fbd155c5ef82adb3f14018e661e6ce0eb620c3b259c5af969d5df56b7
fetched_at: '2026-06-28T22:47:28.729830+00:00'
product: rm
section_id: 19399655101335
source: central-rm
title: RH - RM - Meu RH - Como utilizar o e-mail pessoal na integração do Meu RH com
  o TAE (Totvs Assinatura Eletrônica)
type: support-article
updated_at: '2026-03-06T20:45:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/38833430081687-RH-RM-Meu-RH-Como-utilizar-o-e-mail-pessoal-na-integra%C3%A7%C3%A3o-do-Meu-RH-com-o-TAE-Totvs-Assinatura-Eletr%C3%B4nica
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/38833446746007) Tempo aproximado para leitura: **00:02:03 min**  
  
**Dúvida**  
Como configurar o uso do e-mail pessoal do funcionário na integração de documentos do RM com o TOTVS Assinatura Eletrônica, de forma que os documentos também fiquem disponíveis para visualização no Meu RH?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Meu RH - A partir do release 12.1.2510.186  
  
**Solução**  
Para utilizar o e-mail pessoal na integração do Meu RH com o TAE , realize os seguintes passos:  
  
1. Na configuração de [**Tipos de relatório**](https://RH%20-%20RM%20-%20FOP%20-%20Assinatura%20Eletr%C3%B4nica:%20Tipos%20de%20relat%C3%B3rio), marque o parâmetro  **“Utilizar e-mail pessoal do destinatário caso o principal não esteja preenchido”.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38833446746903)

2. No Grupo de Quiosque do colaborador, acessado pelo caminho: **Folha de pagamento > Configurações > Parametrizador > RM Portal > Edite o Quiosque > Portal Meu RH**, marque o parâmetro  **“Utilizar e-mail pessoal do destinatário caso o principal não esteja preenchido”.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38833446747543)

3. Acesse o cadastro do funcionário e confirme se o campo E-mail Principal, na aba **Identificação**, não está preenchido. Se houver um e-mail informado nesse campo, ele terá prioridade sobre o e-mail pessoal e irá desconsiderá-lo.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38833430051991)

4. Na aba **Endereço Principal** do cadastro do funcionário, preencha o email desejado no campo **EMAILPESSOAL:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/38833430055703)

5. Após efetuar estas parametrizações, ao executar o [**processo de integração de relatórios**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/37934115126551-RH-RM-FOP-TOTVS-Assinatura-Eletr%C3%B4nica-Como-enviar-os-relat%C3%B3rio-do-RM-para-o-TAE-Assinatura-Eletr%C3%B4nica) para o TAE, ele será enviado ao e-mail pessoal do funcionário e ficará disponível também para exibição no Meu RH:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/38833430056471)

**Saiba mais:**

[Integração Meu RH x TAE - RM](https://tdn.totvs.com/pages/viewpage.action?pageId=733186927)

[RH - RM - Meu RH - Relatórios não são apresentado no Meu RH para Assinatura Eletrônica](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19396820792343-RH-RM-Meu-RH-Relat%C3%B3rios-n%C3%A3o-s%C3%A3o-apresentado-no-Meu-RH-para-Assinatura-Eletr%C3%B4nica)
