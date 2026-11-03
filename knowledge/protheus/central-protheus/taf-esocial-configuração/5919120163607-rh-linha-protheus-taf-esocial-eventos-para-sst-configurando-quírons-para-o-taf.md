---
article_id: 5919120163607
category: TAF - eSocial - Configuração
content_hash: 742c97c723f91c9efe618c5a729d3dabcd97c2e386c4bcef4b26909bc0c5c491
fetched_at: '2026-06-28T22:45:14.518440+00:00'
product: protheus
section_id: 1500001536941
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Eventos para SST - Configurando Quírons
  para o TAF
type: support-article
updated_at: '2026-06-24T12:18:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5919120163607-RH-Linha-Protheus-TAF-eSocial-Eventos-para-SST-Configurando-Qu%C3%ADrons-para-o-TAF
---

**Dúvida**Como realizar a configuração do Quírons para o TAF?  
  
**Ambiente**RH - Linha Protheus - TAF - eSocial - Todas as versões

**Atenção:**  
As informações de integração devem ser configuradas individualmente em cada filial do Quírons. Ou seja, é necessário informar os dados de integração em cada uma das filiais cadastradas.

**Configuração do REST:**

Deverá ser configurado um REST (caso não possua) seguindo a orientação confirme material abaixo:

[Automação Fiscal - Configuração - Como criar serviço REST](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413012525591)

**Solução**

Para realizar a configuração, siga os passos abaixo:

1. Acesse a aba de Integrações, clicando sobre o seu nome de usuário localizado no canto superior direito e selecione a opção "Minha Conta":

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5919270816535)

2. Na página "Minha Conta", selecione a opção "Organização":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5919366149911)

3. Na área de Informações Organizacionais, edite as informações clicando no ícone de Lápis localizado à direita dessa área:  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5919391348503)

4. Informe a data de início da obrigatoriedade de SST para a organização, bem como o estado do e-Social como "Produção" (ou "Produção Restrita" para testes):

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5919517218199)

5. Em seguida, vá para a área de "Gerenciar Filiais" e clique na filial que deseja configurar.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5921176728343)

6. Nas configurações de integração à direita, preencha as informações referentes à integração do TAF:

* **Empresa:** Código da Empresa no TAF.
* **Filial:** Código da Filial no TAF.
* **Tipo de Integração:** Deve ser informado "TAF".
* **URL:** URL do REST onde o TAF está disponível.
* **Porta:** Porta do REST onde o TAF está disponível.

**Importante!** Se a URL já contiver a porta ou algum DNS ou URI específica, deixe essa informação zerada. Por exemplo: <https://192.168.0.1:8085/rest> ou <https://minhaorganizacao.com.br/taf>. Em ambos os cenários, a porta é 0.

* **Forma de Autenticação:** Deve ser informada "BasicAuth".
* **Usuário:** Usuário de acesso ao Protheus.
* **Senha:** Senha de acesso ao Protheus.
* **URL TSS:** Não é utilizado na integração TAF. É necessário apontar a URL onde está o serviço do TSS.

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5921136517399)

7. Após preencher as informações, o botão "Fila de Integração eSocial" será habilitado, localizado à direita da filial:

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5921243256599)

8. Clique em "Enviar Carga" para iniciar a carga dos eventos S-2240.:

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5921241066007)

10. Após a conclusão dessa operação, todos os funcionários devem possuir eventos S-2240 gerados. A partir desse momento, as CATs (S-2210) e ASOs (S-2220) gerados serão integrados ao TAF no momento de seu lançamento e/ou impressão.
