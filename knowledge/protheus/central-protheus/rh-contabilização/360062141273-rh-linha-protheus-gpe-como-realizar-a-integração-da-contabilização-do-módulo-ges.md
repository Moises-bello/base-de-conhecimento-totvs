---
article_id: 360062141273
category: RH - Contabilização
content_hash: 4f0497da854eab4ec630d214be9477a127c527cf2bcb89c21bada579b9e913b5
fetched_at: '2026-06-28T22:43:45.859461+00:00'
product: protheus
section_id: 360003109092
source: central-protheus
title: RH - Linha Protheus - GPE - Como realizar a integração da contabilização do
  módulo Gestão de Pessoal com o módulo CON do Logix
type: support-article
updated_at: '2026-06-17T19:31:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062141273-RH-Linha-Protheus-GPE-Como-realizar-a-integra%C3%A7%C3%A3o-da-contabiliza%C3%A7%C3%A3o-do-m%C3%B3dulo-Gest%C3%A3o-de-Pessoal-com-o-m%C3%B3dulo-CON-do-Logix
---

**Dúvida**  
Como realizar a integração da contabilização do módulo Gestão de Pessoal com o módulo CON do Logix ?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.  
  
**Solução**  
Para que a Contabilização seja gerada em arquivo de texto no formato aceito pelo Módulo CON do Logix, siga as instruções abaixo:  
  
**1.** Criar o **De/Para Empresas Mensagem Única**  
**Acessar:** Configurador ->Ambiente ->Schedule ->Emp. filial Mensagem Única: neste cadastro você deve realizar o De/Para das filiais contidas no **Protheus** e outras marcas clicando em Incluir.  
![de_para.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360102727653)  
  
**2.** Ajustar os parâmetros de integração **MV\_RHCONEX, MV\_PASCON e MV\_ERPLOGI**  
**Acessar:** Configurador ->Ambiente ->Cadastros ->Parâmetros: efetuar a busca dos parâmetros relacionados acima.  
  
O parâmetro **MV\_RHCONEX** indica se há ou não integração contábil do RH com um sistema externo, gerando um arquivo TXT. O conteúdo do parâmetro deve ser **.T.**  
![MV_RHCONEX.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360100560354)  
  
O parâmetro **MV\_PASCON** armazena o caminho para geração do arquivo de texto da contabilização  
![MV_PASCON.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360100560394)  
  
O parâmetro **MV\_ERPLOGI** Indica se utiliza integração com o Sistema **LOGIX**. O conteúdo do parâmetro deve ser **1**  
![MV_ERPLOG.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001667202)  
  
**3.** Após realizar as parametrizações acima deve ser executado o procedimento de Contabilização no Gestão de Pessoal preenchendo as perguntas para contabilização na rotina **GPEM110**:   
**Acessar:** Gestão de Pessoal ->Miscelânea ->Fechamentos ->Contabilização: depois que os dados forem apresentados, clique em **Salvar**.  
![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/360102728153)  
  
**4.** Em seguida o sistema apresentará a tela referente **Integração Contábil GPE X Sistema Externo** direcionando para a pasta que consta no parâmetro **MV\_PASCON**, clique novamente em **Salvar** para gerar o arquivo no local indicado.  
  
O sistema leva a informação do campo Código do Histórico Padrão na posição 10 do Txt de integração.

Esse campo funciona da seguinte forma:

* Campo em branco

A informação levada para o Txt será o código do Lançamento Padrão, campo CT2\_LP.

* Campo preenchido

A informação será o código informado pelo usuário no campo.

![contabiliza__o.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001667462)  
  
**5.** Demonstração do arquivo no formato aceito pelo módulo **CON** do **Logix** com o campo preenchido:  
![arquivo.jpg](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001715241)

**Importante:**

Para que a Contabilização seja gerada em arquivo no formato XML, além da configuração descrita acima, é necessário que haja Cadastro do Adapter para a rotin CTBA102, conforme o exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/41303202528663)

Vale ressaltar que a imagem acima apresenta um modelo simples de configuração do adapter, e caso haja dúvidas na configuração do Adapter, indicamos que seja acionado o suporte do Módulo Contabilidade Gerencial.

**Saiba Mais:**  
<https://tdn.totvs.com/pages/releaseview.action?pageId=590229085>
