---
content_hash: a2c02c9a5267c600be9209cee9c65e9de2b7ed387970640fcaa2fe477f36b05b
fetched_at: '2026-06-29T00:09:26.724701+00:00'
page_id: '423938388'
product: rm
source: tdn-rm
title: Sub-Modelos
type: documentation
url: https://tdn.totvs.com/display/LRM/Sub-Modelos
version: 5
---

Esta janela permite cadastrar sub-modelos dos objetos de manutenção. Visualizamos todos os sub-modelos pertencentes a um determinado modelo de objeto de manutenção do sistema. Os seguintes campos deverão ser preenchidos:   
Descrição do Sub-Modelo: Inserir o nome do sub-modelo do objeto de manutenção do sistema.  
**Preço**: Inserir o preço do Sub-Modelo.  
**Produto**: Selecione um produto que poderá ser gerado um objeto de manutenção, para a coligada em questão.   
Este produto terá o tipo de objeto, modelo e sub-modelo da associação correspondente, como suas características. Para isso, é preciso que o seja gerado um  
***Observação***: Um produto será associado somente a um sub-modelo, ou seja, se tentarmos associar P-3000 a outro sub-modelo dará duplicidade na associação.

Após associar produto ao sub-modelo (Tipo de Objeto, Modelo e sub-modelo), se houver objeto de manutenção como Modelo P-3000, Sub-Modelo Único, não será permitido mudar esta associação ou até mesmo deletá-la.  
Para gerar Objetos de Manutenção a partir de produtos, deverá ser acessar o menu Operações | Geração de Objetos de Manutenção | Produto(s).

***Dica***: Caso você precise cadastrar mais informações sobre os sub-modelos, basta habilitar os campos livres que conterão tais dados. Estes campos são habilitados em Opções | Parâmetros | Sistema | Pasta Campos e Tabelas Opcionais | Subpasta Sub-Modelos. Após a configuração dos campos livres nas opções de parâmetros do sistema, será exibida na parte inferior da janela de Sub-Modelos, caixa Campos Livres, contendo os campos especificados nos parâmetros.
