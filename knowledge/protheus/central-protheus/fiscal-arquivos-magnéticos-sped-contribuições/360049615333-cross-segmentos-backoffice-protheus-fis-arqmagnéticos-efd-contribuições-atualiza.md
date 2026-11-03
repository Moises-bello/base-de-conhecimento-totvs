---
article_id: 360049615333
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: d4243e9f240c12af2de38c292bde00a822dea0c1cc8d3013e1c5c8a030513097
fetched_at: '2026-06-28T22:42:05.060309+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Atualização do Ambiente e Módulo 09 (Livros Fiscais)
type: support-article
updated_at: '2026-06-16T20:38:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049615333-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Atualiza%C3%A7%C3%A3o-do-Ambiente-e-M%C3%B3dulo-09-Livros-Fiscais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41273966211735) Tempo aproximado para leitura: **00:08:00 min**  
  
**Ocorrência**  
**Ambiente** e **Módulo 09** (Livros Fiscais) desatualizado.  
  
**Ambiente**  
Cross Segmento - TOTVS *Backoffice* (Linha Protheus) - Livros Fiscais - A partir da versão 2310  
  
**Solução**  
Para solucionar essa ocorrência e evitar possíveis problemas ou inconsistências no Módulo, realize os seguintes passos:  
  
**1.** É possível baixar os pacotes de atualização através do próprio sistema ao acessar a **Central de Diagnósticos**. Para isso, **acesse qualquer rotina do Protheus** e clique nas teclas **Shift+F6** no teclado.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273966213015)  
  
**1.1** Ao acessar a Central, clique no símbolo com o **Globo** a esquerda.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273928693911)  
  
**1.2** Será possível visualizar todos os pacotes necessários para atualizar o ambiente. Para realizar o *download* dos que estiverem com o *Status* "**Desatualizado**", clique no símbolo com o **Seta para Baixo** na coluna **Ação.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273966214295)  
  
**Observação:** Para que o **Dicionário** seja atualizado, é necessário que após a aplicação do Acumulado (*Backoffice*), seja executado o **UPDDISTR.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273928695959)  
  
**2.** Após a aplicação do pacote *Backoffice* e de atualizar o Dicionário de Dados, é necessário atualizar as Procedures acessando o Configurador, seguindo o caminho **SIGACFG > Base de Dados > Dicionário >** ***Stored Procedure.***  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273928696343)  
  
**2.1** Ao acessar as procedures, para garantir a atualização, sugerimos que selecione a **Empresa**, selecione todos os **Processos/*****Procedures*** no símbolo com o **Certo Ticado** e clique no símbolo com a **Caixa e a Seta Vermelha Girando** para **DESINSTALAR** todos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273966217239)  
  
**2.1.1** Em seguida, **confira** se todos os **Processos/Procedures** continuam selecionados e clique no símbolo com a **Caixa e a Seta Verde** para **INSTALAR** todos novamente.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/41273928697623)  
  
**Mais Informações:**  
- [**Stored Procedures - Novo gerenciador de pacotes**](https://tdn.totvs.com/display/public/PROT/Stored+Procedures+-+Novo+gerenciador+de+pacotes)  
  
**3.** Caso esteja com dificuldades para acessar a **Central de Diagnósticos**, seguem abaixo os *links* via portal da **TOTVS.**  
  
**3.1** **LIB, Binários (*****Dbaccess*****,** ***Appserver*****,** ***Webapp*****)** e **Dicionário:**  
- [**SUP.PROTHEUS - Atualizações do Sistema Protheus**](https://tdn.totvs.com/pages/releaseview.action?pageId=550332596)  
  
**3.2** Acumulado ***Backoffice:***  
- [**Expedição Continua - Backoffice Protheus**](https://tdn.totvs.com/pages/releaseview.action?pageId=587835160)  
  
**4.** **Importante:** recomendamos validar o *link* abaixo para verificar a relação de bancos de dados homologados pela TOTVS:  
- [**Bancos de dados homologados**](https://tdn.totvs.com/pages/viewpage.action?pageId=6064703)
