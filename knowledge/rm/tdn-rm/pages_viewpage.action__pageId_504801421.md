---
content_hash: 268738f1e2b1e59afa19f254693980b5cc761e4ade73c97ff59cbcd972f55b6a
fetched_at: '2026-06-29T00:10:25.386011+00:00'
page_id: '504801421'
product: rm
source: tdn-rm
title: Lançamentos Ativo Imobilizado - CIAP
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=504801421
version: 7
---

Utilize este cadastro para inserir no processo do CIAP os Bens de Ativo Imobilizado manualmente. Deve ser utilizado somente se controle do CIAP for  feito em sistemas legados ou se não for possível fazer a entrada do bem pelo meios convencionais: Lançamento Fiscal ou Movimento de Compra de Ativo.

Os bens incluídos por este Cadastro Manual passarão a compor o cálculo/controle do CIAP e serão considerados na geração de Rotinas Fiscais e todos os processos que utilizem esta informação.

Para facilitar a inserção de registros  em grande quantidade o usuário poderá optar por fazê-la [via WebService](http://tdn.totvs.com/display/public/LRM/WebService+RM).

**Regras de validação do cadastro**

* Só é possível a inclusão de registros que possua a data Entrada/Saída maior que 01/08/2000;
* Só poderão ser incluídos registros para o Exercício e Filial corrente;
* O cálculo do CIAP considerará a soma dos valores de ICMS, Diferencial de Alíquota e Frete informados na aba Item do registro;
* O Patrimônio informado no Lançamento deve ser do tipo Patrimônio ou Terceiros;
* Não serão permitidas alterações em Lançamentos de Ativo que estejam associados a Lançamentos Fiscais de Saída de Ativo;
