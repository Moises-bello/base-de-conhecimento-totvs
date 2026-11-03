---
content_hash: aa1a137722649babb76c4f03e43a082771bb947aa07b6bc446a39f8b2d2fcf82
fetched_at: '2026-06-29T00:10:53.303540+00:00'
page_id: '578367433'
product: rm
source: tdn-rm
title: TOTVS Construção Gestão de Imóveis - DAI (Declaração de Atividades Imobiliárias)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=578367433
version: 19
---

A partir da versão 12.1.31

A DAI é o instrumento pelo qual são informados à administração tributária dados relativos a atividades de venda e locação de unidades imobiliárias localizadas no Município de São Paulo, bem como a intermediação dessas atividades. [Site DAI](https://web1.sf.prefeitura.sp.gov.br/DAI)  
  
São responsáveis pela declaração:  
- construtoras ou incorporadoras que comercializarem unidades imobiliárias por conta própria;  
- imobiliárias e administradoras de imóveis que realizarem intermediação de compra e venda e aluguéis de imóveis;  
- leiloeiros oficiais no caso de arrematação de imóveis em hasta pública.  
- agentes, corretores ou intermediários de bens imóveis (a partir da incidência de Agosto / 2017).

### Configurar o TCGI para gerar a DAI

* [Parametrizador TCGI](https://tdn.totvs.com/pages/releaseview.action?pageId=574896220);
* Empreendimento/Subunidade => EFD-Pis/Cofins/DAI e Imóvel Aluguel
  + **Tipo de Imóvel DAI**  
    Neste campo será selecionado o tipo de imóvel referente a subunidade. [Manual DAI](https://web1.sf.prefeitura.sp.gov.br/DAI/Documentos/Manual_DAI.pdf);
* Importar o layout '**TCGILAY0001 - DAI (Declaração de Atividades Imobiliárias).TotvsGen**'  no Gerador de Saída,  menu Gestão do TCGI.

  Informações

  **O Layout poderá ser baixado e atualizado atravéz dos objetos gerenciais (nos patchs superiores a 12.1.34.202 e 12.1.2205.142**

Detalhes dos Campos do [Arquivo DAI](https://tdn.totvs.com/display/LRM/Detalhes+dos+Campos+do+Arquivo+DAI)

### Gerar a DAI

Selecionar o Layout da DAI e clicar em processo => Geração de Saídas

Definir o diretório para gerar o arquivo

Informar a coligada do declarante, código da coligada das transações imobiliárias, ano DAI e mês para geração da DAI.  
***Importante lembrar que estes campos somente serão apresentados ao realizar a importação do novo Layout.***

### Requisitos

* O Código da Coligada informado nos parâmetros da Geração de Saídas, corresponde ao "Declarante" da DAI
* Somente registros cadastrados a partir do ano de 2017;
* Somente Vendas e Locações registradas no mês/ano dos parâmetros da geração da DAI;
* Somente empreendimentos e imóveis com código de município de SP parametrizado serão gerados.
