---
article_id: 1500011294261
category: Call Center - Dúvidas Gerais
content_hash: 9694739be5135d67f9ec9adaad6e63d3831e6292a09177aa216a41adad5b355e
fetched_at: '2026-06-28T22:41:26.600061+00:00'
product: protheus
section_id: 1500001548242
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigatmk - Painel de Gestão
  On line
type: support-article
updated_at: '2021-05-19T12:18:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011294261-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Sigatmk-Painel-de-Gest%C3%A3o-On-line
---

**Dúvida**Configuração do Painel de Gestão On line do Call Center  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Sigatmk - Todas as versões  
  
**Solução**O Painel Online é um recurso que exibe alguns indicadores do módulo na tela principal do mesmo ao acessar o Smartclient. Para que esses indicadores sejam configurados, a documentação de frame work para configuração e ini e do portal desejado:

**<https://tdn.totvs.com/display/public/PROT/Configurar+o+recurso+Painel+Online>**

**1- Exemplo da habilitação da chave para uso do painel no server.ini:**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018339081/mceclip0.png)

**2 - Visualização da habilitação do painel no configurador:**

![configura_ao_do_painel_do_tmk.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018044922/configura_ao_do_painel_do_tmk.gif)

Após as configurações, é necessário acessar o sistema em **modo de acesso MDI** ,e **com o usuário diferente de Admin e senha**. A configuração não aparece para o usuário Admin, ele apenas efetua a configuração em ambiente de Configurador.

Após acessar o sistema poderá visualizar, que é inserido antes a opção atualizações, a opção de Painel On line:

![paineis_tmk_abertura_do_m_dulo.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018355521/paineis_tmk_abertura_do_m_dulo.gif)

**Observação**: Para que cada painel apresente a quantidade de atendimentos relacionados ao tipo de atendimento Call Center é preciso ter esses atendimentos na base de dados.
