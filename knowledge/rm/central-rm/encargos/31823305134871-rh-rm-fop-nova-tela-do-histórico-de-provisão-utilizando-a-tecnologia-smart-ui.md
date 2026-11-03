---
article_id: 31823305134871
category: Encargos
content_hash: 582fc3ef0704fbc311ff2b8308ee8dd72435afb4b9b695ff9858dcc062db71ec
fetched_at: '2026-06-28T22:46:52.221763+00:00'
product: rm
section_id: 1500000834581
source: central-rm
title: RH - RM - FOP - Nova tela do Histórico de Provisão, utilizando a tecnologia
  Smart UI
type: support-article
updated_at: '2025-08-11T14:12:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31823305134871-RH-RM-FOP-Nova-tela-do-Hist%C3%B3rico-de-Provis%C3%A3o-utilizando-a-tecnologia-Smart-UI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31823305101847)**Tempo aproximado para leitura:**00:03:00 min**

**Dúvida**Quais informações importantes para uso da nova tela do **Histórico de Provisão**, utilizando a tecnologia **Smart UI**?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - A partir da versão 12.1.2502

**Solução**Disponibilizamos a tela do **Histórico de Provisão**, utilizando o Smart UI para as versões 12.1.2502 e superiores. Essa implementação alterou visualmente o que já existia trazendo uma visão atualizada da pagina e também a maneira com que a utilizamos.   
  
A tela que já existia em versões inferiores a 12.1.2502 utilizava o padrão que já conhecemos na nossa MDI:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_15-54-50.png?version=1&modificationDate=1730409401483&api=v2)   
  
Agora, com a utilização da nova tecnologia o seu visual ficou assim:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_15-54-33.png?version=1&modificationDate=1730409401540&api=v2)  
  
Agora temos a opção de buscar registros que estão na tela sem necessariamente a criação de um filtro, como por exemplo, abaixo temos alguns registros sendo exibidos e caso queira retornar apenas o funcionário de chapa **00009**,  basta que preencha o campo **Buscar na tabela** :  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_16-1-53.png?version=1&modificationDate=1730409401357&api=v2)  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_16-4-13.png?version=1&modificationDate=1730409401290&api=v2&effects=drop-shadow)  
  
![(informação)](https://tdn.totvs.com/s/-dgf44d/8804/xgjkrn/_/images/icons/emoticons/information.svg)  Vale lembrar que essa funcionalidade realiza a busca em qualquer campo exibido na tela, **somente os registros exibidos**, por padrão a tabela exibe 10 registros por busca, mas esse valor pode ser alterado, exibindo 20 / 50 / 100 / 1000 registros .   
  
Outra função que recebeu alterações visuais e funcionais é o gerenciamento e aplicações de **Filtros,**anteriormente ao clicar em Filtro era aberto uma janela pop-up para que pudessemos criar ou utilizar filtros já criados.  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_16-18-59.png?version=1&modificationDate=1730409401217&api=v2)  
  
Agora ao clicarmos em **Filtro**, será aberta lateralmente uma janela para que possamos gerenciar nossos filtros, onde temos filtros padrões como **Ano**/ **Mês**e **Funcionário** e também há a possibilidade de criarmos filtros personalizados, clicando em **Ir para filtros avançados**e Clicando em **+****Criar Filtro**:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-10-31_16-23-56.png?version=1&modificationDate=1730409401150&api=v2&effects=drop-shadow)  
Para realizar a inclusão das clausulas do filtro, basta clicar em **+ Regra ,**selecionar o **Campo / Operador e Digitar seu filtro** como no exemplo abaixo:  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_5-11-7.png?version=1&modificationDate=1730707868110&api=v2&effects=drop-shadow)  
Para concluir a criação do Filtro, basta clicar então em **Salvar e Filtrar**  
  
Para realizar uma inclusão manual do Histórico de provisão, basta clicarmos em **+ Incluir** na pagina inicial, será então aberta uma pagina para a inclusão dos dados:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-15-13.png?version=1&modificationDate=1730736913497&api=v2&effects=drop-shadow)  
 Após o preenchimento dos dados, basta clicar em Salvar para a inclusão efetiva do registro  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-16-5.png?version=1&modificationDate=1730736965487&api=v2&effects=drop-shadow)  
Caso queira Excluir o registro, é necessário selecionar a linha desejada e clicar em **Excluir**, após a confirmação o registro será excluído:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-20-30.png?version=1&modificationDate=1730737230947&api=v2)  
  
Se necessário editar também um registro é possível selecionando o registro, e clicando em **Editar:  
  
![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-21-21.png?version=1&modificationDate=1730737281843&api=v2)**  
  
Após editar o campo desejado, basta clicar em salvar para que a edição seja concluida  
  
**![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-22-25.png?version=1&modificationDate=1730737345797&api=v2)**Na tela inicial do histórico de provisão é possível também ajustar as colunas do Grid, fixando-as ou então alterando sua posição de exibição ou então a sua não exibição. Também é permitido alterar a quantidade de registros que serão exibidos. Tudo isso pode ser feito através da função**Gerenciar Tabela:**

**![](https://tdn.totvs.com/download/attachments/882635481/image-2024-11-4_13-23-55.png?version=1&modificationDate=1730737435437&api=v2)**

**SAIBA MAIS**

Para mais informações, acesse:

* [Geração Histórico de Provisões (.Net)](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719548)
