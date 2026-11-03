---
content_hash: 4715ca449632d8ed400ad2fc19a6a970e08437bb20b970a74adcb1fe31c70afe
fetched_at: '2026-06-29T00:08:21.988598+00:00'
page_id: '269070417'
product: rm
source: tdn-rm
title: RPT00015.1.2_Exportar_para_Html_Envio_de_E-mail_com_arquivo_Html_como_anexo
type: documentation
url: https://tdn.totvs.com/display/LRM/RPT00015.1.2_Exportar_para_Html_Envio_de_E-mail_com_arquivo_Html_como_anexo
version: 33
---

# Índice:

---

.\*ndice:

# Exportar para Html

---

**Passo a passo:**

falseI1° Passo

Ao gerar o relatório, na etapa **Tipo de Geração**, escolha **Exportação Para Arquivo**

2° Passo

Na Etapa **Tipo de Saída**, Escolha o tipo **Formato de página da Internet (HTML)**.

3° Passo

Na etapa **Caminho**, indique onde o relatório será salvo em sua máquina.

4° Passo

Ao término da geração do relatório, o mesmo será salvo no caminho descrito na etapa **Caminho**, nesse caso, na área de trabalho.

5° Passo

Da mesma forma, ainda no término da **geração do relatório**, o relatório será **apresentado automaticamente** em seu **Browser padrão**.

# Envio de E-mail com arquivo Html como anexo

---

**Passo a passo:**

falseI1° Passo

Ao gerar o relatório, na etapa **Tipo de Geração**, escolha **Envio Por E-Mail**.

2° Passo

Na etapa**Destinatários**marque os**usuários disponíveis,**como destinatários, ou preencha a caixa de texto com um e-mail que**não se encontre**na lista de**usuários disponíveis**. Nesse caso será enviado um e-mail para **[emaildeteste@totvs.com.br](mailto:emaildeteste@totvs.com.br)**.

3° Passo

Na etapa**Assunto,**digite o**assunto do e-mail**e os dizeres do**corpo da Mensagem**.O**corpo da Mensagem** pode ser**Texto,**como na imagem abaixo.

**O **corpo da mensagem** pode ser também um **arquivo HTML**.**

4° Passo

Clique em**[...]** escolha qual **arquivo HTML** será adicionado ao **corpo da mensagem**.

5° Passo

Após a escolha, o**arquivo HTML**selecionado estará descrito no campo **Corpo da Mensagem**.

6° Passo

Na Etapa **Tipo de Saída**, Escolha o tipo **Formato de página da Internet (HTML)**.

7° Passo

Ao término da geração do relatório, o mesmo será **anexado** ao e-mail. Ao clicar no **anexo do e-mail enviado,**o mesmo será**apresentado** em seu**Browser padrão**.

8° Passo

Da mesma forma, ainda no término da **geração do relatório**, o relatório será **apresentado automaticamente** em seu **Browser padrão**.

# Limitações

---

Existem algumas **limitações** tanto ao **exportar o relatório** como **HTML**, quanto **enviar o relatório, em anexo**, através do e-mail.

# Watermark (Marca d'água)

---

Utilizamos no **RM** um conjunto de componentes de uma empresa terceira chamada **"Devexpress"**, onde o **RM** Reports tem como base o **Xtrareports**, pertencente a esse conjunto de componentes.

