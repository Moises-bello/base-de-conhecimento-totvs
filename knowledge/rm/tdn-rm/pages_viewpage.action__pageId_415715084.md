---
content_hash: a4c5a1131ddf94790bc55ed4cd6c663a246b6f51e85e9a19d605ac60ff00801c
fetched_at: '2026-06-29T00:09:12.140635+00:00'
page_id: '415715084'
product: rm
source: tdn-rm
title: RMPES00004_Como Fazer - Personalização do Banco de Talentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415715084
version: 2
---

# Personalização do Banco de Talentos

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Rotina:** | |  | | --- | | **Rotina** | | Banco de Talentos |  |  | | --- | | **Rotina(s) envolvida(s)** | | Recrutamento e Seleção | |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Sistema(s) Operacional(is):** | Sistemas suportados pela solução RM Web |
| **Versões/Release:** | 12.1.9 |

## Descrição

O Banco de Talentos foi redesenhado visando adequar-se à experiência 8 e proporcionar melhorias em sua usabilidade e performance. Devido a esta reformulação, neste documento iremos demonstrar como realizar a personalização do Layout, para que cada empresa faça a adaptação para sua identidade visual.

## \*Procedimento para Personalização

O Banco de Talentos possui o layout baseado por padrão na logomarca TOTVS (utiliza as cores base azul e branca), conforme pode ser visualizado nas imagens , ,  e . Visando facilitar a adaptação, no diretório virtual de instalação do sistema () podemos localizar a pasta "custom" através do caminho "FrameHTML\RM\Rhu-BancoTalentos\framework\assets\custom" que possui as subpastas "img" e "css" que armazenarão respectivamente imagens e um arquivo .css para personalização. Na subpasta "css" existe o arquivo "**layout\_custom.css**" que contém instruções e comentários de como personalizar as páginas,  e já na pasta "img" é utilizada armazenar imagens utilizadas pelo arquivo de personalização que será criado.

Para fazer uma nova personalização deve-se criar um arquivo com o nome \*\*"**rm\_rhu\_layout\_personalizado.css**"(não deve ser utilizado outro nome) na pasta "css"e a logomarca da empresa em questão deve ser armazenada na pasta "img". Uma vez criado estes arquivos, o sistema detectará automaticamente  a existência de uma nova identidade visual e carregará automaticamente no sistema.

Como exemplo disponibilizamos no diretório "css" um tema personalizado com o nome "**rm\_rhu\_layout\_personalizado-sample.css**", caso queira visualizar este exemplo será necessário renomear o "**rm\_rhu\_layout\_personalizado.css**" para que o sistema habilite esse novo visual. Este tema de exemplo pode ser visualizado através das imagens , ,  e .

*\*P*ara realização deste procedimento é necessário que o mesmo seja feito por um profissional com conhecimento de desenvolvimento Web.

*\*\** Toda a personalização deve ser criada a partir das informações contidas no arquivo layout\_custom.css

## Anexos

**Figura 01 - Tela de Home**

**Figura 02 - Tela de Painel de Vagas**

**Figura 03 - Tela Perfil**

**Figura 04 - Edição de Dados Pessoais (Tela de Perfil)**

**Figura 05 - Servidor de Aplicação - Local de Instalação**

**Figura 04 - Tela de Home (personalizada)**

**Figura 05 - Tela de Perfil (personalizada)**

**Figura 06 - Tela de Painel de Vagas (personalizada)**

**Figura 07 -  Edição de Dados Pessoais - Tela de Perfil (personalizada)**
