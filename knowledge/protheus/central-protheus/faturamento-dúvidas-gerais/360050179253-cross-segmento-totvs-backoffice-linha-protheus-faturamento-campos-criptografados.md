---
article_id: 360050179253
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 59c16ad46b3002e25252587d9832492772fccd664b4a296db9032e34860f1f6e
fetched_at: '2026-06-28T22:38:28.474742+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Campos Criptografados
type: support-article
updated_at: '2021-07-30T19:46:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050179253-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-Campos-Criptografados
---

**Dúvida**

A alterar o cadastro da transportadora (**MATA050**), o campo fica cheio de asteriscos como se estivesse criptografado.  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento- a partir de release 12.1.23.

**Solução**

A partir da atualização de fev/2020, a Totvs disponibilizou para todas as releases de lobo guará, a atualização para atender a legislação de LGPD, lei de proteção de dados, onde algumas informações importantes como cpf, endereço, entre outro dados que são considerados como dados sensíveis, não serão apresentados a qualquer usuário do sistema sem a devida permissão no configurador.  
  
O que precisa ser visto pelo administrador do sistema no configurador em  usuários, um usuário diferente de administrador, restrições de acesso, acessos, se exitem as perguntas 192 e 193, e se as mesmas estão marcadas:  
  
![](https://totvssuporte.zendesk.com/attachments/token/TWJSVMfF6OrLSsXlSWYxYdeM6/?name=inline165427172.png)​  
Se as perguntas estiverem conforme o exemplo acima, o cadastro aparecerá com \*\*\*, conforme abaixo:

![](https://totvssuporte.zendesk.com/attachments/token/zeA9AQlwmcDZsOoUKwdc14JIS/?name=inline-310937286.png)​

O administrador ficará normal, até por que é ele quem controla qual o usuário deve ter acesso aos dados. Se as perguntas forem ticadas, conforme abaixo, o usuário terá acesso as informações sem asteriscos:

![](https://totvssuporte.zendesk.com/attachments/token/KaXmkBXyTTHJ49nwvSLM6cKTW/?name=inline-1281936469.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/Z8ABrxNHgHQtsIv244KR28UsQ/?name=inline892614044.png)​  
Verifique se possui essas perguntas no seu configurador, para poder configurar e assim, seus usuários poderão visualizar todas as informações do cadastro.  
  
Caso não tenha, deverá efetuar os passos indicados pela equipe de framework:  
  
Segue passo a passo:  
  
- Pare o serviço Protheus;  
- Faça o backup do RPO;  
- Baixe o Pacote e Dicionário de Dados Diferencial do link abaixo:**[https://suporte.totvs.com/portal/p/10098/download?e=947547](https://www.google.com/url?q=https://suporte.totvs.com/portal/p/10098/download?e%3D947547&sa=D&source=hangouts&ust=1591108062103000&usg=AFQjCNHXYBJioX6S8ylxNPOCQK6RS8UAcA)**  
- Aplique o pacote TTTP120\_LG.PTM;  
- Descompacte o arquivo sdfbra.txt na pasta systemload;  
-Posteriormente, executar o UPDDISTR com o Dicionário de Dados do link passado na interação anterior.  
  
Caso precise apoio na configuração das perguntas, contate a equipe de Frame Work através de um novo atendimento.  
  
Esta é a documentação oficial sobre a lei e as implementações efetuadas por cada módulo do sistema**:** **[Controle de dados protegidos-Protheus+12](https://www.google.com/url?q=https://tdn.totvs.com/display/public/PROT/Controle%2Bde%2Bdados%2Bprotegidos%2B-%2BProtheus%2B12&sa=D&source=hangouts&ust=1591108062103000&usg=AFQjCNGDZwK-AFyFbM6riIpJ_nrsXYDSVA)**  
  
Observação, na release 12.1.27, essas perguntas já são nativas do sistema, não sendo necessário ajustes por dicionários e pacotes complementares.

A seguir estão os processos ajustados para o módulo **Faturamento** – **SIGAFAT**, observando os dados sensíveis e pessoais que são passíveis de proteção dentro do **Sistema Protheus®**.

* **Cadastros (Cliente, Vendedor, Transportadora...)**
* **Cenários de Venda**
* **Gestão de Contas**
* **Administração de Vendas**
* **Contratos**
* **Orçamentos**
* **Pedido de Venda**
* **Consultas**
* **Relatórios**

***Obs: O ajuste da LGPD na release 12.1.17 do Protheus, somente ocorrerá para a versão  com garantia estendida, conforme a documentação informada acima. Lembrando que a a release12.1.17 com garantia estendida foi descontinuada em junho/2021.***