A funcionalidade de **Watermark (Marca d'água / propriedade)** **não é suportada** quando o relatório é apresentado **via browser (navegador),** como reportado pelo próprio suporte da **Devexpress**.

Tanto a versão **10.1** dos componentes **Devexpress** utilizada na versão **11.8x** do **RM**, quanto a versão **14.1** dos componentes da **Devexpress** utilizada na versão **12.1.x** do **RM**, essa propriedade não é suportada.

Existem diversas respostas do suporte da **Devexpress**, em vários intervalos de tempo diferentes, porém colocamos a resposta mais recente que contempla a versão **14.1** da **Devexpress**, apresentada abaixo, traduzida.

**TÓPICO 1 : [XtraReport Export to HTML & MHT does not render watermark / background colour (Relatório Exportar para HTML e MHT, não renderiza marca d'água / cor de fundo)](https://www.devexpress.com/Support/Center/Question/Details/B192785)**

falseTradução

**[...]**

Infelizmente na atual versão do componente XtraReports, marcas d'agua não são apresentadas quando um relatório é usado em uma aplicação web ou exportada no formato HTML. Estamos avisados dessa limitação, e já registramos essa sugestão. 

**[...]**

**TÓPICO 2 : [Watermark not displayed in ReportViewer (Marca d'água não é apresentado no Visualizador de Relatório)](https://www.devexpress.com/Support/Center/Question/Details/CQ40087)**

falseTradução

**[...]**

Sim, o fato de que as marcas d'água não são apresentadas quando um relatório é usado em aplicações web são um problema conhecido - peço que siga a seguinte sugestão em nossa base de dados: "Marca d'água - essa propriedade deveria funcionar quando um relatório é usado em uma aplicação web" ([www.devexpress.com/issue=AS2844](http://www.devexpress.com/issue=AS2844)).

**[...]**

**[...]**

Atualmente, a habilidade de apresentar uma marca d'água dentro de uma página web não foi implementada em nenhuma versão recente desse componente (XtraReport). 

**[...]**

**TÓPICO 3 (Solução dada para versões superiores a 14.3): [Web - The Watermark property should also work when a report is used in a web application (Web - Marca 'água deveria funcionar corretamente quando um relatório é usado em uma aplicação web)](https://www.devexpress.com/Support/Center/Question/Details/AS2844)**

falseTraduçãoOBS

A solução foi dada na versão **14.3**, as soluções **RM** estão atualmente na versão **14.1**, não temos um prazo definido para a migração da versão da **14.1** para versões **superiores** que contemplem essa modificação.

**[...]**

**Implementado:**

* **v2014 vol 2.3**

**Informação Adicional:**

O controle [ASPxDocumentViewer](https://documentation.devexpress.com/#XtraReports/clsDevExpressXtraReportsWebASPxDocumentViewertopic) foi atualizado para suportar a apresentação de [textos e imagens como marcas d'água](https://documentation.devexpress.com/#WindowsForms/CustomDocument7225) em uma página web.

**[...]**

# Falta de Permissão na pasta /temp (usuário local ou Network Service)

---

Caso a imagem não apareça, pode ser um problema de permissão na pasta **/temp,** onde as **imagens** são **salvas temporariamente,** afim de serem **apresentadas** no **arquivo HTML**.

**3.2.1 -** Caso esteja "rodando" a aplicação através de um **usuário local (via host.exe),** verifique se existe **permissão** na pasta **[C:\Users\nomeusuariolocal\AppData\Local]**.

# 

**3.2.2 -** Caso esteja "rodando" a aplicação através de um **serviço (via host.service.exe),** verifique se existe **permissão** na pasta **[C:\Windows\ServiceProfiles\NetworkService\AppData\Local]**

**3.2.3** **-** Clique com o **botão direito** sobre a pasta **/Temp** e vá em **Compartilhar com** **>> Compartilhamento avançado**.

**3.2.4** **-** Marque a opção **Compartilhar pasta,** escolha um nome para o compartilhamento (opcional), depois clique em **Permissões**.

**3.2.5 -** Selecione (e/ou adicione) um **usuário** ou um **grupo** e dê as **permissões** necessárias.

**3.2.6 -** Com as **devidas permissões**, as **imagens** são apresentadas corretamente.

# Suporte das propriedades do componente PictureBox (Imagem) pelo HTML

---

Algumas propriedades do componente **Picturebox**, podem **(ou não)** ser **suportadas** em aplicações web, ou quando se exporta para um **arquivo HTML**.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| image2016-11-28 14:53:10.png1Propriedade Imagem   | Execução | Suporte | | --- | --- | | RM.Host | * Imagens Locais | | RM.Host.Service | * Imagens Locais | | image2016-11-28 14:14:8.png1Propriedade Caminho da Imagem   | Execução | Suporte | | --- | --- | | RM.Host | * Imagens Locais * Url (Web) | | RM.Host.Service | * Url (Web) | | image2016-11-28 14:59:35.png1Propriedade Ligação de Dados -> Caminho da Imagem   | Execução | Suporte | | --- | --- | | RM.Host | * Imagens Locais * Url (Web) | | RM.Host.Service | * Url (Web) |      * **Essa ligação pode ser feita através de**  **campos de tabela da base, ou campos** **de uma consulta SQL.** * **Deverá ser um campo texto contendo** **um caminho, sendo ele um caminho** **fisico na máquina ou uma url web.** |
| image2016-11-28 15:10:32.png1Propriedade Ligação de Dados -> Imagem   | Execução | Suporte | | --- | --- | | **RM.Host** | * **Binário (Consulta SQL)** * **Binário (Campo Base)** | | **RM.Host.Service** | * **Binário (Consulta SQL)** * **Binário (Campo Base)** |      * **Essa ligação pode ser feita através de**  **campos de tabela da base, ou campos** **de uma consulta SQL.** * **Deverá ser um campo texto contendo** **um numero binário representadno a  imagem****.** |  |  |

# Localização das Imagens

---

Para que as imagens sejam apresentadas corretamente elas devem estar em uma pasta com as devidas permissões.

# Locais não permitidos

---

* **Área de Trabalho**
* Meu Computador\**Imagens**
* Meu Computador\**Documentos**
* Meu Computador\**Downloads**
* Meu Computador\**Musicas**
* Meu Computador\**Videos**

Etc...

Em sua grande maioria os locais não permitidos são pastas do sistema operacional com restrições nativas de permissão.

# Locais permitidos

---

* Desktop\**Nome\_de\_pasta\_customizada**
* C:\**Nome\_de\_pasta\_customizada**

falsefalse

**Produto:** Framework

false

**Versão:** 12.01.XX

false

**Processo:** Exportar para HTML

falsefalse

**Status:** Finalizado

false

**Data:** 10/10/2017

false

**Autores:**
