---
article_id: 14526251757975
category: DASHBOARD
content_hash: e5cb306be80646e750e8e79aa17dc31023de4b588183fffd97f69639a7ee9485
fetched_at: '2026-06-28T22:44:41.365875+00:00'
product: protheus
section_id: 10299521604759
source: central-protheus
title: RH - Linha Protheus - MEU RH - Requisitos para exibição da foto do funcionário
type: support-article
updated_at: '2026-06-19T17:09:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14526251757975-RH-Linha-Protheus-MEU-RH-Requisitos-para-exibi%C3%A7%C3%A3o-da-foto-do-funcion%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18603112313239) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Não é exibido a foto do colaborador no aplicativo MEU RH  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – Todas as versões   
  
**Solução**A foto do funcionário exibida no Meu RH, é obtida **a partir do campo "Foto" (RA\_BITMAP)** da tabela Funcionários (SRA), do módulo **Gestão de Pessoal (SIGAGPE)**.  
  
As imagens que são atribuídas aos funcionários ficam armazenadas no **Repositório de Imagens do Protheus**.  
  
**Restrição de uma imagem Padrão:**Quando o funcionário possuir uma imagem em que o arquivo ultrapasse o tamanho de **204800 *Bytes***, o sistema exibirá uma imagem padrão no lugar da foto do funcionário, para indicar que existe um problema na imagem. Vide exemplo abaixo.  
  
Sempre que uma imagem padrão for carregada o sistema apresentará no LOG do console uma mensagem informativa, indicando a matrícula que apresenta problemas na imagem: **"A matricula (Filial/Matricula) não possui imagem, ou ela ultrapassa o limite (204800 Bytes). Será utilizada uma imagem padrão".**  
  
**Manipulação do tamanho limite da imagem:**É possível manipular o tamanho limite de 204800 Bytes que é verificado no Meu RH. Para isso foi disponibilizado o **Ponto de Entrada** **"MRHLOADIMG"**, e por meio deste será possível ampliar ou reduzir o tamanho do arquivo que será verificado para exibição no Meu RH.  
  
Porém, ressaltamos que é preciso muito cuidado, ao estabelecer limites superiores ao valor padrão de 204800 *Bytes*, pois, quando um líder acessa a opção Minha Equipe, o sistema realiza o carregamento das fotos de seus subordinados. Dessa forma, caso existam muitas imagens de alta resolução, o carregamento dos arquivos poderá acarretar em **lentidão**, ou até mesmo **travamento** do sistema.  
  
Maiores informações sobre esse Ponto de Entrada poderão ser obtidas no *link*:  
[**MRHLOADIMG**](https://tdn.totvs.com/display/NPR/9290003+RHMOBILE01-9030+DT+Carregamento+de+Fotos)  
  
**EXEMPLO DE UTILIZAÇÃO**Mensagem exibida no cadastro de funcionários quando o registro possuir uma imagem que ultrapasse o limite de 204800 *Bytes*.  
  
"O tamanho da imagem do funcionário supera 204800 *Bytes*. Isso afeta o desempenho de rotinas executadas via *Job/WebServices*":  
  
![](https://tdn.totvs.com/download/attachments/563431071/validacao_sra.JPG?version=1&modificationDate=1600891389447&api=v2)  
  
Caso o ponto de entrada mencionado no item 01 esteja compilado, o cadastro de funcionários validará o tamanho da imagem conforme definido no PE. No exemplo abaixo, foi definido um tamanho de imagem diferente de 204800 *bytes*.  
  
![](https://tdn.totvs.com/download/attachments/563431071/image2020-11-6_15-39-32.png?version=1&modificationDate=1604691572267&api=v2)  
  
**TELA IMAGEM PADRÃO**Imagem padrão exibida no perfil quando o arquivo da imagem ultrapassar o limite de 204800 *Bytes*.  
  
![](https://tdn.totvs.com/download/thumbnails/563431071/image2020-10-2_17-0-12.png?version=1&modificationDate=1601668812477&api=v2)  
  
Imagem padrão do perfil caso não possua nenhuma foto cadastrada.  
  
![](https://tdn.totvs.com/download/thumbnails/563431071/image2020-10-2_17-1-55.png?version=1&modificationDate=1601668915163&api=v2)  
  
 **TELA PRINCIPAL E OUTRAS ROTINAS**A imagem padrão poderá ser exibida nas seguintes rotinas: Dashboard, Perfil do Colaborador, Gestão do Time, Aniversariantes, entre outras.  
  
![](https://tdn.totvs.com/download/attachments/563431071/image2020-10-2_17-3-24.png?version=1&modificationDate=1601669004543&api=v2)  
  
**Saiba Mais  
[CLIQUE AQUI para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[CLIQUE AQUI para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)**
