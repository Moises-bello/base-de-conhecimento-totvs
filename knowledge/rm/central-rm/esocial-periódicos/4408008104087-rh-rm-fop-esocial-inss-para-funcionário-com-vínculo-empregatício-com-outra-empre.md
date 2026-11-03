---
article_id: 4408008104087
category: esocial - Periódicos
content_hash: 3c5ba80a0dc4b02c08cf5c6788ec610b1ff0b2a695422e2d39f444495b96a231
fetched_at: '2026-06-28T22:47:09.423583+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - INSS para funcionário com vínculo empregatício com
  outra empresa
type: support-article
updated_at: '2026-02-02T15:07:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4408008104087-RH-RM-FOP-eSocial-INSS-para-funcion%C3%A1rio-com-v%C3%ADnculo-empregat%C3%ADcio-com-outra-empresa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17875050103575) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**  
Como realizar o lançamento do INSS de funcionário que possua vínculo com terceiros para correta geração dos eventos eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**  
Para que o sistema calcule e gere corretamente o INSS e, consequentemente, os eventos eSocial para funcionários que possuam vínculo com outras empresas, siga os passos abaixo:

1. No cadastro do funcionário, acesse **Anexos | Folha de Pagamento | Vínculos Empregatícios com Outras Empresas (Terceiros)**;  
1.1. Crie um novo registro preenchendo os dados referente à empresa terceira e ao desconto de INSS realizado por ela. Salve o registro;

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408006877207)

2. Posteriormente, será necessário lançar manualmente (via grupo de eventos, direto no envelope, etc.) uma verba com o código de cálculo **72 - Base INSS Outro Emprego** ou o **181 - Base INSS Outro Emprego Desconto Complementar**;  
2.1. Com o lançamento dos códigos de cálculo supracitados, o sistema irá lançar o código de cálculo **29 - INSS Outro Emprego**, que será utilizado então como base para o cálculo do INSS na empresa atual;

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408007643927)

3. Ao gerar o S-1200, o sistema irá usar as informações do anexo apontado no passo 1 para geração do grupo **infoMV** e as verbas de **Base INSS Outro Emprego** e **INSS Outro Emprego** serão geradas no grupo **remunPerApur**.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4408014382359)

**Importante**  
**1.** O anexo **Folha de Pagamento | Vínculos Empregatícios com Outras Empresas (Terceiros)** não deve ser preenchido quando o outro vínculo do funcionário estiver em outra coligada.   
O anexo também não deve ser preenchido se a empresa atual será a primeira a calcular o INSS do funcionário pois, nesse caso, não é necessário gerar no XML o grupo **infoMV**.  
**2.**Quando a categoria eSocial de ambos os vinculos forem referente a Trabalhador sem Vínculo, o evento a ser lançado no envelope será o de **Código de Cálculo 417- Base Tributada de INSS Autônomos Múltiplos Vínculos** para correta geração do XML com a devida **infoMV**:

![ENVMV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17875333042455)  
  
![XMLMV.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17875122825751)

**Saiba mais**  
Para mais informações, acesse:  
     - [Qual o funcionamento do evento com o código de cálculo 181 e o código de cálculo 72?](https://tdn.totvs.com.br/pages/releaseview.action?pageId=514454885)  
     - [Códigos de Cálculo](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719279)  
[- Código de Cálculo 417- Base Tributada de INSS Autônomos Múltiplos Vínculos](https://tdn.totvs.com/pages/viewpage.action?pageId=492700190)
