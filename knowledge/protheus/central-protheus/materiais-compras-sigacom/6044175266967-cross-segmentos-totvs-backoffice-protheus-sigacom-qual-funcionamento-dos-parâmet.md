---
article_id: 6044175266967
category: Materiais - Compras (SIGACOM)
content_hash: 28dbb153a33881d79566bc65d2322cb7f66a2f5bd47c2ceb0057f66c48824485
fetched_at: '2026-06-28T22:41:24.287494+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Qual Funcionamento
  dos  parâmetros MV_PORTAL1  / MV_PORTAL2 / MV_PORTAL3 e MV_PORTAL4 no Portal do
  Fornecedor ?
type: support-article
updated_at: '2022-05-16T21:05:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6044175266967-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Qual-Funcionamento-dos-par%C3%A2metros-MV-PORTAL1-MV-PORTAL2-MV-PORTAL3-e-MV-PORTAL4-no-Portal-do-Fornecedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**  
Qual Funcionamento dos parâmetros MV\_PORTAL1 / MV\_PORTAL2 / MV\_PORTAL3 e MV\_PORTAL4 no Portal do Fornecedor ?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus)   Compras – A partir da versão 12  
  
**Solução**

* **MV\_PORTAL1  -**Informe a localização, a partir do RootPath do Protheus, onde encontra-se o arquivo com o texto do institucional da Empresa para os portais (mensagem da tela inicial).
  + Permite que seja especificado o caminho (path) do arquivo txt que contém o fonte html que apresenta um texto institucional (ou outro, se desejado) a ser exibido na Pagina principal do Portal Protheus.
  + O texto a ser exibido pode ser livremente editado, utilizando-se de todos os recursos disponíveis em html, como formatação do texto, cor, indentação, entre outros. O arquivo deve obrigatoriamente ser armazenado dentro da Raiz RootPath do Microsiga Protheus Server.
  + Recomenda-se que o mesmo seja mantido dentro do diretório web do Portal Protheus, por questões de organização, embora esta seja uma pratica facultativa. Exemplo:\web\portal\_protheus\institucional.txt  
    Utilizar um caminho/diretório errado neste parâmetro, assim como nos demais parâmetros MV\_PORTAL (2,3 e 4) , pode travar o acesso as rotinas por meio do menu e trazer falha de comunicação com a base de dados.
* **MV\_PORTAL2  -**Informe a localização, a partir do RootPath do Protheus, do arquivo com o logo da Empresa para apresentação nos portais do sistema (logotipo da tela inicial).
* **MV\_PORTAL3  -**Informe a localização do arquivo, a partir do Root Path do Protheus, onde encontra-se as noticias diárias dos portais do sistema (mensagem da tela inicial).
* **MV\_PORTAL4  -** Informe a localização do arquivo com o logo da empresa, a partir do RootPath. O Logo será apresentado nos portais do sistema (logotipo da tela inicial).

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigo Materiais - COMPRAS ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
