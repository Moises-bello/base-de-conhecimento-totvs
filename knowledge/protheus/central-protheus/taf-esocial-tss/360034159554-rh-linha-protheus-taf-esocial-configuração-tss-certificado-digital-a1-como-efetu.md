---
article_id: 360034159554
category: TAF - eSocial -TSS
content_hash: 2a5b9fed5d8d9bf19189883f0d5a2d41ef68237ad978389fd968a64b32620abd
fetched_at: '2026-06-28T22:45:21.922695+00:00'
product: protheus
section_id: 1500001536761
source: central-protheus
title: RH - Linha Protheus - TAF - eSocial - Configuração - TSS - Certificado Digital
  A1 - Como Efetuar Preparação do Certificado Digital e Configurá-lo no TAF?
type: support-article
updated_at: '2026-06-19T21:33:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034159554-RH-Linha-Protheus-TAF-eSocial-Configura%C3%A7%C3%A3o-TSS-Certificado-Digital-A1-Como-Efetuar-Prepara%C3%A7%C3%A3o-do-Certificado-Digital-e-Configur%C3%A1-lo-no-TAF
---

**Dúvida**  
Como efetuar preparação do Certificado Digital para configuração do TSS no TAF?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF eSocial - Atualizador - TSS - Todas as versões  
  
**Solução**

**INSTALAÇÃO DO CERTIFICADO DIGITAL**

1 - Realize a instalação do certificado digital no seu computador:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229898973335)

2 - Especifique o arquivo a ser importado e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856667543)

3 - Insira a senha e selecione as 2 opções de importação e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856671895)

4 - Selecione o repositório para guardar o arquivo e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856675095)

5 - Conclua o assistente:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899005079)

6 - Clique em Ok para finalizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899008407)

7 - Finalizado a importação, deverá ser exibido a mensagem abaixo. Clique em Ok para finalizar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856683799)

**EXPORTAÇÃO DO CERTIFICADO DIGITAL COM CHAVE PRIVADA**

1 - Acesse o Painel de Controle, Rede e Intenet e Opções de Internet ou digite Opções de Internet no menu iniciar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856690839)

2 - Clique na Aba: Conteudo > Certificados:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856692375)

3 - Selecione o certificado da empresa e clique em Exportar:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856695959)

4 - Marque a opção, Sim, exportar a chave privada e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899022359)

5 - Deixe selecionado as opções e avance:

- Incluir todos os certificados no caminho de certificação, se possível,  
- Habilitar privacidade de certificados

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856700183)

6 - Informe novamente a senha do certificado digital e confirme duas vezes e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899030679)

7 - Selecione o arquivo para sobescrever o arquivo salve e avance:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899032087)

8 - Clique em concluir:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229856710039)

9 - Finalize clicando em ok

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27229899041431)

**CONFIGURANDO O CERTFICADO DIGITAL NO SISTEMA**

1 - Acesse o TAF;

2 - Clique em Atualizações e Wizard Config TSS;

3 - Em Rotina de Configuração do Ambiente TAF, clica em Avançar;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001647222)

4 - Verifique se o ambiente é Produção ou Homologação:

5 - Se o ambiente for produção, os campos Ambiente e-Social e Ambiente Reinf.   
Deixe a opção 1 – Produção e clique em Avançar;   
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001695041)

6 - Se o ambiente for homologação, os campos Ambiente e-Social e Ambiente Reinf, deixe a opção 2 – Pré Produção – dados reais e clique em Avançar;  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001647262)

7 - Selecione o tipo de Certificado**(.pem, .pfx, .p12, etc...)** Lembrando que o Smart eSocial não aceita certificado do tipo A3 e os arquivo tem que ser maior ou igual a 7kb. Clique no botão **...** para a selecionar o Certificado Digital;  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001647302)

8 - Repare que ao acessar o certificado digital na sua máquina, no canto superior direito existe um link escrito Arquivos locais: clique aqui*.* Selecione o certificado e clica em Salvar;  
  
**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001695081)**

9 - Digite a senha do certificado digital;  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102708773)

10 - Caso a empresa possua certificado de outorga (procuração eletrônica), antes de avançar, informe o CNPJ ou CPF diferente do empregador, caso não possua outorga, pode deixar o campo em branco e clique em Avançar;  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360100541214)

11 - Se o Certificado Digital não tiver algum problema, ele irá informar que foi configurado com sucesso e clica em Finalizar.
