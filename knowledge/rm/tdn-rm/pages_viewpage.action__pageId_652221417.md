---
content_hash: c4f6b1d3f8f30f39cbe63f2d8768b1e1d4b1713bb24a8e29a3218982ded40d93
fetched_at: '2026-06-29T00:11:12.339934+00:00'
page_id: '652221417'
product: rm
source: tdn-rm
title: Cópia de Localidades entre Coligadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652221417
version: 2
---

A cópia de Localidades é uma entidade disponível na cópia de dados entre coligadas no módulo Serviços Globais.

Regras para cópia:

- Serão copiadas apenas as Localidades que estão ATIVAS;

- O Centro de Custo somente será copiado se o parâmetro "*Vincular Localização com Centro de Custo*" estiver marcado na Coligada de Destino;

- O Responsável somente será copiado se o parâmetro "*Vincular Localização com Responsável*" estiver marcado na Coligada de Destino.

- Para a cópia da informação do Responsável é verificado também o parâmetro "Usar funcionários RM Labore como responsável", que deve estar igual entre a Coligada de Origem e de Destino;

- Os Defaults Contábeis da Localidade também serão copiados, porém, somente se a Conta Contábil existir na Coligada de Destino. Com relação aos demais campos do Default Contábil, caso as entidades não existam no destino a informação será gravada em branco;

- Os Rateios do Default Contábil serão copiados somente se as Contas Gerenciais existirem na Coligada de Destino; 

Durante a cópia caso ocorra algum erro ou aviso, será detalhado no log do processo.
