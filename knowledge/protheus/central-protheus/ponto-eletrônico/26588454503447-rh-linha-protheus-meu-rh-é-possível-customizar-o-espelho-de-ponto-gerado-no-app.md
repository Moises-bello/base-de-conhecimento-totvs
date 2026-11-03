---
article_id: 26588454503447
category: PONTO ELETRÔNICO
content_hash: f9ee820262cef958e31c1daad962fdb673a2891d4c593e07d5568bf94a053c0a
fetched_at: '2026-06-28T22:44:36.475825+00:00'
product: protheus
section_id: 10299685322391
source: central-protheus
title: RH - Linha Protheus - Meu RH - É possível customizar o Espelho de Ponto gerado
  no App
type: support-article
updated_at: '2026-06-23T21:05:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26588454503447-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-customizar-o-Espelho-de-Ponto-gerado-no-App
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26588422139031) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**É possível customizar o Espelho de Ponto gerado no App?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**Quando o funcionário, via App Meu RH, gera o Espelho de Ponto das marcações, **o relatório padrão do Ponto Eletrônico**, será referenciado no momento da impressão.  
  
Porém, **é possível customizar esta geração, compilando o *RDMake* *IMPESP.PRX*, no RPO - Repositório do serviço do Meu RH**, com as devidas customizações e, assim será possível a impressão do Espelho de Ponto via App Meu RH, com as padronizações.  
  
Para coletar o *RDMake* do Espelho de Ponto, acesse o *link* abaixo, onde temos o **pacote de Expedição Contínua do GPE**, nele haverá uma pasta com o mesmo nome e, nela poderá ser baixado o arquivo *IMPESP*.  <https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/RH_EXPEDICAO>  
  
Pasta *RDMakes*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588422140311)  
  
Em tese, se no RPO do serviço do Meu RH/REST, **o *RDMake IMPESP.PRX e o INCLUDE impesp\_pt-br.tres* deverão ser  compilados**, ao gerar o Espelho de Ponto pelo App Meu RH, **a impressão também será padrão**, pois o *RDMake* é uma cópia do fonte PONR010 do módulo SIGAPON.  
  
Exemplo de impressão padrão com o *RDMake* compilado:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588422141079)  
  
Geração:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588422141719)  
  
Para complementar o artigo, realizando um teste simples de alteração em duas *Strings* das duas últimas colunas do Espelho de Ponto, sendo elas **Ad.Not. e Observação.**  
  
Padrão, o *IMPESP* apresenta este cenário das *Strings*:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588454472599)  
  
**Ao alterar a posição das chamadas das *Strings***, e gerar o Espelho de Ponto novamente, verifica-se que os nomes das colunas irão alterar.  
  
Exemplo:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588422148119)  
  
Após reiniciar o serviço, logar no Meu RH novamente e, gerar o Espelho de Ponto, **este foi o resultado:**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26588454473879)  
  
**O exposto acima é somente** **um exemplo, pois todas as customizações devem ser avaliadas pelo próprio cliente, ou se desejar, temos o serviço do HUB.**

Para assuntos sobre **customizações TOTVS**, o time de Suporte consistirá em fornecer as documentações que possibilitem a utilização de **pontos de entrada e rotinas automáticas** documentadas no portal TDN para uso no produto padrão.  
  
**Importante:**  
Os *Includes* **IMPESP****.CH e IMPESP.TRES**, são necessário sua compilação juntamente ao **IMPESP.PRW.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28324185553175)**  
  
Cabe ressaltar que este *RDMake*, é responsável se desejarem realizar uma customização na geração e impressão do **Espelho de Ponto no App Meu RH.**  
  
Os arquivos podem ser baixados através do *link* abaixo específico para download dos **RDMAKES:***Link* direto da Central de *Downloads*: [RDMAKES RH](https://suporte.totvs.com/portal/p/10098/download?e=1083731)  
  
Segue demonstração de como localizar os arquivos de *RDMAKE* na [Central de *Downloads* da TOTVS](https://suporte.totvs.com/portal/p/10098/download#company/).  
Na busca procurar: **RDMAKES\_RECURSOS\_HUMANOS**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28324157301015)  
  
Outra opção: Estes arquivos podem ser encontrados também ao baixar o **Pacote RH Expedição Contínua, no *link* a seguir** [Pacote Acumulado RH](https://suporte.totvs.com/portal/p/10098/download#000006/all/all/search/RH_EXPEDICAO_CONTINUA)  
  
Também poderá acessar a Central e realizar a seguinte busca:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/28324157302551)  
  
Segue documentação padrão sobre o Espelho de Ponto:  
<https://tdn.totvs.com/display/PROT/Ponto+de+Entrada+-+IMPESP+-+Espelho+do+Ponto>  
  
**Saiba Mais:**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
