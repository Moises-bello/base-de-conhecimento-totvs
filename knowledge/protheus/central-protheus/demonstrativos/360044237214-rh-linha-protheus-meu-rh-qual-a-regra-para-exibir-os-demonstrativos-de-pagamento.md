---
article_id: 360044237214
category: DEMONSTRATIVOS
content_hash: ed22690ca1d086ddea66b5ecc354016d0a5bd832594900085335e92530b63d9a
fetched_at: '2026-06-28T22:44:38.459443+00:00'
product: protheus
section_id: 10299629664279
source: central-protheus
title: RH - Linha Protheus - MEU RH - Qual a regra para exibir os Demonstrativos de
  Pagamento (recibos/holerites)
type: support-article
updated_at: '2026-03-30T18:54:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044237214-RH-Linha-Protheus-MEU-RH-Qual-a-regra-para-exibir-os-Demonstrativos-de-Pagamento-recibos-holerites
---

**Dúvida**  
Qual a regra para exibir os Demonstrativos de Pagamento (recibos/holerites)?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH – todas as versões  
  
**Solução**  
A validação que o sistema faz para apresentar os  Demonstrativos de Pagamento (recibos/holerites) no MEU RH depende do conteúdo de diversos parâmetros para que seja possível atender os diferentes cenários das empresas.

Entre eles, temos o **MV\_TCFDFOL** que define a partir de qual data a informação ficará disponível no MEU RH, por exemplo:  
  
Data Base **(*****Windows*****):**  
  
**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061540793)**   
  
**+(mais)**Data Pagamento Definido no cadastro de Períodos **(SIGAGPE):**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060604174)  
  
**+(mais)**Conteúdo do parâmetro **MV\_TCFDFOL** **(pode ser negativo):**  
**![](http://tdn.totvs.com/download/attachments/239026981/image2016-6-10%2013%3A50%3A31.png?version=1&modificationDate=1465573929000&api=v2)**  
  
No exemplo dos prints acima, eu não conseguiria ver o Demonstrativo de Novembro de 2019 que foi pago em **05/12/2019**, pois a data do Windows é **01/12/2019** e o parâmetro **MV\_TCFDFOL**está com conteúdo '**-2**' (sem aspas).  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360061023353)  
  
No mesmo exemplo dos prints acima, eu só conseguiria ver o Demonstrativo de Novembro de 2019 que foi pago em **05/12/2019**, a partir do dia **03/12/2019**.  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060605254)

**![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360060093994)**  
  
**Ou seja:**

* Se eu quero que o Demonstrativo fique disponível somente na data do pagamento, é necessário que eu configure o conteúdo do parâmetro **MV\_TCFDFOL** está com conteúdo '**0**' (sem aspas).
* Se eu quero que o Demonstrativo fique disponível somente um dia depois da data do pagamento, é necessário que eu configure o conteúdo do parâmetro **MV\_TCFDFOL** está com conteúdo '**1**' (sem aspas).
* Se eu quero que o Demonstrativo fique disponível cinco dias antes da data do pagamento, é necessário que eu configure o conteúdo do parâmetro **MV\_TCFDFOL** está com conteúdo '**-5**' (sem aspas).

Também é necessário que confira os parâmetro informados no artigo:  
[GPE054OUTROS\_Consulta\_recibo\_de\_pagamento\_do\_mês\_corrente](https://tdn.totvs.com/pages/viewpage.action?pageId=234617374)

1. MV\_TCFD131 -> Define o dia do mês a partir do qual a 1ª. parcela do 13º. salário está liberada para consulta no RH online;
2. MV\_TCFD132 -> Define o dia do mês a partir do qual a 2ª. parcela do 13º. salário está liberada para consulta no RH online;
3. MV\_TCFDADT -> Define o dia do mês a partir do qual o adiantamento está liberado para consulta no RH On-line;
4. MV\_TCFDEXT -> Define o dia do mês a partir do qual os valores extras e PLR estão liberados para consulta no RH Online;

Com relação aos tipos de demonstrativo (MV\_TCF013A) acesse o artigo: [RHO0006\_Tipos\_de\_demonstrativos\_para\_consulta\_do\_RH\_On-line](https://tdn.totvs.com/display/public/PROT/RHO0006_Tipos_de_demonstrativos_para_consulta_do_RH_On-line)

1. MV\_TCF013A -> (exemplo de conteúdo: 01.02.03.04.05.06.07) -> Opções de consulta do demonstrativo de pagamento:  
   **01** - Adiantamento  
   **02** - Folha  
   **03** - 1ª parcela do 13º  
   **04** - 2ª parcela do 13º   
   **05** - PLR  
   **06** - Autônomos  
   **07** - Valores Extras

**Lembrando que,** se um roteiro for criado no GPE, entrará como uma customização, com isso, o App Meu RH, não irá demonstrar esse roteiro criado pelo usuário no SIGAGPE.  
  
**Exemplo:**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/18944735114135)**  
  
Neste exemplo acima, **o roteiro COM foi criado e tem Origem 2 - Usuário**, com isso, o App Meu RH, não irá demonstrar o recibo deste roteiro, mesmo que pelo SIGAGPE, tenha feito o cálculo corretamente e sem erros.  
  
[**Para exibição de recibos de 13o primeira e segunda parcela**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/18256712088727-RH-Linha-Protheus-Meu-RH-%C3%89-poss%C3%ADvel-determinar-uma-data-para-libera%C3%A7%C3%A3o-do-holerite-da-2%C2%AA-parcela-do-13%C2%BA-sal%C3%A1rio-pelo-App-Meu-RH-MV-TCFD132-e-MV-TCFD131)  
  
**Importante:**  
Existem casos em que o Arquivo PDF não consegue ser gerado com os devidos valores ou é apresentado em branco. Isso ocorre devido à falta da funcionalidade printer ou pdfprinter no serviço (appserver) do Meu RH e do REST. Deste modo, realize os ajustes em seu serviço conforme o documentado abaixo:  
[RH - Linha Protheus - MEU RH - Onde localizo o arquivo PRINTER](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050119614-RH-Linha-Protheus-MEU-RH-Onde-localizo-o-arquivo-PRINTER?source=search)  
  
Com relação ao Recibo de Férias, siga as informações relacionadas no artigo abaixo:  
[MP - MEU RH - Como fazer o download/imprimir o Aviso e o Recibo de Férias no MEU RH?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360055224754)  
  
**Saiba Mais**  
[**CLIQUE AQUI**para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
