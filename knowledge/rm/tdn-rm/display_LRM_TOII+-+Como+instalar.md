---
content_hash: fb2b36f9714b4381f1fcbb7e21ccc79bab2c5e21cb5f1400f386bd395b78d111
fetched_at: '2026-06-29T00:11:44.092884+00:00'
page_id: '80970449'
product: rm
source: tdn-rm
title: TOII - Como instalar
type: documentation
url: https://tdn.totvs.com/display/LRM/TOII+-+Como+instalar
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Instalação do TOII |
| **Subprocesso** | **:** | ***Instalação e utilização do TOII- TOTVS Office Interface Integration*** |
| **Data da publicação** | **:** | 02/10/2013 |

**Introdução**

 Este manual tem por objetivo auxiliar no uso da Funcionalidade **TOII**. Como exemplo, vamos criar uma mala direta.

**1. O que é TOII (***TOTVS Office Interface Integration***)?**

O TOII é um produto originado da parceria entre a TOTVS e a Microsoft, que integra as funcionalidades do ERP da TOTVS com as ferramentas do Microsoft Office.

Com o TOII devidamente instalado poderemos visualizar informações do ERP dentro do Microsoft Office. A integração entre os sistemas também permite alteração nos dados cadastrais informados no ERP.

Tudo isso sendo realizado dentro do Microsoft Office.

A integração entre o TOII e o Microsoft Office também permite a criação de relatórios e planilhas.

**1.1. Como instalar**

*O TOII possuí um instalador próprio, e é liberado a cada release de versão. A cada migração de versão é necessário baixar a nova instalação do TOII, juntamente com os outros arquivos de instalação do ERP.*

*Ao instalar o TOII os arquivos de instalação serão gravados dentro da pasta RM.NET. Após instalar, basta abrir os aplicativos do pacote Office e usufruir da integração com o ERP da TOTVS.*

*Execute o instalador seguindo as imagens disponibilizadas.*

* *Ao executar o instalador* **Clique em Avançar;**
* Leia o contrato de Licença, e clique em "Aceito'' para **Avançar**

* + Cliquem em **Avançar**.

* + Clique em **Instalar** para prosseguir.

* + Clique em **Concluir** para finalizar.

**1.2. Usando as funcionalidades do TOII no Microsoft Word.**

*Após instalar o TOII, vamos executar o Microsoft Word. Para iniciar a integração clique no ícone destacado abaixo.*

* + *Clique em suprimentos e selecione conectar (Esta opção só é apresentada após a instalação do TOII)* - Abaixo segue os exemplos destacados em OFFICE 2007 e 2010
  + **OFFICE 2007**

    1) Acesse o Word /Excel.

    2) Abra o Menu > **Opções** do Word / Excel.

    3) Clique em: **Suplementos**.

    4) Clique em: **Ir**.

    *Marque a opção: TotvsWord2007 (Clique em **OK**).*
  + **OFFICE 2010**

**1.3.** Segue as informações respectivas as opções apresentadas na ferramenta:

**1.4. Clicando em Conectar**

*Ao clicar em **[Conectar]** a tela de Login do ERP da TOTVS será acionada dentro do Microsoft Word.*

*Após digitar, usuário, senha e selecionar o ALIAS será possível acessar as informações do ERP.*

*Após logar, devemos seguir a orientação do Sistema e clicar no Ribbon **[TOTVS 11]** para que o sistema habilite a opção para seleção de **[Contexto]**.*

*Na opção **[Contexto]**, devemos escolher qual sistema desejamos visualizar/manipular os dados. Se a necessidade for visualizar dados dos funcionários, devemos selecionar o sistema **[Folha de Pagamento]**. É importante notar que também podemos inserir Consultas SQL.*

*Ao clicar no ícone **[RM BIS]**, o sistema habilitará uma nova opção para selecionarmos qual o recurso que desejamos visualizar/manipular.*

*Seguindo o exemplo abaixo, vamos visualizar/manipular os dados referentes a Cubos.NET.*

**TOII em ambientes 3 camadas**

* + Caso seja apresentada a mensagem conforme a imagem abaixo ao acessar o TOII, significa que o ambiente esta configurado em três camadas.

* + Neste caso será necessário alterar os arquivo **(TotvsExcel2007.dll.config ) e (TotvsWord2007.dll.config)** localizados no diretório **C:\TOTVS\CorporeRM\RM.Net** incluindo a TAG abaixo:

**add key="JobServer3Camadas" value="true" />**

* + O arquivo ficará conforme a imagem.:

**Informações Adicionais**

*É importante salientar que por se tratar de uma integração entre o ERP da TOTVS com o Microsoft Office podemos usufruir de todos os recursos disponíveis, tais como, tabelas, bordas, sombreamento, dentre outras importantes. Vale lembrar que ainda podemos usar o Microsoft Excel para outros fins.*

****Este foi apenas um pequeno exemplo do ganho de funcionalidade que temos com a integração do ERP com o Office.****

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
