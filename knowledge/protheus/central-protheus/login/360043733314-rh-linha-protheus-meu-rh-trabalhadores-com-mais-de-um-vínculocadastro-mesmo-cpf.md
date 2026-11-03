---
article_id: 360043733314
category: LOGIN
content_hash: a0f0557a718cd59e32b31e456ca29b1b8984cc6b3bff1c8d11a46e6aa8279ed9
fetched_at: '2026-06-28T22:44:40.667392+00:00'
product: protheus
section_id: 10299559916567
source: central-protheus
title: RH - Linha Protheus - MEU RH - Trabalhadores com mais de um Vínculo/Cadastro
  (mesmo CPF) no módulo "07 - SIGAGPE"
type: support-article
updated_at: '2026-06-18T19:20:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043733314-RH-Linha-Protheus-MEU-RH-Trabalhadores-com-mais-de-um-V%C3%ADnculo-Cadastro-mesmo-CPF-no-m%C3%B3dulo-07-SIGAGPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min**

**Dúvida**

MEU RH - Trabalhadores com mais de um Vínculo/Cadastro (mesmo CPF) no módulo "07 - SIGAGPE"  
 **Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas às versões  
  
**Solução**Após realizar um segundo cadastro de um mesmo Trabalhador/CPF no módulo "07- SIGAGPE" o Sistema Apresenta a pergunta abaixo para Relacionar ou Não o **Cadastro do Participante**.  
  
Para o acesso correto ao MEU RH é obrigatório que seja criado esse relacionamento, já estamos trabalhando e melhorias para isso ser automático, mas deve ser estudado o impacto disso em outras rotinas do Protheus.  
  
Clicando em **SIM** para que seja relacionado o vínculo, será criado somente um único registro no **Cadastro de Participantes** relativo a ambos registros do Cadastro do Trabalhador do módulo "07- SIGAGPE"  
  
Desta forma, quando o Usuário/Participante efetuar o login no **MEU RH,** serão apresentadas as duas matrículas para que o Usuário/Participante selecione sobre qual registro gostaria de fazer o acesso.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059811773/mceclip0.png)  
  
Caso tenha respondido **NÃO**,  sugerimos que faça o seguinte procedimento:

1. Backup da tabela RD0 e RDZ;
2. Delete os registros deste Participante de ambas as tabelas (RD0 e RDZ);
3. Acesse o **Cadastro de Participantes** e relacione o Participante novamente, seleciona SIM quando a pergunta for apresentada:  
   **[RH - Linha Protheus - MEU RH - Como relacionar os Participantes?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050255013)**

**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado, pois são disponibilizados periodicamente atualizações com melhorias e correções no MEU RH.  
**[RH - Linha Protheus - MEU RH - Onde baixo a versão mais recente e como atualizar os arquivos do Portal Meu RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043729034)**  
**[RH - Linha Protheus - MEU RH - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007189282)****Saiba Mais:  
[RH - Linha Protheus - MEU RH - Configuração para Login no MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044227453)**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
