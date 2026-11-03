---
article_id: 360010412872
category: RH - Funcionários
content_hash: e9c582047074717c74d2f8702dfce62994def8fac6307d32d5970d2ac4933827
fetched_at: '2026-06-28T22:43:27.345469+00:00'
product: protheus
section_id: 360011909593
source: central-protheus
title: RH - Linha Protheus - GPE - Alterando Função/Cargo do Funcionário o Salário
  é Zerado
type: support-article
updated_at: '2025-08-13T17:43:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360010412872-RH-Linha-Protheus-GPE-Alterando-Fun%C3%A7%C3%A3o-Cargo-do-Funcion%C3%A1rio-o-Sal%C3%A1rio-%C3%A9-Zerado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31481701452311) Tempo aproximado para leitura: **00:01:00 min**

**Dúvida**No módulo **Gestão de Pessoal**, ao alterar função/cargo de uma matrícula no **Cadastro de****Funcionários** o salário deste é zerado.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**Esta situação pode ocorrer, quando a **configuração do parâmetro MV\_ALTSAL** está ativa e/ou a configuração do parâmetro **MV\_FUNCARG está com C** e não existe faixas salariais cadastradas corretamente no módulo SIGACSA.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986447163415)

Para solucionar essa ocorrência, realize os seguintes passos:  
**1 -** Acesse ambiente **SIGACFG (Configurador);**  
**2 -** Através do menu, selecione **Ambiente >** **Cadastros >** **Parâmetros**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986463642903)  
  
**3 -** Clique no sinal de + depois em **Parâmetros**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986545878807)**

**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986505205271)**

**4 -** Clique no ícone da lupa e busque pelo parâmetro **MV\_ALTSAL**

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986572039831)  
  
**5 -** Selecione o parâmetro e clique em **Alterar**

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10986567684759)  
  
**6 -** Altere campo **Cont. Por (Conteúdo Português)**para **"S"**, caso **deseje** que sistema **altere** campo CBO e salário quando alterada Função, ou **"N"** caso **não deseje** que sistema altere campo CBO e salário quando alterada Função.  
  
**7 -** Faça o mesmo procedimento para alteração do parâmetro MV\_FUNCARG, e altere campo **Cont. Por (Conteúdo Português)**para **"F"****Saber Mais:**

[RH - Linha Protheus - GPE - Como alterar função no Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360054491674-RH-Linha-Protheus-GPE-Como-alterar-fun%C3%A7%C3%A3o-no-Gest%C3%A3o-de-Pessoal?source=search)

[RH - Linha Protheus - GPE - Como alterar a Função durante uma transferência](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058248473-RH-Linha-Protheus-GPE-Como-alterar-a-Fun%C3%A7%C3%A3o-durante-uma-transfer%C3%AAncia?source=search)

[RH - Linha Protheus - GPE - Ao alterar uma função no cadastro de funcionário apresenta a mensagem "Não foi possível recuperar o código do cargo"](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403611535255-RH-Linha-Protheus-GPE-Ao-alterar-uma-fun%C3%A7%C3%A3o-no-cadastro-de-funcion%C3%A1rio-apresenta-a-mensagem-N%C3%A3o-foi-poss%C3%ADvel-recuperar-o-c%C3%B3digo-do-cargo-?source=search)

[RH - Linha Protheus - GPE - Após o cadastro do funcionário, como posso alterar os dados de Centro de Custo, Departamento e Função](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404571023767-RH-Linha-Protheus-GPE-Ap%C3%B3s-o-cadastro-do-funcion%C3%A1rio-como-posso-alterar-os-dados-de-Centro-de-Custo-Departamento-e-Fun%C3%A7%C3%A3o?source=search)  
[Parâmetros MV\_ALTSAL e MV\_FUNCARG](https://tdn.totvs.com/pages/viewpage.action?pageId=233760654)
