---
content_hash: ccb9b2729a8710f47fc8d5a9896517316695a21ef663b01d95aab870a7204679
fetched_at: '2026-06-29T00:09:32.407279+00:00'
page_id: '425458842'
product: rm
source: tdn-rm
title: Consultar Projetos de Pesquisa, Projetos de Extensão e Grupos de Pesquisa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458842
version: 3
---

---

O objetivo desta funcionalidade é disponibilizar consultas públicas para os projetos de pesquisa, projetos de extensão e grupos de pesquisa.   
    
 As pesquisas públicas estão em uma pasta denominada"Public" que fica localizada dentro da estrutura do copore.net, na subpasta da pasta "..\Source\Edu-Educacional".   
 Como para acessar as pesquisas públicas não é necessário a autenticação do usuário, o sistema permite que o cliente parametrize um usuário e senha no arquivo do web.config que fica localizado na pasta "Public" que possibilita a chamada ao serviço de pesquisa.  
 Passos para utilização:  
    
 Abrir o Web.config localizado em "<Instalação do CorporeNet>\Source\Edu-Educacional\Public\PesquisaExtensao"  e define as seguintes tags:

* Define a segurança para o acesso as paginas da pasta "PesquisaExtensão"

           <authorization>  
            <allow users="\*"/>     
             </authorization>  
 Onde "\*" libera permissão para todas as páginas localizadas dentro da pasta "Public\PesquisaExtensão "     
 Essas consultas são realizadas para todas as coligadas e filiais, caso queira filtrar é necessário alterar a URL no seguinte formato <Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoPesquisa.html?CODCOLIGADA=<Código da coligada>&CODFILIAL=<Código da filial>

**Obs.** Somente projetos de pesquisa e extensão que estão com a situação "execução" ou "encerrado", são visualizados no resultado da consulta.  
 É possível alterar o web.config para definir quais colunas ficaram visíveis no resultado da pesquisa, Assim por exemplo, basta alterar o campo sumula para false, que o mesmo não aparece na exibição do projeto.

* Pesquisa pública a projetos de pesquisa

          Acesse: <Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoPesquisa.html  
           O Usuário pode utilizar filtros para realizar a pesquisa, tais como: área de conhecimento, código do projeto, nome do coordenador, etc...   
           O relatório EDUREL0079 - PPE- Grupo de Pesquisa está disponível no book de relatórios.

* Pesquisa pública a projetos de extensão

          Acesse <Instalação do CorporeNet>\Source\Edu-Educacional\Public\EduProjetoExtensao.html  
           Os filtros disponíveis para realizar a pesquisa são: Área de conhecimento e subárea, linha de extensão , código e titulo do projeto, nome do participante, nome do coordenador, entre outros.  
           O relatório EDUREL0080 - PPE- Grupo de Pesquisa está disponível no book de relatórios.

* Pesquisa pública aos grupos de pesquisa

          Acesse <Instalação do CoporeNet>\Source\Edu-Educacional\Public\EduGrupoPesquisa.html  
           Os filtros permitidos para realizar a consulta são: Líder do grupo, área de conhecimento e subárea de conhecimento.  
           A consulta não possui nenhum filtro fixo.  
           O relatório EDUREL0078 - PPE- Grupo de Pesquisa está disponível no book de relatórios.

O sistema também disponibiliza um relatório a partir das linhas do resultado da pesquisa, caso queira utilizar o seu próprio relatório é necessário parametrizá-lo no arquivo web.config.  
 A exibição do botão para imprimir o relatório também é configurado no arquivo web.config.

 Veja Também

---

[Documento Técnico - Consultar (projetos de pesquisa, extensão e grupos de pesquisa)](http://tdn.totvs.com/display/LRM/DT_Consulta_Publica)
