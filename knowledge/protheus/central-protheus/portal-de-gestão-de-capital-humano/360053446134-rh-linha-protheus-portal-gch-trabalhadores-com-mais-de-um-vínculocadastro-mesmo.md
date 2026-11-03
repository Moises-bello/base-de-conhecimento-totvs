---
article_id: 360053446134
category: Portal de Gestão de Capital Humano
content_hash: 2c37af93f8f944ef49754011c75e4b194c32ab5e1e6d71b34529dc97ff32294b
fetched_at: '2026-06-28T22:43:00.151165+00:00'
product: protheus
section_id: 206960887
source: central-protheus
title: RH - Linha Protheus - PORTAL GCH - Trabalhadores com mais de um Vínculo/Cadastro
  (mesmo CPF) no módulo "07 - SIGAGPE"
type: support-article
updated_at: '2021-09-29T13:13:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053446134-RH-Linha-Protheus-PORTAL-GCH-Trabalhadores-com-mais-de-um-V%C3%ADnculo-Cadastro-mesmo-CPF-no-m%C3%B3dulo-07-SIGAGPE
---

**Ocorrência**Trabalhadores com mais de um Vínculo/Cadastro (mesmo CPF) no módulo "07 - SIGAGPE".  
  
**Ambiente**TOTVS RH (Linha Protheus) - Portal Gestão do Capital Humano – Todas as versões  
  
**Solução**Após realizar um segundo cadastro de um mesmo Trabalhador/CPF no módulo "07- SIGAGPE" o Sistema apresenta a pergunta abaixo para Relacionar ou Não o **Cadastro do Participante**.  
  
Para o acesso correto ao Portal GCH é obrigatório que seja criado esse relacionamento, já estamos trabalhando e melhorias para isso ser automático, mas deve ser estudado o impacto disso em outras rotinas do Protheus.  
  
Clicando em **SIM** para que seja relacionado o vínculo, será criado somente um único registro no **Cadastro de Participantes** relativo a ambos registros do Cadastro do Trabalhador do módulo "07- SIGAGPE".  
  
Desta forma, quando o Usuário/Participante for logar no Portal GCH, serão apresentadas as duas matrículas para que o Usuário/Participante selecione sobre qual registro gostaria de fazer o acesso.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360059811773/mceclip0.png)  
  
Caso tenha respondido **NÃO**,  sugerimos que faça o seguinte procedimento:

1. Backup da tabela RD0 e RDZ;
2. Delete os registros deste Participante de ambas as tabelas (RD0 e RDZ);
3. Acesse o **Cadastro de Participantes** e relacione o Participante novamente, seleciona SIM quando a pergunta for apresentada:  
   [MP - PORTAL GCH - Como relacionar os Participantes](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051031874)

**ATENÇÃO:** Certifique-se sempre de estar com seu ambiente atualizado com os pacotes abaixo:   
[MP - PORTAL GCH - Como Atualizar os arquivos do Portal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044250613)    
[MP - GPE - Pacote de acumulado do RH no Portal de Cliente](https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848-MP-GPE-Pacote-de-acumulado-do-RH-no-Portal-de-Cliente)         
 **Saiba Mais**Para saber mais consulte os links abaixo:   
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o Portal GCH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960887-RH-Portal-de-Gest%C3%A3o-de-Capital-Humano)
